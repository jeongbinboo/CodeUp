# 삼항연산을 괄호를 이용하여 중첩하여 사용이 가능하다.
a,b,c=input().split(' ')
a=int(a)
b=int(b)
c=int(c)
d= (a if a<b else b) if (a if a<b else b)<c else c
print(d)
