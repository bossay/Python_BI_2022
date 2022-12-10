#!/usr/bin/env python3

import argparse
import os
import shutil
import sys


parser = argparse.ArgumentParser(description='Remove files, directories')
parser.add_argument('filename_or_dirname', default=True, nargs='+', help='input file or directory')
parser.add_argument('-r', '--recursive', action='store_true', help='Recursive deletion')
args = parser.parse_args()

def main(arguments):
    file_or_dir = arguments.filename_or_dirname
    for i_object in file_or_dir:
        if os.path.isdir(i_object):
            if arguments.recursive:
                shutil.rmtree(i_object)
            else:
                print(f'Error: {i_object} is a directory')
                sys.exit(1)
        else:
            os.remove(i_object)

main(args)
