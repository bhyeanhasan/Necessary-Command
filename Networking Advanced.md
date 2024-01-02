#### Configuring Static Route

```
Router(config)# ip route {network} {subnet} {next-hop ip / exit interface}
Router(config)# ip route 192.168.10.0 255.255.255.0 G0/1 192.168.20.0

Default route:
Router(config)# ip route 0.0.0.0 0.0.0.0 192.168.20.0

Floating route:
Router(config)# ip route 0.0.0.0 0.0.0.0 192.168.30.0 5
```

#### Check Route

```
Router# show ip route | begin Gateway
Router# show ip route | include C
Router# show ip route 192.168.10.0
Router# show running-config | section ip route
Router# traceroute 192.168.50.0
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