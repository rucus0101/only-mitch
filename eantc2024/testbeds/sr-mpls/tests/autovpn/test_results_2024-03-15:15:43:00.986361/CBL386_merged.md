# Test results for CBL386

## show version

```text
Arista AWE-5310-F
Hardware version: 00.03
Serial number: WTW22500039
Hardware MAC address: ec8a.4804.2153
System MAC address: ec8a.4804.2153

Software image version: 4.31.2F
Architecture: x86_64
Internal build version: 4.31.2F-35442176.4312F
Internal build ID: 500c58e3-5beb-4481-afe9-8ad77245cc44
Image format version: 3.0
Image optimization: Default

Uptime: 19 hours and 27 minutes
Total memory: 32470188 kB
Free memory: 21161920 kB

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
Ethernet1/5      10.0.255.0/31        up         up              1500          
Ethernet1/7      172.16.0.1/31        up         up              9000          
Loopback0        10.255.255.5/32      up         up             65535          
Management1/1    172.28.138.71/20     up         up              1500          

```

## show interfaces counters rates | nz

```text
Port      Name      Intvl  In Mbps      %  In Kpps Out Mbps      % Out Kpps
Et1/5     CE         0:01     49.2   0.5%       25     44.5   0.5%       22
Et1/7     VZ_OFF     0:01     61.0   0.6%       22     67.3   0.7%       25
Ma1/1                0:01      4.9   0.5%        0      0.2   0.0%        0
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

Gateway of last resort:
 S        0.0.0.0/0 [1/0]
           via 172.16.0.0, Ethernet1/7

 S        10.80.0.0/12 [1/0]
           via 172.28.128.1, Management1/1
 S        10.239.0.0/16 [1/0]
           via 172.28.128.1, Management1/1
 S        10.255.255.1/32
           directly connected, Dps1
 S        10.255.255.4/32
           directly connected, Dps1
 C        10.255.255.5/32
           directly connected, Loopback0
 S        10.255.255.6/32
           directly connected, Dps1
 S        10.255.255.11/32
           directly connected, Dps1
 S        10.255.255.12/32
           directly connected, Dps1
 C        172.16.0.0/31
           directly connected, Ethernet1/7
 S        172.16.0.0/24 [1/0]
           via 172.16.0.0, Ethernet1/7
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

Gateway of last resort:
 S        0.0.0.0/0 [1/0]
           via 172.16.0.0, Ethernet1/7

 S        10.80.0.0/12 [1/0]
           via 172.28.128.1, Management1/1
 S        10.239.0.0/16 [1/0]
           via 172.28.128.1, Management1/1
 S        10.255.255.1/32
           directly connected, Dps1
 S        10.255.255.4/32
           directly connected, Dps1
 C        10.255.255.5/32
           directly connected, Loopback0
 S        10.255.255.6/32
           directly connected, Dps1
 S        10.255.255.11/32
           directly connected, Dps1
 S        10.255.255.12/32
           directly connected, Dps1
 C        172.16.0.0/31
           directly connected, Ethernet1/7
 S        172.16.0.0/24 [1/0]
           via 172.16.0.0, Ethernet1/7
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

 C        10.0.255.0/31
           directly connected, Ethernet1/5
 B I      10.0.255.2/31 [20/0]
           via VTEP 10.255.255.6 VNI 201 router-mac ec:8a:48:04:2b:ae
 B I      10.1.255.0/31 [20/0]
           via VTEP 10.255.255.1 VNI 201 router-mac ec:8a:48:04:f5:30
 B I      10.1.255.2/31 [20/0]
           via VTEP 10.255.255.4 VNI 201 router-mac ec:8a:48:04:ff:5b
           via VTEP 10.255.255.1 VNI 201 router-mac ec:8a:48:04:f5:30
 B I      10.2.255.0/31 [20/0]
           via VTEP 10.255.255.4 VNI 201 router-mac ec:8a:48:04:ff:5b
           via VTEP 10.255.255.1 VNI 201 router-mac ec:8a:48:04:f5:30
 B I      10.2.255.2/31 [20/0]
           via VTEP 10.255.255.8 VNI 201 router-mac ec:8a:48:04:2c:53
 B I      10.4.255.0/31 [20/0]
           via VTEP 10.255.255.4 VNI 201 router-mac ec:8a:48:04:ff:5b
           via VTEP 10.255.255.1 VNI 201 router-mac ec:8a:48:04:f5:30
 B I      10.4.255.2/31 [20/0]
           via VTEP 10.255.255.10 VNI 201 router-mac 00:0c:29:d5:32:d4
 B I      10.5.255.0/31 [20/0]
           via VTEP 10.255.255.4 VNI 201 router-mac ec:8a:48:04:ff:5b
           via VTEP 10.255.255.1 VNI 201 router-mac ec:8a:48:04:f5:30
 B I      10.5.255.2/31 [20/0]
           via VTEP 10.255.255.4 VNI 201 router-mac ec:8a:48:04:ff:5b
 B I      10.6.255.0/31 [20/0]
           via VTEP 10.255.255.11 VNI 201 router-mac 00:0c:29:ba:2d:5e
 B I      10.6.255.2/31 [20/0]
           via VTEP 10.255.255.12 VNI 201 router-mac 00:0c:29:78:c5:2d
 O        10.255.254.1/32 [110/20]
           via 10.0.255.1, Ethernet1/5
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
           via 10.0.255.1, Ethernet1/5
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
Router identifier 10.255.255.5, local AS number 65000
Route status codes: * - valid, > - active, S - Stale, E - ECMP head, e - ECMP
                    c - Contributing to ECMP, % - Pending best path selection
Origin codes: i - IGP, e - EGP, ? - incomplete
AS Path Attributes: Or-ID - Originator ID, C-LST - Cluster List, LL Nexthop - Link Local Nexthop

          Network                Next Hop              Metric  LocPref Weight  Path
 * >      RD: 10.255.255.5:1 ip-prefix 10.0.255.0/31
                                 -                     -       -       0       i
 * >Ec    RD: 10.255.255.6:1 ip-prefix 10.0.255.2/31
                                 10.255.255.6          -       100     0       i Or-ID: 10.255.255.6 C-LST: 10.255.255.4 
 *  ec    RD: 10.255.255.6:1 ip-prefix 10.0.255.2/31
                                 10.255.255.6          -       100     0       i Or-ID: 10.255.255.6 C-LST: 10.255.255.1 10.255.255.4 
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
 * >      RD: 10.255.255.5:1 ip-prefix 10.255.254.1/32
                                 -                     -       -       0       i
          RD: 10.255.255.6:1 ip-prefix 10.255.254.1/32
                                 PolicyReject          -       -       0       i Or-ID: 10.255.255.6 C-LST: 10.255.255.4 
          RD: 10.255.255.6:1 ip-prefix 10.255.254.1/32
                                 PolicyReject          -       -       0       i Or-ID: 10.255.255.6 C-LST: 10.255.255.1 10.255.255.4 
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
 * >      RD: 10.255.255.5:1 ip-prefix 192.168.0.0/24
                                 -                     -       -       0       i
          RD: 10.255.255.6:1 ip-prefix 192.168.0.0/24
                                 PolicyReject          -       -       0       i Or-ID: 10.255.255.6 C-LST: 10.255.255.4 
          RD: 10.255.255.6:1 ip-prefix 192.168.0.0/24
                                 PolicyReject          -       -       0       i Or-ID: 10.255.255.6 C-LST: 10.255.255.1 10.255.255.4 
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
path1:
  Source address: 172.16.0.1, Destination address: 172.16.0.4
  State: established
  Uptime: 11 minutes, 46 seconds
  VRF: default
  Type: static
  Remote IP: 10.255.255.1
  Role: responder
  Inbound SPI: 0xc2e358:
    Request ID: 21, Mode: transport, Replay window size: 16384, Seq: 0x0
    Errors:
      Packets outside replay window: 0, Replay: 0, Integrity failed: 0
    Lifetime config:
      Soft byte limit: 3929364554249, Hard byte limit: 6442450944000
      Soft packet limit: 2234947888, Hard packet limit: 4000000000
      Soft time limit: 2971 secs, Hard time limit: 3600 secs
    Lifetime current:
      Current bytes: 5041617048
      Current packets: 15626094
      SA add time: Fri Mar 15 08:31:22 2024
      SA last use time: Fri Mar 15 08:42:57 2024
  Outbound SPI: 0xc87f42:
    Request ID: 21, Mode: transport, Replay window size: 0, Seq: 0x0
    Errors:
      Packets outside replay window: 0, Replay: 0, Integrity failed: 0
    Lifetime config:
      Soft byte limit: 3792967557749, Hard byte limit: 6442450944000
      Soft packet limit: 2790648145, Hard packet limit: 4000000000
      Soft time limit: 2911 secs, Hard time limit: 3600 secs
    Lifetime current:
      Current bytes: 4588506784
      Current packets: 17112974
      SA add time: Fri Mar 15 08:31:22 2024
      SA last use time: -
path3:
  Source address: 172.16.0.1, Destination address: 172.16.0.3
  State: established
  Uptime: 11 minutes, 9 seconds
  VRF: default
  Type: dynamic
  Remote IP: 10.255.255.6
  Role: responder
  Packets in: 0, Packets out: 0
  Last known rekey count: 0
  Dynamic state: established
  Last established time: Fri Mar 15 08:32:27 2024
  DH crypto:
    Local rekey: 2, Peer rekey: 2, In SPI: 0x76942b17, Out SPI: 0x70504b8c
  DH state:
    Local rekey: 2, Peer rekey: 2, DH rekey state: not rekeying, Role: not rekeying
  SA rekey role: not rekeying
  SA state:
    SA type: ingress , SPI: 0x74506be4
      Role: responder, SA rekey state: initial, Peer nonce type: init
      Add time: Fri Mar 15 08:31:58 2024, Packets: 1453, Pair SPI: 0x7a944b6f
    SA type: egress , SPI: 0x7a944b6f
      Role: responder, SA rekey state: initial, Peer nonce type: init
      Add time: Fri Mar 15 08:31:59 2024, Packets: 1527, Pair SPI: 0x74506be4
  Inbound SPI: 0x74506be4:
    Request ID: 26, Mode: transport, Replay window size: 0, Seq: 0x0
    Errors:
      Packets outside replay window: 0, Replay: 0, Integrity failed: 0
    Lifetime config:
      Soft byte limit: 4711903597575, Hard byte limit: 6442450944000
      Soft packet limit: 2915302151, Hard packet limit: 4000000000
      Soft time limit: 2677 secs, Hard time limit: 3600 secs
    Lifetime current:
      Current bytes: 706924
      Current packets: 1455
      SA add time: Fri Mar 15 08:31:58 2024
      SA last use time: Fri Mar 15 08:42:56 2024
  Outbound SPI: 0x7a944b6f:
    Request ID: 26, Mode: transport, Replay window size: 0, Seq: 0x0
    Errors:
      Packets outside replay window: 0, Replay: 0, Integrity failed: 0
    Lifetime config:
      Soft byte limit: 4760610461400, Hard byte limit: 6442450944000
      Soft packet limit: 2977209346, Hard packet limit: 4000000000
      Soft time limit: 2577 secs, Hard time limit: 3600 secs
    Lifetime current:
      Current bytes: 1278946
      Current packets: 1529
      SA add time: Fri Mar 15 08:31:59 2024
      SA last use time: -
path4:
  Source address: 172.16.0.1, Destination address: 172.16.0.7
  State: established
  Uptime: 13 minutes, 51 seconds
  VRF: default
  Type: static
  Remote IP: 10.255.255.1
  Role: responder
  Inbound SPI: 0xc9fc1f:
    Request ID: 20, Mode: transport, Replay window size: 16384, Seq: 0x0
    Errors:
      Packets outside replay window: 0, Replay: 6, Integrity failed: 0
    Lifetime config:
      Soft byte limit: 3902337844499, Hard byte limit: 6442450944000
      Soft packet limit: 2063099267, Hard packet limit: 4000000000
      Soft time limit: 2597 secs, Hard time limit: 3600 secs
    Lifetime current:
      Current bytes: 101619156
      Current packets: 315425
      SA add time: Fri Mar 15 08:29:17 2024
      SA last use time: Fri Mar 15 08:42:57 2024
  Outbound SPI: 0xc5b724:
    Request ID: 20, Mode: transport, Replay window size: 0, Seq: 0x0
    Errors:
      Packets outside replay window: 0, Replay: 0, Integrity failed: 0
    Lifetime config:
      Soft byte limit: 4153728284249, Hard byte limit: 6442450944000
      Soft packet limit: 2750352620, Hard packet limit: 4000000000
      Soft time limit: 2893 secs, Hard time limit: 3600 secs
    Lifetime current:
      Current bytes: 151286227
      Current packets: 562321
      SA add time: Fri Mar 15 08:29:17 2024
      SA last use time: -
path5:
  Source address: 172.16.0.1, Destination address: 172.16.0.9
  State: established
  Uptime: 12 minutes, 56 seconds
  VRF: default
  Type: dynamic
  Remote IP: 10.255.255.11
  Role: responder
  Packets in: 0, Packets out: 0
  Last known rekey count: 0
  Dynamic state: established
  Last established time: Fri Mar 15 08:30:27 2024
  DH crypto:
    Local rekey: 2, Peer rekey: 2, In SPI: 0x2f87638e, Out SPI: 0xfb00616f
  DH state:
    Local rekey: 2, Peer rekey: 2, DH rekey state: not rekeying, Role: not rekeying
  SA rekey role: not rekeying
  SA state:
    SA type: egress , SPI: 0x398783e6
      Role: responder, SA rekey state: initial, Peer nonce type: init
      Add time: Fri Mar 15 08:30:12 2024, Packets: 1742, Pair SPI: 0x50181c7
    SA type: ingress , SPI: 0x50181c7
      Role: responder, SA rekey state: initial, Peer nonce type: init
      Add time: Fri Mar 15 08:30:12 2024, Packets: 1670, Pair SPI: 0x398783e6
  Inbound SPI: 0x50181c7:
    Request ID: 25, Mode: transport, Replay window size: 0, Seq: 0x0
    Errors:
      Packets outside replay window: 0, Replay: 0, Integrity failed: 0
    Lifetime config:
      Soft byte limit: 4763568836775, Hard byte limit: 6442450944000
      Soft packet limit: 2952680698, Hard packet limit: 4000000000
      Soft time limit: 2624 secs, Hard time limit: 3600 secs
    Lifetime current:
      Current bytes: 730368
      Current packets: 1672
      SA add time: Fri Mar 15 08:30:12 2024
      SA last use time: Fri Mar 15 08:42:56 2024
  Outbound SPI: 0x398783e6:
    Request ID: 25, Mode: transport, Replay window size: 0, Seq: 0x0
    Errors:
      Packets outside replay window: 0, Replay: 0, Integrity failed: 0
    Lifetime config:
      Soft byte limit: 4823705928750, Hard byte limit: 6442450944000
      Soft packet limit: 2910400557, Hard packet limit: 4000000000
      Soft time limit: 2535 secs, Hard time limit: 3600 secs
    Lifetime current:
      Current bytes: 615564
      Current packets: 1744
      SA add time: Fri Mar 15 08:30:12 2024
      SA last use time: -
path6:
  Source address: 172.16.0.1, Destination address: 172.16.0.11
  State: established
  Uptime: 12 minutes, 56 seconds
  VRF: default
  Type: dynamic
  Remote IP: 10.255.255.12
  Role: initiator
  Packets in: 0, Packets out: 0
  Last known rekey count: 0
  Dynamic state: established
  Last established time: Fri Mar 15 08:30:27 2024
  DH crypto:
    Local rekey: 2, Peer rekey: 2, In SPI: 0x304815fc, Out SPI: 0xf3d01204
  DH state:
    Local rekey: 2, Peer rekey: 2, DH rekey state: not rekeying, Role: not rekeying
  SA rekey role: not rekeying
  SA state:
    SA type: egress , SPI: 0x3c483554
      Role: initiator, SA rekey state: initial, Peer nonce type: init
      Add time: Fri Mar 15 08:30:12 2024, Packets: 1740, Pair SPI: 0xffd0325c
    SA type: ingress , SPI: 0xffd0325c
      Role: initiator, SA rekey state: initial, Peer nonce type: init
      Add time: Fri Mar 15 08:30:11 2024, Packets: 1668, Pair SPI: 0x3c483554
  Inbound SPI: 0xffd0325c:
    Request ID: 24, Mode: transport, Replay window size: 0, Seq: 0x0
    Errors:
      Packets outside replay window: 0, Replay: 0, Integrity failed: 0
    Lifetime config:
      Soft byte limit: 4712572495650, Hard byte limit: 6442450944000
      Soft packet limit: 2914100873, Hard packet limit: 4000000000
      Soft time limit: 2665 secs, Hard time limit: 3600 secs
    Lifetime current:
      Current bytes: 730168
      Current packets: 1670
      SA add time: Fri Mar 15 08:30:11 2024
      SA last use time: Fri Mar 15 08:42:56 2024
  Outbound SPI: 0x3c483554:
    Request ID: 24, Mode: transport, Replay window size: 0, Seq: 0x0
    Errors:
      Packets outside replay window: 0, Replay: 0, Integrity failed: 0
    Lifetime config:
      Soft byte limit: 4781431566675, Hard byte limit: 6442450944000
      Soft packet limit: 2929432490, Hard packet limit: 4000000000
      Soft time limit: 2532 secs, Hard time limit: 3600 secs
    Lifetime current:
      Current bytes: 615440
      Current packets: 1742
      SA add time: Fri Mar 15 08:30:12 2024
      SA last use time: -
```

