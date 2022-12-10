#!/usr/bin/env python3

if True:
    FILE    = 'input'
else:
    FILE    = 'in'

def all_different(chars):
    for i in range(len(chars) - 1):
        for j in range(i+1, len(chars)):
            if chars[i] == chars[j]:
                return False
    return True

def marker_start(ln):
    LENGTH = 14
    chars = [ '' for i in range(LENGTH) ]
    pos = 1
    for c in ln:
        chars = chars[1:]
        chars.append(c)
        if pos < LENGTH:
            pass
        elif all_different(chars):
            print(pos)
            return
        pos = pos + 1
        
buf = open(FILE).readlines()
for ln in buf:
    marker_start(ln)

