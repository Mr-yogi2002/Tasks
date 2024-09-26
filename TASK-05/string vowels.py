
str = input("enter the string = ")

def vowels(str):
    for character in str:
        if character in "aeiouAEIOU":
            print(character,end=" ")
        return character

vowels(str)
