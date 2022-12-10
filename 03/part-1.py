#!/usr/bin/env python3

def dup(s):
    l = len(s)//2
    h1 = list(s[:l])
    h2 = list(s[l:])
    for c in h1:
        if c in h2:
            return ord( c )
    return None

def priority(c):
    if c >= ord('a'): 
        return c - ord('a') + 1
    else:
        return c - ord('A') + 27

f = open('input')
priorities = 0
for ln in f:
    priorities = priorities + priority( dup( ln ) )
print(priorities)

