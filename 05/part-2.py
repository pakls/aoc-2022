#!/usr/bin/env python3

if True:
    CRATES  = 9
    INI_ROW = 8
    ACT_ROW = 10
    FILE    = 'input'
else:
    CRATES  = 3
    INI_ROW = 3
    ACT_ROW = 5
    FILE    = 'in'

buf = open(FILE).readlines()
stacks = [ "" for i in range(CRATES) ]

for i in range(INI_ROW):
    line = buf[i] + " " * 10
    for j in range(CRATES):
        pos = j*4 + 1
        if line[pos] != ' ':
            stacks[j] = stacks[j] + line[pos]

def dump():
    for crate in stacks:
        print(crate)
    print("-----------------")

dump()
for i in range(ACT_ROW, len(buf)):
    print(buf[i].strip())
    print("-----------------")
    toks = buf[i].split()
    num = int(toks[1])
    src = int(toks[3]) - 1
    dst = int(toks[5]) - 1
    if num > len(stacks[src]):
        raise
    crate, stacks[src] = stacks[src][:num], stacks[src][num:]
    stacks[dst] = crate + stacks[dst]
    dump()

heads = [ stacks[i][0] for i in range(CRATES) ]
print(''.join(heads))

