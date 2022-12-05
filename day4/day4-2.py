f = open("input")

def get_range(range_str):
    lower, upper = range_str.split("-")
    lower, upper = int(lower), int(upper)
    return range(lower,upper+1)


count = 0

for line in f:
    line = line.strip()
    if line == "": contiune
    range1, range2 = line.split(",")
    range1, range2 = get_range(range1), get_range(range2)
    overlaps = len(set(range1) & set(range2))
    if overlaps>0:
        count+=1
print(count)

