# Test results for IND518

## show version

```text
Arista AWE-5510-F
Hardware version: 11.01
Serial number: WTW23250083
Hardware MAC address: ec8a.4804.ff5b
System MAC address: ec8a.4804.ff5b

Software image version: 4.31.2F
Architecture: x86_64
Internal build version: 4.31.2F-35442176.4312F
Internal build ID: 500c58e3-5beb-4481-afe9-8ad77245cc44
Image format version: 3.0
Image optimization: Default

Uptime: 3 hours and 34 minutes
Total memory: 65396488 kB
Free memory: 39951292 kB

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
Ethernet1/1      10.5.255.2/31        up         up              1500          
Ethernet1/2      172.16.255.1/31      up         up              9000          
Ethernet1/3      172.16.1.5/31        up         up              9000          
Ethernet1/4      172.16.0.7/31        up         up              9000          
Loopback0        10.255.255.4/32      up         up             65535          
Management1/1    172.28.138.224/20    up         up              1500          

```

## show interfaces counters rates | nz

```text
Port      Name      Intvl  In Mbps      %  In Kpps Out Mbps      % Out Kpps
Et1/1                5:00    115.9   1.2%       14    245.7   2.5%       30
Et1/2                5:00    141.1   1.4%       17      0.0   0.0%        0
Et1/3     VZ_NEAR    5:00     57.3   0.6%        6     68.8   0.7%        8
Et1/4     VZ_OFF     5:00    208.2   2.1%       24    208.7   2.1%       24
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
 S        10.255.255.3/32
           directly connected, Dps1
 C        10.255.255.4/32
           directly connected, Loopback0
 S        10.255.255.5/32
           directly connected, Dps1
 S        10.255.255.6/32
           directly connected, Dps1
 S        10.255.255.8/32
           directly connected, Dps1
 S        10.255.255.10/32
           directly connected, Dps1
 S        10.255.255.11/32
           directly connected, Dps1
 S        10.255.255.12/32
           directly connected, Dps1
 S        10.240.0.0/12 [1/0]
           via 172.28.128.1, Management1/1
 C        172.16.0.6/31
           directly connected, Ethernet1/4
 S        172.16.0.0/24 [1/0]
           via 172.16.0.6, Ethernet1/4
 C        172.16.1.4/31
           directly connected, Ethernet1/3
 S        172.16.1.0/24 [1/0]
           via 172.16.1.4, Ethernet1/3
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
 S        10.255.255.3/32
           directly connected, Dps1
 C        10.255.255.4/32
           directly connected, Loopback0
 S        10.255.255.5/32
           directly connected, Dps1
 S        10.255.255.6/32
           directly connected, Dps1
 S        10.255.255.8/32
           directly connected, Dps1
 S        10.255.255.10/32
           directly connected, Dps1
 S        10.255.255.11/32
           directly connected, Dps1
 S        10.255.255.12/32
           directly connected, Dps1
 S        10.240.0.0/12 [1/0]
           via 172.28.128.1, Management1/1
 C        172.16.0.6/31
           directly connected, Ethernet1/4
 S        172.16.0.0/24 [1/0]
           via 172.16.0.6, Ethernet1/4
 C        172.16.1.4/31
           directly connected, Ethernet1/3
 S        172.16.1.0/24 [1/0]
           via 172.16.1.4, Ethernet1/3
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
 B I      10.0.255.2/31 [20/0]
           via VTEP 10.255.255.6 VNI 201 router-mac ec:8a:48:04:2b:ae
 B I      10.1.255.0/31 [20/0]
           via VTEP 10.255.255.1 VNI 201 router-mac ec:8a:48:04:f5:30
 B I      10.1.255.2/31 [20/0]
           via 172.16.255.0, Ethernet1/2
 B I      10.2.255.0/31 [20/0]
           via 172.16.255.0, Ethernet1/2
 B I      10.2.255.2/31 [20/0]
           via VTEP 10.255.255.8 VNI 201 router-mac ec:8a:48:04:2c:53
 B I      10.4.255.0/31 [20/0]
           via 172.16.255.0, Ethernet1/2
 B I      10.4.255.2/31 [20/0]
           via VTEP 10.255.255.10 VNI 201 router-mac 00:0c:29:d5:32:d4
 B I      10.5.255.0/31 [20/0]
           via 172.16.255.0, Ethernet1/2
 C        10.5.255.2/31
           directly connected, Ethernet1/1
 B I      10.6.255.0/31 [20/0]
           via VTEP 10.255.255.11 VNI 201 router-mac 00:0c:29:ba:2d:5e
 B I      10.6.255.2/31 [20/0]
           via VTEP 10.255.255.12 VNI 201 router-mac 00:0c:29:78:c5:2d
 B I      10.255.254.1/32 [20/0]
           via VTEP 10.255.255.5 VNI 201 router-mac ec:8a:48:04:21:53
           via VTEP 10.255.255.6 VNI 201 router-mac ec:8a:48:04:2b:ae
 B I      10.255.254.2/32 [20/0]
           via VTEP 10.255.255.1 VNI 201 router-mac ec:8a:48:04:f5:30
 B I      10.255.254.3/32 [20/0]
           via VTEP 10.255.255.8 VNI 201 router-mac ec:8a:48:04:2c:53
 B I      10.255.254.4/32 [20/0]
           via VTEP 10.255.255.12 VNI 201 router-mac 00:0c:29:78:c5:2d
           via VTEP 10.255.255.11 VNI 201 router-mac 00:0c:29:ba:2d:5e
 B I      10.255.254.5/32 [20/0]
           via VTEP 10.255.255.10 VNI 201 router-mac 00:0c:29:d5:32:d4
 O        10.255.254.6/32 [110/20]
           via 10.5.255.3, Ethernet1/1
 C        172.16.255.0/31
           directly connected, Ethernet1/2
 B I      172.16.255.2/31 [20/0]
           via VTEP 10.255.255.1 VNI 201 router-mac ec:8a:48:04:f5:30
 B I      192.168.0.0/24 [20/0]
           via VTEP 10.255.255.5 VNI 201 router-mac ec:8a:48:04:21:53
           via VTEP 10.255.255.6 VNI 201 router-mac ec:8a:48:04:2b:ae
 B I      192.168.1.0/24 [20/0]
           via VTEP 10.255.255.1 VNI 201 router-mac ec:8a:48:04:f5:30
 B I      192.168.3.0/24 [20/0]
           via VTEP 10.255.255.8 VNI 201 router-mac ec:8a:48:04:2c:53
 O        192.168.5.0/24 [110/20]
           via 10.5.255.3, Ethernet1/1
 B I      192.168.6.0/24 [20/0]
           via VTEP 10.255.255.12 VNI 201 router-mac 00:0c:29:78:c5:2d
           via VTEP 10.255.255.11 VNI 201 router-mac 00:0c:29:ba:2d:5e
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
Router identifier 10.255.255.4, local AS number 65000
Route status codes: * - valid, > - active, S - Stale, E - ECMP head, e - ECMP
                    c - Contributing to ECMP, % - Pending best path selection
Origin codes: i - IGP, e - EGP, ? - incomplete
AS Path Attributes: Or-ID - Originator ID, C-LST - Cluster List, LL Nexthop - Link Local Nexthop

          Network                Next Hop              Metric  LocPref Weight  Path
 * >      RD: 10.255.255.5:1 ip-prefix 10.0.255.0/31
                                 10.255.255.5          -       100     0       i
 * >      RD: 10.255.255.6:1 ip-prefix 10.0.255.2/31
                                 10.255.255.6          -       100     0       i
 * >      RD: 10.255.255.1:1 ip-prefix 10.1.255.0/31
                                 10.255.255.1          -       100     0       i
 * >      RD: 10.255.255.1:1 ip-prefix 10.1.255.2/31
                                 10.255.255.1          -       5       0       i
 * >      RD: 10.255.255.4:1 ip-prefix 10.1.255.2/31
                                 -                     -       5       0       i
 * >      RD: 10.255.255.1:1 ip-prefix 10.2.255.0/31
                                 10.255.255.1          -       5       0       i
 * >      RD: 10.255.255.4:1 ip-prefix 10.2.255.0/31
                                 -                     -       5       0       i Or-ID: 10.255.255.7 C-LST: 172.16.255.0 10.255.255.2 
 * >Ec    RD: 10.255.255.7:1 ip-prefix 10.2.255.2/31
                                 10.255.255.8          -       100     0       i Or-ID: 10.255.255.8 C-LST: 10.255.255.1 
 *  ec    RD: 10.255.255.7:1 ip-prefix 10.2.255.2/31
                                 10.255.255.8          -       100     0       i
 * >      RD: 10.255.255.1:1 ip-prefix 10.4.255.0/31
                                 10.255.255.1          -       5       0       i
 * >      RD: 10.255.255.4:1 ip-prefix 10.4.255.0/31
                                 -                     -       5       0       i Or-ID: 10.255.255.9 C-LST: 172.16.255.0 10.255.255.2 
 * >Ec    RD: 10.255.255.10:1 ip-prefix 10.4.255.2/31
                                 10.255.255.10         -       100     0       i Or-ID: 10.255.255.10 C-LST: 10.255.255.1 
 *  ec    RD: 10.255.255.10:1 ip-prefix 10.4.255.2/31
                                 10.255.255.10         -       100     0       i
 * >      RD: 10.255.255.1:1 ip-prefix 10.5.255.0/31
                                 10.255.255.1          -       5       0       i
 * >      RD: 10.255.255.4:1 ip-prefix 10.5.255.0/31
                                 -                     -       5       0       i
 * >      RD: 10.255.255.4:1 ip-prefix 10.5.255.2/31
                                 -                     -       -       0       i
 * >      RD: 10.255.255.11:1 ip-prefix 10.6.255.0/31
                                 10.255.255.11         -       100     0       i
 * >Ec    RD: 10.255.255.12:1 ip-prefix 10.6.255.2/31
                                 10.255.255.12         -       100     0       i Or-ID: 10.255.255.12 C-LST: 10.255.255.1 
 *  ec    RD: 10.255.255.12:1 ip-prefix 10.6.255.2/31
                                 10.255.255.12         -       100     0       i
 * >      RD: 10.255.255.5:1 ip-prefix 10.255.254.1/32
                                 10.255.255.5          -       100     0       i
 * >Ec    RD: 10.255.255.6:1 ip-prefix 10.255.254.1/32
                                 10.255.255.6          -       100     0       i
 *  ec    RD: 10.255.255.6:1 ip-prefix 10.255.254.1/32
                                 10.255.255.6          -       100     0       i Or-ID: 10.255.255.6 C-LST: 10.255.255.1 
 * >      RD: 10.255.255.1:1 ip-prefix 10.255.254.2/32
                                 10.255.255.1          -       100     0       i
 * >      RD: 10.255.255.4:1 ip-prefix 10.255.254.2/32
                                 -                     -       5       0       i
 * >      RD: 10.255.255.1:1 ip-prefix 10.255.254.3/32
                                 10.255.255.1          -       5       0       i
 * >      RD: 10.255.255.4:1 ip-prefix 10.255.254.3/32
                                 -                     -       5       0       i Or-ID: 10.255.255.7 C-LST: 172.16.255.0 10.255.255.2 
 * >Ec    RD: 10.255.255.7:1 ip-prefix 10.255.254.3/32
                                 10.255.255.8          -       100     0       i
 *  ec    RD: 10.255.255.7:1 ip-prefix 10.255.254.3/32
                                 10.255.255.8          -       100     0       i Or-ID: 10.255.255.8 C-LST: 10.255.255.1 
 * >Ec    RD: 10.255.255.11:1 ip-prefix 10.255.254.4/32
                                 10.255.255.11         -       100     0       i
 *  ec    RD: 10.255.255.11:1 ip-prefix 10.255.254.4/32
                                 10.255.255.11         -       100     0       i Or-ID: 10.255.255.11 C-LST: 10.255.255.1 
 * >Ec    RD: 10.255.255.12:1 ip-prefix 10.255.254.4/32
                                 10.255.255.12         -       100     0       i Or-ID: 10.255.255.12 C-LST: 10.255.255.1 
 *  ec    RD: 10.255.255.12:1 ip-prefix 10.255.254.4/32
                                 10.255.255.12         -       100     0       i
 * >      RD: 10.255.255.1:1 ip-prefix 10.255.254.5/32
                                 10.255.255.1          -       5       0       i
 * >      RD: 10.255.255.4:1 ip-prefix 10.255.254.5/32
                                 -                     -       5       0       i
 * >Ec    RD: 10.255.255.10:1 ip-prefix 10.255.254.5/32
                                 10.255.255.10         -       100     0       i
 *  ec    RD: 10.255.255.10:1 ip-prefix 10.255.254.5/32
                                 10.255.255.10         -       100     0       i Or-ID: 10.255.255.10 C-LST: 10.255.255.1 
          RD: 10.255.255.1:1 ip-prefix 10.255.254.6/32
                                 PolicyReject          -       -       0       i
 * >      RD: 10.255.255.4:1 ip-prefix 10.255.254.6/32
                                 -                     -       -       0       i
 * >      RD: 10.255.255.1:1 ip-prefix 172.16.255.0/31
                                 10.255.255.1          -       5       0       i
 * >      RD: 10.255.255.4:1 ip-prefix 172.16.255.0/31
                                 -                     -       -       0       i
 *        RD: 10.255.255.4:1 ip-prefix 172.16.255.0/31
                                 -                     -       5       0       i
 * >      RD: 10.255.255.1:1 ip-prefix 172.16.255.2/31
                                 10.255.255.1          -       100     0       i
 * >      RD: 10.255.255.4:1 ip-prefix 172.16.255.2/31
                                 -                     -       5       0       i
 * >      RD: 10.255.255.5:1 ip-prefix 192.168.0.0/24
                                 10.255.255.5          -       100     0       i
 * >Ec    RD: 10.255.255.6:1 ip-prefix 192.168.0.0/24
                                 10.255.255.6          -       100     0       i
 *  ec    RD: 10.255.255.6:1 ip-prefix 192.168.0.0/24
                                 10.255.255.6          -       100     0       i Or-ID: 10.255.255.6 C-LST: 10.255.255.1 
 * >      RD: 10.255.255.1:1 ip-prefix 192.168.1.0/24
                                 10.255.255.1          -       100     0       i
 * >      RD: 10.255.255.4:1 ip-prefix 192.168.1.0/24
                                 -                     -       5       0       i
 * >      RD: 10.255.255.1:1 ip-prefix 192.168.3.0/24
                                 10.255.255.1          -       5       0       i
 * >      RD: 10.255.255.4:1 ip-prefix 192.168.3.0/24
                                 -                     -       5       0       i Or-ID: 10.255.255.7 C-LST: 172.16.255.0 10.255.255.2 
 * >Ec    RD: 10.255.255.7:1 ip-prefix 192.168.3.0/24
                                 10.255.255.8          -       100     0       i
 *  ec    RD: 10.255.255.7:1 ip-prefix 192.168.3.0/24
                                 10.255.255.8          -       100     0       i Or-ID: 10.255.255.8 C-LST: 10.255.255.1 
          RD: 10.255.255.1:1 ip-prefix 192.168.5.0/24
                                 PolicyReject          -       -       0       i
 * >      RD: 10.255.255.4:1 ip-prefix 192.168.5.0/24
                                 -                     -       -       0       i
 * >Ec    RD: 10.255.255.11:1 ip-prefix 192.168.6.0/24
                                 10.255.255.11         -       100     0       i
 *  ec    RD: 10.255.255.11:1 ip-prefix 192.168.6.0/24
                                 10.255.255.11         -       100     0       i Or-ID: 10.255.255.11 C-LST: 10.255.255.1 
 * >Ec    RD: 10.255.255.12:1 ip-prefix 192.168.6.0/24
                                 10.255.255.12         -       100     0       i Or-ID: 10.255.255.12 C-LST: 10.255.255.1 
 *  ec    RD: 10.255.255.12:1 ip-prefix 192.168.6.0/24
                                 10.255.255.12         -       100     0       i
 * >      RD: 10.255.255.1:1 ip-prefix 192.168.40.0/24
                                 10.255.255.1          -       5       0       i
 * >      RD: 10.255.255.4:1 ip-prefix 192.168.40.0/24
                                 -                     -       5       0       i
 * >Ec    RD: 10.255.255.10:1 ip-prefix 192.168.40.0/24
                                 10.255.255.10         -       100     0       i
 *  ec    RD: 10.255.255.10:1 ip-prefix 192.168.40.0/24
                                 10.255.255.10         -       100     0       i Or-ID: 10.255.255.10 C-LST: 10.255.255.1 
```

