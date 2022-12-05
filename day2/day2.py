score = 0
score2 = 0
f = open("input")

PAPER_1 = "A"
PAPER_2 = "X"
SCISSOR_1 = "B"
SCISSOR_2 = "Y"
STONE_1 = "C"
STONE_2 = "Z"

LOSE = "X"
DRAW = "Y"
WIN = "Z"

def getscore(c):
    return ord(c)-ord("W")

for line in f:
    line = line.strip()
    if line == "": continue
    p1, p2 = line.split(" ")
    score += ord(p2)-ord("W")
    if p1 == PAPER_1:
        if p2 == PAPER_2:   score+= 3
        if p2 == SCISSOR_2: score+= 6
        if p2 == STONE_2:   score+= 0
        if p2 == LOSE:
            score2 += getscore(STONE_2)
        if p2 == DRAW:
            score2 += 3
            score2 += getscore(PAPER_2)
        if p2 == WIN:
            score2 += 6
            score2 += getscore(SCISSOR_2)
    elif p1 == SCISSOR_1:
        if p2 == PAPER_2:   score+= 0
        if p2 == SCISSOR_2: score+= 3
        if p2 == STONE_2:   score+= 6
        if p2 == LOSE:
            score2 += getscore(PAPER_2)
        if p2 == DRAW:
            score2 += 3
            score2 += getscore(SCISSOR_2)
        if p2 == WIN:
            score2 += 6
            score2 += getscore(STONE_2)
    elif p1 == STONE_1:
        if p2 == PAPER_2:   score+= 6
        if p2 == SCISSOR_2: score+= 0
        if p2 == STONE_2:   score+= 3
        if p2 == LOSE:
            score2 += getscore(SCISSOR_2)
        if p2 == DRAW:
            score2 += 3
            score2 += getscore(STONE_2)
        if p2 == WIN:
            score2 += 6
            score2 += getscore(PAPER_2)

print(score)
print(score2)

