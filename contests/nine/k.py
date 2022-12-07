n, k= map(int, input().split())
s = set()

for i in range(k):
    a,b = map(int,input().split())
    s1 = {i for i in range(a, n+1, b) if not(i%7 in (0,6))}
    s.update(s1)

print(len(s))