## show ip security connection detail

```text
path1:
  Source address: 172.16.0.7, Destination address: 172.16.0.1
  State: established
  Uptime: 3 hours, 31 minutes, 21 seconds
  VRF: default
  Type: static
  Remote IP: 10.255.255.5
  Role: initiator
  Inbound SPI: 0xca8b32:
    Request ID: 4, Mode: transport, Replay window size: 16384, Seq: 0x0
    Errors:
      Packets outside replay window: 0, Replay: 0, Integrity failed: 0
    Lifetime config:
      Soft byte limit: 4705929044249, Hard byte limit: 6442450944000
      Soft packet limit: 2994038381, Hard packet limit: 4000000000
      Soft time limit: 2910 secs, Hard time limit: 3600 secs
    Lifetime current:
      Current bytes: 4238853572
      Current packets: 4001109
      SA add time: Thu Mar 14 16:35:40 2024
      SA last use time: Thu Mar 14 16:51:25 2024
  Outbound SPI: 0xcb3f69:
    Request ID: 4, Mode: transport, Replay window size: 0, Seq: 0x0
    Errors:
      Packets outside replay window: 0, Replay: 0, Integrity failed: 0
    Lifetime config:
      Soft byte limit: 3772510501499, Hard byte limit: 6442450944000
      Soft packet limit: 2745117796, Hard packet limit: 4000000000
      Soft time limit: 2704 secs, Hard time limit: 3600 secs
    Lifetime current:
      Current bytes: 7138906747
      Current packets: 14028820
      SA add time: Thu Mar 14 16:35:40 2024
      SA last use time: Thu Mar 14 16:51:25 2024
path2:
  Source address: 172.16.1.5, Destination address: 172.16.0.1
  State: idle
  Uptime: N/A
  VRF: default
  Type: static
  Remote IP: 10.255.255.5
  Role: initiator
path3:
  Source address: 172.16.0.7, Destination address: 172.16.0.3
  State: established
  Uptime: 13 minutes, 50 seconds
  VRF: default
  Type: static
  Remote IP: 10.255.255.5
  Role: initiator
  Inbound SPI: 0xcb937a:
    Request ID: 6, Mode: transport, Replay window size: 16384, Seq: 0x0
    Errors:
      Packets outside replay window: 0, Replay: 0, Integrity failed: 0
    Lifetime config:
      Soft byte limit: 4215546456749, Hard byte limit: 6442450944000
      Soft packet limit: 2997673469, Hard packet limit: 4000000000
      Soft time limit: 2611 secs, Hard time limit: 3600 secs
    Lifetime current:
      Current bytes: 7381592616
      Current packets: 6965718
      SA add time: Thu Mar 14 16:37:05 2024
      SA last use time: Thu Mar 14 16:51:25 2024
  Outbound SPI: 0xc1e4ab:
    Request ID: 6, Mode: transport, Replay window size: 0, Seq: 0x0
    Errors:
      Packets outside replay window: 0, Replay: 0, Integrity failed: 0
    Lifetime config:
      Soft byte limit: 4367682143999, Hard byte limit: 6442450944000
      Soft packet limit: 2345930772, Hard packet limit: 4000000000
      Soft time limit: 2813 secs, Hard time limit: 3600 secs
    Lifetime current:
      Current bytes: 4076734964
      Current packets: 8012266
      SA add time: Thu Mar 14 16:37:05 2024
      SA last use time: Thu Mar 14 16:51:25 2024
path4:
  Source address: 172.16.1.5, Destination address: 172.16.0.3
  State: idle
  Uptime: N/A
  VRF: default
  Type: static
  Remote IP: 10.255.255.5
  Role: initiator
path5:
  Source address: 172.16.0.7, Destination address: 172.16.1.2
  State: idle
  Uptime: N/A
  VRF: default
  Type: static
  Remote IP: 10.255.255.5
  Role: initiator
path6:
  Source address: 172.16.1.5, Destination address: 172.16.1.2
  State: established
  Uptime: 3 hours, 31 minutes, 11 seconds
  VRF: default
  Type: static
  Remote IP: 10.255.255.5
  Role: initiator
  Inbound SPI: 0xc6d28c:
    Request ID: 8, Mode: transport, Replay window size: 16384, Seq: 0x0
    Errors:
      Packets outside replay window: 0, Replay: 0, Integrity failed: 0
    Lifetime config:
      Soft byte limit: 3334566996749, Hard byte limit: 6442450944000
      Soft packet limit: 2077910474, Hard packet limit: 4000000000
      Soft time limit: 2974 secs, Hard time limit: 3600 secs
    Lifetime current:
      Current bytes: 13383158412
      Current packets: 12630855
      SA add time: Thu Mar 14 16:13:35 2024
      SA last use time: Thu Mar 14 16:51:25 2024
  Outbound SPI: 0xccc229:
    Request ID: 8, Mode: transport, Replay window size: 0, Seq: 0x0
    Errors:
      Packets outside replay window: 0, Replay: 0, Integrity failed: 0
    Lifetime config:
      Soft byte limit: 3898419665249, Hard byte limit: 6442450944000
      Soft packet limit: 2751079415, Hard packet limit: 4000000000
      Soft time limit: 2853 secs, Hard time limit: 3600 secs
    Lifetime current:
      Current bytes: 15692055273
      Current packets: 30837170
      SA add time: Thu Mar 14 16:13:35 2024
      SA last use time: Thu Mar 14 16:51:25 2024
path7:
  Source address: 172.16.0.7, Destination address: 172.16.0.9
  State: established
  Uptime: 11 minutes, 36 seconds
  VRF: default
  Type: static
  Remote IP: 10.255.255.5
  Role: initiator
  Inbound SPI: 0xc78051:
    Request ID: 12, Mode: transport, Replay window size: 16384, Seq: 0x0
    Errors:
      Packets outside replay window: 0, Replay: 0, Integrity failed: 0
    Lifetime config:
      Soft byte limit: 3320740088249, Hard byte limit: 6442450944000
      Soft packet limit: 2412705998, Hard packet limit: 4000000000
      Soft time limit: 2657 secs, Hard time limit: 3600 secs
    Lifetime current:
      Current bytes: 4409226112
      Current packets: 4161224
      SA add time: Thu Mar 14 16:39:19 2024
      SA last use time: Thu Mar 14 16:51:25 2024
  Outbound SPI: 0xca929a:
    Request ID: 12, Mode: transport, Replay window size: 0, Seq: 0x0
    Errors:
      Packets outside replay window: 0, Replay: 0, Integrity failed: 0
    Lifetime config:
      Soft byte limit: 4090222709999, Hard byte limit: 6442450944000
      Soft packet limit: 2491374362, Hard packet limit: 4000000000
      Soft time limit: 2765 secs, Hard time limit: 3600 secs
    Lifetime current:
      Current bytes: 5081173732
      Current packets: 9986124
      SA add time: Thu Mar 14 16:39:19 2024
      SA last use time: Thu Mar 14 16:51:25 2024
path8:
  Source address: 172.16.1.5, Destination address: 172.16.0.9
  State: idle
  Uptime: N/A
  VRF: default
  Type: static
  Remote IP: 10.255.255.5
  Role: initiator
path9:
  Source address: 172.16.0.7, Destination address: 172.16.0.11
  State: established
  Uptime: 3 hours, 29 minutes, 19 seconds
  VRF: default
  Type: static
  Remote IP: 10.255.255.5
  Role: initiator
  Inbound SPI: 0xc0e085:
    Request ID: 13, Mode: transport, Replay window size: 16384, Seq: 0x0
    Errors:
      Packets outside replay window: 0, Replay: 0, Integrity failed: 0
    Lifetime config:
      Soft byte limit: 4257272687999, Hard byte limit: 6442450944000
      Soft packet limit: 2008087880, Hard packet limit: 4000000000
      Soft time limit: 2810 secs, Hard time limit: 3600 secs
    Lifetime current:
      Current bytes: 12960199468
      Current packets: 12231403
      SA add time: Thu Mar 14 16:16:58 2024
      SA last use time: Thu Mar 14 16:51:25 2024
  Outbound SPI: 0xcd5bfa:
    Request ID: 13, Mode: transport, Replay window size: 0, Seq: 0x0
    Errors:
      Packets outside replay window: 0, Replay: 0, Integrity failed: 0
    Lifetime config:
      Soft byte limit: 3821767138499, Hard byte limit: 6442450944000
      Soft packet limit: 2094458265, Hard packet limit: 4000000000
      Soft time limit: 2949 secs, Hard time limit: 3600 secs
    Lifetime current:
      Current bytes: 10267599014
      Current packets: 20182854
      SA add time: Thu Mar 14 16:16:58 2024
      SA last use time: Thu Mar 14 16:51:25 2024
path10:
  Source address: 172.16.1.5, Destination address: 172.16.0.11
  State: idle
  Uptime: N/A
  VRF: default
  Type: static
  Remote IP: 10.255.255.5
  Role: initiator
path11:
  Source address: 172.16.0.7, Destination address: 172.16.1.7
  State: idle
  Uptime: N/A
  VRF: default
  Type: static
  Remote IP: 10.255.255.5
  Role: initiator
path12:
  Source address: 172.16.1.5, Destination address: 172.16.1.7
  State: established
  Uptime: 1 hour, 44 minutes, 10 seconds
  VRF: default
  Type: static
  Remote IP: 10.255.255.5
  Role: initiator
  Inbound SPI: 0xca618d:
    Request ID: 10, Mode: transport, Replay window size: 16384, Seq: 0x0
    Errors:
      Packets outside replay window: 0, Replay: 0, Integrity failed: 0
    Lifetime config:
      Soft byte limit: 4168565361749, Hard byte limit: 6442450944000
      Soft packet limit: 2886627011, Hard packet limit: 4000000000
      Soft time limit: 2761 secs, Hard time limit: 3600 secs
    Lifetime current:
      Current bytes: 691388
      Current packets: 2779
      SA add time: Thu Mar 14 16:36:50 2024
      SA last use time: Thu Mar 14 16:51:25 2024
  Outbound SPI: 0xc8f0a9:
    Request ID: 10, Mode: transport, Replay window size: 0, Seq: 0x0
    Errors:
      Packets outside replay window: 0, Replay: 0, Integrity failed: 0
    Lifetime config:
      Soft byte limit: 4071696248249, Hard byte limit: 6442450944000
      Soft packet limit: 2609267837, Hard packet limit: 4000000000
      Soft time limit: 2876 secs, Hard time limit: 3600 secs
    Lifetime current:
      Current bytes: 541510
      Current packets: 5652
      SA add time: Thu Mar 14 16:36:50 2024
      SA last use time: Thu Mar 14 16:51:25 2024
path13:
  Source address: 172.16.0.7, Destination address: 172.16.1.0
  State: idle
  Uptime: N/A
  VRF: default
  Type: static
  Remote IP: 10.255.255.5
  Role: initiator
path14:
  Source address: 172.16.1.5, Destination address: 172.16.1.0
  State: established
  Uptime: 3 hours, 32 minutes, 36 seconds
  VRF: default
  Type: static
  Remote IP: 10.255.255.5
  Role: initiator
  Inbound SPI: 0xcadf17:
    Request ID: 2, Mode: transport, Replay window size: 16384, Seq: 0x0
    Errors:
      Packets outside replay window: 0, Replay: 0, Integrity failed: 0
    Lifetime config:
      Soft byte limit: 4282378155749, Hard byte limit: 6442450944000
      Soft packet limit: 2544988937, Hard packet limit: 4000000000
      Soft time limit: 2707 secs, Hard time limit: 3600 secs
    Lifetime current:
      Current bytes: 1554432
      Current packets: 5420
      SA add time: Thu Mar 14 16:23:34 2024
      SA last use time: Thu Mar 14 16:51:25 2024
  Outbound SPI: 0xc7814c:
    Request ID: 2, Mode: transport, Replay window size: 0, Seq: 0x0
    Errors:
      Packets outside replay window: 0, Replay: 0, Integrity failed: 0
    Lifetime config:
      Soft byte limit: 3558948140999, Hard byte limit: 6442450944000
      Soft packet limit: 2199328368, Hard packet limit: 4000000000
      Soft time limit: 2906 secs, Hard time limit: 3600 secs
    Lifetime current:
      Current bytes: 2365309
      Current packets: 11090
      SA add time: Thu Mar 14 16:23:34 2024
      SA last use time: Thu Mar 14 16:51:25 2024
```

