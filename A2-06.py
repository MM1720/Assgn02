p=input("Enter the three sides ")
a,b,c=p.split(",")
a=int(a)
b=int(b)
c=int(c)
if a+b>c and b+c>a and c+a>b:
    print("YES")
else:
    print("NO")
