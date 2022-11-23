with open('input.txt', 'r') as f:
        d = {}
        for line in f:
            l = list(map(str,line.split()))
            for i in l:
                if i in d.keys():
                    d[i] += 1
                else:
                    d[i] = 0
                print(d[i], end = " ")
