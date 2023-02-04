# Computer Networking 
## Basic Command

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
S1# show running-config
```



### Django Command
```
python manage.py startapp CoverPage
pip freeze > requirements.txt
pip install -r requirments.txt
```

