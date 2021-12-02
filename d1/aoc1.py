#import sys

f = open('test.txt')
r = f.readlines()
print(len(r))
incr = 0
prev = None

#a better solution for part 2 would just be to compare num[i] and num[i+3] as 
# you'll be removing this value and replacing it with with nums[i+3], so an increase hinges on that  
x = 0
for i in range(len(r)-3):
    x = i
    incr+=1 if int(r[i+3]) > int(r[i]) else 0
print(incr)
print(x)

"""
window = []
for i in range(3):
    window.append(int(r[i].strip()))
print(window)
cur_sum = sum(window)
t_sum = cur_sum
last_ind = 0
for cur in range(3,len(r)):
    
    
    
    c = int(r[cur].strip())
    t_sum-= int(r[last_ind].strip())
    last_ind+=1
    t_sum+=c
    #window.append(c)
    #print(t_sum)
    #print(cur_sum)
    #break
    if t_sum > cur_sum:
        incr+=1
    cur_sum = t_sum
print(incr)        
"""



"""
for cur in r:
    c = int(cur.strip())
    if prev == None:
        prev = c
        continue
    if prev < c:
        incr+=1
    prev = c

print(incr)
        
"""    