import sys
from Crypto.Util.number import *
def xor_bytes(*args):
    from functools import reduce
    return bytes([reduce(lambda x, y: x ^ y, vals) for vals in zip(*args)])

def xor_bytes(data, key_int):
    return bytes([b ^ key_int for b in data])

flagCrypted = '0e0b213f26041e480b26217f27342e175d0e070a3c5b103e2526217f27342e175d0e077e263451150104'
cipher_bytes = bytes.fromhex(flagCrypted)
known_plain = b'crypto{'

# Tìm key từ đoạn đầu
key = b'myXORkey'

# Lặp lại key cho đủ độ dài ciphertext
full_key = (key * (len(cipher_bytes) // len(key) + 1))[:len(cipher_bytes)]

# XOR từng byte
flagDecoded = bytes([c ^ k for c, k in zip(cipher_bytes, full_key)])

print(flagDecoded.decode())