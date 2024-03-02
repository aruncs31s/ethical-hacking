## **Pre-Requests**

Inorder to Upload it `documentations` and `stuff` to Github you need to know the following things
- [Linux](./Linux.md)
  - [linux for Hackers](./Linux.md#linux-for-hackers)
  - [Installition](#installition)

- [Git](./Git.md)
    - [Introduction](./Git.md#git%20introduction)
    - [Installition](./Git.md#git-installition)
    - [Working with Repos](#working-with-repositories)
    - 
- [Github](./github.md)

- [Github-Readme.md](#github-readme)
- [Github-Fork](#github-fork)


---
<!---->
<!-- ## Git -->
<!---->
<!-- - [Introduction](#gitintroduction) -->
<!-- - [Installation](#git-installation) -->
<!-- - [Basics](#git%20basics) -->
<!-- - [Working with Repositories ](#working-with-repositories) -->
<!---->
<!-- ### **Git Introduction** -->
<!---->
<!--   Git is a `source control` created for the `Linux` Kernel by `Linus Torvalds`. Git works the familiar primitives of source control management systems such as `commits`, `diffs`,` trunks, tags, branches, and so on. However, Git has the intrinsic property of being a distributed system - a system in which there is no official client/server relationship. Each repository contains the entire history of revisions. This means that there's no need to have network access or synchronization to a central repository. In essence, a git repository is nonlinear with regard to revisions. two different users may change source code in unique, independent ways without interfering with each other. one benefit of this model is that developers are freer to independently work with, experiment with, and tweak code. -->
<!-- 	Git supports independent development and revision management, it also supports the means to share and incorporate revisions made in unsynchronized repositories. -->
<!---->
<!-- ### **Git Installition** -->
<!-- If your using `debian` based os you should have [`apt`](https://github.com/aruncs31s/ethical-hacking/tree/main/Tools-Used#apt) or if yiu have `arch` based os you shold have `pacman` -->
<!---->
<!---->
<!---->
<!-- ### **Working with Repositories** -->
<!--   _You can either create( initialize ) or clone a repository._  -->
<!-- - **Initializing a repository** -->
<!--  ``` -->
<!-- ~$ mkdir new_project -->
<!-- ~$ cd new_project -->
<!-- ~/new_project$ git init -b main -->
<!--  ``` -->
<!--  - **Adding a file** -->
<!-- ``` -->
<!-- ~/new_project$ touch README.md -->
<!-- ~/new_project$ git add README.md  -->
<!-- ~/new_project$ git commit -m README.md -->
<!--   -->
<!-- ``` -->
<!-- **Note:** *you should edit the README.md file before commiting it othewise it would be jsut a text file also you can add any file by*  -->
<!-- ``` -->
<!-- ~/new_project$ mv filename ~/new_project  -->
<!-- ~/new_project$ git add filename  -->
<!-- ~/new_project$ git commmit -m filename -->
<!-- ``` -->
<!---->
<!-- **Note:***You can sjust simply add all file by `$ git add -A`* -->
<!-- - **Creating a new repository** -->
<!-- 	- goto github.com -->
<!-- 	 -->
<!-- 	![github](/images/github-addressbar.png?raw=true) -->
<!-- 	 -->
<!-- 	- create a new repository  -->
<!---->
<!-- 	![create repo](/images/create-new-repo-1.png?raw=true) -->
<!-- 	 -->
<!-- 	![create repo](/images/create-new-repo-2.png?raw=true) -->
<!-- 	 -->
<!-- 	*Click on create repository* -->
<!-- 	 -->
<!-- 	- copy the repo link  -->
<!-- 	 &#160; -->
<!---->
<!-- 	 ![repo link](/images/clone%20repo.png) -->
<!-- 	 -->
<!-- 	 -->
<!-- * Now open the terminal and navigate to your project repository -->
<!---->
<!-- ``` -->
<!-- ~/new_project$ git remote add origin https://github.com/<username>/new_project git -->
<!---->
<!-- ~/new_project$ git branch -M main -->
<!---->
<!-- ~/new_project$ git push -u origin main -->
<!---->
<!-- ``` -->
<!---->
<!-- <details><summary> <b>Notes :</b> </summary> -->
<!---->
<!-- *Here `new_project` is my project name and you can give any name if you want but you have to replce `new_project` with your project name*  -->
<!---->
<!-- </details> -->
<!---->
<!-- --- -->


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
