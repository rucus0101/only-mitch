# Test results for VM3

## show version

```text
Arista vEOS
Hardware version: 
Serial number: A1952AD30012E93842BDFC8D2EA2E370
Hardware MAC address: 0050.5647.de91
System MAC address: 0050.5647.de91

Software image version: 4.31.2F-cloud
Architecture: i686
Internal build version: 4.31.2F-cloud-35442146.4312F
Internal build ID: 635a071a-386e-447f-942c-bcc34d9ffd3c
Image format version: 1.0
Image optimization: None

Uptime: 19 minutes
Total memory: 16264236 kB
Free memory: 10453696 kB

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
Interface       IP Address            Status     Protocol         MTU   Owner  
--------------- --------------------- ---------- ------------ --------- -------
Ethernet1       172.16.2.7/31         up         up              9000          
Ethernet2       10.4.255.0/31         up         up              1500          
Loopback0       10.255.255.9/32       up         up             65535          
Management1     172.28.138.242/20     up         up              1500          

```

## show interfaces counters rates | nz

```text
Port      Name      Intvl  In Mbps      %  In Kpps Out Mbps      % Out Kpps
Et1       ATT        0:01      0.0   0.0%        0     84.7   0.9%        9
Et2                  0:01     78.5   0.8%        9      0.0   0.0%        0
Ma1                  0:01      0.0   0.0%        0      0.1   0.0%        0
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
           via 172.16.2.6, Ethernet1

 S        10.255.255.2/32
           directly connected, Dps1
 S        10.255.255.3/32
           directly connected, Dps1
 S        10.255.255.7/32
           directly connected, Dps1
 C        10.255.255.9/32
           directly connected, Loopback0
 C        172.16.2.6/31
           directly connected, Ethernet1

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
           via 172.16.2.6, Ethernet1

 S        10.255.255.2/32
           directly connected, Dps1
 S        10.255.255.3/32
           directly connected, Dps1
 S        10.255.255.7/32
           directly connected, Dps1
 C        10.255.255.9/32
           directly connected, Loopback0
 C        172.16.2.6/31
           directly connected, Ethernet1


VRF: MGMT
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
           via 172.28.128.1, Management1

 C        172.28.128.0/20
           directly connected, Management1


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
 B I      10.2.255.0/31 [20/0]
           via VTEP 10.255.255.7 VNI 201 router-mac ec:8a:48:04:2b:da
 B I      10.2.255.2/31 [20/0]
           via VTEP 10.255.255.2 VNI 201 router-mac ec:8a:48:04:f5:69
           via VTEP 10.255.255.3 VNI 201 router-mac ec:8a:48:04:ff:6e
 C        10.4.255.0/31
           directly connected, Ethernet2
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
 B I      10.255.254.3/32 [20/0]
           via VTEP 10.255.255.7 VNI 201 router-mac ec:8a:48:04:2b:da
 B I      10.255.254.4/32 [20/0]
           via VTEP 10.255.255.2 VNI 201 router-mac ec:8a:48:04:f5:69
           via VTEP 10.255.255.3 VNI 201 router-mac ec:8a:48:04:ff:6e
 B I      10.255.254.5/32 [20/0]
           via VTEP 10.255.255.2 VNI 201 router-mac ec:8a:48:04:f5:69
           via VTEP 10.255.255.3 VNI 201 router-mac ec:8a:48:04:ff:6e
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
 B I      192.168.3.0/24 [20/0]
           via VTEP 10.255.255.7 VNI 201 router-mac ec:8a:48:04:2b:da
 B I      192.168.5.0/24 [20/0]
           via VTEP 10.255.255.3 VNI 201 router-mac ec:8a:48:04:ff:6e
 B I      192.168.6.0/24 [20/0]
           via VTEP 10.255.255.2 VNI 201 router-mac ec:8a:48:04:f5:69
           via VTEP 10.255.255.3 VNI 201 router-mac ec:8a:48:04:ff:6e
 B I      192.168.40.0/24 [20/0]
           via VTEP 10.255.255.2 VNI 201 router-mac ec:8a:48:04:f5:69
           via VTEP 10.255.255.3 VNI 201 router-mac ec:8a:48:04:ff:6e

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
Router identifier 10.255.255.9, local AS number 65000
Route status codes: * - valid, > - active, S - Stale, E - ECMP head, e - ECMP
                    c - Contributing to ECMP, % - Pending best path selection
Origin codes: i - IGP, e - EGP, ? - incomplete
AS Path Attributes: Or-ID - Originator ID, C-LST - Cluster List, LL Nexthop - Link Local Nexthop

          Network                Next Hop              Metric  LocPref Weight  Path
 * >Ec    RD: 10.255.255.2:1 ip-prefix 10.0.255.0/31
                                 10.255.255.2          -       5       0       i
 *  ec    RD: 10.255.255.2:1 ip-prefix 10.0.255.0/31
                                 10.255.255.2          -       5       0       i Or-ID: 10.255.255.2 C-LST: 10.255.255.3 10.255.255.2 172.16.255.3 
 * >Ec    RD: 10.255.255.3:1 ip-prefix 10.0.255.0/31
                                 10.255.255.3          -       5       0       i Or-ID: 10.255.255.5 C-LST: 10.255.255.3 10.5.255.2 10.255.255.1 
 *  ec    RD: 10.255.255.3:1 ip-prefix 10.0.255.0/31
                                 10.255.255.3          -       5       0       i Or-ID: 10.255.255.5 C-LST: 10.255.255.2 10.255.255.3 10.5.255.2 10.255.255.1 
 * >Ec    RD: 10.255.255.2:1 ip-prefix 10.0.255.2/31
                                 10.255.255.2          -       5       0       i
 *  ec    RD: 10.255.255.2:1 ip-prefix 10.0.255.2/31
                                 10.255.255.2          -       5       0       i Or-ID: 10.255.255.2 C-LST: 10.255.255.3 10.255.255.2 172.16.255.3 
 * >Ec    RD: 10.255.255.3:1 ip-prefix 10.0.255.2/31
                                 10.255.255.3          -       5       0       i Or-ID: 10.255.255.6 C-LST: 10.255.255.3 10.5.255.2 10.255.255.1 
 *  ec    RD: 10.255.255.3:1 ip-prefix 10.0.255.2/31
                                 10.255.255.3          -       5       0       i Or-ID: 10.255.255.6 C-LST: 10.255.255.2 10.255.255.3 10.5.255.2 10.255.255.1 
 * >Ec    RD: 10.255.255.2:1 ip-prefix 10.1.255.0/31
                                 10.255.255.2          -       5       0       i
 *  ec    RD: 10.255.255.2:1 ip-prefix 10.1.255.0/31
                                 10.255.255.2          -       5       0       i Or-ID: 10.255.255.2 C-LST: 10.255.255.3 10.255.255.2 
 * >Ec    RD: 10.255.255.3:1 ip-prefix 10.1.255.0/31
                                 10.255.255.3          -       5       0       i
 *  ec    RD: 10.255.255.3:1 ip-prefix 10.1.255.0/31
                                 10.255.255.3          -       5       0       i Or-ID: 10.255.255.3 C-LST: 10.255.255.2 10.255.255.3 10.5.255.2 
 * >Ec    RD: 10.255.255.2:1 ip-prefix 10.1.255.2/31
                                 10.255.255.2          -       100     0       i
 *  ec    RD: 10.255.255.2:1 ip-prefix 10.1.255.2/31
                                 10.255.255.2          -       100     0       i Or-ID: 10.255.255.2 C-LST: 10.255.255.3 
 * >Ec    RD: 10.255.255.7:1 ip-prefix 10.2.255.0/31
                                 10.255.255.7          -       100     0       i Or-ID: 10.255.255.7 C-LST: 10.255.255.2 
 *  ec    RD: 10.255.255.7:1 ip-prefix 10.2.255.0/31
                                 10.255.255.7          -       100     0       i Or-ID: 10.255.255.7 C-LST: 10.255.255.3 
 * >Ec    RD: 10.255.255.2:1 ip-prefix 10.2.255.2/31
                                 10.255.255.2          -       5       0       i
 *  ec    RD: 10.255.255.2:1 ip-prefix 10.2.255.2/31
                                 10.255.255.2          -       5       0       i Or-ID: 10.255.255.2 C-LST: 10.255.255.3 10.255.255.2 172.16.255.3 
 * >Ec    RD: 10.255.255.3:1 ip-prefix 10.2.255.2/31
                                 10.255.255.3          -       5       0       i Or-ID: 10.255.255.8 C-LST: 10.255.255.3 10.5.255.2 10.255.255.1 
 *  ec    RD: 10.255.255.3:1 ip-prefix 10.2.255.2/31
                                 10.255.255.3          -       5       0       i Or-ID: 10.255.255.8 C-LST: 10.255.255.2 10.255.255.3 10.5.255.2 10.255.255.1 
 * >      RD: 10.255.255.9:1 ip-prefix 10.4.255.0/31
                                 -                     -       -       0       i
 * >Ec    RD: 10.255.255.2:1 ip-prefix 10.4.255.2/31
                                 10.255.255.2          -       5       0       i
 *  ec    RD: 10.255.255.2:1 ip-prefix 10.4.255.2/31
                                 10.255.255.2          -       5       0       i Or-ID: 10.255.255.2 C-LST: 10.255.255.3 10.255.255.2 172.16.255.3 
 * >Ec    RD: 10.255.255.3:1 ip-prefix 10.4.255.2/31
                                 10.255.255.3          -       5       0       i Or-ID: 10.255.255.10 C-LST: 10.255.255.3 10.5.255.2 10.255.255.1 
 *  ec    RD: 10.255.255.3:1 ip-prefix 10.4.255.2/31
                                 10.255.255.3          -       5       0       i Or-ID: 10.255.255.10 C-LST: 10.255.255.2 10.255.255.3 10.5.255.2 10.255.255.1 
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
                                 10.255.255.2          -       5       0       i
 *  ec    RD: 10.255.255.2:1 ip-prefix 10.6.255.0/31
                                 10.255.255.2          -       5       0       i Or-ID: 10.255.255.2 C-LST: 10.255.255.3 10.255.255.2 172.16.255.3 
 * >Ec    RD: 10.255.255.3:1 ip-prefix 10.6.255.0/31
                                 10.255.255.3          -       5       0       i Or-ID: 10.255.255.11 C-LST: 10.255.255.3 10.5.255.2 10.255.255.1 
 *  ec    RD: 10.255.255.3:1 ip-prefix 10.6.255.0/31
                                 10.255.255.3          -       5       0       i Or-ID: 10.255.255.11 C-LST: 10.255.255.2 10.255.255.3 10.5.255.2 10.255.255.1 
 * >Ec    RD: 10.255.255.2:1 ip-prefix 10.6.255.2/31
                                 10.255.255.2          -       5       0       i
 *  ec    RD: 10.255.255.2:1 ip-prefix 10.6.255.2/31
                                 10.255.255.2          -       5       0       i Or-ID: 10.255.255.2 C-LST: 10.255.255.3 10.255.255.2 172.16.255.3 
 * >Ec    RD: 10.255.255.3:1 ip-prefix 10.6.255.2/31
                                 10.255.255.3          -       5       0       i Or-ID: 10.255.255.12 C-LST: 10.255.255.3 10.5.255.2 10.255.255.1 
 *  ec    RD: 10.255.255.3:1 ip-prefix 10.6.255.2/31
                                 10.255.255.3          -       5       0       i Or-ID: 10.255.255.12 C-LST: 10.255.255.2 10.255.255.3 10.5.255.2 10.255.255.1 
 * >Ec    RD: 10.255.255.2:1 ip-prefix 10.255.254.1/32
                                 10.255.255.2          -       5       0       i
 *  ec    RD: 10.255.255.2:1 ip-prefix 10.255.254.1/32
                                 10.255.255.2          -       5       0       i Or-ID: 10.255.255.2 C-LST: 10.255.255.3 10.255.255.2 172.16.255.3 
 * >Ec    RD: 10.255.255.3:1 ip-prefix 10.255.254.1/32
                                 10.255.255.3          -       5       0       i
 *  ec    RD: 10.255.255.3:1 ip-prefix 10.255.254.1/32
                                 10.255.255.3          -       5       0       i Or-ID: 10.255.255.3 C-LST: 10.255.255.2 10.255.255.3 10.5.255.2 
 * >Ec    RD: 10.255.255.2:1 ip-prefix 10.255.254.2/32
                                 10.255.255.2          -       100     0       i
 *  ec    RD: 10.255.255.2:1 ip-prefix 10.255.254.2/32
                                 10.255.255.2          -       100     0       i Or-ID: 10.255.255.2 C-LST: 10.255.255.3 
 * >      RD: 10.255.255.3:1 ip-prefix 10.255.254.2/32
                                 10.255.255.3          -       5       0       i
 * >Ec    RD: 10.255.255.2:1 ip-prefix 10.255.254.3/32
                                 10.255.255.2          -       5       0       i
 *  ec    RD: 10.255.255.2:1 ip-prefix 10.255.254.3/32
                                 10.255.255.2          -       5       0       i Or-ID: 10.255.255.2 C-LST: 10.255.255.3 10.255.255.2 172.16.255.3 
 * >Ec    RD: 10.255.255.3:1 ip-prefix 10.255.254.3/32
                                 10.255.255.3          -       5       0       i
 *  ec    RD: 10.255.255.3:1 ip-prefix 10.255.254.3/32
                                 10.255.255.3          -       5       0       i Or-ID: 10.255.255.3 C-LST: 10.255.255.2 10.255.255.3 10.5.255.2 
 * >Ec    RD: 10.255.255.7:1 ip-prefix 10.255.254.3/32
                                 10.255.255.7          -       100     0       i Or-ID: 10.255.255.7 C-LST: 10.255.255.3 
 *  ec    RD: 10.255.255.7:1 ip-prefix 10.255.254.3/32
                                 10.255.255.7          -       100     0       i Or-ID: 10.255.255.7 C-LST: 10.255.255.2 
 * >Ec    RD: 10.255.255.2:1 ip-prefix 10.255.254.4/32
                                 10.255.255.2          -       5       0       i
 *  ec    RD: 10.255.255.2:1 ip-prefix 10.255.254.4/32
                                 10.255.255.2          -       5       0       i Or-ID: 10.255.255.2 C-LST: 10.255.255.3 10.255.255.2 172.16.255.3 
 * >Ec    RD: 10.255.255.3:1 ip-prefix 10.255.254.4/32
                                 10.255.255.3          -       5       0       i Or-ID: 10.255.255.12 C-LST: 10.255.255.3 10.5.255.2 10.255.255.1 
 *  ec    RD: 10.255.255.3:1 ip-prefix 10.255.254.4/32
                                 10.255.255.3          -       5       0       i Or-ID: 10.255.255.12 C-LST: 10.255.255.2 10.255.255.3 10.5.255.2 10.255.255.1 
 * >Ec    RD: 10.255.255.2:1 ip-prefix 10.255.254.5/32
                                 10.255.255.2          -       5       0       i
 *  ec    RD: 10.255.255.2:1 ip-prefix 10.255.254.5/32
                                 10.255.255.2          -       5       0       i Or-ID: 10.255.255.2 C-LST: 10.255.255.3 10.255.255.2 172.16.255.3 
 * >Ec    RD: 10.255.255.3:1 ip-prefix 10.255.254.5/32
                                 10.255.255.3          -       5       0       i Or-ID: 10.255.255.10 C-LST: 10.255.255.3 10.5.255.2 10.255.255.1 
 *  ec    RD: 10.255.255.3:1 ip-prefix 10.255.254.5/32
                                 10.255.255.3          -       5       0       i Or-ID: 10.255.255.10 C-LST: 10.255.255.2 10.255.255.3 10.5.255.2 10.255.255.1 
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
                                 10.255.255.3          -       5       0       i Or-ID: 10.255.255.3 C-LST: 10.255.255.2 10.255.255.3 10.5.255.2 
 * >Ec    RD: 10.255.255.2:1 ip-prefix 192.168.0.0/24
                                 10.255.255.2          -       5       0       i
 *  ec    RD: 10.255.255.2:1 ip-prefix 192.168.0.0/24
                                 10.255.255.2          -       5       0       i Or-ID: 10.255.255.2 C-LST: 10.255.255.3 10.255.255.2 172.16.255.3 
 * >Ec    RD: 10.255.255.3:1 ip-prefix 192.168.0.0/24
                                 10.255.255.3          -       5       0       i
 *  ec    RD: 10.255.255.3:1 ip-prefix 192.168.0.0/24
                                 10.255.255.3          -       5       0       i Or-ID: 10.255.255.3 C-LST: 10.255.255.2 10.255.255.3 10.5.255.2 
 * >Ec    RD: 10.255.255.2:1 ip-prefix 192.168.1.0/24
                                 10.255.255.2          -       100     0       i
 *  ec    RD: 10.255.255.2:1 ip-prefix 192.168.1.0/24
                                 10.255.255.2          -       100     0       i Or-ID: 10.255.255.2 C-LST: 10.255.255.3 
 * >      RD: 10.255.255.3:1 ip-prefix 192.168.1.0/24
                                 10.255.255.3          -       5       0       i
 * >Ec    RD: 10.255.255.2:1 ip-prefix 192.168.3.0/24
                                 10.255.255.2          -       5       0       i
 *  ec    RD: 10.255.255.2:1 ip-prefix 192.168.3.0/24
                                 10.255.255.2          -       5       0       i Or-ID: 10.255.255.2 C-LST: 10.255.255.3 10.255.255.2 172.16.255.3 
 * >Ec    RD: 10.255.255.3:1 ip-prefix 192.168.3.0/24
                                 10.255.255.3          -       5       0       i
 *  ec    RD: 10.255.255.3:1 ip-prefix 192.168.3.0/24
                                 10.255.255.3          -       5       0       i Or-ID: 10.255.255.3 C-LST: 10.255.255.2 10.255.255.3 10.5.255.2 
 * >Ec    RD: 10.255.255.7:1 ip-prefix 192.168.3.0/24
                                 10.255.255.7          -       100     0       i Or-ID: 10.255.255.7 C-LST: 10.255.255.3 
 *  ec    RD: 10.255.255.7:1 ip-prefix 192.168.3.0/24
                                 10.255.255.7          -       100     0       i Or-ID: 10.255.255.7 C-LST: 10.255.255.2 
 * >      RD: 10.255.255.2:1 ip-prefix 192.168.5.0/24
                                 10.255.255.2          -       5       0       i
 * >Ec    RD: 10.255.255.3:1 ip-prefix 192.168.5.0/24
                                 10.255.255.3          -       100     0       i
 *  ec    RD: 10.255.255.3:1 ip-prefix 192.168.5.0/24
                                 10.255.255.3          -       100     0       i Or-ID: 10.255.255.3 C-LST: 10.255.255.2 
 * >Ec    RD: 10.255.255.2:1 ip-prefix 192.168.6.0/24
                                 10.255.255.2          -       5       0       i
 *  ec    RD: 10.255.255.2:1 ip-prefix 192.168.6.0/24
                                 10.255.255.2          -       5       0       i Or-ID: 10.255.255.2 C-LST: 10.255.255.3 10.255.255.2 172.16.255.3 
 * >Ec    RD: 10.255.255.3:1 ip-prefix 192.168.6.0/24
                                 10.255.255.3          -       5       0       i Or-ID: 10.255.255.12 C-LST: 10.255.255.3 10.5.255.2 10.255.255.1 
 *  ec    RD: 10.255.255.3:1 ip-prefix 192.168.6.0/24
                                 10.255.255.3          -       5       0       i Or-ID: 10.255.255.12 C-LST: 10.255.255.2 10.255.255.3 10.5.255.2 10.255.255.1 
 * >Ec    RD: 10.255.255.2:1 ip-prefix 192.168.40.0/24
                                 10.255.255.2          -       5       0       i
 *  ec    RD: 10.255.255.2:1 ip-prefix 192.168.40.0/24
                                 10.255.255.2          -       5       0       i Or-ID: 10.255.255.2 C-LST: 10.255.255.3 10.255.255.2 172.16.255.3 
 * >Ec    RD: 10.255.255.3:1 ip-prefix 192.168.40.0/24
                                 10.255.255.3          -       5       0       i Or-ID: 10.255.255.10 C-LST: 10.255.255.3 10.5.255.2 10.255.255.1 
 *  ec    RD: 10.255.255.3:1 ip-prefix 192.168.40.0/24
                                 10.255.255.3          -       5       0       i Or-ID: 10.255.255.10 C-LST: 10.255.255.2 10.255.255.3 10.5.255.2 10.255.255.1 
```

