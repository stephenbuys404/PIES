import hashlib

hash_object = hashlib.md5(b'Hello World')
print(hash_object.hexdigest())

hash_object = hashlib.sha1(b'Hello World')
print(hash_object.hexdigest())

hash_object = hashlib.sha224(b'Hello World')
print(hash_object.hexdigest())

hash_object = hashlib.sha256(b'Hello World')
print(hash_object.hexdigest())

hash_object = hashlib.sha384(b'Hello World')
print(hash_object.hexdigest())

hash_object = hashlib.sha512(b'Hello World')
print(hash_object.hexdigest())
