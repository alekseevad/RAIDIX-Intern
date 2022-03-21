CC = g++
CFLAGS = -c -Wall -Wextra -Wall
all: main

main: main.o
	$(CC) $(CFLAGS) main.o -o main

main.o: main.cpp
	$(CC) $(CFLAGS) main.cpp

clean: 
	rm -rf main.o
  
