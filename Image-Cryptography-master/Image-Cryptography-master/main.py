from rubikencryptor.rubikencryptor import RubikCubeCrypto
from PIL import Image

# Encrypt image
input_image = Image.open(r'C:\Users\Home\Desktop\Image-Cryptography-master\Image-Cryptography-master\example - Copy\original.png')
encryptor = RubikCubeCrypto(input_image)
encrypted_image = encryptor.encrypt(alpha=8, iter_max=10, key_filename='key.txt')
encrypted_image.save('encrypted_image.png')

# Decrypt image
decryptor = RubikCubeCrypto(encrypted_image)
decrypted_image = decryptor.decrypt(key_filename='key.txt')
decrypted_image.save('decrypted_image.png')