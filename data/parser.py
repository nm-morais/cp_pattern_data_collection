#!/usr/bin/python3
import matplotlib.pyplot as plt
import csv
import sys


def main():
	line_counter = 0
	nr_patterns = 0;
	nr_tests_src_size = int(sys.argv[1])
	nr_tests_worker_size = int(sys.argv[2])


	changed = False
	old_nWorkers = 1
	nWorkers = 1


	patterns = {}

	with open("log", 'r+') as f:
		for line in f:
			if "NEW_TEST" in line:
				split = line.split(" ")
				src_size = int(split[1])
				old_nWorkers = nWorkers
				nWorkers = int(split[2])
				if(line_counter != 0):
					changed = True

			else:
				line_counter = line_counter + 1
				if(not changed):
					nr_patterns += 1

				#fetch sequential runtime and function name
				split = line.split("	")
				functionName =  split[0][4:-4]
				#print(functionName)
				par_runtime = int(split[1])
				#print("sequential runtime: " + str(runtime_seq))

				#fetch paralel runtime
				line = next(f)
				split = line.split("	")
				seq_runtime = int(split[1])
				#print("paralel runtime: " + str(runtime_par))

				#fetch speedup
				line = next(f)
				split = line.split("	")
				speedup = float(split[1])
				#print("speedup: " + str(speedup))
				
				#fetch efficiency
				line = next(f)
				split = line.split("	")
				efficiency = float(split[1])
				#print("efficiency: " + str(efficiency))


				try: #no patiente to research on finally on python f that
					target_pattern = patterns[functionName]
					target_pattern["seq_runtime"].append(seq_runtime)
					target_pattern["par_runtime"].append(par_runtime)
					target_pattern["speedup"].append(speedup)
					target_pattern["efficiency"].append(efficiency)
					target_pattern["nWorkers"].append(nWorkers)
					target_pattern["src_size"].append(src_size)
					#print(aux)
				except KeyError:
					print("Detected Pattern: " + functionName)
					data_structure = {}
					data_structure["seq_runtime"] = []
					data_structure["par_runtime"] = []
					data_structure["speedup"] = []
					data_structure["efficiency"] = []
					data_structure["nWorkers"] = []
					data_structure["src_size"] = []
					patterns[functionName] = data_structure

					data_structure["seq_runtime"].append(seq_runtime)
					data_structure["par_runtime"].append(par_runtime)
					data_structure["speedup"].append(speedup)
					data_structure["efficiency"].append(efficiency)
					data_structure["nWorkers"].append(nWorkers)
					data_structure["src_size"].append(src_size)

				


	print("nr_patterns: " , str(nr_patterns))
	print("nr_tests_src_size: " + str(nr_tests_src_size))
	print("nr_tests_worker_size: " + str(nr_tests_worker_size))


	#plotting runtime over data size for each pattern for each thread number
	opt = ""
	while opt != "y" and opt != "Y" and opt != "N" and opt != "n": 
		opt = input("Do you wish to make the graphs automatically?	[Y/N]\n")

	if(opt == "Y" or opt == "y" ):
		seq_runtime_values = []
		par_runtime_values = []
		data_size_values = []



		print("Plotting Runtime over Source Data Size for each Pattern")
		for pattern in patterns:
			for current_workerNr in range(0 , nr_tests_worker_size):
				nWorkers = patterns[pattern]["nWorkers"][current_workerNr * (nr_tests_src_size)]
				seq_runtime_values = patterns[pattern]["seq_runtime"][current_workerNr * (nr_tests_src_size): nr_tests_src_size * current_workerNr + nr_tests_src_size]
				par_runtime_values = patterns[pattern]["par_runtime"][current_workerNr * (nr_tests_src_size): nr_tests_src_size * current_workerNr + nr_tests_src_size]
				src_sizes = patterns[pattern]["src_size"][current_workerNr * (nr_tests_src_size): nr_tests_src_size * current_workerNr + nr_tests_src_size]
				makeRuntimeGraph(seq_runtime_values , par_runtime_values , src_sizes, 
								(pattern) + " pattern Runtime over Data size with number of Workers = "+ str(nWorkers),
								"Runtime in microseconds" , "Size of the data")

		print("Making efficiency and Speedup graphs for each Pattern\n")
		#plotting Efficiency and Speedup over data size for each pattern for each thread number
		for pattern in patterns:
			for current_workerNr in range(0 , nr_tests_worker_size):
				nWorkers = patterns[pattern]["nWorkers"][current_workerNr * (nr_tests_src_size)]
				efficiency_values = patterns[pattern]["efficiency"][current_workerNr * (nr_tests_src_size): nr_tests_src_size * current_workerNr + nr_tests_src_size]
				speedup_values = patterns[pattern]["speedup"][current_workerNr * (nr_tests_src_size): nr_tests_src_size * current_workerNr + nr_tests_src_size]
				src_sizes = patterns[pattern]["src_size"][current_workerNr * (nr_tests_src_size): nr_tests_src_size * current_workerNr + nr_tests_src_size]
				

				makeRuntimeEfficiencyGraph(efficiency_values , speedup_values , src_sizes, 
								(pattern) + " pattern Speedup and Efficiency over Data size with number of Workers = "+ str(nWorkers),
								"" , "")

	print("Writing CSV's")
	for pattern in patterns:
		 with open("csv/" + pattern+ '.csv', 'w', newline='') as csvfile:
		 	spamwriter = csv.writer(csvfile, delimiter=';',
                            quotechar='|', quoting=csv.QUOTE_MINIMAL)
	 		spamwriter.writerow(target_pattern["par_runtime"])
	 		spamwriter.writerow(target_pattern["seq_runtime"])
	 		spamwriter.writerow(target_pattern["src_size"])
	 		spamwriter.writerow(target_pattern["nWorkers"])
	 		spamwriter.writerow(target_pattern["speedup"])
	 		spamwriter.writerow(target_pattern["efficiency"])
	 		



		#plotting speedup and efficiency over data size



	f.close()


