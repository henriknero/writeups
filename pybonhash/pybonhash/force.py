output = open("pybonhash/hash.txt").read()
fuck = [output[i:i+64] for i in range(0, len(output), 64)]

import binascii, hashlib
from Crypto.Cipher import AES
from itertools import product
from string import ascii_letters
keyword_map= {}
for x in range(0,128):
    for y in range(0,128):
        keyword_map[binascii.hexlify(hashlib.md5((chr(x) + chr(y)).encode('utf-8')).digest())] = (chr(x) + chr(y))
for x in range(0,128):
    print(bytes([x, y]))
    for y in range(0,128):
        thiskey = bytes([x, y]) * 16
        cipher = AES.new(thiskey, AES.MODE_ECB)
        for key in keyword_map:
            enc = cipher.encrypt(key)
            if binascii.hexlify(enc).decode('ascii') in fuck:
                print(binascii.hexlify(enc).decode('ascii') + " : " + chr(x) + chr(y))
        