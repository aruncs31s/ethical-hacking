## **Setting Up hacking Environment**
- [Introduction](#introduction)
- [Hacking OS](#hacking-os)
- [Installing ArchLinux](#installing-archlinu)
### **introduction**
    A hacking environment is essential for to do hacking .In good old days everyone has to setup their own hacking environment inorder to start hacking but nowdays some community/companies do this for you that is , they make an hacking os which comes with all the neccessary tools out of the box 
    In this section We will setup a hacking os and explore some premaid one's like kali and parrot 

### **Hacking OS**
   Hacking os is a premaid OS which shipps with hacking tools pre-installed , which saves time but increases system's size . So in this section we will be installing archlinux and setup blackarch


## **Installing ArchLinux**
[*Official Guide](https://wiki.archlinux.org/title/installation_guide)

- [Introduction](#introduction)
- [Downloading ISO]()
- [Making Bootable Pendrive]()
- [Booting]()
- [Connecting to Internet]()
- [Setting Time]()
- [Formating Drives]()
- [Mounting Drives]()
- [Install]

### **Introduction**
    Arch Linux simple and lightweight operating system . I choose Arch linux insted of Debian because  in arch linux you'll get the latest tools and packages and it only take as little as `77 MB` after installing


### **Downloading ISO**
    Goto [Archlinux/Downloads](https://archlinux.org/download/) then download the iso 


### **Making Bootable Pendrive**
    - [For windows](#windows)
        for those who are using windows you have to download either ["Rufus"](https://rufus.ie/) or ["Balena Etcher"](https://etcher.balena.io/) they are self explanatory
*Note* 
    We are concentraing mostly on bios mode not uefi


    - [For linux](#linux)

```
dd if=/path/to/archlinux.iso of=/dev/sdx status=progress bs=4M
```



