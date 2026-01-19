import random

def generate_password(length=12):
    chars= 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789'

    password = ''.join(random.choice(chars) for _ in range(length))
    return password

print("random password is ",generate_password())