## show ip security connection detail

```text
path3:
  Source address: 172.16.2.7, Destination address: 172.16.2.0
  State: established
  Uptime: 15 minutes, 11 seconds
  VRF: default
  Type: static
  Remote IP: 10.255.255.7
  Role: responder
  Inbound SPI: 0xcdfa87:
    Request ID: 2, Mode: transport, Replay window size: 16384, Seq: 0x0
    Errors:
      Packets outside replay window: 0, Replay: 0, Integrity failed: 0
    Lifetime config:
      Soft byte limit: 4633907000999, Hard byte limit: 6442450944000
      Soft packet limit: 2784220454, Hard packet limit: 4000000000
      Soft time limit: 2865 secs, Hard time limit: 3600 secs
    Lifetime current:
      Current bytes: 1071090944
      Current packets: 1061016
      SA add time: Thu Mar 14 20:22:47 2024
      SA last use time: Thu Mar 14 20:38:05 2024
  Outbound SPI: 0xcc759a:
    Request ID: 2, Mode: transport, Replay window size: 0, Seq: 0x0
    Errors:
      Packets outside replay window: 0, Replay: 0, Integrity failed: 0
    Lifetime config:
      Soft byte limit: 4452216232499, Hard byte limit: 6442450944000
      Soft packet limit: 2979851885, Hard packet limit: 4000000000
      Soft time limit: 2661 secs, Hard time limit: 3600 secs
    Lifetime current:
      Current bytes: 2542140175
      Current packets: 5050370
      SA add time: Thu Mar 14 20:22:47 2024
      SA last use time: Thu Mar 14 20:38:06 2024
path4:
  Source address: 172.16.2.7, Destination address: 172.16.2.5
  State: established
  Uptime: 16 minutes, 6 seconds
  VRF: default
  Type: static
  Remote IP: 10.255.255.7
  Role: responder
  Inbound SPI: 0xc65c20:
    Request ID: 1, Mode: transport, Replay window size: 16384, Seq: 0x0
    Errors:
      Packets outside replay window: 0, Replay: 0, Integrity failed: 0
    Lifetime config:
      Soft byte limit: 4039536256499, Hard byte limit: 6442450944000
      Soft packet limit: 2456260532, Hard packet limit: 4000000000
      Soft time limit: 2870 secs, Hard time limit: 3600 secs
    Lifetime current:
      Current bytes: 47915084
      Current packets: 88691
      SA add time: Thu Mar 14 20:21:52 2024
      SA last use time: Thu Mar 14 20:38:05 2024
  Outbound SPI: 0xc85f3d:
    Request ID: 1, Mode: transport, Replay window size: 0, Seq: 0x0
    Errors:
      Packets outside replay window: 0, Replay: 0, Integrity failed: 0
    Lifetime config:
      Soft byte limit: 4243643812499, Hard byte limit: 6442450944000
      Soft packet limit: 2518962420, Hard packet limit: 4000000000
      Soft time limit: 3008 secs, Hard time limit: 3600 secs
    Lifetime current:
      Current bytes: 3962628795
      Current packets: 7831648
      SA add time: Thu Mar 14 20:21:52 2024
      SA last use time: Thu Mar 14 20:38:06 2024
path5:
  Source address: 172.16.2.7, Destination address: 172.16.2.2
  State: established
  Uptime: 14 minutes, 37 seconds
  VRF: default
  Type: dynamic
  Remote IP: 10.255.255.7
  Role: responder
  Packets in: 0, Packets out: 0
  Last known rekey count: 0
  Dynamic state: established
  Last established time: Thu Mar 14 20:23:49 2024
  DH crypto:
    Local rekey: 0, Peer rekey: 0, In SPI: 0xb3cebedf, Out SPI: 0xcdcb1079
  DH state:
    Local rekey: 0, Peer rekey: 0, DH rekey state: not rekeying, Role: not rekeying
  SA rekey role: not rekeying
  SA state:
    SA type: ingress , SPI: 0xd6cf30d1
      Role: responder, SA rekey state: initial, Peer nonce type: init
      Add time: Thu Mar 14 20:23:21 2024, Packets: 38860, Pair SPI: 0xbcd2de37
    SA type: egress , SPI: 0xbcd2de37
      Role: responder, SA rekey state: initial, Peer nonce type: init
      Add time: Thu Mar 14 20:23:21 2024, Packets: 5757208, Pair SPI: 0xd6cf30d1
  Inbound SPI: 0xd6cf30d1:
    Request ID: 3, Mode: transport, Replay window size: 0, Seq: 0x0
    Errors:
      Packets outside replay window: 0, Replay: 0, Integrity failed: 0
    Lifetime config:
      Soft byte limit: 4689227038725, Hard byte limit: 6442450944000
      Soft packet limit: 2928510589, Hard packet limit: 4000000000
      Soft time limit: 2599 secs, Hard time limit: 3600 secs
    Lifetime current:
      Current bytes: 39540896
      Current packets: 38868
      SA add time: Thu Mar 14 20:23:21 2024
      SA last use time: Thu Mar 14 20:38:05 2024
  Outbound SPI: 0xbcd2de37:
    Request ID: 3, Mode: transport, Replay window size: 0, Seq: 0x0
    Errors:
      Packets outside replay window: 0, Replay: 0, Integrity failed: 0
    Lifetime config:
      Soft byte limit: 4797247243650, Hard byte limit: 6442450944000
      Soft packet limit: 2920059117, Hard packet limit: 4000000000
      Soft time limit: 2599 secs, Hard time limit: 3600 secs
    Lifetime current:
      Current bytes: 2944783258
      Current packets: 5786762
      SA add time: Thu Mar 14 20:23:21 2024
      SA last use time: Thu Mar 14 20:38:06 2024
```

