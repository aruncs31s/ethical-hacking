# Tools Used

## Hacking Tools
| Tool Name | Usage| 
|-----------|-------------|
|[`Metasploit`](#metasploit)|provides information about security vulnerabilities and aids in penetration testing|
|[`tor`](#tor) |Tor is a connection-based low-latency anonymous communication system |
| [`proxychains`]() |Proxy chains force any tcp connection made by any given tcp client
to follow through proxy (or proxy chain). It is a kind of proxifier.
It acts like sockscap / premeo / eborder driver ( intercepts TCP calls )  |




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

### tor
<!--source apt show tor -->

**Source = apt show tor**

Tor is a connection-based low-latency anonymous communication system.
Clients choose a source-routed path through a set of relays, and
 negotiate a "virtual circuit" through the network, in which each relay
 knows its predecessor and successor, but no others. Traffic flowing
 down the circuit is decrypted at each relay, which reveals the
 downstream relay.
 .
 Basically, Tor provides a distributed network of relays. Users bounce
 their TCP streams (web traffic, ftp, ssh, etc) around the relays, and
 recipients, observers, and even the relays themselves have difficulty
 learning which users connected to which destinations.
 .
 This package enables only a Tor client by default, but it can also be
 configured as a relay and/or a hidden service easily.
 .
 Client applications can use the Tor network by connecting to the local
 socks proxy interface provided by your Tor instance. If the application
 itself does not come with socks support, you can use a socks client
 such as torsocks.
 .
 Note that Tor does no protocol cleaning on application traffic. There
 is a danger that application protocols and associated programs can be
 induced to reveal information about the user. Tor depends on Torbutton
 and similar protocol cleaners to solve this problem. For best
 protection when web surfing, the Tor Project recommends that you use
 the Tor Browser Bundle, a standalone tarball that includes static
 builds of Tor, Torbutton, and a modified Firefox that is patched to fix
 a variety of privacy bugs.


### proxychains

**Source = apt show proxychains**
Proxy chains force any tcp connection made by any given tcp client
to follow through proxy (or proxy chain). It is a kind of proxifier.
It acts like sockscap / premeo / eborder driver ( intercepts TCP calls )

.
 This version supports SOCKS4, SOCKS5 and HTTP CONNECT proxy servers.
 Different proxy types can be mixed in the same chain.
 .
 Features
   * Access Internet from behind restrictive firewall.
   * Source IP masquerade.
   * SSH tunneling and forwarding.
   * Dynamic LAN-to-LAN VPN channel.
   * Servers and daemons friendly (works fine with sendmail MTA).
 .
 http://proxychains.sourceforge.net

### Netcat
  Netcat (often abbreviated as "nc") is a command-line networking utility in Linux and other operating systems that can be used for various network-related tasks, such as transferring files, port scanning, and debugging network connections. It is designed to be a simple and flexible tool that can work with both TCP and UDP protocols and can be used in a wide range of scenarios. Some of the common use cases of netcat include establishing a two-way data transfer between two computers, creating a simple chat server, and testing network services and firewalls. It is a powerful and versatile tool that can be used by system administrators, network engineers, and security professionals for various networking tasks.

## **Nikto**
  


## **Tcpdump**
tcpdump command in Linux is used to monitor traffic on a specific network interface

## 










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
eg : 
```
$ apt remove gimp
```

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

