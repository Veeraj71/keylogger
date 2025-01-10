from cryptography.fernet import Fernet
def decrypt(keyname,filename):
    with open (keyname,'rb') as key_file:
        key = key_file.read()
    z = Fernet(key)
    with open (filename,'rb') as file:
        for encryptedline in file:
            decrypeddata=z.decrypt(encryptedline).decode()
            print(decrypeddata)

decrypt('/home/purplerain/Desktop/GDG/CyberSec/Project/key.txt', '/home/purplerain/Desktop/GDG/CyberSec/Project/input.txt')