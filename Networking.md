
## Computer Networking

>Switch>show version

### How to set clock
```
Switch>show clock
Switch>enable
Switch#clock set ?
Switch#clock set 11:33:10 ?
Switch#clock set 11:33:10 3 February ?
Switch#clock set 11:33:10 3 February 2023 
```
### How to configure switch
```
Switch>enable
Switch#configure terminal
Switch#config t
s1(config)#no ip domain-lookup
S1(config)# enable secret class
S1(config)# line con 0
S1(config-line)# password cisco
S1(config-line)# login
S1(config-line)# exit
S1(config)# interface vlan 1
S1(config-if)# ip address 192.168.1.1 255.255.255.0
S1(config-if)# no shut
S1(config)# banner motd # Unauthorized access is strictly prohibited and prosecuted to the full extent of the law. #
S1(config)# exit
![img_1.png](img_1.png)
S1# show running-config
S1# copy running-config startup-config

R1-ISP(config)#interface S0/0/0
R1-ISP(config-if)#ip address 192.168.3.98 255.255.255.252
R1(config-if)# ipv6 address 2001:db8:acad::1/64 
R1(config-if)# ipv6 address FE80::1 link-local
R1-ISP(config-if)#no shutdown 

R1-ISP(config)#interface S0/0/0
R1-ISP(config-if)#clock rate 64000
R1-ISP(config-if)#exit 

R1-ISP(config)#line vty 0
R1-ISP(config-line)#password cisco
R1-ISP(config-line)#login
R1-ISP(config-line)#exit

R2-Central(config)#ip route
R2-Central(config)#ip route 0.0.0.0 0.0.0.0 192.168.3.98

R1-ISP(config)#ip route 192.168.3.0 255.255.255.224 192.168.3.97
R1-ISP(config)#exit
```
[IP list](https://1drv.ms/x/s!AmZ4AO27AT3OiqEHUVaPeLujSmz2Tw?e=C8Argw)



```
C:\>ftp 192.168.0.100
Username:noyon
Password:123
ftp>dir
ftp>put bhyean.txt
ftp>get bhyean.txt

telnet 192.168.0.10
```

