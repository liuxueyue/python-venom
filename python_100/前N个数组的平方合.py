def shuzi_2_he(num):
    re = 0
    for i in range(1,num+1):
        re += i*i
    return re


print(shuzi_2_he(50))