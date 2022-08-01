# File IO Lab

## Learning Goals

- Practice using file IO.
- Execute and test Python code using the Python shell and `pytest`.

***

## Introduction

In the last lesson we learned about the tools that can help us work
with files. Creating and manipulating files is a crucial skill that can
help you create useful and complex programs. In this lab we will explore
file IO.

***

## Instructions

Lets practice! In the file `file_io.py` write a function called `write_file` that takes in the arguments `file_name` and `file_content`.
The `file_name` can be a combined file path/name.
This function should use `file_name` and `file_content` to write a `txt`
file.

Write a `append_to_file` function that takes in the same parameters and
appends to the `.txt` file.

Write a `read_file` function that takes in a file name and  returns the
 content of the `.txt` file.

Example usage:

```py
# use write_file function. 
write_file(file_name="logfile", file_content="Log 1: 5 bananas added" )
append_file(file_name="logfile", append_content="Log 2: 3 bananas subtracted")

read_file(file_name="logfile")
# Log 1: 5 bananas added
# Log 2: 3 bananas subtracted
```

***

## Resources

- [Python File IO](https://docs.python.org/3/tutorial/inputoutput.html#reading-and-writing-files)
