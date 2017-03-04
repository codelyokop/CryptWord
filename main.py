import random
import string

print("made by jack")

def pass_gen(size, chars=string.ascii_lowercase + string.digits):
	return "".join(random.SystemRandom().choice(string.ascii_lowercase + string.digits) for _ in range(size))

versionNumber = "0.0.1"

print("CryptWord Version {}".format(versionNumber))

passwordLength = int(input("How many characters do you want your password to be? "))

print(pass_gen(passwordLength))
