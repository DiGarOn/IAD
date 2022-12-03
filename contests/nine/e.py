# ok
n,m = map(int,input().split())
a = set()
b = set()
for i in range(n):
    a.update(set([int(input())]))
for i in range(m):
    b.update(set([int(input())]))
c = a.intersection(b)
a.difference_update(c)
b.difference_update(c)

print(len(c))
print(*sorted(c))
print(len(a))
print(*sorted(a))
print(len(b))
print(*sorted(b))