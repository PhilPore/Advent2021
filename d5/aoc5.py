vents = []
inp = "input.txt"
dev = "test.txt"
with open(inp) as f:
    raw = f.read().strip()
    vents = raw.split("\n")
    
#print(vents)
vents_lst = [] #a list of tuple pairs (x1,y1), (x2, y2)
max_val = 0
for i in vents:
    parse = i.split(" -> ")
    buffer = []
    for j in parse:
        x = j.split(",")
        buffer.append((int(x[0]),int(x[1])))
        t_val = max(int(x[0]),int(x[1]))
        max_val = max(t_val,max_val)
    vents_lst.append(buffer)

#print(vents_lst)
#for i in vents_lst:
#    print(i)    

def build_horiz_vert(vents_lst):
    #return a lst of only horizontal and vertical lines
    res = []
    diags = []
    for vent in vents_lst:
        if vent[0][0] != vent[1][0] and vent[0][1] != vent[1][1]:
            diags.append(vent)
            continue
        res.append(vent)
    return (res,diags)
def build_p2(vents_lst):
    res = []
    for vent in vents_lst:
        if vent[0][0] == vent[1][0] or vent[0][1] == vent[1][1]:
            res.append(vent)
        elif abs(vent[0][0]-vent[1][0]) == abs(vent[0][1]-vent[1][1]):
            res.append(vent) 
    return res
def handle_hor(tup_pair, tup_list,ind,grid):
    cross_lst = []
    #horizontal
    #print("Cur {}".format(tup_pair))
   
    for cur in range(ind,len(tup_list)):
        parse = tup_list[cur]
        x_start = max(parse[0][0],tup_pair[0][0])
        x_end = min(parse[1][0],tup_pair[1][0])
        #print("{} | {} {} | {} {}".format(parse,parse[0][1],tup_pair[0][1],parse[1][1],tup_pair[1][1] ))
        if parse[0][1] == tup_pair[0][1] and parse[1][1] == tup_pair[1][1]:
            #print(parse)
            #print(tup_pair)
            #print("---")
            if x_start <= x_end:
                #print("Value in range")
                cross_lst.append(parse)
                if parse[0][1] not in grid:
                    grid[parse[0][1]] = set()
                for s in range(x_start,x_end+1):
                    grid[parse[0][1]].add(s)
                            
                    #print("{} {}".format(x_start,y_start))
        elif (parse[1][1] != parse[0][1]):
            #print("hey, potential overlap with x-y")
            #print("{}|  {} =?= {}".format(parse,max(parse[0][1],tup_pair[0][1]),min(parse[1][1],tup_pair[1][1])))
            #print("{} {}".format(x_start,x_end))
            if (max(parse[0][1],tup_pair[0][1]) == min(parse[1][1],tup_pair[1][1])):
                if x_start <= x_end:
                    #print("Value in cross range {}".format(parse))
                    cross_lst.append(parse)
                    if tup_pair[0][1] not in grid:
                        grid[tup_pair[0][1]] = set()
                    for s in range(x_start,x_end+1):
                        grid[tup_pair[0][1]].add(s)

def handle_vert(tup_pair, tup_list,ind,grid):
    cross_lst = []
    for cur in range(ind,len(tup_list)):
        parse = tup_list[cur]

        y_start =  max(parse[0][1],tup_pair[0][1])
        y_end = min(parse[1][1],tup_pair[1][1])
        if (parse[0][0] == tup_pair[0][0] and parse[1][0] == tup_pair[1][0]):
                #overlap of verticals
                #print("V-O {} --- {} -> {}".format(parse, y_start, y_end))
                #print(dif)
                #print("***")
            if y_start <= y_end:
                cross_lst.append(parse)
                for i in range(y_start,y_end+1):
                    if i not in grid:
                        grid[i] = set()
                        #if parse[0][0] not in grid[i]:
                    grid[i].add(parse[0][0])
        elif (parse[0][0] != parse[1][0]):
            if (max(parse[0][1],tup_pair[0][1]) == min(parse[1][1],tup_pair[1][1])):
                y_cord = min(parse[1][1],tup_pair[1][1])
                x_start = max(parse[0][0],tup_pair[0][0])
                x_end = min(parse[1][0],tup_pair[1][0])
                if y_cord not in grid:
                    grid[y_cord] = set()
                if x_start <= x_end:
                    #print("Y overlap found")
                    cross_lst.append(parse)
                    for i in range(x_start,x_end+1):
                        grid[y_cord].add(i)

