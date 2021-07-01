# and 예약어는 주어진 두 불 값이 모두 True 일 때만 True로 계산하고 나머지는 False로 계산한다.
a,b=input().split(' ')
a=int(a)
b=int(b)
print(bool(a and b))
