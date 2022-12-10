#!/usr/bin/env python3

Elves = [ 0, 0, 0 ]

def _update(idx, num):

    # if index is too large or less than this elf
    if idx >= len(Elves) or num < Elves[idx]:
        return None

    # check next elf
    _num = _update( idx + 1, num )
    
    # more than next elf
    if _num != None:
        n = Elves[ idx ]
        Elves[ idx ] = _num
        return n
    else:
        n = Elves[ idx ]
        Elves[ idx ] = num
        return n

def update(num):
    _update(0, num)

f = open('input')
Sum = 0
for ln in f:
    ln = ln.strip()
    if len(ln) == 0:
        update(Sum)
        Sum = 0
        continue
    Sum = Sum + int(ln)
    
print(Elves[0] + Elves[1] + Elves[2])

