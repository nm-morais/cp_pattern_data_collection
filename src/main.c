#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>

#include <time.h>
#include <sys/time.h>

#include "unit.h"
#include "debug.h"

#define TYPE double

static long long wall_clock_time(void) {
    struct timeval tv;
    gettimeofday(&tv, NULL);
    return tv.tv_sec * 1e6 + tv.tv_usec;
}



int main(int argc, char* argv[]) {
    int i, N, timesToRepeat, nWorkers;
    long long start, end, start_seq, end_seq;
    float speedup, efficiency, average_seq, average_par;
    int c;


    nWorkers = atoi(argv[2]);
    timesToRepeat = atoi(argv[3]);


    while ((c = getopt (argc, argv, "d")) != -1)
        switch (c) {
            case 'd':
                debug = 1; break;
            default:
                printf("Invalid option\n");
                abort ();
        }
    argc -= optind;
    argv += optind;
    
    if (argc != 3) {
        printf("Usage: ./example N nWorkers timesToRepeat\n");
        return -1;
    }

    srand(time(NULL));
    srand48(time(NULL));

    N = atol(argv[0]);
    TYPE *src = malloc (sizeof(*src) * N);
    for (i = 0; i < N; i++)
        src[i] = drand48();
    //printf ("Done!\n");
    
    printDouble (src, N, "SRC");
    if (debug)
        printf ("\n\n");

    speedup = 0.0;
    efficiency = 0.0;
    average_seq = 0.0;
    average_par = 0.0;


    for (int i = 0;  i < nTestFunction;  i+=2) {
        for(int j = 0 ; j < timesToRepeat; j++){
            start = wall_clock_time();
            testFunction[i] (src, N, sizeof(*src));
            end = wall_clock_time();

            start_seq = wall_clock_time();
            testFunction[i+1] (src, N, sizeof(*src));
            end_seq = wall_clock_time();
           
            average_seq += (end_seq - start_seq);
            average_par += (end - start);

        }

        average_seq = average_seq / timesToRepeat;
        average_par = average_par / timesToRepeat;

        speedup = (average_par / (average_seq * 1.0)); //force cast
        efficiency = speedup / (nWorkers * 1.0); //force cast

        printf("%s:\t%8ld\tmicroseconds\n", testNames[i], (long) (average_par));
        printf("%s:\t%8ld\tmicroseconds\n", testNames[i + 1], (long) (average_seq));
        printf("Speedup: \t%lf\n" , speedup);
        printf("Efficiency \t%lf\n", efficiency);

        average_seq = 0.0;
        average_par = 0.0;

    }

    return 0;
}
