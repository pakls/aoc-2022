#!/usr/bin/env python3

def contains(b1, e1, b2, e2):
    return int(b1) <= int(b2) and int(e1) >= int(e2)

def in_range(x1, x2, x):
    return x1 <= x and x <= x2

def overlapped(b1, e1, b2, e2):
    return in_range(int(b1), int(e1), int(b2)) or in_range(int(b1), int(e1), int(e2))

f = open('input')
overlap = 0
for ln in f:
    sec1,sec2 = ln.split(',')
    b1,e1 = sec1.split('-')
    b2,e2 = sec2.split('-')
    if contains(b1, e1, b2, e2) or contains(b2, e2, b1, e1):
        overlap = overlap + 1
    elif overlapped(b1, e1, b2, e2):
        overlap = overlap + 1

print(overlap)

