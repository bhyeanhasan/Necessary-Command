

#### RIP v2 Configuration
``` 
Router(config)# router rip  
Router(config-router)# version 2
Router(config-router)# network 10.0.0.0
```

#### EIGRP Configuration
``` 
Router(config)# router eigrp 100  
Router(config-router)# network 192.168.1.0
Router(config-router)# network 192.168.10.4 0.0.0.3
Router(config-if)# ip hello-interval eigrp 100 30
```

#### OSPF Configuration
``` 
Router(config)# router ospf 100  
Router(config-router)# router-id 192.168.1.1
Router(config-router)# network 192.168.1.0 0.0.0.255 area 0
Router(config-if)# ip ospf hello-interval 30
```

#### BGP Configuration
```
Router(config)# router bgp 100  # BGP Autonomous System number (AS)
Router(config-router)# neighbor 192.168.2.2 remote-as 200  # Remote BGP neighbor IP and AS
Router(config-router)# network 192.168.1.0 mask 255.255.255.0  # Network advertisement
```

#### Inter VLAN Communication
``` 
Router(config)# interface fa0/0.10
Router(config-subif)# encapsulation dot1Q 10
Router(config-subif)# ip address 192.168.10.1 255.255.255.0
Router(config-subif)# exit

Router(config)# interface fa0/0.20
Router(config-subif)# encapsulation dot1Q 20
Router(config-subif)# ip address 192.168.20.1 255.255.255.0
Router(config-subif)# exit
```

#### Configuring VLAN 
```
Switch(config)# vlan 20 
Switch(config-vlan)# name student

Switch(config)# interface fa0/0
Switch(config-if)# switchport mode access
Switch(config-if)# switchport access vlan 10
```

#### Check VLAN 
```
Switch# show vlan brief
Switch# show vlan name student
```

#### Configuring Trunk
```
Switch(config)# interface fa0/0
Switch(config-if)# switchport mode trunk
Switch(config-if)# switchport trunk allowed vlan 10,20,99
Switch(config-if)# switchport trunk native vlan 99
```

#### Check Trunk 
```
Switch# show interface trunk
```
