from Crypto import Random
from Crypto.Cipher import AES
from Crypto.Util.Padding import pad
def encrypt(value, key):
    value = value.encode('ascii')
    iv = Random.new().read(AES.block_size)
    cipher = AES.new(key, AES.MODE_CBC, iv)
    ciphertext = cipher.encrypt(pad(bytes(value, encoding='utf8'), 24))
    return iv

def main():
    v = 'oGIr8/T5VNg1S3k9YyaXrEizVmCcDh7pO8IJJqH5JWZM4V9s66iOVA7U67zoH1SwlTVV7EmyYIG2FWMe928xM0hPqL0/neh33zUdGEJdwR7dCRvWGi9lWZqrkyZrJcmgMbRxIIMd35MPcp+3lM1IkQ=='
    k = 'i32ebzbETjBWBxzZXR7B9w==' # 24
    print(encrypt(v,k))
