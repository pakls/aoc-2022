#!/usr/bin/env python3

def contains(b1, e1, b2, e2):
    return int(b1) <= int(b2) and int(e1) >= int(e2)

f = open('input')
fully = 0
for ln in f:
    sec1,sec2 = ln.split(',')
    b1,e1 = sec1.split('-')
    b2,e2 = sec2.split('-')
    if contains(b1, e1, b2, e2) or contains(b2, e2, b1, e1):
        fully = fully + 1

print(fully)
