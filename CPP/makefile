CC = g++
CFLAGS = -std=c++11
LDFLAGS = -lm

all: leetcode.exe
	./$<

leetcode.exe: leetcode.cpp
	$(CC) $< $(CFLAGS) $(LDFLAGS) -o $@

# leetcode.o: leetcode.cpp
# 	$(CC) -c $<
	
clean:
	rm *.o *.exe
