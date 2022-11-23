with open('input.txt', 'r') as f:
    d = {}
    for line in f:
        l = list(map(str,line.split()))
        if(l[0] in d.keys()):
            d[l[0]] += int(l[1])
        else:
            d[l[0]] = int(l[1])
    l = sorted(d.keys())
    for k in l:
        print(k, d[k])
