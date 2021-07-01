stu=[]
n=int(input())
check=input().split()

for i in range(n):
    stu.append(int(check[i]))
for i in range(n):
    print(stu[n-i-1],end=' ')
