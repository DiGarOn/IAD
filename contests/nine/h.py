#ok

with open("input.txt") as f:
    n = int(f.readline())
    yes = {i for i in range(1,n+1)}

    for line in f:
        if(line[0] != 'H'):
            tmp = set(map(int,line.split()))
            if(len(tmp) >= len(yes)/2):
                if(len(yes.intersection(tmp)) > len(yes.difference(tmp))):
                    print("YES")
                    yes.intersection_update(tmp)
                else:
                    print("NO")
                    yes.difference_update(tmp)
            else:
                print("NO")
                yes.difference_update(tmp)
        else:
            print(*sorted(yes))
