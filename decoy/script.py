#%%
#!/usr/bin/python3
hexstring = "(mv|GLp+Gv+"
xor = hex(int('b',16)^int('13',16))
print(xor)
xor = int(xor, 16)
output = ''
for x in hexstring:
    output += chr(ord(x)^xor)
print(output)
#%%
hexstring = "}[2waHmrgxj"
output2 = ""
for x in hexstring[6:]:
    output2+=chr(ord(x)-4)
for x in hexstring[:6]:
    output2+=chr(ord(x)-2)

print(output2 + output)

#%%
output3 = ""
hexstring = '{`I5z%u5dL~'
for x in hexstring:
    output3 +=chr(ord(x)-1)
print(output3)
#%%
hexstring = "n]9Uf9p\x1EA\x15}"
prev=1
output4=""
for index,x in enumerate(hexstring[::-1]):
    if(index != 0):
        prev = ord(hexstring[::-1][index-1])
    output4+=chr(ord(x)^prev)
output4 = output4[::-1]
print(output4)

