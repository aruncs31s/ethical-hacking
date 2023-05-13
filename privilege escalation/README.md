- [Linux](#linux)
  -[CVE-2022-0847](#CVE-2022-0847)
  -[Dirty Cow`(CVE-2016-5195)](#Dirty Cow`(CVE-2016-5195))
<p align='justify'>
    Privilege escalation is the act of exploiting a bug, a design flaw, or a configuration oversight in an operating system or software application to gain elevated access to resources that are normally protected from an application or user   
    The result is that an application with more privileges than intended by the application developer or system administrator can perform unauthorized actions. 
</p>


[Source](https://en.wikipedia.org/wiki/Privilege_escalation)  




## Linux 

1. [`CVE-2022-0847`](#CVE-2022-0847)
<p align='justify'>
CVE-2022-0847, a vulnerability in the Linux kernel since 5.8 which allows overwriting data in arbitrary read-only files. This leads to privilege escalation because unprivileged processes can inject code into root processes.</p>

 ####  Support 

- Linux kernel versions newer than `5.8` are affected.

- Later fixed on `5.16.11` 
`5.15.25` 
`5.10.102`

### Requirements 

`gcc`



### Exploit 1

```

gcc CVE-2022-0847-exploit.c -o exploit-1

./exploit-1 
```

### Exploit 2

```

gcc CVE-2022-0847-exploit2.c -o exploit-2

find / -perm -4000 2>/dev/null

./exploit-2 /usr/bin/sudo

```



### Source / Credits 

- [link](https://dirtypipe.cm4all.com/)

- [link](https://github.com/febinrev/dirtypipez-exploit)

- [link](https://github.com/basharkey/CVE-2022-0847-dirty-pipe-checker)

- [link](https://github.com/AlexisAhmed/CVE-2022-0847-DirtyPipe-Exploits)


2. [`Dirty Cow`(CVE-2016-5195)](https://dirtycow.ninja/)

<p align="center">
    CVE-2016-5195 is the official reference to this bug. CVE (Common Vulnerabilities and Exposures) is the Standard for Information Security Vulnerability Names maintained by MITRE.
    </p>
    
#### Why is it called the Dirty COW bug?

"A race condition was found in the way the Linux kernel's memory subsystem handled the copy-on-write (COW) breakage of private read-only memory mappings. An unprivileged local user could use this flaw to gain write access to otherwise read-only memory mappings and thus increase their privileges on the system." (RH) - by [Dirtycow.ninja](https://dirtycow.ninja/)

to read more click [here](https://dirtycow.ninja/)


### Source / Credits 


[Dirty cow](https://github.com/dirtycow)
[Link](https://dirtycow.ninja/)

