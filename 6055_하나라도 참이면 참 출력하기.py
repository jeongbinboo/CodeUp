# or 예약어는 두 불 값 중에서 하나라도 True이면 True로 계산하고 나머지 경우는 False로 계산
a,b=input().split(' ')
a=int(a)
b=int(b)
print(bool(a or b)) # print(a or b)를 하게 되면 True가 아닌 1 이 출력