## show stun client translations detail

```text
Current System Time: Thu Mar 14 16:50:56 2024
```

## show stun server bindings detail

```text
Current System Time: Thu Mar 14 16:50:57 2024
Transaction ID 000000010affff0500000000
Public Address: 172.16.0.1:4500
Number of Attributes: 3
Timeout Interval: 0:10:00
Timeout: 0:07:17
Attribute Type   Length Value           
---------------- ------ ----------------
PATH_GROUP            6 VZ_OFF          
VTEP_IP               4 10.255.255.5    
WAN_ID                4 1               

Transaction ID 000000010affff0600000000
Public Address: 172.16.0.3:4500
Number of Attributes: 3
Timeout Interval: 0:10:00
Timeout: 0:08:04
Attribute Type   Length Value           
---------------- ------ ----------------
PATH_GROUP            6 VZ_OFF          
VTEP_IP               4 10.255.255.6    
WAN_ID                4 1               

Transaction ID 000000010affff0800000000
Public Address: 172.16.1.2:4500
Number of Attributes: 3
Timeout Interval: 0:10:00
Timeout: 0:07:36
Attribute Type   Length Value           
---------------- ------ ----------------
PATH_GROUP            7 VZ_NEAR         
VTEP_IP               4 10.255.255.8    
WAN_ID                4 1               

Transaction ID 000000010affff0a00000000
Public Address: 172.16.1.7:4500
Number of Attributes: 3
Timeout Interval: 0:10:00
Timeout: 0:07:50
Attribute Type   Length Value           
---------------- ------ ----------------
PATH_GROUP            7 VZ_NEAR         
VTEP_IP               4 10.255.255.10   
WAN_ID                4 1               

Transaction ID 000000020affff0100000000
Public Address: 172.16.1.0:4500
Number of Attributes: 3
Timeout Interval: 0:10:00
Timeout: 0:08:11
Attribute Type   Length Value           
---------------- ------ ----------------
PATH_GROUP            7 VZ_NEAR         
VTEP_IP               4 10.255.255.1    
WAN_ID                4 2               

Transaction ID 000000020affff0b00000000
Public Address: 172.16.0.9:4500
Number of Attributes: 3
Timeout Interval: 0:10:00
Timeout: 0:07:23
Attribute Type   Length Value           
---------------- ------ ----------------
PATH_GROUP            6 VZ_OFF          
VTEP_IP               4 10.255.255.11   
WAN_ID                4 2               

Transaction ID 000000020affff0c00000000
Public Address: 172.16.0.11:4500
Number of Attributes: 3
Timeout Interval: 0:10:00
Timeout: 0:09:36
Attribute Type   Length Value           
---------------- ------ ----------------
PATH_GROUP            6 VZ_OFF          
VTEP_IP               4 10.255.255.12   
WAN_ID                4 2               

```

