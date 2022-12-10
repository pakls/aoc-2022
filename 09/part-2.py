#!/usr/bin/env python3

class p:
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y
    def __sub__(self, obj):
        return max(abs(self.x - obj.x), abs(self.y - obj.y))
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
    def move(self, op):
        self.__getattribute__(op)()
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
pts     = [p() for i in range(10)]
ins(p(0,0))

if True:
    buf = open('input').readlines()
else:
    buf = open('in').readlines()

for ln in buf:
    [op, steps] = parse(ln)
    #print(op, steps)
    for i in range(steps):
        pts[0].move(op)
        for j in range(1, 10):
            p0, p1 = pts[j - 1], pts[j]
            if p0 - p1 < 2:
                break
            if p0.x > p1.x:
                p1.R()
            if p0.x < p1.x:
                p1.L()
            if p0.y > p1.y:
                p1.U()
            if p0.y < p1.y:
                p1.D()
        ins(pts[9])

print(len(visited))

