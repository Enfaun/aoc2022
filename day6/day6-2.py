f = open("input")
code = f.read().strip()
buf = ""
index = 0

while index < len(code):
    buf += code[index]
    buf = buf[-14:]
    index += 1
    if len(buf) == 14:
        if len(set(buf)) < len(buf):
            continue
        else:
            print(index, buf)
            break

