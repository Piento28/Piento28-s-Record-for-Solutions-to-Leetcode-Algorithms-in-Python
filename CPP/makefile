all: leetcode.exe
	./$<

leetcode.exe: leetcode.o
	gcc -o $@ $<

leetcode.o: leetcode.cpp
	gcc -c $<
	
clean:
	rm *.o *.exe
