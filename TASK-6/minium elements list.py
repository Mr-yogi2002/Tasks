list = [5,6,1,2,3,4]
efx = len(list)

def findmin(list,efx):
    min_ele = list[0]
    for i in range(efx):
        if list[i] < min_ele:
            min_ele = list[i]
    return min_ele
print(findmin(list,efx))