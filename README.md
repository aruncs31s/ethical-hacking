## Under construction
[![License: GPL v3](https://img.shields.io/badge/License-GPLv3-blue.svg)](https://www.gnu.org/licenses/gpl-3.0)   [![fork](https://img.shields.io/github/forks/aruncs31s/ethical-hacking?color=green)](https://github.com/aruncs31s/ethical-hacking/network/members) [![status](https://img.shields.io/badge/status-building-red)](https://github.com/aruncs31s/ethical-hacking/commits?author=aruncs31s) [![commits](https://img.shields.io/github/commit-activity/m/aruncs31s/ethical-hacking?label=commits)](https://github.com/aruncs31s/ethical-hacking/commits?author=aruncs31s) [![contributers](https://img.shields.io/github/contributors/aruncs31s/ethical-hacking?color=%23ff0000&style=plastic)](https://github.com/aruncs31s/ethical-hacking/graphs/contributors)

# <h1 align="center">**Ethical-hacking**</h1>

- [**Introduction**](#introduction)
- [**Prerequisites**](#prerequisites)
  - [**Git**](./Documentations/Prerequisites/README.md#Git)
  - [**Github**](./Documentations/Prerequisites/README.md#Github)
  - [**Linux**](./Documentations/Prerequisites/README.md#Linux)

- [**Basics**](#basics)
  - [**Setting Up Hacking Environment**](#setting-up-hacking-environment)
  - [**Reconnaissance**](./Documentations/Basics/Reconnaissance.md) 
  - [**Proxy Servers and Stay Anonymous**](./Basics/README.md#proxy-servers-and-stay-anonymous)
  - [**WordList**](./Basics/README.md#wordlist)
- [**languages**](#languages)
  - [**Bash**](./languages/README.md#introduction-to-bash)
- [**Hacks**](#hacks)
  - [**Wifi password hacking**](/Hacks/Wifi%20Hacking/README.md)
- [**Scripts**](#scripts)
  - [**Payload Generator**](https://github.com/aruncs31s/ethical-hacking/blob/main/Scripts/payload-generator-script1.sh)
  - [**Neovim theme installer**](https://github.com/aruncs31s/neovim-vscode-theme/blob/main/install.sh)

- [Tools Used](#Tools-Used)

- [Team Members](#team-members)

- [Join us](#join-us)

- [Images](#images)

- [videos]()



<h2 align="center" id="introduction">Introduction</h2>
<p align="justify"><i>This is a free and open source project made by few students and anyone intrested sharing 
  hacking or linux skill or anyone willing to learn hacking are welcome here 
</i></p>

<h2 align="center">Disclimer</h2>
<p align="justify"><i>   This whole project is for educational purpose only and we suggest that you should gain full permission before doing anything on their network even before scanning</i></p>

<h2 align="center">What is this all about?</h2>
<p align="justify"><i class="discription">   We all know what hacking is and we've seen lot of hacker in movies right? the one always with masks and they just press one key and the system is hacked . That's not realy how things work a simple simple scan can even take more than the whole movie(depents on what your scanning).Inorder to be a hacker (or just to know how it works) we should at least know about linux and how to execute a command, becouse now days everything is available on github from simple phishing scripts to whole hacking framework, Hacking using those scripts still make you a hacker but you will be known as a "script kiddie" (the person who plays with scripts) and who does not even know what he is doing </i>
</p>

for more [click here](https://github.com/aruncs31s/ethical-hacking/tree/main/Introduction)


<h2 align="center" id="prerequisites"> <b> Prerequisites</b></h2>

<p align="justify"> followings are required to function effectively on this project and essential in bocoming an ethical hacker . You can skip this if you already know this or You can all this later</p>

- [**Git**](/Documentations/Prerequisites/README.md#git) 
- [**Github**](/Documentations/Prerequisites/README.md#github) 
- [**Linux**](/Documentations/Prerequisites/README.md#linux)

Learn more about it [here](/Documentations/prerequisites.md)
### **Linux**
Linux is a must have skill for any hacker or it professionals because you'll encounter it everywhere and you'll be doing all the hacks from a linux operating system like `kali` , `parrot` or `exodia`

### **Git**




<!-- - [Linux](./Pre-Requests#linux) -->
<!--     - [Rookie](./Pre-Requests#rookie) -->
<!--         - [Introduction]() -->
<!--         - [Firing Up]() -->
<!--     - [Intermediate](#intermediate) -->
<!--         - [Introduction]() -->
<!--         - [tty]() -->
<!--         - [Terminal]() -->
<!--     - [Expert](#expert) -->
<!-- - [Git](#git) -->
<!--     - [Introduction](#git-introduction) -->
<!--     - [Installition](#git-installition) -->
<!--     - [Working with Repos](#working-with-repositories) -->
<!--     -  -->
<!-- - [Github](#github) -->
<!-- - [Github-Readme.md](#github-readme) -->
<!-- - [Github-Fork](#github-fork) -->
<!---->
<!---->
[click here](https://github.com/aruncs31s/ethical-hacking/tree/main/Pre-Requests)






---

<h2 align=center id="setting-up-hacking-environment"><b>Setting Up hacking Environment</b></h2>

- [Introduction](#introduction)
- [Hacking OS](#hacking-os)
- [Installing ArchLinux](#installing-archlinux)
- [Setting up Black Arch](#setting-up-black-arch)
- [Adding a restricted user]()
- [Creating a restricted group]()


### **Introduction**
A hacking environment is essential for doing hacks.In good old days everyone has to setup their own hacking environment inorder to start hacking but nowdays some community/companies do this for you that is , they make an hacking os which comes with all the neccessary tools out of the box 
*In this section We will setup a hacking os and explore some pre-maid one's like kali and parrot os* *You are free to use any other hacking os like parrot os kali but "i" preffer to use arch/black arch for hacking* 

### **Hacking OS**
Hacking os is a premaid OS which shipps with hacking tools pre-installed , which saves time but increases system's size . So inorder to reduce we will setup a hacking os from just a normal `Arch` install iso. 

### **Installing ArchLinux**
Arch Linux simple and lightweight operating system . I choose Arch linux insted of Debian because  in arch linux you'll get the latest tools and packages and it only take as little as `77 MB` after installing.

Learn more about installing arch linux [here](./Pre-Requests/Environment.md#installing-archlinux)

### **Setting up Black Arch**
Black arch is is an arch based penetration testing operating system which has over 2800 tools. This makes installing hacking tools easy .

Learn more about setting up Black arch [here](./Pre-Requests/Environment.md#setting-up-black-arch)

### **Adding a restricted user**
It is not neccessary to add a restricted user but in some case or in my opinion it is good to isolate the user from accessing others files and obtaining `root` access etc.
- It isolates the restricted user from others
- Good if your using the same Operating System for personal use

Learn more about `Adding a restricted user` [here](./Pre-Requests/Environment.md#adding-a-restricted-user)

### **Creating a Restricted group**
Creating a restricted group also helps in isolating the user for example consider if you use `sudo` group or `wheel` group for hacking and they both can access `sudo` seamlessly like consider if you have a script that you downloaded from github or some place and you wont be able to execute it with super user permission if your using `restricted user` and we can control which program should get to run with `root` permission using `custom group`

Learn more about `Creating a restricted group` [here](./Pre-Requests/Environment.md#creating-a-restricted-group)

[More about Setting up hacking environment](/Pre-Requests/Environment.md)

---
<h2 align="center" id="Basics"> <b> Basics</b></h2>

- [**Reconnaissance**](#reconnaissance)

1. [**Proxy Servers and Stay Anonymous**](1.-proxy-servers-and-stay-anonymous)
2. [**Phishing**](https://github.com/aruncs31s/ethical-hacking/tree/main/Basics#phishing)

This sections's discus about all basic hacks [click here](https://github.com/aruncs31s/ethical-hacking/tree/main/Basics) to know more 

### **1. Proxy Servers and Stay Anonymous**
Staying anonymous is an importent thing in hacking as well as in surfing the internet. In the dark side of things the main advantage of staying anonymous is that you won't get caught. This section is highly recomented before anything else. and more about this [click here](./Basics#proxy-servers-and-stay-anonymous)



---
<h2 align="center" id="languages"> <b> Languages</b></h2>

- [Bash](https://github.com/aruncs31s/ethical-hacking/tree/main/languages)


## Reconnaissance

[Click here]()

<h2 align="center" id="cryptography"> <b> Cryptography</b></h2>

<p align="justify"><i>Cryptography</i> itself is a very huge topic and it will not fit in this simple markdown page and i dont have the time to explain it. So i will surf throught the surface and only point out the important stuffs .So in simple words cryptography is a tool used to make a data secure by coverting it into some format to make the information/data secure.</p>

Learn more about cryptography [here](./Basics/Crypto/Cryptography.md)
<h2 align="center" id="hacks"> <b> Hacks</b></h2>

- [Android Hacking](https://github.com/aruncs31s/ethical-hacking/tree/main/android-hacking)

- [privilege escalation](https://github.com/aruncs31s/ethical-hacking/tree/main/privilege%20escalation)

- [wifi password hacking](https://github.com/aruncs31s/ethical-hacking/tree/main/Wifi%20Hacking)



<h2 align="center" id="scripts"> <b> Scripts</b></h2>

*Followings are scripts made for this project*

- [payload-generator](https://github.com/aruncs31s/ethical-hacking/blob/main/Scripts/payload-generator-script1.sh)
- [Neovim theme installer](https://github.com/aruncs31s/neovim-vscode-theme/blob/main/install.sh)
- [Ransomeware](https://github.com/sonyt86/programming/blob/main/python/ransomware.py)

<h2 align="center" id="exploits"> <b> Exploits</b></h2>

- [CVE-2022-0847-exploit](https://github.com/aruncs31s/ethical-hacking/blob/main/Scripts/CVE-2022-0847-exploit.c)
- [CVE-2022-0847-exploit 2](https://github.com/aruncs31s/ethical-hacking/blob/main/Scripts/CVE-2022-0847-exploit.c2)

<h2 align="center" id="tools-used"> <b> Tools Used</b></h2>
[`Metasploit`](./Tools-used#metasploit)  `gcc`  `Nikto` `nmap` 

## Contact

[Telegram](https://t.me/+mqL4fZrUtEw0MjJl)

<h2 align="center" id="team-members"> <b> Team members</b></h2>

**Arun CS** [<img src="https://github.com/aruncs31s/ethical-hacking/blob/main/images/github-mark-white.png?raw=true" width="16"/>](https://github.com/aruncs31s/)  [<img src="https://github.com/aruncs31s/ethical-hacking/blob/main/images/telegram-logo-944.png?raw=true" width="16">](https://t.me/killadinjan)

**Amarnath**  [<img src="https://github.com/aruncs31s/ethical-hacking/blob/main/images/github-mark-white.png?raw=true" width="16"/>](https://github.com/amarnath749)

**Goutham Naik**  [<img src="https://github.com/aruncs31s/ethical-hacking/blob/main/images/github-mark-white.png?raw=true" width="16"/>](https://github.com/Gouthamexe)

**Anurag M K**  [<img src="https://github.com/aruncs31s/ethical-hacking/blob/main/images/github-mark-white.png?raw=true" width="16"/>]()

**Sony Thomas**  [<img src="https://github.com/aruncs31s/ethical-hacking/blob/main/images/github-mark-white.png?raw=true" width="16"/>](https://github.com/sonyt86)

**MaxStee**  [<img src="https://github.com/aruncs31s/ethical-hacking/blob/main/images/github-mark-white.png?raw=true" width="16"/>](https://github.com/Maxsteee)


**Anoop J J**  [<img src="https://github.com/aruncs31s/ethical-hacking/blob/main/images/github-mark-white.png?raw=true" width="16"/>]()

**Athul vv** [<img src="https://github.com/aruncs31s/ethical-hacking/blob/main/images/github-mark-white.png?raw=true" width="16"/>](https://github.com/athulvv1)

**Swetha Kc**  [<img src="https://github.com/aruncs31s/ethical-hacking/blob/main/images/github-mark-white.png?raw=true" width="16"/>]()

**Aslam**  [<img src="https://github.com/aruncs31s/ethical-hacking/blob/main/images/github-mark-white.png?raw=true" width="16"/>]()

**gouthamdaas** [<img src="https://github.com/aruncs31s/ethical-hacking/blob/main/images/github-mark-white.png?raw=true" width="16"/>](https://github.com/Gouthamdaas)

[**Anuranch C**](https://github.com/anuranch) [<img src="https://github.com/aruncs31s/ethical-hacking/blob/main/images/github-mark-white.png?raw=true" width="16"/>](https://github.com/anuranch)

### Join us
*you can join us and simply start learning together 
for more details contact [here](https://t.me/+mqL4fZrUtEw0MjJl)*

