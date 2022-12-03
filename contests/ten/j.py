with open("input.txt") as f:
    d = {}
    s = 0
    count = 0
    digits = set("1 2 3 4 5 6 7 8 9 0".split())
    for line in f:
        count += 1
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

