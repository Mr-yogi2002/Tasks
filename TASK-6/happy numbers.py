a = [10,501,20,37,100,999,87,351]
#a = [8,2,7,82]
b = []
def is_happy(a):
    for i in range (len(a)):
        sum = a[i]
        while sum!=1 and sum !=4:
            tempsum = 0
            for digit in str(sum):
                tempsum += int(digit) ** 2
            sum = tempsum
        if sum == 1:
            b.append(a[i])
    return b
print(is_happy(a))