n=i=1
l=p=[]
while n<=1000:
    while i<=n:
        if n%i==0:
            l.append(n)
            if i<n:
                i+=1
            else:
                i=2
                if len(l)==1:
                    p.append(n)
                l=[]
                break
        elif n!=i and i<n:
            i+=1
    n+=1
print(p)
