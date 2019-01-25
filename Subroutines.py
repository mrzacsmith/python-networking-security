__author__ = 'silverback'

def sub(x,y):
    z = x - y
    print(z)

def add(x,y):
    return x + y

# DRY ~ create variables to avoid repeating

num1 = 15
num2 = 4

print(add(num1, num2))

sub(num1, num2)