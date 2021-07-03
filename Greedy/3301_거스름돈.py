price=int(input())
cnt=0

while price!=0:
    if price//50000>0:
        n=price//50000
        price-=n*50000
        cnt+=n
    elif price//10000>0:
        n=price//10000
        price-=n*10000
        cnt+=n
    elif price//5000>0:
        n=price//5000
        price-=n*5000
        cnt+=n
    elif price//1000>0:
        n=price//1000
        price-=n*1000
        cnt+=n
    elif price//500>0:
        n=price//500
        price-=n*500
        cnt+=n
    elif price//100>0:
        n=price//100
        price-=n*100
        cnt+=n
    elif price//50>0:
        n=price//50
        price-=n*50
        cnt+=n
    else:
        n=price//10
        price-=n*10
        cnt+=n
print(cnt)
