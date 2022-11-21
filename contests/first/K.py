n = int(input())
s = []
s.append("   _~_    ")
s.append("  (o o)   ")
s.append(" /  V  \  ")
s.append("/(  _  )\ ")
s.append("  ^^ ^^   ")

for j in range(5):
    for i in range(n):
        print(s[j], end = " ")
    print("\n")