## show stun client translations detail

```text
Current System Time: Thu Mar 14 20:37:59 2024
Transaction ID 000000020affff0900000000
Agent Name: dps
Source Address: 172.16.2.7:4500
Public Address: 172.16.2.7:4500
Number of Attributes: 3
Timeout Interval: 0:00:10
Last Refreshed: 0:00:09 ago
Attribute Type   Length Value           
---------------- ------ ----------------
PATH_GROUP            3 ATT             
VTEP_IP               4 10.255.255.9    
WAN_ID                4 2               

```

## show stun server bindings detail

```text
Current System Time: Thu Mar 14 20:37:59 2024
```

## show path-selection paths detail

```text
Peer: 10.255.255.2, Path group ATT
Path name: path3, static, Label: 3
Source: 172.16.2.7, Port: 4500, WAN ID: 2
Destination: 172.16.2.0, Port: 4500, WAN ID: 2886730240
Local interface: Ethernet1
Route state: IPsec established
Traffic class 0: active (0:15:11)
MTU: 8914

Peer: 10.255.255.3, Path group ATT
Path name: path4, static, Label: 4
Source: 172.16.2.7, Port: 4500, WAN ID: 2
Destination: 172.16.2.5, Port: 4500, WAN ID: 2886730245
Local interface: Ethernet1
Route state: IPsec established
Traffic class 0: active (0:16:05)
MTU: 8914

Peer: 10.255.255.7, Path group ATT
Path name: path5, dynamic, Label: 5
Source: 172.16.2.7, Port: 4500, WAN ID: 2
Destination: 172.16.2.2, Port: 4500, WAN ID: 1
Local interface: Ethernet1
Route state: IPsec established
Traffic class 0: active (0:14:36)
MTU: 8914

```

