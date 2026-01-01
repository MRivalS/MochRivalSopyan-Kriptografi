from Crypto.Cipher import DES
from Crypto.Util.Padding import pad, unpad


real_key = b'\x05' * 8
plaintext = b'DATA RAHASIA'
cipher = DES.new(real_key, DES.MODE_ECB)
ciphertext = cipher.encrypt(pad(plaintext, 8))


for i in range(256):
    test_key = bytes([i]) * 8
    test_cipher = DES.new(test_key, DES.MODE_ECB)
    try:
        decrypted = unpad(test_cipher.decrypt(ciphertext), 8)
        if decrypted == plaintext:
            print("Kunci ditemukan:", test_key)
            break
    except:
        pass
