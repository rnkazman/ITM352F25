from cryptography.fernet import Fernet

key = Fernet.generate_key()
cipher_suite = Fernet(key)
token = cipher_suite.encrypt(b"This is a really secret message! Not for sharing!")
print(token)

decrypted = cipher_suite.decrypt(token)
print("Decrypted token=", decrypted)
print(decrypted.decode())