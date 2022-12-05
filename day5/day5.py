f = open("input")

lines = f.read().split("\n")
f.close()

stacks = []

initial_stack = []

while True:
    line = lines[0]
    if line == "": break
    initial_stack.insert(0, line)
    lines.pop(0)
lines.pop(0)
stack_count = len(initial_stack[0].split())
for i in range(stack_count):
    stacks.append([])
initial_stack.pop(0)
for line in initial_stack:
    for i in range(stack_count):
        item = line[1+i*4]
        if item == " ": continue
        stacks[i].append(line[1+i*4])

for line in lines:
    if line == "": continue
    print(line)
    cmd = line.split()
    count = int(cmd[1])
    src = int(cmd[3])-1
    dst = int(cmd[5])-1
    for _ in range(count):
        item = stacks[src].pop()
        stacks[dst].append(item)

for stack in stacks:
    print(" ".join(stack))

