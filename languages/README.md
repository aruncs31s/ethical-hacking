# *Bash* 
**currently beeing constrected in another repo**
*https://github.com/aruncs31s/bash*
- [Introduction](#introduction)
- [Creating a Script]()


# [Bash]()

### Pre-requests



## Introduction

--- 
<p align=justify>
    Shell Scripting is mainly used to automate taks with the help of shell scripting language and Bash is the most used of em' `Bash` is the default shell in allmost all linux operating systems 

</p>


_This repo will contain complete tutorial about bash_

- [Introduction](#introduction)
- [Basic commands](#basic-commands)
- [All commands used](#all-commands-used)
-

### Pre-requests

- a terminal
- bash or zsh installed

## Introduction
<p align="center">
![](https://github.com/aruncs31s/bash/blob/main/images/terminal.png?raw=true)

</p>
---

_Shell Scripting is mainly used to automate taks with the help of shell scripting language and Bash is the most used of em' `Bash` is the default shell in allmost all linux operating systems_

---

Type Following on any terminal

```
$ echo $BASH_VERSION

```

_this will print current version of bash you are using_

![alt-text](https://github.com/aruncs31s/ethical-hacking/blob/main/images/bash_version.png?raw=true)

**Important thing to note** _You can get full usage of almost any command in linux usig --help option with_ _sometimes -h also works and do the same_
eg:

```
> pwd --help
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

### Basic commands



| Commands | Description                                     |
| -------- | ----------------------------------------------- |
| [`ls`](#ls)     | List all the files in the current directry      |
| [`pwd`](#pwd)  | Print the name of the current working directory |
| `cd`     | change the current working directry             |
| `mv`| move files to directories or rename files|
|`cp`|copy files to directories |


## ***more about this below***

### ***ls***

_Normaly bash program will be situated under the /bin folder where almost all the user executable programs contains you can take a look at what inside that folder by_

```
$ ls /bin
```

_so we used `ls` to list all the files_

![ls](https://github.com/aruncs31s/bash/blob/main/images/ls.png?raw=ture)

*we can give some arguments to the ls command which will produce diffrent outputs*
*for example "-lh" argument combined with `ls` will show you the size of that file*

![](https://github.com/aruncs31s/bash/blob/main/images/ls%20-lh.png?raw=true)

> -l is used to use a long listing format

> -h is used to make it human readable 

**To see Other ls arguments and it's properties**  [`click here`](../languages/bash/README.md/#ls)


### ***pwd***










**File Related commands**





*****Linux programs found in /bin**
