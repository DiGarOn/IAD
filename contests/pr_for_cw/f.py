import functools

n = int(input())
l = []
for i in range(n):
    l.append(input())
gl = set("a e i o u".split())

def count_gl(a:str):
    global gl
    s = 0
    for i in a:
        if i in gl:
            s += 1
    return s

def compare(a, b):
    s1 = count_gl(a)
    s2 = count_gl(b)
    if(s1 > s2):
        return -1
    elif s1 < s2:
        return 1
    else:
        if(len(a) < len(b)):
            return -1
        elif (len(a) > len(b)):
            return 1
        else:
            return 0
l.sort(key=functools.cmp_to_key(compare))
for i in l:
    print(i)