# cp_pattern_data_collection

## READ ME FIRST

This is an automated data collection script, it contains:

1. A bash script to automate the execution of the program and save the output

1. A python script to parse the data file

1. A skeleton of the project where you should just drop your patterns.c and patterns

it took lots of time to develop and be "presentable" for others to use, so if you used this tool in some way, please refer us in the report, we are g28, composed by:

Nuno Morais, Marta Carlos, Luís Correia

**you should proof-read what i did, and verify everything**

If you need to make changes, feel free to, or make a pull request and contribute!


# REQUIREMENTS: 

1. CilkPlus

1. Python3 + matplotlib

1. Bash

1. Around 30 MB of space for the graphs (depends on the size of the tests)

# INSTRUCTIONS

## PRE: 

ssh into a computer with the requirements specified above, 
if the computer does not have python (like the LAB server)
there will be a note in the end

## INSTRUCTIONS STEP-BY-STEP: 

**0 - Change to home dir and clone the tool:**

  $ cd ~/ && git clone https://github.com/nm-morais/cp_pattern_data_collection.git

**1 - change into cp_pattern_data_collection:**

  $ cd cp_pattern_data_collection
  
**2 - Copy your implementation of patterns.c into the src directory (cp_pattern_data_collection/src) and compile it**

  For this you can use scp:
  $ scp  my_local_path_to_file/patterns.c  gXX@LAB_IP:~/cp_pattern_data_collection/src
  
  $ cd src
  
  $ make
  
  
**3 - run the bash script  which calls the entire chain of tools (READ CAREFULLY):**

  **BE RESPECTFULL**, if you use this in the lab, beware of the load you will be inflicting on the server
  
  **READ CAREFULLY**:
  
  the arguments are:
  **USAGE: start_tests.sh [MAX SOURCE SIZE] [INCREMENT] [MAX WORKERS] [TIMES TO AVERAGE]**

  **[MAX SOURCE SIZE]** : is the max size for the src array

  **[INCREMENT]** :  is by HOW MUCH you want to increment the size of your tests until INCREMENT==MAX SOURCE SIZE
    e.g. source size of 10 and increment of 1 leads to 10 tests

  **[MAX WORKERS]** : the number of threads for cilk to test up to

  **[TIMES TO AVERAGE]** : the number of times to run the test and get an average of
    
   IF you do max src = 10 and increment = 1 and max workers = 4 and times to average = 5, you will be making 10 * 4 * 5 = 200 tests!!!!
  
  example explained above : $ bash start_tests.sh 10 1 4 5
 
**4 - follow the script until the end, if you get following output or similar:**
 
    PARSING AND MAKING GRAPHS

    Starting : data/parser.py 1 2
    Traceback (most recent call last):
    File "data/parser.py", line 2, in <module>
    import matplotlib.pyplot as plt
    ImportError: No module named 'matplotlib'
    
  This means the computer you are working on doesn't have the requirements to run the python script, therefore you must copy the log file over to your computer and run in a computer with the requirements . use scp for this again:

  **$ scp \~/cp_pattern_data_collection gXX@LAB_IP:~/cp_pattern_data_collection/log**

  create a directory for the graphs and the csv's 
  **$ mkdir csv**
  **$ mkdir graphs**
  
  if you care about the graphs: run the python script with the following argumments: 
  
  **data = [MAX SOURCE SIZE] / [INCREMENT]**
  
  **arg2 = [MAX WORKERS]**
  
  **$ python3 parser.py arg1 arg2**

  if you dont: run the python script with 2 arguments randomly ,e.g.:
  
  **$ python3 parser.py -1 -1**
    and say N to the graph question

**5 - Results:**

  in your data folder **(cp_pattern_data_collection/data)** there should be two folders: **csv** and **graphs**,
  if you chose to make the graphs, there will be files in the graphs folder, they are self-explanatory
  In the CSV folder, there will be as many CSV files as the number of patterns you tested, the data in them follows the following structure:
  
    1 - paralel runtime
    2 - sequential runtime
    3 - source size
    4 - number of workers
    5 - speedup
    6 - efficiency
  
  
  

