with open("input.txt", "r") as f:
    l = []
    k = int(f.readline())
    for line in f:
        l1 = list(map(str,line.split()))
        if((int(l1[-1]) >= 40) and (int(l1[-2]) >= 40) and (int(l1[-3]) >= 40)):
            s = int(l1[-1]) + int(l1[-2]) + int(l1[-3])
            l.append(s)
    l.sort(reverse=True)

    if(k >= len(l)):
        print(0)
    elif(l.count(l[0]) > k):
        print(1)
    else:
        res = 0
        for i in range(len(l)-1):
            if((l[i] != l[i+1]) and i+1 <= k):
                res = l[i]
        print(res)