n=int(input())
p=input().split()
password=[]
strange=[]

for i in range(n):
    password.append(int(p[i]))

for i in range(n):
    left=password[(i-1)%n]-password[i] if password[(i-1)%n]>password[i] else password[i]-password[(i-1)%n]
    right=password[(i+1)%n]-password[i] if password[(i+1)%n]>password[i] else password[i]-password[(i+1)%n]
    print('%d %d %d %d'%(i,password[i],left,right))
    if (left != 1 and left != (n-1)) or (right != 1 and right != (n-1)):
        strange.append(password[i])

print(strange)
strange.sort()
print(strange)
if strange[1]-strange[0]>1:
    
