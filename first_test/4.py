n = int(input())
mas = list(map(int,input().split()))
mas.sort()
count = 0

for i in range(n):
    for j in range(i+1, n):
        for k in range(j+1, n):
            if((mas[i] + mas[j] > mas[k]) and (mas[k] + mas[j] > mas[i]) and (mas[i] + mas[k] > mas[j])):
                count += 1
print(count)