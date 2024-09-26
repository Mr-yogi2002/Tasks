#prime or not prime numbers

list=[10,501,22,37,100,999,87,351]
prime = []

for i in list:
    c = 0
    for efx in range(1,i):
        if i % efx == 0:
            c = c+1
    if c == 1:
        prime.append(i)
print("prime numbers are: ",prime)
