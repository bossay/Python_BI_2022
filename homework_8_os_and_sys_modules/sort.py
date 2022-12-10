#!/usr/bin/env python3

import argparse

# Make container for argument specifications
parser = argparse.ArgumentParser(description='Sorts the contents of a text file, line by line')
parser.add_argument('file', default=True, help='input file')
args = parser.parse_args()


# Main function
def read_file_and_sort(file):
    l_of_lines = []
    with open(file, 'r') as inf:  # read the file line by line
        for line in inf:
            l_of_lines.append(line[:-1])
    l_of_lines.sort()  # sort the list with lines
    return l_of_lines


print('\n'.join(map(str, read_file_and_sort(args.file))))
