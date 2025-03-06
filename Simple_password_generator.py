import random
import string

length = int(input("Enter password length: "))
password = ''.join(random.choice(string.ascii_letters + string.digits)

for _ in range(length))

print(f"Your password: {password}")


