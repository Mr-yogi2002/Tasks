x = input("enter the string ")
vowels_string = "aeiouAEIOU"
print("input string ",x)

for efx in x:
    if efx in vowels_string:
        x=x.replace(efx,"")
print("output wothout vowels string ",x)