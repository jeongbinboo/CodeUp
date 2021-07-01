n=int(input())
check=input().split()
for i in range(n):
    check[i]=int(check[i])
check.sort()
print(check[0])
