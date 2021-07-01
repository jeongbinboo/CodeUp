#문자를 16진수로 바꾸려면 int(n,16)  10진수를 16진수로 바꾸려면 %x로 출
n=input()
n=int(n,16)
for i in range(15):
    print('%X*%X=%X'%(n,i+1,n*(i+1)))
