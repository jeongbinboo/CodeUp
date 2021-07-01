n=int(input())
check=input().split()

stu=[]
for i in range(23):
    stu.append(0)

for i in range(n):
    stu[int(check[i])-1]+=1
for i in range(23):
    print(stu[i],end=' ')
