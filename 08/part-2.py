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

def distance(h, trees):
    d = 0
    for [i, j] in trees:
        d = d + 1
        if height(i, j) >= h:
            break
    #print('distance', i, j, d)
    return d

def scene_score(r, c):
    #print('check', r, c)
    h = height(r, c)
    u = [ [i,c] for i in range(r-1, -1, -1) ]
    d = [ [i,c] for i in range(r+1, rows) ]
    l = [ [r,i] for i in range(c-1, -1, -1) ]
    r = [ [r,i] for i in range(c+1, cols) ]
    U = distance(h, u)
    D = distance(h, d)
    L = distance(h, l)
    R = distance(h, r)
    #print('u d l r', U,D,L,R, '=>', U*D*L*R)
    return U*D*L*R

highest_score = 0
rr = cc = 0
for r in range(1, rows - 1):
    for c in range(1, cols - 1):
        score = scene_score(r, c)
        #print(score, r, c)
        if score > highest_score:
            highest_score = score
            rr = r
            cc = c

print(highest_score, '@', rr, cc)