## show path-selection paths detail

```text
Peer: 10.255.255.1, Path group VZ_NEAR
Path name: path14, dynamic, Label: 14
Source: 172.16.1.5, Port: 4500, WAN ID: 2
Destination: 172.16.1.0, Port: 4500, WAN ID: 2
Local interface: Ethernet1/3
Route state: IPsec established
Traffic class 0: active (3:32:28)
MTU: 8914

Peer: 10.255.255.5, Path group VZ_OFF
Path name: path1, dynamic, Label: 1
Source: 172.16.0.7, Port: 4500, WAN ID: 1
Destination: 172.16.0.1, Port: 4500, WAN ID: 1
Local interface: Ethernet1/4
Route state: IPsec established
Traffic class 0: active (3:14:14)
MTU: 8914

Peer: 10.255.255.6, Path group VZ_OFF
Path name: path3, dynamic, Label: 3
Source: 172.16.0.7, Port: 4500, WAN ID: 1
Destination: 172.16.0.3, Port: 4500, WAN ID: 1
Local interface: Ethernet1/4
Route state: IPsec established
Traffic class 0: active (0:13:49)
MTU: 8914

Peer: 10.255.255.8, Path group VZ_NEAR
Path name: path6, dynamic, Label: 6
Source: 172.16.1.5, Port: 4500, WAN ID: 2
Destination: 172.16.1.2, Port: 4500, WAN ID: 1
Local interface: Ethernet1/3
Route state: IPsec established
Traffic class 0: active (3:31:03)
MTU: 8914

Peer: 10.255.255.10, Path group VZ_NEAR
Path name: path12, dynamic, Label: 12
Source: 172.16.1.5, Port: 4500, WAN ID: 2
Destination: 172.16.1.7, Port: 4500, WAN ID: 1
Local interface: Ethernet1/3
Route state: IPsec established
Traffic class 0: active (1:44:07)
MTU: 1424

Peer: 10.255.255.11, Path group VZ_OFF
Path name: path7, dynamic, Label: 7
Source: 172.16.0.7, Port: 4500, WAN ID: 1
Destination: 172.16.0.9, Port: 4500, WAN ID: 2
Local interface: Ethernet1/4
Route state: IPsec established
Traffic class 0: active (0:11:36)
MTU: 1424

Peer: 10.255.255.12, Path group VZ_OFF
Path name: path9, dynamic, Label: 9
Source: 172.16.0.7, Port: 4500, WAN ID: 1
Destination: 172.16.0.11, Port: 4500, WAN ID: 2
Local interface: Ethernet1/4
Route state: IPsec established
Traffic class 0: active (3:29:13)
MTU: 1424

```

## show bgp neighbors

