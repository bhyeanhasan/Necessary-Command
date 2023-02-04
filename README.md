# Basic Command
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
S1# show running-config
```



## Django Command
```
python manage.py startapp CoverPage
pip freeze > requirements.txt
pip install -r requirments.txt
```

## How to back up Driver
```
To save> DISM /Online /Export-Driver /Destination:"D:\DriverBackup"
To load> Export-WindowsDriver -Online -Destination D:\DriverBackup
```


## Competitive Programming
### CP Template
```
/**===========================================================================================
                                B H Yean Hasan (NoYoN)
                    Patuakhali Science and Technology University
                     Faculty of Computer Science and Engineering
/*===========================================================================================**/
/*============================================
    move line           Alt+up/Alt+down
    Duplicate line      Ctrl + D
    Swap line above 	Ctrl + T
    Line cut.	        Ctrl + L
    Line copy.      	Alt + c
    Line delete.	    Ctrl + Shift + L
/*=============================================*/
    #include<bits/stdc++.h>
    #define pi acos(-1)
    #define jor_even(i) (!(i & 1))
    #define bijor_odd(i) (i & 1)
    #define gcd(a, b) __gcd(a,b)
    #define lcm(a, b) (((a)/gcd(a,b))*b)
    #define binaryToDecimal(str) stoi(str,nullptr,2)
    #define octalToDecimal(str) stoi(str,nullptr,8)
    #define hexaToDecimal(str) stoi(str,nullptr,16)
    #define fil(arr,value) memset(arr,value,arr.size())
    #define vfill(v,value)  v.assign(v.size(),value)
    #define pb(x) push_back(x)
    #define ll long long int
    #define vc vector<ll>
    #define show(arr) for( auto &it : arr ) cout<<it<<" "
    #define input(arr) for( auto &it : arr ) cin>>it
    #define fr(i,n) for(ll i=0;i<n;i++)
    #define srt(a) sort(a.begin(),a.end())
    #define print(x) cout<<x<<endl
    #define in(a) scanf("%lld",&a)
    #define yes cout<<"YES"<<endl
    #define no cout<<"NO"<<endl
    #define FILE_io freopen("input.txt", "r", stdin); freopen("output.txt", "w", stdout);
    #define TEST ll test; cin>>test; for(ll T=1;T<=test;T++)
    #define START ll n,a,b,c,x,y,z,i,j,k,sum=0,t=0,count=0,flag=0,place=-1; string s,s1,s2,s3; bool is = false; double Sum=0;
    #define READY ios_base::sync_with_stdio(false); cin.tie(NULL);cout.tie(0);

using namespace std;
    string sss;
    long long arr[100009];

int main()
{
    READY;
    START;
//    TEST
{
/*===========================================================================================*/

    s = "babul";
    s1 = "hasan";

    int oka = int("bab");
    print(oka);

/*===========================================================================================*/
} return 0; }
```

