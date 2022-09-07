n = int(input())
s = 0
res = ""
for i in range(2, n+1):
    res += str(i-1) + "*" + str(i) + "+"
    s += i*(i-1)
res = res[:len(res)-1]
res += "=" + str(s)
print(res)