## show stun client translations detail

```text
Current System Time: Fri Mar 15 08:43:09 2024
Transaction ID 000000010affff0500000000
Agent Name: dps
Source Address: 172.16.0.1:4500
Public Address: 172.16.0.1:4500
Number of Attributes: 3
Timeout Interval: 0:03:00
Last Refreshed: 0:01:55 ago
Attribute Type   Length Value           
---------------- ------ ----------------
PATH_GROUP            6 VZ_OFF          
VTEP_IP               4 10.255.255.5    
WAN_ID                4 1               

```

## show stun server bindings detail

```text
Current System Time: Fri Mar 15 08:43:10 2024
```

## show path-selection paths detail

```text
Peer: 10.255.255.1, Path group VZ_OFF
Path name: path1, static, Label: 4097
Source: 172.16.0.1, Port: 4500, WAN ID: 1
Destination: 172.16.0.4, Port: 4500, WAN ID: 2886729732
Local interface: Ethernet1/7
Route state: IPsec established
Traffic class 0: active (0:11:47)
MTU: 8914

Peer: 10.255.255.4, Path group VZ_OFF
Path name: path4, static, Label: 4100
Source: 172.16.0.1, Port: 4500, WAN ID: 1
Destination: 172.16.0.7, Port: 4500, WAN ID: 2886729735
Local interface: Ethernet1/7
Route state: IPsec established
Traffic class 0: active (0:13:51)
MTU: 8914

Peer: 10.255.255.6, Path group VZ_OFF
Path name: path3, dynamic, Label: 4099
Source: 172.16.0.1, Port: 4500, WAN ID: 1
Destination: 172.16.0.3, Port: 4500, WAN ID: 1
Local interface: Ethernet1/7
Route state: IPsec established
Traffic class 0: active (0:11:08)
MTU: 8914

Peer: 10.255.255.11, Path group VZ_OFF
Path name: path5, dynamic, Label: 4101
Source: 172.16.0.1, Port: 4500, WAN ID: 1
Destination: 172.16.0.9, Port: 4500, WAN ID: 2
Local interface: Ethernet1/7
Route state: IPsec established
Traffic class 0: active (0:12:57)
MTU: 1424

Peer: 10.255.255.12, Path group VZ_OFF
Path name: path6, dynamic, Label: 4102
Source: 172.16.0.1, Port: 4500, WAN ID: 1
Destination: 172.16.0.11, Port: 4500, WAN ID: 2
Local interface: Ethernet1/7
Route state: IPsec established
Traffic class 0: active (0:12:57)
MTU: 1424

```

