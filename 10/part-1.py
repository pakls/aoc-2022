#!/usr/bin/env python3

if True:
    buf = open('input').readlines()
else:
    buf = open('in').readlines()

X = 1
T = 1

signal = 0

def sampling(t):
    global T, signal, X
    interests = [ 20, 60, 100, 140, 180, 220 ]
    for i in interests:
        if i in range(T, T+t):
            print('cycle {} X {} signal {}'.format(i, X, X * i))
            signal = signal + X * i

for ln in buf:
    toks = ln.split()
    if toks[0] == 'noop':
        print(ln.strip(), T, X)
        sampling(1)
        T = T + 1
    elif toks[0] == 'addx':
        print('T {} X {} --- {}'.format(T, X, ln.strip()))
        sampling(2)
        T = T + 2
        X = X + int(toks[1])

print(signal)

