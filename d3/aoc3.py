# COME BACK AND REFACTOR THIS SHIT

bindig = []
with open("input.txt") as f:
    raw = f.read().strip()
    bindig = raw.split("\n")
    
ro_len = len(bindig)
col_len = (len(bindig[0]))


def part1(bindig: list,ro_len: int,col_len: int):
    #effectively find the most common binary bits for each column
    gamma = "" #most common
    epsilon = "" #least common
    for c in range(col_len):
        ones = 0
        zeds = 0
        #so what we can notice is that as soon as the amount of 
        # 2*something is >= our ro_len, thats our most common
        for r in range(ro_len):
            if bindig[r][c] == "1":
                ones+=1
            else:
                zeds+=1
        if ones > zeds:
            gamma+="1"
            epsilon+="0"
        elif zeds > ones:
            gamma+="0"
            epsilon+="1"
    
    print(gamma)
    print(epsilon)
    print("---")
    print(int(gamma,2)*int(epsilon,2))
    return [gamma,epsilon]


def get_zo_diff(lst,ind):
    z = 0
    o = 0
    for seq in lst:
        if seq[ind] == "1":
            o+=1
        else:
            z+=1
    return (o,z)

def part2(gamma,epsilon,bindig):
    #print("Do something")
    o2 = list(bindig)
    co2 = list(bindig)
    gamma_1 = ""
    g2 = ""
    epsilon_1 = ""
    e2 = ""
    for i in range(len(bindig[0])):
        o = get_zo_diff(o2,i)
        #print(o)
        c = get_zo_diff(co2,i)
        #print(c)
        gamma_1 = "1" if o[0] >= o[1] else "0"
        epsilon_1 = "0" if c[1] <= c[0] else "1"
        g2+=gamma_1
        e2+=epsilon_1
        #print("{} | {}".format(gamma_1,epsilon_1))
        
        if len(o2) > 1:
            #do something
            o2 = [v for v in o2 if v[i] == gamma_1]
        if len(co2) > 1:
            #do something
            co2 = [v for v in co2 if v[i] == epsilon_1]
    
    print(o2)
    print(co2)
    print(int(o2[0],2)*int(co2[0],2))
    return [g2, e2]
        
    #print(o2)
def a_p2(bindig) -> int: #Andrews
    values = bindig
    k = len(values[0])
    oxy = list(values)
    co2 = list(values)

    for i in range(k):
        g = ""
        e = ""
        oxy_common = "1" if 2 * sum(int(v[i]) for v in oxy) >= len(oxy) else "0"
        co2_common = "1" if 2 * sum(int(v[i]) for v in co2) >= len(co2) else "0"
        print("{}|{}".format(oxy_common,co2_common)) #This was really cool. Andrew treated it like two gammas
        
        if len(oxy) > 1:
            oxy = [v for v in oxy if v[i] == oxy_common]
        if len(co2) > 1:
            co2 = [v for v in co2 if v[i] != co2_common] #as long as its not the common, aka epsilon
    print("{} {}".format(g, e))
    return int(oxy[0], base=2) * int(co2[0], base=2)
    
def main():
    x1 = part1(bindig,ro_len,col_len)
    x2 = part2(x1[0],x1[1],bindig)
    #a_p2(bindig)
    print(x2)

if __name__ == "__main__":
    main()  
'''
m = len(bindig)
n = len(bindig[0])
gamma = ""
epsilon =""
print(type(bindig[1][0]))
for i in range(n):
    
    ones = 0
    zero = 0
    seq = 0
    for j in range(m):
        if bindig[j][i] == "1":
            ones+=1
        else:
            zero+=1
    
    #print(ones)
    #print(zero)
    #print("---")
    if ones > zero:
        gamma+="1"
        epsilon+="0"
    else:
        gamma+="0"
        epsilon+="1"
        
    #print("---")
print(gamma)
print(epsilon)
print(int(gamma,2)*int(epsilon,2))

O_g = []
Co = []
#for i in range(len(gamma)):
for j in bindig:
    if j[0] == gamma[0]:
        O_g.append(j)
    elif j[0] == epsilon[0]:
        Co.append(j)
#print(O_g)
#print(Co)
for i in range(1,len(gamma)):
    if len(O_g) == 1:
        break
    ind = 0
    one = 0
    z = 0
    for r in range(len(O_g)):
        if O_g[r][i] == "1":
            one+=1
        else:
            z+=1
    #print(one)
    #print(z)
    prune = "1" if z <= one else "0"
    buffer = []
    for li in O_g:
        if li[i] == prune:
            buffer.append(li)
    O_g = buffer

#print(Co)
#print(len(Co))
#print(Co)
for i in range(1,len(epsilon)):
    if len(Co) == 1:
        break
    ind = 0
    one = 0
    z = 0
    for r in range(len(Co)):
        if Co[r][i] == "1":
            one+=1
        else:
            z+=1
    #print(one)
    #print(z)
    #print("---")
    prune = "0" if z <= one else "1"
    buffer = []
    for li in Co:
        if li[i] == prune:
            buffer.append(li)
    Co = buffer
#print(Co)

print(int(Co[0],2)*int(O_g[0],2))           
            
#print(O_g)
#print(O_g)
         
    
'''