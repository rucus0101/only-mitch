# Test results for CBL386

## show version

```text
Arista AWE-5310-F
Hardware version: 00.03
Serial number: WTW22500039
Hardware MAC address: ec8a.4804.2153
System MAC address: ec8a.4804.2153

Software image version: 4.31.2F-36028628.gangesA1rel (engineering build)
Architecture: x86_64
Internal build version: 4.31.2F-36028628.gangesA1rel
Internal build ID: da266e39-7d88-46c7-a67b-d8bbbe31ee51
Image format version: 3.0
Image optimization: Default

Uptime: 2 days, 8 hours and 32 minutes
Total memory: 32470188 kB
Free memory: 21170688 kB

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
           via VTEP 10.255.255.1 VNI 201 router-mac ec:8a:48:04:f5:30
           via VTEP 10.255.255.4 VNI 201 router-mac ec:8a:48:04:ff:5b
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
           via 10.0.255.1, Ethernet1/5
 B I      10.255.254.2/32 [20/0]
           via VTEP 10.255.255.1 VNI 201 router-mac ec:8a:48:04:f5:30
 B I      10.255.254.3/32 [20/0]
           via VTEP 10.255.255.8 VNI 201 router-mac ec:8a:48:04:2c:53
 B I      10.255.254.4/32 [20/0]
           via VTEP 10.255.255.11 VNI 201 router-mac 00:0c:29:ba:2d:5e
           via VTEP 10.255.255.12 VNI 201 router-mac 00:0c:29:78:c5:2d
 B I      10.255.254.5/32 [20/0]
           via VTEP 10.255.255.1 VNI 201 router-mac ec:8a:48:04:f5:30
           via VTEP 10.255.255.4 VNI 201 router-mac ec:8a:48:04:ff:5b
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
           via VTEP 10.255.255.1 VNI 201 router-mac ec:8a:48:04:f5:30
           via VTEP 10.255.255.4 VNI 201 router-mac ec:8a:48:04:ff:5b

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
                                 10.255.255.6          -       100     0       i Or-ID: 10.255.255.6 C-LST: 10.255.255.1 
 * >Ec    RD: 10.255.255.1:1 ip-prefix 10.1.255.0/31
                                 10.255.255.1          -       100     0       i Or-ID: 10.255.255.1 C-LST: 10.255.255.4 
 *  ec    RD: 10.255.255.1:1 ip-prefix 10.1.255.0/31
                                 10.255.255.1          -       100     0       i
 * >      RD: 10.255.255.1:1 ip-prefix 10.1.255.2/31
                                 10.255.255.1          -       5       0       i
 * >Ec    RD: 10.255.255.4:1 ip-prefix 10.1.255.2/31
                                 10.255.255.4          -       5       0       i
 *  ec    RD: 10.255.255.4:1 ip-prefix 10.1.255.2/31
                                 10.255.255.4          -       5       0       i Or-ID: 10.255.255.4 C-LST: 10.255.255.1 10.255.255.4 172.16.255.0 
 * >      RD: 10.255.255.1:1 ip-prefix 10.2.255.0/31
                                 10.255.255.1          -       5       0       i Or-ID: 10.255.255.7 C-LST: 10.255.255.1 172.16.255.2 10.255.255.3 
 * >Ec    RD: 10.255.255.4:1 ip-prefix 10.2.255.0/31
                                 10.255.255.4          -       5       0       i
 *  ec    RD: 10.255.255.4:1 ip-prefix 10.2.255.0/31
                                 10.255.255.4          -       5       0       i Or-ID: 10.255.255.4 C-LST: 10.255.255.1 10.255.255.4 172.16.255.0 
 * >Ec    RD: 10.255.255.7:1 ip-prefix 10.2.255.2/31
                                 10.255.255.8          -       100     0       i Or-ID: 10.255.255.8 C-LST: 10.255.255.4 
 *  ec    RD: 10.255.255.7:1 ip-prefix 10.2.255.2/31
                                 10.255.255.8          -       100     0       i Or-ID: 10.255.255.8 C-LST: 10.255.255.1 
 * >      RD: 10.255.255.1:1 ip-prefix 10.4.255.0/31
                                 10.255.255.1          -       5       0       i Or-ID: 10.255.255.9 C-LST: 10.255.255.1 172.16.255.2 10.255.255.3 
 * >Ec    RD: 10.255.255.4:1 ip-prefix 10.4.255.0/31
                                 10.255.255.4          -       5       0       i
 *  ec    RD: 10.255.255.4:1 ip-prefix 10.4.255.0/31
                                 10.255.255.4          -       5       0       i Or-ID: 10.255.255.4 C-LST: 10.255.255.1 10.255.255.4 172.16.255.0 
 * >      RD: 10.255.255.1:1 ip-prefix 10.4.255.2/31
                                 10.255.255.1          -       5       0       i Or-ID: 10.255.255.9 C-LST: 10.255.255.1 172.16.255.2 10.255.255.3 
 * >Ec    RD: 10.255.255.4:1 ip-prefix 10.4.255.2/31
                                 10.255.255.4          -       5       0       i
 *  ec    RD: 10.255.255.4:1 ip-prefix 10.4.255.2/31
                                 10.255.255.4          -       5       0       i Or-ID: 10.255.255.4 C-LST: 10.255.255.1 10.255.255.4 172.16.255.0 
 * >      RD: 10.255.255.1:1 ip-prefix 10.5.255.0/31
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
                                 10.255.255.11         -       100     0       i Or-ID: 10.255.255.11 C-LST: 10.255.255.1 
 * >Ec    RD: 10.255.255.12:1 ip-prefix 10.6.255.2/31
                                 10.255.255.12         -       100     0       i Or-ID: 10.255.255.12 C-LST: 10.255.255.4 
 *  ec    RD: 10.255.255.12:1 ip-prefix 10.6.255.2/31
                                 10.255.255.12         -       100     0       i Or-ID: 10.255.255.12 C-LST: 10.255.255.1 10.255.255.4 
 * >      RD: 10.255.255.5:1 ip-prefix 10.255.254.1/32
                                 -                     -       -       0       i
          RD: 10.255.255.6:1 ip-prefix 10.255.254.1/32
                                 PolicyReject          -       -       0       i Or-ID: 10.255.255.6 C-LST: 10.255.255.4 
          RD: 10.255.255.6:1 ip-prefix 10.255.254.1/32
                                 PolicyReject          -       -       0       i Or-ID: 10.255.255.6 C-LST: 10.255.255.1 
 * >Ec    RD: 10.255.255.1:1 ip-prefix 10.255.254.2/32
                                 10.255.255.1          -       100     0       i Or-ID: 10.255.255.1 C-LST: 10.255.255.4 
 *  ec    RD: 10.255.255.1:1 ip-prefix 10.255.254.2/32
                                 10.255.255.1          -       100     0       i
 * >      RD: 10.255.255.4:1 ip-prefix 10.255.254.2/32
                                 10.255.255.4          -       5       0       i
 * >      RD: 10.255.255.1:1 ip-prefix 10.255.254.3/32
                                 10.255.255.1          -       5       0       i Or-ID: 10.255.255.7 C-LST: 10.255.255.1 172.16.255.2 10.255.255.3 
 * >Ec    RD: 10.255.255.4:1 ip-prefix 10.255.254.3/32
                                 10.255.255.4          -       5       0       i
 *  ec    RD: 10.255.255.4:1 ip-prefix 10.255.254.3/32
                                 10.255.255.4          -       5       0       i Or-ID: 10.255.255.4 C-LST: 10.255.255.1 10.255.255.4 172.16.255.0 
 * >Ec    RD: 10.255.255.7:1 ip-prefix 10.255.254.3/32
                                 10.255.255.8          -       100     0       i Or-ID: 10.255.255.8 C-LST: 10.255.255.4 
 *  ec    RD: 10.255.255.7:1 ip-prefix 10.255.254.3/32
                                 10.255.255.8          -       100     0       i Or-ID: 10.255.255.8 C-LST: 10.255.255.1 
 * >Ec    RD: 10.255.255.11:1 ip-prefix 10.255.254.4/32
                                 10.255.255.11         -       100     0       i Or-ID: 10.255.255.11 C-LST: 10.255.255.4 
 *  ec    RD: 10.255.255.11:1 ip-prefix 10.255.254.4/32
                                 10.255.255.11         -       100     0       i Or-ID: 10.255.255.11 C-LST: 10.255.255.1 
 * >Ec    RD: 10.255.255.12:1 ip-prefix 10.255.254.4/32
                                 10.255.255.12         -       100     0       i Or-ID: 10.255.255.12 C-LST: 10.255.255.4 
 *  ec    RD: 10.255.255.12:1 ip-prefix 10.255.254.4/32
                                 10.255.255.12         -       100     0       i Or-ID: 10.255.255.12 C-LST: 10.255.255.1 10.255.255.4 
 * >      RD: 10.255.255.1:1 ip-prefix 10.255.254.5/32
                                 10.255.255.1          -       5       0       i Or-ID: 10.255.255.9 C-LST: 10.255.255.1 172.16.255.2 10.255.255.3 
 * >Ec    RD: 10.255.255.4:1 ip-prefix 10.255.254.5/32
                                 10.255.255.4          -       5       0       i
 *  ec    RD: 10.255.255.4:1 ip-prefix 10.255.254.5/32
                                 10.255.255.4          -       5       0       i Or-ID: 10.255.255.4 C-LST: 10.255.255.1 10.255.255.4 172.16.255.0 
 * >      RD: 10.255.255.1:1 ip-prefix 10.255.254.6/32
                                 10.255.255.1          -       5       0       i
 * >Ec    RD: 10.255.255.4:1 ip-prefix 10.255.254.6/32
                                 10.255.255.4          -       100     0       i
 *  ec    RD: 10.255.255.4:1 ip-prefix 10.255.254.6/32
                                 10.255.255.4          -       100     0       i Or-ID: 10.255.255.4 C-LST: 10.255.255.1 
 * >      RD: 10.255.255.1:1 ip-prefix 172.16.255.0/31
                                 10.255.255.1          -       5       0       i
 * >Ec    RD: 10.255.255.4:1 ip-prefix 172.16.255.0/31
                                 10.255.255.4          -       100     0       i
 *  ec    RD: 10.255.255.4:1 ip-prefix 172.16.255.0/31
                                 10.255.255.4          -       100     0       i Or-ID: 10.255.255.4 C-LST: 10.255.255.1 
 * >Ec    RD: 10.255.255.1:1 ip-prefix 172.16.255.2/31
                                 10.255.255.1          -       100     0       i
 *  ec    RD: 10.255.255.1:1 ip-prefix 172.16.255.2/31
                                 10.255.255.1          -       100     0       i Or-ID: 10.255.255.1 C-LST: 10.255.255.4 
 * >Ec    RD: 10.255.255.4:1 ip-prefix 172.16.255.2/31
                                 10.255.255.4          -       5       0       i
 *  ec    RD: 10.255.255.4:1 ip-prefix 172.16.255.2/31
                                 10.255.255.4          -       5       0       i Or-ID: 10.255.255.4 C-LST: 10.255.255.1 10.255.255.4 172.16.255.0 
 * >      RD: 10.255.255.5:1 ip-prefix 192.168.0.0/24
                                 -                     -       -       0       i
          RD: 10.255.255.6:1 ip-prefix 192.168.0.0/24
                                 PolicyReject          -       -       0       i Or-ID: 10.255.255.6 C-LST: 10.255.255.4 
          RD: 10.255.255.6:1 ip-prefix 192.168.0.0/24
                                 PolicyReject          -       -       0       i Or-ID: 10.255.255.6 C-LST: 10.255.255.1 
 * >Ec    RD: 10.255.255.1:1 ip-prefix 192.168.1.0/24
                                 10.255.255.1          -       100     0       i Or-ID: 10.255.255.1 C-LST: 10.255.255.4 
 *  ec    RD: 10.255.255.1:1 ip-prefix 192.168.1.0/24
                                 10.255.255.1          -       100     0       i
 * >      RD: 10.255.255.4:1 ip-prefix 192.168.1.0/24
                                 10.255.255.4          -       5       0       i
 * >      RD: 10.255.255.1:1 ip-prefix 192.168.3.0/24
                                 10.255.255.1          -       5       0       i Or-ID: 10.255.255.7 C-LST: 10.255.255.1 172.16.255.2 10.255.255.3 
 * >Ec    RD: 10.255.255.4:1 ip-prefix 192.168.3.0/24
                                 10.255.255.4          -       5       0       i
 *  ec    RD: 10.255.255.4:1 ip-prefix 192.168.3.0/24
                                 10.255.255.4          -       5       0       i Or-ID: 10.255.255.4 C-LST: 10.255.255.1 10.255.255.4 172.16.255.0 
 * >Ec    RD: 10.255.255.7:1 ip-prefix 192.168.3.0/24
                                 10.255.255.8          -       100     0       i Or-ID: 10.255.255.8 C-LST: 10.255.255.4 
 *  ec    RD: 10.255.255.7:1 ip-prefix 192.168.3.0/24
                                 10.255.255.8          -       100     0       i Or-ID: 10.255.255.8 C-LST: 10.255.255.1 
 * >      RD: 10.255.255.1:1 ip-prefix 192.168.5.0/24
                                 10.255.255.1          -       5       0       i
 * >Ec    RD: 10.255.255.4:1 ip-prefix 192.168.5.0/24
                                 10.255.255.4          -       100     0       i
 *  ec    RD: 10.255.255.4:1 ip-prefix 192.168.5.0/24
                                 10.255.255.4          -       100     0       i Or-ID: 10.255.255.4 C-LST: 10.255.255.1 
 * >Ec    RD: 10.255.255.11:1 ip-prefix 192.168.6.0/24
                                 10.255.255.11         -       100     0       i Or-ID: 10.255.255.11 C-LST: 10.255.255.4 
 *  ec    RD: 10.255.255.11:1 ip-prefix 192.168.6.0/24
                                 10.255.255.11         -       100     0       i Or-ID: 10.255.255.11 C-LST: 10.255.255.1 
 * >Ec    RD: 10.255.255.12:1 ip-prefix 192.168.6.0/24
                                 10.255.255.12         -       100     0       i Or-ID: 10.255.255.12 C-LST: 10.255.255.4 
 *  ec    RD: 10.255.255.12:1 ip-prefix 192.168.6.0/24
                                 10.255.255.12         -       100     0       i Or-ID: 10.255.255.12 C-LST: 10.255.255.1 10.255.255.4 
 * >      RD: 10.255.255.1:1 ip-prefix 192.168.40.0/24
                                 10.255.255.1          -       5       0       i Or-ID: 10.255.255.9 C-LST: 10.255.255.1 172.16.255.2 10.255.255.3 
 * >Ec    RD: 10.255.255.4:1 ip-prefix 192.168.40.0/24
                                 10.255.255.4          -       5       0       i
 *  ec    RD: 10.255.255.4:1 ip-prefix 192.168.40.0/24
                                 10.255.255.4          -       5       0       i Or-ID: 10.255.255.4 C-LST: 10.255.255.1 10.255.255.4 172.16.255.0 
```