## show bgp neighbors

```text
BGP neighbor is 10.255.255.1, remote AS 65000, internal link
  BGP version 4, remote router ID 10.255.255.1, VRF default
  Inherits configuration from and member of peer-group PATHFINDER
  Last read 00:00:06, last write 00:00:49
  Hold time is 180, keepalive interval is 60 seconds
  Configured hold time is 180, keepalive interval is 60 seconds
  Effective minimum hold time is 3 seconds
  Send failure hold time is 0 seconds
  Hold timer is active, time left: 00:02:54
  Keepalive timer is active, time left: 00:00:03
  Connect timer is inactive
  Idle-restart timer is inactive
  BGP state is Established, up for 00:11:46
  Number of transitions to established: 5
  Last state was OpenConfirm
  Last event was RecvUpdate
  Last sent notification:Hold Timer Expired Error/None, Last time 00:13:49
  Last sent socket-error:Connect (No route to host), Last time 19:24:42
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
      Received 00:11:45
      Number of stale paths removed after graceful restart: 0
      Number of paths received before End-of-RIB: 14
    L2VPN EVPN End-of-RIB received: Yes
      Received 00:11:45
      Number of stale paths removed after graceful restart: 0
      Number of paths received before End-of-RIB: 40
  AIGP attribute send and receive for IPv4 Unicast are enabled
  AIGP attribute send and receive for IPv4 with MPLS Labels are enabled
  AIGP attribute send and receive for IPv6 Unicast are enabled
  AIGP attribute send and receive for IPv6 with MPLS Labels are enabled
  BGP session driven failover for IPv4 Unicast is disabled
  BGP session driven failover for IPv6 Unicast is disabled
  Message Statistics:
                                  Sent      Rcvd
    Opens:                           5         5
    Notifications:                   4         0
    Updates:                        49     34972
    Keepalives:                   1356      1353
    Enhanced Route Refresh:          0         0
    Begin of Route Refresh:          0         0
    End of Route Refresh:            0         0
    Total messages:               1414     36330
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
    Nexthop matches local IP address: 3
    Unexpected IPv6 nexthop for IPv4 routes: 0
  Inbound updates with attribute errors:
    Resulting in removal of all paths in update (treat as withdraw): 3
    Resulting in AFI/SAFI disable: 0
    Resulting in attribute ignore: 0
    Disabled AFI/SAFIs: None
    Last treat-as-withdraw attribute error: Nexthop is local address
    Last update with error received at: 00:11:12
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
Local AS is 65000, local router ID 10.255.255.5
TTL is 255
Local TCP address is 10.255.255.5, local port is 33415
Remote TCP address is 10.255.255.1, remote port is 179
Local next hop for next hop self:
  Dps: 10.255.255.5
  L2VPN EVPN: 10.255.255.5
BFD is enabled with configured transmit interval 1000ms, receive interval 1000ms, multiplier 3 and state is Up
TCP Socket Information:
  TCP state is ESTABLISHED
  Recv-Q: 0/32768
  Send-Q: 0/46080
  Outgoing Maximum Segment Size (MSS): 1448
  Total Number of TCP retransmissions: 3
  Options:
    Timestamps enabled: yes
    Selective Acknowledgments enabled: yes
    Window Scale enabled: yes
    Explicit Congestion Notification (ECN) enabled: no
  Socket Statistics:
    Window Scale (wscale): 7,7
    Retransmission Timeout (rto): 208.0ms
    Round-trip Time (rtt/rtvar): 6.8ms/4.9ms
    Delayed Ack Timeout (ato): 40.0ms
    Congestion Window (cwnd): 2
    TCP Throughput: 3.43 Mbps
    Advertised Recv Window (rcv_space): 14480

BGP neighbor is 10.255.255.4, remote AS 65000, internal link
  BGP version 4, remote router ID 10.255.255.4, VRF default
  Inherits configuration from and member of peer-group PATHFINDER
  Last read 00:00:15, last write 00:00:03
  Hold time is 180, keepalive interval is 60 seconds
  Configured hold time is 180, keepalive interval is 60 seconds
  Effective minimum hold time is 3 seconds
  Send failure hold time is 0 seconds
  Hold timer is active, time left: 00:02:45
  Keepalive timer is active, time left: 00:00:39
  Connect timer is inactive
  Idle-restart timer is inactive
  BGP state is Established, up for 00:13:01
  Number of transitions to established: 9
  Last state was OpenConfirm
  Last event was RecvUpdate
  Last sent notification:Cease/BFD down, Last time 00:13:03, First time 19:07:22, Repeats 7
  Last sent socket-error:Connect (No route to host), Last time 00:13:58, First time 19:24:42, Repeats 1
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
      Received 00:12:59
      Number of stale paths removed after graceful restart: 0
      Number of paths received before End-of-RIB: 9
    L2VPN EVPN End-of-RIB received: Yes
      Received 00:12:59
      Number of stale paths removed after graceful restart: 0
      Number of paths received before End-of-RIB: 27
  AIGP attribute send and receive for IPv4 Unicast are enabled
  AIGP attribute send and receive for IPv4 with MPLS Labels are enabled
  AIGP attribute send and receive for IPv6 Unicast are enabled
  AIGP attribute send and receive for IPv6 with MPLS Labels are enabled
  BGP session driven failover for IPv4 Unicast is disabled
  BGP session driven failover for IPv6 Unicast is disabled
  Message Statistics:
                                  Sent      Rcvd
    Opens:                           9         9
    Notifications:                   8         0
    Updates:                        68     22845
    Keepalives:                   1363      1347
    Enhanced Route Refresh:          0         0
    Begin of Route Refresh:          0         0
    End of Route Refresh:            0         0
    Total messages:               1448     24201
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
Local AS is 65000, local router ID 10.255.255.5
TTL is 255
Local TCP address is 10.255.255.5, local port is 43779
Remote TCP address is 10.255.255.4, remote port is 179
Local next hop for next hop self:
  Dps: 10.255.255.5
  L2VPN EVPN: 10.255.255.5
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
    Retransmission Timeout (rto): 208.0ms
    Round-trip Time (rtt/rtvar): 6.3ms/6.5ms
    Delayed Ack Timeout (ato): 40.0ms
    Congestion Window (cwnd): 10
    TCP Throughput: 18.35 Mbps
    Recv Round-trip Time (rcv_rtt): 2230.9ms
    Advertised Recv Window (rcv_space): 14480

```

