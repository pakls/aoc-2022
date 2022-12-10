#!/usr/bin/env python3

if False:
    FILE    = 'input'
else:
    FILE    = 'in'

def marker_start(ln):
    c1 = c2 = c3 = 0
    pos = 1
    for c4 in ln:
        if pos < 4:
            pass
        elif c1 != c2 and c1 != c3 and c1 != c4 and c2 != c3 and c2 != c4 and c3 != c4:
            print(pos)
            return
        pos = pos + 1
        c1, c2, c3 = c2, c3, c4
        
buf = open(FILE).readlines()
for ln in buf:
    marker_start(ln)

