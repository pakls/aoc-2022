#!/usr/bin/env python3

if True:
    FILE    = 'input'
else:
    FILE    = 'in'

def cd(cwd, d):
    if d == '..':
        d = '/'.join(cwd.split('/')[:-1])
    elif d != '/':
        if cwd == '/':
            d = cwd + d
        else:
            d = cwd + '/' + d
    return d

fs = {}

buf = open(FILE).readlines()
cwd = None
for ln in buf:
    toks = ln.split()
    if len(toks) == 0:
        break
    #print(ln.strip())
    if toks[0] == '$':

        if toks[1] == 'cd':
            cwd = cd( cwd, toks[2] )
        elif toks[1] == 'ls':
            #print('ls ---> ' + cwd)
            fs[ cwd ] = { 'd': [], 'f': {}  }
        
    else:
        #print('listing ' + cwd)
        if toks[0] == 'dir':
            fs[ cwd ][ 'd' ].append( cd( cwd, toks[1] ) )
        else:
            fs[ cwd ][ 'f' ][ toks[1] ] = int(toks[0])

#print(fs)

def size(fs, d):
    total = 0
    for sub in fs[d]['d']:
        total = total + size(fs, sub)
    for f in fs[d]['f']:
        total = total + fs[d]['f'][f]
    return total

needed = 30000000 - (70000000 - size(fs, '/'))
print('root ' + str(size(fs,'/')))
delete = -1

for d in fs:
    s = size(fs, d)
    #print('---> ' + d + ' ' + str(s))
    if s >= needed and (delete == -1 or s < delete):
        delete = s

print(delete)

