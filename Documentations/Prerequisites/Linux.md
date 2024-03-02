### **Linux**
  Linux is a free and open source operating system that uses linux kernal and mainained by FOSS developers. Linux is easy and the same difficult to understand if you don't have enough technical knowledge, it is also to be noted that you will never learn linux unless u actually use it . It is just like windows and macos but it is free and open source so you dont have to pay anything to get it working on your machine . It can be installed on a hardware as small as your home router in fact linux is the lites among all other os's . 
#### **Linux for Hackers**
  Most of the time(aproximately all the time) a hacker will use Linux for their hacking purpose Hacking os to be exact . A Hacking os comes with pre installed tools for hacking and other usefull tools which helps them to make hacking ease . Some examples of such os are `Kali linux`([click here](https://www.kali.org/docs/) to know more) by offensive security , `Parrot os`( [Click here](https://www.parrotsec.org/) to know more) by [Some good developers](https://www.parrotsec.org/team/) and `Balck arch`

#####  **Parrot os** 
  ![Parrot os](/images/ParrotOS-4.6-plasma.jpg?raw=true)<!-- source wikkipedia https://en.wikipedia.org/-->
  Parrot os is a debian based linux distro specially for hackers and security specialists and can be also used for normal computing tasks like watching movies surfing the internet the good stuffs . Intrestingly enough they have the like special purpose versions for `Penetration Testing and Red Team operations` that is the ` Security edition` and <!-- by parrotsec --> `Home edition` for normal use so on 

![paroot\ os](/images/parrot_os_versions.jpg)

#### **Installition**
  It is pretty easy to install linux on older hardware compared to newer once and there are plety of installers out there which comes with automated scripts to install linux and if you are very intrested in hard working you can also try to install a linux distro called `Arch linux` which is difficult to install but offers more control over what your installing
  &#160;&#160;&#160;&#160;&#160;When its comes to installing linux you have to chose from overweling amount of distros which is the most complicated decition among these installing steps for example there is `Ubuntu` , `Manjaro` , `Mint` , `MX linux` the list will go on and on an  on, i will recomment `Linux Mint` or `Ubuntu` if your new to Linux but we are intrested in Hacking So we will choose either `kali linux` , `Paroot os` or `Black arch` 






















#### Linux File System

![linux file system](../images/linux-file-system.webp?raw=true) 

**/bin :**  
<details>
<summary>Notes: </summary>You can get full usage of almost any command in linux usig --help option with_ _sometimes -h also works and do the same_
eg:

```
$ pwd --help
```

output

```
pwd: pwd [-LP]
    Print the name of the current working directory.                                                                                                            Options:
      -L        print the value of $PWD if it names the current working directory
      -P        print the physical directory, without any symbolic links

    By default, `pwd' behaves as if `-L' were specified.
                                                                                  Exit Status:
    Returns 0 unless an invalid option is given or the current directory
    cannot be read
```
</details>


--- 
## Basic commands

| Commands |  Description           |
| :--------: | ------------------------ |
|[`mkdir`](#mkdir)| To make a directories/directory(folder)|
| [`ls`](#ls)     | List all the files in the current directry      |
| [`pwd`](#pwd)  | Print the name of the current working directory |
| [`cd`](#cd)     | change the current working directry             |
| [`mv`](#mv)| move files to directories or rename files|
|[`cp`](#cp)|copy files to directories |
| [`rm`](#rm)| To remove files/directories | 

## ***more about this below***

### ***mkdir***
  *[`mkdir`](#mkdir) (make directory)*  is used to create directory(folder) or miltiple directories (folders)

*we can create a folder called new-directory using mkdie*

```
$ mkdir new-folder

```

![mkdir](./bash/images/ls-mkdir.png)

[`mkdir`](#mkdir)o list out folders and files the current working directory



*we can also create multiple directories using [`mkdir`](#mkdir)* 


![cd-mkdir](./bash/images/cd-mkdir.png)

![multiple-mkdir](./bash/images/multiple-mkdir.png)

*we can see that if we type more names after  [`mkdir`](#mkdir) it creates mutliple [`directory`](../Dictionary#directory)*

*So the basic syntax of mkdir is*

```
$ mkdir <foldername> <foldername2> ...

```
learn more about `mkdir`     [here](https://www.gnu.org/software/coreutils/mkdir)


### ***ls***

_Normaly bash program will be situated under the /bin folder where almost all the user executable programs contains you can take a look at what inside that folder by_

```
$ ls /bin
```

_so we used `ls` to list all the files_

<img src="../images/ls.png">




<details>
<summary>Notes: </summary>
*we can give some arguments to the ls command which will produce diffrent outputs*
*for example "-lh" argument combined with `ls` will show you the size of that file*
</details>


![](https://github.com/aruncs31s/bash/blob/main/images/ls%20-lh.png?raw=true)

> -l is used to use a long listing format

> -h is used to make it human readable 

*Learn more about  `ls`  [here](https://www.gnu.org/software/coreutils/ls) 

### ***pwd***
  *`pwd` is used to know your [current directory](../Dictionar#current-directory)*

![pwd](./bash/images/pwd.png)

*The /home/aruncs folder have an nother property it is yout home path* [more about this](#paths)



### ***cd***
  `cd` is used for changing working [`directries`](../Dictionary/README.md/#directory)(folder)


<details>
<summary>Notes</summary>
*To understand this simply consider if we have to delete a file which we have downloaded from internet and we dont know it's name but it is in the folder `$HOME/Downloads` we can do this in many ways azbut one of the easyest way is to go into the folder and inspect the files and delete the one that we dont need suppose we want to delete song.mp3 form download ; we first need to go to the folder specified above so inorder to go to that folder we use `cd`(change directory) command*
</details>

#### **Usage**

``` 
cd /path/to/the/folder

```



![ls-pwd](../images/ls-pwd.png)

we can see there is a folder named test in our current working directry


Tip: We used [`ls`](#ls) command to list(to see as a list) the files

![ls-pwd](../images/ls-pwd-cd.png)

*Dont confuse with that path name, we will cover that one in
linux file system* 

*So specified the path name after cd , after that we can see that our current directory is changed to `/tmp/test/test` before it was `/tmp/test`

### **cp**

**cp** is used to copy files/folders  




#### **Usage**
```
cp old_name new_name 
```
which renames file named name1 to name2 

**Note:** We can use cp to copy folders as well as files 

<details><summary>Explenation: </summary>

</details>

```
$ ls

song.mp3

$ cp song.mp3 old_song.mp3 

$ ls

old_song.mp3
```

</details>




---
### **mv**
**mv** is mainly used to move or renames files the 

#### **Uses**

```
mv old_name new_name

```


##### **Files**
```
mv old_name new_name
```

**Note:** We can use `mv` to rename both folders and files


<details><summary>Explenation: </summary>

f
</details>

---
### **rm**
    `rm` is used to remove files or folders, 

#### **Usage**

```
rm file_name

rm folder_name


```
<details><summary>Note: </summary>Inorder to remove folders/directories you need to use `--recursive` `-r` and you can also force the deletion using `-f` `--force` argument</details>

[more details](https://gnu.org/software/coreutils/rm)

```
$ ls

song.mp3

$ rm song.mp3

$ ls

$
```



## **Paths**

*We can check the current Varriables that are beeing used by just typing system

```
$ set
BASH=/usr/bin/bash
BASHOPTS=checkwinsize:cmdhist:complete_fullquote:expand_aliases:extglob:extquote:force_fignore:globasciiranges:histappend:interactive_comments:progcomp:promptvars:sourcepath
BASH_ALIASES=()
BASH_ARGC=([0]="0")
BASH_ARGV=()
BASH_CMDS=()
BASH_COMPLETION_VERSINFO=([0]="2" [1]="11")
BASH_LINENO=()
BASH_REMATCH=()
BASH_SOURCE=()
BASH_VERSINFO=([0]="5" [1]="1" [2]="4" [3]="1" [4]="release" [5]="x86_64-pc-linux-gnu")
BASH_VERSION='5.1.4(1)-release'
COLORTERM=truecolor
COLUMNS=127
COMP_WORDBREAKS=$' \t\n"\'><=;|&(:'
DBUS_SESSION_BUS_ADDRESS=unix:path=/run/user/1000/bus
DESKTOP_SESSION=lightdm-xsession
DIRSTACK=()
DISPLAY=:0.0
EUID=1000
GDMSESSION=lightdm-xsession
GPG_AGENT_INFO=/run/user/1000/gnupg/S.gpg-agent:0:1
GROUPS=()
GTK_MODULES=gail:atk-bridge
GTK_OVERLAY_SCROLLING=0
HISTCONTROL=ignoreboth
HISTFILE=/home/axux/.bash_history
HISTFILESIZE=2000
HISTSIZE=1000
HOME=/home/axux
HOSTNAME=parrot
HOSTTYPE=x86_64
IFS=$' \t\n'
```

**HOME**

*home path will be always be your /home/username unless you cange it*

![home](/languages//bash/images/echo%20%24HOME.png)

*Also `~` this symbol is linked to HOME variable/reference*

![~](/languages//bash/images/echo%20~.png)


