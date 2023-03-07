import string
from secrets import choice

letters = string.ascii_letters
digits = string.digits
special_characters = string.punctuation

alphabet = letters + digits + special_characters

while True:
    pwd = ''
    for pwd_length in range(8):
        pwd += ''.join(choice(alphabet))
    if(any(char in special_characters for char in pwd)) and sum(char in digits for char in pwd) >=2:
        break
print(pwd)