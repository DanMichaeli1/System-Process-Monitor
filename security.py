__author__ = 'Dan'

from Crypto.Cipher import AES
import random

def encryptFile(file, key):
    iv = ''.join([chr(random.randint(0, 0xFF)) for i in range(16)])
    aes = AES.new(key, AES.MODE_CBC, iv)