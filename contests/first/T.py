n = int(input())
m = int(input())

r = m//n
m = m - n*(m//n)
if(m > 0):
    r+=1

print(r)