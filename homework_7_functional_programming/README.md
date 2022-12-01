# Introduction to functional programming

Functional programming is the use of functions with the best effect to create clean and maintainable software.


## About Functional

This set of functions to work with other functions that simplify the development and writing of scripts.

>OS: Windows 10, 21H2, x64
>Python 3.11.0

## About functions

+ `sequential_map` - a function takes any number of functions as arguments and a container of some values and returns a list of results of sequentially applying the passed functions to the values in the container.
+ `consensus_filter` - the function takes any number of functions that return `True` or `False` and a container of some values. It returns a list of values that, when passed to all functions, give `True`.
+ `conditional_reduce` - takes 2 functions and a container of values and returns the value of the second function, skipping values with which the first function gave `False`.
+ `sequential_map` - the function takes any number of functions and returns a function that combines all passed functions by consecutive execution. 
