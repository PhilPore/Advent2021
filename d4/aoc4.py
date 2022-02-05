import sys
from copy import deepcopy
bingos = []
with open("input.txt") as f:
    raw = f.read().strip()
    bingos = raw.split("\n")


    """
    
    YOUR BIG ISSUE WAS THAT YOU ACCOUNTED FOR DIAGONALS. READ THE DIRECTIONS

    Returns:
        [type]: [description]
    """


#num_seqs = [int(i) for i in bingos[0].split(",")]
num_seqs = [i for i in bingos[0].split(",")]
#bingos_p = bingos[2:]
boards = []
#print(num_seqs)
tmp = []
#all these boards are 5x5. We can parse
#elements = 0
for i in range(2,len(bingos)):
   if len(bingos[i]) == 0:
       boards.append(tmp)
       tmp = []
       continue
   #t_str = [int(j) for j in bingos[i].split()]
   t_str = [j for j in bingos[i].split()]
   tmp.append(t_str)

boards.append(tmp)
boards2 = deepcopy(boards)
#print(boards[-1])
#horizontal
def check_win(board):
    #rows
    for ro in board:
        xs = 0
        for col in range(len(ro)):
            if ro[col] == 'x':
                xs+=1
                
            if xs==5:
                return True
    #cols
    for col in range(len(board)):
        xs = 0
        for ro in board:
            if ro[col] == 'x':
                xs+=1
        
            if xs == 5:
                return True
    return False

def find_winner(board,num_seq):
    print("DO something")
    winner_found = False       
    #get first 5. Only way to determine a sequence first. Like a sliding window
    for i in range(len(num_seq)):
        #we needd to start marking the sequences. After the fifth num, we gotta check
        for b in board:
            marked = False
            mark_board(b,num_seq[i])
            if i >= 4:
                if check_win(b):
                    #we get the sum of nonmarked stuff
                    print("hahaha WINNER")
                    print(num_seq[i])
                    val = 0
                    #for ro in b:
                    #    print(ro)
                    val = sum_board(b)
                    #print(val)
                    #print(i)
                    print(val*int(num_seq[i]))
                    #print(b)
                    return
        
def mark_board(board,num_seq):
    for ro in range(len(board)):
        for col in range(len(board[0])):
            if num_seq == board[ro][col]:
                board[ro][col] = 'x'
                return  True
    return False
def sum_board(board):
    val = 0
    for ro in board:
        for col in range(len(ro)):
            if ro[col] != 'x':
                val+=int(ro[col])
    return val
    
def find_squid_win(boards, num_seq):
    winner_found = False
    for i in range(len(num_seq)):
        
        
        for board in boards:
            mark_board(board,num_seq[i])
        
        ind = 0
        while ind < len(boards):

            if check_win(boards[ind]):
                if len(boards) > 1:
                    boards.pop(ind)
                
                else:
                    return sum_board(boards[ind])*int(num_seq[i])

                #print(boards[ind])
    
            else:
                ind+=1
            
            





find_winner(boards,num_seqs)
#print(boards2[0])
print(find_squid_win(boards2,num_seqs))