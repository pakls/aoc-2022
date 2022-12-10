#!/usr/bin/env python3

def common(l1,l2,l3):
    s1=list(l1.strip())
    s2=list(l2.strip())
    s3=list(l3.strip())
    for c in s1:
        if c in s2 and c in s3:
            return ord(c)
    return None

def priority(c):
    if c >= ord('a'): 
        return c - ord('a') + 1
    else:
        return c - ord('A') + 27

f = open('input')
priorities = 0
while True:
    l1 = f.readline()
    if len(l1) == 0:
        break
    l2 = f.readline()
    l3 = f.readline()
    priorities = priorities + priority( common( l1,l2,l3 ) )
print(priorities)

