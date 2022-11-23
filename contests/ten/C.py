n = int(input())
d = {}
for i in range(n):
    a,b = map(str, input().split())
    d[a] = b
    d[b] = a
c = input()
print(d[c])