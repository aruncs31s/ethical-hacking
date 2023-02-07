import pathlib
import secrets
import os
import base64
import getpass
import cryptography
from cryptography.fernet import Fernet
from cryptography.hazmat.primitives.kdf.scrypt import Scrypt
def generate_salt(size=16):
    """Generate the salt used for key generation
    'size' is the length of the salt to generate"""
    return secrets.token_bytes(size)
def derive_key(salt,passwd):
    #Derive the key from the 'passwd' using the passed 'salt'
    dky=Scrypt(salt=salt,length=32,n=2**14,r=8,p=1)
    return dky.derive(passwd.encode())
def load_salt():
    #load salt from salt.salt file
    return open("salt.salt","rb").read()
def generate_key(passwd,salt_size=16,load_existing_salt=False,save_salt=True):
    """Generate a key from a 'passwd' and the salt.
    If 'load_existing_salt' is True,it'll load the salt 
    from a file in the current directory called 'salt.salt'.
    If 'save_salt' is true then it will generate a new salt 
    and save it to 'salt.salt'"""
    if load_existing_salt:
        salt=load_salt()    #to load existing salt
    elif save_salt:
        salt=generate_salt(salt_size)   #generate new salt and save it
        with open("salt.salt","wb") as salt_file:
            salt_file.write(salt)
    derived_key=derive_key(salt,passwd)  #generate the key from the salt and the passwd
    return base64.urlsafe_b64encode(derived_key)    #encode it using Base 64 and return it
def encrypt(filename,key):
    f=Fernet(key)
    with open(filename,"rb") as file:
        file_data=file.read()   #to read file
    encrypted_data=f.encrypt(file_data) #to encrypt data
    with open(filename,"wb") as file:
        file.write(encrypted_data)  #to write into file the encrypted data
def decrypt(filename,key):
    f=Fernet(key)
    with open(filename,"rb") as file:
        encrypted_data=file.read()
    try:
        decrypted_data=f.decrypt(encrypted_data)
    except cryptography.fernet.InvalidToken:
        print("[!] invalid token,The password is incorrect")
        return
    with open(filename,"wb") as file:
        file.write(decrypted_data)
def encrypt_folder(foldername,key):
    for f in pathlib.Path(foldername).glob("*"):
        if f.is_file():
            print("Encrypting",f)
            encrypt(f,key)
        elif f.is_dir():
            encrypt_folder(f,key)
def decrypt_folder(foldername,key):
    for f in pathlib.Path(foldername).glob("*"):
        if f.is_file():
            print("Decrypting",f)
            decrypt(f,key)
        elif f.is_dir():
            decrypt_folder(f,key)


if __name__=="__main__":
    import argparse
    parser=argparse.ArgumentParser(description="File Encryption Script with a Password")
    parser.add_argument("path",help="Path to encrypt/decrypt, can be a file or an entire folder")
    parser.add_argument("-s","--salt-size",help="If this is set,a new salt with the passed size is generated",type=int)
    parser.add_argument("-e","--encrypt",action="store_true",help="Whether to encrypt the file/folder,only -e or -d can be specified")
    parser.add_argument("-d","--decrypt",action="store_true",help="Whether to decrypt the file/folder,only -e or -d can be specified")
    args=parser.parse_args()
    if args.encrypt:
        passwd=getpass.getpass("Enter the password for encryption:")
    elif args.decrypt:
        passwd=getpass.getpass("Enter the password you used for encryption")
    if args.salt_size:
        key=generate_key(passwd,salt_size=args.salt_size,save_salt=True)
    else:
        key=generate_key(passwd,load_existing_salt=True)
    encrypt_=args.encrypt
    decrypt_=args.decrypt
    if encrypt_ and decrypt_:
        raise TypeError("Please specify whether you want to encrypt the file or decrypt it.")
    elif encrypt_:
        if os.path.isfile(args.path):
            encrypt(args.path,key)
        elif os.path.isdir(args.path):
            encrypt_folder(args.path,key)
    elif decrypt_:
        if os.path.isfile(args.path):
            decrypt(args.path,key)
        elif os.path.isdir(args.path):
            decrypt_folder(args.path,key)
    else:
        raise TypeError("Please specify whether you want to encrypt the file or decrypt it.")