''' 
def find_in_range(tup_pair, tup_list,ind,grid): 
    #we could send in the tup_pair[i] and tup_list[i+1:] but I dont like the pythonic way
    #Plan: Run tup_pair down tup_list[ind:] and see if we find overlaps. 
    # If yes, we increment, and mark the zones overlapped. Can be handled by an explored dictionary (this is to avoid re-marking the same range) 
    print("Do something")
    cross_lst = []
    #horizontal
    print("Cur {}".format(tup_pair))
   
    for cur in range(ind,len(tup_list)):
        parse = tup_list[cur]
        if tup_pair[0][1]  == tup_pair[1][1]: #a horizontal
            x_start = max(parse[0][0],tup_pair[0][0])
            x_end = min(parse[1][0],tup_pair[1][0])
            #print("{} | {} {} | {} {}".format(parse,parse[0][1],tup_pair[0][1],parse[1][1],tup_pair[1][1] ))
            if parse[0][1] == tup_pair[0][1] and parse[1][1] == tup_pair[1][1]:
                #print(parse)
                #print(tup_pair)
                #print("---")
                if x_start <= x_end:
                    #print("Value in range")
                    cross_lst.append(parse)
                    if parse[0][1] not in grid:
                        grid[parse[0][1]] = set()
                    for s in range(x_start,x_end+1):
                        grid[parse[0][1]].add(s)
                            
                    #print("{} {}".format(x_start,y_start))
            elif (parse[1][1] != parse[0][1]):
                #print("hey, potential overlap with x-y")
                #print("{}|  {} =?= {}".format(parse,max(parse[0][1],tup_pair[0][1]),min(parse[1][1],tup_pair[1][1])))
                #print("{} {}".format(x_start,x_end))
                if (max(parse[0][1],tup_pair[0][1]) == min(parse[1][1],tup_pair[1][1])):
                    if x_start <= x_end:
                        #print("Value in cross range {}".format(parse))
                        cross_lst.append(parse)
                        if tup_pair[0][1] not in grid:
                            grid[tup_pair[0][1]] = set()
                        for s in range(x_start,x_end+1):
                            grid[tup_pair[0][1]].add(s)
                    
               
                #print(parse)
                #print("-*-")
        elif tup_pair[0][0]  == tup_pair[1][0]:
            #print("Vert {}".format(parse))
            #dif = (parse[0][0]+parse[1][0])
            #print(dif)
            #print("***")
            y_start =  max(parse[0][1],tup_pair[0][1])
            y_end = min(parse[1][1],tup_pair[1][1])
            if (parse[0][0] == tup_pair[0][0] and parse[1][0] == tup_pair[1][0]):
                #overlap of verticals
                #print("V-O {} --- {} -> {}".format(parse, y_start, y_end))
                #print(dif)
                #print("***")
                if y_start <= y_end:
                    cross_lst.append(parse)
                    for i in range(y_start,y_end+1):
                        if i not in grid:
                            grid[i] = set()
                        #if parse[0][0] not in grid[i]:
                        grid[i].add(parse[0][0])
            elif (parse[0][0] != parse[1][0]):
                if (max(parse[0][1],tup_pair[0][1]) == min(parse[1][1],tup_pair[1][1])):
                    y_cord = min(parse[1][1],tup_pair[1][1])
                    x_start = max(parse[0][0],tup_pair[0][0])
                    x_end = min(parse[1][0],tup_pair[1][0])
                    if y_cord not in grid:
                        grid[y_cord] = set()
                    if x_start <= x_end:
                        #print("Y overlap found")
                        cross_lst.append(parse)
                        for i in range(x_start,x_end+1):
                            grid[y_cord].add(i)
                      
    #print(cross_lst)
'''   

def p1_handle(vents,grid):
    overlaps = 0
    for cur in range(len(vents)):
        parse = vents[cur]
        if parse[0][1] == parse[1][1]:
            #a horizontal
            for i in range(parse[0][0],parse[1][0]+1):
                if grid[parse[0][1]][i] < 0:
                    continue
                grid[parse[0][1]][i]+=1 
                if grid[parse[0][1]][i] > 1:
                    overlaps+=1
                    grid[parse[0][1]][i] = -1
                    
                    
        else:
            for i in range(parse[0][1],parse[1][1]+1):
                if grid[i][parse[0][0]] < 0:
                    continue
                grid[i][parse[0][0]]+=1
                if grid[i][parse[0][0]] > 1:
                    overlaps+=1
                    grid[i][parse[0][0]] = -1
        
    return overlaps
                    
