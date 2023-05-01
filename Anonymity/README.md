
- [**Introduction](introduction)
- [**torctl**](torctl)
- [Basics]()
    - [Vpn]()
    - [Proxy]()
    - [tor]()
- [Setup]()
    - [vpn]()
    - [proxy]()
    - [tor]()
- [Fully Anonymize]()
## **Introduction**
**In the dark side of hacking not getting caught is an essential thing . That is you should be fully anonymous which is much more difficult now days due to logging of each and every activity on the internet**. **Which is Why staying anonymous is important**

--- 
**Thus This Section will purely concentrated on anonymity rather than hacking**
**And the following will contain basic info about `vpn` `proxy` `tor` etc**

## **torctl** 
`torctl` redirect all traffic through tor network , which basicly means that you will be somewhat anonymous .


### Installition

- On debian based
```
$ sudo apt-get install torctl
or
$ sudo aptitude install torctl
```
- On arch based 

```
$ yay -S torctl
or
$ sudo pacman -S torctl
```
*torctl is not defautly available in the repo in some operating systems* *However you can Install it by adding kali's repo in debian based and blackarch on arch based*


- To start the redirection
```
$ sudo torctl start
```
- To stop the redirection
```
$ sudo torctl stop
```

> Other usefull commands

|Command|Use|
|----------|---------|
|start      | start tor and redirect all traffic through tor|
|stop       | stop tor and redirect all traffic through clearnet |
|status     | get tor service status|
|restart    | restart tor and traffic rules|
|autowipe    | enable memory wipe at shutdown|
|autostart   | start torctl at startup|
|ip          | get remote ip address|
|chngid      | change tor identity|
|chngmac     | change mac addresses of all interfaces|
|rvmac       | revert mac addresses of all interfaces|
|version     | print version of torctl and exit|
*source torctl --help*

### Setting Up Tor

- Installition

```

$ sudo apt install tor proxychains-ng # for Debian

$ sudo pacman -S tor proxychains-ng # for arch linux
```

- Editing Config

``` 
$ sudo nano /etc/proxychains.conf

```

- after opening the config file uncomment `dynamic chain` and comment `strict chain`
*you can uncomment a string by removing the hash(pound) string*   

- then start the tor service by

```
$ sudo systemctl start tor
```




