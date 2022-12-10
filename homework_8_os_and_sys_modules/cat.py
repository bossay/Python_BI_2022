#!/usr/bin/env python3

import argparse

# Make container for argument specifications
parser = argparse.ArgumentParser(description='Reads data from the file and gives their content as output')
parser.add_argument('file', default=True, help='Input file')
arguments = parser.parse_args()


# Main function
def read_file(file):
	with open(file, 'r') as inf:  # read the file line by line
		for line in inf:
			print(line[:-1])  # print the file line by line


read_file(arguments.file)
