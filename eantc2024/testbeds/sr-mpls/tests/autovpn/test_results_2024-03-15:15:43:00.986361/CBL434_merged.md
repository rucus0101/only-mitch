# Test results for CBL434

## show version

```text
Arista AWE-5310-F
Hardware version: 11.01
Serial number: WTW23341340
Hardware MAC address: ec8a.4804.2bda
System MAC address: ec8a.4804.2bda

Software image version: 4.31.2F
Architecture: x86_64
Internal build version: 4.31.2F-35442176.4312F
Internal build ID: 500c58e3-5beb-4481-afe9-8ad77245cc44
Image format version: 3.0
Image optimization: Default

Uptime: 19 hours and 27 minutes
Total memory: 32470188 kB
Free memory: 21203576 kB

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
Ethernet1/5      10.2.255.0/31        up         up              1500          
Ethernet1/7      172.16.2.2/31        up         up              9000          
Loopback0        10.255.255.7/32      up         up             65535          
Management1/1    172.28.138.221/20    up         up              1500          

```

## show interfaces counters rates | nz

```text
Port      Name      Intvl  In Mbps      %  In Kpps Out Mbps      % Out Kpps
Ma1/1                0:01      4.5   0.5%        0      0.2   0.0%        0
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
 S        10.255.255.2/32
           directly connected, Dps1
 S        10.255.255.3/32
           directly connected, Dps1
 C        10.255.255.7/32
           directly connected, Loopback0
 S        10.255.255.9/32
           directly connected, Dps1
 S        10.240.0.0/12 [1/0]
           via 172.28.128.1, Management1/1
 C        172.16.2.2/31
           directly connected, Ethernet1/7
 S        172.16.2.0/24 [1/0]
           via 172.16.2.3, Ethernet1/7
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
 S        10.255.255.2/32
           directly connected, Dps1
 S        10.255.255.3/32
           directly connected, Dps1
 C        10.255.255.7/32
           directly connected, Loopback0
 S        10.255.255.9/32
           directly connected, Dps1
 S        10.240.0.0/12 [1/0]
           via 172.28.128.1, Management1/1
 C        172.16.2.2/31
           directly connected, Ethernet1/7
 S        172.16.2.0/24 [1/0]
           via 172.16.2.3, Ethernet1/7
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
           via VTEP 10.255.255.2 VNI 201 router-mac ec:8a:48:04:f5:69
           via VTEP 10.255.255.3 VNI 201 router-mac ec:8a:48:04:ff:6e
 B I      10.0.255.2/31 [20/0]
           via VTEP 10.255.255.2 VNI 201 router-mac ec:8a:48:04:f5:69
           via VTEP 10.255.255.3 VNI 201 router-mac ec:8a:48:04:ff:6e
 B I      10.1.255.0/31 [20/0]
           via VTEP 10.255.255.2 VNI 201 router-mac ec:8a:48:04:f5:69
           via VTEP 10.255.255.3 VNI 201 router-mac ec:8a:48:04:ff:6e
 B I      10.1.255.2/31 [20/0]
           via VTEP 10.255.255.2 VNI 201 router-mac ec:8a:48:04:f5:69
 C        10.2.255.0/31
           directly connected, Ethernet1/5
 B I      10.2.255.2/31 [20/0]
           via VTEP 10.255.255.2 VNI 201 router-mac ec:8a:48:04:f5:69
           via VTEP 10.255.255.3 VNI 201 router-mac ec:8a:48:04:ff:6e
 B I      10.4.255.0/31 [20/0]
           via VTEP 10.255.255.9 VNI 201 router-mac 00:50:56:47:de:91
 B I      10.4.255.2/31 [20/0]
           via VTEP 10.255.255.2 VNI 201 router-mac ec:8a:48:04:f5:69
           via VTEP 10.255.255.3 VNI 201 router-mac ec:8a:48:04:ff:6e
 B I      10.5.255.0/31 [20/0]
           via VTEP 10.255.255.3 VNI 201 router-mac ec:8a:48:04:ff:6e
 B I      10.5.255.2/31 [20/0]
           via VTEP 10.255.255.2 VNI 201 router-mac ec:8a:48:04:f5:69
           via VTEP 10.255.255.3 VNI 201 router-mac ec:8a:48:04:ff:6e
 B I      10.6.255.0/31 [20/0]
           via VTEP 10.255.255.2 VNI 201 router-mac ec:8a:48:04:f5:69
           via VTEP 10.255.255.3 VNI 201 router-mac ec:8a:48:04:ff:6e
 B I      10.6.255.2/31 [20/0]
           via VTEP 10.255.255.2 VNI 201 router-mac ec:8a:48:04:f5:69
           via VTEP 10.255.255.3 VNI 201 router-mac ec:8a:48:04:ff:6e
 B I      10.255.254.1/32 [20/0]
           via VTEP 10.255.255.2 VNI 201 router-mac ec:8a:48:04:f5:69
           via VTEP 10.255.255.3 VNI 201 router-mac ec:8a:48:04:ff:6e
 B I      10.255.254.2/32 [20/0]
           via VTEP 10.255.255.2 VNI 201 router-mac ec:8a:48:04:f5:69
 O        10.255.254.3/32 [110/20]
           via 10.2.255.1, Ethernet1/5
 B I      10.255.254.4/32 [20/0]
           via VTEP 10.255.255.2 VNI 201 router-mac ec:8a:48:04:f5:69
           via VTEP 10.255.255.3 VNI 201 router-mac ec:8a:48:04:ff:6e
 B I      10.255.254.5/32 [20/0]
           via VTEP 10.255.255.9 VNI 201 router-mac 00:50:56:47:de:91
 B I      10.255.254.6/32 [20/0]
           via VTEP 10.255.255.3 VNI 201 router-mac ec:8a:48:04:ff:6e
 B I      172.16.255.0/31 [20/0]
           via VTEP 10.255.255.3 VNI 201 router-mac ec:8a:48:04:ff:6e
 B I      172.16.255.2/31 [20/0]
           via VTEP 10.255.255.2 VNI 201 router-mac ec:8a:48:04:f5:69
 B I      192.168.0.0/24 [20/0]
           via VTEP 10.255.255.2 VNI 201 router-mac ec:8a:48:04:f5:69
           via VTEP 10.255.255.3 VNI 201 router-mac ec:8a:48:04:ff:6e
 B I      192.168.1.0/24 [20/0]
           via VTEP 10.255.255.2 VNI 201 router-mac ec:8a:48:04:f5:69
 O        192.168.3.0/24 [110/20]
           via 10.2.255.1, Ethernet1/5
 B I      192.168.5.0/24 [20/0]
           via VTEP 10.255.255.3 VNI 201 router-mac ec:8a:48:04:ff:6e
 B I      192.168.6.0/24 [20/0]
           via VTEP 10.255.255.2 VNI 201 router-mac ec:8a:48:04:f5:69
           via VTEP 10.255.255.3 VNI 201 router-mac ec:8a:48:04:ff:6e
 B I      192.168.40.0/24 [20/0]
           via VTEP 10.255.255.9 VNI 201 router-mac 00:50:56:47:de:91

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
Router identifier 10.255.255.7, local AS number 65000
Route status codes: * - valid, > - active, S - Stale, E - ECMP head, e - ECMP
                    c - Contributing to ECMP, % - Pending best path selection
Origin codes: i - IGP, e - EGP, ? - incomplete
AS Path Attributes: Or-ID - Originator ID, C-LST - Cluster List, LL Nexthop - Link Local Nexthop

          Network                Next Hop              Metric  LocPref Weight  Path
 * >Ec    RD: 10.255.255.2:1 ip-prefix 10.0.255.0/31
                                 10.255.255.2          -       5       0       i Or-ID: 10.255.255.5 C-LST: 10.255.255.2 172.16.255.3 10.255.255.4 
 *  ec    RD: 10.255.255.2:1 ip-prefix 10.0.255.0/31
                                 10.255.255.2          -       5       0       i Or-ID: 10.255.255.5 C-LST: 10.255.255.3 10.255.255.2 172.16.255.3 10.255.255.4 
 * >Ec    RD: 10.255.255.3:1 ip-prefix 10.0.255.0/31
                                 10.255.255.3          -       5       0       i
 *  ec    RD: 10.255.255.3:1 ip-prefix 10.0.255.0/31
                                 10.255.255.3          -       5       0       i Or-ID: 10.255.255.3 C-LST: 10.255.255.2 10.255.255.3 172.16.255.1 
 * >Ec    RD: 10.255.255.2:1 ip-prefix 10.0.255.2/31
                                 10.255.255.2          -       5       0       i Or-ID: 10.255.255.6 C-LST: 10.255.255.2 172.16.255.3 10.255.255.4 
 *  ec    RD: 10.255.255.2:1 ip-prefix 10.0.255.2/31
                                 10.255.255.2          -       5       0       i Or-ID: 10.255.255.6 C-LST: 10.255.255.3 10.255.255.2 172.16.255.3 10.255.255.4 
 * >Ec    RD: 10.255.255.3:1 ip-prefix 10.0.255.2/31
                                 10.255.255.3          -       5       0       i
 *  ec    RD: 10.255.255.3:1 ip-prefix 10.0.255.2/31
                                 10.255.255.3          -       5       0       i Or-ID: 10.255.255.3 C-LST: 10.255.255.2 10.255.255.3 172.16.255.1 
 * >Ec    RD: 10.255.255.2:1 ip-prefix 10.1.255.0/31
                                 10.255.255.2          -       5       0       i
 *  ec    RD: 10.255.255.2:1 ip-prefix 10.1.255.0/31
                                 10.255.255.2          -       5       0       i Or-ID: 10.255.255.2 C-LST: 10.255.255.3 10.255.255.2 
 * >Ec    RD: 10.255.255.3:1 ip-prefix 10.1.255.0/31
                                 10.255.255.3          -       5       0       i
 *  ec    RD: 10.255.255.3:1 ip-prefix 10.1.255.0/31
                                 10.255.255.3          -       5       0       i Or-ID: 10.255.255.3 C-LST: 10.255.255.2 10.255.255.3 172.16.255.1 
 * >Ec    RD: 10.255.255.2:1 ip-prefix 10.1.255.2/31
                                 10.255.255.2          -       100     0       i
 *  ec    RD: 10.255.255.2:1 ip-prefix 10.1.255.2/31
                                 10.255.255.2          -       100     0       i Or-ID: 10.255.255.2 C-LST: 10.255.255.3 
 * >      RD: 10.255.255.7:1 ip-prefix 10.2.255.0/31
                                 -                     -       -       0       i
 * >Ec    RD: 10.255.255.2:1 ip-prefix 10.2.255.2/31
                                 10.255.255.2          -       5       0       i Or-ID: 10.255.255.8 C-LST: 10.255.255.2 172.16.255.3 10.255.255.4 
 *  ec    RD: 10.255.255.2:1 ip-prefix 10.2.255.2/31
                                 10.255.255.2          -       5       0       i Or-ID: 10.255.255.8 C-LST: 10.255.255.3 10.255.255.2 172.16.255.3 10.255.255.4 
 * >Ec    RD: 10.255.255.3:1 ip-prefix 10.2.255.2/31
                                 10.255.255.3          -       5       0       i
 *  ec    RD: 10.255.255.3:1 ip-prefix 10.2.255.2/31
                                 10.255.255.3          -       5       0       i Or-ID: 10.255.255.3 C-LST: 10.255.255.2 10.255.255.3 172.16.255.1 
 * >Ec    RD: 10.255.255.9:1 ip-prefix 10.4.255.0/31
                                 10.255.255.9          -       100     0       i Or-ID: 10.255.255.9 C-LST: 10.255.255.2 
 *  ec    RD: 10.255.255.9:1 ip-prefix 10.4.255.0/31
                                 10.255.255.9          -       100     0       i Or-ID: 10.255.255.9 C-LST: 10.255.255.3 
 * >Ec    RD: 10.255.255.2:1 ip-prefix 10.4.255.2/31
                                 10.255.255.2          -       5       0       i Or-ID: 10.255.255.10 C-LST: 10.255.255.2 172.16.255.3 10.255.255.4 
 *  ec    RD: 10.255.255.2:1 ip-prefix 10.4.255.2/31
                                 10.255.255.2          -       5       0       i Or-ID: 10.255.255.10 C-LST: 10.255.255.3 10.255.255.2 172.16.255.3 10.255.255.4 
 * >Ec    RD: 10.255.255.3:1 ip-prefix 10.4.255.2/31
                                 10.255.255.3          -       5       0       i
 *  ec    RD: 10.255.255.3:1 ip-prefix 10.4.255.2/31
                                 10.255.255.3          -       5       0       i Or-ID: 10.255.255.3 C-LST: 10.255.255.2 10.255.255.3 172.16.255.1 
 * >Ec    RD: 10.255.255.3:1 ip-prefix 10.5.255.0/31
                                 10.255.255.3          -       100     0       i
 *  ec    RD: 10.255.255.3:1 ip-prefix 10.5.255.0/31
                                 10.255.255.3          -       100     0       i Or-ID: 10.255.255.3 C-LST: 10.255.255.2 
 * >Ec    RD: 10.255.255.2:1 ip-prefix 10.5.255.2/31
                                 10.255.255.2          -       5       0       i
 *  ec    RD: 10.255.255.2:1 ip-prefix 10.5.255.2/31
                                 10.255.255.2          -       5       0       i Or-ID: 10.255.255.2 C-LST: 10.255.255.3 10.255.255.2 172.16.255.3 
 * >Ec    RD: 10.255.255.3:1 ip-prefix 10.5.255.2/31
                                 10.255.255.3          -       5       0       i
 *  ec    RD: 10.255.255.3:1 ip-prefix 10.5.255.2/31
                                 10.255.255.3          -       5       0       i Or-ID: 10.255.255.3 C-LST: 10.255.255.2 10.255.255.3 
 * >Ec    RD: 10.255.255.2:1 ip-prefix 10.6.255.0/31
                                 10.255.255.2          -       5       0       i Or-ID: 10.255.255.11 C-LST: 10.255.255.2 172.16.255.3 10.255.255.4 
 *  ec    RD: 10.255.255.2:1 ip-prefix 10.6.255.0/31
                                 10.255.255.2          -       5       0       i Or-ID: 10.255.255.11 C-LST: 10.255.255.3 10.255.255.2 172.16.255.3 10.255.255.4 
 * >Ec    RD: 10.255.255.3:1 ip-prefix 10.6.255.0/31
                                 10.255.255.3          -       5       0       i
 *  ec    RD: 10.255.255.3:1 ip-prefix 10.6.255.0/31
                                 10.255.255.3          -       5       0       i Or-ID: 10.255.255.3 C-LST: 10.255.255.2 10.255.255.3 172.16.255.1 
 * >Ec    RD: 10.255.255.2:1 ip-prefix 10.6.255.2/31
                                 10.255.255.2          -       5       0       i Or-ID: 10.255.255.12 C-LST: 10.255.255.2 172.16.255.3 10.255.255.4 
 *  ec    RD: 10.255.255.2:1 ip-prefix 10.6.255.2/31
                                 10.255.255.2          -       5       0       i Or-ID: 10.255.255.12 C-LST: 10.255.255.3 10.255.255.2 172.16.255.3 10.255.255.4 
 * >Ec    RD: 10.255.255.3:1 ip-prefix 10.6.255.2/31
                                 10.255.255.3          -       5       0       i
 *  ec    RD: 10.255.255.3:1 ip-prefix 10.6.255.2/31
                                 10.255.255.3          -       5       0       i Or-ID: 10.255.255.3 C-LST: 10.255.255.2 10.255.255.3 172.16.255.1 
 * >Ec    RD: 10.255.255.2:1 ip-prefix 10.255.254.1/32
                                 10.255.255.2          -       5       0       i Or-ID: 10.255.255.5 C-LST: 10.255.255.2 172.16.255.3 10.255.255.4 
 *  ec    RD: 10.255.255.2:1 ip-prefix 10.255.254.1/32
                                 10.255.255.2          -       5       0       i Or-ID: 10.255.255.5 C-LST: 10.255.255.3 10.255.255.2 172.16.255.3 10.255.255.4 
 * >Ec    RD: 10.255.255.3:1 ip-prefix 10.255.254.1/32
                                 10.255.255.3          -       5       0       i
 *  ec    RD: 10.255.255.3:1 ip-prefix 10.255.254.1/32
                                 10.255.255.3          -       5       0       i Or-ID: 10.255.255.3 C-LST: 10.255.255.2 10.255.255.3 172.16.255.1 
 * >Ec    RD: 10.255.255.2:1 ip-prefix 10.255.254.2/32
                                 10.255.255.2          -       100     0       i
 *  ec    RD: 10.255.255.2:1 ip-prefix 10.255.254.2/32
                                 10.255.255.2          -       100     0       i Or-ID: 10.255.255.2 C-LST: 10.255.255.3 
 * >      RD: 10.255.255.3:1 ip-prefix 10.255.254.2/32
                                 10.255.255.3          -       5       0       i
          RD: 10.255.255.2:1 ip-prefix 10.255.254.3/32
                                 PolicyReject          -       -       0       i Or-ID: 10.255.255.8 C-LST: 10.255.255.2 172.16.255.3 10.255.255.4 
          RD: 10.255.255.2:1 ip-prefix 10.255.254.3/32
                                 PolicyReject          -       -       0       i Or-ID: 10.255.255.8 C-LST: 10.255.255.3 10.255.255.2 172.16.255.3 10.255.255.4 
          RD: 10.255.255.3:1 ip-prefix 10.255.254.3/32
                                 PolicyReject          -       -       0       i
          RD: 10.255.255.3:1 ip-prefix 10.255.254.3/32
                                 PolicyReject          -       -       0       i Or-ID: 10.255.255.3 C-LST: 10.255.255.2 10.255.255.3 172.16.255.1 
 * >      RD: 10.255.255.7:1 ip-prefix 10.255.254.3/32
                                 -                     -       -       0       i
 * >Ec    RD: 10.255.255.2:1 ip-prefix 10.255.254.4/32
                                 10.255.255.2          -       5       0       i Or-ID: 10.255.255.12 C-LST: 10.255.255.2 172.16.255.3 10.255.255.4 
 *  ec    RD: 10.255.255.2:1 ip-prefix 10.255.254.4/32
                                 10.255.255.2          -       5       0       i Or-ID: 10.255.255.12 C-LST: 10.255.255.3 10.255.255.2 172.16.255.3 10.255.255.4 
 * >Ec    RD: 10.255.255.3:1 ip-prefix 10.255.254.4/32
                                 10.255.255.3          -       5       0       i
 *  ec    RD: 10.255.255.3:1 ip-prefix 10.255.254.4/32
                                 10.255.255.3          -       5       0       i Or-ID: 10.255.255.3 C-LST: 10.255.255.2 10.255.255.3 172.16.255.1 
 * >Ec    RD: 10.255.255.2:1 ip-prefix 10.255.254.5/32
                                 10.255.255.2          -       5       0       i Or-ID: 10.255.255.10 C-LST: 10.255.255.2 172.16.255.3 10.255.255.4 
 *  ec    RD: 10.255.255.2:1 ip-prefix 10.255.254.5/32
                                 10.255.255.2          -       5       0       i Or-ID: 10.255.255.10 C-LST: 10.255.255.3 10.255.255.2 172.16.255.3 10.255.255.4 
 * >Ec    RD: 10.255.255.3:1 ip-prefix 10.255.254.5/32
                                 10.255.255.3          -       5       0       i
 *  ec    RD: 10.255.255.3:1 ip-prefix 10.255.254.5/32
                                 10.255.255.3          -       5       0       i Or-ID: 10.255.255.3 C-LST: 10.255.255.2 10.255.255.3 172.16.255.1 
 * >Ec    RD: 10.255.255.9:1 ip-prefix 10.255.254.5/32
                                 10.255.255.9          -       100     0       i Or-ID: 10.255.255.9 C-LST: 10.255.255.2 
 *  ec    RD: 10.255.255.9:1 ip-prefix 10.255.254.5/32
                                 10.255.255.9          -       100     0       i Or-ID: 10.255.255.9 C-LST: 10.255.255.3 
 * >      RD: 10.255.255.2:1 ip-prefix 10.255.254.6/32
                                 10.255.255.2          -       5       0       i
 * >Ec    RD: 10.255.255.3:1 ip-prefix 10.255.254.6/32
                                 10.255.255.3          -       100     0       i
 *  ec    RD: 10.255.255.3:1 ip-prefix 10.255.254.6/32
                                 10.255.255.3          -       100     0       i Or-ID: 10.255.255.3 C-LST: 10.255.255.2 
 * >Ec    RD: 10.255.255.2:1 ip-prefix 172.16.255.0/31
                                 10.255.255.2          -       5       0       i
 *  ec    RD: 10.255.255.2:1 ip-prefix 172.16.255.0/31
                                 10.255.255.2          -       5       0       i Or-ID: 10.255.255.2 C-LST: 10.255.255.3 10.255.255.2 172.16.255.3 
 * >Ec    RD: 10.255.255.3:1 ip-prefix 172.16.255.0/31
                                 10.255.255.3          -       100     0       i
 *  ec    RD: 10.255.255.3:1 ip-prefix 172.16.255.0/31
                                 10.255.255.3          -       100     0       i Or-ID: 10.255.255.3 C-LST: 10.255.255.2 
 * >Ec    RD: 10.255.255.2:1 ip-prefix 172.16.255.2/31
                                 10.255.255.2          -       100     0       i
 *  ec    RD: 10.255.255.2:1 ip-prefix 172.16.255.2/31
                                 10.255.255.2          -       100     0       i Or-ID: 10.255.255.2 C-LST: 10.255.255.3 
 * >Ec    RD: 10.255.255.3:1 ip-prefix 172.16.255.2/31
                                 10.255.255.3          -       5       0       i
 *  ec    RD: 10.255.255.3:1 ip-prefix 172.16.255.2/31
                                 10.255.255.3          -       5       0       i Or-ID: 10.255.255.3 C-LST: 10.255.255.2 10.255.255.3 172.16.255.1 
 * >Ec    RD: 10.255.255.2:1 ip-prefix 192.168.0.0/24
                                 10.255.255.2          -       5       0       i Or-ID: 10.255.255.5 C-LST: 10.255.255.2 172.16.255.3 10.255.255.4 
 *  ec    RD: 10.255.255.2:1 ip-prefix 192.168.0.0/24
                                 10.255.255.2          -       5       0       i Or-ID: 10.255.255.5 C-LST: 10.255.255.3 10.255.255.2 172.16.255.3 10.255.255.4 
 * >Ec    RD: 10.255.255.3:1 ip-prefix 192.168.0.0/24
                                 10.255.255.3          -       5       0       i
 *  ec    RD: 10.255.255.3:1 ip-prefix 192.168.0.0/24
                                 10.255.255.3          -       5       0       i Or-ID: 10.255.255.3 C-LST: 10.255.255.2 10.255.255.3 172.16.255.1 
 * >Ec    RD: 10.255.255.2:1 ip-prefix 192.168.1.0/24
                                 10.255.255.2          -       100     0       i
 *  ec    RD: 10.255.255.2:1 ip-prefix 192.168.1.0/24
                                 10.255.255.2          -       100     0       i Or-ID: 10.255.255.2 C-LST: 10.255.255.3 
 * >      RD: 10.255.255.3:1 ip-prefix 192.168.1.0/24
                                 10.255.255.3          -       5       0       i
          RD: 10.255.255.2:1 ip-prefix 192.168.3.0/24
                                 PolicyReject          -       -       0       i Or-ID: 10.255.255.8 C-LST: 10.255.255.2 172.16.255.3 10.255.255.4 
          RD: 10.255.255.2:1 ip-prefix 192.168.3.0/24
                                 PolicyReject          -       -       0       i Or-ID: 10.255.255.8 C-LST: 10.255.255.3 10.255.255.2 172.16.255.3 10.255.255.4 
          RD: 10.255.255.3:1 ip-prefix 192.168.3.0/24
                                 PolicyReject          -       -       0       i
          RD: 10.255.255.3:1 ip-prefix 192.168.3.0/24
                                 PolicyReject          -       -       0       i Or-ID: 10.255.255.3 C-LST: 10.255.255.2 10.255.255.3 172.16.255.1 
 * >      RD: 10.255.255.7:1 ip-prefix 192.168.3.0/24
                                 -                     -       -       0       i
 * >      RD: 10.255.255.2:1 ip-prefix 192.168.5.0/24
                                 10.255.255.2          -       5       0       i
 * >Ec    RD: 10.255.255.3:1 ip-prefix 192.168.5.0/24
                                 10.255.255.3          -       100     0       i
 *  ec    RD: 10.255.255.3:1 ip-prefix 192.168.5.0/24
                                 10.255.255.3          -       100     0       i Or-ID: 10.255.255.3 C-LST: 10.255.255.2 
 * >Ec    RD: 10.255.255.2:1 ip-prefix 192.168.6.0/24
                                 10.255.255.2          -       5       0       i Or-ID: 10.255.255.12 C-LST: 10.255.255.2 172.16.255.3 10.255.255.4 
 *  ec    RD: 10.255.255.2:1 ip-prefix 192.168.6.0/24
                                 10.255.255.2          -       5       0       i Or-ID: 10.255.255.12 C-LST: 10.255.255.3 10.255.255.2 172.16.255.3 10.255.255.4 
 * >Ec    RD: 10.255.255.3:1 ip-prefix 192.168.6.0/24
                                 10.255.255.3          -       5       0       i
 *  ec    RD: 10.255.255.3:1 ip-prefix 192.168.6.0/24
                                 10.255.255.3          -       5       0       i Or-ID: 10.255.255.3 C-LST: 10.255.255.2 10.255.255.3 172.16.255.1 
 * >Ec    RD: 10.255.255.2:1 ip-prefix 192.168.40.0/24
                                 10.255.255.2          -       5       0       i Or-ID: 10.255.255.10 C-LST: 10.255.255.2 172.16.255.3 10.255.255.4 
 *  ec    RD: 10.255.255.2:1 ip-prefix 192.168.40.0/24
                                 10.255.255.2          -       5       0       i Or-ID: 10.255.255.10 C-LST: 10.255.255.3 10.255.255.2 172.16.255.3 10.255.255.4 
 * >Ec    RD: 10.255.255.3:1 ip-prefix 192.168.40.0/24
                                 10.255.255.3          -       5       0       i
 *  ec    RD: 10.255.255.3:1 ip-prefix 192.168.40.0/24
                                 10.255.255.3          -       5       0       i Or-ID: 10.255.255.3 C-LST: 10.255.255.2 10.255.255.3 172.16.255.1 
 * >Ec    RD: 10.255.255.9:1 ip-prefix 192.168.40.0/24
                                 10.255.255.9          -       100     0       i Or-ID: 10.255.255.9 C-LST: 10.255.255.2 
 *  ec    RD: 10.255.255.9:1 ip-prefix 192.168.40.0/24
                                 10.255.255.9          -       100     0       i Or-ID: 10.255.255.9 C-LST: 10.255.255.3 
```

