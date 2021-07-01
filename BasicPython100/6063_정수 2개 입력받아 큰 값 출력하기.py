# x if C else y 의 형태로 3개의 요소로 이루어지는 3항 연산이 가능하다.

a,b=input().split(' ')
a=int(a)
b=int(b)
print(a if (a>=b) else b)
