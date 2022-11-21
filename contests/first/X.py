a = int(input())
b = int(input())

print("YES"*(a%b==0 or b%a==0) + "NO"*(a%b!=0 and b%a!=0))