## show ip security connection detail

```text
path1:
  Source address: 172.16.2.2, Destination address: 172.16.2.0
  State: established
  Uptime: 15 hours, 56 minutes, 41 seconds
  VRF: default
  Type: static
  Remote IP: 10.255.255.9
  Role: initiator
  Inbound SPI: 0xcc1c91:
    Request ID: 8, Mode: transport, Replay window size: 16384, Seq: 0x0
    Errors:
      Packets outside replay window: 0, Replay: 0, Integrity failed: 0
    Lifetime config:
      Soft byte limit: 4439635892249, Hard byte limit: 6442450944000
      Soft packet limit: 2987910067, Hard packet limit: 4000000000
      Soft time limit: 2612 secs, Hard time limit: 3600 secs
    Lifetime current:
      Current bytes: 1833552
      Current packets: 5916
      SA add time: Fri Mar 15 08:13:50 2024
      SA last use time: Fri Mar 15 08:43:07 2024
  Outbound SPI: 0xcad2a8:
    Request ID: 8, Mode: transport, Replay window size: 0, Seq: 0x0
    Errors:
      Packets outside replay window: 0, Replay: 0, Integrity failed: 0
    Lifetime config:
      Soft byte limit: 3542194802249, Hard byte limit: 6442450944000
      Soft packet limit: 2074601913, Hard packet limit: 4000000000
      Soft time limit: 2823 secs, Hard time limit: 3600 secs
    Lifetime current:
      Current bytes: 2798435
      Current packets: 6083
      SA add time: Fri Mar 15 08:13:50 2024
      SA last use time: -
path3:
  Source address: 172.16.2.2, Destination address: 172.16.2.5
  State: established
  Uptime: 15 hours, 56 minutes, 41 seconds
  VRF: default
  Type: static
  Remote IP: 10.255.255.9
  Role: initiator
  Inbound SPI: 0xc8bce1:
    Request ID: 7, Mode: transport, Replay window size: 16384, Seq: 0x0
    Errors:
      Packets outside replay window: 0, Replay: 0, Integrity failed: 0
    Lifetime config:
      Soft byte limit: 3464535630749, Hard byte limit: 6442450944000
      Soft packet limit: 2521179225, Hard packet limit: 4000000000
      Soft time limit: 2582 secs, Hard time limit: 3600 secs
    Lifetime current:
      Current bytes: 1564204
      Current packets: 5243
      SA add time: Fri Mar 15 08:17:02 2024
      SA last use time: Fri Mar 15 08:43:08 2024
  Outbound SPI: 0xca7c08:
    Request ID: 7, Mode: transport, Replay window size: 0, Seq: 0x0
    Errors:
      Packets outside replay window: 0, Replay: 0, Integrity failed: 0
    Lifetime config:
      Soft byte limit: 3684061693499, Hard byte limit: 6442450944000
      Soft packet limit: 2183762480, Hard packet limit: 4000000000
      Soft time limit: 2896 secs, Hard time limit: 3600 secs
    Lifetime current:
      Current bytes: 2353165
      Current packets: 5394
      SA add time: Fri Mar 15 08:17:02 2024
      SA last use time: -
path4:
  Source address: 172.16.2.2, Destination address: 172.16.2.7
  State: established
  Uptime: 15 hours, 56 minutes, 38 seconds
  VRF: default
  Type: dynamic
  Remote IP: 10.255.255.9
  Role: initiator
  Packets in: 189344533, Packets out: 75937645
  Last known rekey count: 2
  Dynamic state: established
  Last established time: Fri Mar 15 08:20:36 2024
  DH crypto:
    Local rekey: 1, Peer rekey: 1, In SPI: 0xda5a26c2, Out SPI: 0xbc846cba
    Local rekey: 2, Peer rekey: 2, In SPI: 0x9b1a74c8, Out SPI: 0x5aa5b922
    Local rekey: 1, Peer rekey: 0, In SPI: 0x9bfffd1f, Out SPI: 0x9800b9b4
    Local rekey: 1, Peer rekey: 2, In SPI: 0xbf3610af, Out SPI: 0xd3dcfa4a
    Local rekey: 2, Peer rekey: 1, In SPI: 0xa871ac12, Out SPI: 0x7621bec9
  DH state:
    Local rekey: 2, Peer rekey: 2, DH rekey state: not rekeying, Role: not rekeying
  SA crypto:
    Local rekey: 2, Peer rekey: 2, In SPI 0x3fee3575, Out SPI 0x3c04ec87
  SA rekey role: not rekeying
  SA state:
    SA type: ingress , SPI: 0x45080ce0
      Role: initiator, SA rekey state: initial, Peer nonce type: init
      Add time: Fri Mar 15 08:18:49 2024, Packets: 3094, Pair SPI: 0x48f255cd
    SA type: egress , SPI: 0x48f255cd
      Role: initiator, SA rekey state: initial, Peer nonce type: init
      Add time: Fri Mar 15 08:18:58 2024, Packets: 3212, Pair SPI: 0x45080ce0
  Inbound SPI: 0x45080ce0:
    Request ID: 9, Mode: transport, Replay window size: 0, Seq: 0x0
    Errors:
      Packets outside replay window: 0, Replay: 0, Integrity failed: 0
    Lifetime config:
      Soft byte limit: 4809444144150, Hard byte limit: 6442450944000
      Soft packet limit: 2994826523, Hard packet limit: 4000000000
      Soft time limit: 2612 secs, Hard time limit: 3600 secs
    Lifetime current:
      Current bytes: 1251120
      Current packets: 3100
      SA add time: Fri Mar 15 08:18:49 2024
      SA last use time: Fri Mar 15 08:43:08 2024
  Outbound SPI: 0x48f255cd:
    Request ID: 9, Mode: transport, Replay window size: 0, Seq: 0x0
    Errors:
      Packets outside replay window: 0, Replay: 0, Integrity failed: 0
    Lifetime config:
      Soft byte limit: 4735456659900, Hard byte limit: 6442450944000
      Soft packet limit: 2943331024, Hard packet limit: 4000000000
      Soft time limit: 2539 secs, Hard time limit: 3600 secs
    Lifetime current:
      Current bytes: 1042752
      Current packets: 3218
      SA add time: Fri Mar 15 08:18:58 2024
      SA last use time: -
```