## show bgp neighbors

```text
BGP neighbor is 10.255.255.2, remote AS 65000, internal link
  BGP version 4, remote router ID 10.255.255.2, VRF default
  Inherits configuration from and member of peer-group PATHFINDER
  Last read 00:00:12, last write 00:00:24
  Hold time is 180, keepalive interval is 60 seconds
  Configured hold time is 180, keepalive interval is 60 seconds
  Effective minimum hold time is 3 seconds
  Send failure hold time is 0 seconds
  Hold timer is active, time left: 00:02:48
  Keepalive timer is active, time left: 00:00:25
  Connect timer is inactive
  Idle-restart timer is inactive
  BGP state is Established, up for 00:15:04
  Number of transitions to established: 1
  Last state was OpenConfirm
  Last event was Established
  Last sent socket-error:Connect (Network is unreachable), Last time 00:18:16
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
      Received 00:14:33
      Number of stale paths removed after graceful restart: 0
      Number of paths received before End-of-RIB: 6
    L2VPN EVPN End-of-RIB received: Yes
      Received 00:14:33
      Number of stale paths removed after graceful restart: 0
      Number of paths received before End-of-RIB: 35
  AIGP attribute send and receive for IPv4 Unicast are enabled
  AIGP attribute send and receive for IPv4 with MPLS Labels are enabled
  AIGP attribute send and receive for IPv6 Unicast are enabled
  AIGP attribute send and receive for IPv6 with MPLS Labels are enabled
  BGP session driven failover for IPv6 Unicast is disabled
  BGP session driven failover for IPv4 Unicast is disabled
  Message Statistics:
                                  Sent      Rcvd
    Opens:                           1         1
    Notifications:                   0         0
    Updates:                         8     37348
    Keepalives:                     19        14
    Enhanced Route Refresh:          0         0
    Begin of Route Refresh:          0         0
    End of Route Refresh:            0         0
    Total messages:                 28     37363
  Prefix Statistics:
                                   Sent      Rcvd     Best Paths     Best ECMP Paths
    IPv4 Unicast:                     0         0              0                   0
    IPv4 Dps:                         2         6              6                   3
    IPv6 Unicast:                     0         0              0                   0
    EVPN:                             1        47             47                  22
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
    Last update with error received at: 00:15:03
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
Local AS is 65000, local router ID 10.255.255.9
TTL is 255
Local TCP address is 10.255.255.9, local port is 33303
Remote TCP address is 10.255.255.2, remote port is 179
Local next hop for next hop self:
  Dps: 10.255.255.9
  L2VPN EVPN: 10.255.255.9
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
    Retransmission Timeout (rto): 208.0ms
    Round-trip Time (rtt/rtvar): 5.5ms/5.2ms
    Delayed Ack Timeout (ato): 40.0ms
    Congestion Window (cwnd): 2
    TCP Throughput: 4.24 Mbps
    Recv Round-trip Time (rcv_rtt): 514.0ms
    Advertised Recv Window (rcv_space): 64398

BGP neighbor is 10.255.255.3, remote AS 65000, internal link
  BGP version 4, remote router ID 10.255.255.3, VRF default
  Inherits configuration from and member of peer-group PATHFINDER
  Last read 00:00:56, last write 00:00:06
  Hold time is 180, keepalive interval is 60 seconds
  Configured hold time is 180, keepalive interval is 60 seconds
  Effective minimum hold time is 3 seconds
  Send failure hold time is 0 seconds
  Hold timer is active, time left: 00:02:04
  Keepalive timer is active, time left: 00:00:49
  Connect timer is inactive
  Idle-restart timer is inactive
  BGP state is Established, up for 00:01:49
  Number of transitions to established: 3
  Last state was OpenConfirm
  Last event was RecvUpdate
  Last rcvd notification:Cease/administrative reset, Last time 00:01:50, First time 00:02:53, Repeats 1
  Last sent socket-error:Connect (Network is unreachable), Last time 00:18:17
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
      Received 00:01:48
      Number of stale paths removed after graceful restart: 0
      Number of paths received before End-of-RIB: 6
    L2VPN EVPN End-of-RIB received: Yes
      Received 00:01:48
      Number of stale paths removed after graceful restart: 0
      Number of paths received before End-of-RIB: 43
  AIGP attribute send and receive for IPv4 Unicast are enabled
  AIGP attribute send and receive for IPv4 with MPLS Labels are enabled
  AIGP attribute send and receive for IPv6 Unicast are enabled
  AIGP attribute send and receive for IPv6 with MPLS Labels are enabled
  BGP session driven failover for IPv6 Unicast is disabled
  BGP session driven failover for IPv4 Unicast is disabled
  Message Statistics:
                                  Sent      Rcvd
    Opens:                           3         3
    Notifications:                   0         2
    Updates:                        18     29745
    Keepalives:                     23        16
    Enhanced Route Refresh:          0         0
    Begin of Route Refresh:          0         0
    End of Route Refresh:            0         0
    Total messages:                 44     29766
  Prefix Statistics:
                                   Sent      Rcvd     Best Paths     Best ECMP Paths
    IPv4 Unicast:                     0         0              0                   0
    IPv4 Dps:                         2         6              6                   1
    IPv6 Unicast:                     0         0              0                   0
    EVPN:                             1        47             47                  23
  Configured maximum total number of routes is 12000
  Inbound updates dropped by reason:
    AS path loop detection: 0
    Cluster ID loop detection: 0
    Enforced First AS: 0
    Malformed MPBGP routes: 0
    Originator ID matches local router ID: 2
    Nexthop matches local IP address: 1
    Unexpected IPv6 nexthop for IPv4 routes: 0
  Inbound updates with attribute errors:
    Resulting in removal of all paths in update (treat as withdraw): 1
    Resulting in AFI/SAFI disable: 0
    Resulting in attribute ignore: 0
    Disabled AFI/SAFIs: None
    Last treat-as-withdraw attribute error: Nexthop is local address
    Last update with error received at: 00:01:48
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
Local AS is 65000, local router ID 10.255.255.9
TTL is 255
Local TCP address is 10.255.255.9, local port is 46465
Remote TCP address is 10.255.255.3, remote port is 179
Local next hop for next hop self:
  Dps: 10.255.255.9
  L2VPN EVPN: 10.255.255.9
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
    Retransmission Timeout (rto): 212.0ms
    Round-trip Time (rtt/rtvar): 11.0ms/15.4ms
    Delayed Ack Timeout (ato): 40.0ms
    Congestion Window (cwnd): 10
    TCP Throughput: 10.50 Mbps
    Advertised Recv Window (rcv_space): 14480

```

