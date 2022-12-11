#!/usr/bin/env python3

if True:
    buf = open('input').readlines()
else:
    buf = open('in').readlines()

class Monkey:
    def __init__(self):
        self.items = []
        self.num   = -1
        self.op    = False # add if True, mul if False
        self.opnd  = None
        self.div   = None
        self.throw = {}

        self.inspects = 0

    def __repr__(self):
        return "\n".join([
            "Monkey {}".format(self.num),
            "    Items: {}".format(','.join( [ str(i) for i in self.items ] )),
            "    Op: new = old {} {}".format(self.op, self.opnd),
            "    Test: divisible by {}".format(self.div),
            "    Throw to {} or {}".format(self.throw[True], self.throw[False]),
            "    Inspects {}".format(self.inspects)
        ] )

def parse_monkey(buf):

    m = Monkey()

    toks = buf[0].replace(':', ' ').split()
    m.num = int(toks[1])

    for i in buf[1].replace(',', ' ').split()[2:]:
        m.items.append(int(i))

    toks   = buf[2].split()
    if toks[4] == '+':
        m.op = '+'
        m.opnd = int(toks[5])
    elif toks[5] == 'old':
        m.op = '^'
    else:
        m.op = '*'
        m.opnd = int(toks[5])
    
    m.div  = int(buf[3].split()[3])

    m.throw[True]  = int(buf[4].split()[5])

    m.throw[False] = int(buf[5].split()[5])

    return m


def parse(buf):
    arr = []
    l = len(buf)
    k = 0
    while k + 6 <= l:
        print('line {} to line {}'.format(l,k+6))
        arr.append(parse_monkey(buf[k:k+6]))
        k = k + 7
    return arr

monkeys = parse(buf)
for m in monkeys:
    print(m)

div = 1
for d in [ m.div for m in monkeys ]:
    div = div * d

for i in range(10000):
    print('round {}'.format(i))
    for m in monkeys:
        for item in m.items:
            m.inspects = m.inspects + 1
            if m.op == '+':
                item = item + m.opnd
            elif m.op == '*':
                item = item * m.opnd
            elif m.op == '^':
                item = item * item 
            item = item % div
            to_monkey = m.throw[ (item % m.div) == 0 ]
            monkeys[ to_monkey ].items.append( item )
        m.items = []

for m in monkeys:
    print(m)

inspects = [ m.inspects for m in monkeys ]
inspects.sort(reverse = True)

print(inspects[0] * inspects[1])