## show stun client translations detail

```text
Current System Time: Fri Mar 15 08:43:08 2024
Transaction ID 000000010affff0700000000
Agent Name: dps
Source Address: 172.16.2.2:4500
Public Address: 172.16.2.2:4500
Number of Attributes: 3
Timeout Interval: 0:00:10
Last Refreshed: 0:00:01 ago
Attribute Type   Length Value           
---------------- ------ ----------------
PATH_GROUP            3 ATT             
VTEP_IP               4 10.255.255.7    
WAN_ID                4 1               

```

## show stun server bindings detail

```text
Current System Time: Fri Mar 15 08:43:09 2024
```

## show path-selection paths detail

```text
Peer: 10.255.255.2, Path group ATT
Path name: path1, static, Label: 1
Source: 172.16.2.2, Port: 4500, WAN ID: 1
Destination: 172.16.2.0, Port: 4500, WAN ID: 2886730240
Local interface: Ethernet1/7
Route state: IPsec established
Traffic class 0: active (15:56:09)
MTU: 8914

Peer: 10.255.255.3, Path group ATT
Path name: path3, static, Label: 3
Source: 172.16.2.2, Port: 4500, WAN ID: 1
Destination: 172.16.2.5, Port: 4500, WAN ID: 2886730245
Local interface: Ethernet1/7
Route state: IPsec established
Traffic class 0: active (0:12:12)
MTU: 8914

Peer: 10.255.255.9, Path group ATT
Path name: path4, dynamic, Label: 4
Source: 172.16.2.2, Port: 4500, WAN ID: 1
Destination: 172.16.2.7, Port: 4500, WAN ID: 2
Local interface: Ethernet1/7
Route state: IPsec established
Traffic class 0: active (15:56:05)
MTU: 1424

```

