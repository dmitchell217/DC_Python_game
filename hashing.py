import string
import random

numbers = "123456789"
def hash_code(itemtype, stringLength=8):
    letters = string.ascii_lowercase
    combined = letters+numbers
    return str(''.join(random.choice(combined) for i in range(len(combined)))) + "_" + str(itemtype)

# print(hash_code("tree"))