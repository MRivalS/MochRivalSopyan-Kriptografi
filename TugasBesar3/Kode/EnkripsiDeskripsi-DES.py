from Crypto.Cipher import DES
from Crypto.Util.Padding import pad, unpad

key = b'8bytekey'
plaintext = b'ini  pesan rahasia'

cipher = DES.new(key, DES.MODE_ECB)
ciphertext = cipher.encrypt(pad(plaintext, 8))

decipher = DES.new(key, DES.MODE_ECB)
decrypted = unpad(decipher.decrypt(ciphertext), 8)

print("Plaintext :", plaintext)
print("Ciphertext:", ciphertext)
print("Decrypted :", decrypted)
