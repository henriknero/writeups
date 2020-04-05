# Pybonhash writeup
We are given a [.pyc file](https://github.com/henriknero/writeups/tree/master/pybonhash/pybonhash/pybonhash.cpython-36.pyc), this file can simply be decompiled using uncompyle6 which gives us [this](https://github.com/henriknero/writeups/tree/master/pybonhash/pybonhash/pybonhash.py). We are also supplied with a hash.txt that is 6528(204*32) characters long. 


## pybonhash file
```python
import string, sys, hashlib, binascii
from Crypto.Cipher import AES
from flag import key
assert len(key) == 42
data = open(sys.argv[1], 'rb').read()
assert len(data) >= 191
FIBOFFSET = 4919
MAXFIBSIZE = len(key) + len(data) + FIBOFFSET

def fibseq(n):
    out = [
     0, 1]
    for i in range(2, n):
        out += [out[(i - 1)] + out[(i - 2)
    return out

FIB = fibseq(MAXFIBSIZE)
i = 0
output = ''
while i < len(data):
    data1 = data[(FIB[i] % len(data))]
    key1 = key[((i + FIB[(FIBOFFSET + i)]) % len(key))]
    i += 1
    data2 = data[(FIB[i] % len(data))]
    key2 = key[((i + FIB[(FIBOFFSET + i)]) % len(key))]
    i += 1
    tohash = bytes([data1, data2])
    toencrypt = hashlib.md5(tohash).hexdigest()
    thiskey = bytes([key1, key2]) * 16
    cipher = AES.new(thiskey, AES.MODE_ECB)
    enc = cipher.encrypt(toencrypt)
    output += binascii.hexlify(enc).decode('ascii')

print(output)

```
So data i read from a file supplied in arg 1. The data is then hashed using the key supplied in a file flag.py and outputted to stdout. 

So the program iterates through the data and the key for len(data) times. Each iteration generating a 64byte string. Each iteration picks 2 characters from the data-string and 2 characters from the key at the index of a fibonacci number which is chosen by two different equations.

Each 2byte datastring is hashed using md5, and the 2 bytes taken from the key are multiplied to generate a 32byte key for a AES ECB crypto. 

```
md5(2 databytes) -> AES_ECB(2 keybytes*16) -> "output_hash"
```

So initially we thought we would need to utilize knowledge of the flag format ```midnight{xxxxxxxxxxxxxxxxxxxx}```. But the script hints that each character is ascii encoded which means "only" 128 possible solutions per key and data byte. So there are 128^4 possible inputs for each 64byte output. And we know that because of it being md5hashed we can be relatively certain that each input output 64byte is unique. **TLDR We bruteforced it.**

```python
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
``` 
So at this moment I just put the output of this script into the [pybonhash script](https://github.com/henriknero/writeups/tree/master/pybonhash/pybonhash/pybonhash_mod.py) and map each output-hash to the key. Then print the key:

```midnight{xwJjPw4Vp0Zl19xIdaNuz6zTeMQ1wlNP}```


