# Test results for VM2

## show version

```text
Arista vEOS
Hardware version: 
Serial number: 5D0D99A5000E23386CCBB77AFF777B18
Hardware MAC address: 000c.2978.c52d
System MAC address: 000c.2978.c52d

Software image version: 4.31.2F-cloud
Architecture: i686
Internal build version: 4.31.2F-cloud-35442146.4312F
Internal build ID: 635a071a-386e-447f-942c-bcc34d9ffd3c
Image format version: 1.0
Image optimization: None

Uptime: 17 hours and 1 minute
Total memory: 16264192 kB
Free memory: 10337940 kB

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
Ethernet1       172.16.0.11/31        up         up              9000          
Ethernet2       10.6.255.2/31         up         up              1500          
Loopback0       10.255.255.12/32      up         up             65535          
Management1     172.28.138.241/20     up         up              1500          

```

## show interfaces counters rates | nz

```text
Port      Name         Intvl  In Mbps      %  In Kpps Out Mbps      % Out Kpps
Et1       VZ_OFF        0:01    137.6   1.4%       16    169.3   1.7%       19
Et2       CE_interface  0:01    157.0   1.6%       19    127.6   1.3%       16
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
           via 172.16.0.10, Ethernet1

 S        10.255.255.1/32
           directly connected, Dps1
 S        10.255.255.4/32
           directly connected, Dps1
 S        10.255.255.5/32
           directly connected, Dps1
 S        10.255.255.6/32
           directly connected, Dps1
 S        10.255.255.11/32
           directly connected, Dps1
 C        10.255.255.12/32
           directly connected, Loopback0
 C        172.16.0.10/31
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
           via 172.16.0.10, Ethernet1

 S        10.255.255.1/32
           directly connected, Dps1
 S        10.255.255.4/32
           directly connected, Dps1
 S        10.255.255.5/32
           directly connected, Dps1
 S        10.255.255.6/32
           directly connected, Dps1
 S        10.255.255.11/32
           directly connected, Dps1
 C        10.255.255.12/32
           directly connected, Loopback0
 C        172.16.0.10/31
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
           via VTEP 10.255.255.5 VNI 201 router-mac ec:8a:48:04:21:53
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
 C        10.6.255.2/31
           directly connected, Ethernet2
 B I      10.255.254.1/32 [20/0]
           via VTEP 10.255.255.5 VNI 201 router-mac ec:8a:48:04:21:53
           via VTEP 10.255.255.6 VNI 201 router-mac ec:8a:48:04:2b:ae
 B I      10.255.254.2/32 [20/0]
           via VTEP 10.255.255.1 VNI 201 router-mac ec:8a:48:04:f5:30
 B I      10.255.254.3/32 [20/0]
           via VTEP 10.255.255.8 VNI 201 router-mac ec:8a:48:04:2c:53
 O        10.255.254.4/32 [110/20]
           via 10.6.255.3, Ethernet2
 B I      10.255.254.5/32 [20/0]
           via VTEP 10.255.255.10 VNI 201 router-mac 00:0c:29:d5:32:d4
 B I      10.255.254.6/32 [20/0]
           via VTEP 10.255.255.4 VNI 201 router-mac ec:8a:48:04:ff:5b
 B I      172.16.255.0/31 [20/0]
           via VTEP 10.255.255.4 VNI 201 router-mac ec:8a:48:04:ff:5b
 B I      172.16.255.2/31 [20/0]
           via VTEP 10.255.255.1 VNI 201 router-mac ec:8a:48:04:f5:30
 B I      192.168.0.0/24 [20/0]
           via VTEP 10.255.255.5 VNI 201 router-mac ec:8a:48:04:21:53
           via VTEP 10.255.255.6 VNI 201 router-mac ec:8a:48:04:2b:ae
 B I      192.168.1.0/24 [20/0]
           via VTEP 10.255.255.1 VNI 201 router-mac ec:8a:48:04:f5:30
 B I      192.168.3.0/24 [20/0]
           via VTEP 10.255.255.8 VNI 201 router-mac ec:8a:48:04:2c:53
 B I      192.168.5.0/24 [20/0]
           via VTEP 10.255.255.4 VNI 201 router-mac ec:8a:48:04:ff:5b
 O        192.168.6.0/24 [110/20]
           via 10.6.255.3, Ethernet2
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
Router identifier 10.255.255.12, local AS number 65000
Route status codes: * - valid, > - active, S - Stale, E - ECMP head, e - ECMP
                    c - Contributing to ECMP, % - Pending best path selection
Origin codes: i - IGP, e - EGP, ? - incomplete
AS Path Attributes: Or-ID - Originator ID, C-LST - Cluster List, LL Nexthop - Link Local Nexthop

          Network                Next Hop              Metric  LocPref Weight  Path
 * >Ec    RD: 10.255.255.5:1 ip-prefix 10.0.255.0/31
                                 10.255.255.5          -       100     0       i Or-ID: 10.255.255.5 C-LST: 10.255.255.4 
 *  ec    RD: 10.255.255.5:1 ip-prefix 10.0.255.0/31
                                 10.255.255.5          -       100     0       i Or-ID: 10.255.255.5 C-LST: 10.255.255.1 10.255.255.4 
 * >Ec    RD: 10.255.255.6:1 ip-prefix 10.0.255.2/31
                                 10.255.255.6          -       100     0       i Or-ID: 10.255.255.6 C-LST: 10.255.255.4 
 *  ec    RD: 10.255.255.6:1 ip-prefix 10.0.255.2/31
                                 10.255.255.6          -       100     0       i Or-ID: 10.255.255.6 C-LST: 10.255.255.1 10.255.255.4 
 * >Ec    RD: 10.255.255.1:1 ip-prefix 10.1.255.0/31
                                 10.255.255.1          -       100     0       i
 *  ec    RD: 10.255.255.1:1 ip-prefix 10.1.255.0/31
                                 10.255.255.1          -       100     0       i Or-ID: 10.255.255.1 C-LST: 10.255.255.4 
 * >Ec    RD: 10.255.255.1:1 ip-prefix 10.1.255.2/31
                                 10.255.255.1          -       5       0       i Or-ID: 10.255.255.1 C-LST: 10.255.255.4 10.255.255.1 
 *  ec    RD: 10.255.255.1:1 ip-prefix 10.1.255.2/31
                                 10.255.255.1          -       5       0       i
 * >Ec    RD: 10.255.255.4:1 ip-prefix 10.1.255.2/31
                                 10.255.255.4          -       5       0       i
 *  ec    RD: 10.255.255.4:1 ip-prefix 10.1.255.2/31
                                 10.255.255.4          -       5       0       i Or-ID: 10.255.255.4 C-LST: 10.255.255.1 10.255.255.4 172.16.255.0 
 * >Ec    RD: 10.255.255.1:1 ip-prefix 10.2.255.0/31
                                 10.255.255.1          -       5       0       i
 *  ec    RD: 10.255.255.1:1 ip-prefix 10.2.255.0/31
                                 10.255.255.1          -       5       0       i Or-ID: 10.255.255.1 C-LST: 10.255.255.4 10.255.255.1 172.16.255.2 
 * >Ec    RD: 10.255.255.4:1 ip-prefix 10.2.255.0/31
                                 10.255.255.4          -       5       0       i Or-ID: 10.255.255.7 C-LST: 10.255.255.4 172.16.255.0 10.255.255.2 
 *  ec    RD: 10.255.255.4:1 ip-prefix 10.2.255.0/31
                                 10.255.255.4          -       5       0       i Or-ID: 10.255.255.7 C-LST: 10.255.255.1 10.255.255.4 172.16.255.0 10.255.255.2 
 * >Ec    RD: 10.255.255.7:1 ip-prefix 10.2.255.2/31
                                 10.255.255.8          -       100     0       i Or-ID: 10.255.255.8 C-LST: 10.255.255.1 
 *  ec    RD: 10.255.255.7:1 ip-prefix 10.2.255.2/31
                                 10.255.255.8          -       100     0       i Or-ID: 10.255.255.8 C-LST: 10.255.255.4 10.255.255.1 
 * >Ec    RD: 10.255.255.1:1 ip-prefix 10.4.255.0/31
                                 10.255.255.1          -       5       0       i Or-ID: 10.255.255.1 C-LST: 10.255.255.4 10.255.255.1 172.16.255.2 
 *  ec    RD: 10.255.255.1:1 ip-prefix 10.4.255.0/31
                                 10.255.255.1          -       5       0       i
 * >Ec    RD: 10.255.255.4:1 ip-prefix 10.4.255.0/31
                                 10.255.255.4          -       5       0       i Or-ID: 10.255.255.9 C-LST: 10.255.255.4 172.16.255.0 10.255.255.2 
 *  ec    RD: 10.255.255.4:1 ip-prefix 10.4.255.0/31
                                 10.255.255.4          -       5       0       i Or-ID: 10.255.255.9 C-LST: 10.255.255.1 10.255.255.4 172.16.255.0 10.255.255.2 
 * >Ec    RD: 10.255.255.10:1 ip-prefix 10.4.255.2/31
                                 10.255.255.10         -       100     0       i Or-ID: 10.255.255.10 C-LST: 10.255.255.1 
 *  ec    RD: 10.255.255.10:1 ip-prefix 10.4.255.2/31
                                 10.255.255.10         -       100     0       i Or-ID: 10.255.255.10 C-LST: 10.255.255.4 10.255.255.1 
 * >Ec    RD: 10.255.255.1:1 ip-prefix 10.5.255.0/31
                                 10.255.255.1          -       5       0       i
 *  ec    RD: 10.255.255.1:1 ip-prefix 10.5.255.0/31
                                 10.255.255.1          -       5       0       i Or-ID: 10.255.255.1 C-LST: 10.255.255.4 10.255.255.1 172.16.255.2 
 * >Ec    RD: 10.255.255.4:1 ip-prefix 10.5.255.0/31
                                 10.255.255.4          -       5       0       i
 *  ec    RD: 10.255.255.4:1 ip-prefix 10.5.255.0/31
                                 10.255.255.4          -       5       0       i Or-ID: 10.255.255.4 C-LST: 10.255.255.1 10.255.255.4 
 * >Ec    RD: 10.255.255.4:1 ip-prefix 10.5.255.2/31
                                 10.255.255.4          -       100     0       i Or-ID: 10.255.255.4 C-LST: 10.255.255.1 
 *  ec    RD: 10.255.255.4:1 ip-prefix 10.5.255.2/31
                                 10.255.255.4          -       100     0       i
 * >Ec    RD: 10.255.255.11:1 ip-prefix 10.6.255.0/31
                                 10.255.255.11         -       100     0       i Or-ID: 10.255.255.11 C-LST: 10.255.255.4 
 *  ec    RD: 10.255.255.11:1 ip-prefix 10.6.255.0/31
                                 10.255.255.11         -       100     0       i Or-ID: 10.255.255.11 C-LST: 10.255.255.1 10.255.255.4 
 * >      RD: 10.255.255.12:1 ip-prefix 10.6.255.2/31
                                 -                     -       -       0       i
 * >Ec    RD: 10.255.255.5:1 ip-prefix 10.255.254.1/32
                                 10.255.255.5          -       100     0       i Or-ID: 10.255.255.5 C-LST: 10.255.255.4 
 *  ec    RD: 10.255.255.5:1 ip-prefix 10.255.254.1/32
                                 10.255.255.5          -       100     0       i Or-ID: 10.255.255.5 C-LST: 10.255.255.1 10.255.255.4 
 * >Ec    RD: 10.255.255.6:1 ip-prefix 10.255.254.1/32
                                 10.255.255.6          -       100     0       i Or-ID: 10.255.255.6 C-LST: 10.255.255.1 
 *  ec    RD: 10.255.255.6:1 ip-prefix 10.255.254.1/32
                                 10.255.255.6          -       100     0       i Or-ID: 10.255.255.6 C-LST: 10.255.255.4 
 * >Ec    RD: 10.255.255.1:1 ip-prefix 10.255.254.2/32
                                 10.255.255.1          -       100     0       i Or-ID: 10.255.255.1 C-LST: 10.255.255.4 
 *  ec    RD: 10.255.255.1:1 ip-prefix 10.255.254.2/32
                                 10.255.255.1          -       100     0       i
 * >      RD: 10.255.255.4:1 ip-prefix 10.255.254.2/32
                                 10.255.255.4          -       5       0       i
 * >Ec    RD: 10.255.255.1:1 ip-prefix 10.255.254.3/32
                                 10.255.255.1          -       5       0       i
 *  ec    RD: 10.255.255.1:1 ip-prefix 10.255.254.3/32
                                 10.255.255.1          -       5       0       i Or-ID: 10.255.255.1 C-LST: 10.255.255.4 10.255.255.1 172.16.255.2 
 * >Ec    RD: 10.255.255.4:1 ip-prefix 10.255.254.3/32
                                 10.255.255.4          -       5       0       i Or-ID: 10.255.255.7 C-LST: 10.255.255.4 172.16.255.0 10.255.255.2 
 *  ec    RD: 10.255.255.4:1 ip-prefix 10.255.254.3/32
                                 10.255.255.4          -       5       0       i Or-ID: 10.255.255.7 C-LST: 10.255.255.1 10.255.255.4 172.16.255.0 10.255.255.2 
 * >Ec    RD: 10.255.255.7:1 ip-prefix 10.255.254.3/32
                                 10.255.255.8          -       100     0       i Or-ID: 10.255.255.8 C-LST: 10.255.255.1 
 *  ec    RD: 10.255.255.7:1 ip-prefix 10.255.254.3/32
                                 10.255.255.8          -       100     0       i Or-ID: 10.255.255.8 C-LST: 10.255.255.4 
          RD: 10.255.255.11:1 ip-prefix 10.255.254.4/32
                                 PolicyReject          -       -       0       i Or-ID: 10.255.255.11 C-LST: 10.255.255.1 
          RD: 10.255.255.11:1 ip-prefix 10.255.254.4/32
                                 PolicyReject          -       -       0       i Or-ID: 10.255.255.11 C-LST: 10.255.255.4 
 * >      RD: 10.255.255.12:1 ip-prefix 10.255.254.4/32
                                 -                     -       -       0       i
 * >Ec    RD: 10.255.255.1:1 ip-prefix 10.255.254.5/32
                                 10.255.255.1          -       5       0       i
 *  ec    RD: 10.255.255.1:1 ip-prefix 10.255.254.5/32
                                 10.255.255.1          -       5       0       i Or-ID: 10.255.255.1 C-LST: 10.255.255.4 10.255.255.1 172.16.255.2 
 * >Ec    RD: 10.255.255.4:1 ip-prefix 10.255.254.5/32
                                 10.255.255.4          -       5       0       i
 *  ec    RD: 10.255.255.4:1 ip-prefix 10.255.254.5/32
                                 10.255.255.4          -       5       0       i Or-ID: 10.255.255.4 C-LST: 10.255.255.1 10.255.255.4 172.16.255.0 
 * >Ec    RD: 10.255.255.10:1 ip-prefix 10.255.254.5/32
                                 10.255.255.10         -       100     0       i Or-ID: 10.255.255.10 C-LST: 10.255.255.4 
 *  ec    RD: 10.255.255.10:1 ip-prefix 10.255.254.5/32
                                 10.255.255.10         -       100     0       i Or-ID: 10.255.255.10 C-LST: 10.255.255.1 
 * >      RD: 10.255.255.1:1 ip-prefix 10.255.254.6/32
                                 10.255.255.1          -       5       0       i
 * >Ec    RD: 10.255.255.4:1 ip-prefix 10.255.254.6/32
                                 10.255.255.4          -       100     0       i Or-ID: 10.255.255.4 C-LST: 10.255.255.1 
 *  ec    RD: 10.255.255.4:1 ip-prefix 10.255.254.6/32
                                 10.255.255.4          -       100     0       i
 * >Ec    RD: 10.255.255.1:1 ip-prefix 172.16.255.0/31
                                 10.255.255.1          -       5       0       i
 *  ec    RD: 10.255.255.1:1 ip-prefix 172.16.255.0/31
                                 10.255.255.1          -       5       0       i Or-ID: 10.255.255.1 C-LST: 10.255.255.4 10.255.255.1 172.16.255.2 
 * >Ec    RD: 10.255.255.4:1 ip-prefix 172.16.255.0/31
                                 10.255.255.4          -       100     0       i Or-ID: 10.255.255.4 C-LST: 10.255.255.1 
 *  ec    RD: 10.255.255.4:1 ip-prefix 172.16.255.0/31
                                 10.255.255.4          -       100     0       i
 * >Ec    RD: 10.255.255.1:1 ip-prefix 172.16.255.2/31
                                 10.255.255.1          -       100     0       i
 *  ec    RD: 10.255.255.1:1 ip-prefix 172.16.255.2/31
                                 10.255.255.1          -       100     0       i Or-ID: 10.255.255.1 C-LST: 10.255.255.4 
 * >Ec    RD: 10.255.255.4:1 ip-prefix 172.16.255.2/31
                                 10.255.255.4          -       5       0       i
 *  ec    RD: 10.255.255.4:1 ip-prefix 172.16.255.2/31
                                 10.255.255.4          -       5       0       i Or-ID: 10.255.255.4 C-LST: 10.255.255.1 10.255.255.4 172.16.255.0 
 * >Ec    RD: 10.255.255.5:1 ip-prefix 192.168.0.0/24
                                 10.255.255.5          -       100     0       i Or-ID: 10.255.255.5 C-LST: 10.255.255.4 
 *  ec    RD: 10.255.255.5:1 ip-prefix 192.168.0.0/24
                                 10.255.255.5          -       100     0       i Or-ID: 10.255.255.5 C-LST: 10.255.255.1 10.255.255.4 
 * >Ec    RD: 10.255.255.6:1 ip-prefix 192.168.0.0/24
                                 10.255.255.6          -       100     0       i Or-ID: 10.255.255.6 C-LST: 10.255.255.1 
 *  ec    RD: 10.255.255.6:1 ip-prefix 192.168.0.0/24
                                 10.255.255.6          -       100     0       i Or-ID: 10.255.255.6 C-LST: 10.255.255.4 
 * >Ec    RD: 10.255.255.1:1 ip-prefix 192.168.1.0/24
                                 10.255.255.1          -       100     0       i
 *  ec    RD: 10.255.255.1:1 ip-prefix 192.168.1.0/24
                                 10.255.255.1          -       100     0       i Or-ID: 10.255.255.1 C-LST: 10.255.255.4 
 * >      RD: 10.255.255.4:1 ip-prefix 192.168.1.0/24
                                 10.255.255.4          -       5       0       i
 * >Ec    RD: 10.255.255.1:1 ip-prefix 192.168.3.0/24
                                 10.255.255.1          -       5       0       i
 *  ec    RD: 10.255.255.1:1 ip-prefix 192.168.3.0/24
                                 10.255.255.1          -       5       0       i Or-ID: 10.255.255.1 C-LST: 10.255.255.4 10.255.255.1 172.16.255.2 
 * >Ec    RD: 10.255.255.4:1 ip-prefix 192.168.3.0/24
                                 10.255.255.4          -       5       0       i Or-ID: 10.255.255.7 C-LST: 10.255.255.4 172.16.255.0 10.255.255.2 
 *  ec    RD: 10.255.255.4:1 ip-prefix 192.168.3.0/24
                                 10.255.255.4          -       5       0       i Or-ID: 10.255.255.7 C-LST: 10.255.255.1 10.255.255.4 172.16.255.0 10.255.255.2 
 * >Ec    RD: 10.255.255.7:1 ip-prefix 192.168.3.0/24
                                 10.255.255.8          -       100     0       i Or-ID: 10.255.255.8 C-LST: 10.255.255.1 
 *  ec    RD: 10.255.255.7:1 ip-prefix 192.168.3.0/24
                                 10.255.255.8          -       100     0       i Or-ID: 10.255.255.8 C-LST: 10.255.255.4 
 * >      RD: 10.255.255.1:1 ip-prefix 192.168.5.0/24
                                 10.255.255.1          -       5       0       i
 * >Ec    RD: 10.255.255.4:1 ip-prefix 192.168.5.0/24
                                 10.255.255.4          -       100     0       i Or-ID: 10.255.255.4 C-LST: 10.255.255.1 
 *  ec    RD: 10.255.255.4:1 ip-prefix 192.168.5.0/24
                                 10.255.255.4          -       100     0       i
          RD: 10.255.255.11:1 ip-prefix 192.168.6.0/24
                                 PolicyReject          -       -       0       i Or-ID: 10.255.255.11 C-LST: 10.255.255.1 
          RD: 10.255.255.11:1 ip-prefix 192.168.6.0/24
                                 PolicyReject          -       -       0       i Or-ID: 10.255.255.11 C-LST: 10.255.255.4 
 * >      RD: 10.255.255.12:1 ip-prefix 192.168.6.0/24
                                 -                     -       -       0       i
 * >Ec    RD: 10.255.255.1:1 ip-prefix 192.168.40.0/24
                                 10.255.255.1          -       5       0       i
 *  ec    RD: 10.255.255.1:1 ip-prefix 192.168.40.0/24
                                 10.255.255.1          -       5       0       i Or-ID: 10.255.255.1 C-LST: 10.255.255.4 10.255.255.1 172.16.255.2 
 * >Ec    RD: 10.255.255.4:1 ip-prefix 192.168.40.0/24
                                 10.255.255.4          -       5       0       i
 *  ec    RD: 10.255.255.4:1 ip-prefix 192.168.40.0/24
                                 10.255.255.4          -       5       0       i Or-ID: 10.255.255.4 C-LST: 10.255.255.1 10.255.255.4 172.16.255.0 
 * >Ec    RD: 10.255.255.10:1 ip-prefix 192.168.40.0/24
                                 10.255.255.10         -       100     0       i Or-ID: 10.255.255.10 C-LST: 10.255.255.4 
 *  ec    RD: 10.255.255.10:1 ip-prefix 192.168.40.0/24
                                 10.255.255.10         -       100     0       i Or-ID: 10.255.255.10 C-LST: 10.255.255.1 
```

