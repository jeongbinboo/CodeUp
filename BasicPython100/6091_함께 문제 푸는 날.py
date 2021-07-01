a,b,c=input().split()
a=int(a)
b=int(b)
c=int(c)

res=1
while res%a!=0 or res%b!=0 or res%c!=0:
    res+=1
print(res)
