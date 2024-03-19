# Test results for CBL433

## show version

```text
Arista AWE-5310-F
Hardware version: 11.01
Serial number: WTW23341336
Hardware MAC address: ec8a.4804.2bae
System MAC address: ec8a.4804.2bae

Software image version: 4.31.2F
Architecture: x86_64
Internal build version: 4.31.2F-35442176.4312F
Internal build ID: 500c58e3-5beb-4481-afe9-8ad77245cc44
Image format version: 3.0
Image optimization: Default

Uptime: 19 hours and 27 minutes
Total memory: 32470188 kB
Free memory: 21137660 kB

```

## show mac address-table

```text
          Mac Address Table
------------------------------------------------------------------

Vlan    Mac Address       Type        Ports      Moves   Last Move
----    -----------       ----        -----      -----   ---------
Total Mac Addresses for this criterion: 0
```

## show ip interface brief | exclude una

```text
                                                                        Address
Interface        IP Address           Status     Protocol         MTU   Owner  
---------------- -------------------- ---------- ------------ --------- -------
Ethernet1/5      10.0.255.2/31        up         up              1500          
Ethernet1/7      172.16.0.3/31        up         up              9000          
Loopback0        10.255.255.6/32      up         up             65535          
Management1/1    172.28.138.220/20    up         up              1500          

```

## show interfaces counters rates | nz

```text
Port      Name      Intvl  In Mbps      %  In Kpps Out Mbps      % Out Kpps
Et1/5     CE         0:01     44.2   0.5%       22     48.0   0.5%       24
Et1/7     VZ_FF      0:01     65.9   0.7%       24     60.3   0.6%       22
Ma1/1                0:01     11.4   1.2%        1      0.2   0.0%        0
```

## show ip route

```text

VRF: default
Source Codes:
       C - connected, S - static, K - kernel,
       O - OSPF, IA - OSPF inter area, E1 - OSPF external type 1,
       E2 - OSPF external type 2, N1 - OSPF NSSA external type 1,
       N2 - OSPF NSSA external type2, B - Other BGP Routes,
       B I - iBGP, B E - eBGP, R - RIP, I L1 - IS-IS level 1,
       I L2 - IS-IS level 2, O3 - OSPFv3, A B - BGP Aggregate,
       A O - OSPF Summary, NG - Nexthop Group Static Route,
       V - VXLAN Control Service, M - Martian,
       DH - DHCP client installed default route,
       DP - Dynamic Policy Route, L - VRF Leaked,
       G  - gRIBI, RC - Route Cache Route,
       CL - CBF Leaked Route

Gateway of last resort is not set

 S        10.80.0.0/12 [1/0]
           via 172.28.128.1, Management1/1
 S        10.224.0.0/12 [1/0]
           via 172.28.128.1, Management1/1
 S        10.255.255.1/32
           directly connected, Dps1
 S        10.255.255.4/32
           directly connected, Dps1
 S        10.255.255.5/32
           directly connected, Dps1
 C        10.255.255.6/32
           directly connected, Loopback0
 S        10.255.255.11/32
           directly connected, Dps1
 S        10.255.255.12/32
           directly connected, Dps1
 S        10.240.0.0/12 [1/0]
           via 172.28.128.1, Management1/1
 C        172.16.0.2/31
           directly connected, Ethernet1/7
 S        172.16.0.0/24 [1/0]
           via 172.16.0.2, Ethernet1/7
 C        172.28.128.0/20
           directly connected, Management1/1
 S        172.16.0.0/12 [1/0]
           via 172.28.128.1, Management1/1

```

## show ip route vrf all

```text

VRF: default
Source Codes:
       C - connected, S - static, K - kernel,
       O - OSPF, IA - OSPF inter area, E1 - OSPF external type 1,
       E2 - OSPF external type 2, N1 - OSPF NSSA external type 1,
       N2 - OSPF NSSA external type2, B - Other BGP Routes,
       B I - iBGP, B E - eBGP, R - RIP, I L1 - IS-IS level 1,
       I L2 - IS-IS level 2, O3 - OSPFv3, A B - BGP Aggregate,
       A O - OSPF Summary, NG - Nexthop Group Static Route,
       V - VXLAN Control Service, M - Martian,
       DH - DHCP client installed default route,
       DP - Dynamic Policy Route, L - VRF Leaked,
       G  - gRIBI, RC - Route Cache Route,
       CL - CBF Leaked Route

Gateway of last resort is not set

 S        10.80.0.0/12 [1/0]
           via 172.28.128.1, Management1/1
 S        10.224.0.0/12 [1/0]
           via 172.28.128.1, Management1/1
 S        10.255.255.1/32
           directly connected, Dps1
 S        10.255.255.4/32
           directly connected, Dps1
 S        10.255.255.5/32
           directly connected, Dps1
 C        10.255.255.6/32
           directly connected, Loopback0
 S        10.255.255.11/32
           directly connected, Dps1
 S        10.255.255.12/32
           directly connected, Dps1
 S        10.240.0.0/12 [1/0]
           via 172.28.128.1, Management1/1
 C        172.16.0.2/31
           directly connected, Ethernet1/7
 S        172.16.0.0/24 [1/0]
           via 172.16.0.2, Ethernet1/7
 C        172.28.128.0/20
           directly connected, Management1/1
 S        172.16.0.0/12 [1/0]
           via 172.28.128.1, Management1/1


VRF: USAA
Source Codes:
       C - connected, S - static, K - kernel,
       O - OSPF, IA - OSPF inter area, E1 - OSPF external type 1,
       E2 - OSPF external type 2, N1 - OSPF NSSA external type 1,
       N2 - OSPF NSSA external type2, B - Other BGP Routes,
       B I - iBGP, B E - eBGP, R - RIP, I L1 - IS-IS level 1,
       I L2 - IS-IS level 2, O3 - OSPFv3, A B - BGP Aggregate,
       A O - OSPF Summary, NG - Nexthop Group Static Route,
       V - VXLAN Control Service, M - Martian,
       DH - DHCP client installed default route,
       DP - Dynamic Policy Route, L - VRF Leaked,
       G  - gRIBI, RC - Route Cache Route,
       CL - CBF Leaked Route

Gateway of last resort is not set

 B I      10.0.255.0/31 [20/0]
           via VTEP 10.255.255.5 VNI 201 router-mac ec:8a:48:04:21:53
 C        10.0.255.2/31
           directly connected, Ethernet1/5
 B I      10.1.255.0/31 [20/0]
           via VTEP 10.255.255.1 VNI 201 router-mac ec:8a:48:04:f5:30
 B I      10.1.255.2/31 [20/0]
           via VTEP 10.255.255.1 VNI 201 router-mac ec:8a:48:04:f5:30
           via VTEP 10.255.255.4 VNI 201 router-mac ec:8a:48:04:ff:5b
 B I      10.2.255.0/31 [20/0]
           via VTEP 10.255.255.1 VNI 201 router-mac ec:8a:48:04:f5:30
           via VTEP 10.255.255.4 VNI 201 router-mac ec:8a:48:04:ff:5b
 B I      10.2.255.2/31 [20/0]
           via VTEP 10.255.255.8 VNI 201 router-mac ec:8a:48:04:2c:53
 B I      10.4.255.0/31 [20/0]
           via VTEP 10.255.255.1 VNI 201 router-mac ec:8a:48:04:f5:30
           via VTEP 10.255.255.4 VNI 201 router-mac ec:8a:48:04:ff:5b
 B I      10.4.255.2/31 [20/0]
           via VTEP 10.255.255.10 VNI 201 router-mac 00:0c:29:d5:32:d4
 B I      10.5.255.0/31 [20/0]
           via VTEP 10.255.255.1 VNI 201 router-mac ec:8a:48:04:f5:30
           via VTEP 10.255.255.4 VNI 201 router-mac ec:8a:48:04:ff:5b
 B I      10.5.255.2/31 [20/0]
           via VTEP 10.255.255.4 VNI 201 router-mac ec:8a:48:04:ff:5b
 B I      10.6.255.0/31 [20/0]
           via VTEP 10.255.255.11 VNI 201 router-mac 00:0c:29:ba:2d:5e
 B I      10.6.255.2/31 [20/0]
           via VTEP 10.255.255.12 VNI 201 router-mac 00:0c:29:78:c5:2d
 O        10.255.254.1/32 [110/20]
           via 10.0.255.3, Ethernet1/5
 B I      10.255.254.2/32 [20/0]
           via VTEP 10.255.255.1 VNI 201 router-mac ec:8a:48:04:f5:30
 B I      10.255.254.3/32 [20/0]
           via VTEP 10.255.255.8 VNI 201 router-mac ec:8a:48:04:2c:53
 B I      10.255.254.4/32 [20/0]
           via VTEP 10.255.255.11 VNI 201 router-mac 00:0c:29:ba:2d:5e
           via VTEP 10.255.255.12 VNI 201 router-mac 00:0c:29:78:c5:2d
 B I      10.255.254.5/32 [20/0]
           via VTEP 10.255.255.10 VNI 201 router-mac 00:0c:29:d5:32:d4
 B I      10.255.254.6/32 [20/0]
           via VTEP 10.255.255.4 VNI 201 router-mac ec:8a:48:04:ff:5b
 B I      172.16.255.0/31 [20/0]
           via VTEP 10.255.255.4 VNI 201 router-mac ec:8a:48:04:ff:5b
 B I      172.16.255.2/31 [20/0]
           via VTEP 10.255.255.1 VNI 201 router-mac ec:8a:48:04:f5:30
 O        192.168.0.0/24 [110/20]
           via 10.0.255.3, Ethernet1/5
 B I      192.168.1.0/24 [20/0]
           via VTEP 10.255.255.1 VNI 201 router-mac ec:8a:48:04:f5:30
 B I      192.168.3.0/24 [20/0]
           via VTEP 10.255.255.8 VNI 201 router-mac ec:8a:48:04:2c:53
 B I      192.168.5.0/24 [20/0]
           via VTEP 10.255.255.4 VNI 201 router-mac ec:8a:48:04:ff:5b
 B I      192.168.6.0/24 [20/0]
           via VTEP 10.255.255.11 VNI 201 router-mac 00:0c:29:ba:2d:5e
           via VTEP 10.255.255.12 VNI 201 router-mac 00:0c:29:78:c5:2d
 B I      192.168.40.0/24 [20/0]
           via VTEP 10.255.255.10 VNI 201 router-mac 00:0c:29:d5:32:d4

```

