with open("input.txt") as f:
    n = int(f.readline())
    s = set(i for i in range(1,n+1))
    yes = set()
    no = {}
    for line in f:
        if(l[0] != 'H'):
            tmp = set(map(int, line.split()))
            if(len(tmp) == len(s)/2):
                print("NO")
                s.difference_update(tmp)
            else:
                if()
