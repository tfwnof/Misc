a=b=i=1
f=[]
while i<=100:
    f.append(a)
    f.append(b)
    i+=1
    a+=b
    b+=a
print(f)
