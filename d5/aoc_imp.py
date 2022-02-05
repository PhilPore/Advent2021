vents = []
inp = "input.txt"
dev = "test.txt"
with open(inp) as f:
    raw = f.read().strip()
    vents = raw.split("\n")
v_list = []
for i in vents:
    p0,p1 = i.split(' -> ')
    p0 = tuple(map(int,p0.split(",")))
    p1 = tuple(map(int,p1.split(",")))
    v_list.append((p0,p1))

def part1_hor_vert(lst):
    
    #counter = 0
    point_map = {}
    for ((x1, y1),(x2,y2)) in lst:
        if x1 == x2 or y1 == y2:
            delta = abs(x2-x1) or abs(y2-y1)
            x_inc =  (x2-x1)/delta
            y_inc = (y2-y1)/delta
            #you can store tuples as keys
            
            for i in range(delta+1):
                point = ((x1+i*x_inc),(y1+i*y_inc))
                point_map[point] = point_map.get(point,0)+1
    val = sum(1 for i in point_map.values() if i >= 2)
    return val 

def part2_all(vents):
    point_map = {}
    for ((x1, y1),(x2,y2)) in vents:
        delta = abs(x2-x1) or abs(y2-y1) #we can use the distance to help us figure out direction of points
        x_inc = (x2-x1)/delta #for example, a delta of 2 with x2 = 4 x1 = 6 leads us to -2/2 = -1, meaning go backwards. 
        #A lot nicer than what we were trying previous. Dont need to worry about y or x = 0 
        y_inc = (y2-y1)/delta
        for i in range(delta+1):
            point = ((x1+i*x_inc),(y1+i*y_inc))
            point_map[point] = point_map.get(point,0)+1
    val = sum(1 for i in point_map.values() if i >= 2)
    return val 

    

print(part1_hor_vert(v_list))
print(part2_all(v_list))