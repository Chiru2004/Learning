                           #TIC TAC TOE game
  
def sum(a,b,c):
    return a+b+c
def winner(x,y):
    wins=[[0,1,2],[3,4,5],[6,7,8],[0,3,6],[1,4,7],[2,5,8],[0,4,8],[2,4,6]]
    for win in wins:
       if sum(x[win[0]],x[win[1]],x[win[2]])==3:
           print(' X is the Winner!!!')
           return 1
       if sum(y[win[0]],y[win[1]],y[win[2]])==3:
           print(' Y is the Winner!!!')
           return 0
    return -1        
def mainboard(x,y):
    one='X' if x[0] else ('O' if y[0] else 0)
    two='X' if x[1] else ('O' if y[1] else 1)
    three='X' if x[2] else ('O' if y[2] else 2)
    four='X' if x[3] else ('O' if y[3] else 3)
    five='X' if x[4] else ('O' if y[4] else 4)
    six='X' if x[5] else ('O' if y[5] else 5)
    seven='X' if x[6] else ('O' if y[6] else 6)
    eight='X' if x[7] else ('O' if y[7] else 7)
    nine='X' if x[8] else ('O' if y[8] else 8)
    print(f'      {one} | {two} | {three} ')
    print('     ---|---|---')
    print(f'      {four} | {five} | {six} ')
    print('     ---|---|---')
    print(f'      {seven} | {eight} | {nine} ')

if __name__=="__main__":
    x=[0,0,0,0,0,0,0,0,0]
    y=[0,0,0,0,0,0,0,0,0]
    print("   WELCOME TO TIC TAC TOE  ")
    turn=1
    while(True):
        mainboard(x,y)
        if(turn==1):
           print("X's chance to PLAY")
           value=int(input("Enter your value please:"))
           x[value]=1
           
        else:
           print("Y's chance to PLAY")
           value=int(input("Enter your value please"))   
           y[value]=1
        count=winner(x,y)
        if count!=-1:
           mainboard(x,y)
           break
        turn=1-turn
        