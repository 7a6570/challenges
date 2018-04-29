#!/usr/bin/python

from Crypto.Cipher import AES
from Crypto.Util import Counter


encrypted_aes_key='n0T_My_passW0rD!'
ciphertext='b2d3cf567d5f4b72f8b3e297e93e52f2f3f3c7212f8e084f3c8f01c4adf49ff2df5985796ed289b99024f79c4747befd1dff843e284969ae56e915dacffe6efacdee881c082545b7c42fc6dcd9f815a6b207c2098e48480dbc9ef744c83b18cb979a5c944184a53e00d703eed7c78cdc60a55489'


cipherbytes = bytes.fromhex(ciphertext)

keys=[]

for xor_key in range(0,256):

	key=bytearray()

	for c in encrypted_aes_key:

		key.append(ord(c) ^ xor_key)

	keys.append((bytes(key), xor_key))

for k,xor_key in keys:

    ctr = Counter.new(128)
    cipher = AES.new(k, mode=AES.MODE_CTR, counter= ctr)
    r=cipher.decrypt(cipherbytes)

    try:
        print(r.decode('utf-8'))
    except Exception as e:
        pass
