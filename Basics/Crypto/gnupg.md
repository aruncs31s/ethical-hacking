<h1 align="center"><b>Gnupg</b></h1>

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
