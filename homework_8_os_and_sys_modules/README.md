# The os and sys modules

Here are the command line programs implemented in python using the **os**, **sys** and **argparse** modules.

Authors: Alexandra Kasyanova ([albidgy](https://github.com/albidgy)), Amina Ibragimova ([ibragimovaamina](https://github.com/ibragimovaamina)), Polina Bogaichuk ([bossay](https://github.com/bossay))

## About modules

> **os - Miscellaneous operating system interfaces.** Is a library of functions for working with the operating system. [More about os](https://docs.python.org/3/library/os.html)

> **sys - System-specific parameters and functions.** This is a set of functions for interacting the Python interpreter with the operating system. [More about sys](https://docs.python.org/3/library/sys.html)

> **argparse - Parser for command-line options, arguments and sub-commands.** This is a module for handling command line arguments. [More about argparse](https://docs.python.org/3/library/argparse.html)


## Set of programs

+ wc.py (-l, -w, -c)
+ ls.py (-a)
+ sort.py
+ rm.py (-r)
+ cat.py
+ tail.py (-n)
+ uniq.py

## wc.py (-l, -w, -c)
**wc.py** is used to find out number of lines, word count, byte and characters count in the files specified in the file arguments.

```{ruby}
wc.py [ Options ] [File]
```

The command has several options:

+ **-l**: This option prints the number of lines present in a file. With this option wc command displays two-columnar output, 1st column shows number of lines present in a file and 2nd itself represent the file name.

```{ruby}
wc.py -l file.txt
```

+ **-w**: This option prints the number of words present in a file. With this option wc command displays two-columnar output, 1st column shows number of words present in a file and 2nd is the file name.

```{ruby}
wc.py -w file.txt
```

+ **-c**: This option displays count of bytes present in a file. With this option it display two-columnar output, 1st column shows number of bytes present in a file and 2nd is the file name.

```{ruby}
wc.py -c file.txt
```

+ You can also use any combination of options:

```{ruby}
wc.py -lwc file.txt
wc.py -lc file.txt
wc.py -wc file.txt
```

## ls.py (-a)
**ls.py** is a command that lists directory contents of files and directories. **ls.py** has the following basic syntax:

```{ruby}
ls.py [ Options ] [File]
```
The command has a single option - list all files including hidden file starting with '.'. Use the -a option of the ls command to show hidden files and directories in the current directory:

```{ruby}
ls.py -a
```
The files that start with the dot are hidden (.). The current directory (.) as well as the parent directory (..) are displayed by `ls -a`.

## sort.py
**sort.py** command is used to sort a file, arranging the records in a particular order.

```{ruby}
sort.py [File]
```
To sort a text file, line by line, use:

```{ruby}
sort.py file.txt
```

## rm.py (-r)

**rm.py** is used for removing files.

```{ruby}
rm.py [OPTION]... FILE...
```
The command has a single option - delete all the files and sub-directories recursively of the parent directory:

```{ruby}
rm.py -r ./directory
```

## cat.py

**cat.py** (concatenate) command reads data from the file and gives their content as output. 

```{ruby}
cat.py file.txt
```


## tail.py (-n)

**tail.py** print the last N number of data of the given input. By default it prints the last 10 lines of the specified files.

```{ruby}
tail.py [OPTION]... FILE...
```
To output a certain number of lines from the end of the file, use the -n option:

```{ruby}
tail.py -n 50 file.txt
```

## uniq.py

**uniq.py** filters out the adjacent matching lines from the input file:

```{ruby}
uniq.py file.txt
```