## show ipv6 route

```text

VRF: default
Displaying 0 of 3 IPv6 routing table entries
Source Codes:
       C - connected, S - static, K - kernel, O3 - OSPFv3,
       B - Other BGP Routes, A B - BGP Aggregate, R - RIP,
       I L1 - IS-IS level 1, I L2 - IS-IS level 2, DH - DHCP,
       NG - Nexthop Group Static Route, M - Martian,
       DP - Dynamic Policy Route, L - VRF Leaked,
       G  - gRIBI, RC - Route Cache Route,
       CL - CBF Leaked Route


! IPv6 routing not enabled
```

## show bgp evpn

```text
BGP routing table information for VRF default
Router identifier 10.255.255.6, local AS number 65000
Route status codes: * - valid, > - active, S - Stale, E - ECMP head, e - ECMP
                    c - Contributing to ECMP, % - Pending best path selection
Origin codes: i - IGP, e - EGP, ? - incomplete
AS Path Attributes: Or-ID - Originator ID, C-LST - Cluster List, LL Nexthop - Link Local Nexthop

          Network                Next Hop              Metric  LocPref Weight  Path
 * >Ec    RD: 10.255.255.5:1 ip-prefix 10.0.255.0/31
                                 10.255.255.5          -       100     0       i Or-ID: 10.255.255.5 C-LST: 10.255.255.4 
 *  ec    RD: 10.255.255.5:1 ip-prefix 10.0.255.0/31
                                 10.255.255.5          -       100     0       i Or-ID: 10.255.255.5 C-LST: 10.255.255.1 10.255.255.4 
 * >      RD: 10.255.255.6:1 ip-prefix 10.0.255.2/31
                                 -                     -       -       0       i
 * >Ec    RD: 10.255.255.1:1 ip-prefix 10.1.255.0/31
                                 10.255.255.1          -       100     0       i Or-ID: 10.255.255.1 C-LST: 10.255.255.4 
 *  ec    RD: 10.255.255.1:1 ip-prefix 10.1.255.0/31
                                 10.255.255.1          -       100     0       i
 * >Ec    RD: 10.255.255.1:1 ip-prefix 10.1.255.2/31
                                 10.255.255.1          -       5       0       i Or-ID: 10.255.255.1 C-LST: 10.255.255.4 10.255.255.1 
 *  ec    RD: 10.255.255.1:1 ip-prefix 10.1.255.2/31
                                 10.255.255.1          -       5       0       i
 * >Ec    RD: 10.255.255.4:1 ip-prefix 10.1.255.2/31
                                 10.255.255.4          -       5       0       i
 *  ec    RD: 10.255.255.4:1 ip-prefix 10.1.255.2/31
                                 10.255.255.4          -       5       0       i Or-ID: 10.255.255.4 C-LST: 10.255.255.1 10.255.255.4 172.16.255.0 
 * >Ec    RD: 10.255.255.1:1 ip-prefix 10.2.255.0/31
                                 10.255.255.1          -       5       0       i Or-ID: 10.255.255.1 C-LST: 10.255.255.4 10.255.255.1 172.16.255.2 
 *  ec    RD: 10.255.255.1:1 ip-prefix 10.2.255.0/31
                                 10.255.255.1          -       5       0       i
 * >Ec    RD: 10.255.255.4:1 ip-prefix 10.2.255.0/31
                                 10.255.255.4          -       5       0       i Or-ID: 10.255.255.7 C-LST: 10.255.255.4 172.16.255.0 10.255.255.2 
 *  ec    RD: 10.255.255.4:1 ip-prefix 10.2.255.0/31
                                 10.255.255.4          -       5       0       i Or-ID: 10.255.255.7 C-LST: 10.255.255.1 10.255.255.4 172.16.255.0 10.255.255.2 
 * >Ec    RD: 10.255.255.7:1 ip-prefix 10.2.255.2/31
                                 10.255.255.8          -       100     0       i Or-ID: 10.255.255.8 C-LST: 10.255.255.4 
 *  ec    RD: 10.255.255.7:1 ip-prefix 10.2.255.2/31
                                 10.255.255.8          -       100     0       i Or-ID: 10.255.255.8 C-LST: 10.255.255.1 10.255.255.4 
 * >Ec    RD: 10.255.255.1:1 ip-prefix 10.4.255.0/31
                                 10.255.255.1          -       5       0       i Or-ID: 10.255.255.1 C-LST: 10.255.255.4 10.255.255.1 172.16.255.2 
 *  ec    RD: 10.255.255.1:1 ip-prefix 10.4.255.0/31
                                 10.255.255.1          -       5       0       i
 * >Ec    RD: 10.255.255.4:1 ip-prefix 10.4.255.0/31
                                 10.255.255.4          -       5       0       i
 *  ec    RD: 10.255.255.4:1 ip-prefix 10.4.255.0/31
                                 10.255.255.4          -       5       0       i Or-ID: 10.255.255.4 C-LST: 10.255.255.1 10.255.255.4 172.16.255.0 
 * >Ec    RD: 10.255.255.10:1 ip-prefix 10.4.255.2/31
                                 10.255.255.10         -       100     0       i Or-ID: 10.255.255.10 C-LST: 10.255.255.4 
 *  ec    RD: 10.255.255.10:1 ip-prefix 10.4.255.2/31
                                 10.255.255.10         -       100     0       i Or-ID: 10.255.255.10 C-LST: 10.255.255.1 10.255.255.4 
 * >Ec    RD: 10.255.255.1:1 ip-prefix 10.5.255.0/31
                                 10.255.255.1          -       5       0       i Or-ID: 10.255.255.1 C-LST: 10.255.255.4 10.255.255.1 172.16.255.2 
 *  ec    RD: 10.255.255.1:1 ip-prefix 10.5.255.0/31
                                 10.255.255.1          -       5       0       i
 * >Ec    RD: 10.255.255.4:1 ip-prefix 10.5.255.0/31
                                 10.255.255.4          -       5       0       i
 *  ec    RD: 10.255.255.4:1 ip-prefix 10.5.255.0/31
                                 10.255.255.4          -       5       0       i Or-ID: 10.255.255.4 C-LST: 10.255.255.1 10.255.255.4 
 * >Ec    RD: 10.255.255.4:1 ip-prefix 10.5.255.2/31
                                 10.255.255.4          -       100     0       i
 *  ec    RD: 10.255.255.4:1 ip-prefix 10.5.255.2/31
                                 10.255.255.4          -       100     0       i Or-ID: 10.255.255.4 C-LST: 10.255.255.1 
 * >Ec    RD: 10.255.255.11:1 ip-prefix 10.6.255.0/31
                                 10.255.255.11         -       100     0       i Or-ID: 10.255.255.11 C-LST: 10.255.255.4 
 *  ec    RD: 10.255.255.11:1 ip-prefix 10.6.255.0/31
                                 10.255.255.11         -       100     0       i Or-ID: 10.255.255.11 C-LST: 10.255.255.1 10.255.255.4 
 * >Ec    RD: 10.255.255.12:1 ip-prefix 10.6.255.2/31
                                 10.255.255.12         -       100     0       i Or-ID: 10.255.255.12 C-LST: 10.255.255.4 
 *  ec    RD: 10.255.255.12:1 ip-prefix 10.6.255.2/31
                                 10.255.255.12         -       100     0       i Or-ID: 10.255.255.12 C-LST: 10.255.255.1 10.255.255.4 
          RD: 10.255.255.5:1 ip-prefix 10.255.254.1/32
                                 PolicyReject          -       -       0       i Or-ID: 10.255.255.5 C-LST: 10.255.255.4 
          RD: 10.255.255.5:1 ip-prefix 10.255.254.1/32
                                 PolicyReject          -       -       0       i Or-ID: 10.255.255.5 C-LST: 10.255.255.1 10.255.255.4 
 * >      RD: 10.255.255.6:1 ip-prefix 10.255.254.1/32
                                 -                     -       -       0       i
 * >Ec    RD: 10.255.255.1:1 ip-prefix 10.255.254.2/32
                                 10.255.255.1          -       100     0       i Or-ID: 10.255.255.1 C-LST: 10.255.255.4 
 *  ec    RD: 10.255.255.1:1 ip-prefix 10.255.254.2/32
                                 10.255.255.1          -       100     0       i
 * >      RD: 10.255.255.4:1 ip-prefix 10.255.254.2/32
                                 10.255.255.4          -       5       0       i
 * >Ec    RD: 10.255.255.1:1 ip-prefix 10.255.254.3/32
                                 10.255.255.1          -       5       0       i Or-ID: 10.255.255.1 C-LST: 10.255.255.4 10.255.255.1 172.16.255.2 
 *  ec    RD: 10.255.255.1:1 ip-prefix 10.255.254.3/32
                                 10.255.255.1          -       5       0       i
 * >Ec    RD: 10.255.255.4:1 ip-prefix 10.255.254.3/32
                                 10.255.255.4          -       5       0       i Or-ID: 10.255.255.7 C-LST: 10.255.255.4 172.16.255.0 10.255.255.2 
 *  ec    RD: 10.255.255.4:1 ip-prefix 10.255.254.3/32
                                 10.255.255.4          -       5       0       i Or-ID: 10.255.255.7 C-LST: 10.255.255.1 10.255.255.4 172.16.255.0 10.255.255.2 
 * >Ec    RD: 10.255.255.7:1 ip-prefix 10.255.254.3/32
                                 10.255.255.8          -       100     0       i Or-ID: 10.255.255.8 C-LST: 10.255.255.4 
 *  ec    RD: 10.255.255.7:1 ip-prefix 10.255.254.3/32
                                 10.255.255.8          -       100     0       i Or-ID: 10.255.255.8 C-LST: 10.255.255.1 10.255.255.4 
 * >Ec    RD: 10.255.255.11:1 ip-prefix 10.255.254.4/32
                                 10.255.255.11         -       100     0       i Or-ID: 10.255.255.11 C-LST: 10.255.255.4 
 *  ec    RD: 10.255.255.11:1 ip-prefix 10.255.254.4/32
                                 10.255.255.11         -       100     0       i Or-ID: 10.255.255.11 C-LST: 10.255.255.1 10.255.255.4 
 * >Ec    RD: 10.255.255.12:1 ip-prefix 10.255.254.4/32
                                 10.255.255.12         -       100     0       i Or-ID: 10.255.255.12 C-LST: 10.255.255.4 
 *  ec    RD: 10.255.255.12:1 ip-prefix 10.255.254.4/32
                                 10.255.255.12         -       100     0       i Or-ID: 10.255.255.12 C-LST: 10.255.255.1 10.255.255.4 
 * >Ec    RD: 10.255.255.1:1 ip-prefix 10.255.254.5/32
                                 10.255.255.1          -       5       0       i Or-ID: 10.255.255.1 C-LST: 10.255.255.4 10.255.255.1 172.16.255.2 
 *  ec    RD: 10.255.255.1:1 ip-prefix 10.255.254.5/32
                                 10.255.255.1          -       5       0       i
 * >Ec    RD: 10.255.255.4:1 ip-prefix 10.255.254.5/32
                                 10.255.255.4          -       5       0       i
 *  ec    RD: 10.255.255.4:1 ip-prefix 10.255.254.5/32
                                 10.255.255.4          -       5       0       i Or-ID: 10.255.255.4 C-LST: 10.255.255.1 10.255.255.4 172.16.255.0 
 * >Ec    RD: 10.255.255.10:1 ip-prefix 10.255.254.5/32
                                 10.255.255.10         -       100     0       i Or-ID: 10.255.255.10 C-LST: 10.255.255.4 
 *  ec    RD: 10.255.255.10:1 ip-prefix 10.255.254.5/32
                                 10.255.255.10         -       100     0       i Or-ID: 10.255.255.10 C-LST: 10.255.255.1 10.255.255.4 
 * >      RD: 10.255.255.1:1 ip-prefix 10.255.254.6/32
                                 10.255.255.1          -       5       0       i
 * >Ec    RD: 10.255.255.4:1 ip-prefix 10.255.254.6/32
                                 10.255.255.4          -       100     0       i
 *  ec    RD: 10.255.255.4:1 ip-prefix 10.255.254.6/32
                                 10.255.255.4          -       100     0       i Or-ID: 10.255.255.4 C-LST: 10.255.255.1 
 * >Ec    RD: 10.255.255.1:1 ip-prefix 172.16.255.0/31
                                 10.255.255.1          -       5       0       i Or-ID: 10.255.255.1 C-LST: 10.255.255.4 10.255.255.1 172.16.255.2 
 *  ec    RD: 10.255.255.1:1 ip-prefix 172.16.255.0/31
                                 10.255.255.1          -       5       0       i
 * >Ec    RD: 10.255.255.4:1 ip-prefix 172.16.255.0/31
                                 10.255.255.4          -       100     0       i
 *  ec    RD: 10.255.255.4:1 ip-prefix 172.16.255.0/31
                                 10.255.255.4          -       100     0       i Or-ID: 10.255.255.4 C-LST: 10.255.255.1 
 * >Ec    RD: 10.255.255.1:1 ip-prefix 172.16.255.2/31
                                 10.255.255.1          -       100     0       i Or-ID: 10.255.255.1 C-LST: 10.255.255.4 
 *  ec    RD: 10.255.255.1:1 ip-prefix 172.16.255.2/31
                                 10.255.255.1          -       100     0       i
 * >Ec    RD: 10.255.255.4:1 ip-prefix 172.16.255.2/31
                                 10.255.255.4          -       5       0       i
 *  ec    RD: 10.255.255.4:1 ip-prefix 172.16.255.2/31
                                 10.255.255.4          -       5       0       i Or-ID: 10.255.255.4 C-LST: 10.255.255.1 10.255.255.4 172.16.255.0 
          RD: 10.255.255.5:1 ip-prefix 192.168.0.0/24
                                 PolicyReject          -       -       0       i Or-ID: 10.255.255.5 C-LST: 10.255.255.4 
          RD: 10.255.255.5:1 ip-prefix 192.168.0.0/24
                                 PolicyReject          -       -       0       i Or-ID: 10.255.255.5 C-LST: 10.255.255.1 10.255.255.4 
 * >      RD: 10.255.255.6:1 ip-prefix 192.168.0.0/24
                                 -                     -       -       0       i
 * >Ec    RD: 10.255.255.1:1 ip-prefix 192.168.1.0/24
                                 10.255.255.1          -       100     0       i Or-ID: 10.255.255.1 C-LST: 10.255.255.4 
 *  ec    RD: 10.255.255.1:1 ip-prefix 192.168.1.0/24
                                 10.255.255.1          -       100     0       i
 * >      RD: 10.255.255.4:1 ip-prefix 192.168.1.0/24
                                 10.255.255.4          -       5       0       i
 * >Ec    RD: 10.255.255.1:1 ip-prefix 192.168.3.0/24
                                 10.255.255.1          -       5       0       i Or-ID: 10.255.255.1 C-LST: 10.255.255.4 10.255.255.1 172.16.255.2 
 *  ec    RD: 10.255.255.1:1 ip-prefix 192.168.3.0/24
                                 10.255.255.1          -       5       0       i
 * >Ec    RD: 10.255.255.4:1 ip-prefix 192.168.3.0/24
                                 10.255.255.4          -       5       0       i Or-ID: 10.255.255.7 C-LST: 10.255.255.4 172.16.255.0 10.255.255.2 
 *  ec    RD: 10.255.255.4:1 ip-prefix 192.168.3.0/24
                                 10.255.255.4          -       5       0       i Or-ID: 10.255.255.7 C-LST: 10.255.255.1 10.255.255.4 172.16.255.0 10.255.255.2 
 * >Ec    RD: 10.255.255.7:1 ip-prefix 192.168.3.0/24
                                 10.255.255.8          -       100     0       i Or-ID: 10.255.255.8 C-LST: 10.255.255.4 
 *  ec    RD: 10.255.255.7:1 ip-prefix 192.168.3.0/24
                                 10.255.255.8          -       100     0       i Or-ID: 10.255.255.8 C-LST: 10.255.255.1 10.255.255.4 
 * >      RD: 10.255.255.1:1 ip-prefix 192.168.5.0/24
                                 10.255.255.1          -       5       0       i
 * >Ec    RD: 10.255.255.4:1 ip-prefix 192.168.5.0/24
                                 10.255.255.4          -       100     0       i
 *  ec    RD: 10.255.255.4:1 ip-prefix 192.168.5.0/24
                                 10.255.255.4          -       100     0       i Or-ID: 10.255.255.4 C-LST: 10.255.255.1 
 * >Ec    RD: 10.255.255.11:1 ip-prefix 192.168.6.0/24
                                 10.255.255.11         -       100     0       i Or-ID: 10.255.255.11 C-LST: 10.255.255.4 
 *  ec    RD: 10.255.255.11:1 ip-prefix 192.168.6.0/24
                                 10.255.255.11         -       100     0       i Or-ID: 10.255.255.11 C-LST: 10.255.255.1 10.255.255.4 
 * >Ec    RD: 10.255.255.12:1 ip-prefix 192.168.6.0/24
                                 10.255.255.12         -       100     0       i Or-ID: 10.255.255.12 C-LST: 10.255.255.4 
 *  ec    RD: 10.255.255.12:1 ip-prefix 192.168.6.0/24
                                 10.255.255.12         -       100     0       i Or-ID: 10.255.255.12 C-LST: 10.255.255.1 10.255.255.4 
 * >Ec    RD: 10.255.255.1:1 ip-prefix 192.168.40.0/24
                                 10.255.255.1          -       5       0       i Or-ID: 10.255.255.1 C-LST: 10.255.255.4 10.255.255.1 172.16.255.2 
 *  ec    RD: 10.255.255.1:1 ip-prefix 192.168.40.0/24
                                 10.255.255.1          -       5       0       i
 * >Ec    RD: 10.255.255.4:1 ip-prefix 192.168.40.0/24
                                 10.255.255.4          -       5       0       i
 *  ec    RD: 10.255.255.4:1 ip-prefix 192.168.40.0/24
                                 10.255.255.4          -       5       0       i Or-ID: 10.255.255.4 C-LST: 10.255.255.1 10.255.255.4 172.16.255.0 
 * >Ec    RD: 10.255.255.10:1 ip-prefix 192.168.40.0/24
                                 10.255.255.10         -       100     0       i Or-ID: 10.255.255.10 C-LST: 10.255.255.4 
 *  ec    RD: 10.255.255.10:1 ip-prefix 192.168.40.0/24
                                 10.255.255.10         -       100     0       i Or-ID: 10.255.255.10 C-LST: 10.255.255.1 10.255.255.4 
```

