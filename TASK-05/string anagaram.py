def check (s1,s2):
    if sorted(s1)==sorted(s2):
        print(sorted(s1))
        print(sorted(s2))
        print('the string are anagram')
    else:
        print("the string aren't anagram")

s1="listen"
s2="silent"
check(s1,s2)