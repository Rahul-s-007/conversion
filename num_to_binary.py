#CONVERT NUMBER TO BINARY

n=int(input("ENTER A NUMBER:"))
d=n
b=""
c=0
if ((n%2)==0):
    b=b+"0"
if ((n%2)==1):
    b=b+"1"
while (d>1):
    d=d//2
    if ((d%2)==0):
        b=b+"0"
    if ((d%2)==1):
        b=b+"1"
binary=b[::-1]
print(n,"in base 2 =",binary)
print("WORKING :")
l=len(b)
for a in binary:
    x=int(a)
    l=l-1
    if (x==1):
        power=pow(2,(l))
        print("2^",(l),"=",power)
        c=c+power
print("SUM =",c)
    





    