## show ip security connection detail

```text
path2:
  Source address: 172.16.0.3, Destination address: 172.16.0.4
  State: established
  Uptime: 11 minutes, 11 seconds
  VRF: default
  Type: static
  Remote IP: 10.255.255.12
  Role: initiator
  Inbound SPI: 0xc4d82b:
    Request ID: 32, Mode: transport, Replay window size: 16384, Seq: 0x0
    Errors:
      Packets outside replay window: 0, Replay: 0, Integrity failed: 0
    Lifetime config:
      Soft byte limit: 3325194337499, Hard byte limit: 6442450944000
      Soft packet limit: 2125835444, Hard packet limit: 4000000000
      Soft time limit: 2939 secs, Hard time limit: 3600 secs
    Lifetime current:
      Current bytes: 5137715672
      Current packets: 15918374
      SA add time: Fri Mar 15 08:31:56 2024
      SA last use time: Fri Mar 15 08:43:06 2024
  Outbound SPI: 0xc5613c:
    Request ID: 32, Mode: transport, Replay window size: 0, Seq: 0x0
    Errors:
      Packets outside replay window: 0, Replay: 0, Integrity failed: 0
    Lifetime config:
      Soft byte limit: 3832411034249, Hard byte limit: 6442450944000
      Soft packet limit: 2895207083, Hard packet limit: 4000000000
      Soft time limit: 3048 secs, Hard time limit: 3600 secs
    Lifetime current:
      Current bytes: 3868116367
      Current packets: 14433893
      SA add time: Fri Mar 15 08:31:57 2024
      SA last use time: -
path3:
  Source address: 172.16.0.3, Destination address: 172.16.0.1
  State: established
  Uptime: 11 minutes, 7 seconds
  VRF: default
  Type: dynamic
  Remote IP: 10.255.255.5
  Role: initiator
  Packets in: 0, Packets out: 0
  Last known rekey count: 0
  Dynamic state: established
  Last established time: Fri Mar 15 08:32:34 2024
  DH crypto:
    Local rekey: 2, Peer rekey: 2, In SPI: 0x70504b8c, Out SPI: 0x76942b17
  DH state:
    Local rekey: 2, Peer rekey: 2, DH rekey state: not rekeying, Role: not rekeying
  SA rekey role: not rekeying
  SA state:
    SA type: ingress , SPI: 0x7a944b6f
      Role: initiator, SA rekey state: initial, Peer nonce type: init
      Add time: Fri Mar 15 08:32:00 2024, Packets: 1451, Pair SPI: 0x74506be4
    SA type: egress , SPI: 0x74506be4
      Role: initiator, SA rekey state: initial, Peer nonce type: init
      Add time: Fri Mar 15 08:32:00 2024, Packets: 1523, Pair SPI: 0x7a944b6f
  Inbound SPI: 0x7a944b6f:
    Request ID: 35, Mode: transport, Replay window size: 0, Seq: 0x0
    Errors:
      Packets outside replay window: 0, Replay: 0, Integrity failed: 0
    Lifetime config:
      Soft byte limit: 4707032299350, Hard byte limit: 6442450944000
      Soft packet limit: 2951035637, Hard packet limit: 4000000000
      Soft time limit: 2677 secs, Hard time limit: 3600 secs
    Lifetime current:
      Current bytes: 706724
      Current packets: 1453
      SA add time: Fri Mar 15 08:32:00 2024
      SA last use time: Fri Mar 15 08:43:05 2024
  Outbound SPI: 0x74506be4:
    Request ID: 35, Mode: transport, Replay window size: 0, Seq: 0x0
    Errors:
      Packets outside replay window: 0, Replay: 0, Integrity failed: 0
    Lifetime config:
      Soft byte limit: 4783261175175, Hard byte limit: 6442450944000
      Soft packet limit: 2938139006, Hard packet limit: 4000000000
      Soft time limit: 2544 secs, Hard time limit: 3600 secs
    Lifetime current:
      Current bytes: 1278730
      Current packets: 1525
      SA add time: Fri Mar 15 08:32:00 2024
      SA last use time: -
path4:
  Source address: 172.16.0.3, Destination address: 172.16.0.7
  State: established
  Uptime: 11 minutes, 10 seconds
  VRF: default
  Type: static
  Remote IP: 10.255.255.12
  Role: initiator
  Inbound SPI: 0xc135e0:
    Request ID: 31, Mode: transport, Replay window size: 16384, Seq: 0x0
    Errors:
      Packets outside replay window: 0, Replay: 0, Integrity failed: 0
    Lifetime config:
      Soft byte limit: 4716013600499, Hard byte limit: 6442450944000
      Soft packet limit: 2725112557, Hard packet limit: 4000000000
      Soft time limit: 2957 secs, Hard time limit: 3600 secs
    Lifetime current:
      Current bytes: 823608
      Current packets: 2254
      SA add time: Fri Mar 15 08:31:57 2024
      SA last use time: Fri Mar 15 08:43:05 2024
  Outbound SPI: 0xcc62b4:
    Request ID: 31, Mode: transport, Replay window size: 0, Seq: 0x0
    Errors:
      Packets outside replay window: 0, Replay: 0, Integrity failed: 0
    Lifetime config:
      Soft byte limit: 4601254759499, Hard byte limit: 6442450944000
      Soft packet limit: 2945498336, Hard packet limit: 4000000000
      Soft time limit: 2712 secs, Hard time limit: 3600 secs
    Lifetime current:
      Current bytes: 1350449
      Current packets: 2329
      SA add time: Fri Mar 15 08:31:57 2024
      SA last use time: -
path5:
  Source address: 172.16.0.3, Destination address: 172.16.0.9
  State: established
  Uptime: 11 minutes, 8 seconds
  VRF: default
  Type: dynamic
  Remote IP: 10.255.255.11
  Role: responder
  Packets in: 0, Packets out: 0
  Last known rekey count: 0
  Dynamic state: established
  Last established time: Fri Mar 15 08:32:34 2024
  DH crypto:
    Local rekey: 2, Peer rekey: 2, In SPI: 0x7c213f51, Out SPI: 0xb46f2af4
  DH state:
    Local rekey: 2, Peer rekey: 2, DH rekey state: not rekeying, Role: not rekeying
  SA rekey role: not rekeying
  SA state:
    SA type: ingress , SPI: 0xc06f4a4c
      Role: responder, SA rekey state: initial, Peer nonce type: init
      Add time: Fri Mar 15 08:31:59 2024, Packets: 1452, Pair SPI: 0x88215fa9
    SA type: egress , SPI: 0x88215fa9
      Role: responder, SA rekey state: initial, Peer nonce type: init
      Add time: Fri Mar 15 08:32:00 2024, Packets: 1523, Pair SPI: 0xc06f4a4c
  Inbound SPI: 0xc06f4a4c:
    Request ID: 33, Mode: transport, Replay window size: 0, Seq: 0x0
    Errors:
      Packets outside replay window: 0, Replay: 0, Integrity failed: 0
    Lifetime config:
      Soft byte limit: 4822000433700, Hard byte limit: 6442450944000
      Soft packet limit: 2930172619, Hard packet limit: 4000000000
      Soft time limit: 2677 secs, Hard time limit: 3600 secs
    Lifetime current:
      Current bytes: 706824
      Current packets: 1454
      SA add time: Fri Mar 15 08:31:59 2024
      SA last use time: Fri Mar 15 08:43:05 2024
  Outbound SPI: 0x88215fa9:
    Request ID: 33, Mode: transport, Replay window size: 0, Seq: 0x0
    Errors:
      Packets outside replay window: 0, Replay: 0, Integrity failed: 0
    Lifetime config:
      Soft byte limit: 4739793074625, Hard byte limit: 6442450944000
      Soft packet limit: 2947815705, Hard packet limit: 4000000000
      Soft time limit: 2603 secs, Hard time limit: 3600 secs
    Lifetime current:
      Current bytes: 603730
      Current packets: 1525
      SA add time: Fri Mar 15 08:32:00 2024
      SA last use time: -
path6:
  Source address: 172.16.0.3, Destination address: 172.16.0.11
  State: established
  Uptime: 11 minutes, 7 seconds
  VRF: default
  Type: dynamic
  Remote IP: 10.255.255.12
  Role: initiator
  Packets in: 0, Packets out: 0
  Last known rekey count: 0
  Dynamic state: established
  Last established time: Fri Mar 15 08:32:34 2024
  DH crypto:
    Local rekey: 2, Peer rekey: 2, In SPI: 0x58c95997, Out SPI: 0x790a51cc
  DH state:
    Local rekey: 2, Peer rekey: 2, DH rekey state: not rekeying, Role: not rekeying
  SA rekey role: not rekeying
  SA state:
    SA type: ingress , SPI: 0x870a7124
      Role: initiator, SA rekey state: initial, Peer nonce type: init
      Add time: Fri Mar 15 08:32:00 2024, Packets: 1450, Pair SPI: 0x66c979ef
    SA type: egress , SPI: 0x66c979ef
      Role: initiator, SA rekey state: initial, Peer nonce type: init
      Add time: Fri Mar 15 08:32:00 2024, Packets: 1522, Pair SPI: 0x870a7124
  Inbound SPI: 0x870a7124:
    Request ID: 34, Mode: transport, Replay window size: 0, Seq: 0x0
    Errors:
      Packets outside replay window: 0, Replay: 0, Integrity failed: 0
    Lifetime config:
      Soft byte limit: 4820361758250, Hard byte limit: 6442450944000
      Soft packet limit: 2963017447, Hard packet limit: 4000000000
      Soft time limit: 2699 secs, Hard time limit: 3600 secs
    Lifetime current:
      Current bytes: 706624
      Current packets: 1452
      SA add time: Fri Mar 15 08:32:00 2024
      SA last use time: Fri Mar 15 08:43:05 2024
  Outbound SPI: 0x66c979ef:
    Request ID: 34, Mode: transport, Replay window size: 0, Seq: 0x0
    Errors:
      Packets outside replay window: 0, Replay: 0, Integrity failed: 0
    Lifetime config:
      Soft byte limit: 4703886345225, Hard byte limit: 6442450944000
      Soft packet limit: 2972558955, Hard packet limit: 4000000000
      Soft time limit: 2656 secs, Hard time limit: 3600 secs
    Lifetime current:
      Current bytes: 603668
      Current packets: 1524
      SA add time: Fri Mar 15 08:32:00 2024
      SA last use time: -
```