def makeRuntimeGraph(seq_runtime, par_runtime, src_sizes ,title , x_plot_label, y_plot_labels):
    plt.figure(figsize=(8, 8), frameon=False)


    plt.plot(src_sizes, seq_runtime, '-ro', linewidth=2, label="Sequential runtime")
    plt.plot(src_sizes, par_runtime, '-go', linewidth=2, label="Paralel runtime")
    plt.title(title)
    plt.legend()
    plt.xlabel("Source Size")
    plt.ylabel("Runtime in microseconds")
    plt.savefig("graphs/" + title + ".png", dpi=300, bbox_inches="tight")
    # plt.show()
    plt.close()

def makeRuntimeEfficiencyGraph(efficiency_values, speedup_values, src_sizes ,title , x_plot_label, y_plot_labels):
    plt.figure(figsize=(8, 8), frameon=False)


    plt.plot(src_sizes, efficiency_values, '-ro', linewidth=2, label="Efficiency")
    plt.plot(src_sizes, speedup_values, '-go', linewidth=2, label="Speedup")
    plt.title(title)
    plt.legend()
    plt.xlabel("Source Size")
    plt.ylabel("")
    plt.savefig("graphs/" + title + ".png", dpi=300, bbox_inches="tight")
    # plt.show()
    plt.close()


def makeSmoothGraph(x_values, val_errors, train_errors,
                    test_errors, title, x_plot_label, y_plot_label):

    x_smooth, val_errors_smooth = smoothLine(x_values, val_errors)
    x_smooth, train_errors_smooth = smoothLine(x_values, train_errors)
    x_smooth, test_errors_smooth = smoothLine(x_values, test_errors)
    plt.figure(figsize=(8, 8), frameon=False)
    plt.plot(x_smooth, val_errors_smooth, '-b',
             linewidth=2, label="Validation Error")
    plt.plot(x_smooth, train_errors_smooth, '-g',
             linewidth=2, label="Train Error")
    plt.plot(x_smooth, test_errors_smooth, '-r',
             linewidth=2, label="Test Error")
    plt.title(title)
    plt.legend()
    plt.xlabel(x_plot_label)
    plt.ylabel(y_plot_label)
    plt.savefig(title + ".png", dpi=300, bbox_inches="tight")
    # plt.show()
    plt.close


if __name__ == "__main__":
	main()

