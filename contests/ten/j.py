with open("input.txt") as f:
    d = {}
    s = 0
    digits = "1234567890"
    for line in f:
        l = list(map(str,line.split()))
        index = 0
        for i in range(len(l)):
            if l[i][0] in digits:
                index = i
                break
        name = ""
        for i in range(index):
            name += l[i] + " "
        name = name[:len(name)-1]
        d[name] = int(l[index])
        s += int(l[index])
    n = s//450
    s1 = 0
    l = []
    if n != 0:
        for k in d.keys():
            l.append((d[k]%n, k))
            d[k] = d[k]//n
            s1 += d[k]
        l.sort(reverse=True)
    else:
        l = sorted(d.values(),reverse=True)
    k = 0
    while (s1 < 450):
        d[l[k][1]] += 1
        s1 += 1
        k+=1
    for k in d.keys():
        print(k, d[k])

