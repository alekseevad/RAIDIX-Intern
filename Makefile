.PHONY: all clean install uninstall
CC = g++
CFLAGS = -Wall -Wextra -Wall

all: main

clean:
	rm -rf *.o main 	

main: main.o
	$(CC) main.o $(CFLAGS) -o main

main.o: main.cpp
	$(CC) -c $(CFLAGS) main.cpp



  
