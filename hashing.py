import string
import random

numbers = "123456789"
def hash_code(stringLength=8):
    letters = string.ascii_lowercase
    combined = letters+numbers
    return ''.join(random.choice(combined) for i in range(len(combined)))

print(hash_code())