```text
BGP neighbor is 10.255.255.1, remote AS 65000, internal link
  BGP version 4, remote router ID 10.255.255.1, VRF default
  Inherits configuration from and member of peer-group autovpnEdges
  Last read 00:00:39, last write 00:00:05
  Hold time is 180, keepalive interval is 60 seconds
  Configured hold time is 180, keepalive interval is 60 seconds
  Effective minimum hold time is 3 seconds
  Send failure hold time is 0 seconds
  Hold timer is active, time left: 00:02:21
  Keepalive timer is active, time left: 00:00:44
  Connect timer is inactive
  Idle-restart timer is inactive
  BGP state is Established, up for 03:32:30
  Number of transitions to established: 1
  Last state was OpenConfirm
  Last event was Established
  Last sent socket-error:Connect (Network is unreachable), Last time 03:33:19, First time 03:33:45, Repeats 3
  Types of communities advertised: extended
  Enhanced route refresh stale path removal disabled
  Outbound enhanced route refresh enabled
  Neighbor is a route reflector client
  Neighbor is using global cluster ID 10.255.255.4
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
      Received 03:31:01
      Number of stale paths removed after graceful restart: 0
      Number of paths received before End-of-RIB: 9
    L2VPN EVPN End-of-RIB received: Yes
      Received 03:31:01
      Number of stale paths removed after graceful restart: 0
      Number of paths received before End-of-RIB: 26
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
    Updates:                     12852     34463
    Keepalives:                    233       236
    Enhanced Route Refresh:          0         0
    Begin of Route Refresh:          0         0
    End of Route Refresh:            0         0
    Total messages:              13086     34700
  Prefix Statistics:
                                   Sent      Rcvd     Best Paths     Best ECMP Paths
    IPv4 Unicast:                     0         0              0                   0
    IPv4 Dps:                        13        13             13                   6
    IPv6 Unicast:                     0         0              0                   0
    EVPN:                            28        28             26                   5
  Configured maximum total number of routes is 12000
  Inbound updates dropped by reason:
    AS path loop detection: 0
    Cluster ID loop detection: 0
    Enforced First AS: 0
    Malformed MPBGP routes: 0
    Originator ID matches local router ID: 0
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
  Inbound route map for L2VPN EVPN is SET_COMM_EDGE
  Additional-paths send mode:
    Dps: any
Local AS is 65000, local router ID 10.255.255.4
TTL is 255
Local TCP address is 10.255.255.4, local port is 34325
Remote TCP address is 10.255.255.1, remote port is 179
Local next hop for next hop self:
  Dps: 10.255.255.4
  L2VPN EVPN: 10.255.255.4
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
    Retransmission Timeout (rto): 212.0ms
    Round-trip Time (rtt/rtvar): 9.4ms/11.9ms
    Delayed Ack Timeout (ato): 40.0ms
    Congestion Window (cwnd): 2
    TCP Throughput: 2.47 Mbps
    Recv Round-trip Time (rcv_rtt): 36.4ms
    Advertised Recv Window (rcv_space): 14480

BGP neighbor is 10.255.255.2, remote AS 65000, internal link
  BGP version 4, remote router ID 0.0.0.0, VRF default
  Inherits configuration from and member of peer-group autovpnEdges
  Last read never, last write never
  Hold time is 0, keepalive interval is 0 seconds
  Configured hold time is 180, keepalive interval is 60 seconds
  Effective minimum hold time is 3 seconds
  Send failure hold time is 0 seconds
  Hold timer is inactive
  Keepalive timer is inactive
  Connect timer is active, time left: 00:00:18
  Connection interval is 20 seconds
  Failed connection attempts is 562
  Idle-restart timer is inactive
  BGP state is Connect
  Number of transitions to established: 0
  Last state was Active
  Last event was ConnectRetry
  Last sent socket-error:Connect (Network is unreachable), Last time 03:33:19, First time 03:33:45, Repeats 3
  Types of communities advertised: extended
  Neighbor is a route reflector client
  Neighbor is using global cluster ID 10.255.255.4
  Neighbor Capabilities:
  Restart timer is inactive
  End of rib timer is inactive
  AIGP attribute send and receive for IPv4 Unicast are enabled
  AIGP attribute send and receive for IPv4 with MPLS Labels are enabled
  AIGP attribute send and receive for IPv6 Unicast are enabled
  AIGP attribute send and receive for IPv6 with MPLS Labels are enabled
  BGP session driven failover for IPv6 Unicast is disabled
  BGP session driven failover for IPv4 Unicast is disabled
  Message Statistics:
                         Sent      Rcvd
    Opens:                  0         0
    Notifications:          0         0
    Updates:                0         0
    Keepalives:             0         0
    Route Refresh:          0         0
    Total messages:         0         0
  Prefix Statistics:
                                   Sent      Rcvd     Best Paths     Best ECMP Paths
    IPv4 Unicast:                     0         0              0                   0
    IPv6 Unicast:                     0         0              0                   0
  Configured maximum total number of routes is 12000
  Inbound updates dropped by reason:
    AS path loop detection: 0
    Cluster ID loop detection: 0
    Enforced First AS: 0
    Malformed MPBGP routes: 0
    Originator ID matches local router ID: 0
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
    Link-state NLRIs dropped because reception is unsupported: 0
    RT Membership NLRIs dropped due to local origin ASN received from external peer: 0
  Outbound paths dropped by reason:
    IPv4 local address not available: 0
    IPv6 local address not available: 0
  Inbound route map for L2VPN EVPN is SET_COMM_EDGE
Local AS is 65000, local router ID 10.255.255.4
TTL is 255
Local TCP address is 10.255.255.4
Remote TCP address is 10.255.255.2, remote port is 179
BFD is enabled with configured transmit interval 1000ms, receive interval 1000ms, multiplier 3 and state is Down
TCP Socket Information:
  TCP state is SYN-SENT
  Recv-Q: 0/131072
  Send-Q: 0/16384
  Outgoing Maximum Segment Size (MSS): 524
  Total Number of TCP retransmissions: 2
  Options:
    Timestamps enabled: no
    Selective Acknowledgments enabled: no
    Window Scale enabled: no
    Explicit Congestion Notification (ECN) enabled: no
  Socket Statistics:
    Window Scale (wscale): 0,0
    Retransmission Timeout (rto): 4000.0ms
    Round-trip Time (rtt/rtvar): 0.0ms/250.0ms
    Delayed Ack Timeout (ato): 0.0ms
    Congestion Window (cwnd): 1
    Slow-start Threshold (ssthresh): 7

BGP neighbor is 10.255.255.5, remote AS 65000, internal link
  BGP version 4, remote router ID 10.255.255.5, VRF default
  Inherits configuration from and member of peer-group autovpnEdges
  Last read 00:00:21, last write 00:00:07
  Hold time is 180, keepalive interval is 60 seconds
  Configured hold time is 180, keepalive interval is 60 seconds
  Effective minimum hold time is 3 seconds
  Send failure hold time is 0 seconds
  Hold timer is active, time left: 00:02:39
  Keepalive timer is active, time left: 00:00:34
  Connect timer is inactive
  Idle-restart timer is inactive
  BGP state is Established, up for 03:14:19
  Number of transitions to established: 1
  Last state was OpenConfirm
  Last event was RecvUpdate
  Types of communities advertised: extended
  Enhanced route refresh stale path removal disabled
  Outbound enhanced route refresh enabled
  Neighbor is a route reflector client
  Neighbor is using global cluster ID 10.255.255.4
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
      Received 03:14:19
      Number of stale paths removed after graceful restart: 0
      Number of paths received before End-of-RIB: 2
    L2VPN EVPN End-of-RIB received: Yes
      Received 03:14:19
      Number of stale paths removed after graceful restart: 0
      Number of paths received before End-of-RIB: 4
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
    Updates:                       132        11
    Keepalives:                    220       227
    Enhanced Route Refresh:          0         0
    Begin of Route Refresh:          0         0
    End of Route Refresh:            0         0
    Total messages:                353       239
  Prefix Statistics:
                                   Sent      Rcvd     Best Paths     Best ECMP Paths
    IPv4 Unicast:                     0         0              0                   0
    IPv4 Dps:                        24         2              2                   2
    IPv6 Unicast:                     0         0              0                   0
    EVPN:                            43         3              3                   0
  Configured maximum total number of routes is 12000
  Inbound updates dropped by reason:
    AS path loop detection: 0
    Cluster ID loop detection: 0
    Enforced First AS: 0
    Malformed MPBGP routes: 0
    Originator ID matches local router ID: 0
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
  Inbound route map for L2VPN EVPN is SET_COMM_EDGE
  Additional-paths send mode:
    Dps: any
Local AS is 65000, local router ID 10.255.255.4
TTL is 255
Local TCP address is 10.255.255.4, local port is 179
Remote TCP address is 10.255.255.5, remote port is 36245
Local next hop for next hop self:
  Dps: 10.255.255.4
  L2VPN EVPN: 10.255.255.4
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
    Round-trip Time (rtt/rtvar): 2.6ms/0.9ms
    Delayed Ack Timeout (ato): 40.0ms
    Congestion Window (cwnd): 10
    TCP Throughput: 43.88 Mbps
    Recv Round-trip Time (rcv_rtt): 4.0ms
    Advertised Recv Window (rcv_space): 14600

BGP neighbor is 10.255.255.6, remote AS 65000, internal link
  BGP version 4, remote router ID 10.255.255.6, VRF default
  Inherits configuration from and member of peer-group autovpnEdges
  Last read 00:00:17, last write 00:00:54
  Hold time is 180, keepalive interval is 60 seconds
  Configured hold time is 180, keepalive interval is 60 seconds
  Effective minimum hold time is 3 seconds
  Send failure hold time is 0 seconds
  Hold timer is active, time left: 00:02:43
  Keepalive timer is inactive
  Connect timer is inactive
  Idle-restart timer is inactive
  BGP state is Established, up for 00:13:50
  Number of transitions to established: 1
  Last state was OpenConfirm
  Last event was RecvUpdate
  Types of communities advertised: extended
  Enhanced route refresh stale path removal disabled
  Outbound enhanced route refresh enabled
  Neighbor is a route reflector client
  Neighbor is using global cluster ID 10.255.255.4
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
      Received 00:13:50
      Number of stale paths removed after graceful restart: 0
      Number of paths received before End-of-RIB: 2
    L2VPN EVPN End-of-RIB received: Yes
      Received 00:13:50
      Number of stale paths removed after graceful restart: 0
      Number of paths received before End-of-RIB: 1
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
    Updates:                        85         6
    Keepalives:                     13        18
    Enhanced Route Refresh:          0         0
    Begin of Route Refresh:          0         0
    End of Route Refresh:            0         0
    Total messages:                 99        25
  Prefix Statistics:
                                   Sent      Rcvd     Best Paths     Best ECMP Paths
    IPv4 Unicast:                     0         0              0                   0
    IPv4 Dps:                        24         2              2                   2
    IPv6 Unicast:                     0         0              0                   0
    EVPN:                            43         3              3                   2
  Configured maximum total number of routes is 12000
  Inbound updates dropped by reason:
    AS path loop detection: 0
    Cluster ID loop detection: 0
    Enforced First AS: 0
    Malformed MPBGP routes: 0
    Originator ID matches local router ID: 0
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
  Inbound route map for L2VPN EVPN is SET_COMM_EDGE
  Additional-paths send mode:
    Dps: any
Local AS is 65000, local router ID 10.255.255.4
TTL is 255
Local TCP address is 10.255.255.4, local port is 179
Remote TCP address is 10.255.255.6, remote port is 37775
Local next hop for next hop self:
  Dps: 10.255.255.4
  L2VPN EVPN: 10.255.255.4
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
    Round-trip Time (rtt/rtvar): 2.7ms/1.1ms
    Delayed Ack Timeout (ato): 40.0ms
    Congestion Window (cwnd): 10
    TCP Throughput: 42.37 Mbps
    Recv Round-trip Time (rcv_rtt): 4.0ms
    Advertised Recv Window (rcv_space): 14600

BGP neighbor is 10.255.255.8, remote AS 65000, internal link
  BGP version 4, remote router ID 10.255.255.8, VRF default
  Inherits configuration from and member of peer-group autovpnEdges
  Last read 00:00:13, last write 00:00:12
  Hold time is 180, keepalive interval is 60 seconds
  Configured hold time is 180, keepalive interval is 60 seconds
  Effective minimum hold time is 3 seconds
  Send failure hold time is 0 seconds
  Hold timer is active, time left: 00:02:47
  Keepalive timer is active, time left: 00:00:39
  Connect timer is inactive
  Idle-restart timer is inactive
  BGP state is Established, up for 03:31:09
  Number of transitions to established: 1
  Last state was OpenConfirm
  Last event was Established
  Types of communities advertised: extended
  Enhanced route refresh stale path removal disabled
  Outbound enhanced route refresh enabled
  Neighbor is a route reflector client
  Neighbor is using global cluster ID 10.255.255.4
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
      Received 03:31:09
      Number of stale paths removed after graceful restart: 0
      Number of paths received before End-of-RIB: 2
    L2VPN EVPN End-of-RIB received: Yes
      Received 03:31:09
      Number of stale paths removed after graceful restart: 0
      Number of paths received before End-of-RIB: 4
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
    Updates:                     21770        12
    Keepalives:                    232       249
    Enhanced Route Refresh:          0         0
    Begin of Route Refresh:          0         0
    End of Route Refresh:            0         0
    Total messages:              22003       262
  Prefix Statistics:
                                   Sent      Rcvd     Best Paths     Best ECMP Paths
    IPv4 Unicast:                     0         0              0                   0
    IPv4 Dps:                        24         2              2                   0
    IPv6 Unicast:                     0         0              0                   0
    EVPN:                            44         3              3                   2
  Configured maximum total number of routes is 12000
  Inbound updates dropped by reason:
    AS path loop detection: 0
    Cluster ID loop detection: 0
    Enforced First AS: 0
    Malformed MPBGP routes: 0
    Originator ID matches local router ID: 0
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
  Inbound route map for L2VPN EVPN is SET_COMM_EDGE
  Additional-paths send mode:
    Dps: any
Local AS is 65000, local router ID 10.255.255.4
TTL is 255
Local TCP address is 10.255.255.4, local port is 179
Remote TCP address is 10.255.255.8, remote port is 34621
Local next hop for next hop self:
  Dps: 10.255.255.4
  L2VPN EVPN: 10.255.255.4
BFD is enabled with configured transmit interval 1000ms, receive interval 1000ms, multiplier 3 and state is Up
TCP Socket Information:
  TCP state is ESTABLISHED
  Recv-Q: 0/32768
  Send-Q: 0/46080
  Outgoing Maximum Segment Size (MSS): 1284
  Total Number of TCP retransmissions: 2
  Options:
    Timestamps enabled: yes
    Selective Acknowledgments enabled: yes
    Window Scale enabled: yes
    Explicit Congestion Notification (ECN) enabled: no
  Socket Statistics:
    Window Scale (wscale): 7,7
    Retransmission Timeout (rto): 208.0ms
    Round-trip Time (rtt/rtvar): 6.7ms/5.0ms
    Delayed Ack Timeout (ato): 40.0ms
    Congestion Window (cwnd): 8
    TCP Throughput: 12.33 Mbps
    Advertised Recv Window (rcv_space): 14600

BGP neighbor is 10.255.255.10, remote AS 65000, internal link
  BGP version 4, remote router ID 10.255.255.10, VRF default
  Inherits configuration from and member of peer-group autovpnEdges
  Last read 00:00:39, last write 00:00:51
  Hold time is 180, keepalive interval is 60 seconds
  Configured hold time is 180, keepalive interval is 60 seconds
  Effective minimum hold time is 3 seconds
  Send failure hold time is 0 seconds
  Hold timer is active, time left: 00:02:21
  Keepalive timer is active, time left: 00:00:01
  Connect timer is inactive
  Idle-restart timer is inactive
  BGP state is Established, up for 01:44:03
  Number of transitions to established: 1
  Last state was OpenConfirm
  Last event was RecvUpdate
  Types of communities advertised: extended
  Enhanced route refresh stale path removal disabled
  Outbound enhanced route refresh enabled
  Neighbor is a route reflector client
  Neighbor is using global cluster ID 10.255.255.4
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
      Received 01:44:02
      Number of stale paths removed after graceful restart: 0
      Number of paths received before End-of-RIB: 2
    L2VPN EVPN End-of-RIB received: Yes
      Received 01:44:02
      Number of stale paths removed after graceful restart: 0
      Number of paths received before End-of-RIB: 1
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
    Updates:                       123         7
    Keepalives:                    116       123
    Enhanced Route Refresh:          0         0
    Begin of Route Refresh:          0         0
    End of Route Refresh:            0         0
    Total messages:                240       131
  Prefix Statistics:
                                   Sent      Rcvd     Best Paths     Best ECMP Paths
    IPv4 Unicast:                     0         0              0                   0
    IPv4 Dps:                        24         2              2                   0
    IPv6 Unicast:                     0         0              0                   0
    EVPN:                            44         3              3                   2
  Configured maximum total number of routes is 12000
  Inbound updates dropped by reason:
    AS path loop detection: 0
    Cluster ID loop detection: 0
    Enforced First AS: 0
    Malformed MPBGP routes: 0
    Originator ID matches local router ID: 0
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
  Inbound route map for L2VPN EVPN is SET_COMM_EDGE
  Additional-paths send mode:
    Dps: any
Local AS is 65000, local router ID 10.255.255.4
TTL is 255
Local TCP address is 10.255.255.4, local port is 179
Remote TCP address is 10.255.255.10, remote port is 35215
Local next hop for next hop self:
  Dps: 10.255.255.4
  L2VPN EVPN: 10.255.255.4
BFD is enabled with configured transmit interval 1000ms, receive interval 1000ms, multiplier 3 and state is Up
TCP Socket Information:
  TCP state is ESTABLISHED
  Recv-Q: 0/32768
  Send-Q: 0/46080
  Outgoing Maximum Segment Size (MSS): 1372
  Total Number of TCP retransmissions: 0
  Options:
    Timestamps enabled: yes
    Selective Acknowledgments enabled: yes
    Window Scale enabled: yes
    Explicit Congestion Notification (ECN) enabled: no
  Socket Statistics:
    Window Scale (wscale): 7,7
    Retransmission Timeout (rto): 204.0ms
    Round-trip Time (rtt/rtvar): 3.5ms/1.5ms
    Delayed Ack Timeout (ato): 40.0ms
    Congestion Window (cwnd): 10
    TCP Throughput: 31.64 Mbps
    Recv Round-trip Time (rcv_rtt): 1.0ms
    Advertised Recv Window (rcv_space): 14600

BGP neighbor is 10.255.255.11, remote AS 65000, internal link
  BGP version 4, remote router ID 10.255.255.11, VRF default
  Inherits configuration from and member of peer-group autovpnEdges
  Last read 00:00:27, last write 00:00:50
  Hold time is 180, keepalive interval is 60 seconds
  Configured hold time is 180, keepalive interval is 60 seconds
  Effective minimum hold time is 3 seconds
  Send failure hold time is 0 seconds
  Hold timer is active, time left: 00:02:33
  Keepalive timer is inactive
  Connect timer is inactive
  Idle-restart timer is inactive
  BGP state is Established, up for 00:11:29
  Number of transitions to established: 1
  Last state was OpenConfirm
  Last event was RecvUpdate
  Types of communities advertised: extended
  Enhanced route refresh stale path removal disabled
  Outbound enhanced route refresh enabled
  Neighbor is a route reflector client
  Neighbor is using global cluster ID 10.255.255.4
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
      Received 00:11:29
      Number of stale paths removed after graceful restart: 0
      Number of paths received before End-of-RIB: 2
    L2VPN EVPN End-of-RIB received: Yes
      Received 00:11:29
      Number of stale paths removed after graceful restart: 0
      Number of paths received before End-of-RIB: 1
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
    Updates:                        73         6
    Keepalives:                     11        15
    Enhanced Route Refresh:          0         0
    Begin of Route Refresh:          0         0
    End of Route Refresh:            0         0
    Total messages:                 85        22
  Prefix Statistics:
                                   Sent      Rcvd     Best Paths     Best ECMP Paths
    IPv4 Unicast:                     0         0              0                   0
    IPv4 Dps:                        24         2              2                   2
    IPv6 Unicast:                     0         0              0                   0
    EVPN:                            43         3              3                   2
  Configured maximum total number of routes is 12000
  Inbound updates dropped by reason:
    AS path loop detection: 0
    Cluster ID loop detection: 0
    Enforced First AS: 0
    Malformed MPBGP routes: 0
    Originator ID matches local router ID: 0
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
  Inbound route map for L2VPN EVPN is SET_COMM_EDGE
  Additional-paths send mode:
    Dps: any
Local AS is 65000, local router ID 10.255.255.4
TTL is 255
Local TCP address is 10.255.255.4, local port is 179
Remote TCP address is 10.255.255.11, remote port is 36151
Local next hop for next hop self:
  Dps: 10.255.255.4
  L2VPN EVPN: 10.255.255.4
BFD is enabled with configured transmit interval 1000ms, receive interval 1000ms, multiplier 3 and state is Up
TCP Socket Information:
  TCP state is ESTABLISHED
  Recv-Q: 0/32768
  Send-Q: 0/46080
  Outgoing Maximum Segment Size (MSS): 1372
  Total Number of TCP retransmissions: 0
  Options:
    Timestamps enabled: yes
    Selective Acknowledgments enabled: yes
    Window Scale enabled: yes
    Explicit Congestion Notification (ECN) enabled: no
  Socket Statistics:
    Window Scale (wscale): 7,7
    Retransmission Timeout (rto): 204.0ms
    Round-trip Time (rtt/rtvar): 3.7ms/1.1ms
    Delayed Ack Timeout (ato): 40.0ms
    Congestion Window (cwnd): 10
    TCP Throughput: 29.97 Mbps
    Recv Round-trip Time (rcv_rtt): 4.0ms
    Advertised Recv Window (rcv_space): 14600

BGP neighbor is 10.255.255.12, remote AS 65000, internal link
  BGP version 4, remote router ID 10.255.255.12, VRF default
  Inherits configuration from and member of peer-group autovpnEdges
  Last read 00:00:23, last write 00:00:21
  Hold time is 180, keepalive interval is 60 seconds
  Configured hold time is 180, keepalive interval is 60 seconds
  Effective minimum hold time is 3 seconds
  Send failure hold time is 0 seconds
  Hold timer is active, time left: 00:02:37
  Keepalive timer is active, time left: 00:00:26
  Connect timer is inactive
  Idle-restart timer is inactive
  BGP state is Established, up for 03:29:14
  Number of transitions to established: 1
  Last state was OpenConfirm
  Last event was RecvUpdate
  Types of communities advertised: extended
  Enhanced route refresh stale path removal disabled
  Outbound enhanced route refresh enabled
  Neighbor is a route reflector client
  Neighbor is using global cluster ID 10.255.255.4
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
      Received 03:29:13
      Number of stale paths removed after graceful restart: 0
      Number of paths received before End-of-RIB: 2
    L2VPN EVPN End-of-RIB received: Yes
      Received 03:29:13
      Number of stale paths removed after graceful restart: 0
      Number of paths received before End-of-RIB: 3
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
    Updates:                      9758         8
    Keepalives:                    235       246
    Enhanced Route Refresh:          0         0
    Begin of Route Refresh:          0         0
    End of Route Refresh:            0         0
    Total messages:               9994       255
  Prefix Statistics:
                                   Sent      Rcvd     Best Paths     Best ECMP Paths
    IPv4 Unicast:                     0         0              0                   0
    IPv4 Dps:                        24         2              2                   0
    IPv6 Unicast:                     0         0              0                   0
    EVPN:                            46         3              3                   0
  Configured maximum total number of routes is 12000
  Inbound updates dropped by reason:
    AS path loop detection: 0
    Cluster ID loop detection: 0
    Enforced First AS: 0
    Malformed MPBGP routes: 0
    Originator ID matches local router ID: 0
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
  Inbound route map for L2VPN EVPN is SET_COMM_EDGE
  Additional-paths send mode:
    Dps: any
Local AS is 65000, local router ID 10.255.255.4
TTL is 255
Local TCP address is 10.255.255.4, local port is 179
Remote TCP address is 10.255.255.12, remote port is 43595
Local next hop for next hop self:
  Dps: 10.255.255.4
  L2VPN EVPN: 10.255.255.4
BFD is enabled with configured transmit interval 1000ms, receive interval 1000ms, multiplier 3 and state is Up
TCP Socket Information:
  TCP state is ESTABLISHED
  Recv-Q: 0/32768
  Send-Q: 0/46080
  Outgoing Maximum Segment Size (MSS): 1372
  Total Number of TCP retransmissions: 0
  Options:
    Timestamps enabled: yes
    Selective Acknowledgments enabled: yes
    Window Scale enabled: yes
    Explicit Congestion Notification (ECN) enabled: no
  Socket Statistics:
    Window Scale (wscale): 7,7
    Retransmission Timeout (rto): 204.0ms
    Round-trip Time (rtt/rtvar): 3.7ms/1.1ms
    Delayed Ack Timeout (ato): 40.0ms
    Congestion Window (cwnd): 10
    TCP Throughput: 29.97 Mbps
    Recv Round-trip Time (rcv_rtt): 4.0ms
    Advertised Recv Window (rcv_space): 14600

```