## show ip security connection detail

```text
path3:
  Source address: 172.16.0.11, Destination address: 172.16.0.4
  State: established
  Uptime: 16 hours, 58 minutes, 40 seconds
  VRF: default
  Type: static
  Remote IP: 10.255.255.1
  Role: initiator
  Inbound SPI: 0xc9d81d:
    Request ID: 2, Mode: transport, Replay window size: 16384, Seq: 0x0
    Errors:
      Packets outside replay window: 0, Replay: 0, Integrity failed: 0
    Lifetime config:
      Soft byte limit: 3601917260999, Hard byte limit: 6442450944000
      Soft packet limit: 2085116766, Hard packet limit: 4000000000
      Soft time limit: 2844 secs, Hard time limit: 3600 secs
    Lifetime current:
      Current bytes: 3174882892
      Current packets: 2996323
      SA add time: Fri Mar 15 13:39:43 2024
      SA last use time: Fri Mar 15 13:44:04 2024
  Outbound SPI: 0xc8697c:
    Request ID: 2, Mode: transport, Replay window size: 0, Seq: 0x0
    Errors:
      Packets outside replay window: 0, Replay: 0, Integrity failed: 0
    Lifetime config:
      Soft byte limit: 3553890059249, Hard byte limit: 6442450944000
      Soft packet limit: 2690759917, Hard packet limit: 4000000000
      Soft time limit: 2763 secs, Hard time limit: 3600 secs
    Lifetime current:
      Current bytes: 3051307093
      Current packets: 5995796
      SA add time: Fri Mar 15 13:39:43 2024
      SA last use time: Fri Mar 15 13:44:04 2024
path4:
  Source address: 172.16.0.11, Destination address: 172.16.0.7
  State: established
  Uptime: 16 hours, 55 minutes, 30 seconds
  VRF: default
  Type: static
  Remote IP: 10.255.255.1
  Role: initiator
  Inbound SPI: 0xca6f33:
    Request ID: 1, Mode: transport, Replay window size: 16384, Seq: 0x0
    Errors:
      Packets outside replay window: 0, Replay: 0, Integrity failed: 0
    Lifetime config:
      Soft byte limit: 3624899382749, Hard byte limit: 6442450944000
      Soft packet limit: 2579766349, Hard packet limit: 4000000000
      Soft time limit: 2955 secs, Hard time limit: 3600 secs
    Lifetime current:
      Current bytes: 2979406784
      Current packets: 2812376
      SA add time: Fri Mar 15 13:36:57 2024
      SA last use time: Fri Mar 15 13:44:04 2024
  Outbound SPI: 0xc7ec1c:
    Request ID: 1, Mode: transport, Replay window size: 0, Seq: 0x0
    Errors:
      Packets outside replay window: 0, Replay: 0, Integrity failed: 0
    Lifetime config:
      Soft byte limit: 4761156512999, Hard byte limit: 6442450944000
      Soft packet limit: 2525471698, Hard packet limit: 4000000000
      Soft time limit: 2736 secs, Hard time limit: 3600 secs
    Lifetime current:
      Current bytes: 3578377861
      Current packets: 7032278
      SA add time: Fri Mar 15 13:36:57 2024
      SA last use time: Fri Mar 15 13:44:04 2024
path5:
  Source address: 172.16.0.11, Destination address: 172.16.0.1
  State: established
  Uptime: 16 hours, 40 minutes, 28 seconds
  VRF: default
  Type: dynamic
  Remote IP: 10.255.255.5
  Role: responder
  Packets in: 71440015, Packets out: 423434242
  Last known rekey count: 2
  Dynamic state: established
  Last established time: Fri Mar 15 13:05:58 2024
  DH crypto:
    Local rekey: 2, Peer rekey: 1, In SPI: 0xe1649337, Out SPI: 0xa0200676
    Local rekey: 1, Peer rekey: 0, In SPI: 0x98046581, Out SPI: 0xe914526e
    Local rekey: 1, Peer rekey: 2, In SPI: 0xe0d22099, Out SPI: 0xda7dc617
    Local rekey: 2, Peer rekey: 2, In SPI: 0xf3d01204, Out SPI: 0x304815fc
    Local rekey: 2, Peer rekey: 0, In SPI: 0x1335737a, Out SPI: 0xd30c11a6
    Local rekey: 1, Peer rekey: 1, In SPI: 0x6781658a, Out SPI: 0xd2451a05
  DH state:
    Local rekey: 2, Peer rekey: 2, DH rekey state: not rekeying, Role: not rekeying
  SA crypto:
    Local rekey: 2, Peer rekey: 2, In SPI 0x8a7cb04f, Out SPI 0xbf88d688
  SA rekey role: not rekeying
  SA state:
    SA type: ingress , SPI: 0xcb88f6e0
      Role: responder, SA rekey state: initial, Peer nonce type: init
      Add time: Fri Mar 15 13:04:49 2024, Packets: 3058989, Pair SPI: 0x967cd0a7
    SA type: egress , SPI: 0x967cd0a7
      Role: responder, SA rekey state: initial, Peer nonce type: init
      Add time: Fri Mar 15 13:04:57 2024, Packets: 18326378, Pair SPI: 0xcb88f6e0
  Inbound SPI: 0xcb88f6e0:
    Request ID: 6, Mode: transport, Replay window size: 0, Seq: 0x0
    Errors:
      Packets outside replay window: 0, Replay: 0, Integrity failed: 0
    Lifetime config:
      Soft byte limit: 4739935563825, Hard byte limit: 6442450944000
      Soft packet limit: 2962533029, Hard packet limit: 4000000000
      Soft time limit: 2552 secs, Hard time limit: 3600 secs
    Lifetime current:
      Current bytes: 3240426940
      Current packets: 3061459
      SA add time: Fri Mar 15 13:04:49 2024
      SA last use time: Fri Mar 15 13:44:04 2024
  Outbound SPI: 0x967cd0a7:
    Request ID: 6, Mode: transport, Replay window size: 0, Seq: 0x0
    Errors:
      Packets outside replay window: 0, Replay: 0, Integrity failed: 0
    Lifetime config:
      Soft byte limit: 4780605712500, Hard byte limit: 6442450944000
      Soft packet limit: 2959957988, Hard packet limit: 4000000000
      Soft time limit: 2557 secs, Hard time limit: 3600 secs
    Lifetime current:
      Current bytes: 9333552932
      Current packets: 18341180
      SA add time: Fri Mar 15 13:04:57 2024
      SA last use time: Fri Mar 15 13:44:04 2024
path6:
  Source address: 172.16.0.11, Destination address: 172.16.0.9
  State: established
  Uptime: 13 hours, 37 minutes, 38 seconds
  VRF: default
  Type: dynamic
  Remote IP: 10.255.255.11
  Role: initiator
  Packets in: 96712, Packets out: 205744
  Last known rekey count: 2
  Dynamic state: established
  Last established time: Fri Mar 15 13:06:58 2024
  DH crypto:
    Local rekey: 2, Peer rekey: 1, In SPI: 0x5a09bb66, Out SPI: 0xaabac3c6
    Local rekey: 1, Peer rekey: 0, In SPI: 0xdfa09aef, Out SPI: 0x31bf817c
    Local rekey: 1, Peer rekey: 2, In SPI: 0x919d7a64, Out SPI: 0xcf8468ac
    Local rekey: 2, Peer rekey: 2, In SPI: 0x19e03a15, Out SPI: 0x8b5834d1
    Local rekey: 2, Peer rekey: 0, In SPI: 0x52bde789, Out SPI: 0xb3e94756
    Local rekey: 1, Peer rekey: 1, In SPI: 0xb04614cb, Out SPI: 0xafe08e2
  DH state:
    Local rekey: 2, Peer rekey: 2, DH rekey state: not rekeying, Role: not rekeying
  SA crypto:
    Local rekey: 2, Peer rekey: 2, In SPI 0xa032bef3, Out SPI 0x447d27e2
  SA rekey role: not rekeying
  SA state:
    SA type: egress , SPI: 0xb432de4b
      Role: initiator, SA rekey state: initial, Peer nonce type: init
      Add time: Fri Mar 15 13:04:59 2024, Packets: 11100, Pair SPI: 0x587d473a
    SA type: ingress , SPI: 0x587d473a
      Role: initiator, SA rekey state: initial, Peer nonce type: init
      Add time: Fri Mar 15 13:04:54 2024, Packets: 5193, Pair SPI: 0xb432de4b
  Inbound SPI: 0x587d473a:
    Request ID: 9, Mode: transport, Replay window size: 0, Seq: 0x0
    Errors:
      Packets outside replay window: 0, Replay: 0, Integrity failed: 0
    Lifetime config:
      Soft byte limit: 4778444813475, Hard byte limit: 6442450944000
      Soft packet limit: 2952217749, Hard packet limit: 4000000000
      Soft time limit: 2578 secs, Hard time limit: 3600 secs
    Lifetime current:
      Current bytes: 790196
      Current packets: 5197
      SA add time: Fri Mar 15 13:04:54 2024
      SA last use time: Fri Mar 15 13:44:04 2024
  Outbound SPI: 0xb432de4b:
    Request ID: 9, Mode: transport, Replay window size: 0, Seq: 0x0
    Errors:
      Packets outside replay window: 0, Replay: 0, Integrity failed: 0
    Lifetime config:
      Soft byte limit: 4770008062350, Hard byte limit: 6442450944000
      Soft packet limit: 2937997596, Hard packet limit: 4000000000
      Soft time limit: 2571 secs, Hard time limit: 3600 secs
    Lifetime current:
      Current bytes: 1864112
      Current packets: 11108
      SA add time: Fri Mar 15 13:04:59 2024
      SA last use time: Fri Mar 15 13:44:04 2024
path7:
  Source address: 172.16.0.11, Destination address: 172.16.0.3
  State: established
  Uptime: 1 hour, 23 minutes, 34 seconds
  VRF: default
  Type: dynamic
  Remote IP: 10.255.255.6
  Role: responder
  Packets in: 6437623, Packets out: 12864880
  Last known rekey count: 0
  Dynamic state: established
  Last established time: Fri Mar 15 13:07:58 2024
  DH crypto:
    Local rekey: 2, Peer rekey: 1, In SPI: 0xd44e6442, Out SPI: 0xb5f12ddd
    Local rekey: 1, Peer rekey: 0, In SPI: 0x24aed630, Out SPI: 0xc26d0bc2
    Local rekey: 1, Peer rekey: 2, In SPI: 0x77452b11, Out SPI: 0x3fa069fd
    Local rekey: 2, Peer rekey: 2, In SPI: 0x790a51cc, Out SPI: 0x58c95997
    Local rekey: 2, Peer rekey: 0, In SPI: 0x8a0501cd, Out SPI: 0xc9c6e8b8
    Local rekey: 1, Peer rekey: 1, In SPI: 0xdd335acc, Out SPI: 0x3c393013
  DH state:
    Local rekey: 2, Peer rekey: 2, DH rekey state: not rekeying, Role: not rekeying
  SA crypto:
    Local rekey: 2, Peer rekey: 2, In SPI 0xa9d8a03f, Out SPI 0x4a61f234
  SA rekey role: not rekeying
  SA state:
    SA type: egress , SPI: 0xb7d8c097
      Role: responder, SA rekey state: initial, Peer nonce type: init
      Add time: Fri Mar 15 13:06:43 2024, Packets: 11701152, Pair SPI: 0x5861128d
    SA type: ingress , SPI: 0x5861128d
      Role: responder, SA rekey state: initial, Peer nonce type: init
      Add time: Fri Mar 15 13:06:42 2024, Packets: 5848257, Pair SPI: 0xb7d8c097
  Inbound SPI: 0x5861128d:
    Request ID: 8, Mode: transport, Replay window size: 0, Seq: 0x0
    Errors:
      Packets outside replay window: 0, Replay: 0, Integrity failed: 0
    Lifetime config:
      Soft byte limit: 4702367932575, Hard byte limit: 6442450944000
      Soft packet limit: 2936135411, Hard packet limit: 4000000000
      Soft time limit: 2539 secs, Hard time limit: 3600 secs
    Lifetime current:
      Current bytes: 6199865188
      Current packets: 5853193
      SA add time: Fri Mar 15 13:06:42 2024
      SA last use time: Fri Mar 15 13:44:04 2024
  Outbound SPI: 0xb7d8c097:
    Request ID: 8, Mode: transport, Replay window size: 0, Seq: 0x0
    Errors:
      Packets outside replay window: 0, Replay: 0, Integrity failed: 0
    Lifetime config:
      Soft byte limit: 4831184434350, Hard byte limit: 6442450944000
      Soft packet limit: 2903198874, Hard packet limit: 4000000000
      Soft time limit: 2593 secs, Hard time limit: 3600 secs
    Lifetime current:
      Current bytes: 5959009784
      Current packets: 11711023
      SA add time: Fri Mar 15 13:06:43 2024
      SA last use time: Fri Mar 15 13:44:04 2024
```

