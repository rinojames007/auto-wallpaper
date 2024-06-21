import os
from cryptography.fernet import Fernet

key = Fernet.generate_key()
value = os.environ.get["ACCESS_KEY"]
with open("secret.key", "wb") as file:
    file.write(key)

fernet = Fernet(key)
ACCESS_KEY = b"TccG2BrkmoayHRsGEE19MdK7yRjr7bZDWkXUxGm5Mc0"
ENCRYPTED_KEY = fernet.encrypt(ACCESS_KEY)

with open("key.txt", "wb") as file:
    file.write(ENCRYPTED_KEY)

