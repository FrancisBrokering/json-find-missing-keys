#!/usr/bin/env python3

import sys
import json

missing = False
mylist = []
mydict = dict()
for i in sys.argv[1:]:
    with open(i) as file:
        mydict[i] = set(json.load(file).keys())

myset = set()
for s in mydict.values():
    myset = myset.union(s)

for key, value in mydict.items():
    diff = myset.difference(value)
    if (diff != set()):
        for i in diff:  
            print('"{0}" is missing from the file {1}'.format(i, key), file=sys.stderr)
        missing = True

if (not missing):
    print("no missing keys!")
    exit(0)

else:
    exit(1)