## show stun client translations detail

```text
Current System Time: Fri Mar 15 13:46:33 2024
Transaction ID 000000020affff0c00000000
Agent Name: dps
Source Address: 172.16.0.11:4500
Public Address: 172.16.0.11:4500
Number of Attributes: 3
Timeout Interval: 0:03:00
Last Refreshed: 0:02:34 ago
Attribute Type   Length Value           
---------------- ------ ----------------
PATH_GROUP            6 VZ_OFF          
VTEP_IP               4 10.255.255.12   
WAN_ID                4 2               

```

## show stun server bindings detail

```text
Current System Time: Fri Mar 15 13:46:34 2024
```

## show path-selection paths detail

```text
Peer: 10.255.255.1, Path group VZ_OFF
Path name: path3, static, Label: 3
Source: 172.16.0.11, Port: 4500, WAN ID: 2
Destination: 172.16.0.4, Port: 4500, WAN ID: 2886729732
Local interface: Ethernet1
Route state: IPsec established
Traffic class 0: active (16:56:05)
MTU: 8914

Peer: 10.255.255.4, Path group VZ_OFF
Path name: path4, static, Label: 4
Source: 172.16.0.11, Port: 4500, WAN ID: 2
Destination: 172.16.0.7, Port: 4500, WAN ID: 2886729735
Local interface: Ethernet1
Route state: IPsec established
Traffic class 0: active (16:52:56)
MTU: 8914

Peer: 10.255.255.5, Path group VZ_OFF
Path name: path5, dynamic, Label: 5
Source: 172.16.0.11, Port: 4500, WAN ID: 2
Destination: 172.16.0.1, Port: 4500, WAN ID: 1
Local interface: Ethernet1
Route state: IPsec established
Traffic class 0: active (16:37:55)
MTU: 8914

Peer: 10.255.255.6, Path group VZ_OFF
Path name: path7, dynamic, Label: 7
Source: 172.16.0.11, Port: 4500, WAN ID: 2
Destination: 172.16.0.3, Port: 4500, WAN ID: 1
Local interface: Ethernet1
Route state: IPsec established
Traffic class 0: active (1:23:20)
MTU: 8914

Peer: 10.255.255.11, Path group VZ_OFF
Path name: path6, dynamic, Label: 6
Source: 172.16.0.11, Port: 4500, WAN ID: 2
Destination: 172.16.0.9, Port: 4500, WAN ID: 2
Local interface: Ethernet1
Route state: IPsec established
Traffic class 0: active (13:35:33)
MTU: 1424

```

