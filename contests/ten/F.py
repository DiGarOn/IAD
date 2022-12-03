with open("input.txt") as f:
    d = {}
    for line in f:
        l = list(map(str,line.split()))
        for i in l:
            if(i in d.keys()):
                d[i] += 1
            else:
                d[i] = 1

    d1 = {}
    for k in d.keys():
        if(d[k] in d1.keys()):
            d1[d[k]].append(k)
        else:
            d1[d[k]] = [k]
    l = sorted(d1.keys(), reverse=True)
    # print(l)
    for i in l:
        print("\n".join(sorted(d1[i])))