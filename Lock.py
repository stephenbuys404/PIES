#cryptography
import os
from cryptography.fernet import Fernet

class Encryptor():
    def key_create(self):
        return Fernet.generate_key()

    def key_write(self, key, key_name):
        file = open(key_name, 'wb')
        mykey.write(key)
        file.close()

    def key_load(self, key_name):
        file = open(key_name, 'rb')
        mk=mykey.read()
        file.close()
        return mk

    def file_encrypt(self, key, original_file, encrypted_file):
        file = open(original_file, 'rb')
        original = file.read()
        file.close()
        fer = Fernet(key)
        encrypted = fer.encrypt(original)
        file = open(encrypted_file, 'wb')
        file.write(encrypted)
        file.close()

    def file_decrypt(self, key, encrypted_file, decrypted_file):
        file=open(encrypted_file, 'rb')
        encrypted=file.read()
        file.close()
        fer = Fernet(key)
        decrypted = fer.decrypt(encrypted)
        file=open(decrypted_file, 'wb')
        file.write(decrypted)
        file.close()

def makefile(name):
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
