## Basics

- [Proxy Servers and Stay Anonymous](#proxy-servers-and-stay-anonymous)
- [Vulnerability Scanning](#vulnerability-scanning)
- [Phishing](#phishing)
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


<details id="tor"><summary> tor :</summary>
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
</details>



<details><summary>proxychains: </summary>

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

</details>



















### **Phishing**

*Phishing is a cybercrime in which a target or targets are contacted by email, telephone or text message by someone posing as a legitimate institution to lure individuals into providing sensitive data such as personally identifiable information, banking and credit card details, and passwords.

The information is then used to access important accounts and can result in identity theft and financial loss.*

<!-- source https://www.phishing.org/what-is-phishing -->

#### **Steps involved in phishing**
1. **Planing** : *Criminals,Usually called as phishers , decide the target and determine how to get E-Mail addres of that target or customers of that bussiness. Phishers often user mailing and adress collectiontechnique as spammers*
2. **Setup**: *Once a phisher know which business/business house to spoof and who their victims are, they will create methods for delivering the messege and to collect data about the target . Most often this invoilves E-Mail address and a  webpage*
3. **Attack** : *This is the deep step pople are most familiar with - the phisher sends a phony messege that apppears to be from a reputable source.*
4. **Collection** : *Phoishers record the information of victims entering into webpages or pop-up window.*
5. **Identify theft and Fraud** : *phishers use the information that they have gathered to make illegal purchases or commit fraud*



<button onclick="document.location='www.google.com'"> Google</button>

### **Password cracking** 
 *Password cracking is a process of recovering passwords from data that havebeen stored in or transmitted by a computersystem*



