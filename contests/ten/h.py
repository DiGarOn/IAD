with open("input.txt") as f:
    d = {}
    for line in f:
        l = list(map(str, line.split()))
        if(l[0] in d.keys()):
            if(l[1] in d[l[0]].keys()):
                d[l[0]][l[1]] += int(l[2])
            else:
                d[l[0]][l[1]] = int(l[2])
        else:
            d[l[0]] = {l[1]:int(l[2])}
    l1 = sorted(d.keys())
    for k in l1:
        print("{0}:".format(k))
        l2 = sorted(d[k].keys())
        for j in l2:
            print(j, d[k][j])