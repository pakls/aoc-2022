#!/usr/bin/env python3

f = open('input')

# A rock, B paper, C scissor
# X lose, Y, draw, Z win

# win 6, draw 3, lose 0
# A gets 1, B gets 2, C gets 3

scores = {
    'A': { 'X': 0+3, 'Y': 3+1, 'Z': 6+2 },
    'B': { 'X': 0+1, 'Y': 3+2, 'Z': 6+3 },
    'C': { 'X': 0+2, 'Y': 3+3, 'Z': 6+1 }
}

score = 0
for ln in f:
    score = score + scores[ln[0]][ln[2]]
print(score)

