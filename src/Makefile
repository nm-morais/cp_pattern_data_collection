CC=gcc
CFLAGS=-g -std=gnu11 -Wall -Werror -fcilkplus
LDFLAGS=-lcilkrts -lm

S=debug.c main.c patterns.c unit.c patternsSeq.c
O=$(patsubst %.c,%.o,$(S))

TARGET=main
all: $(TARGET)

main: $(O)
	$(CC) -o $@ $^ $(LDFLAGS)

clean:
	rm -f $(TARGET) $(O)


debug.o: debug.c debug.h
main.o: main.c unit.h debug.h
patternsSeq.o: patternsSeq.c patternsSeq.h
patterns.o: patterns.c patterns.h
unit.o: unit.c patterns.h debug.h unit.h patternsSeq.h
