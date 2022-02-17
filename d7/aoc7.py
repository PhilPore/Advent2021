import sys
positions = []
inp = "input.txt"
dev = "test.txt"
with open(inp) as f:
    raw = f.read().strip()
    positions = raw.split("\n")


pos = [int(i) for i in positions[0].split(',')]

#either find most frequent or the median. i sort of want to try the median first


def part1_S(pos):
    pos.sort()
    div = pos[len(pos)//2]
    val = 0
    for i in pos:
        val+= abs(i-div)
    return (val,len(pos)//2)

def part1_F(pos):
    #frequency
    dic = {}
    cur_max = -1
    for i in pos:
        if i not in dic:
            dic[i] = 0
        dic[i]+=1
        
        cur_max = i if dic[i] > dic.get(cur_max,0) else cur_max
    val = 0
    for i in pos:
        val+= abs(i-cur_max)
    return val

def part2(cur_m,cur_i, pos):
    #we have the mid poin so maybe incremednt until we get a value thats less than our cur best?
    #have to look into it further
    print("Do something")
    t_max = sys.maxsize
    for i in range(pos[len(pos)//2],pos[-1]):
        t_val = 0
        c_v = i
        #print("------")
        #print(c_v)
        for j in pos:
            dif = abs(j-c_v)*((abs(j - c_v) + 1) // 2) 
            #this is just the sum of all natural numbers up to that point. Cost goes up by 1 
            # and increments as we go like n*(n+1)//2
            
        #    print(tv)
            t_val+=dif
        #print("----------")
        if t_val > t_max:
            return t_max    
        t_max = min(t_max,t_val)
    return t_max
    
#print(part1_F(pos)) This is wrong. I wonder why.  
x = part1_S(pos)
print(part1_S(pos))
pos.sort()
print(part2(x[0],x[1],pos))
