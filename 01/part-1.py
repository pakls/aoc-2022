#!/usr/bin/env python3

f = open('input')
Max = Now = 0
for ln in f:
    ln = ln.strip()
    if len(ln) == 0:
        Now = 0
    else:
        Now = Now + int(ln)
        Max = Now if Now > Max else Max
    
print(Max)

