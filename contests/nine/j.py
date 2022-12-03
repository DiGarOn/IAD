l = list(map(int,input().split()))
s1 = {i for i in range(min(l[0],l[1]), max(l[0],l[1]) + 1)}
s2 = {i for i in range(min(l[2],l[3]), max(l[2],l[3]) + 1)}

# print(s1)
# print(s2)

print(len(s1.intersection(s2)))