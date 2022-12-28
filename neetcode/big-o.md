# Big-O Notation - For Coding Interviews


https://www.youtube.com/watch?v=BgLTDT03QtU&ab_channel=NeetCode

# Overview

Big O notation is about measuring the time an algorythm will took to perform his job with a variable size input (like a list or dictionnary or some iterable)

Time in this context is generalization because time of execution varies from server to server (cpu, ram, disk speed, conccurent process, resources availability and so on). In fact by time it mean how many time the operations within the algorythm will be executed.

For example, if your the method make 3 operation on each element of the input, but only with a single for-loop, it will be a O(n*2).

- O(1) -> constant time complexity-> time is always the same, not matter the input size. u
- O(n) -> linear grow time -> as input size increse, the time increase linearly. single for-loop over an iterable is a linear algorythm
searching an array is a linear. In the worst case you'll have to iterate over the whole list which is O(n)
- O(n^2) -> inner for-loop.  Or matrix iteration.
- O(log n) - when you remove half the remaining inputs at each iteration. binary tree search for eg.
...