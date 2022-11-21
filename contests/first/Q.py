s = int(input())
m = s//60
h = m//60
h = h%24
m = m%60
s = s%60
res = "{0}:".format(h)
if(m < 10):
    res += "0{0}".format(m)
else:
    res += str(m)
res += ":"
if(s < 10):
    res += "0{0}".format(s)
else:
    res += str(s)

print(res)
