#!/usr/bin/env python3

f = open('input')

# A,X rock, B,Y paper, C,Z scissor
# win 6, draw 3, lose 0
# X gets 1, Y gets 2, Z gets 3

scores = {
    'A': { 'X': 3+1, 'Y': 6+2, 'Z': 0+3 },
    'B': { 'X': 0+1, 'Y': 3+2, 'Z': 6+3 },
    'C': { 'X': 6+1, 'Y': 0+2, 'Z': 3+3 }
}

score = 0
for ln in f:
    score = score + scores[ln[0]][ln[2]]
print(score)

