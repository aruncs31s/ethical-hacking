<h1 align="center"><b>Cryptography</b></h1>

## **Chapters**

- [Introduction](#introduction)
- [Types](#types-of-cryptography)
- [Cryptography tools]()
- [GnuPG](#gnupg)
---

## **Introduction**

<p align="justify"><i>Cryptography</i> itself is a very huge topic and it will not fit in this simple markdown page and i dont have the time to explain it. So i will surf throught the surface and only point out the important stuffs .So in simple words cryptography is a tool used to make a data secure by coverting it into some format to make the information/data secure.</p>

## **Types of Cryptography**

<p align="justify">There are mainly Two types of cryptography</p>

- [Symmetric Key Cryptography](#symetric-key-cryptography)
- [Asymmetric Key Cryptography](#asymmetric-key-cryptography)


### **Symmetric Key Cryptography**
In `Symmetric` Key Cryptography the same key is used for encrypting and decrypting the file.

### **Asymmetric Key Cryptography**
In `Asymmetric` Key Cryptography There is `public` and `private` Keys . 

- Public Key is used to encrypt while private key is used in decrypting

- You can share the `public key` with anyone and they can encrypt their files with it but only you can decrypt it

the following is an example for my public key

```
-----BEGIN PGP PUBLIC KEY BLOCK-----

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
=jQqa
-----END PGP PUBLIC KEY BLOCK-----
```

- Following is an example for private key

```
-----BEGIN PGP PRIVATE KEY BLOCK-----

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
=jQqa
-----END PGP PRIVATE KEY BLOCK-----

```


## **Cryptography Tools**
There are so many tools which uses cryptography but as we are linux guys we use `Gnupg` .Which is widely used in communication and for military grade encryption

Followings are some tools i use very often 

- [Gnupg](./gnupg.md)
- Veracrypt
- Cryptsetup
- openssl

---

<h1 align="center" id="gnupg"><b>Gnupg</b></h1>

`GnuPG`, which stands for `GNU Privacy Guard` is open source application that provides lot of functionality related to cryptography like encryption , decryption , signing etc..


## **Chapters**
- [Creating a GPG keypairs](#creating-a-gpg-keypair)
- [Encrypting a file](#encrypting-a-file)
- [Decrypting a file]()
- [Exporting Public Key]()
- [Encrypting using public key]()
- []

## **Creating a GPG keypair**

- Run the following in your terminal

```
$ gpg --full-generate-key
```
- after running the above command you'll get the following

```
gpg (GnuPG) 2.2.41; Copyright (C) 2022 g10 Code GmbH
This is free software: you are free to change and redistribute it.
There is NO WARRANTY, to the extent permitted by law.

Please select what kind of key you want:
   (1) RSA and RSA (default)
   (2) DSA and Elgamal
   (3) DSA (sign only)
   (4) RSA (sign only)
  (14) Existing key from card
Your selection?
```
- type `1` and hit enter
- after selecting `1` you will be prompted with the following
```
RSA keys may be between 1024 and 4096 bits long.
What keysize do you want? (3072)
```
- type `4096` and hit enter
- afterwards youll be prompted with the following
```
Please specify how long the key should be valid.
         0 = key does not expire
      <n>  = key expires in n days
      <n>w = key expires in n weeks
      <n>m = key expires in n months
      <n>y = key expires in n years
Key is valid for? (0)
```
- for now we crate a non expiring key so type `0` and hit enter
- if it ask `Is this correct?` just type `y` and hit enter
- Now provide your real or some name in the following prompt
```

GnuPG needs to construct a user ID to identify your key.

Real name: Hacker
```
- i choose `Hacker` you can choose what ever you want!
- after this it will ask for email provide any
```
Email address: hacker@email.com

```
- after completing you'll get the following output
```
You selected this USER-ID:
    "Hacker <hacker@email.com>"

Change (N)ame, (C)omment, (E)mail or (O)kay/(Q)uit?

```
- type `O`(not zero ) and hit enter

![pass ask](../../images/password_ask.png?raw=true)

- after typing the password you'll get the following
```
public and secret key created and signed.

pub   rsa4096 2023-08-30 [SC]
      D3034E4791F8142079F0A5DEB3B7ACA36C02064C
uid                      Hacker <hacker@email.com>
sub   rsa4096 2023-08-30 [E]

```


- Now you are free to encrypt


## **Encrypting a file**
Encrypting a file is very simple after a keypair is been created. In this chapter we try to encypt a file named `found.me`

![found.me](../../images/found.me.png?raw=true)

you can see that i have a file named `found.me` and it contains `just a text file` . just a plain text so we'll now try to encrypt using gpg and our newly created `public key`


### **Steps**

- List the keys

```
$ gpg --list-keys

```
- you'll get something similar to following

```
/root/.gnupg/pubring.kbx
------------------------
pub   rsa4096 2023-08-30 [SC]
      D3034E4791F8142079F0A5DEB3B7ACA36C02064C
uid           [ultimate] Hacker <hacker@email.com>
sub   rsa4096 2023-08-30 [E]

```


- you can either use `uid` or the long text `D3034E4791F8142079F0A5DEB3B7ACA36C02064C` to use as recipient or sometimes u can just provide the `Real name` itself, in this case `Hacker`

```
$ gpg -r Hacker -e found.me
```
or
```
$ gpg -r hacker@email.com -e found.me
```
or


```
$ gpg -r D3034E4791F8142079F0A5DEB3B7ACA36C02064C -e found.me

```

- You should change this with corresponding

- You can also use a public key to encrypt a file

```
gpg -r /path/to/key/file -e <any_file>
```


- `e` is used to specify the file to be encrypted
- `r` is used to specify the recipient or the key

- after encrypting the text file

![found me .gpg](../../images/found.me.gpg.png)


## **Decrypting an encrypted file**
Decrypting an encrypted file is really easy if you have the private key with you.
A good thing about Gnupg  is that you can share the `private key` which is not safe but even if someone has access to your private they still require the passphrase/password

### **Steps**

- If you have the private key
```
$ gpg -d /path/to/encryptedfile.gpg
```

- If you dont have the private key
you have to import the keys inorder to decrypt the file

### **Exporting Public Key**

### **Encrypting using public key**

### **Exporting Private Key**

### **Dercypting using private key**