## show stun client translations detail

```text
Current System Time: Fri Mar 15 08:43:08 2024
Transaction ID 000000010affff0600000000
Agent Name: dps
Source Address: 172.16.0.3:4500
Public Address: 172.16.0.3:4500
Number of Attributes: 3
Timeout Interval: 0:03:00
Last Refreshed: 0:02:15 ago
Attribute Type   Length Value           
---------------- ------ ----------------
PATH_GROUP            6 VZ_OFF          
VTEP_IP               4 10.255.255.6    
WAN_ID                4 1               

```

## show stun server bindings detail

```text
Current System Time: Fri Mar 15 08:43:09 2024
```

## show path-selection paths detail

```text
Peer: 10.255.255.1, Path group VZ_OFF
Path name: path2, static, Label: 8194
Source: 172.16.0.3, Port: 4500, WAN ID: 1
Destination: 172.16.0.4, Port: 4500, WAN ID: 2886729732
Local interface: Ethernet1/7
Route state: IPsec established
Traffic class 0: active (0:11:11)
MTU: 8914

Peer: 10.255.255.4, Path group VZ_OFF
Path name: path4, static, Label: 8196
Source: 172.16.0.3, Port: 4500, WAN ID: 1
Destination: 172.16.0.7, Port: 4500, WAN ID: 2886729735
Local interface: Ethernet1/7
Route state: IPsec established
Traffic class 0: active (0:11:11)
MTU: 8914

Peer: 10.255.255.5, Path group VZ_OFF
Path name: path3, dynamic, Label: 8195
Source: 172.16.0.3, Port: 4500, WAN ID: 1
Destination: 172.16.0.1, Port: 4500, WAN ID: 1
Local interface: Ethernet1/7
Route state: IPsec established
Traffic class 0: active (0:11:08)
MTU: 8914

Peer: 10.255.255.11, Path group VZ_OFF
Path name: path5, dynamic, Label: 8197
Source: 172.16.0.3, Port: 4500, WAN ID: 1
Destination: 172.16.0.9, Port: 4500, WAN ID: 2
Local interface: Ethernet1/7
Route state: IPsec established
Traffic class 0: active (0:11:08)
MTU: 1424

Peer: 10.255.255.12, Path group VZ_OFF
Path name: path6, dynamic, Label: 8198
Source: 172.16.0.3, Port: 4500, WAN ID: 1
Destination: 172.16.0.11, Port: 4500, WAN ID: 2
Local interface: Ethernet1/7
Route state: IPsec established
Traffic class 0: active (0:11:08)
MTU: 1424

```