## show ip security connection detail

```text
path1:
  Source address: 172.16.0.1, Destination address: 172.16.0.4
  State: established
  Uptime: 2 days, 6 hours, 54 minutes, 50 seconds
  VRF: default
  Type: static
  Remote IP: 10.255.255.12
  Role: initiator
  Inbound SPI: 0xcac3eb:
    Request ID: 1, Mode: transport, Replay window size: 16384, Seq: 0x0
    Errors:
      Packets outside replay window: 0, Replay: 0, Integrity failed: 0
    Lifetime config:
      Soft byte limit: 3871411894499, Hard byte limit: 6442450944000
      Soft packet limit: 2877126393, Hard packet limit: 4000000000
      Soft time limit: 2919 secs, Hard time limit: 3600 secs
    Lifetime current:
      Current bytes: 550688
      Current packets: 1580
      SA add time: Sun Mar 17 17:27:50 2024
      SA last use time: Sun Mar 17 17:34:22 2024
  Outbound SPI: 0xcad9e5:
    Request ID: 1, Mode: transport, Replay window size: 0, Seq: 0x0
    Errors:
      Packets outside replay window: 0, Replay: 0, Integrity failed: 0
    Lifetime config:
      Soft byte limit: 3982405895999, Hard byte limit: 6442450944000
      Soft packet limit: 2069166873, Hard packet limit: 4000000000
      Soft time limit: 2898 secs, Hard time limit: 3600 secs
    Lifetime current:
      Current bytes: 904551
      Current packets: 1630
      SA add time: Sun Mar 17 17:27:50 2024
      SA last use time: -
path3:
  Source address: 172.16.0.1, Destination address: 172.16.0.3
  State: established
  Uptime: 1 day, 9 hours, 11 minutes, 1 second
  VRF: default
  Type: dynamic
  Remote IP: 10.255.255.6
  Role: initiator
  Packets in: 253751, Packets out: 263712
  Last known rekey count: 7
  Dynamic state: established
  Last established time: Sun Mar 17 17:29:45 2024
  DH crypto:
    Local rekey: 7, Peer rekey: 5, In SPI: 0xaa70f0b9, Out SPI: 0x3af1647a
    Local rekey: 6, Peer rekey: 4, In SPI: 0x429fee12, Out SPI: 0x3db0868f
    Local rekey: 7, Peer rekey: 7, In SPI: 0xde82d115, Out SPI: 0x510aeb88
    Local rekey: 6, Peer rekey: 6, In SPI: 0x2d671cdc, Out SPI: 0xf4d20600
    Local rekey: 7, Peer rekey: 6, In SPI: 0x72851a56, Out SPI: 0xa76bf4a0
    Local rekey: 6, Peer rekey: 5, In SPI: 0x7a6a1c41, Out SPI: 0xa87f1efb
  DH state:
    Local rekey: 7, Peer rekey: 7, DH rekey state: not rekeying, Role: not rekeying
  SA crypto:
    Local rekey: 7, Peer rekey: 7, In SPI 0xd36d305c, Out SPI 0xe85afa33
  SA rekey role: not rekeying
  SA state:
    SA type: egress , SPI: 0xd76d50b4
      Role: initiator, SA rekey state: initial, Peer nonce type: init
      Add time: Sun Mar 17 17:28:12 2024, Packets: 966, Pair SPI: 0xec5a1a8c
    SA type: ingress , SPI: 0xec5a1a8c
      Role: initiator, SA rekey state: initial, Peer nonce type: init
      Add time: Sun Mar 17 17:28:02 2024, Packets: 946, Pair SPI: 0xd76d50b4
  Inbound SPI: 0xec5a1a8c:
    Request ID: 64, Mode: transport, Replay window size: 0, Seq: 0x0
    Errors:
      Packets outside replay window: 0, Replay: 0, Integrity failed: 0
    Lifetime config:
      Soft byte limit: 4742139287475, Hard byte limit: 6442450944000
      Soft packet limit: 2908738069, Hard packet limit: 4000000000
      Soft time limit: 2607 secs, Hard time limit: 3600 secs
    Lifetime current:
      Current bytes: 285964
      Current packets: 951
      SA add time: Sun Mar 17 17:28:02 2024
      SA last use time: Sun Mar 17 17:34:22 2024
  Outbound SPI: 0xd76d50b4:
    Request ID: 64, Mode: transport, Replay window size: 0, Seq: 0x0
    Errors:
      Packets outside replay window: 0, Replay: 0, Integrity failed: 0
    Lifetime config:
      Soft byte limit: 4741127915100, Hard byte limit: 6442450944000
      Soft packet limit: 2938015564, Hard packet limit: 4000000000
      Soft time limit: 2617 secs, Hard time limit: 3600 secs
    Lifetime current:
      Current bytes: 451238
      Current packets: 971
      SA add time: Sun Mar 17 17:28:12 2024
      SA last use time: -
path4:
  Source address: 172.16.0.1, Destination address: 172.16.0.7
  State: established
  Uptime: 2 days, 6 hours, 54 minutes, 50 seconds
  VRF: default
  Type: static
  Remote IP: 10.255.255.12
  Role: initiator
  Inbound SPI: 0xc879a5:
    Request ID: 2, Mode: transport, Replay window size: 16384, Seq: 0x0
    Errors:
      Packets outside replay window: 0, Replay: 0, Integrity failed: 0
    Lifetime config:
      Soft byte limit: 4624284604499, Hard byte limit: 6442450944000
      Soft packet limit: 2493713462, Hard packet limit: 4000000000
      Soft time limit: 2948 secs, Hard time limit: 3600 secs
    Lifetime current:
      Current bytes: 345892
      Current packets: 1393
      SA add time: Sun Mar 17 17:28:36 2024
      SA last use time: Sun Mar 17 17:34:22 2024
  Outbound SPI: 0xccfeb9:
    Request ID: 2, Mode: transport, Replay window size: 0, Seq: 0x0
    Errors:
      Packets outside replay window: 0, Replay: 0, Integrity failed: 0
    Lifetime config:
      Soft byte limit: 3907759694249, Hard byte limit: 6442450944000
      Soft packet limit: 2015404503, Hard packet limit: 4000000000
      Soft time limit: 2911 secs, Hard time limit: 3600 secs
    Lifetime current:
      Current bytes: 492338
      Current packets: 1417
      SA add time: Sun Mar 17 17:28:36 2024
      SA last use time: -
path5:
  Source address: 172.16.0.1, Destination address: 172.16.0.9
  State: established
  Uptime: 2 days, 6 hours, 54 minutes, 47 seconds
  VRF: default
  Type: dynamic
  Remote IP: 10.255.255.11
  Role: responder
  Packets in: 129607211, Packets out: 84532077
  Last known rekey count: 7
  Dynamic state: established
  Last established time: Sun Mar 17 17:23:45 2024
  DH crypto:
    Local rekey: 6, Peer rekey: 7, In SPI: 0xbf75519e, Out SPI: 0x6e920521
    Local rekey: 6, Peer rekey: 9, In SPI: 0xc2af77f6, Out SPI: 0x992922cb
    Local rekey: 6, Peer rekey: 8, In SPI: 0x409b7e67, Out SPI: 0x300a60d3
    Local rekey: 7, Peer rekey: 9, In SPI: 0x35a5f1c, Out SPI: 0x992fc716
    Local rekey: 7, Peer rekey: 8, In SPI: 0x5dc88a26, Out SPI: 0xaf1cf9a9
  DH state:
    Local rekey: 7, Peer rekey: 9, DH rekey state: not rekeying, Role: not rekeying
  SA crypto:
    Local rekey: 7, Peer rekey: 9, In SPI 0x4815d2bf, Out SPI 0xea0df3ec
  SA rekey role: not rekeying
  SA state:
    SA type: egress , SPI: 0x5215f217
      Role: responder, SA rekey state: initial, Peer nonce type: init
      Add time: Sun Mar 17 17:22:09 2024, Packets: 1819, Pair SPI: 0xf40d1345
    SA type: ingress , SPI: 0xf40d1345
      Role: responder, SA rekey state: initial, Peer nonce type: init
      Add time: Sun Mar 17 17:22:01 2024, Packets: 1750, Pair SPI: 0x5215f217
  Inbound SPI: 0xf40d1345:
    Request ID: 63, Mode: transport, Replay window size: 0, Seq: 0x0
    Errors:
      Packets outside replay window: 0, Replay: 0, Integrity failed: 0
    Lifetime config:
      Soft byte limit: 4781444450100, Hard byte limit: 6442450944000
      Soft packet limit: 2911587297, Hard packet limit: 4000000000
      Soft time limit: 2586 secs, Hard time limit: 3600 secs
    Lifetime current:
      Current bytes: 739224
      Current packets: 1754
      SA add time: Sun Mar 17 17:22:01 2024
      SA last use time: Sun Mar 17 17:34:21 2024
  Outbound SPI: 0x5215f217:
    Request ID: 63, Mode: transport, Replay window size: 0, Seq: 0x0
    Errors:
      Packets outside replay window: 0, Replay: 0, Integrity failed: 0
    Lifetime config:
      Soft byte limit: 4723281335325, Hard byte limit: 6442450944000
      Soft packet limit: 2925558810, Hard packet limit: 4000000000
      Soft time limit: 2599 secs, Hard time limit: 3600 secs
    Lifetime current:
      Current bytes: 619838
      Current packets: 1823
      SA add time: Sun Mar 17 17:22:09 2024
      SA last use time: -
path6:
  Source address: 172.16.0.1, Destination address: 172.16.0.11
  State: established
  Uptime: 2 days, 6 hours, 54 minutes, 47 seconds
  VRF: default
  Type: dynamic
  Remote IP: 10.255.255.12
  Role: initiator
  Packets in: 194200701, Packets out: 136240057
  Last known rekey count: 7
  Dynamic state: established
  Last established time: Sun Mar 17 17:24:45 2024
  DH crypto:
    Local rekey: 6, Peer rekey: 7, In SPI: 0x39ab08e3, Out SPI: 0xdbde291e
    Local rekey: 6, Peer rekey: 9, In SPI: 0xa834aa9b, Out SPI: 0xfb4b6d70
    Local rekey: 6, Peer rekey: 8, In SPI: 0x3b9989a6, Out SPI: 0xdbbd2635
    Local rekey: 7, Peer rekey: 9, In SPI: 0x30aa5ace, Out SPI: 0xe8f619c
    Local rekey: 7, Peer rekey: 8, In SPI: 0xab9f9c3, Out SPI: 0x34959d0b
  DH state:
    Local rekey: 7, Peer rekey: 9, DH rekey state: not rekeying, Role: not rekeying
  SA crypto:
    Local rekey: 7, Peer rekey: 9, In SPI 0xfeae49a4, Out SPI 0x45a4eaa9
  SA rekey role: not rekeying
  SA state:
    SA type: egress , SPI: 0xaaf69fc
      Role: initiator, SA rekey state: initial, Peer nonce type: init
      Add time: Sun Mar 17 17:23:10 2024, Packets: 1634, Pair SPI: 0x51a40a02
    SA type: ingress , SPI: 0x51a40a02
      Role: initiator, SA rekey state: initial, Peer nonce type: init
      Add time: Sun Mar 17 17:23:01 2024, Packets: 1625, Pair SPI: 0xaaf69fc
  Inbound SPI: 0x51a40a02:
    Request ID: 62, Mode: transport, Replay window size: 0, Seq: 0x0
    Errors:
      Packets outside replay window: 0, Replay: 0, Integrity failed: 0
    Lifetime config:
      Soft byte limit: 4703640777750, Hard byte limit: 6442450944000
      Soft packet limit: 2972584162, Hard packet limit: 4000000000
      Soft time limit: 2533 secs, Hard time limit: 3600 secs
    Lifetime current:
      Current bytes: 725716
      Current packets: 1629
      SA add time: Sun Mar 17 17:23:01 2024
      SA last use time: Sun Mar 17 17:34:21 2024
  Outbound SPI: 0xaaf69fc:
    Request ID: 62, Mode: transport, Replay window size: 0, Seq: 0x0
    Errors:
      Packets outside replay window: 0, Replay: 0, Integrity failed: 0
    Lifetime config:
      Soft byte limit: 4704506238975, Hard byte limit: 6442450944000
      Soft packet limit: 2946688145, Hard packet limit: 4000000000
      Soft time limit: 2622 secs, Hard time limit: 3600 secs
    Lifetime current:
      Current bytes: 436084
      Current packets: 1638
      SA add time: Sun Mar 17 17:23:10 2024
      SA last use time: -
```

