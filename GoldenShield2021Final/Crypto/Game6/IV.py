from Crypto import Random
from Crypto.Cipher import AES
from Crypto.Util.Padding import pad
def encrypt(value, key):
    value = value.encode('ascii')
    iv = Random.new().read(AES.block_size)
    cipher = AES.new(key, AES.MODE_CBC, iv)
    ciphertext = cipher.encrypt(pad(bytes(value, encoding='utf8'), size))
    return iv + ciphertext