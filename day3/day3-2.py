f = open("input")

def get_priority(c):
    if c.islower():
        return ord(c)-ord('a')+1
    else:
        return ord(c)-ord('A')+27

lines = f.read().split("\n")
if lines[len(lines)-1] == "": lines.pop()

priority_sum = 0

while len(lines)>0:
    s1 = set(lines.pop(0))
    s2 = set(lines.pop(0))
    s3 = set(lines.pop(0))
    s = s1 & s2 & s3
    priority_sum += get_priority(s.pop())

print(priority_sum)
