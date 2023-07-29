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
- [Setting clock]()
- [Partitioning Disks]
- [Formating Drives]()
- [Mounting Drives]()
- [Install]

### **Introduction**
    Arch Linux simple and lightweight operating system . I choose Arch linux insted of Debian because  in arch linux you'll get the latest tools and packages and it only take as little as `77 MB` after installing

**Note** : free up some space to install linux and make a 1000 mb and 40 bg partition with any file system for `boot` and 'root'


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

### **Booting**
Booting Into arch live environment is pretty simple
- Plug the bootable usb
- Goto [BIOS](./Dictionary/README.md#BIOS) by pressing `F2` or `ESC` or `DEL` according to your latop/desktop
- Turn of secure boot if pressent and set the usb to highest priority in boot option
- Or you can skip above stage and press `F12` and select usb while booting (Works in some laptop/desktop)



### **Connecting to Internet**
After booting the usb the first thing you have to do is "connect you machine(latop/desktop) to the Internet",I highly prefer using [`usb tetherig`](./Dictionary/README.md#usb-tethering)

- USB tetherig
    - Take a usb data cable and plug it into the phone and laptop
    - In phone go to settings and turn on  usb tethering

Check you connection using [`ping`](./Dictionary/README.md#ping) 
```
$ ping google.com

```

### **Setting clock**

```
$ timedatectl set-timezone Asia/Kolkata
$ timedatectl set-ntp true

```


### **Partitioning Disks**
[`Partitioning`](./Dictionary/README.md#partitioning) Disks are the most coplicated steps in this whole proccess becouse if you select the wrong partition or delete the wrong partition you can loose the whole data in that partition . It is recomended that you partition or free up some space before booting into this live environment

|partition | Minimum size(recomended size)| 
|----------|-------------------|
| `/boot`  | `500 MB`          |
| '/'      | `25 GB` or more|
| `swap`   | `3 GB` | 

- *swap is not recomended if you have like more than 8gb of ram*
- `/boot` requres more storage if you are planing to install more kernals like `lts` an `zen`
- `root` partition usage will grow according to use 
- `/boot/efi` only for uefi systems

my partition scheme looks like in the below
```
NAME        MAJ:MIN RM   SIZE RO TYPE MOUNTPOINTS
sda           8:0    0 931.5G  0 disk
├─sda1        8:1    0 195.3G  0 part
├─sda2        8:2    0  97.7G  0 part
└─sda3        8:3    0 638.5G  0 part
nvme0n1     259:0    0 223.6G  0 disk
├─nvme0n1p1 259:1    0  1001M  0 part /boot/efi
├─nvme0n1p2 259:2    0  58.6G  0 part /
├─nvme0n1p3 259:3    0   9.8G  0 part [SWAP]
├─nvme0n1p4 259:4    0    16M  0 part
├─nvme0n1p5 259:5    0  78.1G  0 part
├─nvme0n1p6 259:6    0   954M  0 part
└─nvme0n1p7 259:7    0  75.2G  0 part

```

![lsblk](./images/lsblk-arch.png?raw=true)
![df](./images/df-arch.png?raw=ture)

