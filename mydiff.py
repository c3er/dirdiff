#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Based on "diff.py" from Python distribution (Tools/scripts)


""" Command line interface to difflib.py providing diffs in four formats:

* ndiff:    lists every line and highlights interline changes.
* context:  highlights clusters of changes in a before/after format.
* unified:  highlights clusters of changes in an inline format.
* html:     generates side by side comparison with change highlights.

"""


import sys
import os
import time
import argparse
import datetime
import difflib


def file_mtime(path):
    return (
        datetime.datetime
        .fromtimestamp(os.stat(path).st_mtime, datetime.timezone.utc)
        .astimezone()
        .isoformat()
    )

    
def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('-c', "--context", action='store_true', default=False, help='Produce a context format diff (default)')
    parser.add_argument('-u', "--unified", action='store_true', default=False, help='Produce a unified format diff')
    parser.add_argument('-m', "--makehtml", type=str, default="", help='Name for HTML side by side diff file (can use -c and -l in conjunction)')
    parser.add_argument('-n', "--ndiff", action='store_true', default=False, help='Produce a ndiff format diff')
    parser.add_argument('-l', '--lines', type=int, default=3, help='Set number of context lines (default 3)')
    parser.add_argument('-o', '--outfile', type=str, default="", help='Optional: Write diff to an output text file')
    parser.add_argument('fromfile')
    parser.add_argument('tofile')
    options = parser.parse_args()

    lines = options.lines
    fromfile = options.fromfile
    tofile = options.tofile
    
    if options.makehtml and options.outfile:
        print("-m and -o not allowed together", file=sys.stderr)
        sys.exit(1)
    elif options.makehtml:
        outfile = options.makehtml
        makehtml = True
    elif options.outfile:
        outfile = options.outfile
        makehtml = False
    else:
        outfile = ""
        makehtml = False

    fromdate = file_mtime(fromfile)
    todate = file_mtime(tofile)
    with open(fromfile) as ff:
        fromlines = ff.readlines()
    with open(tofile) as tf:
        tolines = tf.readlines()

    if options.unified:
        diff = difflib.unified_diff(fromlines, tolines, fromfile, tofile, fromdate, todate, n=lines)
    elif options.ndiff:
        diff = difflib.ndiff(fromlines, tolines)
    elif makehtml:
        diff = difflib.HtmlDiff().make_file(fromlines, tolines, fromfile, tofile, context=options.context, numlines=lines)
    else:
        # --context is default
        diff = difflib.context_diff(fromlines, tolines, fromfile, tofile, fromdate, todate, n=lines)

    if outfile:
        print("Outfile:", outfile)
    else:
        sys.stdout.writelines(diff)

    
if __name__ == '__main__':
    main()