parsed = []
inp = "input.txt"
dev = "test.txt"
with open(inp) as f:
    raw = f.read().strip()
    parsed = raw.split("\n")
    
    
#count all lantern fish

def go_thru_lst(lst):
    for i in range(len(lst)):
        if lst[i] == 0:
            lst[i] = 6
            lst.append(8)
            continue
        lst[i]-=1

def p1_get_num(period,fishes):
    for i in range(period):
        go_thru_lst(fishes)
    return len(fishes)

def update_list(fishes):
    #generate a list. We only need to worry about 0 to 8. SO we just build a list o size 9 and 
    # move numbers down as well as add to 8 when the 0 counter is filled. THis will ensure we account for the new fish being spanned
    #basically, these are all counters for each stage that we adjust after each period of time.
    upd_8 = 0
    mov_fishes = 0
    for i in range(8):
        if fishes[i] > 0:
            mov_fishes = fishes[i]
            fishes[i] = 0
            if i == 0:
                upd_8 = mov_fishes
                continue
            fishes[i-1] += mov_fishes                
    #print(fishes)
    #print("++++")
    fishes[7]+=fishes[8]
    fishes[8]= 0
    fishes[8]+=upd_8
    fishes[6]+=upd_8
    #print(fishes)
    #print("===")
        
    
    
def p2_runtime(period,fishes):
    #use our generated list to do increments. We cna do a constant time indexing
    # its actually fucking fire rn. We dont need to worry about 8 and 7 until last
    
    
    generated = [0 for i in range(9)]
    for i in fishes:
        generated[i]+=1
    print(generated)

    for i in range(period):
        update_list(generated)
                
    print(sum(generated))
        

fish =[int(i) for i in parsed[0].split(',')]
#print(p1_get_num(80,fish))
print(fish)
p2_runtime(256,fish)