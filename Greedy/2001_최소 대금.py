p1=int(input())
p2=int(input())
p3=int(input())
j1=int(input())
j2=int(input())

p=(p1 if p1<p2 else p2) if (p1 if p1<p2 else p2)<p3 else p3
j=j1 if j1<j2 else j2

print('%.1f'%(p+j+(p+j)*0.1))