## show bgp path-selection detail

```text
BGP routing table information for VRF default
Router identifier 10.255.255.9, local AS number 65000
Bgp routing table entry for ipv4Dps VTEP 10.255.255.7/32
 Paths: 4 available
  Local
    :: from 10.255.255.2 (10.255.255.2)
      Origin IGP, metric -, localpref 100, weight 0, received 00:14:37 ago, valid, internal
      Tunnel encapsulation attribute: Dynamic path selection
        Endpoint: 172.16.2.2, Path group name: ATT, WAN ID: 1, UDP port: 4500
  Local
    :: from 10.255.255.3 (10.255.255.3)
      Origin IGP, metric -, localpref 100, weight 0, received 00:01:49 ago, valid, internal
      Tunnel encapsulation attribute: Dynamic path selection
        Endpoint: 172.16.2.2, Path group name: ATT, WAN ID: 1, UDP port: 4500
  Local
    :: from 10.255.255.3 (10.255.255.3)
      Origin IGP, metric -, localpref 100, weight 0, received 00:01:49 ago, valid, internal
      Tunnel encapsulation attribute: Dynamic path selection
        Endpoint: 172.16.2.2, Path group name: ATT, WAN ID: 1, UDP port: 4500
  Local
    :: from 10.255.255.2 (10.255.255.2)
      Origin IGP, metric -, localpref 100, weight 0, received 00:01:49 ago, valid, internal
      Tunnel encapsulation attribute: Dynamic path selection
        Endpoint: 172.16.2.2, Path group name: ATT, WAN ID: 1, UDP port: 4500
Bgp routing table entry for ipv4Dps VTEP 10.255.255.9/32
 Paths: 1 available
  Local
    - from - (0.0.0.0)
      Origin IGP, metric -, localpref -, weight 0, received 00:16:11 ago, valid, local
      Tunnel encapsulation attribute: Dynamic path selection
        Endpoint: 172.16.2.7, Path group name: ATT, WAN ID: 2, UDP port: 4500
Bgp routing table entry for ipv4Ipsec VTEP 10.255.255.2/32
 Paths: 2 available
  Local
    :: from 10.255.255.2 (10.255.255.2)
      Origin IGP, metric -, localpref 100, weight 0, received 00:15:04 ago, valid, internal
      Tunnel encapsulation attribute: IP security
        Initial contact: false, Rekey counter: 0, Nonce length: 32
        DH group: 14, DH key length: 256
        Encryption algo: aes256, Authentication algo: sha256
  Local
    :: from 10.255.255.3 (10.255.255.3)
      Origin IGP, metric -, localpref 100, weight 0, received 00:01:49 ago, valid, internal
      Tunnel encapsulation attribute: IP security
        Initial contact: false, Rekey counter: 0, Nonce length: 32
        DH group: 14, DH key length: 256
        Encryption algo: aes256, Authentication algo: sha256
Bgp routing table entry for ipv4Ipsec VTEP 10.255.255.3/32
 Paths: 2 available
  Local
    :: from 10.255.255.3 (10.255.255.3)
      Origin IGP, metric -, localpref 100, weight 0, received 00:01:49 ago, valid, internal
      Tunnel encapsulation attribute: IP security
        Initial contact: false, Rekey counter: 0, Nonce length: 32
        DH group: 14, DH key length: 256
        Encryption algo: aes256, Authentication algo: sha256
  Local
    :: from 10.255.255.2 (10.255.255.2)
      Origin IGP, metric -, localpref 100, weight 0, received 00:01:49 ago, valid, internal
      Tunnel encapsulation attribute: IP security
        Initial contact: false, Rekey counter: 0, Nonce length: 32
        DH group: 14, DH key length: 256
        Encryption algo: aes256, Authentication algo: sha256
Bgp routing table entry for ipv4Ipsec VTEP 10.255.255.7/32
 Paths: 4 available
  Local
    :: from 10.255.255.2 (10.255.255.2)
      Origin IGP, metric -, localpref 100, weight 0, received 00:14:37 ago, valid, internal
      Tunnel encapsulation attribute: IP security
        Initial contact: false, Rekey counter: 0, Nonce length: 32
        DH group: 14, DH key length: 256
        Encryption algo: aes256, Authentication algo: sha256
  Local
    :: from 10.255.255.3 (10.255.255.3)
      Origin IGP, metric -, localpref 100, weight 0, received 00:01:49 ago, valid, internal
      Tunnel encapsulation attribute: IP security
        Initial contact: false, Rekey counter: 0, Nonce length: 32
        DH group: 14, DH key length: 256
        Encryption algo: aes256, Authentication algo: sha256
  Local
    :: from 10.255.255.3 (10.255.255.3)
      Origin IGP, metric -, localpref 100, weight 0, received 00:01:49 ago, valid, internal
      Tunnel encapsulation attribute: IP security
        Initial contact: false, Rekey counter: 0, Nonce length: 32
        DH group: 14, DH key length: 256
        Encryption algo: aes256, Authentication algo: sha256
  Local
    :: from 10.255.255.2 (10.255.255.2)
      Origin IGP, metric -, localpref 100, weight 0, received 00:01:49 ago, valid, internal
      Tunnel encapsulation attribute: IP security
        Initial contact: false, Rekey counter: 0, Nonce length: 32
        DH group: 14, DH key length: 256
        Encryption algo: aes256, Authentication algo: sha256
Bgp routing table entry for ipv4Ipsec VTEP 10.255.255.9/32
 Paths: 1 available
  Local
    - from - (0.0.0.0)
      Origin IGP, metric -, localpref -, weight 0, received 00:18:11 ago, valid, local
      Tunnel encapsulation attribute: IP security
        Initial contact: false, Rekey counter: 0, Nonce length: 32
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
>C    10.255.255.9/32 [0 pref/0 metric] updated 00:18:24 ago
         via Loopback0, directly connected
>C    172.16.2.6/31 [0 pref/0 metric] updated 00:18:17 ago
         via Ethernet1, directly connected
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
>S    0.0.0.0/0 [1 pref/0 metric] updated 00:18:17 ago
         via 172.16.2.6 [0 pref/0 metric] type ipv4
            via 172.16.2.6, Ethernet1
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
>P    0.0.0.0/8 [1 pref/0 metric] updated 00:18:23 ago
         via Null0, directly connected [NF]
>P    10.255.255.2/32 [1 pref/0 metric] updated 00:18:13 ago
         via 10.255.255.2, Dps1
>P    10.255.255.3/32 [1 pref/0 metric] updated 00:18:13 ago
         via 10.255.255.3, Dps1
>P    10.255.255.7/32 [1 pref/0 metric] updated 00:14:41 ago
         via 10.255.255.7, Dps1
>P    127.0.0.0/8 [1 pref/0 metric] updated 00:18:23 ago
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
>P    ::/96 [1 pref/0 metric] updated 00:18:14 ago
         via Null0, directly connected [NF]
>P    ::ffff:127.0.0.0/104 [1 pref/0 metric] updated 00:18:14 ago
         via :: [1 pref/1 metric] type ipv6
            via , directly connected
>P    fe80::/10 [1 pref/0 metric] updated 00:18:14 ago
```

