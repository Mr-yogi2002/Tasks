
list1=[10, 20, 30, 20, 20, 30, 40, 50, -20, 60, 60, -20, -20]
def check_duplicated(x):
    size = len(x)
    repeated = []
    for i in range(size):
        k =i+1
        for j in range(k,size):
            if x[i] == x[j] and x[i] not in repeated:
                repeated.append(x[i])
    return repeated
print(check_duplicated(list1))