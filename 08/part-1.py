#!/usr/bin/env python3

if True:
    FILE    = 'input'
else:
    FILE    = 'in'

buf = open(FILE).readlines()
rows = len(buf)
cols = len(buf[0].strip())

trees = 0

def height(r, c):
    if r < 0 or r >= rows or c < 0 or c >= cols:
        return -1
    return int(buf[r][c])

def shorter(h, trees):
    for [i, j] in trees:
        if height(i, j) >= h:
            return False
    return True

def viewable(r, c):
    h = height(r, c)

    n1 = [ [i,c] for i in range(-1, r) ]
    n2 = [ [i,c] for i in range(r + 1, rows + 1) ]
    n3 = [ [r,i] for i in range(-1, c) ]
    n4 = [ [r,i] for i in range(c + 1, cols + 1) ]

    if shorter(h, n1) or shorter(h, n2) or shorter(h, n3) or shorter(h, n4):
        return 1
    return 0

for r in range(rows):
    for c in range(cols):
        trees = trees + viewable(r, c)

print(trees)
            