## show bgp neighbors

```text
BGP neighbor is 10.255.255.1, remote AS 65000, internal link
  BGP version 4, remote router ID 10.255.255.1, VRF default
  Inherits configuration from and member of peer-group PATHFINDER
  Last read 00:00:41, last write 00:00:05
  Hold time is 180, keepalive interval is 60 seconds
  Configured hold time is 180, keepalive interval is 60 seconds
  Effective minimum hold time is 3 seconds
  Send failure hold time is 0 seconds
  Hold timer is active, time left: 00:02:19
  Keepalive timer is active, time left: 00:00:42
  Connect timer is inactive
  Idle-restart timer is inactive
  BGP state is Established, up for 00:10:06
  Number of transitions to established: 5
  Last state was OpenConfirm
  Last event was RecvUpdate
  Last sent notification:Hold Timer Expired Error/None, Last time 00:10:10, First time 00:14:02, Repeats 1
  Last rcvd notification:Cease/BFD down, Last time 00:13:15
  Last sent socket-error:Connect (Network is unreachable), Last time 19:24:56
  Types of communities advertised: standard extended large
  Enhanced route refresh stale path removal disabled
  Outbound enhanced route refresh enabled
  Neighbor Capabilities:
    Multiprotocol Dps: advertised and received and negotiated
    Multiprotocol L2VPN EVPN: advertised and received and negotiated
    Four Octet ASN: advertised and received and negotiated
    Route Refresh: advertised and received and negotiated
    Enhanced route refresh: advertised and received and negotiated
    Send End-of-RIB messages: advertised and received and negotiated
    Additional-paths recv capability:
      Dps: negotiated
      L2VPN EVPN: advertised
    Additional-paths send capability:
      Dps: negotiated
      L2VPN EVPN: received
  Restart timer is inactive
  End of rib timer is inactive
    Dps End-of-RIB received: Yes
      Received 00:10:05
      Number of stale paths removed after graceful restart: 0
      Number of paths received before End-of-RIB: 22
    L2VPN EVPN End-of-RIB received: Yes
      Received 00:10:05
      Number of stale paths removed after graceful restart: 0
      Number of paths received before End-of-RIB: 43
  AIGP attribute send and receive for IPv4 Unicast are enabled
  AIGP attribute send and receive for IPv4 with MPLS Labels are enabled
  AIGP attribute send and receive for IPv6 Unicast are enabled
  AIGP attribute send and receive for IPv6 with MPLS Labels are enabled
  BGP session driven failover for IPv4 Unicast is disabled
  BGP session driven failover for IPv6 Unicast is disabled
  Message Statistics:
                                  Sent      Rcvd
    Opens:                           7         6
    Notifications:                   5         1
    Updates:                        44     45171
    Keepalives:                   1365      1339
    Enhanced Route Refresh:          0         0
    Begin of Route Refresh:          0         0
    End of Route Refresh:            0         0
    Total messages:               1421     46517
  Prefix Statistics:
                                   Sent      Rcvd     Best Paths     Best ECMP Paths
    IPv4 Unicast:                     0         0              0                   0
    IPv4 Dps:                         2        22             22                   0
    IPv6 Unicast:                     0         0              0                   0
    EVPN:                             3        43             41                   0
  Configured maximum total number of routes is 12000
  Inbound updates dropped by reason:
    AS path loop detection: 0
    Cluster ID loop detection: 0
    Enforced First AS: 0
    Malformed MPBGP routes: 0
    Originator ID matches local router ID: 2
    Nexthop matches local IP address: 2
    Unexpected IPv6 nexthop for IPv4 routes: 0
  Inbound updates with attribute errors:
    Resulting in removal of all paths in update (treat as withdraw): 2
    Resulting in AFI/SAFI disable: 0
    Resulting in attribute ignore: 0
    Disabled AFI/SAFIs: None
    Last treat-as-withdraw attribute error: Nexthop is local address
    Last update with error received at: 00:10:05
  Inbound paths dropped by reason:
    IPv4 unicast NLRIs dropped due to martian prefix: 0
    IPv6 unicast NLRIs dropped due to martian prefix: 0
    IPv4 labeled-unicast NLRIs dropped due to excessive labels: 0
    IPv4 labeled-unicast NLRIs dropped due to martian prefix: 0
    IPv6 labeled-unicast NLRIs dropped due to excessive labels: 0
    IPv6 labeled-unicast NLRIs dropped due to martian prefix: 0
    VPN-IPv4 NLRIs dropped due to route import match failure: 0
    VPN-IPv6 NLRIs dropped due to route import match failure: 0
    L2VPN EVPN NLRIs dropped due to route import match failure: 0
    L2VPN EVPN NLRIs dropped due to unsupported route type: 0
    L2VPN EVPN NLRIs dropped due to maximum route limit violation: 0
    Link-state NLRIs dropped because reception is unsupported: 0
    RT Membership NLRIs dropped due to local origin ASN received from external peer: 0
  Outbound paths dropped by reason:
    IPv4 local address not available: 0
    IPv6 local address not available: 0
  Inbound route map for L2VPN EVPN is DENY-SOO
  Additional-paths send mode:
    Dps: any
Local AS is 65000, local router ID 10.255.255.6
TTL is 255
Local TCP address is 10.255.255.6, local port is 40279
Remote TCP address is 10.255.255.1, remote port is 179
Local next hop for next hop self:
  Dps: 10.255.255.6
  L2VPN EVPN: 10.255.255.6
BFD is enabled with configured transmit interval 1000ms, receive interval 1000ms, multiplier 3 and state is Up
TCP Socket Information:
  TCP state is ESTABLISHED
  Recv-Q: 0/32768
  Send-Q: 0/46080
  Outgoing Maximum Segment Size (MSS): 1448
  Total Number of TCP retransmissions: 0
  Options:
    Timestamps enabled: yes
    Selective Acknowledgments enabled: yes
    Window Scale enabled: yes
    Explicit Congestion Notification (ECN) enabled: no
  Socket Statistics:
    Window Scale (wscale): 7,7
    Retransmission Timeout (rto): 204.0ms
    Round-trip Time (rtt/rtvar): 3.6ms/1.5ms
    Delayed Ack Timeout (ato): 40.0ms
    Congestion Window (cwnd): 10
    TCP Throughput: 32.36 Mbps
    Advertised Recv Window (rcv_space): 14480

BGP neighbor is 10.255.255.4, remote AS 65000, internal link
  BGP version 4, remote router ID 10.255.255.4, VRF default
  Inherits configuration from and member of peer-group PATHFINDER
  Last read 00:00:24, last write 00:00:41
  Hold time is 180, keepalive interval is 60 seconds
  Configured hold time is 180, keepalive interval is 60 seconds
  Effective minimum hold time is 3 seconds
  Send failure hold time is 0 seconds
  Hold timer is active, time left: 00:02:36
  Keepalive timer is active, time left: 00:00:01
  Connect timer is inactive
  Idle-restart timer is inactive
  BGP state is Established, up for 00:11:11
  Number of transitions to established: 10
  Last state was OpenConfirm
  Last event was RecvUpdate
  Last sent notification:Cease/BFD down, Last time 00:13:03, First time 16:10:33, Repeats 8
  Last sent socket-error:Connect (No route to host), Last time 00:15:15
  Types of communities advertised: standard extended large
  Enhanced route refresh stale path removal disabled
  Outbound enhanced route refresh enabled
  Neighbor Capabilities:
    Multiprotocol Dps: advertised and received and negotiated
    Multiprotocol L2VPN EVPN: advertised and received and negotiated
    Four Octet ASN: advertised and received and negotiated
    Route Refresh: advertised and received and negotiated
    Enhanced route refresh: advertised and received and negotiated
    Send End-of-RIB messages: advertised and received and negotiated
    Additional-paths recv capability:
      Dps: negotiated
      L2VPN EVPN: advertised
    Additional-paths send capability:
      Dps: negotiated
      L2VPN EVPN: received
  Restart timer is inactive
  End of rib timer is inactive
    Dps End-of-RIB received: Yes
      Received 00:11:10
      Number of stale paths removed after graceful restart: 0
      Number of paths received before End-of-RIB: 18
    L2VPN EVPN End-of-RIB received: Yes
      Received 00:11:10
      Number of stale paths removed after graceful restart: 0
      Number of paths received before End-of-RIB: 43
  AIGP attribute send and receive for IPv4 Unicast are enabled
  AIGP attribute send and receive for IPv4 with MPLS Labels are enabled
  AIGP attribute send and receive for IPv6 Unicast are enabled
  AIGP attribute send and receive for IPv6 with MPLS Labels are enabled
  BGP session driven failover for IPv4 Unicast is disabled
  BGP session driven failover for IPv6 Unicast is disabled
  Message Statistics:
                                  Sent      Rcvd
    Opens:                          10        10
    Notifications:                   9         0
    Updates:                        78     29364
    Keepalives:                   1363      1344
    Enhanced Route Refresh:          0         0
    Begin of Route Refresh:          0         0
    End of Route Refresh:            0         0
    Total messages:               1460     30718
  Prefix Statistics:
                                   Sent      Rcvd     Best Paths     Best ECMP Paths
    IPv4 Unicast:                     0         0              0                   0
    IPv4 Dps:                         2        22             22                  12
    IPv6 Unicast:                     0         0              0                   0
    EVPN:                             3        43             41                  39
  Configured maximum total number of routes is 12000
  Inbound updates dropped by reason:
    AS path loop detection: 0
    Cluster ID loop detection: 0
    Enforced First AS: 0
    Malformed MPBGP routes: 0
    Originator ID matches local router ID: 2
    Nexthop matches local IP address: 0
    Unexpected IPv6 nexthop for IPv4 routes: 0
  Inbound updates with attribute errors:
    Resulting in removal of all paths in update (treat as withdraw): 0
    Resulting in AFI/SAFI disable: 0
    Resulting in attribute ignore: 0
    Disabled AFI/SAFIs: None
  Inbound paths dropped by reason:
    IPv4 unicast NLRIs dropped due to martian prefix: 0
    IPv6 unicast NLRIs dropped due to martian prefix: 0
    IPv4 labeled-unicast NLRIs dropped due to excessive labels: 0
    IPv4 labeled-unicast NLRIs dropped due to martian prefix: 0
    IPv6 labeled-unicast NLRIs dropped due to excessive labels: 0
    IPv6 labeled-unicast NLRIs dropped due to martian prefix: 0
    VPN-IPv4 NLRIs dropped due to route import match failure: 0
    VPN-IPv6 NLRIs dropped due to route import match failure: 0
    L2VPN EVPN NLRIs dropped due to route import match failure: 0
    L2VPN EVPN NLRIs dropped due to unsupported route type: 0
    L2VPN EVPN NLRIs dropped due to maximum route limit violation: 0
    Link-state NLRIs dropped because reception is unsupported: 0
    RT Membership NLRIs dropped due to local origin ASN received from external peer: 0
  Outbound paths dropped by reason:
    IPv4 local address not available: 0
    IPv6 local address not available: 0
  Inbound route map for L2VPN EVPN is DENY-SOO
  Additional-paths send mode:
    Dps: any
Local AS is 65000, local router ID 10.255.255.6
TTL is 255
Local TCP address is 10.255.255.6, local port is 45333
Remote TCP address is 10.255.255.4, remote port is 179
Local next hop for next hop self:
  Dps: 10.255.255.6
  L2VPN EVPN: 10.255.255.6
BFD is enabled with configured transmit interval 1000ms, receive interval 1000ms, multiplier 3 and state is Up
TCP Socket Information:
  TCP state is ESTABLISHED
  Recv-Q: 0/32768
  Send-Q: 0/46080
  Outgoing Maximum Segment Size (MSS): 1448
  Total Number of TCP retransmissions: 4
  Options:
    Timestamps enabled: yes
    Selective Acknowledgments enabled: yes
    Window Scale enabled: yes
    Explicit Congestion Notification (ECN) enabled: no
  Socket Statistics:
    Window Scale (wscale): 7,7
    Retransmission Timeout (rto): 1356.0ms
    Round-trip Time (rtt/rtvar): 123.4ms/218.9ms
    Delayed Ack Timeout (ato): 40.0ms
    Congestion Window (cwnd): 2
    TCP Throughput: 0.19 Mbps
    Advertised Recv Window (rcv_space): 14480

```

