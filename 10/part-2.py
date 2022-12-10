#!/usr/bin/env python3

if True:
    buf = open('input').readlines()
else:
    buf = open('in').readlines()

X = 1
T = 1

def crt_draw(reg, cycle):
    pos = (cycle - 1) % 40
    if pos >= reg - 1 and pos <= reg + 1:
        print('#', end='')
    else:
        print('.', end='')
    if ((pos + 1) % 40) == 0:
        print()

for ln in buf:
    toks = ln.split()
    if toks[0] == 'noop':
        #print(ln.strip(), T, X)
        crt_draw(X, T)
        T = T + 1
    elif toks[0] == 'addx':
        #print('T {} X {} --- {}'.format(T, X, ln.strip()))
        crt_draw(X, T)
        crt_draw(X, T+1)
        T = T + 2
        X = X + int(toks[1])