## show bgp path-selection detail

```text
BGP routing table information for VRF default
Router identifier 10.255.255.4, local AS number 65000
Bgp routing table entry for ipv4Dps VTEP 10.255.255.5/32
 Paths: 2 available
  Local (Received from a RR-client)
    :: from 10.255.255.5 (10.255.255.5)
      Origin IGP, metric -, localpref 100, weight 0, received 03:14:20 ago, valid, internal
      Tunnel encapsulation attribute: Dynamic path selection
        Endpoint: 172.16.0.1, Path group name: VZ_OFF, WAN ID: 1, UDP port: 4500
  Local (Received from a RR-client)
    :: from 10.255.255.1 (10.255.255.1)
      Origin IGP, metric -, localpref 100, weight 0, received 03:14:19 ago, valid, internal
      Tunnel encapsulation attribute: Dynamic path selection
        Endpoint: 172.16.0.1, Path group name: VZ_OFF, WAN ID: 1, UDP port: 4500
Bgp routing table entry for ipv4Dps VTEP 10.255.255.6/32
 Paths: 2 available
  Local (Received from a RR-client)
    :: from 10.255.255.6 (10.255.255.6)
      Origin IGP, metric -, localpref 100, weight 0, received 00:13:51 ago, valid, internal
      Tunnel encapsulation attribute: Dynamic path selection
        Endpoint: 172.16.0.3, Path group name: VZ_OFF, WAN ID: 1, UDP port: 4500
  Local (Received from a RR-client)
    :: from 10.255.255.1 (10.255.255.1)
      Origin IGP, metric -, localpref 100, weight 0, received 00:13:47 ago, valid, internal
      Tunnel encapsulation attribute: Dynamic path selection
        Endpoint: 172.16.0.3, Path group name: VZ_OFF, WAN ID: 1, UDP port: 4500
Bgp routing table entry for ipv4Dps VTEP 10.255.255.8/32
 Paths: 2 available
  Local (Received from a RR-client)
    :: from 10.255.255.1 (10.255.255.1)
      Origin IGP, metric -, localpref 100, weight 0, received 03:31:11 ago, valid, internal
      Tunnel encapsulation attribute: Dynamic path selection
        Endpoint: 172.16.1.2, Path group name: VZ_NEAR, WAN ID: 1, UDP port: 4500
  Local (Received from a RR-client)
    :: from 10.255.255.8 (10.255.255.8)
      Origin IGP, metric -, localpref 100, weight 0, received 03:31:09 ago, valid, internal
      Tunnel encapsulation attribute: Dynamic path selection
        Endpoint: 172.16.1.2, Path group name: VZ_NEAR, WAN ID: 1, UDP port: 4500
Bgp routing table entry for ipv4Dps VTEP 10.255.255.10/32
 Paths: 2 available
  Local (Received from a RR-client)
    :: from 10.255.255.1 (10.255.255.1)
      Origin IGP, metric -, localpref 100, weight 0, received 01:44:08 ago, valid, internal
      Tunnel encapsulation attribute: Dynamic path selection
        Endpoint: 172.16.1.7, Path group name: VZ_NEAR, WAN ID: 1, UDP port: 4500
  Local (Received from a RR-client)
    :: from 10.255.255.10 (10.255.255.10)
      Origin IGP, metric -, localpref 100, weight 0, received 01:44:03 ago, valid, internal
      Tunnel encapsulation attribute: Dynamic path selection
        Endpoint: 172.16.1.7, Path group name: VZ_NEAR, WAN ID: 1, UDP port: 4500
Bgp routing table entry for ipv4Dps VTEP 10.255.255.11/32
 Paths: 2 available
  Local (Received from a RR-client)
    :: from 10.255.255.11 (10.255.255.11)
      Origin IGP, metric -, localpref 100, weight 0, received 00:11:30 ago, valid, internal
      Tunnel encapsulation attribute: Dynamic path selection
        Endpoint: 172.16.0.9, Path group name: VZ_OFF, WAN ID: 2, UDP port: 4500
  Local (Received from a RR-client)
    :: from 10.255.255.1 (10.255.255.1)
      Origin IGP, metric -, localpref 100, weight 0, received 00:11:29 ago, valid, internal
      Tunnel encapsulation attribute: Dynamic path selection
        Endpoint: 172.16.0.9, Path group name: VZ_OFF, WAN ID: 2, UDP port: 4500
Bgp routing table entry for ipv4Dps VTEP 10.255.255.12/32
 Paths: 2 available
  Local (Received from a RR-client)
    :: from 10.255.255.1 (10.255.255.1)
      Origin IGP, metric -, localpref 100, weight 0, received 03:32:30 ago, valid, internal
      Tunnel encapsulation attribute: Dynamic path selection
        Endpoint: 172.16.0.11, Path group name: VZ_OFF, WAN ID: 2, UDP port: 4500
  Local (Received from a RR-client)
    :: from 10.255.255.12 (10.255.255.12)
      Origin IGP, metric -, localpref 100, weight 0, received 03:29:14 ago, valid, internal
      Tunnel encapsulation attribute: Dynamic path selection
        Endpoint: 172.16.0.11, Path group name: VZ_OFF, WAN ID: 2, UDP port: 4500
Bgp routing table entry for ipv4Ipsec VTEP 10.255.255.1/32
 Paths: 1 available
  Local (Received from a RR-client)
    :: from 10.255.255.1 (10.255.255.1)
      Origin IGP, metric -, localpref 100, weight 0, received 03:32:31 ago, valid, internal
      Tunnel encapsulation attribute: IP security
        Initial contact: false, Rekey counter: 0, Nonce length: 32
        DH group: 14, DH key length: 256
        Encryption algo: aes256, Authentication algo: sha256
Bgp routing table entry for ipv4Ipsec VTEP 10.255.255.4/32
 Paths: 1 available
  Local
    - from - (0.0.0.0)
      Origin IGP, metric -, localpref -, weight 0, received 03:32:50 ago, valid, local
      Tunnel encapsulation attribute: IP security
        Initial contact: false, Rekey counter: 0, Nonce length: 32
        DH group: 14, DH key length: 256
        Encryption algo: aes256, Authentication algo: sha256
Bgp routing table entry for ipv4Ipsec VTEP 10.255.255.5/32
 Paths: 2 available
  Local (Received from a RR-client)
    :: from 10.255.255.5 (10.255.255.5)
      Origin IGP, metric -, localpref 100, weight 0, received 03:14:20 ago, valid, internal
      Tunnel encapsulation attribute: IP security
        Initial contact: false, Rekey counter: 0, Nonce length: 32
        DH group: 14, DH key length: 256
        Encryption algo: aes256, Authentication algo: sha256
  Local (Received from a RR-client)
    :: from 10.255.255.1 (10.255.255.1)
      Origin IGP, metric -, localpref 100, weight 0, received 03:14:19 ago, valid, internal
      Tunnel encapsulation attribute: IP security
        Initial contact: false, Rekey counter: 0, Nonce length: 32
        DH group: 14, DH key length: 256
        Encryption algo: aes256, Authentication algo: sha256
Bgp routing table entry for ipv4Ipsec VTEP 10.255.255.6/32
 Paths: 2 available
  Local (Received from a RR-client)
    :: from 10.255.255.6 (10.255.255.6)
      Origin IGP, metric -, localpref 100, weight 0, received 00:13:51 ago, valid, internal
      Tunnel encapsulation attribute: IP security
        Initial contact: false, Rekey counter: 0, Nonce length: 32
        DH group: 14, DH key length: 256
        Encryption algo: aes256, Authentication algo: sha256
  Local (Received from a RR-client)
    :: from 10.255.255.1 (10.255.255.1)
      Origin IGP, metric -, localpref 100, weight 0, received 00:13:47 ago, valid, internal
      Tunnel encapsulation attribute: IP security
        Initial contact: false, Rekey counter: 0, Nonce length: 32
        DH group: 14, DH key length: 256
        Encryption algo: aes256, Authentication algo: sha256
Bgp routing table entry for ipv4Ipsec VTEP 10.255.255.8/32
 Paths: 2 available
  Local (Received from a RR-client)
    :: from 10.255.255.1 (10.255.255.1)
      Origin IGP, metric -, localpref 100, weight 0, received 03:31:11 ago, valid, internal
      Tunnel encapsulation attribute: IP security
        Initial contact: false, Rekey counter: 0, Nonce length: 32
        DH group: 14, DH key length: 256
        Encryption algo: aes256, Authentication algo: sha256
  Local (Received from a RR-client)
    :: from 10.255.255.8 (10.255.255.8)
      Origin IGP, metric -, localpref 100, weight 0, received 03:31:09 ago, valid, internal
      Tunnel encapsulation attribute: IP security
        Initial contact: false, Rekey counter: 0, Nonce length: 32
        DH group: 14, DH key length: 256
        Encryption algo: aes256, Authentication algo: sha256
Bgp routing table entry for ipv4Ipsec VTEP 10.255.255.10/32
 Paths: 2 available
  Local (Received from a RR-client)
    :: from 10.255.255.1 (10.255.255.1)
      Origin IGP, metric -, localpref 100, weight 0, received 01:44:08 ago, valid, internal
      Tunnel encapsulation attribute: IP security
        Initial contact: false, Rekey counter: 0, Nonce length: 32
        DH group: 14, DH key length: 256
        Encryption algo: aes256, Authentication algo: sha256
  Local (Received from a RR-client)
    :: from 10.255.255.10 (10.255.255.10)
      Origin IGP, metric -, localpref 100, weight 0, received 01:44:03 ago, valid, internal
      Tunnel encapsulation attribute: IP security
        Initial contact: false, Rekey counter: 0, Nonce length: 32
        DH group: 14, DH key length: 256
        Encryption algo: aes256, Authentication algo: sha256
Bgp routing table entry for ipv4Ipsec VTEP 10.255.255.11/32
 Paths: 2 available
  Local (Received from a RR-client)
    :: from 10.255.255.11 (10.255.255.11)
      Origin IGP, metric -, localpref 100, weight 0, received 00:11:30 ago, valid, internal
      Tunnel encapsulation attribute: IP security
        Initial contact: false, Rekey counter: 0, Nonce length: 32
        DH group: 14, DH key length: 256
        Encryption algo: aes256, Authentication algo: sha256
  Local (Received from a RR-client)
    :: from 10.255.255.1 (10.255.255.1)
      Origin IGP, metric -, localpref 100, weight 0, received 00:11:29 ago, valid, internal
      Tunnel encapsulation attribute: IP security
        Initial contact: false, Rekey counter: 0, Nonce length: 32
        DH group: 14, DH key length: 256
        Encryption algo: aes256, Authentication algo: sha256
Bgp routing table entry for ipv4Ipsec VTEP 10.255.255.12/32
 Paths: 2 available
  Local (Received from a RR-client)
    :: from 10.255.255.1 (10.255.255.1)
      Origin IGP, metric -, localpref 100, weight 0, received 03:32:30 ago, valid, internal
      Tunnel encapsulation attribute: IP security
        Initial contact: false, Rekey counter: 0, Nonce length: 32
        DH group: 14, DH key length: 256
        Encryption algo: aes256, Authentication algo: sha256
  Local (Received from a RR-client)
    :: from 10.255.255.12 (10.255.255.12)
      Origin IGP, metric -, localpref 100, weight 0, received 03:29:14 ago, valid, internal
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
>C    10.255.255.4/32 [0 pref/0 metric] updated 03:33:51 ago
         via Loopback0, directly connected
>C    172.16.0.6/31 [0 pref/0 metric] updated 03:32:49 ago
         via Ethernet1/4, directly connected
>C    172.16.1.4/31 [0 pref/0 metric] updated 03:32:49 ago
         via Ethernet1/3, directly connected
>C    172.28.128.0/20 [0 pref/0 metric] updated 03:33:21 ago
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
>S    10.80.0.0/12 [1 pref/0 metric] updated 03:33:21 ago
         via 172.28.128.1 [0 pref/0 metric] type ipv4
            via 172.28.128.1, Management1/1
>S    10.224.0.0/12 [1 pref/0 metric] updated 03:33:21 ago
         via 172.28.128.1 [0 pref/0 metric] type ipv4
            via 172.28.128.1, Management1/1
>S    10.240.0.0/12 [1 pref/0 metric] updated 03:33:21 ago
         via 172.28.128.1 [0 pref/0 metric] type ipv4
            via 172.28.128.1, Management1/1
>S    172.16.0.0/12 [1 pref/0 metric] updated 03:33:21 ago
         via 172.28.128.1 [0 pref/0 metric] type ipv4
            via 172.28.128.1, Management1/1
>S    172.16.0.0/24 [1 pref/0 metric] updated 03:32:49 ago
         via 172.16.0.6 [0 pref/0 metric] type ipv4
            via 172.16.0.6, Ethernet1/4
>S    172.16.1.0/24 [1 pref/0 metric] updated 03:32:49 ago
         via 172.16.1.4 [0 pref/0 metric] type ipv4
            via 172.16.1.4, Ethernet1/3
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
>P    0.0.0.0/8 [1 pref/0 metric] updated 03:33:50 ago
         via Null0, directly connected [NF]
>P    10.255.255.1/32 [1 pref/0 metric] updated 03:32:45 ago
         via 10.255.255.1, Dps1
>P    10.255.255.3/32 [1 pref/0 metric] updated 03:32:51 ago
         via 10.255.255.3, Dps1
>P    10.255.255.5/32 [1 pref/0 metric] updated 03:32:26 ago
         via 10.255.255.5, Dps1
>P    10.255.255.6/32 [1 pref/0 metric] updated 03:32:24 ago
         via 10.255.255.6, Dps1
>P    10.255.255.8/32 [1 pref/0 metric] updated 03:32:16 ago
         via 10.255.255.8, Dps1
>P    10.255.255.10/32 [1 pref/0 metric] updated 03:31:36 ago
         via 10.255.255.10, Dps1
>P    10.255.255.11/32 [1 pref/0 metric] updated 03:30:28 ago
         via 10.255.255.11, Dps1
>P    10.255.255.12/32 [1 pref/0 metric] updated 03:30:26 ago
         via 10.255.255.12, Dps1
>P    127.0.0.0/8 [1 pref/0 metric] updated 03:33:50 ago
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
>P    ::/96 [1 pref/0 metric] updated 03:32:52 ago
         via Null0, directly connected [NF]
>P    ::ffff:127.0.0.0/104 [1 pref/0 metric] updated 03:32:52 ago
         via :: [1 pref/1 metric] type ipv6
            via , directly connected
>P    fe80::/10 [1 pref/0 metric] updated 03:32:52 ago
```

