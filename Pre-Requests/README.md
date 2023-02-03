## Pre-Requests

Inorder to Upload it `documentations` and `stuff` to Github you need to know the following things
- [Linux](#linux)
    - [Rookie](#rookie)
        - [Introduction]()
        - [Firing Up]()
    - [Intermediate](#intermediate)
        - [Introduction]()
        - [tty]()
        - [Terminal]()
    - [Expert](#expert)
- [Git](#git)
    - [Introduction](#git-introduction)
    - [Installition](#git-installition)
    - [Working with Repos](#working-with-repositories)
    - 
- [Github](#github)
- [Github-Readme.md](#github-readme)
- [Github-Fork](#github-fork)

### Linux
  Linux is easy and the same difficult to understand if you don't have enough technical knowledge . I have devided this tutorial for Rookie,Intermediate,Expert so that you can choose according to you level
  
#### Linux for Rookies
  
  
  

### Git
- [Introduction](#gitintroduction)
- [Installation](#git-installation)
- [Working with Repositories ](#working-with-repositories)
#### **Git Introduction**

  Git is a `source control` created for the `Linux` Kernel by `Linus Torvalds`. Git works the familiar primitives of source control management systems such as `commits`, `diffs`,` trunks, tags, branches, and so on. However, Git has the intrinsic property of being a distributed system - a system in which there is no official client/server relationship. Each repository contains the entire history of revisions. This means that there's no need to have network access or synchronization to a central repository. In essence, a git repository is nonlinear with regard to revisions. two different users may change source code in unique, independent ways without interfering with each other. one benefit of this model is that developers are freer to independently work with, experiment with, and tweak code.
	Git supports independent development and revision management, it also supports the means to share and incorporate revisions made in unsynchronized repositories.

#### Git Installition
If your using `debian` based os you should have [`apt`](../Tools-Used#apt) or if yiu have `arch` based os you shold have `pacman`


#### Working with Repositories 
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
**Note:***you should edit the README.md file before commiting it othewise it would be jsut a text file also you can add any file by  
```
~/new_project$ mv filename ~/new_project 
~/new_project$ git add filename 
~/new_project$ git commmit -m filename
```

**Note:***You can sjust simply add all file by `$ git add .`*
- **Creating a new repository**
	- goto github.com
	
	![github](https://github.com/aruncs31s/ethical-hacking/blob/main/images/github-addressbar.png?raw=true)
	
	- create a new repository 

	![create repo](https://github.com/aruncs31s/ethical-hacking/blob/main/images/create-new-repo-1.png?raw=true)
	
	![create repo](https://github.com/aruncs31s/ethical-hacking/blob/main/images/create-new-repo-2.png?raw=true)
	
	*Click on create repository*
	
	- copy the repo link 
	 
	 ![repo link](https://github.com/aruncs31s/ethical-hacking/raw/main/images/clone%20repo.png)
	
	



### Github 
  Github itself is selfexplanatory just goto [https://github.com](https://github.com)


#### Tutorial 

- [ `Youtube ` Malayalam](https://youtu.be/aJ1cbdMdfys)


###  Github-Readme



#### Tutorials 

- [ `Web documentation`](https://docs.github.com/en/get-started/writing-on-github/getting-started-with-writing-and-formatting-on-github/basic-writing-and-formatting-syntax)
- [ `Web documentation` ](https://medium.com/analytics-vidhya/writing-github-readme-e593f278a796#:~:text=For%20a%20line%20break%20or,more%20spaces%2C%20and%20hit%20enter.)
- [`Youtube` English](https://youtu.be/yXY3f9jw7fg)
- [`Youtube` Malayalam]()

### Github-Fork



#### Tutorial

[`Web documentation`](https://docs.github.com/en/get-started/quickstart/fork-a-repo)
