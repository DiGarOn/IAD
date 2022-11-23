with open("input.txt") as f:
    d = {}
    for line in f:
        l = list(map(str,line.split()))
        for i in l:
            if(i in d.keys()):
                d[i] += 1
            else:
                d[i] = 1
    l = []
    for k in d.keys():
        l.append((d[k], k))
    print(l)
    l.sort(reverse=True)
    for i in l:
        print(i[1])