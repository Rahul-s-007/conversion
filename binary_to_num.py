#BINARY TO NUMBER

b=str(input("ENTER THE BINARY :"))
l=len(b)
c=0
for a in b:
    x=int(a)
    l=l-1
    if (x==1):
        power=pow(2,(l))
        print("2^",(l),"=",power)
        c=c+power
print("SUM =",c)