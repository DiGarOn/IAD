i = int(input())

def fib(i):
    if(i == 1):
        return 'a'
    elif i == 2:
        return 'b'
    else:
        return fib(i-2) + fib(i-1)

print(fib(i))