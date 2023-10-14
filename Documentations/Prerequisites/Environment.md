## **Setting Up hacking Environment**
- [Introduction](#introduction)
- [Hacking OS](#hacking-os)
- [Installing ArchLinux](#installing-archlinu)
- [Setting up Black Arch](#setting-up-black-arch)
- [Adding a restricted user](#adding-a-restricted-user)
- [Creating a restricted group](#creating-a-restricted-group)

### **introduction**
A hacking environment is essential for to do hacking .In good old days everyone has to setup their own hacking environment inorder to start hacking but nowdays some community/companies do this for you that is , they make an hacking os which comes with all the neccessary tools out of the box 
*In this section We will setup a hacking os and explore some pre-maid one's like kali and parrot os* *You are free to use any other hacking os like parrot os kali but "i" preffer to use arch/black arch for hacking*

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
- [Partitioning Disks]()
    - [UEFI](#uefi)
    - [BIOS](#bios)
- [Formating Drives]()
- [Mounting Drives]()
- [Install packages to new root]()

### **Introduction**
Arch Linux simple and lightweight operating system . I choose Arch linux insted of Debian because  in arch linux you'll get the latest tools and packages and it only take as little as `77 MB` after installing.

**Note** : free up some space to install linux and make a 1000 MB and 40 GB partition with any file system for `boot` and 'root'


### **Downloading ISO**
    Goto [Archlinux/Downloads](https://archlinux.org/download/) then download the iso 


### **Making Bootable Pendrive**
- [For windows](#windows)
        for those who are using windows you have to download either ["Rufus"](https://rufus.ie/) or ["Balena Etcher"](https://etcher.balena.io/) they are self explanatory
*Note* 
    We are concentraing mostly on bios mode not uefi


- [For linux](#linux)

```
$ dd if=/path/to/archlinux.iso of=/dev/sdx status=progress bs=4M
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
- UEFI

![lsblk](./images/lsblk-arch.png?raw=true)
![df](./images/df-arch.png?raw=ture)


You can see that i have mounted `/boot/eft` in `nvme0n1p1` and `/` in `nvme0n1p2` and `swap` in `nvme0n1p3` . I have `/boot/efi` insted of `/boot` because i have a uefi system but the procedures are almost same and uefi does not require this much space as 1GB but i have given it anyways. you can see that in second screenshot
```
/dev/nvme0n1p1   1022976    10252   1012724   2% /boot/efi
```
where `/boot/efi` is only using `2%` from its alocated size `1GB`

- BIOS

![lsblk-bios](./images/lsblk-df-bios.png?raw=true)

this screenshot shows a pation scheme of a bios in th is we can see that `/boot` have used 23% from the alocated size with only 2 kernals installed and the mounting poin is `/` snd `/boot` insted `/boot/efi` 



### **Formating Disks**
we use [`mkfs`](./Dictionary/README.md#mkfs) for Formating the Drives

imagine `/dev/sda1` is your `/boot` partition and `/dev/sda2` is your `root` or `/` partition then 

- for BIOS

```
$ mkfs.ext4 /dev/sda1 -L ARCHBOOT
$ mkfs.ext4 /dev/sda2 -L ARCHROOT

```

- for UEFI
consider `/dev/sda1` as your uefi partition

```
$ mkfs.fat -F 32 /dev/sda1 -n ARCHUEFI
$ mkfs.ext4 /dev/sda2 -L ARCHROOT
```
*here `-n` and `-L` are used to set labels for the partition*



*you can setup swap partition later*

### Mounting Drives

- BIOS

```
$ mount /dev/sda2 /mnt

$ mkdir /mnt/boot

$ mount /dev/sda1 /mnt/boot
```

- UEFI

```
$ mount /dev/sda2 /mnt

$ mkdir -p /mnt/boot/efi

$ mount /dev/sda1 /mnt/boot/efi


```

### **Install packages to new root*

```
$ pacstrap -K /mnt linux linux-firmware base vim nano networkmanager

```

- You can install some of your fav apps and your preffered editor now 
- It is recomended that you install [`networkmanager`](./Dictionary/README.md#networkmanager) 

### **Generating fstab**

```
$ genfstab -U /mnt >> /mnt/etc/fstab
```

### **Some more mandatory setups**
**This step include**
- Setting Up Time Zone.
- Generate Hardware Clock Settings.
- Set Up Language Settings(Locale)
- setting passwd for the root user
- Installing GRUB bootloader


- [`chroot`](./Dictionary/README.md#chroot) into new root

```
$ arch-chroot /mnt
```
- Create a soft link to your set-timezone

```
$ ln -sf /usr/share/zoneinfo/Asia/Kolkata /etc/localtime


```
- Language setup
```
$ echo en_US.UTF-8 UTF-8 >> /etc/locale.gen

$ locale-gen

```

- Setting hostname

```
$ echo archLinux > /etc/hostname
```

- **setting Root user password**

```
$ passwd
```
*Note* : password will not show when you are typing 

**!if you skip this step you will not be able to login to your system after reboot**

- adding hosts

add this in your `/etc/hosts`

```
$ nano /etc/hosts
```

- type the following 
```
127.0.0.1 localhost
::        localhost

```

- after typing 
- Press `CTRL O` and press enter
- Press `CTRL X` to exit


### Installing The GRUB bootloader

```
$ pacman -S grub os-prober

```
- for BIOS
```
$ grub-install /dev/sda1 
$ grub-mkconfig -o /boot/grub/grub.cfg
```

- for UEFI

```
$ grub-install --target=x86_64-efi --bootloader-id=grub --efi-directory=/boot/efi

$ grub-mkconfig -o /boot/grub/grub.cfg
```

- now press `CTRL d`


-  now remove the usb and reboot your system 

```
$ reboot

```

### **Essentials**
after rebooting

username will be = root

Enable the NetworkManager
```
systemctl enable NetworkManager
systemctl start NetworkManager

```
and use `nmtui` to connect to networks



## **Setting Up Black Arch**
Black arch is is an arch based penetration testing operating system which has over 2800 tools.I am assuming that you have installed the arch linux on your pc/laptop/... or you have alredy have it on your system.  Now we have to install blackarch into your arch linux installition which makes installing tools easy 
![Blackarch](./images/blackarch_fluxbox.jpg?raw=true)

click [here](https://blackarch.org/) to know more
### Installing

```
$ sudo sh $(curl -fsSL https://blackarch.org/strap.sh)

```

- To install balckarch tools
```
$ sudo pacman -S blackarch-<category>


```
- To see all blackarh categories
```
$ sudo pacman -Sg | grep blackarch
```

## **Adding a restricted user**
*replace all <username> with desired name*
It is not neccessary to add a restricted user but in some case or in my opinion it is good to isolate the user from accessing others files and obtaining `root` access etc.
- It isolates the restricted user from others
- Good if your using the same Operating System for personal use

### **Setps to create a new restricted user**
- Create a new user
```
$ userdd -m <newuser> -s /bin/rbash
```
*rbash or restricted bash is used restrict the shell of new user*

- set password for new user
```
$ passwd <newuser>
```
- add new user to sudo group
```
sudo usermod -aG sudo <newuser>

```
*you can also create a new group other than sudo to limit even further more details will be posted later*

![rbash](./images/rbash.png)
*You can see that the user is restricted to use certain commands*


## **Creating a restricted group**
Creating a restricted group also helps in isolating the user for example consider if you use `sudo` group or `wheel` group for hacking and they both can access `sudo` seamlessly like consider if you have a script that you downloaded from github or some place and you wont be able to execute it with super user permission if your using `restricted user` and we can control which program should get to run with `root` permission using `custom group` 

### **Setting up a restricted user**
*replace all <groupname> with desired name*
- Add a new group
```
$ groupadd <groupname>
```
- Adding users to group
    - Adding existing user
    ```
    $ usermod -aG <groupname> <username>
    ```
    - Creating a new user with this group
    ```
    $ useradd -G <groupname> -m -s /bin/rbash
    ```
- Editing `/etc/sudoers` file to restrict sudo access


```
$ sudo visudo 
```
and you will see the following window

![visudo](./images/sudo-visudo.png?raw=true)

- add the following lines to restrict group/users within the group
```
%<groupname> ALL=(ALL:ALL) /usr/bin/nmap, /usr/bin/aircrack-ng
```
*you can add more programs ass above and dont forgot to put `,` `comma`
