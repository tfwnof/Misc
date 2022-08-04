# Problem 2
# Even Fibonacci numbers
# By considering the terms in the Fibonacci sequence whose values do not exceed four million, find the sum of the even-valued terms.

a,b,c = 1,2,0
while c <= 4000000:
    if a%2==0:
        c += a
    elif b%2==0:
        c += b
    a += b
    b += a
print(c)
