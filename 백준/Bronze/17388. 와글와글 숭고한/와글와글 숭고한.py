a, b, c = map(int,input().split())

if a+b+c>=100:
    print("OK")
elif a+b+c<100 and a<b and a<c:
    print("Soongsil")
elif a+b+c<100 and b<a and b<c:
    print("Korea")
else:
    print("Hanyang")
