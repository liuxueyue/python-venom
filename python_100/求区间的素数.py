def sushu(x,y):
    lis1 = []
    for i in range(x,y+1):
        if i >1:
            for n in range(2,i):
                if (i % n) == 0:
                    break
            else:
                lis1.append(i)
    return lis1


print(sushu(1, 10))

def sushu2(x,y):
    lis = []
    def is_bool(n):
        if n ==1:
            return False
        for idx in range(2,n):
            if n % idx == 0:
                return False
        return True

    for i in range(x,y+1):
        if is_bool(i):
            lis.append(i)
    return lis


print(sushu2(1, 25))