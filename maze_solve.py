import numpy as np
import random
cx=[0,0,1,-1]
cy=[1,-1,0,0]
solution = [[(0,0) for i in range(30)] for j in range(30)]
arr = []
def check_valid(x,y,n):
    if x>=1 and x<=n and y>=1 and y<=n:
        return 1;
    else:
        return 0;
def dig(x,y,H,V,visit,n):
    visit[x][y]=1
    print(x,y)
    t=random.randint(0,4)
    for i in range(0,4):
        if check_valid(x+cx[t%4],y+cy[t%4],n) and visit[x+cx[t%4]][y+cy[t%4]]==0:
            if (t%4)<=1:
                H[x+cx[t%4]][min(y,y+cy[t%4])]=0
            else:
                V[y+cy[t%4]][min(x,x+cx[t%4])]=0
            H,V=dig(x+cx[t%4],y+cy[t%4],H,V,visit,n)
        t+=1
    return H,V
    
def make_maze(n):
    H = np.ones( (n+1,n+1) ,dtype=np.int32)
    V = np.ones( (n+1,n+1) ,dtype=np.int32)
    visit = np.zeros( (n+1,n+1) ,dtype=np.int32)
    H,V=dig(1,1,H,V,visit,n)
    return H,V

def print_maze(H,V,n):
    k=n
    l=n
    file1 = open("maze.txt", "w")
    for i in range(0,2*n+1):
        if i%2==0:
            t=1
            for j in range(0,2*n+1):
                if j%2==1:
                    if H[t][k]==0:
                        print(" ",end="")
                        file1.write(" ")
                    else:
                        print("-",end="")
                        file1.write("-")
                    t+=1
                else:
                    print("+",end="")
                    file1.write("+")
            k-=1
        else:
            t=0
            for j in range(0,2*n+1):
               if j%2==0:
                   if V[l][t]==0:
                       print(" ",end="")
                       file1.write(" ")
                   else:
                       print("|",end="")
                       file1.write("|")
                   t+=1
               else:
                   print(" ",end="")
                   file1.write(" ")
            l-=1
        print()
        file1.write("\n")
    file1.close()


n=int(input("Enter the value of n: "))
H,V=make_maze(n)
print(H)
print(V)
print_maze(H,V,n);
for i in range(1,n+1):
    for j in range(1,n+1):
        print(solution[i][j],end=" ")
    print()

#Drawing Maze with Matplotlib
import matplotlib.pyplot as plt
maze = []
with open("maze.txt", 'r') as file:
    for line in file:
        line = line.rstrip()
        row = []
        mat = []
        for c in line:
            if c == ' ':
                row.append(1) # spaces are 1s
                mat.append(2)
            #elif c == '^':
            #    row.append(2) # minus are 2s
            else:
                row.append(0) # walls are 0s
                mat.append(0)
        maze.append(row)
        arr.append(mat)

#find solution to maze
print(arr)
flg=0
def find_path(x,y):
    global flg
    visit[x][y]=1
    if flg or (x==len(arr[0])-2 and y==len(arr[0])-2):
        flg=1
        return;
    for i in range(0,4):
        if arr[x+cx[i]][y+cy[i]]==2 and visit[x+cx[i]][y+cy[i]]==0:
            solution[x+cx[i]][y+cy[i]]=(x,y)
            find_path(x+cx[i],y+cy[i]);
            
visit = np.zeros( (30,30) ,dtype=np.int32)
find_path(1,1)
x=len(arr[0])-2
y=len(arr[0])-2
while x!=1 or y!=1:
    arr[x][y]=1
    (x,y)=solution[x][y];
arr[x][y]=1
print(arr)

#Plot random maze
plt.title('Random Maze', fontweight ="bold") 
plt.pcolormesh(maze)
plt.axes().set_aspect('equal') #set the x and y axes to the same scale
plt.xticks([]) # remove the tick marks by setting to an empty list
plt.yticks([]) # remove the tick marks by setting to an empty list
plt.axes().invert_yaxis() #invert the y-axis so the first row of data is at the top
plt.show()

#Plot random maze solution
plt.title('Random Maze solution', fontweight ="bold") 
plt.pcolormesh(arr)
plt.axes().set_aspect('equal') #set the x and y axes to the same scale
plt.xticks([]) # remove the tick marks by setting to an empty list
plt.yticks([]) # remove the tick marks by setting to an empty list
plt.axes().invert_yaxis() #invert the y-axis so the first row of data is at the top
plt.show()
