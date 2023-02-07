



# Languages

- [Bash](#bash)



## Bash

- [Introduction](#introduction)
- [Basic commands](#basic-commands)
- [Paths](#paths)
-

### Pre-requests



## Introduction
--- 
          Shell Scripting is mainly used to automate taks with the help of shell scripting language, and Bash is the most used of em' `Bash` is the default shell in allmost all linux operating systems 


_This repo will contain complete tutorial about bash_

- [Introduction](#introduction)
- [Basic commands](#basic-commands)
- [Paths](#paths)
-

### Pre-requests
- PC or Termux or ish
- a terminal
- bash or zsh installed

## Introduction
<!-- 
<img align="center"  src="https://github.com/aruncs31s/bash/blob/main/images/terminal.png?raw=true">

<img  src="">

-->
---


_Shell Scripting is mainly used to automate taks with the help of shell scripting language and Bash is the most used of em' `Bash` is the default shell in allmost all linux operating systems_

---

Type Following on any terminal

```
$ echo $BASH_VERSION

```


this will print current version of bash you are using



<img src="https://github.com/aruncs31s/ethical-hacking/blob/main/images/bash_version.png?raw=true">


<details>
<summary>echo :</summary>
<a href="#echo">echo  </a>is same as printf in c programming or print in python programming the oly diffrence is more like the main diffrence is in its syntax , that it does not need a bracket before giving the strings as its arguments or the value that you want to display into the monitor/screen in this case

</details>
<details>
<summary>$ :</summary>

$ 

</details>



<details>
<summary>Notes: </summary>You can get full usage of almost any command in linux usig --help option with_ _sometimes -h also works and do the same_
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

</details>

## Basic commands

| Commands |  Description           |
| :--------: | ------------------------ |
|[`mkdir`](#mkdir)| To make a directories/directory(folder)|
| [`ls`](#ls)     | List all the files in the current directry      |
| [`pwd`](#pwd)  | Print the name of the current working directory |
| [`cd`](#cd)     | change the current working directry             |
| [`mv`](#mv)| move files to directories or rename files|
|[`cp`](#cp)|copy files to directories |


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

<img src="https://github.com/aruncs31s/bash/blob/main/images/ls.png?raw=true">




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

#### Usage

``` 
cd /path/to/the/folder

```

![ls-pwd](../images/ls-pwd.png)

<details>
<summary>Notes</summary>
<p>
*we can see there is a folder named test in our current working directry*</p>

</details>
Tip: We used [`ls`](#ls) command to list(to see as a list) the files

![ls-pwd](../images/ls-pwd-cd.png)
*Dont confuse with that path name we will cover that 
linux file system arangement* 

*Now 






## Paths

**HOME**
*home path will be always be your /home/username unless you cange it*

![home](./bash/images/echo%20%24HOME.png)

*Also `~` this symbol is linked to HOME variable/reference*

![~](./bash/images/echo%20~.png)

