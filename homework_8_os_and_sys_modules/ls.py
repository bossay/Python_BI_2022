#! /usr/bin/env python3

import argparse
import os


parser = argparse.ArgumentParser(description='Lists directory contents of files and directories')
parser.add_argument('path_to_file', nargs='*', default='./', help='directory')
parser.add_argument('-a', '--all_files', action='store_true', help='show all files')
args = parser.parse_args()

def main(arguments):
    path = arguments.path_to_file[0]
    l_files_in_dir = os.listdir(path)
    if arguments.all_files:
        print('.')
        print('..')
        for file in l_files_in_dir:
            print(file)
    else:
        for file in l_files_in_dir:
            if file.startswith('.'):
                continue
            else:
                print(file)

main(args)