## show bgp neighbors

```text
BGP neighbor is 10.255.255.1, remote AS 65000, internal link
  BGP version 4, remote router ID 10.255.255.1, VRF default
  Inherits configuration from and member of peer-group PATHFINDER
  Last read 00:00:31, last write 00:00:15
  Hold time is 180, keepalive interval is 60 seconds
  Configured hold time is 180, keepalive interval is 60 seconds
  Effective minimum hold time is 3 seconds
  Send failure hold time is 0 seconds
  Hold timer is active, time left: 00:02:29
  Keepalive timer is active, time left: 00:00:40
  Connect timer is inactive
  Idle-restart timer is inactive
  BGP state is Established, up for 16:58:40
  Number of transitions to established: 1
  Last state was OpenConfirm
  Last event was Established
  Last sent socket-error:Connect (Network is unreachable), Last time 16:59:43
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
      Received 16:57:11
      Number of stale paths removed after graceful restart: 0
      Number of paths received before End-of-RIB: 14
    L2VPN EVPN End-of-RIB received: Yes
      Received 16:57:11
      Number of stale paths removed after graceful restart: 0
      Number of paths received before End-of-RIB: 34
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
    Updates:                        11     46962
    Keepalives:                   1192      1179
    Enhanced Route Refresh:          0         0
    Begin of Route Refresh:          0         0
    End of Route Refresh:            0         0
    Total messages:               1204     48142
  Prefix Statistics:
                                   Sent      Rcvd     Best Paths     Best ECMP Paths
    IPv4 Unicast:                     0         0              0                   0
    IPv4 Dps:                         2        22             22                   6
    IPv6 Unicast:                     0         0              0                   0
    EVPN:                             3        43             41                  20
  Configured maximum total number of routes is 12000
  Inbound updates dropped by reason:
    AS path loop detection: 0
    Cluster ID loop detection: 0
    Enforced First AS: 0
    Malformed MPBGP routes: 0
    Originator ID matches local router ID: 4
    Nexthop matches local IP address: 1
    Unexpected IPv6 nexthop for IPv4 routes: 0
  Inbound updates with attribute errors:
    Resulting in removal of all paths in update (treat as withdraw): 1
    Resulting in AFI/SAFI disable: 0
    Resulting in attribute ignore: 0
    Disabled AFI/SAFIs: None
    Last treat-as-withdraw attribute error: Nexthop is local address
    Last update with error received at: 13:37:40
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
Local AS is 65000, local router ID 10.255.255.12
TTL is 255
Local TCP address is 10.255.255.12, local port is 37635
Remote TCP address is 10.255.255.1, remote port is 179
Local next hop for next hop self:
  Dps: 10.255.255.12
  L2VPN EVPN: 10.255.255.12
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
    Round-trip Time (rtt/rtvar): 3.8ms/0.6ms
    Delayed Ack Timeout (ato): 40.0ms
    Congestion Window (cwnd): 10
    TCP Throughput: 30.74 Mbps
    Recv Round-trip Time (rcv_rtt): 451.4ms
    Advertised Recv Window (rcv_space): 64353

BGP neighbor is 10.255.255.4, remote AS 65000, internal link
  BGP version 4, remote router ID 10.255.255.4, VRF default
  Inherits configuration from and member of peer-group PATHFINDER
  Last read 00:00:02, last write 00:00:26
  Hold time is 180, keepalive interval is 60 seconds
  Configured hold time is 180, keepalive interval is 60 seconds
  Effective minimum hold time is 3 seconds
  Send failure hold time is 0 seconds
  Hold timer is active, time left: 00:02:58
  Keepalive timer is active, time left: 00:00:33
  Connect timer is inactive
  Idle-restart timer is inactive
  BGP state is Established, up for 16:55:25
  Number of transitions to established: 1
  Last state was OpenConfirm
  Last event was RecvUpdate
  Last sent socket-error:Connect (Network is unreachable), Last time 16:59:43
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
      Received 16:55:24
      Number of stale paths removed after graceful restart: 0
      Number of paths received before End-of-RIB: 22
    L2VPN EVPN End-of-RIB received: Yes
      Received 16:55:24
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
    Updates:                        10      9780
    Keepalives:                   1188      1180
    Enhanced Route Refresh:          0         0
    Begin of Route Refresh:          0         0
    End of Route Refresh:            0         0
    Total messages:               1199     10961
  Prefix Statistics:
                                   Sent      Rcvd     Best Paths     Best ECMP Paths
    IPv4 Unicast:                     0         0              0                   0
    IPv4 Dps:                         2        22             22                   6
    IPv6 Unicast:                     0         0              0                   0
    EVPN:                             3        43             41                  19
  Configured maximum total number of routes is 12000
  Inbound updates dropped by reason:
    AS path loop detection: 0
    Cluster ID loop detection: 0
    Enforced First AS: 0
    Malformed MPBGP routes: 0
    Originator ID matches local router ID: 4
    Nexthop matches local IP address: 3
    Unexpected IPv6 nexthop for IPv4 routes: 0
  Inbound updates with attribute errors:
    Resulting in removal of all paths in update (treat as withdraw): 3
    Resulting in AFI/SAFI disable: 0
    Resulting in attribute ignore: 0
    Disabled AFI/SAFIs: None
    Last treat-as-withdraw attribute error: Nexthop is local address
    Last update with error received at: 13:37:40
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
Local AS is 65000, local router ID 10.255.255.12
TTL is 255
Local TCP address is 10.255.255.12, local port is 43595
Remote TCP address is 10.255.255.4, remote port is 179
Local next hop for next hop self:
  Dps: 10.255.255.12
  L2VPN EVPN: 10.255.255.12
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
    Round-trip Time (rtt/rtvar): 4.1ms/1.1ms
    Delayed Ack Timeout (ato): 40.0ms
    Congestion Window (cwnd): 2
    TCP Throughput: 5.65 Mbps
    Recv Round-trip Time (rcv_rtt): 779.1ms
    Advertised Recv Window (rcv_space): 19137

```

