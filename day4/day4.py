f = open("input")

def get_range(range_str):
    lower, upper = range_str.split("-")
    lower, upper = int(lower), int(upper)
    return range(lower,upper+1)

def in_range(range1, range2):
    if not range1: return True
    if not range2: return False
    return range1.start in range2 and range1[-1] in range2

count = 0

for line in f:
    line = line.strip()
    if line == "": contiune
    range1, range2 = line.split(",")
    range1, range2 = get_range(range1), get_range(range2)
    if in_range(range1, range2):
        count+=1
    elif in_range(range2, range1):
        count+=1
print(count)
