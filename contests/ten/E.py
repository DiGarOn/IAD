with open('input.txt', 'r') as f:
    d = {}
    for line in f:
        l = list(map(str,line.split()))
        for i in range(len(l)):
            if(l[i] in d.keys()):
                d[l[i]] += 1
            else:
                d[l[i]] = 1
    # print(d)
    l = []
    mi = 0
    for i in d.keys():
        if(d[i] == mi):
            l.append(i)
        elif d[i] > mi:
            # print("here")
            l.clear()
            mi = d[i]
            l.append(i)
    l = sorted(l)
    print(l[0])