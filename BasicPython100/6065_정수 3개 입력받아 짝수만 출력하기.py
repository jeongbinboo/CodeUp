a,b,c=input().split(' ')
num=[]
num.append(int(a))
num.append(int(b))
num.append(int(c))

for i in num:
    if i%2==0:
        print(i)
