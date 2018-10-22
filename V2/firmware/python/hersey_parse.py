a = open('hersey_codes.txt', 'r')
lines = a.readlines()

for line in lines:
    if not '#' in line:
        if line.strip()>0:
            print("    '': '%s'," % line.strip())
    else:
        print(line.strip())