## show bgp path-selection detail

```text
BGP routing table information for VRF default
Router identifier 10.255.255.5, local AS number 65000
Bgp routing table entry for ipv4Dps VTEP 10.255.255.5/32
 Paths: 1 available
  Local
    - from - (0.0.0.0)
      Origin IGP, metric -, localpref -, weight 0, received 00:13:52 ago, valid, local
      Tunnel encapsulation attribute: Dynamic path selection
        Endpoint: 172.16.0.1, Path group name: VZ_OFF, WAN ID: 1, UDP port: 4500
Bgp routing table entry for ipv4Dps VTEP 10.255.255.6/32
 Paths: 4 available
  Local
    :: from 10.255.255.4 (10.255.255.4)
      Origin IGP, metric -, localpref 100, weight 0, received 00:11:12 ago, valid, internal
      Tunnel encapsulation attribute: Dynamic path selection
        Endpoint: 172.16.0.3, Path group name: VZ_OFF, WAN ID: 1, UDP port: 4500
  Local
    :: from 10.255.255.1 (10.255.255.1)
      Origin IGP, metric -, localpref 100, weight 0, received 00:11:12 ago, valid, internal
      Tunnel encapsulation attribute: Dynamic path selection
        Endpoint: 172.16.0.3, Path group name: VZ_OFF, WAN ID: 1, UDP port: 4500
  Local
    :: from 10.255.255.1 (10.255.255.1)
      Origin IGP, metric -, localpref 100, weight 0, received 00:10:06 ago, valid, internal
      Tunnel encapsulation attribute: Dynamic path selection
        Endpoint: 172.16.0.3, Path group name: VZ_OFF, WAN ID: 1, UDP port: 4500
  Local
    :: from 10.255.255.4 (10.255.255.4)
      Origin IGP, metric -, localpref 100, weight 0, received 00:10:06 ago, valid, internal
      Tunnel encapsulation attribute: Dynamic path selection
        Endpoint: 172.16.0.3, Path group name: VZ_OFF, WAN ID: 1, UDP port: 4500
Bgp routing table entry for ipv4Dps VTEP 10.255.255.8/32
 Paths: 4 available
  Local
    :: from 10.255.255.4 (10.255.255.4)
      Origin IGP, metric -, localpref 100, weight 0, received 00:12:59 ago, valid, internal
      Tunnel encapsulation attribute: Dynamic path selection
        Endpoint: 172.16.1.2, Path group name: VZ_NEAR, WAN ID: 1, UDP port: 4500
  Local
    :: from 10.255.255.1 (10.255.255.1)
      Origin IGP, metric -, localpref 100, weight 0, received 00:11:45 ago, valid, internal
      Tunnel encapsulation attribute: Dynamic path selection
        Endpoint: 172.16.1.2, Path group name: VZ_NEAR, WAN ID: 1, UDP port: 4500
  Local
    :: from 10.255.255.1 (10.255.255.1)
      Origin IGP, metric -, localpref 100, weight 0, received 00:11:04 ago, valid, internal
      Tunnel encapsulation attribute: Dynamic path selection
        Endpoint: 172.16.1.2, Path group name: VZ_NEAR, WAN ID: 1, UDP port: 4500
  Local
    :: from 10.255.255.4 (10.255.255.4)
      Origin IGP, metric -, localpref 100, weight 0, received 00:11:04 ago, valid, internal
      Tunnel encapsulation attribute: Dynamic path selection
        Endpoint: 172.16.1.2, Path group name: VZ_NEAR, WAN ID: 1, UDP port: 4500
Bgp routing table entry for ipv4Dps VTEP 10.255.255.10/32
 Paths: 4 available
  Local
    :: from 10.255.255.4 (10.255.255.4)
      Origin IGP, metric -, localpref 100, weight 0, received 00:12:59 ago, valid, internal
      Tunnel encapsulation attribute: Dynamic path selection
        Endpoint: 172.16.1.7, Path group name: VZ_NEAR, WAN ID: 1, UDP port: 4500
  Local
    :: from 10.255.255.1 (10.255.255.1)
      Origin IGP, metric -, localpref 100, weight 0, received 00:11:45 ago, valid, internal
      Tunnel encapsulation attribute: Dynamic path selection
        Endpoint: 172.16.1.7, Path group name: VZ_NEAR, WAN ID: 1, UDP port: 4500
  Local
    :: from 10.255.255.1 (10.255.255.1)
      Origin IGP, metric -, localpref 100, weight 0, received 00:11:06 ago, valid, internal
      Tunnel encapsulation attribute: Dynamic path selection
        Endpoint: 172.16.1.7, Path group name: VZ_NEAR, WAN ID: 1, UDP port: 4500
  Local
    :: from 10.255.255.4 (10.255.255.4)
      Origin IGP, metric -, localpref 100, weight 0, received 00:11:06 ago, valid, internal
      Tunnel encapsulation attribute: Dynamic path selection
        Endpoint: 172.16.1.7, Path group name: VZ_NEAR, WAN ID: 1, UDP port: 4500
Bgp routing table entry for ipv4Dps VTEP 10.255.255.11/32
 Paths: 4 available
  Local
    :: from 10.255.255.4 (10.255.255.4)
      Origin IGP, metric -, localpref 100, weight 0, received 00:12:59 ago, valid, internal
      Tunnel encapsulation attribute: Dynamic path selection
        Endpoint: 172.16.0.9, Path group name: VZ_OFF, WAN ID: 2, UDP port: 4500
  Local
    :: from 10.255.255.4 (10.255.255.4)
      Origin IGP, metric -, localpref 100, weight 0, received 00:11:56 ago, valid, internal
      Tunnel encapsulation attribute: Dynamic path selection
        Endpoint: 172.16.0.9, Path group name: VZ_OFF, WAN ID: 2, UDP port: 4500
  Local
    :: from 10.255.255.1 (10.255.255.1)
      Origin IGP, metric -, localpref 100, weight 0, received 00:11:45 ago, valid, internal
      Tunnel encapsulation attribute: Dynamic path selection
        Endpoint: 172.16.0.9, Path group name: VZ_OFF, WAN ID: 2, UDP port: 4500
  Local
    :: from 10.255.255.1 (10.255.255.1)
      Origin IGP, metric -, localpref 100, weight 0, received 00:11:45 ago, valid, internal
      Tunnel encapsulation attribute: Dynamic path selection
        Endpoint: 172.16.0.9, Path group name: VZ_OFF, WAN ID: 2, UDP port: 4500
Bgp routing table entry for ipv4Dps VTEP 10.255.255.12/32
 Paths: 4 available
  Local
    :: from 10.255.255.4 (10.255.255.4)
      Origin IGP, metric -, localpref 100, weight 0, received 00:12:59 ago, valid, internal
      Tunnel encapsulation attribute: Dynamic path selection
        Endpoint: 172.16.0.11, Path group name: VZ_OFF, WAN ID: 2, UDP port: 4500
  Local
    :: from 10.255.255.4 (10.255.255.4)
      Origin IGP, metric -, localpref 100, weight 0, received 00:11:55 ago, valid, internal
      Tunnel encapsulation attribute: Dynamic path selection
        Endpoint: 172.16.0.11, Path group name: VZ_OFF, WAN ID: 2, UDP port: 4500
  Local
    :: from 10.255.255.1 (10.255.255.1)
      Origin IGP, metric -, localpref 100, weight 0, received 00:11:45 ago, valid, internal
      Tunnel encapsulation attribute: Dynamic path selection
        Endpoint: 172.16.0.11, Path group name: VZ_OFF, WAN ID: 2, UDP port: 4500
  Local
    :: from 10.255.255.1 (10.255.255.1)
      Origin IGP, metric -, localpref 100, weight 0, received 00:11:45 ago, valid, internal
      Tunnel encapsulation attribute: Dynamic path selection
        Endpoint: 172.16.0.11, Path group name: VZ_OFF, WAN ID: 2, UDP port: 4500
Bgp routing table entry for ipv4Ipsec VTEP 10.255.255.1/32
 Paths: 2 available
  Local
    :: from 10.255.255.4 (10.255.255.4)
      Origin IGP, metric -, localpref 100, weight 0, received 00:12:03 ago, valid, internal
      Tunnel encapsulation attribute: IP security
        Initial contact: false, Rekey counter: 1, Nonce length: 32
        DH group: 14, DH key length: 256
        Encryption algo: aes256, Authentication algo: sha256
  Local
    :: from 10.255.255.1 (10.255.255.1)
      Origin IGP, metric -, localpref 100, weight 0, received 00:11:45 ago, valid, internal
      Tunnel encapsulation attribute: IP security
        Initial contact: false, Rekey counter: 1, Nonce length: 32
        DH group: 14, DH key length: 256
        Encryption algo: aes256, Authentication algo: sha256
Bgp routing table entry for ipv4Ipsec VTEP 10.255.255.4/32
 Paths: 2 available
  Local
    :: from 10.255.255.4 (10.255.255.4)
      Origin IGP, metric -, localpref 100, weight 0, received 00:12:59 ago, valid, internal
      Tunnel encapsulation attribute: IP security
        Initial contact: false, Rekey counter: 0, Nonce length: 32
        DH group: 14, DH key length: 256
        Encryption algo: aes256, Authentication algo: sha256
  Local
    :: from 10.255.255.1 (10.255.255.1)
      Origin IGP, metric -, localpref 100, weight 0, received 00:11:45 ago, valid, internal
      Tunnel encapsulation attribute: IP security
        Initial contact: false, Rekey counter: 0, Nonce length: 32
        DH group: 14, DH key length: 256
        Encryption algo: aes256, Authentication algo: sha256
Bgp routing table entry for ipv4Ipsec VTEP 10.255.255.5/32
 Paths: 1 available
  Local
    - from - (0.0.0.0)
      Origin IGP, metric -, localpref -, weight 0, received 19:24:43 ago, valid, local
      Tunnel encapsulation attribute: IP security
        Initial contact: false, Rekey counter: 2, Nonce length: 32
        DH group: 14, DH key length: 256
        Encryption algo: aes256, Authentication algo: sha256
Bgp routing table entry for ipv4Ipsec VTEP 10.255.255.6/32
 Paths: 4 available
  Local
    :: from 10.255.255.4 (10.255.255.4)
      Origin IGP, metric -, localpref 100, weight 0, received 00:11:12 ago, valid, internal
      Tunnel encapsulation attribute: IP security
        Initial contact: false, Rekey counter: 2, Nonce length: 32
        DH group: 14, DH key length: 256
        Encryption algo: aes256, Authentication algo: sha256
  Local
    :: from 10.255.255.1 (10.255.255.1)
      Origin IGP, metric -, localpref 100, weight 0, received 00:11:12 ago, valid, internal
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
    :: from 10.255.255.4 (10.255.255.4)
      Origin IGP, metric -, localpref 100, weight 0, received 00:10:06 ago, valid, internal
      Tunnel encapsulation attribute: IP security
        Initial contact: false, Rekey counter: 2, Nonce length: 32
        DH group: 14, DH key length: 256
        Encryption algo: aes256, Authentication algo: sha256
Bgp routing table entry for ipv4Ipsec VTEP 10.255.255.8/32
 Paths: 4 available
  Local
    :: from 10.255.255.4 (10.255.255.4)
      Origin IGP, metric -, localpref 100, weight 0, received 00:12:59 ago, valid, internal
      Tunnel encapsulation attribute: IP security
        Initial contact: false, Rekey counter: 2, Nonce length: 32
        DH group: 14, DH key length: 256
        Encryption algo: aes256, Authentication algo: sha256
  Local
    :: from 10.255.255.1 (10.255.255.1)
      Origin IGP, metric -, localpref 100, weight 0, received 00:11:45 ago, valid, internal
      Tunnel encapsulation attribute: IP security
        Initial contact: false, Rekey counter: 2, Nonce length: 32
        DH group: 14, DH key length: 256
        Encryption algo: aes256, Authentication algo: sha256
  Local
    :: from 10.255.255.1 (10.255.255.1)
      Origin IGP, metric -, localpref 100, weight 0, received 00:11:04 ago, valid, internal
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
Bgp routing table entry for ipv4Ipsec VTEP 10.255.255.10/32
 Paths: 4 available
  Local
    :: from 10.255.255.4 (10.255.255.4)
      Origin IGP, metric -, localpref 100, weight 0, received 00:12:59 ago, valid, internal
      Tunnel encapsulation attribute: IP security
        Initial contact: false, Rekey counter: 2, Nonce length: 32
        DH group: 14, DH key length: 256
        Encryption algo: aes256, Authentication algo: sha256
  Local
    :: from 10.255.255.1 (10.255.255.1)
      Origin IGP, metric -, localpref 100, weight 0, received 00:11:45 ago, valid, internal
      Tunnel encapsulation attribute: IP security
        Initial contact: false, Rekey counter: 2, Nonce length: 32
        DH group: 14, DH key length: 256
        Encryption algo: aes256, Authentication algo: sha256
  Local
    :: from 10.255.255.1 (10.255.255.1)
      Origin IGP, metric -, localpref 100, weight 0, received 00:11:06 ago, valid, internal
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
Bgp routing table entry for ipv4Ipsec VTEP 10.255.255.11/32
 Paths: 4 available
  Local
    :: from 10.255.255.4 (10.255.255.4)
      Origin IGP, metric -, localpref 100, weight 0, received 00:12:59 ago, valid, internal
      Tunnel encapsulation attribute: IP security
        Initial contact: false, Rekey counter: 2, Nonce length: 32
        DH group: 14, DH key length: 256
        Encryption algo: aes256, Authentication algo: sha256
  Local
    :: from 10.255.255.4 (10.255.255.4)
      Origin IGP, metric -, localpref 100, weight 0, received 00:11:56 ago, valid, internal
      Tunnel encapsulation attribute: IP security
        Initial contact: false, Rekey counter: 2, Nonce length: 32
        DH group: 14, DH key length: 256
        Encryption algo: aes256, Authentication algo: sha256
  Local
    :: from 10.255.255.1 (10.255.255.1)
      Origin IGP, metric -, localpref 100, weight 0, received 00:11:45 ago, valid, internal
      Tunnel encapsulation attribute: IP security
        Initial contact: false, Rekey counter: 2, Nonce length: 32
        DH group: 14, DH key length: 256
        Encryption algo: aes256, Authentication algo: sha256
  Local
    :: from 10.255.255.1 (10.255.255.1)
      Origin IGP, metric -, localpref 100, weight 0, received 00:11:45 ago, valid, internal
      Tunnel encapsulation attribute: IP security
        Initial contact: false, Rekey counter: 2, Nonce length: 32
        DH group: 14, DH key length: 256
        Encryption algo: aes256, Authentication algo: sha256
Bgp routing table entry for ipv4Ipsec VTEP 10.255.255.12/32
 Paths: 4 available
  Local
    :: from 10.255.255.4 (10.255.255.4)
      Origin IGP, metric -, localpref 100, weight 0, received 00:12:59 ago, valid, internal
      Tunnel encapsulation attribute: IP security
        Initial contact: false, Rekey counter: 2, Nonce length: 32
        DH group: 14, DH key length: 256
        Encryption algo: aes256, Authentication algo: sha256
  Local
    :: from 10.255.255.4 (10.255.255.4)
      Origin IGP, metric -, localpref 100, weight 0, received 00:11:55 ago, valid, internal
      Tunnel encapsulation attribute: IP security
        Initial contact: false, Rekey counter: 2, Nonce length: 32
        DH group: 14, DH key length: 256
        Encryption algo: aes256, Authentication algo: sha256
  Local
    :: from 10.255.255.1 (10.255.255.1)
      Origin IGP, metric -, localpref 100, weight 0, received 00:11:45 ago, valid, internal
      Tunnel encapsulation attribute: IP security
        Initial contact: false, Rekey counter: 2, Nonce length: 32
        DH group: 14, DH key length: 256
        Encryption algo: aes256, Authentication algo: sha256
  Local
    :: from 10.255.255.1 (10.255.255.1)
      Origin IGP, metric -, localpref 100, weight 0, received 00:11:45 ago, valid, internal
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
>C    10.255.255.5/32 [0 pref/0 metric] updated 19:25:25 ago
         via Loopback0, directly connected
>C    172.16.0.0/31 [0 pref/0 metric] updated 00:14:01 ago
         via Ethernet1/7, directly connected
>C    172.28.128.0/20 [0 pref/0 metric] updated 19:25:05 ago
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
>S    0.0.0.0/0 [1 pref/0 metric] updated 00:13:56 ago
         via 172.16.0.0 [0 pref/0 metric] type ipv4
            via 172.16.0.0, Ethernet1/7
>S    10.80.0.0/12 [1 pref/0 metric] updated 19:25:05 ago
         via 172.28.128.1 [0 pref/0 metric] type ipv4
            via 172.28.128.1, Management1/1
>S    10.239.0.0/16 [1 pref/0 metric] updated 19:25:05 ago
         via 172.28.128.1 [0 pref/0 metric] type ipv4
            via 172.28.128.1, Management1/1
>S    172.16.0.0/12 [1 pref/0 metric] updated 19:25:05 ago
         via 172.28.128.1 [0 pref/0 metric] type ipv4
            via 172.28.128.1, Management1/1
>S    172.16.0.0/24 [1 pref/0 metric] updated 00:13:56 ago
         via 172.16.0.0 [0 pref/0 metric] type ipv4
            via 172.16.0.0, Ethernet1/7
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
>P    0.0.0.0/8 [1 pref/0 metric] updated 19:25:23 ago
         via Null0, directly connected [NF]
>P    10.255.255.1/32 [1 pref/0 metric] updated 00:13:59 ago
         via 10.255.255.1, Dps1
>P    10.255.255.4/32 [1 pref/0 metric] updated 00:13:59 ago
         via 10.255.255.4, Dps1
>P    10.255.255.6/32 [1 pref/0 metric] updated 00:11:13 ago
         via 10.255.255.6, Dps1
>P    10.255.255.11/32 [1 pref/0 metric] updated 00:13:00 ago
         via 10.255.255.11, Dps1
>P    10.255.255.12/32 [1 pref/0 metric] updated 00:13:00 ago
         via 10.255.255.12, Dps1
>P    127.0.0.0/8 [1 pref/0 metric] updated 19:25:23 ago
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
>P    ::/96 [1 pref/0 metric] updated 19:24:48 ago
         via Null0, directly connected [NF]
>P    ::ffff:127.0.0.0/104 [1 pref/0 metric] updated 19:24:48 ago
         via :: [1 pref/1 metric] type ipv6
            via , directly connected
>P    fe80::/10 [1 pref/0 metric] updated 19:24:48 ago
```

## show platform sfe worker summary

```text
 WorkerId Busy       PPS
 -------- ---- ---------
        0    7     25023
        1    5     29187
        2    1      4633
        3    3     25955
        4    0      3245
        5    1      5559

```

