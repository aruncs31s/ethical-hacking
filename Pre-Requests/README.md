## **Pre-Requests**

Inorder to Upload it `documentations` and `stuff` to Github you need to know the following things
- [Linux](#linux)
  - [linux for Hackers](#linux-for-hackers)
  - [Installition](#installition)

- [Git](#git)
    - [Introduction](#git-introduction)
    - [Installition](#git-installition)
    - [Working with Repos](#working-with-repositories)
    - 
- [Github](#github)

- [Github-Readme.md](#github-readme)
- [Github-Fork](#github-fork)

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

  
#### Linux for Rookies
  
---

## Git
- [Introduction](#gitintroduction)
- [Installation](#git-installation)
- [Working with Repositories ](#working-with-repositories)
### **Git Introduction**

  Git is a `source control` created for the `Linux` Kernel by `Linus Torvalds`. Git works the familiar primitives of source control management systems such as `commits`, `diffs`,` trunks, tags, branches, and so on. However, Git has the intrinsic property of being a distributed system - a system in which there is no official client/server relationship. Each repository contains the entire history of revisions. This means that there's no need to have network access or synchronization to a central repository. In essence, a git repository is nonlinear with regard to revisions. two different users may change source code in unique, independent ways without interfering with each other. one benefit of this model is that developers are freer to independently work with, experiment with, and tweak code.
	Git supports independent development and revision management, it also supports the means to share and incorporate revisions made in unsynchronized repositories.

### **Git Installition**
If your using `debian` based os you should have [`apt`](https://github.com/aruncs31s/ethical-hacking/tree/main/Tools-Used#apt) or if yiu have `arch` based os you shold have `pacman`

<details><summary> <b>Notes :</b> </summary>

Install [`gh`](https://cli.github.com/) which is a cli version of github and it is easier this was to to login to your github account through `git`

</details>



### **Working with Repositories**
  _You can either create( initialize ) or clone a repository._ 
- **Initializing a repository**
 ```
~$ mkdir new_project
~$ cd new_project
~/new_project$ git init -b main
 ```
 - **Adding a file**
```
~/new_project$ touch README.md
~/new_project$ git add README.md 
~/new_project$ git commit -m README.md
 
```
**Note:** *you should edit the README.md file before commiting it othewise it would be jsut a text file also you can add any file by* 
```
~/new_project$ mv filename ~/new_project 
~/new_project$ git add filename 
~/new_project$ git commmit -m filename
```

**Note:***You can sjust simply add all file by `$ git add -A`*
- **Creating a new repository**
	- goto github.com
	
	![github](https://github.com/aruncs31s/ethical-hacking/blob/main/images/github-addressbar.png?raw=true)
	
	- create a new repository 

	![create repo](https://github.com/aruncs31s/ethical-hacking/blob/main/images/create-new-repo-1.png?raw=true)
	
	![create repo](https://github.com/aruncs31s/ethical-hacking/blob/main/images/create-new-repo-2.png?raw=true)
	
	*Click on create repository*
	
	- copy the repo link 
	 &#160;

	 ![repo link](https://github.com/aruncs31s/ethical-hacking/raw/main/images/clone%20repo.png)
	
	
* Now open the terminal and navigate to your project repository

```
~/new_project$ git remote add origin https://github.com/<username>/new_project git

~/new_project$ git branch -M main

~/new_project$ git push -u origin main

```

<details><summary> <b>Notes :</b> </summary>

*Here `new_project` is my project name and you can give any name if you want but you have to replce `new_project` with your project name* 

</details>

---

## **Github**
  Github itself is selfexplanatory just goto [https://github.com](https://github.com)


### **Tocken Generation**


![video](../video/tocken_generation.gif)

---
### **Tutorial** 

- [ `Youtube ` Malayalam](https://youtu.be/aJ1cbdMdfys)


##  **Github-Readme**



### **Tutorials** 

- [ `Web documentation`](https://docs.github.com/en/get-started/writing-on-github/getting-started-with-writing-and-formatting-on-github/basic-writing-and-formatting-syntax)
- [ `Web documentation` ](https://medium.com/analytics-vidhya/writing-github-readme-e593f278a796#:~:text=For%20a%20line%20break%20or,more%20spaces%2C%20and%20hit%20enter.)
- [`Youtube` English](https://youtu.be/yXY3f9jw7fg)
- [`Youtube` Malayalam]()

---

## **Github-Fork**
&#160;&#160;&#160;&#160;&#160;You can use either `Web browser` or [`gh`](https://cli.github.com/) 


### **Tutorial**

[`Web documentation`](https://docs.github.com/en/get-started/quickstart/fork-a-repo)

#### **Using gh**

```
$ gh repo fork REPOSITORY

```

#### **Using Web Browser**

1. **Go to the repository which you want to fork**

2. **Click on the drop down menu button named `fork`**
![](/images/fork2.png?raw=ture)
3. **Then click on the &#160;&#160;`+ create a new fork`**

![](/images/fork3.png?raw=true)

4. **Now click on the <button style="background-color: #4CAF50;" type="button" >Create fork</button> buttton**




---