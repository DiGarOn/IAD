with open("input.txt") as f:
    d = {}
    s = 0
    count = 0
    digits = set("1234567890")
    for line in f:
        count += 1
        l = list(map(str,line.split()))
        name = ""
        for i in range(len(l)-1):
            name += l[i] + " "
        name = name[:len(name)-1]
        d[name] = int(l[-1])
        s += int(l[-1])
    s1 = 0
    l = []
    if s//450 != 0:
        for k in d.keys():
            l.append(((d[k]*450)%s, k))
            d[k] = (d[k]*450)//s
            s1 += d[k]
        l.sort(reverse=True)
    else:
        l = sorted([(d[k], k) for k in d.keys()],reverse=True)
        for k in d.keys():
            s1 += d[k]
    k = 0

    while (s1 < 450):
        d[l[k][1]] += 1
        s1 += 1
        k= (k +1)%count
    for k in d.keys():
        print(k, d[k])

