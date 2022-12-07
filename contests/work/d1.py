d = []
k = -1
with open("input.txt", "r", encoding = "utf-8") as f:
    k = int(f.readline())
    for i in f.readlines():
        a = i.replace("\n", "").split()
#         print(a)
        score1 = int(a[-3])
        score2 = int(a[-2])
        score3 = int(a[-1])
        if score1 >= 40 and score2 >= 40 and score3 >= 40:
            d.append(score1 + score2 + score3)
sorted(d)[::-1]
# print(d)
if len(d) <= k:
    print(0)
elif d[0] == d[k]:
    print(1)
else:
    res = 0
    for i in range(len(d)-1):
        if((d[i] != d[i+1]) and i+1 <= k):
            res = d[i]
    print(res)