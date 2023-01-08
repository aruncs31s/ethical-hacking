- [Linux](#linux)

<p align='justify'>
    Privilege escalation is the act of exploiting a bug, a design flaw, or a configuration oversight in an operating system or software application to gain elevated access to resources that are normally protected from an application or user   
    The result is that an application with more privileges than intended by the application developer or system administrator can perform unauthorized actions. 
</p>

 ####  Support 

- Linux kernel versions newer than `5.8` are affected.

- Later fixed on `5.16.11` 
`5.15.25` 
`5.10.102`


[Source](https://en.wikipedia.org/wiki/Privilege_escalation)  




## Linux 

1. [`CVE-2022-0847`](#CVE-2022-0847)
<p align='justify'>
CVE-2022-0847, a vulnerability in the Linux kernel since 5.8 which allows overwriting data in arbitrary read-only files. This leads to privilege escalation because unprivileged processes can inject code into root processes.</p>


### Source / Credits 

- [link](https://dirtypipe.cm4all.com/)

- [link](https://github.com/febinrev/dirtypipez-exploit)

- [link](https://github.com/basharkey/CVE-2022-0847-dirty-pipe-checker)

- [link](https://github.com/AlexisAhmed/CVE-2022-0847-DirtyPipe-Exploits)


2. [`Dirty Cow`](https://dirtycow.ninja/)


