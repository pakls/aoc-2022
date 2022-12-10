#!/usr/bin/env python3

class p:
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y
    def __sub__(self, obj):
        return abs(self.x - obj.x) > 1 or abs(self.y - obj.y) > 1
    def __eq__(self, obj):
        return self.x == obj.x and self.y == obj.y
    def L(self):
        self.x = self.x - 1
    def R(self):
        self.x = self.x + 1
    def U(self):
        self.y = self.y + 1
    def D(self):
        self.y = self.y - 1
    def __repr__(self):
        return "({}, {})".format(self.x, self.y)
    def clone(self, obj):
        self.x = obj.x
        self.y = obj.y

def parse(ln):
    toks = ln.split()
    toks[1] = int(toks[1])
    return toks

def ins(pt):
    for q in visited:
        if pt == q:
            return
    n = p()
    n.clone(pt)
    visited.append(n)

visited = []
oh = p()
ot = p()
nh = p()
nt = p()
ins(p(0,0))

if True:
    buf = open('input').readlines()
else:
    buf = open('in').readlines()

for ln in buf:
    [op, steps] = parse(ln)
    print(op, steps)
    for i in range(steps):
        ot.clone(nt)
        oh.clone(nh)
        nh.__getattribute__(op)()
        if nh - ot:
            nt.clone(oh)
            ins(nt)
        #print("head {} -> {}, tail {} -> {}, visited {}".format(oh, nh, ot, nt, len(visited)))

if False:
    for y in range(4, -1, -1):
        print(str(y) + ' ', end='')
        for x in range(0, 6):
            pt = p(x, y)
            if pt in visited:
                print('#', end='')
            else:
                print('.', end='')
        print()

print(len(visited))