## show stun client translations detail

```text
Current System Time: Sun Mar 17 17:35:47 2024
Transaction ID 000000010affff0500000000
Agent Name: dps
Source Address: 172.16.0.1:4500
Public Address: 172.16.0.1:4500
Number of Attributes: 3
Timeout Interval: 0:03:00
Last Refreshed: 0:02:02 ago
Attribute Type   Length Value           
---------------- ------ ----------------
PATH_GROUP            6 VZ_OFF          
VTEP_IP               4 10.255.255.5    
WAN_ID                4 1               

```

## show stun server bindings detail

```text
Current System Time: Sun Mar 17 17:35:47 2024
```

## show path-selection paths detail

```text
Peer: 10.255.255.1, Path group VZ_OFF
Path name: path1, static, Label: 1
Source: 172.16.0.1, Port: 4500, WAN ID: 1
Destination: 172.16.0.4, Port: 4500, WAN ID: 2886729732
Local interface: Ethernet1/7
Route state: IPsec established
Traffic class 0: active (2 days, 1:16:19)
MTU: 8914

Peer: 10.255.255.4, Path group VZ_OFF
Path name: path4, static, Label: 4
Source: 172.16.0.1, Port: 4500, WAN ID: 1
Destination: 172.16.0.7, Port: 4500, WAN ID: 2886729735
Local interface: Ethernet1/7
Route state: IPsec established
Traffic class 0: active (2 days, 1:16:14)
MTU: 8914

Peer: 10.255.255.6, Path group VZ_OFF
Path name: path3, dynamic, Label: 3
Source: 172.16.0.1, Port: 4500, WAN ID: 1
Destination: 172.16.0.3, Port: 4500, WAN ID: 1
Local interface: Ethernet1/7
Route state: IPsec established
Traffic class 0: active (1 day, 9:09:52)
MTU: 8914

Peer: 10.255.255.11, Path group VZ_OFF
Path name: path5, dynamic, Label: 5
Source: 172.16.0.1, Port: 4500, WAN ID: 1
Destination: 172.16.0.9, Port: 4500, WAN ID: 2
Local interface: Ethernet1/7
Route state: IPsec established
Traffic class 0: active (2 days, 6:52:56)
MTU: 1424

Peer: 10.255.255.12, Path group VZ_OFF
Path name: path6, dynamic, Label: 6
Source: 172.16.0.1, Port: 4500, WAN ID: 1
Destination: 172.16.0.11, Port: 4500, WAN ID: 2
Local interface: Ethernet1/7
Route state: IPsec established
Traffic class 0: active (2 days, 1:16:14)
MTU: 1424

```

