#cryptography
import os
from cryptography.fernet import Fernet

class Encryptor():
    def key_create(self):
        return Fernet.generate_key()

    def key_write(self, key, key_name):
        with open(key_name, 'wb') as mykey:
            mykey.write(key)

    def key_load(self, key_name):
        with open(key_name, 'rb') as mykey:
            return mykey.read()

    def file_encrypt(self, key, original_file, encrypted_file):
        fer = Fernet(key)
        with open(original_file, 'rb') as file:
            original = file.read()
        encrypted = fer.encrypt(original)
        with open (encrypted_file, 'wb') as file:
            file.write(encrypted)

    def file_decrypt(self, key, encrypted_file, decrypted_file):
        fer = Fernet(key)
        with open(encrypted_file, 'rb') as file:
            encrypted = file.read()
        decrypted = fer.decrypt(encrypted)
        with open(decrypted_file, 'wb') as file:
            file.write(decrypted)

def makefile(name):
    if(not os.path.exists(name+'.csv')):
        file = open(name+'.csv','a')
        file.write('1,2,3,4,5,6,7,8')
        file.close()

encryptor=Encryptor()
mykey=encryptor.key_create()
encryptor.key_write(mykey,'secret.key')
loaded_key=encryptor.key_load('secret.key')
makefile('data')
encryptor.file_encrypt(loaded_key, 'data.csv', 'enc_data.csv')
encryptor.file_decrypt(loaded_key, 'enc_data.csv', 'dec_data.csv')