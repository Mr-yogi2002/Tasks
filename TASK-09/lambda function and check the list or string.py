# initializing string
test_string = "There are 2 apples for 4 persons"
test_list = ['apples', 'oranges']

print("The original string : " + test_string)

print("The original list : " + str(test_list))

test_string = test_string.split(" ")

count = 0
for i in test_string:
    for j in test_list:
        if i == j:
            count = 1
            break
if count == 1:
    print("String contains the list element")
else:
    print("String does not contains the list element")