## show bgp neighbors

```text
BGP neighbor is 10.255.255.1, remote AS 65000, internal link
  BGP version 4, remote router ID 10.255.255.1, VRF default
  Inherits configuration from and member of peer-group PATHFINDER
  Last read 00:00:22, last write 00:00:13
  Hold time is 180, keepalive interval is 60 seconds
  Configured hold time is 180, keepalive interval is 60 seconds
  Effective minimum hold time is 3 seconds
  Send failure hold time is 0 seconds
  Hold timer is active, time left: 00:02:38
  Keepalive timer is active, time left: 00:00:43
  Connect timer is inactive
  Idle-restart timer is inactive
  BGP state is Established, up for 2d01h
  Number of transitions to established: 35
  Last state was OpenConfirm
  Last event was RecvUpdate
  Last sent notification:Cease/BFD down, Last time 2d01h, First time 2d08h, Repeats 29
  Last rcvd notification:Cease/BFD down, Last time 2d07h, First time 2d07h, Repeats 2
  Last sent socket-error:Connect (Network is unreachable), Last time 2d08h, First time 2d08h, Repeats 1
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
      Received 2d01h
      Number of stale paths removed after graceful restart: 0
      Number of paths received before End-of-RIB: 22
    L2VPN EVPN End-of-RIB received: Yes
      Received 2d01h
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
    Opens:                          37        36
    Notifications:                  30         6
    Updates:                       210      1742
    Keepalives:                   4020      3992
    Enhanced Route Refresh:          0         0
    Begin of Route Refresh:          0         0
    End of Route Refresh:            0         0
    Total messages:               4297      5776
  Prefix Statistics:
                                   Sent      Rcvd     Best Paths     Best ECMP Paths
    IPv4 Unicast:                     0         0              0                   0
    IPv4 Dps:                         2        18             18                   0
    IPv6 Unicast:                     0         0              0                   0
    EVPN:                             3        42             40                   1
  Configured maximum total number of routes is 12000
  Inbound updates dropped by reason:
    AS path loop detection: 0
    Cluster ID loop detection: 0
    Enforced First AS: 0
    Malformed MPBGP routes: 0
    Originator ID matches local router ID: 9
    Nexthop matches local IP address: 2
    Unexpected IPv6 nexthop for IPv4 routes: 0
  Inbound updates with attribute errors:
    Resulting in removal of all paths in update (treat as withdraw): 2
    Resulting in AFI/SAFI disable: 0
    Resulting in attribute ignore: 0
    Disabled AFI/SAFIs: None
    Last treat-as-withdraw attribute error: Nexthop is local address
    Last update with error received at: 2d01h
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
Local TCP address is 10.255.255.5, local port is 37129
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
    Round-trip Time (rtt/rtvar): 4.4ms/0.8ms
    Delayed Ack Timeout (ato): 44.0ms
    Congestion Window (cwnd): 7
    Slow-start Threshold (ssthresh): 7
    TCP Throughput: 18.49 Mbps
    Recv Round-trip Time (rcv_rtt): 4.1ms
    Advertised Recv Window (rcv_space): 14480

BGP neighbor is 10.255.255.4, remote AS 65000, internal link
  BGP version 4, remote router ID 10.255.255.4, VRF default
  Inherits configuration from and member of peer-group PATHFINDER
  Last read 00:00:06, last write 00:00:42
  Hold time is 180, keepalive interval is 60 seconds
  Configured hold time is 180, keepalive interval is 60 seconds
  Effective minimum hold time is 3 seconds
  Send failure hold time is 0 seconds
  Hold timer is active, time left: 00:02:54
  Keepalive timer is active, time left: 00:00:14
  Connect timer is inactive
  Idle-restart timer is inactive
  BGP state is Established, up for 2d06h
  Number of transitions to established: 20
  Last state was OpenConfirm
  Last event was RecvUpdate
  Last sent notification:Cease/BFD down, Last time 2d06h, First time 2d08h, Repeats 18
  Last sent socket-error:Connect (Network is unreachable), Last time 2d08h, First time 2d08h, Repeats 1
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
      Received 2d06h
      Number of stale paths removed after graceful restart: 0
      Number of paths received before End-of-RIB: 16
    L2VPN EVPN End-of-RIB received: Yes
      Received 2d06h
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
    Opens:                          20        20
    Notifications:                  19         0
    Updates:                       155      1441
    Keepalives:                   3997      3964
    Enhanced Route Refresh:          0         0
    Begin of Route Refresh:          0         0
    End of Route Refresh:            0         0
    Total messages:               4191      5425
  Prefix Statistics:
                                   Sent      Rcvd     Best Paths     Best ECMP Paths
    IPv4 Unicast:                     0         0              0                   0
    IPv4 Dps:                         2        18             18                  10
    IPv6 Unicast:                     0         0              0                   0
    EVPN:                             3        32             30                  27
  Configured maximum total number of routes is 12000
  Inbound updates dropped by reason:
    AS path loop detection: 0
    Cluster ID loop detection: 0
    Enforced First AS: 0
    Malformed MPBGP routes: 0
    Originator ID matches local router ID: 13
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
Local TCP address is 10.255.255.5, local port is 40559
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
  Total Number of TCP retransmissions: 3
  Options:
    Timestamps enabled: yes
    Selective Acknowledgments enabled: yes
    Window Scale enabled: yes
    Explicit Congestion Notification (ECN) enabled: no
  Socket Statistics:
    Window Scale (wscale): 7,7
    Retransmission Timeout (rto): 208.0ms
    Round-trip Time (rtt/rtvar): 5.1ms/1.0ms
    Delayed Ack Timeout (ato): 40.0ms
    Congestion Window (cwnd): 2
    TCP Throughput: 4.57 Mbps
    Recv Round-trip Time (rcv_rtt): 837.0ms
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
      Origin IGP, metric -, localpref -, weight 0, received 2d08h ago, valid, local
      Tunnel encapsulation attribute: Dynamic path selection
        Endpoint: 172.16.0.1, Path group name: VZ_OFF, WAN ID: 1, UDP port: 4500
Bgp routing table entry for ipv4Dps VTEP 10.255.255.6/32
 Paths: 4 available
  Local
    :: from 10.255.255.4 (10.255.255.4)
      Origin IGP, metric -, localpref 100, weight 0, received 2d06h ago, valid, internal
      Tunnel encapsulation attribute: Dynamic path selection
        Endpoint: 172.16.0.3, Path group name: VZ_OFF, WAN ID: 1, UDP port: 4500
  Local
    :: from 10.255.255.4 (10.255.255.4)
      Origin IGP, metric -, localpref 100, weight 0, received 2d01h ago, valid, internal
      Tunnel encapsulation attribute: Dynamic path selection
        Endpoint: 172.16.0.3, Path group name: VZ_OFF, WAN ID: 1, UDP port: 4500
  Local
    :: from 10.255.255.1 (10.255.255.1)
      Origin IGP, metric -, localpref 100, weight 0, received 2d01h ago, valid, internal
      Tunnel encapsulation attribute: Dynamic path selection
        Endpoint: 172.16.0.3, Path group name: VZ_OFF, WAN ID: 1, UDP port: 4500
  Local
    :: from 10.255.255.1 (10.255.255.1)
      Origin IGP, metric -, localpref 100, weight 0, received 2d01h ago, valid, internal
      Tunnel encapsulation attribute: Dynamic path selection
        Endpoint: 172.16.0.3, Path group name: VZ_OFF, WAN ID: 1, UDP port: 4500
Bgp routing table entry for ipv4Dps VTEP 10.255.255.8/32
 Paths: 4 available
  Local
    :: from 10.255.255.4 (10.255.255.4)
      Origin IGP, metric -, localpref 100, weight 0, received 2d06h ago, valid, internal
      Tunnel encapsulation attribute: Dynamic path selection
        Endpoint: 172.16.1.2, Path group name: VZ_NEAR, WAN ID: 1, UDP port: 4500
  Local
    :: from 10.255.255.4 (10.255.255.4)
      Origin IGP, metric -, localpref 100, weight 0, received 2d01h ago, valid, internal
      Tunnel encapsulation attribute: Dynamic path selection
        Endpoint: 172.16.1.2, Path group name: VZ_NEAR, WAN ID: 1, UDP port: 4500
  Local
    :: from 10.255.255.1 (10.255.255.1)
      Origin IGP, metric -, localpref 100, weight 0, received 2d01h ago, valid, internal
      Tunnel encapsulation attribute: Dynamic path selection
        Endpoint: 172.16.1.2, Path group name: VZ_NEAR, WAN ID: 1, UDP port: 4500
  Local
    :: from 10.255.255.1 (10.255.255.1)
      Origin IGP, metric -, localpref 100, weight 0, received 2d01h ago, valid, internal
      Tunnel encapsulation attribute: Dynamic path selection
        Endpoint: 172.16.1.2, Path group name: VZ_NEAR, WAN ID: 1, UDP port: 4500
Bgp routing table entry for ipv4Dps VTEP 10.255.255.11/32
 Paths: 4 available
  Local
    :: from 10.255.255.4 (10.255.255.4)
      Origin IGP, metric -, localpref 100, weight 0, received 2d06h ago, valid, internal
      Tunnel encapsulation attribute: Dynamic path selection
        Endpoint: 172.16.0.9, Path group name: VZ_OFF, WAN ID: 2, UDP port: 4500
  Local
    :: from 10.255.255.4 (10.255.255.4)
      Origin IGP, metric -, localpref 100, weight 0, received 2d01h ago, valid, internal
      Tunnel encapsulation attribute: Dynamic path selection
        Endpoint: 172.16.0.9, Path group name: VZ_OFF, WAN ID: 2, UDP port: 4500
  Local
    :: from 10.255.255.1 (10.255.255.1)
      Origin IGP, metric -, localpref 100, weight 0, received 2d01h ago, valid, internal
      Tunnel encapsulation attribute: Dynamic path selection
        Endpoint: 172.16.0.9, Path group name: VZ_OFF, WAN ID: 2, UDP port: 4500
  Local
    :: from 10.255.255.1 (10.255.255.1)
      Origin IGP, metric -, localpref 100, weight 0, received 2d01h ago, valid, internal
      Tunnel encapsulation attribute: Dynamic path selection
        Endpoint: 172.16.0.9, Path group name: VZ_OFF, WAN ID: 2, UDP port: 4500
Bgp routing table entry for ipv4Dps VTEP 10.255.255.12/32
 Paths: 4 available
  Local
    :: from 10.255.255.4 (10.255.255.4)
      Origin IGP, metric -, localpref 100, weight 0, received 2d06h ago, valid, internal
      Tunnel encapsulation attribute: Dynamic path selection
        Endpoint: 172.16.0.11, Path group name: VZ_OFF, WAN ID: 2, UDP port: 4500
  Local
    :: from 10.255.255.4 (10.255.255.4)
      Origin IGP, metric -, localpref 100, weight 0, received 2d01h ago, valid, internal
      Tunnel encapsulation attribute: Dynamic path selection
        Endpoint: 172.16.0.11, Path group name: VZ_OFF, WAN ID: 2, UDP port: 4500
  Local
    :: from 10.255.255.1 (10.255.255.1)
      Origin IGP, metric -, localpref 100, weight 0, received 2d01h ago, valid, internal
      Tunnel encapsulation attribute: Dynamic path selection
        Endpoint: 172.16.0.11, Path group name: VZ_OFF, WAN ID: 2, UDP port: 4500
  Local
    :: from 10.255.255.1 (10.255.255.1)
      Origin IGP, metric -, localpref 100, weight 0, received 2d01h ago, valid, internal
      Tunnel encapsulation attribute: Dynamic path selection
        Endpoint: 172.16.0.11, Path group name: VZ_OFF, WAN ID: 2, UDP port: 4500
Bgp routing table entry for ipv4Ipsec VTEP 10.255.255.1/32
 Paths: 2 available
  Local
    :: from 10.255.255.4 (10.255.255.4)
      Origin IGP, metric -, localpref 100, weight 0, received 2d01h ago, valid, internal
      Tunnel encapsulation attribute: IP security
        Initial contact: false, Rekey counter: 0, Nonce length: 32
        DH group: 14, DH key length: 256
        Encryption algo: aes256, Authentication algo: sha256
  Local
    :: from 10.255.255.1 (10.255.255.1)
      Origin IGP, metric -, localpref 100, weight 0, received 2d01h ago, valid, internal
      Tunnel encapsulation attribute: IP security
        Initial contact: false, Rekey counter: 0, Nonce length: 32
        DH group: 14, DH key length: 256
        Encryption algo: aes256, Authentication algo: sha256
Bgp routing table entry for ipv4Ipsec VTEP 10.255.255.4/32
 Paths: 2 available
  Local
    :: from 10.255.255.4 (10.255.255.4)
      Origin IGP, metric -, localpref 100, weight 0, received 2d06h ago, valid, internal
      Tunnel encapsulation attribute: IP security
        Initial contact: false, Rekey counter: 0, Nonce length: 32
        DH group: 14, DH key length: 256
        Encryption algo: aes256, Authentication algo: sha256
  Local
    :: from 10.255.255.1 (10.255.255.1)
      Origin IGP, metric -, localpref 100, weight 0, received 2d01h ago, valid, internal
      Tunnel encapsulation attribute: IP security
        Initial contact: false, Rekey counter: 0, Nonce length: 32
        DH group: 14, DH key length: 256
        Encryption algo: aes256, Authentication algo: sha256
Bgp routing table entry for ipv4Ipsec VTEP 10.255.255.5/32
 Paths: 1 available
  Local
    - from - (0.0.0.0)
      Origin IGP, metric -, localpref -, weight 0, received 2d08h ago, valid, local
      Tunnel encapsulation attribute: IP security
        Initial contact: false, Rekey counter: 7, Nonce length: 32
        DH group: 14, DH key length: 256
        Encryption algo: aes256, Authentication algo: sha256
Bgp routing table entry for ipv4Ipsec VTEP 10.255.255.6/32
 Paths: 4 available
  Local
    :: from 10.255.255.4 (10.255.255.4)
      Origin IGP, metric -, localpref 100, weight 0, received 02:19:15 ago, valid, internal
      Tunnel encapsulation attribute: IP security
        Initial contact: false, Rekey counter: 7, Nonce length: 32
        DH group: 14, DH key length: 256
        Encryption algo: aes256, Authentication algo: sha256
  Local
    :: from 10.255.255.1 (10.255.255.1)
      Origin IGP, metric -, localpref 100, weight 0, received 02:19:15 ago, valid, internal
      Tunnel encapsulation attribute: IP security
        Initial contact: false, Rekey counter: 7, Nonce length: 32
        DH group: 14, DH key length: 256
        Encryption algo: aes256, Authentication algo: sha256
  Local
    :: from 10.255.255.4 (10.255.255.4)
      Origin IGP, metric -, localpref 100, weight 0, received 02:19:15 ago, valid, internal
      Tunnel encapsulation attribute: IP security
        Initial contact: false, Rekey counter: 7, Nonce length: 32
        DH group: 14, DH key length: 256
        Encryption algo: aes256, Authentication algo: sha256
  Local
    :: from 10.255.255.1 (10.255.255.1)
      Origin IGP, metric -, localpref 100, weight 0, received 02:19:15 ago, valid, internal
      Tunnel encapsulation attribute: IP security
        Initial contact: false, Rekey counter: 7, Nonce length: 32
        DH group: 14, DH key length: 256
        Encryption algo: aes256, Authentication algo: sha256
Bgp routing table entry for ipv4Ipsec VTEP 10.255.255.8/32
 Paths: 4 available
  Local
    :: from 10.255.255.4 (10.255.255.4)
      Origin IGP, metric -, localpref 100, weight 0, received 1d09h ago, valid, internal
      Tunnel encapsulation attribute: IP security
        Initial contact: false, Rekey counter: 3, Nonce length: 32
        DH group: 14, DH key length: 256
        Encryption algo: aes256, Authentication algo: sha256
  Local
    :: from 10.255.255.1 (10.255.255.1)
      Origin IGP, metric -, localpref 100, weight 0, received 1d09h ago, valid, internal
      Tunnel encapsulation attribute: IP security
        Initial contact: false, Rekey counter: 3, Nonce length: 32
        DH group: 14, DH key length: 256
        Encryption algo: aes256, Authentication algo: sha256
  Local
    :: from 10.255.255.1 (10.255.255.1)
      Origin IGP, metric -, localpref 100, weight 0, received 1d09h ago, valid, internal
      Tunnel encapsulation attribute: IP security
        Initial contact: false, Rekey counter: 3, Nonce length: 32
        DH group: 14, DH key length: 256
        Encryption algo: aes256, Authentication algo: sha256
  Local
    :: from 10.255.255.4 (10.255.255.4)
      Origin IGP, metric -, localpref 100, weight 0, received 1d09h ago, valid, internal
      Tunnel encapsulation attribute: IP security
        Initial contact: false, Rekey counter: 3, Nonce length: 32
        DH group: 14, DH key length: 256
        Encryption algo: aes256, Authentication algo: sha256
Bgp routing table entry for ipv4Ipsec VTEP 10.255.255.11/32
 Paths: 4 available
  Local
    :: from 10.255.255.4 (10.255.255.4)
      Origin IGP, metric -, localpref 100, weight 0, received 06:40:54 ago, valid, internal
      Tunnel encapsulation attribute: IP security
        Initial contact: false, Rekey counter: 9, Nonce length: 32
        DH group: 14, DH key length: 256
        Encryption algo: aes256, Authentication algo: sha256
  Local
    :: from 10.255.255.1 (10.255.255.1)
      Origin IGP, metric -, localpref 100, weight 0, received 06:40:54 ago, valid, internal
      Tunnel encapsulation attribute: IP security
        Initial contact: false, Rekey counter: 9, Nonce length: 32
        DH group: 14, DH key length: 256
        Encryption algo: aes256, Authentication algo: sha256
  Local
    :: from 10.255.255.1 (10.255.255.1)
      Origin IGP, metric -, localpref 100, weight 0, received 06:40:54 ago, valid, internal
      Tunnel encapsulation attribute: IP security
        Initial contact: false, Rekey counter: 9, Nonce length: 32
        DH group: 14, DH key length: 256
        Encryption algo: aes256, Authentication algo: sha256
  Local
    :: from 10.255.255.4 (10.255.255.4)
      Origin IGP, metric -, localpref 100, weight 0, received 06:40:54 ago, valid, internal
      Tunnel encapsulation attribute: IP security
        Initial contact: false, Rekey counter: 9, Nonce length: 32
        DH group: 14, DH key length: 256
        Encryption algo: aes256, Authentication algo: sha256
Bgp routing table entry for ipv4Ipsec VTEP 10.255.255.12/32
 Paths: 4 available
  Local
    :: from 10.255.255.4 (10.255.255.4)
      Origin IGP, metric -, localpref 100, weight 0, received 06:42:53 ago, valid, internal
      Tunnel encapsulation attribute: IP security
        Initial contact: false, Rekey counter: 9, Nonce length: 32
        DH group: 14, DH key length: 256
        Encryption algo: aes256, Authentication algo: sha256
  Local
    :: from 10.255.255.1 (10.255.255.1)
      Origin IGP, metric -, localpref 100, weight 0, received 06:42:53 ago, valid, internal
      Tunnel encapsulation attribute: IP security
        Initial contact: false, Rekey counter: 9, Nonce length: 32
        DH group: 14, DH key length: 256
        Encryption algo: aes256, Authentication algo: sha256
  Local
    :: from 10.255.255.4 (10.255.255.4)
      Origin IGP, metric -, localpref 100, weight 0, received 06:42:53 ago, valid, internal
      Tunnel encapsulation attribute: IP security
        Initial contact: false, Rekey counter: 9, Nonce length: 32
        DH group: 14, DH key length: 256
        Encryption algo: aes256, Authentication algo: sha256
  Local
    :: from 10.255.255.1 (10.255.255.1)
      Origin IGP, metric -, localpref 100, weight 0, received 06:42:53 ago, valid, internal
      Tunnel encapsulation attribute: IP security
        Initial contact: false, Rekey counter: 9, Nonce length: 32
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
>C    10.255.255.5/32 [0 pref/0 metric] updated 2d08h ago
         via Loopback0, directly connected
>C    172.16.0.0/31 [0 pref/0 metric] updated 2d08h ago
         via Ethernet1/7, directly connected
>C    172.28.128.0/20 [0 pref/0 metric] updated 2d08h ago
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
>S    0.0.0.0/0 [1 pref/0 metric] updated 2d08h ago
         via 172.16.0.0 [0 pref/0 metric] type ipv4
            via 172.16.0.0, Ethernet1/7
>S    10.80.0.0/12 [1 pref/0 metric] updated 2d08h ago
         via 172.28.128.1 [0 pref/0 metric] type ipv4
            via 172.28.128.1, Management1/1
>S    10.239.0.0/16 [1 pref/0 metric] updated 2d08h ago
         via 172.28.128.1 [0 pref/0 metric] type ipv4
            via 172.28.128.1, Management1/1
>S    172.16.0.0/12 [1 pref/0 metric] updated 2d08h ago
         via 172.28.128.1 [0 pref/0 metric] type ipv4
            via 172.28.128.1, Management1/1
>S    172.16.0.0/24 [1 pref/0 metric] updated 2d08h ago
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
>P    0.0.0.0/8 [1 pref/0 metric] updated 2d08h ago
         via Null0, directly connected [NF]
>P    10.255.255.1/32 [1 pref/0 metric] updated 2d08h ago
         via 10.255.255.1, Dps1
>P    10.255.255.4/32 [1 pref/0 metric] updated 2d08h ago
         via 10.255.255.4, Dps1
>P    10.255.255.6/32 [1 pref/0 metric] updated 2d06h ago
         via 10.255.255.6, Dps1
>P    10.255.255.11/32 [1 pref/0 metric] updated 2d06h ago
         via 10.255.255.11, Dps1
>P    10.255.255.12/32 [1 pref/0 metric] updated 2d06h ago
         via 10.255.255.12, Dps1
>P    127.0.0.0/8 [1 pref/0 metric] updated 2d08h ago
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
>P    ::/96 [1 pref/0 metric] updated 2d08h ago
         via Null0, directly connected [NF]
>P    ::ffff:127.0.0.0/104 [1 pref/0 metric] updated 2d08h ago
         via :: [1 pref/1 metric] type ipv6
            via , directly connected
>P    fe80::/10 [1 pref/0 metric] updated 2d08h ago
```

## show platform sfe worker summary

```text
 WorkerId Busy       PPS
 -------- ---- ---------
        0    0         6
        1    0         1
        2    0         0
        3    0        14
        4    0         2
        5    0         1

```

