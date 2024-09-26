list=[10,501,20,37,100,999,87,351]
even=[]
odd=[]

for efx in(list):
    if (efx%2==0):
        even.append(efx)
    else:
        odd.append(efx)
print("even numbers i list: ",even)
print("odd numbers in list: ",odd)