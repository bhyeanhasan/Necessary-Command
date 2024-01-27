
### LAB 11 (RIP)
##### B1-R1
```
enable 
config t
hostname B1-R1

int Se0/0/0
ip address 10.1.244.2 255.255.252.0
no shut

int Fa0/0
ip address 10.1.0.1 255.255.252.0
no shut

int Fa0/1
ip address 10.1.4.1 255.255.252.0
no shut

int Fa1/0
ip address 10.1.8.1 255.255.252.0
no shut

int Fa1/1
ip address 10.1.12.1 255.255.252.0
no shut
```
##### B2-R1
```
enable 
config t
hostname B2-R1

int Se0/0/0
ip address 10.1.248.2 255.255.252.0
no shut

int Fa0/0
ip address 10.1.16.1 255.255.252.0
no shut

int Fa0/1
ip address 10.1.20.1 255.255.252.0
no shut

int Fa1/0
ip address 10.1.24.1 255.255.252.0
no shut

int Fa1/1
ip address 10.1.28.1 255.255.252.0
no shut
```
##### B3-R1
```
enable 
config t
hostname B3-R1

int Se0/0/0
ip address 10.1.252.2 255.255.252.0
no shut

int Fa0/0
ip address 10.1.32.1 255.255.252.0
no shut

int Fa0/1
ip address 10.1.36.1 255.255.252.0
no shut

int Fa1/0
ip address 10.1.40.1 255.255.252.0
no shut

int Fa1/1
ip address 10.1.44.1 255.255.252.0
no shut
```



##### R1
```
enable 
config t
hostname R1

int Se0/0/0
ip address 10.1.244.1 255.255.252.0
clock rate 64000
no shut

int Se0/0/1
ip address 10.1.248.1 255.255.252.0
clock rate 64000
no shut

int Se0/1/0
ip address 10.1.252.1 255.255.252.0
clock rate 64000
no shut
```



##### B1-R2
```
enable 
config t
hostname B1-R2

int Se0/0/0
ip address 172.20.250.2 255.255.254.0
no shut

int Fa0/0
ip address 172.20.0.1 255.255.254.0
no shut

int Fa0/1
ip address 172.20.2.1 255.255.254.0
no shut

int Fa1/0
ip address 172.20.4.1 255.255.254.0
no shut

int Fa1/1
ip address 172.20.6.1 255.255.254.0
no shut
```
##### B2-R2
```
enable 
config t
hostname B2-R2

int Se0/0/0
ip address 172.20.252.2 255.255.254.0
no shut

int Fa0/0
ip address 172.20.8.1 255.255.254.0
no shut

int Fa0/1
ip address 172.20.10.1 255.255.254.0
no shut

int Fa1/0
ip address 172.20.12.1 255.255.254.0
no shut

int Fa1/1
ip address 172.20.14.1 255.255.254.0
no shut
```
##### B3-R2
```
enable 
config t
hostname B3-R2

int Se0/0/0
ip address 172.20.254.2 255.255.254.0
no shut

int Fa0/0
ip address 172.20.16.1 255.255.254.0
no shut

int Fa0/1
ip address 172.20.18.1 255.255.254.0
no shut

int Fa1/0
ip address 172.20.20.1 255.255.254.0
no shut

int Fa1/1
ip address 172.20.22.1 255.255.254.0
no shut
```

##### R2

```
enable 
config t
hostname R2

int Se0/0/0
ip address 172.20.250.1 255.255.254.0
clock rate 64000
no shut

int Se0/0/1
ip address 172.20.252.1 255.255.254.0
clock rate 64000
no shut

int Se0/1/0
ip address 172.20.254.1 255.255.254.0
clock rate 64000
no shut
```



##### Static Route
```
ISP R1
    ip route 10.1.0.0 255.255.0.0 Se0/0/0
    ip route 172.20.0.0 255.255.0.0 Se0/0/1

ISP R2
    ip route 10.1.0.0 255.255.0.0 Se0/0/1
    ip route 172.20.0.0 255.255.0.0 Se0/0/0

R1
    ip route 0.0.0.0 0.0.0.0 Se0/1/1

R2
    ip route 0.0.0.0 0.0.0.0 Se0/1/1
```

```
enable
conf t

router rip

network 10.1.0.0
network 10.1.4.0
network 10.1.8.0
network 10.1.12.0
network 10.1.244.0

passive-interface fa0/0
passive-interface fa0/1
passive-interface fa1/0
passive-interface fa1/1
```

```
enable
conf t

router rip

network 10.1.16.0
network 10.1.20.0
network 10.1.24.0
network 10.1.28.0
network 10.1.248.0

passive-interface fa0/0
passive-interface fa0/1
passive-interface fa1/0
passive-interface fa1/1
```
```
enable
conf t

router rip

network 10.1.32.0
network 10.1.36.0
network 10.1.40.0
network 10.1.44.0
network 10.1.252.0

passive-interface fa0/0
passive-interface fa0/1
passive-interface fa1/0
passive-interface fa1/1
```
```
enable
conf t

router rip

network 172.20.0.0
network 172.20.2.0
network 172.20.4.0
network 172.20.6.0
network 172.20.250.0

passive-interface fa0/0
passive-interface fa0/1
passive-interface fa1/0
passive-interface fa1/1
```
```
enable
conf t

router rip

network 172.20.8.0
network 172.20.10.0
network 172.20.12.0
network 172.20.14.0
network 172.20.252.0

passive-interface fa0/0
passive-interface fa0/1
passive-interface fa1/0
passive-interface fa1/1
```
```
enable
conf t

router rip

network 172.20.16.0
network 172.20.18.0
network 172.20.20.0
network 172.20.22.0
network 172.20.254.0

passive-interface fa0/0
passive-interface fa0/1
passive-interface fa1/0
passive-interface fa1/1
```
```
enable
conf t

router rip

network 10.1.244.0
network 10.1.248.0
network 10.1.252.0

passive-interface Se0/1/1
default-information originate
```
```
enable
conf t

router rip

network 172.20.250.0
network 172.20.252.0
network 172.20.254.0

passive-interface Se0/1/1
default-information originate
```