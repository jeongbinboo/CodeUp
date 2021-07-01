h,w=input().split()
arr=[]
for i in range(int(h)):
    arr.append([0]*int(w))
        
n=int(input())
for i in range(n):
    l,d,x,y=input().split()
    l=int(l)
    d=int(d)
    x=int(x)
    y=int(y)
    for j in range(l):
        arr[x-1][y-1]=1
        if d==0:
            y+=1
        else:
            x+=1
for i in range(int(h)):
    for j in range(int(w)):
        print(arr[i][j],end=' ')
    print()
    
