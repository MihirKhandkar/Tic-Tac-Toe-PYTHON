print("Welcome to Tic-Tac-Toe !!!!")
print(" ")
print("Here's the board:")
print("|1|2|3|\n|4|5|6|\n|7|8|9|")

a = " "
b = " "
c = " "
d = " "
e = " "
f = " "
g = " "
h = " "
i = " "
j = " "
index = [a,b,c,d,e,f,g,h,i]


def print_board():
   print("|",index[0],"|",index[1],"|",index[2],"|")
   print("|",index[3],"|",index[4],"|",index[5],"|")
   print("|",index[6],"|",index[7],"|",index[8],"|")


def check_winner():
    global count

    if(index[0]==index[1]==index[2]=="X" or
       index[3]==index[4]==index[5]=="X" or
       index[6]==index[7]==index[8]=="X" or
       index[0]==index[3]==index[6]=="X" or
       index[1]==index[4]==index[7]=="X" or
       index[2]==index[5]==index[8]=="X" or
       index[0]==index[4]==index[8]=="X" or
       index[2]==index[4]==index[6]=="X"):
         print("PLAYER 1 WINS")
         count+=1
    elif(index[0]==index[1]==index[2]=="O" or
       index[3]==index[4]==index[5]=="O" or
       index[6]==index[7]==index[8]=="O" or
       index[0]==index[3]==index[6]=="O" or
       index[1]==index[4]==index[7]=="O" or
       index[2]==index[5]==index[8]=="O" or
       index[0]==index[4]==index[8]=="O" or
       index[2]==index[4]==index[6]=="O"):
          print("PLAYER 2 WINS")
          count+=1

count = 0

for i in range (9):
    
    if i%2==0:
        m = int(input("Player 1 enter position: "))
        index[m-1] = "X"
        print_board()
        check_winner()
        if(count>0):
            break
              
    else:
        m = int(input("Player 2 enter position: "))
        index[m-1] = "O"
        print_board()
        check_winner()
        if(count>0):
            break

if(count==0):
    print("IT IS A DRAW")