import random

def gen_pass(n):
    craracter = "+-/*!&$#?=@abcdefghijklnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890"

    password = ""
    for i in range(n):
        password += random.choice(craracter)

    return password

n = int(input("Enter the length of password: "))
print("Hasil Generate: ", gen_pass(n))

