a, b, n = map(int, input().split())
a *= n
a += (b*n)//100
b = (b*n)%100
print(a,b)