## show bgp neighbors

```text
BGP neighbor is 10.255.255.2, remote AS 65000, internal link
  BGP version 4, remote router ID 10.255.255.2, VRF default
  Inherits configuration from and member of peer-group PATHFINDER
  Last read 00:00:10, last write 00:00:44
  Hold time is 180, keepalive interval is 60 seconds
  Configured hold time is 180, keepalive interval is 60 seconds
  Effective minimum hold time is 3 seconds
  Send failure hold time is 0 seconds
  Hold timer is active, time left: 00:02:50
  Keepalive timer is active, time left: 00:00:14
  Connect timer is inactive
  Idle-restart timer is inactive
  BGP state is Established, up for 00:12:31
  Number of transitions to established: 5
  Last state was OpenConfirm
  Last event was RecvUpdate
  Last sent notification:Cease/BFD down, Last time 00:12:42, First time 16:01:39, Repeats 2
  Last rcvd notification:Cease/BFD down, Last time 00:12:54
  Last sent socket-error:Connect (Network is unreachable), Last time 19:24:54
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
      Received 00:12:30
      Number of stale paths removed after graceful restart: 0
      Number of paths received before End-of-RIB: 1
    L2VPN EVPN End-of-RIB received: Yes
      Received 00:12:30
      Number of stale paths removed after graceful restart: 0
      Number of paths received before End-of-RIB: 5
  AIGP attribute send and receive for IPv4 Unicast are enabled
  AIGP attribute send and receive for IPv4 with MPLS Labels are enabled
  AIGP attribute send and receive for IPv6 Unicast are enabled
  AIGP attribute send and receive for IPv6 with MPLS Labels are enabled
  BGP session driven failover for IPv6 Unicast is disabled
  BGP session driven failover for IPv4 Unicast is disabled
  Message Statistics:
                                  Sent      Rcvd
    Opens:                           5         5
    Notifications:                   3         1
    Updates:                        49     33459
    Keepalives:                   1369      1348
    Enhanced Route Refresh:          0         0
    Begin of Route Refresh:          0         0
    End of Route Refresh:            0         0
    Total messages:               1426     34813
  Prefix Statistics:
                                   Sent      Rcvd     Best Paths     Best ECMP Paths
    IPv4 Unicast:                     0         0              0                   0
    IPv4 Dps:                         2         6              6                   3
    IPv6 Unicast:                     0         0              0                   0
    EVPN:                             3        47             43                  22
  Configured maximum total number of routes is 12000
  Inbound updates dropped by reason:
    AS path loop detection: 0
    Cluster ID loop detection: 0
    Enforced First AS: 0
    Malformed MPBGP routes: 0
    Originator ID matches local router ID: 6
    Nexthop matches local IP address: 2
    Unexpected IPv6 nexthop for IPv4 routes: 0
  Inbound updates with attribute errors:
    Resulting in removal of all paths in update (treat as withdraw): 2
    Resulting in AFI/SAFI disable: 0
    Resulting in attribute ignore: 0
    Disabled AFI/SAFIs: None
    Last treat-as-withdraw attribute error: Nexthop is local address
    Last update with error received at: 00:12:30
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
Local AS is 65000, local router ID 10.255.255.7
TTL is 255
Local TCP address is 10.255.255.7, local port is 46841
Remote TCP address is 10.255.255.2, remote port is 179
Local next hop for next hop self:
  Dps: 10.255.255.7
  L2VPN EVPN: 10.255.255.7
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
    Retransmission Timeout (rto): 8684.0ms
    Round-trip Time (rtt/rtvar): 691.5ms/1311.9ms
    Delayed Ack Timeout (ato): 40.0ms
    Congestion Window (cwnd): 10
    TCP Throughput: 0.17 Mbps
    Recv Round-trip Time (rcv_rtt): 2.0ms
    Advertised Recv Window (rcv_space): 14480

BGP neighbor is 10.255.255.3, remote AS 65000, internal link
  BGP version 4, remote router ID 10.255.255.3, VRF default
  Inherits configuration from and member of peer-group PATHFINDER
  Last read 00:00:14, last write 00:00:32
  Hold time is 180, keepalive interval is 60 seconds
  Configured hold time is 180, keepalive interval is 60 seconds
  Effective minimum hold time is 3 seconds
  Send failure hold time is 0 seconds
  Hold timer is active, time left: 00:02:46
  Keepalive timer is active, time left: 00:00:14
  Connect timer is inactive
  Idle-restart timer is inactive
  BGP state is Established, up for 00:12:07
  Number of transitions to established: 6
  Last state was OpenConfirm
  Last event was RecvUpdate
  Last sent notification:Cease/BFD down, Last time 15:59:23, First time 16:01:39, Repeats 1
  Last rcvd notification:Cease/BFD down, Last time 00:12:15
  Last sent socket-error:Connect (Network is unreachable), Last time 19:24:54
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
      Received 00:12:06
      Number of stale paths removed after graceful restart: 0
      Number of paths received before End-of-RIB: 6
    L2VPN EVPN End-of-RIB received: Yes
      Received 00:12:06
      Number of stale paths removed after graceful restart: 0
      Number of paths received before End-of-RIB: 27
  AIGP attribute send and receive for IPv4 Unicast are enabled
  AIGP attribute send and receive for IPv4 with MPLS Labels are enabled
  AIGP attribute send and receive for IPv6 Unicast are enabled
  AIGP attribute send and receive for IPv6 with MPLS Labels are enabled
  BGP session driven failover for IPv6 Unicast is disabled
  BGP session driven failover for IPv4 Unicast is disabled
  Message Statistics:
                                  Sent      Rcvd
    Opens:                           6         6
    Notifications:                   2         3
    Updates:                        48     21406
    Keepalives:                   1369      1346
    Enhanced Route Refresh:          0         0
    Begin of Route Refresh:          0         0
    End of Route Refresh:            0         0
    Total messages:               1425     22761
  Prefix Statistics:
                                   Sent      Rcvd     Best Paths     Best ECMP Paths
    IPv4 Unicast:                     0         0              0                   0
    IPv4 Dps:                         2         6              6                   1
    IPv6 Unicast:                     0         0              0                   0
    EVPN:                             3        47             43                  19
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
    Last update with error received at: 00:12:06
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
Local AS is 65000, local router ID 10.255.255.7
TTL is 255
Local TCP address is 10.255.255.7, local port is 46809
Remote TCP address is 10.255.255.3, remote port is 179
Local next hop for next hop self:
  Dps: 10.255.255.7
  L2VPN EVPN: 10.255.255.7
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
    Retransmission Timeout (rto): 204.0ms
    Round-trip Time (rtt/rtvar): 3.7ms/3.2ms
    Delayed Ack Timeout (ato): 40.0ms
    Congestion Window (cwnd): 2
    TCP Throughput: 6.24 Mbps
    Recv Round-trip Time (rcv_rtt): 955.0ms
    Advertised Recv Window (rcv_space): 14480

```

