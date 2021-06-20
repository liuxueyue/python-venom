def num2(num):
    re = 1
    while num > 0:
        re *= num
        num -=1
    return re

print(num2(6))

def num1(num):
    re = 1
    for x in range(1,num +1):
        re *= x
    return re


print(num1(6))