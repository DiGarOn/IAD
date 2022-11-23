from functools import cache

d = {}

@cache
def func (name:str, s:frozenset):
    global d
    if(name in s):
        return 1 + func(d[name], s)
    else:
        return 0


with open("input.txt") as f:
    n = int(f.readline())
    d = {}
    s = set()
    s1 = set()
    for i in range(n-1):
        a, b = map(str,f.readline().split())
        d[a] = b
        s1.update([a])
        s1.update([b])
        s.update([a])
    r = frozenset(s)
    s1 = sorted(s1)
    for i in s1:
        print(i, func(i,r))