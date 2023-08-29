- [Scanning]


### Scanning 

#### Nmap
- **Nmap** (Network Mapper) is an open-source tool specialized in network exploration and
security auditing. 

Nmap categorizes ports into two `open` and `close`

- Open: This indicates that an application is listening for connections on this port.

- Closed: This indicates that the probes were received but there is no application
listening on this port.

- Filtered: This indicates that the probes were not received and the state could not
be established. It also indicates that the probes are being dropped by some
kind of filtering.
- Unfiltered: This indicates that the probes were received but a state could not
be established.
- Open/Filtered: This indicates that the port was filtered or open but Nmap couldn't
establish the state.
- Closed/Filtered: This indicates that the port was filtered or closed but Nmap
couldn't establish the state.



- Simple Scan

```
                                                                                                                                                                
┌──(hecker㉿kaliLinuxSec)-[~/Desktop]
└─$ nmap 192.168.43.88 
Starting Nmap 7.94 ( https://nmap.org ) at 2023-08-01 22:09 IST
Nmap scan report for 192.168.43.88
Host is up (0.0026s latency).
Not shown: 977 closed tcp ports (conn-refused)
PORT     STATE SERVICE
21/tcp   open  ftp
22/tcp   open  ssh
23/tcp   open  telnet
25/tcp   open  smtp
53/tcp   open  domain
80/tcp   open  http
111/tcp  open  rpcbind
139/tcp  open  netbios-ssn
445/tcp  open  microsoft-ds
512/tcp  open  exec
513/tcp  open  login
514/tcp  open  shell
1099/tcp open  rmiregistry
1524/tcp open  ingreslock
2049/tcp open  nfs
2121/tcp open  ccproxy-ftp
3306/tcp open  mysql
5432/tcp open  postgresql
5900/tcp open  vnc
6000/tcp open  X11
6667/tcp open  irc
8009/tcp open  ajp13
8180/tcp open  unknown

Nmap done: 1 IP address (1 host up) scanned in 0.28 seconds
                                                               

```

This command does the following

- Nmap begins by converting the hostname to an IPv4 address using DNS
- Afterwards, it pings the target address to check if the host is alive.
- Nmap then converts the IPv4 address back to a hostname by using a reverse DNS call
- Finally, it launches a TCP port scan


- Scanning all ports

```
$ nmap -p- 192.168.43.88


┌──(hecker㉿kaliLinuxSec)-[~/Desktop]
└─$ nmap -p- 192.168.43.88
Starting Nmap 7.94 ( https://nmap.org ) at 2023-08-01 22:20 IST
Nmap scan report for 192.168.43.88
Host is up (0.0050s latency).
Not shown: 65505 closed tcp ports (conn-refused)
PORT      STATE SERVICE
21/tcp    open  ftp
22/tcp    open  ssh
23/tcp    open  telnet
25/tcp    open  smtp
53/tcp    open  domain
80/tcp    open  http
111/tcp   open  rpcbind
139/tcp   open  netbios-ssn
445/tcp   open  microsoft-ds
512/tcp   open  exec
513/tcp   open  login
514/tcp   open  shell
1099/tcp  open  rmiregistry
1524/tcp  open  ingreslock
2049/tcp  open  nfs
2121/tcp  open  ccproxy-ftp
3306/tcp  open  mysql
3632/tcp  open  distccd
5432/tcp  open  postgresql
5900/tcp  open  vnc
6000/tcp  open  X11
6667/tcp  open  irc
6697/tcp  open  ircs-u
8009/tcp  open  ajp13
8180/tcp  open  unknown
8787/tcp  open  msgsrvr
36137/tcp open  unknown
46082/tcp open  unknown
57557/tcp open  unknown
58149/tcp open  unknown

Nmap done: 1 IP address (1 host up) scanned in 3.11 seconds
                                                       

```

- Scan only range of ports

```
┌──(hecker㉿kaliLinuxSec)-[~/Desktop]
└─$ nmap -p[1-100] 192.168.43.88
Starting Nmap 7.94 ( https://nmap.org ) at 2023-08-01 22:23 IST
Nmap scan report for 192.168.43.88
Host is up (0.0097s latency).
Not shown: 93 closed tcp ports (conn-refused)
PORT   STATE SERVICE
21/tcp open  ftp
22/tcp open  ssh
23/tcp open  telnet
25/tcp open  smtp
53/tcp open  domain
80/tcp open  http

Nmap done: 1 IP address (1 host up) scanned in 0.22 seconds

```


