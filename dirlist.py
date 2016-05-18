#!/usr/bin/env python3
# -*- coding: utf-8 -*-


"""Get a list of all directories under the given.
The directory tree will be browsed recursively to get a complete list.
"""


HELP = """\
Usage:

dirlist.py <root directory> <ouput file>
"""


import sys
import os


def error(msg):
    print(msg, file=sys.stderr)
    exit(1)


def getpaths(root):
    paths = []
    tree = os.walk(root)
    for dir in tree:
        paths += list(map(lambda file: os.path.join(dir[0], file), dir[1] + dir[2]))
    return sorted(paths)


def main(args):
    if len(args) != 3 or not os.path.isdir(args[1]):
        error(HELP)
    root = args[1]
    outfile = args[2]
    
    paths = getpaths(root)
    with open(outfile, "w", encoding="utf8") as f:
        for path in paths:
            f.write(path + "\n")


if __name__ == "__main__":
    main(sys.argv)