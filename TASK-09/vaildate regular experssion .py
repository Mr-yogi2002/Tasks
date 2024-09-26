#email address
import re
regex = re.compile((r'([A-Za-z0-9]+[.-_])*[A-Za-z0-9]+@[A-Za-z0-9-]+(\.[A-Z|a-z]{2,})+'))

def email_vaild(email):
    if re.fullmatch(regex,email):
        print("the given mail is vaild")
    else:
        print("the given mail is invaild")

email_vaild("rtyogesh123@gmail.com")

#mobiles numbers bangladesh
import re
regex = re.compile(r"^[5-9]{1}[0-9]{9}$")
def mobiles_numbers(mobiles):
    if re.fullmatch(regex,mobiles):
        print("the given mobile is vaild")
    else:
        print("the given mobile is invaild")
mobiles_numbers("01054 694200")

#telephones numbers of USA
import re
regex = re.compile((r'(\b[\w.]+@+[\w.]+.+[\w.]\b)'))
def telephone_numbers_USA(telephone):
    if re.fullmatch(regex,telephone):
        print("the given telephone numbers USA is vaild")
    else:
        print("the given telephone numbers USA is invaild")

telephone_numbers_USA("555 555 1234")

#password composed
import re

def vaildate_password(password):
    if len(password)<8:
        return False
    if not re.search("[a-z]",password):
        return False
    if not re.search("[A-Z]",password):
        return False
    if not re.search("[0-9]",password):
        return False
    return True

password=("P@ssw0rd")
vaildate_password("password")

if vaildate_password(password):
    print("vaild password")
else:
    print("invaild password")


