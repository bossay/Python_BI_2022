#!/usr/bin/env python3

import argparse


# Make container for argument specifications
parser = argparse.ArgumentParser(description='Print the last N (10 - default) number of data of the given input')
parser.add_argument('-n', '--line', action='count', help='output a specific number of lines')
parser.add_argument('integer', metavar='N', type=int, default=10, nargs='?', help='the number of lines to output')
parser.add_argument('file', default=True, help='input file')
args = parser.parse_args()


# Main function
def main(file_name):
    l_of_lines = []  # list with answers
    with open(file_name, 'r') as inf:  # read the file line by line
        for line in inf:
            l_of_lines.append(line[:-1])
    return l_of_lines


# Main conditions
if args.line:  # if the number of lines -n is entered, print this number of lines from the end of the file
    result = main(args.file)[-args.integer:]
else:  # output the default number of lines (10)
    result = main(args.file)[-10:]

print('\n'.join(map(str, result)))