## show bgp path-selection detail

```text
BGP routing table information for VRF default
Router identifier 10.255.255.7, local AS number 65000
Bgp routing table entry for ipv4Dps VTEP 10.255.255.7/32
 Paths: 1 available
  Local
    - from - (0.0.0.0)
      Origin IGP, metric -, localpref -, weight 0, received 15:57:40 ago, valid, local
      Tunnel encapsulation attribute: Dynamic path selection
        Endpoint: 172.16.2.2, Path group name: ATT, WAN ID: 1, UDP port: 4500
Bgp routing table entry for ipv4Dps VTEP 10.255.255.9/32
 Paths: 4 available
  Local
    :: from 10.255.255.2 (10.255.255.2)
      Origin IGP, metric -, localpref 100, weight 0, received 00:12:30 ago, valid, internal
      Tunnel encapsulation attribute: Dynamic path selection
        Endpoint: 172.16.2.7, Path group name: ATT, WAN ID: 2, UDP port: 4500
  Local
    :: from 10.255.255.3 (10.255.255.3)
      Origin IGP, metric -, localpref 100, weight 0, received 00:12:07 ago, valid, internal
      Tunnel encapsulation attribute: Dynamic path selection
        Endpoint: 172.16.2.7, Path group name: ATT, WAN ID: 2, UDP port: 4500
  Local
    :: from 10.255.255.3 (10.255.255.3)
      Origin IGP, metric -, localpref 100, weight 0, received 00:12:07 ago, valid, internal
      Tunnel encapsulation attribute: Dynamic path selection
        Endpoint: 172.16.2.7, Path group name: ATT, WAN ID: 2, UDP port: 4500
  Local
    :: from 10.255.255.2 (10.255.255.2)
      Origin IGP, metric -, localpref 100, weight 0, received 00:12:07 ago, valid, internal
      Tunnel encapsulation attribute: Dynamic path selection
        Endpoint: 172.16.2.7, Path group name: ATT, WAN ID: 2, UDP port: 4500
Bgp routing table entry for ipv4Ipsec VTEP 10.255.255.2/32
 Paths: 2 available
  Local
    :: from 10.255.255.2 (10.255.255.2)
      Origin IGP, metric -, localpref 100, weight 0, received 00:12:31 ago, valid, internal
      Tunnel encapsulation attribute: IP security
        Initial contact: false, Rekey counter: 0, Nonce length: 32
        DH group: 14, DH key length: 256
        Encryption algo: aes256, Authentication algo: sha256
  Local
    :: from 10.255.255.3 (10.255.255.3)
      Origin IGP, metric -, localpref 100, weight 0, received 00:12:07 ago, valid, internal
      Tunnel encapsulation attribute: IP security
        Initial contact: false, Rekey counter: 0, Nonce length: 32
        DH group: 14, DH key length: 256
        Encryption algo: aes256, Authentication algo: sha256
Bgp routing table entry for ipv4Ipsec VTEP 10.255.255.3/32
 Paths: 2 available
  Local
    :: from 10.255.255.3 (10.255.255.3)
      Origin IGP, metric -, localpref 100, weight 0, received 00:12:07 ago, valid, internal
      Tunnel encapsulation attribute: IP security
        Initial contact: false, Rekey counter: 0, Nonce length: 32
        DH group: 14, DH key length: 256
        Encryption algo: aes256, Authentication algo: sha256
  Local
    :: from 10.255.255.2 (10.255.255.2)
      Origin IGP, metric -, localpref 100, weight 0, received 00:12:07 ago, valid, internal
      Tunnel encapsulation attribute: IP security
        Initial contact: false, Rekey counter: 0, Nonce length: 32
        DH group: 14, DH key length: 256
        Encryption algo: aes256, Authentication algo: sha256
Bgp routing table entry for ipv4Ipsec VTEP 10.255.255.7/32
 Paths: 1 available
  Local
    - from - (0.0.0.0)
      Origin IGP, metric -, localpref -, weight 0, received 19:24:34 ago, valid, local
      Tunnel encapsulation attribute: IP security
        Initial contact: false, Rekey counter: 2, Nonce length: 32
        DH group: 14, DH key length: 256
        Encryption algo: aes256, Authentication algo: sha256
Bgp routing table entry for ipv4Ipsec VTEP 10.255.255.9/32
 Paths: 4 available
  Local
    :: from 10.255.255.2 (10.255.255.2)
      Origin IGP, metric -, localpref 100, weight 0, received 00:12:30 ago, valid, internal
      Tunnel encapsulation attribute: IP security
        Initial contact: false, Rekey counter: 2, Nonce length: 32
        DH group: 14, DH key length: 256
        Encryption algo: aes256, Authentication algo: sha256
  Local
    :: from 10.255.255.3 (10.255.255.3)
      Origin IGP, metric -, localpref 100, weight 0, received 00:12:07 ago, valid, internal
      Tunnel encapsulation attribute: IP security
        Initial contact: false, Rekey counter: 2, Nonce length: 32
        DH group: 14, DH key length: 256
        Encryption algo: aes256, Authentication algo: sha256
  Local
    :: from 10.255.255.3 (10.255.255.3)
      Origin IGP, metric -, localpref 100, weight 0, received 00:12:07 ago, valid, internal
      Tunnel encapsulation attribute: IP security
        Initial contact: false, Rekey counter: 2, Nonce length: 32
        DH group: 14, DH key length: 256
        Encryption algo: aes256, Authentication algo: sha256
  Local
    :: from 10.255.255.2 (10.255.255.2)
      Origin IGP, metric -, localpref 100, weight 0, received 00:12:07 ago, valid, internal
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
>C    10.255.255.7/32 [0 pref/0 metric] updated 19:25:15 ago
         via Loopback0, directly connected
>C    172.16.2.2/31 [0 pref/0 metric] updated 15:57:50 ago
         via Ethernet1/7, directly connected
>C    172.28.128.0/20 [0 pref/0 metric] updated 19:24:55 ago
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
>S    10.80.0.0/12 [1 pref/0 metric] updated 19:24:55 ago
         via 172.28.128.1 [0 pref/0 metric] type ipv4
            via 172.28.128.1, Management1/1
>S    10.224.0.0/12 [1 pref/0 metric] updated 19:24:55 ago
         via 172.28.128.1 [0 pref/0 metric] type ipv4
            via 172.28.128.1, Management1/1
>S    10.240.0.0/12 [1 pref/0 metric] updated 19:24:55 ago
         via 172.28.128.1 [0 pref/0 metric] type ipv4
            via 172.28.128.1, Management1/1
>S    172.16.0.0/12 [1 pref/0 metric] updated 19:24:55 ago
         via 172.28.128.1 [0 pref/0 metric] type ipv4
            via 172.28.128.1, Management1/1
>S    172.16.2.0/24 [1 pref/0 metric] updated 15:57:50 ago
         via 172.16.2.3 [0 pref/0 metric] type ipv4
            via 172.16.2.3, Ethernet1/7
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
>P    0.0.0.0/8 [1 pref/0 metric] updated 19:25:13 ago
         via Null0, directly connected [NF]
>P    10.255.255.2/32 [1 pref/0 metric] updated 19:24:34 ago
         via 10.255.255.2, Dps1
>P    10.255.255.3/32 [1 pref/0 metric] updated 19:24:34 ago
         via 10.255.255.3, Dps1
>P    10.255.255.9/32 [1 pref/0 metric] updated 15:56:42 ago
         via 10.255.255.9, Dps1
>P    127.0.0.0/8 [1 pref/0 metric] updated 19:25:13 ago
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
>P    ::/96 [1 pref/0 metric] updated 19:24:37 ago
         via Null0, directly connected [NF]
>P    ::ffff:127.0.0.0/104 [1 pref/0 metric] updated 19:24:37 ago
         via :: [1 pref/1 metric] type ipv6
            via , directly connected
>P    fe80::/10 [1 pref/0 metric] updated 19:24:37 ago
```

## show platform sfe worker summary

```text
 WorkerId Busy       PPS
 -------- ---- ---------
        0    0         6
        1    0         1
        2    0         0
        3    0         9
        4    0         2
        5    0         0

```
