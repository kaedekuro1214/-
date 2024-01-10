import hashlib

message = 'Hash'

hash_sha256 = hashlib.sha256(message.encode())

print(hash_sha256)