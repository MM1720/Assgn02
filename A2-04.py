a=int(input("Enter number "))
b=int(input("Enter number "))
c=int(input("Enter number "))
#print(max(a,b,c),"is grearer
if a>b:
    if c>a:
        print("c=",c,"is greater")
    elif a==c:
        print("a=c=",a,"is greater")
    else:
        print("a=",a,"is greater")
elif a==b:
    if c>b:
        print("c =",c,"is greater")
    elif c<b:
        print("a=b=",b,"is greater")
    else:
        print("a=b=c=",b,"and all are equal")
else:
    if c>b:
        print("c=",c,"is greater")
    elif c==b:
        print("b=c=",b,"is greater")
    else:
        print("b=",b,"is greater")
