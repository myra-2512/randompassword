import random
import string

def generate_password(length=12, use_uppercase=True, use_digits=True, use_special_chars=True):
    
    if length < 4:
        raise ValueError("Password length should be at least 4 characters.")

    char_pool = string.ascii_lowercase
    if use_uppercase:
        char_pool += string.ascii_uppercase
    if use_digits:
        char_pool += string.digits
    if use_special_chars:
        char_pool += string.punctuation

    if not char_pool:
        raise ValueError("At least one character type must be selected.")

    password = ''.join(random.choice(char_pool) for _ in range(length))
    return password
if __name__ == "__main__":
    print("Generated Password:", generate_password(length=16, use_uppercase=True, use_digits=True, use_special_chars=True))
    