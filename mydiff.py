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


ENCODING = "utf8"


def file_mtime(path):
    return (
        datetime.datetime
        .fromtimestamp(os.stat(path).st_mtime, datetime.timezone.utc)
        .astimezone()
        .isoformat()
    )
    
    
def getdifflines(fromfile, tofile, encoding):
    with open(fromfile, encoding=encoding) as ff:
        fromlines = ff.readlines()
    with open(tofile, encoding=encoding) as tf:
        tolines = tf.readlines()
    return fromlines, tolines

    
def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('-c', "--context", action='store_true', default=False, help='Produce a context format diff (default)')
    parser.add_argument('-u', "--unified", action='store_true', default=False, help='Produce a unified format diff')
    parser.add_argument('-n', "--ndiff", action='store_true', default=False, help='Produce a ndiff format diff')
    parser.add_argument('-l', '--lines', type=int, default=3, help='Set number of context lines (default 3)')
    parser.add_argument('-o', '--outfile', type=str, default="", help='Write diff to an output file. If the filename ends with ".html" a HTML side by side diff will be produced. All other endings will be treated as text containing the console output.')
    parser.add_argument('fromfile', help="First file for diff")
    parser.add_argument('tofile', help="Second file for diff")
    options = parser.parse_args()

    lines = options.lines
    fromfile = options.fromfile
    tofile = options.tofile
    
    if options.outfile:
        outfile = options.outfile
        makehtml = outfile.endswith((".html", ".htm"))
    else:
        outfile = ""
        makehtml = False

    fromdate = file_mtime(fromfile)
    todate = file_mtime(tofile)

    if outfile:
        fromlines, tolines = getdifflines(fromfile, tofile, ENCODING)
    else:
        fromlines, tolines = getdifflines(fromfile, tofile, None)

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
        with open(outfile, "w", encoding=ENCODING) as f:
            f.writelines(diff)
        print("{} written".format(outfile))
    else:
        sys.stdout.writelines(diff)

    
if __name__ == '__main__':
    main()
