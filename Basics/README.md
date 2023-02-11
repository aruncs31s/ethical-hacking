## Basics

- [Proxy Servers and Stay Anonymous](#proxy-servers-and-stay-anonymous)
- [Vulnerability Scanning](#vulnerability-scanning)
- [Phishing](#phishing)
- [Malware]()
- [Denial of service (DoS) ](#denial-of-service)
- [Man-in-the-middle ](#mitm)
- [SQL injection ](sql-injection)
- 
### Proxy Servers and Stay Anonymous
<br>
<p align="justify"> 
    Proxy server is a computer on a network which acts as an intermediary for connections with other computer on that network 
     </p>
    
 <!--from https://www.fortinet.com/resources/cyberglossary/proxy-server-->

A proxy server is a system or router that provides a gateway between users and the internet. Therefore, it helps prevent cyber attackers from entering a private network. It is a server, referred to as an “intermediary” because it goes between end-users and the web pages they visit online.

#### Used for 
1. *Keep the system behind the curtain (mainly for security resons)*
2. *Speed up the acces to a resource (through "cqching")*
3. *Speacialized proxy servers are used to filter unwanted content such as advertisements.*
4. *Proxy servers can be used as IP address multiplexer to enable to connect number of computers on the internet, whatever only has one IP address*

*Get proxy servers [here](https://spys.one/en/)*


#### Setup using Tor

##### Pre-Requests


[`tor`](#tor)    [`proxychains*`](#proxychains) 







### **Vulnerability Scanning**
  vulnerability scanning is the procces of scanning/identifing existing vulnerabilities (you can also call it as loop hole) for the  the purpose of  exploiting or fixing the vulnerability 

  <details><summary> More Explenation: </summary>
  You can consider vulnerability as it's(Computer's) weakeness or just a flow in the code.
  </details>
 We use vulnerabilily scanner to order to scan for vulnerability in a system 

#### Scanners
Scanners are used to scan the system and identify the vulnerability , we also use scanner to check the open ports

**Eg :**

[`OpenVAS`](../Tools-Used/README.md#openvas) `


### **Phishing**

*Phishing is a cybercrime in which a target or targets are contacted by email, telephone or text message by someone posing as a legitimate institution to lure individuals into providing sensitive data such as personally identifiable information, banking and credit card details, and passwords.

The information is then used to access important accounts and can result in identity theft and financial loss.*

<!-- source https://www.phishing.org/what-is-phishing -->

#### **Steps involved in phishing**

1.**Planing** : *Criminals,Usually called as phishers , decide the target and determine how to get E-Mail addres of that target or customers of that bussiness. Phishers often user mailing and adress collectiontechnique as spammers*
2.**Setup**: *Once a phisher know which business/business house to spoof and who their victims are, they will create methods for delivering the messege and to collect data about the target . Most often this invoilves E-Mail address and a  webpage*
3.**Attack** : *This is the deep step pople are most familiar with - the phisher sends a phony messege that apppears to be from a reputable source.*
4.**Collection** : *Phoishers record the information of victims entering into webpages or pop-up window.*
5.**Identify theft and Fraud** : *phishers use the information that they have gathered to make illegal purchases or commit fraud*



<button onclick="document.location='www.google.com'"> Google</button>

### **Password cracking** 
 *Password cracking is a process of recovering passwords from data that havebeen stored in or transmitted by a computersystem*


### **Port Forwarding**
<!---Source Chat Gpt --->
  Port forwarding is a technique used in computer networking to redirect incoming network traffic from one port on a network device to another port on a different device.
<details><summary>Uses :</summary>

It is often used to allow external users or services to connect to a specific service running on a local network device, such as a web server or a game server.By forwarding the appropriate network traffic from the external device's port to the local device's port, port forwarding enables remote access and communication between the devices. Port forwarding can be configured in various ways, including through a router or a firewall, and typically requires the use of a static IP address and specific port numbers. It is an important tool for managing and securing network connections, but should be used with caution to prevent unauthorized access or security breaches.
</details>

#### Setup 

1 Identify the local IP address of the device that you want to forward traffic to. You can use the `ifconfig` or `ip addr` command to find the IP address

2. Determine the port number of the service that you want to forward traffic to on the local device
3. Configure the network router or firewall to forward traffic from a specific external port to the local IP address and port number. This can typically be done through the router's web-based interface or command-line interface.
4. Optionally, configure the local device's firewall to allow incoming traffic on the specified port
5. Test the port forwarding by attempting to connect to the external IP address and port number from a remote device. You can use the telnet or nc command to test the connection

### **Malware**
malicious software are malicious files such as viruses, trojans, or ransomware, and which is used to gain control of a system or steal data.


### **Denial of service**
overwhelming a system or network with traffic or requests to cause it to crash or become unavailable.

### Man in the middle attack
Man in the middle (MITM) intercepting and altering network traffic between two parties to gain access to sensitive data or perform unauthorized actions

### **sql injection**
exploiting vulnerabilities in web applications to execute unauthorized SQL commands and extract sensitive information.