## show bgp path-selection detail

```text
BGP routing table information for VRF default
Router identifier 10.255.255.6, local AS number 65000
Bgp routing table entry for ipv4Dps VTEP 10.255.255.5/32
 Paths: 4 available
  Local
    :: from 10.255.255.4 (10.255.255.4)
      Origin IGP, metric -, localpref 100, weight 0, received 00:11:11 ago, valid, internal
      Tunnel encapsulation attribute: Dynamic path selection
        Endpoint: 172.16.0.1, Path group name: VZ_OFF, WAN ID: 1, UDP port: 4500
  Local
    :: from 10.255.255.4 (10.255.255.4)
      Origin IGP, metric -, localpref 100, weight 0, received 00:11:11 ago, valid, internal
      Tunnel encapsulation attribute: Dynamic path selection
        Endpoint: 172.16.0.1, Path group name: VZ_OFF, WAN ID: 1, UDP port: 4500
  Local
    :: from 10.255.255.1 (10.255.255.1)
      Origin IGP, metric -, localpref 100, weight 0, received 00:10:06 ago, valid, internal
      Tunnel encapsulation attribute: Dynamic path selection
        Endpoint: 172.16.0.1, Path group name: VZ_OFF, WAN ID: 1, UDP port: 4500
  Local
    :: from 10.255.255.1 (10.255.255.1)
      Origin IGP, metric -, localpref 100, weight 0, received 00:10:06 ago, valid, internal
      Tunnel encapsulation attribute: Dynamic path selection
        Endpoint: 172.16.0.1, Path group name: VZ_OFF, WAN ID: 1, UDP port: 4500
Bgp routing table entry for ipv4Dps VTEP 10.255.255.6/32
 Paths: 1 available
  Local
    - from - (0.0.0.0)
      Origin IGP, metric -, localpref -, weight 0, received 00:11:13 ago, valid, local
      Tunnel encapsulation attribute: Dynamic path selection
        Endpoint: 172.16.0.3, Path group name: VZ_OFF, WAN ID: 1, UDP port: 4500
Bgp routing table entry for ipv4Dps VTEP 10.255.255.8/32
 Paths: 4 available
  Local
    :: from 10.255.255.4 (10.255.255.4)
      Origin IGP, metric -, localpref 100, weight 0, received 00:11:11 ago, valid, internal
      Tunnel encapsulation attribute: Dynamic path selection
        Endpoint: 172.16.1.2, Path group name: VZ_NEAR, WAN ID: 1, UDP port: 4500
  Local
    :: from 10.255.255.4 (10.255.255.4)
      Origin IGP, metric -, localpref 100, weight 0, received 00:11:04 ago, valid, internal
      Tunnel encapsulation attribute: Dynamic path selection
        Endpoint: 172.16.1.2, Path group name: VZ_NEAR, WAN ID: 1, UDP port: 4500
  Local
    :: from 10.255.255.1 (10.255.255.1)
      Origin IGP, metric -, localpref 100, weight 0, received 00:10:06 ago, valid, internal
      Tunnel encapsulation attribute: Dynamic path selection
        Endpoint: 172.16.1.2, Path group name: VZ_NEAR, WAN ID: 1, UDP port: 4500
  Local
    :: from 10.255.255.1 (10.255.255.1)
      Origin IGP, metric -, localpref 100, weight 0, received 00:10:06 ago, valid, internal
      Tunnel encapsulation attribute: Dynamic path selection
        Endpoint: 172.16.1.2, Path group name: VZ_NEAR, WAN ID: 1, UDP port: 4500
Bgp routing table entry for ipv4Dps VTEP 10.255.255.10/32
 Paths: 4 available
  Local
    :: from 10.255.255.4 (10.255.255.4)
      Origin IGP, metric -, localpref 100, weight 0, received 00:11:11 ago, valid, internal
      Tunnel encapsulation attribute: Dynamic path selection
        Endpoint: 172.16.1.7, Path group name: VZ_NEAR, WAN ID: 1, UDP port: 4500
  Local
    :: from 10.255.255.4 (10.255.255.4)
      Origin IGP, metric -, localpref 100, weight 0, received 00:11:06 ago, valid, internal
      Tunnel encapsulation attribute: Dynamic path selection
        Endpoint: 172.16.1.7, Path group name: VZ_NEAR, WAN ID: 1, UDP port: 4500
  Local
    :: from 10.255.255.1 (10.255.255.1)
      Origin IGP, metric -, localpref 100, weight 0, received 00:10:06 ago, valid, internal
      Tunnel encapsulation attribute: Dynamic path selection
        Endpoint: 172.16.1.7, Path group name: VZ_NEAR, WAN ID: 1, UDP port: 4500
  Local
    :: from 10.255.255.1 (10.255.255.1)
      Origin IGP, metric -, localpref 100, weight 0, received 00:10:06 ago, valid, internal
      Tunnel encapsulation attribute: Dynamic path selection
        Endpoint: 172.16.1.7, Path group name: VZ_NEAR, WAN ID: 1, UDP port: 4500
Bgp routing table entry for ipv4Dps VTEP 10.255.255.11/32
 Paths: 4 available
  Local
    :: from 10.255.255.4 (10.255.255.4)
      Origin IGP, metric -, localpref 100, weight 0, received 00:11:11 ago, valid, internal
      Tunnel encapsulation attribute: Dynamic path selection
        Endpoint: 172.16.0.9, Path group name: VZ_OFF, WAN ID: 2, UDP port: 4500
  Local
    :: from 10.255.255.4 (10.255.255.4)
      Origin IGP, metric -, localpref 100, weight 0, received 00:11:11 ago, valid, internal
      Tunnel encapsulation attribute: Dynamic path selection
        Endpoint: 172.16.0.9, Path group name: VZ_OFF, WAN ID: 2, UDP port: 4500
  Local
    :: from 10.255.255.1 (10.255.255.1)
      Origin IGP, metric -, localpref 100, weight 0, received 00:10:06 ago, valid, internal
      Tunnel encapsulation attribute: Dynamic path selection
        Endpoint: 172.16.0.9, Path group name: VZ_OFF, WAN ID: 2, UDP port: 4500
  Local
    :: from 10.255.255.1 (10.255.255.1)
      Origin IGP, metric -, localpref 100, weight 0, received 00:10:06 ago, valid, internal
      Tunnel encapsulation attribute: Dynamic path selection
        Endpoint: 172.16.0.9, Path group name: VZ_OFF, WAN ID: 2, UDP port: 4500
Bgp routing table entry for ipv4Dps VTEP 10.255.255.12/32
 Paths: 4 available
  Local
    :: from 10.255.255.4 (10.255.255.4)
      Origin IGP, metric -, localpref 100, weight 0, received 00:11:11 ago, valid, internal
      Tunnel encapsulation attribute: Dynamic path selection
        Endpoint: 172.16.0.11, Path group name: VZ_OFF, WAN ID: 2, UDP port: 4500
  Local
    :: from 10.255.255.4 (10.255.255.4)
      Origin IGP, metric -, localpref 100, weight 0, received 00:11:11 ago, valid, internal
      Tunnel encapsulation attribute: Dynamic path selection
        Endpoint: 172.16.0.11, Path group name: VZ_OFF, WAN ID: 2, UDP port: 4500
  Local
    :: from 10.255.255.1 (10.255.255.1)
      Origin IGP, metric -, localpref 100, weight 0, received 00:10:06 ago, valid, internal
      Tunnel encapsulation attribute: Dynamic path selection
        Endpoint: 172.16.0.11, Path group name: VZ_OFF, WAN ID: 2, UDP port: 4500
  Local
    :: from 10.255.255.1 (10.255.255.1)
      Origin IGP, metric -, localpref 100, weight 0, received 00:10:06 ago, valid, internal
      Tunnel encapsulation attribute: Dynamic path selection
        Endpoint: 172.16.0.11, Path group name: VZ_OFF, WAN ID: 2, UDP port: 4500
Bgp routing table entry for ipv4Ipsec VTEP 10.255.255.1/32
 Paths: 2 available
  Local
    :: from 10.255.255.4 (10.255.255.4)
      Origin IGP, metric -, localpref 100, weight 0, received 00:11:11 ago, valid, internal
      Tunnel encapsulation attribute: IP security
        Initial contact: false, Rekey counter: 1, Nonce length: 32
        DH group: 14, DH key length: 256
        Encryption algo: aes256, Authentication algo: sha256
  Local
    :: from 10.255.255.1 (10.255.255.1)
      Origin IGP, metric -, localpref 100, weight 0, received 00:10:06 ago, valid, internal
      Tunnel encapsulation attribute: IP security
        Initial contact: false, Rekey counter: 1, Nonce length: 32
        DH group: 14, DH key length: 256
        Encryption algo: aes256, Authentication algo: sha256
Bgp routing table entry for ipv4Ipsec VTEP 10.255.255.4/32
 Paths: 2 available
  Local
    :: from 10.255.255.4 (10.255.255.4)
      Origin IGP, metric -, localpref 100, weight 0, received 00:11:11 ago, valid, internal
      Tunnel encapsulation attribute: IP security
        Initial contact: false, Rekey counter: 0, Nonce length: 32
        DH group: 14, DH key length: 256
        Encryption algo: aes256, Authentication algo: sha256
  Local
    :: from 10.255.255.1 (10.255.255.1)
      Origin IGP, metric -, localpref 100, weight 0, received 00:10:06 ago, valid, internal
      Tunnel encapsulation attribute: IP security
        Initial contact: false, Rekey counter: 0, Nonce length: 32
        DH group: 14, DH key length: 256
        Encryption algo: aes256, Authentication algo: sha256
Bgp routing table entry for ipv4Ipsec VTEP 10.255.255.5/32
 Paths: 4 available
  Local
    :: from 10.255.255.4 (10.255.255.4)
      Origin IGP, metric -, localpref 100, weight 0, received 00:11:11 ago, valid, internal
      Tunnel encapsulation attribute: IP security
        Initial contact: false, Rekey counter: 2, Nonce length: 32
        DH group: 14, DH key length: 256
        Encryption algo: aes256, Authentication algo: sha256
  Local
    :: from 10.255.255.4 (10.255.255.4)
      Origin IGP, metric -, localpref 100, weight 0, received 00:11:11 ago, valid, internal
      Tunnel encapsulation attribute: IP security
        Initial contact: false, Rekey counter: 2, Nonce length: 32
        DH group: 14, DH key length: 256
        Encryption algo: aes256, Authentication algo: sha256
  Local
    :: from 10.255.255.1 (10.255.255.1)
      Origin IGP, metric -, localpref 100, weight 0, received 00:10:06 ago, valid, internal
      Tunnel encapsulation attribute: IP security
        Initial contact: false, Rekey counter: 2, Nonce length: 32
        DH group: 14, DH key length: 256
        Encryption algo: aes256, Authentication algo: sha256
  Local
    :: from 10.255.255.1 (10.255.255.1)
      Origin IGP, metric -, localpref 100, weight 0, received 00:10:06 ago, valid, internal
      Tunnel encapsulation attribute: IP security
        Initial contact: false, Rekey counter: 2, Nonce length: 32
        DH group: 14, DH key length: 256
        Encryption algo: aes256, Authentication algo: sha256
Bgp routing table entry for ipv4Ipsec VTEP 10.255.255.6/32
 Paths: 1 available
  Local
    - from - (0.0.0.0)
      Origin IGP, metric -, localpref -, weight 0, received 19:24:36 ago, valid, local
      Tunnel encapsulation attribute: IP security
        Initial contact: false, Rekey counter: 2, Nonce length: 32
        DH group: 14, DH key length: 256
        Encryption algo: aes256, Authentication algo: sha256
Bgp routing table entry for ipv4Ipsec VTEP 10.255.255.8/32
 Paths: 4 available
  Local
    :: from 10.255.255.4 (10.255.255.4)
      Origin IGP, metric -, localpref 100, weight 0, received 00:11:11 ago, valid, internal
      Tunnel encapsulation attribute: IP security
        Initial contact: false, Rekey counter: 2, Nonce length: 32
        DH group: 14, DH key length: 256
        Encryption algo: aes256, Authentication algo: sha256
  Local
    :: from 10.255.255.4 (10.255.255.4)
      Origin IGP, metric -, localpref 100, weight 0, received 00:11:04 ago, valid, internal
      Tunnel encapsulation attribute: IP security
        Initial contact: false, Rekey counter: 2, Nonce length: 32
        DH group: 14, DH key length: 256
        Encryption algo: aes256, Authentication algo: sha256
  Local
    :: from 10.255.255.1 (10.255.255.1)
      Origin IGP, metric -, localpref 100, weight 0, received 00:10:06 ago, valid, internal
      Tunnel encapsulation attribute: IP security
        Initial contact: false, Rekey counter: 2, Nonce length: 32
        DH group: 14, DH key length: 256
        Encryption algo: aes256, Authentication algo: sha256
  Local
    :: from 10.255.255.1 (10.255.255.1)
      Origin IGP, metric -, localpref 100, weight 0, received 00:10:06 ago, valid, internal
      Tunnel encapsulation attribute: IP security
        Initial contact: false, Rekey counter: 2, Nonce length: 32
        DH group: 14, DH key length: 256
        Encryption algo: aes256, Authentication algo: sha256
Bgp routing table entry for ipv4Ipsec VTEP 10.255.255.10/32
 Paths: 4 available
  Local
    :: from 10.255.255.4 (10.255.255.4)
      Origin IGP, metric -, localpref 100, weight 0, received 00:11:11 ago, valid, internal
      Tunnel encapsulation attribute: IP security
        Initial contact: false, Rekey counter: 2, Nonce length: 32
        DH group: 14, DH key length: 256
        Encryption algo: aes256, Authentication algo: sha256
  Local
    :: from 10.255.255.4 (10.255.255.4)
      Origin IGP, metric -, localpref 100, weight 0, received 00:11:06 ago, valid, internal
      Tunnel encapsulation attribute: IP security
        Initial contact: false, Rekey counter: 2, Nonce length: 32
        DH group: 14, DH key length: 256
        Encryption algo: aes256, Authentication algo: sha256
  Local
    :: from 10.255.255.1 (10.255.255.1)
      Origin IGP, metric -, localpref 100, weight 0, received 00:10:06 ago, valid, internal
      Tunnel encapsulation attribute: IP security
        Initial contact: false, Rekey counter: 2, Nonce length: 32
        DH group: 14, DH key length: 256
        Encryption algo: aes256, Authentication algo: sha256
  Local
    :: from 10.255.255.1 (10.255.255.1)
      Origin IGP, metric -, localpref 100, weight 0, received 00:10:06 ago, valid, internal
      Tunnel encapsulation attribute: IP security
        Initial contact: false, Rekey counter: 2, Nonce length: 32
        DH group: 14, DH key length: 256
        Encryption algo: aes256, Authentication algo: sha256
Bgp routing table entry for ipv4Ipsec VTEP 10.255.255.11/32
 Paths: 4 available
  Local
    :: from 10.255.255.4 (10.255.255.4)
      Origin IGP, metric -, localpref 100, weight 0, received 00:11:11 ago, valid, internal
      Tunnel encapsulation attribute: IP security
        Initial contact: false, Rekey counter: 2, Nonce length: 32
        DH group: 14, DH key length: 256
        Encryption algo: aes256, Authentication algo: sha256
  Local
    :: from 10.255.255.4 (10.255.255.4)
      Origin IGP, metric -, localpref 100, weight 0, received 00:11:11 ago, valid, internal
      Tunnel encapsulation attribute: IP security
        Initial contact: false, Rekey counter: 2, Nonce length: 32
        DH group: 14, DH key length: 256
        Encryption algo: aes256, Authentication algo: sha256
  Local
    :: from 10.255.255.1 (10.255.255.1)
      Origin IGP, metric -, localpref 100, weight 0, received 00:10:06 ago, valid, internal
      Tunnel encapsulation attribute: IP security
        Initial contact: false, Rekey counter: 2, Nonce length: 32
        DH group: 14, DH key length: 256
        Encryption algo: aes256, Authentication algo: sha256
  Local
    :: from 10.255.255.1 (10.255.255.1)
      Origin IGP, metric -, localpref 100, weight 0, received 00:10:06 ago, valid, internal
      Tunnel encapsulation attribute: IP security
        Initial contact: false, Rekey counter: 2, Nonce length: 32
        DH group: 14, DH key length: 256
        Encryption algo: aes256, Authentication algo: sha256
Bgp routing table entry for ipv4Ipsec VTEP 10.255.255.12/32
 Paths: 4 available
  Local
    :: from 10.255.255.4 (10.255.255.4)
      Origin IGP, metric -, localpref 100, weight 0, received 00:11:11 ago, valid, internal
      Tunnel encapsulation attribute: IP security
        Initial contact: false, Rekey counter: 2, Nonce length: 32
        DH group: 14, DH key length: 256
        Encryption algo: aes256, Authentication algo: sha256
  Local
    :: from 10.255.255.4 (10.255.255.4)
      Origin IGP, metric -, localpref 100, weight 0, received 00:11:11 ago, valid, internal
      Tunnel encapsulation attribute: IP security
        Initial contact: false, Rekey counter: 2, Nonce length: 32
        DH group: 14, DH key length: 256
        Encryption algo: aes256, Authentication algo: sha256
  Local
    :: from 10.255.255.1 (10.255.255.1)
      Origin IGP, metric -, localpref 100, weight 0, received 00:10:06 ago, valid, internal
      Tunnel encapsulation attribute: IP security
        Initial contact: false, Rekey counter: 2, Nonce length: 32
        DH group: 14, DH key length: 256
        Encryption algo: aes256, Authentication algo: sha256
  Local
    :: from 10.255.255.1 (10.255.255.1)
      Origin IGP, metric -, localpref 100, weight 0, received 00:10:06 ago, valid, internal
      Tunnel encapsulation attribute: IP security
        Initial contact: false, Rekey counter: 2, Nonce length: 32
        DH group: 14, DH key length: 256
        Encryption algo: aes256, Authentication algo: sha256
```

