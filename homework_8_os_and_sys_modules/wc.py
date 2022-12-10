#!/usr/bin/env python3

import argparse
import os


parser = argparse.ArgumentParser(description='Find out number of lines, word count and byte in the file')
parser.add_argument('filename', default=True, help='input file')
parser.add_argument('-l', '--lines', action='store_true', help='Number of lines in file')
parser.add_argument('-c', '--bytes', action='store_true', help='File size in bytes')
parser.add_argument('-w', '--words', action='store_true', help='Number of words in file')
arguments = parser.parse_args()

# prints the number of lines
def wc_count_line(input_file):
	file_read = open(input_file, 'r')
	file = file_read.read()
	file_read.close()
	return file.count('\n')

# prints the number of words
def wc_count_words(input_file):
	file_read = open(input_file, 'r')
	file = file_read.read()
	file_read.close()
	return file.count(' ') + file.count('\n')

# displays count of bytes
def wc_count_bytes(input_file):
    return os.path.getsize(input_file) 

def main(arguments):
	result = [] # list with answers
	input_file = arguments.filename
	if arguments.lines:
		result.append(wc_count_line(input_file))
	if arguments.words:
		result.append(wc_count_words(input_file))
	if arguments.bytes:
		result.append(wc_count_bytes(input_file))
	string_result = '\t' + '\t'.join(map(str, result)) + ' ' + input_file
	return string_result
		
print(main(arguments))

