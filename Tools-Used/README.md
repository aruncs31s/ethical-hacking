# Tools Used

## Hacking Tools
| Tool Name | Usage| 
|-----------|-------------|
|[`Metasploit`](#metasploit)|provides information about security vulnerabilities and aids in penetration testing|
| | |


## Utilities 
|Tool Name | Usage |
|----------|-------|
|[`apt`](#apt)|used to manage apps on debian based linux OS's|





### Metasploit
<!-- source = Wikipedia--> 
<p align=justify>
    The Metasploit Project is a computer security project that provides information about security vulnerabilities and aids in penetration testing and IDS signature development. It is owned by Boston, Massachusetts-based security company Rapid7
    </p>
    
### **Instalision**

#### **Linux**
```
 $ sudo apt install metasploit-framework

```
*if the following is not available*

```

wget http://downloads.metasploit.com/data/releases/metasploit-latest-linux-x64-installer.run

chmod +x ./metasploit-latest-linux-x64-installer.run

./metasploit-latest-linux-x64-installer.run

```
for more details check [here](https://adamtheautomator.com/install-metasploit-on-ubuntu/)

[official Website](https://www.metasploit.com)

[official Repository](https://github.com/rapid7/metasploit-framework)


### **apt**
<!-- source apt -h -->
  apt is a commandline package manager and provides
  commands for                                      searching and managing as well as querying information about packages.
  It provides the same functionality as the specialized APT tools,                                    like apt-get and apt-cache, but enables options more suitable for
  interactive use by default.

#### usage
apt [options] commands

- to install package :
```
 $ apt install package-name 
```
eg : $ apt install gimp
- to uninstall package :
```
$ apt remove package-name
```
eg : ```$ apt remove gimp```

#### most used commands

|Commands|Uses|
|---|---|
|list| list packages based on package names|
|search | search in package descriptions| |show | show package details|
|install|install packages|
|reinstall |reinstall packages |
|remove | remove packages|
|autoremove |automatically remove all unused packages|
|update | update list of available packages|
|upgrade | upgrade the system by installing/upgrading packages  |
|full-upgrade | upgrade the system by removing/installing/upgrading packages|
|edit-sources |edit the source information file|
|satisfy | satisfy dependency strings|

