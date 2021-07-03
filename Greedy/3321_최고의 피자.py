n=int(input())
pod,pot=input().split()
pod=int(pod)
pot=int(pot)
cod=int(input())
cot=[]
price=pod
cal=cod
for i in range(n):
    topping=int(input())
    cot.append(topping)
cot.sort()
cot.reverse()

for i in range(n):
    pre=cal/price
    next=(cal+cot[i])/(price+pot)
    if next>pre:
        cal+=cot[i]
        price+=pot
    else:
        break
print('%d'%(cal/price))