## show bgp path-selection detail

```text
BGP routing table information for VRF default
Router identifier 10.255.255.12, local AS number 65000
Bgp routing table entry for ipv4Dps VTEP 10.255.255.5/32
 Paths: 4 available
  Local
    :: from 10.255.255.4 (10.255.255.4)
      Origin IGP, metric -, localpref 100, weight 0, received 16:40:31 ago, valid, internal
      Tunnel encapsulation attribute: Dynamic path selection
        Endpoint: 172.16.0.1, Path group name: VZ_OFF, WAN ID: 1, UDP port: 4500
  Local
    :: from 10.255.255.1 (10.255.255.1)
      Origin IGP, metric -, localpref 100, weight 0, received 16:40:31 ago, valid, internal
      Tunnel encapsulation attribute: Dynamic path selection
        Endpoint: 172.16.0.1, Path group name: VZ_OFF, WAN ID: 1, UDP port: 4500
  Local
    :: from 10.255.255.1 (10.255.255.1)
      Origin IGP, metric -, localpref 100, weight 0, received 16:40:30 ago, valid, internal
      Tunnel encapsulation attribute: Dynamic path selection
        Endpoint: 172.16.0.1, Path group name: VZ_OFF, WAN ID: 1, UDP port: 4500
  Local
    :: from 10.255.255.4 (10.255.255.4)
      Origin IGP, metric -, localpref 100, weight 0, received 16:40:30 ago, valid, internal
      Tunnel encapsulation attribute: Dynamic path selection
        Endpoint: 172.16.0.1, Path group name: VZ_OFF, WAN ID: 1, UDP port: 4500
Bgp routing table entry for ipv4Dps VTEP 10.255.255.6/32
 Paths: 4 available
  Local
    :: from 10.255.255.4 (10.255.255.4)
      Origin IGP, metric -, localpref 100, weight 0, received 13:40:01 ago, valid, internal
      Tunnel encapsulation attribute: Dynamic path selection
        Endpoint: 172.16.0.3, Path group name: VZ_OFF, WAN ID: 1, UDP port: 4500
  Local
    :: from 10.255.255.1 (10.255.255.1)
      Origin IGP, metric -, localpref 100, weight 0, received 13:40:01 ago, valid, internal
      Tunnel encapsulation attribute: Dynamic path selection
        Endpoint: 172.16.0.3, Path group name: VZ_OFF, WAN ID: 1, UDP port: 4500
  Local
    :: from 10.255.255.1 (10.255.255.1)
      Origin IGP, metric -, localpref 100, weight 0, received 13:39:58 ago, valid, internal
      Tunnel encapsulation attribute: Dynamic path selection
        Endpoint: 172.16.0.3, Path group name: VZ_OFF, WAN ID: 1, UDP port: 4500
  Local
    :: from 10.255.255.4 (10.255.255.4)
      Origin IGP, metric -, localpref 100, weight 0, received 13:39:58 ago, valid, internal
      Tunnel encapsulation attribute: Dynamic path selection
        Endpoint: 172.16.0.3, Path group name: VZ_OFF, WAN ID: 1, UDP port: 4500
Bgp routing table entry for ipv4Dps VTEP 10.255.255.8/32
 Paths: 4 available
  Local
    :: from 10.255.255.1 (10.255.255.1)
      Origin IGP, metric -, localpref 100, weight 0, received 16:57:22 ago, valid, internal
      Tunnel encapsulation attribute: Dynamic path selection
        Endpoint: 172.16.1.2, Path group name: VZ_NEAR, WAN ID: 1, UDP port: 4500
  Local
    :: from 10.255.255.1 (10.255.255.1)
      Origin IGP, metric -, localpref 100, weight 0, received 16:57:20 ago, valid, internal
      Tunnel encapsulation attribute: Dynamic path selection
        Endpoint: 172.16.1.2, Path group name: VZ_NEAR, WAN ID: 1, UDP port: 4500
  Local
    :: from 10.255.255.4 (10.255.255.4)
      Origin IGP, metric -, localpref 100, weight 0, received 16:55:25 ago, valid, internal
      Tunnel encapsulation attribute: Dynamic path selection
        Endpoint: 172.16.1.2, Path group name: VZ_NEAR, WAN ID: 1, UDP port: 4500
  Local
    :: from 10.255.255.4 (10.255.255.4)
      Origin IGP, metric -, localpref 100, weight 0, received 16:55:25 ago, valid, internal
      Tunnel encapsulation attribute: Dynamic path selection
        Endpoint: 172.16.1.2, Path group name: VZ_NEAR, WAN ID: 1, UDP port: 4500
Bgp routing table entry for ipv4Dps VTEP 10.255.255.10/32
 Paths: 4 available
  Local
    :: from 10.255.255.1 (10.255.255.1)
      Origin IGP, metric -, localpref 100, weight 0, received 15:10:19 ago, valid, internal
      Tunnel encapsulation attribute: Dynamic path selection
        Endpoint: 172.16.1.7, Path group name: VZ_NEAR, WAN ID: 1, UDP port: 4500
  Local
    :: from 10.255.255.4 (10.255.255.4)
      Origin IGP, metric -, localpref 100, weight 0, received 15:10:19 ago, valid, internal
      Tunnel encapsulation attribute: Dynamic path selection
        Endpoint: 172.16.1.7, Path group name: VZ_NEAR, WAN ID: 1, UDP port: 4500
  Local
    :: from 10.255.255.4 (10.255.255.4)
      Origin IGP, metric -, localpref 100, weight 0, received 15:10:14 ago, valid, internal
      Tunnel encapsulation attribute: Dynamic path selection
        Endpoint: 172.16.1.7, Path group name: VZ_NEAR, WAN ID: 1, UDP port: 4500
  Local
    :: from 10.255.255.1 (10.255.255.1)
      Origin IGP, metric -, localpref 100, weight 0, received 15:10:14 ago, valid, internal
      Tunnel encapsulation attribute: Dynamic path selection
        Endpoint: 172.16.1.7, Path group name: VZ_NEAR, WAN ID: 1, UDP port: 4500
Bgp routing table entry for ipv4Dps VTEP 10.255.255.11/32
 Paths: 4 available
  Local
    :: from 10.255.255.4 (10.255.255.4)
      Origin IGP, metric -, localpref 100, weight 0, received 13:37:41 ago, valid, internal
      Tunnel encapsulation attribute: Dynamic path selection
        Endpoint: 172.16.0.9, Path group name: VZ_OFF, WAN ID: 2, UDP port: 4500
  Local
    :: from 10.255.255.1 (10.255.255.1)
      Origin IGP, metric -, localpref 100, weight 0, received 13:37:41 ago, valid, internal
      Tunnel encapsulation attribute: Dynamic path selection
        Endpoint: 172.16.0.9, Path group name: VZ_OFF, WAN ID: 2, UDP port: 4500
  Local
    :: from 10.255.255.1 (10.255.255.1)
      Origin IGP, metric -, localpref 100, weight 0, received 13:37:40 ago, valid, internal
      Tunnel encapsulation attribute: Dynamic path selection
        Endpoint: 172.16.0.9, Path group name: VZ_OFF, WAN ID: 2, UDP port: 4500
  Local
    :: from 10.255.255.4 (10.255.255.4)
      Origin IGP, metric -, localpref 100, weight 0, received 13:37:40 ago, valid, internal
      Tunnel encapsulation attribute: Dynamic path selection
        Endpoint: 172.16.0.9, Path group name: VZ_OFF, WAN ID: 2, UDP port: 4500
Bgp routing table entry for ipv4Dps VTEP 10.255.255.12/32
 Paths: 1 available
  Local
    - from - (0.0.0.0)
      Origin IGP, metric -, localpref -, weight 0, received 16:59:06 ago, valid, local
      Tunnel encapsulation attribute: Dynamic path selection
        Endpoint: 172.16.0.11, Path group name: VZ_OFF, WAN ID: 2, UDP port: 4500
Bgp routing table entry for ipv4Ipsec VTEP 10.255.255.1/32
 Paths: 2 available
  Local
    :: from 10.255.255.1 (10.255.255.1)
      Origin IGP, metric -, localpref 100, weight 0, received 16:58:40 ago, valid, internal
      Tunnel encapsulation attribute: IP security
        Initial contact: false, Rekey counter: 0, Nonce length: 32
        DH group: 14, DH key length: 256
        Encryption algo: aes256, Authentication algo: sha256
  Local
    :: from 10.255.255.4 (10.255.255.4)
      Origin IGP, metric -, localpref 100, weight 0, received 16:55:25 ago, valid, internal
      Tunnel encapsulation attribute: IP security
        Initial contact: false, Rekey counter: 0, Nonce length: 32
        DH group: 14, DH key length: 256
        Encryption algo: aes256, Authentication algo: sha256
Bgp routing table entry for ipv4Ipsec VTEP 10.255.255.4/32
 Paths: 2 available
  Local
    :: from 10.255.255.1 (10.255.255.1)
      Origin IGP, metric -, localpref 100, weight 0, received 16:58:40 ago, valid, internal
      Tunnel encapsulation attribute: IP security
        Initial contact: false, Rekey counter: 0, Nonce length: 32
        DH group: 14, DH key length: 256
        Encryption algo: aes256, Authentication algo: sha256
  Local
    :: from 10.255.255.4 (10.255.255.4)
      Origin IGP, metric -, localpref 100, weight 0, received 16:55:25 ago, valid, internal
      Tunnel encapsulation attribute: IP security
        Initial contact: false, Rekey counter: 0, Nonce length: 32
        DH group: 14, DH key length: 256
        Encryption algo: aes256, Authentication algo: sha256
Bgp routing table entry for ipv4Ipsec VTEP 10.255.255.5/32
 Paths: 4 available
  Local
    :: from 10.255.255.4 (10.255.255.4)
      Origin IGP, metric -, localpref 100, weight 0, received 01:32:34 ago, valid, internal
      Tunnel encapsulation attribute: IP security
        Initial contact: false, Rekey counter: 2, Nonce length: 32
        DH group: 14, DH key length: 256
        Encryption algo: aes256, Authentication algo: sha256
  Local
    :: from 10.255.255.1 (10.255.255.1)
      Origin IGP, metric -, localpref 100, weight 0, received 01:32:34 ago, valid, internal
      Tunnel encapsulation attribute: IP security
        Initial contact: false, Rekey counter: 2, Nonce length: 32
        DH group: 14, DH key length: 256
        Encryption algo: aes256, Authentication algo: sha256
  Local
    :: from 10.255.255.4 (10.255.255.4)
      Origin IGP, metric -, localpref 100, weight 0, received 01:32:34 ago, valid, internal
      Tunnel encapsulation attribute: IP security
        Initial contact: false, Rekey counter: 2, Nonce length: 32
        DH group: 14, DH key length: 256
        Encryption algo: aes256, Authentication algo: sha256
  Local
    :: from 10.255.255.1 (10.255.255.1)
      Origin IGP, metric -, localpref 100, weight 0, received 01:32:34 ago, valid, internal
      Tunnel encapsulation attribute: IP security
        Initial contact: false, Rekey counter: 2, Nonce length: 32
        DH group: 14, DH key length: 256
        Encryption algo: aes256, Authentication algo: sha256
Bgp routing table entry for ipv4Ipsec VTEP 10.255.255.6/32
 Paths: 4 available
  Local
    :: from 10.255.255.1 (10.255.255.1)
      Origin IGP, metric -, localpref 100, weight 0, received 01:29:27 ago, valid, internal
      Tunnel encapsulation attribute: IP security
        Initial contact: false, Rekey counter: 2, Nonce length: 32
        DH group: 14, DH key length: 256
        Encryption algo: aes256, Authentication algo: sha256
  Local
    :: from 10.255.255.4 (10.255.255.4)
      Origin IGP, metric -, localpref 100, weight 0, received 01:29:27 ago, valid, internal
      Tunnel encapsulation attribute: IP security
        Initial contact: false, Rekey counter: 2, Nonce length: 32
        DH group: 14, DH key length: 256
        Encryption algo: aes256, Authentication algo: sha256
  Local
    :: from 10.255.255.4 (10.255.255.4)
      Origin IGP, metric -, localpref 100, weight 0, received 01:29:27 ago, valid, internal
      Tunnel encapsulation attribute: IP security
        Initial contact: false, Rekey counter: 2, Nonce length: 32
        DH group: 14, DH key length: 256
        Encryption algo: aes256, Authentication algo: sha256
  Local
    :: from 10.255.255.1 (10.255.255.1)
      Origin IGP, metric -, localpref 100, weight 0, received 01:29:27 ago, valid, internal
      Tunnel encapsulation attribute: IP security
        Initial contact: false, Rekey counter: 2, Nonce length: 32
        DH group: 14, DH key length: 256
        Encryption algo: aes256, Authentication algo: sha256
Bgp routing table entry for ipv4Ipsec VTEP 10.255.255.8/32
 Paths: 4 available
  Local
    :: from 10.255.255.4 (10.255.255.4)
      Origin IGP, metric -, localpref 100, weight 0, received 01:31:28 ago, valid, internal
      Tunnel encapsulation attribute: IP security
        Initial contact: false, Rekey counter: 2, Nonce length: 32
        DH group: 14, DH key length: 256
        Encryption algo: aes256, Authentication algo: sha256
  Local
    :: from 10.255.255.1 (10.255.255.1)
      Origin IGP, metric -, localpref 100, weight 0, received 01:31:28 ago, valid, internal
      Tunnel encapsulation attribute: IP security
        Initial contact: false, Rekey counter: 2, Nonce length: 32
        DH group: 14, DH key length: 256
        Encryption algo: aes256, Authentication algo: sha256
  Local
    :: from 10.255.255.1 (10.255.255.1)
      Origin IGP, metric -, localpref 100, weight 0, received 01:31:28 ago, valid, internal
      Tunnel encapsulation attribute: IP security
        Initial contact: false, Rekey counter: 2, Nonce length: 32
        DH group: 14, DH key length: 256
        Encryption algo: aes256, Authentication algo: sha256
  Local
    :: from 10.255.255.4 (10.255.255.4)
      Origin IGP, metric -, localpref 100, weight 0, received 01:31:28 ago, valid, internal
      Tunnel encapsulation attribute: IP security
        Initial contact: false, Rekey counter: 2, Nonce length: 32
        DH group: 14, DH key length: 256
        Encryption algo: aes256, Authentication algo: sha256
Bgp routing table entry for ipv4Ipsec VTEP 10.255.255.10/32
 Paths: 4 available
  Local
    :: from 10.255.255.1 (10.255.255.1)
      Origin IGP, metric -, localpref 100, weight 0, received 01:34:41 ago, valid, internal
      Tunnel encapsulation attribute: IP security
        Initial contact: false, Rekey counter: 2, Nonce length: 32
        DH group: 14, DH key length: 256
        Encryption algo: aes256, Authentication algo: sha256
  Local
    :: from 10.255.255.4 (10.255.255.4)
      Origin IGP, metric -, localpref 100, weight 0, received 01:34:41 ago, valid, internal
      Tunnel encapsulation attribute: IP security
        Initial contact: false, Rekey counter: 2, Nonce length: 32
        DH group: 14, DH key length: 256
        Encryption algo: aes256, Authentication algo: sha256
  Local
    :: from 10.255.255.4 (10.255.255.4)
      Origin IGP, metric -, localpref 100, weight 0, received 01:34:41 ago, valid, internal
      Tunnel encapsulation attribute: IP security
        Initial contact: false, Rekey counter: 2, Nonce length: 32
        DH group: 14, DH key length: 256
        Encryption algo: aes256, Authentication algo: sha256
  Local
    :: from 10.255.255.1 (10.255.255.1)
      Origin IGP, metric -, localpref 100, weight 0, received 01:34:41 ago, valid, internal
      Tunnel encapsulation attribute: IP security
        Initial contact: false, Rekey counter: 2, Nonce length: 32
        DH group: 14, DH key length: 256
        Encryption algo: aes256, Authentication algo: sha256
Bgp routing table entry for ipv4Ipsec VTEP 10.255.255.11/32
 Paths: 4 available
  Local
    :: from 10.255.255.4 (10.255.255.4)
      Origin IGP, metric -, localpref 100, weight 0, received 01:32:30 ago, valid, internal
      Tunnel encapsulation attribute: IP security
        Initial contact: false, Rekey counter: 2, Nonce length: 32
        DH group: 14, DH key length: 256
        Encryption algo: aes256, Authentication algo: sha256
  Local
    :: from 10.255.255.1 (10.255.255.1)
      Origin IGP, metric -, localpref 100, weight 0, received 01:32:30 ago, valid, internal
      Tunnel encapsulation attribute: IP security
        Initial contact: false, Rekey counter: 2, Nonce length: 32
        DH group: 14, DH key length: 256
        Encryption algo: aes256, Authentication algo: sha256
  Local
    :: from 10.255.255.1 (10.255.255.1)
      Origin IGP, metric -, localpref 100, weight 0, received 01:32:30 ago, valid, internal
      Tunnel encapsulation attribute: IP security
        Initial contact: false, Rekey counter: 2, Nonce length: 32
        DH group: 14, DH key length: 256
        Encryption algo: aes256, Authentication algo: sha256
  Local
    :: from 10.255.255.4 (10.255.255.4)
      Origin IGP, metric -, localpref 100, weight 0, received 01:32:30 ago, valid, internal
      Tunnel encapsulation attribute: IP security
        Initial contact: false, Rekey counter: 2, Nonce length: 32
        DH group: 14, DH key length: 256
        Encryption algo: aes256, Authentication algo: sha256
Bgp routing table entry for ipv4Ipsec VTEP 10.255.255.12/32
 Paths: 1 available
  Local
    - from - (0.0.0.0)
      Origin IGP, metric -, localpref -, weight 0, received 16:59:36 ago, valid, local
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
>C    10.255.255.12/32 [0 pref/0 metric] updated 16:59:54 ago
         via Loopback0, directly connected
>C    172.16.0.10/31 [0 pref/0 metric] updated 16:59:43 ago
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
>S    0.0.0.0/0 [1 pref/0 metric] updated 16:59:43 ago
         via 172.16.0.10 [0 pref/0 metric] type ipv4
            via 172.16.0.10, Ethernet1
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
>P    0.0.0.0/8 [1 pref/0 metric] updated 16:59:52 ago
         via Null0, directly connected [NF]
>P    10.255.255.1/32 [1 pref/0 metric] updated 16:59:37 ago
         via 10.255.255.1, Dps1
>P    10.255.255.4/32 [1 pref/0 metric] updated 16:59:37 ago
         via 10.255.255.4, Dps1
>P    10.255.255.5/32 [1 pref/0 metric] updated 16:40:32 ago
         via 10.255.255.5, Dps1
>P    10.255.255.6/32 [1 pref/0 metric] updated 13:40:02 ago
         via 10.255.255.6, Dps1
>P    10.255.255.11/32 [1 pref/0 metric] updated 13:37:42 ago
         via 10.255.255.11, Dps1
>P    127.0.0.0/8 [1 pref/0 metric] updated 16:59:52 ago
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
>P    ::/96 [1 pref/0 metric] updated 16:59:39 ago
         via Null0, directly connected [NF]
>P    ::ffff:127.0.0.0/104 [1 pref/0 metric] updated 16:59:39 ago
         via :: [1 pref/1 metric] type ipv6
            via , directly connected
>P    fe80::/10 [1 pref/0 metric] updated 16:59:39 ago
```