def p2_diag(lst,grid,cur_olaps):
    act_lstx = [1,-1]
    act_lsty = [1,-1]
    xy = [0,0]
    for diag in lst:
        #xy_0 = x | xy_1 = y
        if ((diag[0][1] < diag[1][1]) and (diag[0][0] < diag[1][0])):
            xy[0],xy[1] = 0,0
        elif ((diag[0][1] < diag[1][1]) and (diag[0][0] > diag[1][0])):
            xy[0],xy[1] = 1,0
        elif ((diag[0][1] > diag[1][1]) and (diag[0][0] < diag[1][0])):
            xy[0],xy[1] = 0,1
        else:
            xy[0],xy[1] = 1,1
        #print("{}\n==\n{}\n==\n{}\n".format(diag,xy,act_lstx))
        #x,y = 0,0
        #print(diag)
        #print("{} {}".format(act_lstx[xy[0]],act_lsty[xy[1]]))
        #print("=^=")
        #print(abs(diag[0][0]-diag[1][0]))
        #print("=v=")
        point = [diag[0][0],diag[0][1]]
        for i in range(abs(diag[0][0]-diag[1][0])+1):
            #print("y-{} | x-{}".format(point[1],point[0]))
            if grid[point[1]][point[0]] < 0:
                point[0]+=act_lstx[xy[0]]
                point[1]+=act_lsty[xy[1]]
                continue
            grid[point[1]][point[0]]+=1
            if grid[point[1]][point[0]] > 1:
                cur_olaps+=1
                grid[point[1]][point[0]] = -1
            point[0]+=act_lstx[xy[0]]
            point[1]+=act_lsty[xy[1]]
        #print("****")
    return cur_olaps
            
            
                
#print(len(vents_lst))
filtered_vents,diag_vents = build_horiz_vert(vents_lst)
#print(filtered_vents)
#f2_lst = build_p2(vents_lst)
#print("=========")
#for i in filtered_vents:
#    print(i)
#print(len(vents_lst))
#print(len(filtered_vents))

#filtered_vents.sort(key= lambda x: x[1][1])
#print(len(filtered_vents))
#print(len(f2_lst))
#print("--")
#print(max_val)
grid = [[0 for i in range(max_val+1)] for _ in range(max_val+1)]

#print("--")
for ind,i in enumerate(filtered_vents):
    if i[1][0] < i[0][0] or i[1][1] < i[0][1]:
        filtered_vents[ind][0],filtered_vents[ind][1] = filtered_vents[ind][1],filtered_vents[ind][0] 
    
#print(filtered_vents)   
x = p1_handle(filtered_vents,grid)
print(x)
#for i in grid:
#    print(i)
p2 = p2_diag(diag_vents,grid,x)
print(p2)




    #print(i)
#for vent in filtered_vents:
#    print(vent)
#test = [[(2,1), (2,2)],[(2,2),(2,4)],[(0,2),(4,2)],[(2,5),(2,9)],[(3,2), (9,2)]]
#test = [
#[(3, 4), (9, 4)],
#[(0, 0), (0, 4)],
#[(7, 0), (7, 4)],
#[(0, 9), (2, 9)],
#[(1, 4), (3, 4)]
#]

#find_in_range(filtered_vents[1],filtered_vents,2)



""""
olap = {}
gref = {}
for i in range(len(filtered_vents)):
    #find_in_range(filtered_vents[i],filtered_vents,i+1,olap)
    x = filtered_vents[i]
    if x[0][1]  == x[1][1]:
        handle_hor(filtered_vents[i],filtered_vents,i+1,gref)
    elif x[0][0]  == x[1][0]:
        handle_vert(filtered_vents[i],filtered_vents,i+1,gref)

#find_in_range(filtered_vents[0],filtered_vents,1,olap)
#val = 0
#for key in olap:
#    val+=len(olap[key])
#    #print("{}:{} - {}".format(key,len(olap[key]),olap[key]))
#print(val)
v2 = 0
for key in gref:
    v2+=len(gref[key])
print(v2)
"""