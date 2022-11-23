n, m = map(int,input().split())
k,p = map(int,input().split())
for i in range(k, n+1, k):
    for j in range(p, m+1, p):
        print(i*100 + j)
