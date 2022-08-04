# Problem 2

a,b,c = 1,2,0
while c <= 4000000:
    if a%2==0:
        c += a
    elif b%2==0:
        c += b
    a += b
    b += a
print(c)
