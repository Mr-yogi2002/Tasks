string = input("enter the string ")

#def ispalindrome(string):
#    if(string==string[::-1]):
#        return"the string in a palindrome"
#    else:
#        return"the string in a not palindrome"

#print(ispalindrome("string"))

def isapalindrome(string):
    if(string==string[::-1]):
        return "the string is a palindrome"
    else:
        return "the string is not a palindrome"
print("isapalindrome ",string)


