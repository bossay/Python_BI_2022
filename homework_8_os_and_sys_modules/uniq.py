#!/usr/bin/env python3

import argparse

# Make container for argument specifications
parser = argparse.ArgumentParser(description='Filters out the adjacent matching lines from the input file')
parser.add_argument('file', default=True, help='input file')
args = parser.parse_args()


# Main function
def main(input_file):
    list_of_lines = []  # list with answers
    with open(input_file, 'r') as file:  # read the file line by line
        for line in file:
            if len(list_of_lines) == 0:
                list_of_lines.append(line[:-1])  # if the list is empty add the first line to the sheet without  \n
            if line[:-1] != list_of_lines[-1]:  # add a new line if it is not the same as the last line in the list
                list_of_lines.append(line[:-1])
    return list_of_lines


print('\n'.join(map(str, main(args.file))))
