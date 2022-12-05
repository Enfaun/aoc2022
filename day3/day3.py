f = open("input")

def get_priority(c):
    if c.islower():
        return ord(c)-ord('a')+1
    else:
        return ord(c)-ord('A')+27

priority_sum = 0

for line in f:
    line = line.strip()
    half = int(len(line)/2)
    comp1, comp2 = line[:half], line[half:]
    print(comp1)
    print(comp2)
    s1 = set(comp1)
    s2 = set(comp2)
    s = s1 & s2
    priority_sum += get_priority(s.pop())

print(priority_sum)
