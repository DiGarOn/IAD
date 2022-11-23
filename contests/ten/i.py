with open("input.txt") as f:
    d = {}
    for line in f:
        l = list(map(str,line.split()))
        if len(l) == 2:
            if(l[0] == "INCOME"):
                for k in d.keys():
                    if(d[k] > 0):
                        d[k] *= (100 + int(l[1]))*1.0/100
                        d[k] = int(d[k])
            else:
                if(l[1] in d.keys()):
                    print(int(d[l[1]]))
                else:
                    print("ERROR")
        elif len(l) == 3:
            if(l[0] == "DEPOSIT"):
                if(l[1] in d.keys()):
                    d[l[1]] += int(l[2])
                else:
                    d[l[1]] = int(l[2])
            else:
                if(l[1] in d.keys()):
                    d[l[1]] -= int(l[2])
                else:
                    d[l[1]] = -1*int(l[2])
        else:
            if(l[1] in d.keys()):
                if(l[2] in d.keys()):
                    d[l[1]] -= int(l[3])
                    d[l[2]] += int(l[3])
                else:
                    d[l[1]] -= int(l[3])
                    d[l[2]] = int(l[3])
            else:
                if(l[2] in d.keys()):
                    d[l[1]] = -1*int(l[3])
                    d[l[2]] += int(l[3])
                else:
                    d[l[1]] = -1*int(l[3])
                    d[l[2]] = int(l[3])
