f = open('input.txt')
commands = f.readlines()
def get_cord_prod(commands):
    cord = [0,0]
    for line in commands:
        if line == '\n':
            continue
        com, val = line.split()
        val = int(val)
        if com == 'forward':
            cord[1]+=val
        elif com == 'up':
            cord[0]-=val
        else:
            cord[0]+=val
    print(cord[0]*cord[1])
def p2_use_depth(commands):
    depth = 0
    #aim is y pos
    cord = [0,0]
    for line in commands:
        if line == '\n':
            continue
        com, val = line.split()
        val = int(val)
        if com == 'forward':
            cord[1]+=val
            depth+=val*cord[0]
        elif com == 'up':
            cord[0]-=val
        else:
            cord[0]+=val
    print(depth*cord[1])

get_cord_prod(commands)
p2_use_depth(commands)