## show rib route ip

```text
VRF: default, Protocol: connected
Codes: C - Connected, S - Static, P - Route Input, G - Gribi
       B - BGP, O - Ospf, O3 - Ospf3, I - Isis, R - Rip, VL - VRF Leak
       > - Best Route, * - Unresolved Next hop
       EM - Exact match of the SR-TE Policy
       NM - Null endpoint match of the SR-TE Policy
       AM - Any endpoint match of the SR-TE Policy
       L - Part of a recursive route resolution loop
       A - Next hop not resolved in ARP/ND
       NF - Not in FEC
>C    10.255.255.6/32 [0 pref/0 metric] updated 19:25:16 ago
         via Loopback0, directly connected
>C    172.16.0.2/31 [0 pref/0 metric] updated 00:11:21 ago
         via Ethernet1/7, directly connected
>C    172.28.128.0/20 [0 pref/0 metric] updated 19:24:58 ago
         via Management1/1, directly connected
VRF: default, Protocol: static
Codes: C - Connected, S - Static, P - Route Input, G - Gribi
       B - BGP, O - Ospf, O3 - Ospf3, I - Isis, R - Rip, VL - VRF Leak
       > - Best Route, * - Unresolved Next hop
       EM - Exact match of the SR-TE Policy
       NM - Null endpoint match of the SR-TE Policy
       AM - Any endpoint match of the SR-TE Policy
       L - Part of a recursive route resolution loop
       A - Next hop not resolved in ARP/ND
       NF - Not in FEC
>S    10.80.0.0/12 [1 pref/0 metric] updated 19:24:58 ago
         via 172.28.128.1 [0 pref/0 metric] type ipv4
            via 172.28.128.1, Management1/1
>S    10.224.0.0/12 [1 pref/0 metric] updated 19:24:58 ago
         via 172.28.128.1 [0 pref/0 metric] type ipv4
            via 172.28.128.1, Management1/1
>S    10.240.0.0/12 [1 pref/0 metric] updated 19:24:58 ago
         via 172.28.128.1 [0 pref/0 metric] type ipv4
            via 172.28.128.1, Management1/1
>S    172.16.0.0/12 [1 pref/0 metric] updated 19:24:58 ago
         via 172.28.128.1 [0 pref/0 metric] type ipv4
            via 172.28.128.1, Management1/1
>S    172.16.0.0/24 [1 pref/0 metric] updated 00:11:16 ago
         via 172.16.0.2 [0 pref/0 metric] type ipv4
            via 172.16.0.2, Ethernet1/7
VRF: default, Protocol: route-input
Codes: C - Connected, S - Static, P - Route Input, G - Gribi
       B - BGP, O - Ospf, O3 - Ospf3, I - Isis, R - Rip, VL - VRF Leak
       > - Best Route, * - Unresolved Next hop
       EM - Exact match of the SR-TE Policy
       NM - Null endpoint match of the SR-TE Policy
       AM - Any endpoint match of the SR-TE Policy
       L - Part of a recursive route resolution loop
       A - Next hop not resolved in ARP/ND
       NF - Not in FEC
>P    0.0.0.0/8 [1 pref/0 metric] updated 19:25:16 ago
         via Null0, directly connected [NF]
>P    10.255.255.1/32 [1 pref/0 metric] updated 00:11:20 ago
         via 10.255.255.1, Dps1
>P    10.255.255.4/32 [1 pref/0 metric] updated 00:11:20 ago
         via 10.255.255.4, Dps1
>P    10.255.255.5/32 [1 pref/0 metric] updated 00:11:12 ago
         via 10.255.255.5, Dps1
>P    10.255.255.11/32 [1 pref/0 metric] updated 00:11:12 ago
         via 10.255.255.11, Dps1
>P    10.255.255.12/32 [1 pref/0 metric] updated 00:11:12 ago
         via 10.255.255.12, Dps1
>P    127.0.0.0/8 [1 pref/0 metric] updated 19:25:16 ago
         via :: [1 pref/1 metric] type ipv4
            via , directly connected
```

## show rib route ipv6

```text
VRF: default, Protocol: route-input
Codes: C - Connected, S - Static, P - Route Input, G - Gribi
       B - BGP, O - Ospf, O3 - Ospf3, I - Isis, R - Rip, VL - VRF Leak
       > - Best Route, * - Unresolved Next hop
       EM - Exact match of the SR-TE Policy
       NM - Null endpoint match of the SR-TE Policy
       AM - Any endpoint match of the SR-TE Policy
       L - Part of a recursive route resolution loop
       A - Next hop not resolved in ARP/ND
       NF - Not in FEC
>P    ::/96 [1 pref/0 metric] updated 19:24:40 ago
         via Null0, directly connected [NF]
>P    ::ffff:127.0.0.0/104 [1 pref/0 metric] updated 19:24:40 ago
         via :: [1 pref/1 metric] type ipv6
            via , directly connected
>P    fe80::/10 [1 pref/0 metric] updated 19:24:40 ago
```

## show platform sfe worker summary

```text
 WorkerId Busy       PPS
 -------- ---- ---------
        0    0      2322
        1    5     27795
        2    1      3705
        3    8     49583
        4    1      3708
        5    1      4633

```

