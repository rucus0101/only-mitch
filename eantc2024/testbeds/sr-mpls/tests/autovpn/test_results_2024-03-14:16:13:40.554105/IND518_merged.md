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

Uptime: 2 hours and 28 minutes
Total memory: 65396488 kB
Free memory: 39548536 kB

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
Et1/1                5:00     21.8   0.2%        2     10.9   0.1%        1
Et1/3     VZ_NEAR    5:00     12.9   0.1%        1     13.8   0.1%        1
Et1/4     VZ_OFF     5:00      0.1   0.0%        0      0.1   0.0%        0
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
 S        10.255.255.8/32
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
 C        172.16.255.0/31
           directly connected, Ethernet1/2
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
 S        10.255.255.8/32
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
 C        172.16.255.0/31
           directly connected, Ethernet1/2
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
 B I      10.1.255.0/31 [20/0]
           via VTEP 10.255.255.1 VNI 201 router-mac ec:8a:48:04:f5:30
 B I      10.1.255.2/31 [20/0]
           via VTEP 10.255.255.1 VNI 201 router-mac ec:8a:48:04:f5:30
 B I      10.2.255.0/31 [20/0]
           via VTEP 10.255.255.8 VNI 201 router-mac ec:8a:48:04:2c:53
 B I      10.2.255.2/31 [20/0]
           via VTEP 10.255.255.8 VNI 201 router-mac ec:8a:48:04:2c:53
 B I      10.4.255.0/31 [20/0]
           via VTEP 10.255.255.10 VNI 201 router-mac 00:0c:29:d5:32:d4
 B I      10.4.255.2/31 [20/0]
           via VTEP 10.255.255.10 VNI 201 router-mac 00:0c:29:d5:32:d4
 O        10.5.255.0/31 [110/20]
           via 10.5.255.3, Ethernet1/1
 C        10.5.255.2/31
           directly connected, Ethernet1/1
 B I      10.6.255.0/31 [20/0]
           via VTEP 10.255.255.11 VNI 201 router-mac 00:0c:29:ba:2d:5e
 B I      10.6.255.2/31 [20/0]
           via VTEP 10.255.255.12 VNI 201 router-mac 00:0c:29:78:c5:2d
 B I      10.255.254.1/32 [20/0]
           via VTEP 10.255.255.5 VNI 201 router-mac ec:8a:48:04:21:53
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
 B I      192.168.0.0/24 [20/0]
           via VTEP 10.255.255.5 VNI 201 router-mac ec:8a:48:04:21:53
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
                                 10.255.255.5          -       100     0       i Or-ID: 10.255.255.5 C-LST: 10.255.255.1 
 * >      RD: 10.255.255.1:1 ip-prefix 10.1.255.0/31
                                 10.255.255.1          -       100     0       i
 * >      RD: 10.255.255.1:1 ip-prefix 10.1.255.2/31
                                 10.255.255.1          -       100     0       i
 * >      RD: 10.255.255.7:1 ip-prefix 10.2.255.0/31
                                 10.255.255.8          -       100     0       i Or-ID: 10.255.255.8 C-LST: 10.255.255.1 
 * >      RD: 10.255.255.7:1 ip-prefix 10.2.255.2/31
                                 10.255.255.8          -       100     0       i Or-ID: 10.255.255.8 C-LST: 10.255.255.1 
 * >      RD: 10.255.255.10:1 ip-prefix 10.4.255.0/31
                                 10.255.255.10         -       100     0       i Or-ID: 10.255.255.10 C-LST: 10.255.255.1 
 * >      RD: 10.255.255.10:1 ip-prefix 10.4.255.2/31
                                 10.255.255.10         -       100     0       i Or-ID: 10.255.255.10 C-LST: 10.255.255.1 
 * >      RD: 10.255.255.4:1 ip-prefix 10.5.255.0/31
                                 -                     -       -       0       i
 * >      RD: 10.255.255.4:1 ip-prefix 10.5.255.2/31
                                 -                     -       -       0       i
 * >      RD: 10.255.255.11:1 ip-prefix 10.6.255.0/31
                                 10.255.255.11         -       100     0       i Or-ID: 10.255.255.11 C-LST: 10.255.255.1 
 * >      RD: 10.255.255.12:1 ip-prefix 10.6.255.2/31
                                 10.255.255.12         -       100     0       i Or-ID: 10.255.255.12 C-LST: 10.255.255.1 
 * >      RD: 10.255.255.5:1 ip-prefix 10.255.254.1/32
                                 10.255.255.5          -       100     0       i Or-ID: 10.255.255.5 C-LST: 10.255.255.1 
 * >      RD: 10.255.255.1:1 ip-prefix 10.255.254.2/32
                                 10.255.255.1          -       100     0       i
 * >      RD: 10.255.255.7:1 ip-prefix 10.255.254.3/32
                                 10.255.255.8          -       100     0       i Or-ID: 10.255.255.8 C-LST: 10.255.255.1 
 * >      RD: 10.255.255.11:1 ip-prefix 10.255.254.4/32
                                 10.255.255.11         -       100     0       i Or-ID: 10.255.255.11 C-LST: 10.255.255.1 
 * >      RD: 10.255.255.12:1 ip-prefix 10.255.254.4/32
                                 10.255.255.12         -       100     0       i Or-ID: 10.255.255.12 C-LST: 10.255.255.1 
 * >      RD: 10.255.255.10:1 ip-prefix 10.255.254.5/32
                                 10.255.255.10         -       100     0       i Or-ID: 10.255.255.10 C-LST: 10.255.255.1 
 * >      RD: 10.255.255.4:1 ip-prefix 10.255.254.6/32
                                 -                     -       -       0       i
 * >      RD: 10.255.255.5:1 ip-prefix 192.168.0.0/24
                                 10.255.255.5          -       100     0       i Or-ID: 10.255.255.5 C-LST: 10.255.255.1 
 * >      RD: 10.255.255.1:1 ip-prefix 192.168.1.0/24
                                 10.255.255.1          -       100     0       i
 * >      RD: 10.255.255.7:1 ip-prefix 192.168.3.0/24
                                 10.255.255.8          -       100     0       i Or-ID: 10.255.255.8 C-LST: 10.255.255.1 
 * >      RD: 10.255.255.4:1 ip-prefix 192.168.5.0/24
                                 -                     -       -       0       i
 * >      RD: 10.255.255.11:1 ip-prefix 192.168.6.0/24
                                 10.255.255.11         -       100     0       i Or-ID: 10.255.255.11 C-LST: 10.255.255.1 
 * >      RD: 10.255.255.12:1 ip-prefix 192.168.6.0/24
                                 10.255.255.12         -       100     0       i Or-ID: 10.255.255.12 C-LST: 10.255.255.1 
 * >      RD: 10.255.255.10:1 ip-prefix 192.168.40.0/24
                                 10.255.255.10         -       100     0       i Or-ID: 10.255.255.10 C-LST: 10.255.255.1 
```

## show ip security connection detail

```text
path1:
  Source address: 172.16.0.7, Destination address: 172.16.0.1
  State: idle
  Uptime: N/A
  VRF: default
  Type: static
  Remote IP: 10.255.255.1
  Role: initiator
path2:
  Source address: 172.16.1.5, Destination address: 172.16.0.1
  State: idle
  Uptime: N/A
  VRF: default
  Type: static
  Remote IP: 10.255.255.1
  Role: initiator
path5:
  Source address: 172.16.0.7, Destination address: 172.16.1.2
  State: idle
  Uptime: N/A
  VRF: default
  Type: static
  Remote IP: 10.255.255.1
  Role: initiator
path6:
  Source address: 172.16.1.5, Destination address: 172.16.1.2
  State: established
  Uptime: 1 second
  VRF: default
  Type: static
  Remote IP: 10.255.255.1
  Role: initiator
  Inbound SPI: 0xc36915:
    Request ID: 341, Mode: transport, Replay window size: 16384, Seq: 0x0
    Errors:
      Packets outside replay window: 0, Replay: 0, Integrity failed: 0
    Lifetime config:
      Soft byte limit: 4753247924999, Hard byte limit: 6442450944000
      Soft packet limit: 2285343653, Hard packet limit: 4000000000
      Soft time limit: 2787 secs, Hard time limit: 3600 secs
    Lifetime current:
      Current bytes: 4047336
      Current packets: 3690
      SA add time: Thu Mar 14 09:13:44 2024
      SA last use time: Thu Mar 14 09:14:19 2024
  Outbound SPI: 0xc27227:
    Request ID: 341, Mode: transport, Replay window size: 0, Seq: 0x0
    Errors:
      Packets outside replay window: 0, Replay: 0, Integrity failed: 0
    Lifetime config:
      Soft byte limit: 3316495699499, Hard byte limit: 6442450944000
      Soft packet limit: 2086410765, Hard packet limit: 4000000000
      Soft time limit: 3023 secs, Hard time limit: 3600 secs
    Lifetime current:
      Current bytes: 13213514
      Current packets: 25314
      SA add time: Thu Mar 14 09:13:44 2024
      SA last use time: Thu Mar 14 09:14:19 2024
path7:
  Source address: 172.16.0.7, Destination address: 172.16.0.9
  State: established
  Uptime: 8 seconds
  VRF: default
  Type: static
  Remote IP: 10.255.255.1
  Role: initiator
  Inbound SPI: 0xcbce32:
    Request ID: 330, Mode: transport, Replay window size: 16384, Seq: 0x0
    Errors:
      Packets outside replay window: 0, Replay: 0, Integrity failed: 0
    Lifetime config:
      Soft byte limit: 3485245541249, Hard byte limit: 6442450944000
      Soft packet limit: 2848198104, Hard packet limit: 4000000000
      Soft time limit: 2669 secs, Hard time limit: 3600 secs
    Lifetime current:
      Current bytes: 191932
      Current packets: 75
      SA add time: Thu Mar 14 09:13:37 2024
      SA last use time: Thu Mar 14 09:14:19 2024
  Outbound SPI: 0xc0bc12:
    Request ID: 330, Mode: transport, Replay window size: 0, Seq: 0x0
    Errors:
      Packets outside replay window: 0, Replay: 0, Integrity failed: 0
    Lifetime config:
      Soft byte limit: 4050809269499, Hard byte limit: 6442450944000
      Soft packet limit: 2100504632, Hard packet limit: 4000000000
      Soft time limit: 2559 secs, Hard time limit: 3600 secs
    Lifetime current:
      Current bytes: 178979
      Current packets: 178
      SA add time: Thu Mar 14 09:13:37 2024
      SA last use time: Thu Mar 14 09:14:18 2024
path8:
  Source address: 172.16.1.5, Destination address: 172.16.0.9
  State: idle
  Uptime: N/A
  VRF: default
  Type: static
  Remote IP: 10.255.255.1
  Role: initiator
path9:
  Source address: 172.16.0.7, Destination address: 172.16.0.11
  State: established
  Uptime: 8 seconds
  VRF: default
  Type: static
  Remote IP: 10.255.255.1
  Role: initiator
  Inbound SPI: 0xc79146:
    Request ID: 337, Mode: transport, Replay window size: 16384, Seq: 0x0
    Errors:
      Packets outside replay window: 0, Replay: 0, Integrity failed: 0
    Lifetime config:
      Soft byte limit: 4083077585999, Hard byte limit: 6442450944000
      Soft packet limit: 2204367378, Hard packet limit: 4000000000
      Soft time limit: 2547 secs, Hard time limit: 3600 secs
    Lifetime current:
      Current bytes: 190584
      Current packets: 66
      SA add time: Thu Mar 14 09:13:37 2024
      SA last use time: Thu Mar 14 09:14:18 2024
  Outbound SPI: 0xc063e5:
    Request ID: 337, Mode: transport, Replay window size: 0, Seq: 0x0
    Errors:
      Packets outside replay window: 0, Replay: 0, Integrity failed: 0
    Lifetime config:
      Soft byte limit: 4659611281499, Hard byte limit: 6442450944000
      Soft packet limit: 2135385590, Hard packet limit: 4000000000
      Soft time limit: 2888 secs, Hard time limit: 3600 secs
    Lifetime current:
      Current bytes: 178162
      Current packets: 162
      SA add time: Thu Mar 14 09:13:37 2024
      SA last use time: Thu Mar 14 09:14:18 2024
path10:
  Source address: 172.16.1.5, Destination address: 172.16.0.11
  State: idle
  Uptime: N/A
  VRF: default
  Type: static
  Remote IP: 10.255.255.1
  Role: initiator
path13:
  Source address: 172.16.0.7, Destination address: 172.16.1.0
  State: idle
  Uptime: N/A
  VRF: default
  Type: static
  Remote IP: 10.255.255.1
  Role: initiator
path14:
  Source address: 172.16.1.5, Destination address: 172.16.1.0
  State: established
  Uptime: 9 seconds
  VRF: default
  Type: static
  Remote IP: 10.255.255.1
  Role: initiator
  Inbound SPI: 0xc25ee3:
    Request ID: 327, Mode: transport, Replay window size: 16384, Seq: 0x0
    Errors:
      Packets outside replay window: 0, Replay: 0, Integrity failed: 0
    Lifetime config:
      Soft byte limit: 3907702550249, Hard byte limit: 6442450944000
      Soft packet limit: 2205202335, Hard packet limit: 4000000000
      Soft time limit: 2719 secs, Hard time limit: 3600 secs
    Lifetime current:
      Current bytes: 189628
      Current packets: 59
      SA add time: Thu Mar 14 09:13:36 2024
      SA last use time: Thu Mar 14 09:14:19 2024
  Outbound SPI: 0xc8931f:
    Request ID: 327, Mode: transport, Replay window size: 0, Seq: 0x0
    Errors:
      Packets outside replay window: 0, Replay: 0, Integrity failed: 0
    Lifetime config:
      Soft byte limit: 3821226054749, Hard byte limit: 6442450944000
      Soft packet limit: 2356394326, Hard packet limit: 4000000000
      Soft time limit: 2730 secs, Hard time limit: 3600 secs
    Lifetime current:
      Current bytes: 404036
      Current packets: 184
      SA add time: Thu Mar 14 09:13:36 2024
      SA last use time: Thu Mar 14 09:14:19 2024
path15:
  Source address: 172.16.255.1, Destination address: 172.16.1.2
  State: idle
  Uptime: N/A
  VRF: default
  Type: static
  Remote IP: 10.255.255.1
  Role: initiator
path16:
  Source address: 172.16.255.1, Destination address: 172.16.1.0
  State: idle
  Uptime: N/A
  VRF: default
  Type: static
  Remote IP: 10.255.255.1
  Role: initiator
path17:
  Source address: 172.16.255.1, Destination address: 172.16.0.9
  State: idle
  Uptime: N/A
  VRF: default
  Type: static
  Remote IP: 10.255.255.1
  Role: initiator
path19:
  Source address: 172.16.255.1, Destination address: 172.16.0.1
  State: idle
  Uptime: N/A
  VRF: default
  Type: static
  Remote IP: 10.255.255.1
  Role: initiator
path21:
  Source address: 172.16.255.1, Destination address: 172.16.0.11
  State: idle
  Uptime: N/A
  VRF: default
  Type: static
  Remote IP: 10.255.255.1
  Role: initiator
path22:
  Source address: 172.16.0.7, Destination address: 172.16.255.0
  State: idle
  Uptime: N/A
  VRF: default
  Type: static
  Remote IP: 10.255.255.1
  Role: initiator
path23:
  Source address: 172.16.1.5, Destination address: 172.16.255.0
  State: idle
  Uptime: N/A
  VRF: default
  Type: static
  Remote IP: 10.255.255.1
  Role: initiator
path24:
  Source address: 172.16.255.1, Destination address: 172.16.255.0
  State: established
  Uptime: 0 seconds
  VRF: default
  Type: static
  Remote IP: 10.255.255.1
  Role: initiator
  Inbound SPI: 0xc22e7d:
    Request ID: 342, Mode: transport, Replay window size: 16384, Seq: 0x0
    Errors:
      Packets outside replay window: 0, Replay: 0, Integrity failed: 0
    Lifetime config:
      Soft byte limit: 3934950332999, Hard byte limit: 6442450944000
      Soft packet limit: 2254278596, Hard packet limit: 4000000000
      Soft time limit: 2650 secs, Hard time limit: 3600 secs
    Lifetime current:
      Current bytes: 187452
      Current packets: 39
      SA add time: Thu Mar 14 09:13:45 2024
      SA last use time: Thu Mar 14 09:14:18 2024
  Outbound SPI: 0xc5edb7:
    Request ID: 342, Mode: transport, Replay window size: 0, Seq: 0x0
    Errors:
      Packets outside replay window: 0, Replay: 0, Integrity failed: 0
    Lifetime config:
      Soft byte limit: 4621427411249, Hard byte limit: 6442450944000
      Soft packet limit: 2459480932, Hard packet limit: 4000000000
      Soft time limit: 2850 secs, Hard time limit: 3600 secs
    Lifetime current:
      Current bytes: 256
      Current packets: 8
      SA add time: Thu Mar 14 09:13:45 2024
      SA last use time: Thu Mar 14 09:14:18 2024
```

## show stun client translations detail

```text
Current System Time: Thu Mar 14 09:13:46 2024
```

## show stun server bindings detail

```text
Current System Time: Thu Mar 14 09:13:46 2024
Transaction ID 000000010affff0500000000
Public Address: 172.16.0.1:4500
Number of Attributes: 3
Timeout Interval: 0:10:00
Timeout: 0:09:45
Attribute Type   Length Value           
---------------- ------ ----------------
PATH_GROUP            6 VZ_OFF          
VTEP_IP               4 10.255.255.5    
WAN_ID                4 1               

Transaction ID 000000010affff0800000000
Public Address: 172.16.1.2:4500
Number of Attributes: 3
Timeout Interval: 0:10:00
Timeout: 0:09:46
Attribute Type   Length Value           
---------------- ------ ----------------
PATH_GROUP            7 VZ_NEAR         
VTEP_IP               4 10.255.255.8    
WAN_ID                4 1               

Transaction ID 000000020affff0100000000
Public Address: 172.16.1.0:4500
Number of Attributes: 3
Timeout Interval: 0:10:00
Timeout: 0:09:44
Attribute Type   Length Value           
---------------- ------ ----------------
PATH_GROUP            7 VZ_NEAR         
VTEP_IP               4 10.255.255.1    
WAN_ID                4 2               

Transaction ID 000000020affff0b00000000
Public Address: 172.16.0.9:4500
Number of Attributes: 3
Timeout Interval: 0:10:00
Timeout: 0:09:44
Attribute Type   Length Value           
---------------- ------ ----------------
PATH_GROUP            6 VZ_OFF          
VTEP_IP               4 10.255.255.11   
WAN_ID                4 2               

Transaction ID 000000020affff0c00000000
Public Address: 172.16.0.11:4500
Number of Attributes: 3
Timeout Interval: 0:10:00
Timeout: 0:09:45
Attribute Type   Length Value           
---------------- ------ ----------------
PATH_GROUP            6 VZ_OFF          
VTEP_IP               4 10.255.255.12   
WAN_ID                4 2               

Transaction ID 000000080affff0300000000
Public Address: 172.16.255.0:4500
Number of Attributes: 3
Timeout Interval: 0:10:00
Timeout: 0:09:51
Attribute Type   Length Value           
---------------- ------ ----------------
PATH_GROUP            4 PEER            
VTEP_IP               4 10.255.255.3    
WAN_ID                4 8               

```

## show path-selection paths detail

```text
Peer: 10.255.255.1, Path group VZ_NEAR
Path name: path14, dynamic, Label: 24590
Source: 172.16.1.5, Port: 4500, WAN ID: 2
Destination: 172.16.1.0, Port: 4500, WAN ID: 2
Local interface: Ethernet1/3
Route state: IPsec established
Traffic class 0: active (0:00:09)
MTU: 8914

Peer: 10.255.255.3, Path group PEER
Path name: path24, dynamic, Label: 24600
Source: 172.16.255.1, Port: 4500, WAN ID: 3
Destination: 172.16.255.0, Port: 4500, WAN ID: 8
Local interface: Ethernet1/2
Route state: IPsec established
Traffic class 0: active (0:00:00)
MTU: 8914

Peer: 10.255.255.8, Path group VZ_NEAR
Path name: path6, dynamic, Label: 24582
Source: 172.16.1.5, Port: 4500, WAN ID: 2
Destination: 172.16.1.2, Port: 4500, WAN ID: 1
Local interface: Ethernet1/3
Route state: IPsec established
Traffic class 0: active (0:00:02)
MTU: 8914

Peer: 10.255.255.11, Path group VZ_OFF
Path name: path7, dynamic, Label: 24583
Source: 172.16.0.7, Port: 4500, WAN ID: 1
Destination: 172.16.0.9, Port: 4500, WAN ID: 2
Local interface: Ethernet1/4
Route state: IPsec established
Traffic class 0: active (0:00:09)
MTU: 1424

Peer: 10.255.255.12, Path group VZ_OFF
Path name: path9, dynamic, Label: 24585
Source: 172.16.0.7, Port: 4500, WAN ID: 1
Destination: 172.16.0.11, Port: 4500, WAN ID: 2
Local interface: Ethernet1/4
Route state: IPsec established
Traffic class 0: active (0:00:09)
MTU: 1424

```

## show bgp neighbors

```text
BGP neighbor is 10.255.255.1, remote AS 65000, internal link
  BGP version 4, remote router ID 10.255.255.1, VRF default
  Inherits configuration from and member of peer-group autovpnEdges
  Last read 00:02:28, last write 00:00:08
  Hold time is 180, keepalive interval is 60 seconds
  Configured hold time is 180, keepalive interval is 60 seconds
  Effective minimum hold time is 3 seconds
  Send failure hold time is 0 seconds
  Hold timer is active, time left: 00:00:32
  Keepalive timer is active, time left: 00:00:51
  Connect timer is inactive
  Idle-restart timer is inactive
  BGP state is Established, up for 00:06:31
  Number of transitions to established: 9
  Last state was OpenConfirm
  Last event was RecvUpdate
  Last sent notification:Hold Timer Expired Error/None, Last time 00:08:25, First time 01:09:38, Repeats 2
  Last rcvd notification:Cease/connection collision resolution, Last time 02:20:30, First time 02:20:44, Repeats 2
  Last sent socket-error:Connect (Network is unreachable), Last time 02:26:39, First time 02:27:05, Repeats 3
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
      Received 00:06:30
      Number of stale paths removed after graceful restart: 0
      Number of paths received before End-of-RIB: 11
    L2VPN EVPN End-of-RIB received: Yes
      Received 00:06:30
      Number of stale paths removed after graceful restart: 0
      Number of paths received before End-of-RIB: 21
  AIGP attribute send and receive for IPv4 Unicast are enabled
  AIGP attribute send and receive for IPv4 with MPLS Labels are enabled
  AIGP attribute send and receive for IPv6 Unicast are enabled
  AIGP attribute send and receive for IPv6 with MPLS Labels are enabled
  BGP session driven failover for IPv6 Unicast is disabled
  BGP session driven failover for IPv4 Unicast is disabled
  Message Statistics:
                                  Sent      Rcvd
    Opens:                          13        13
    Notifications:                  13         3
    Updates:                       411       235
    Keepalives:                    120       114
    Enhanced Route Refresh:          0         0
    Begin of Route Refresh:          0         0
    End of Route Refresh:            0         0
    Total messages:                557       365
  Prefix Statistics:
                                   Sent      Rcvd     Best Paths     Best ECMP Paths
    IPv4 Unicast:                     0         0              0                   0
    IPv4 Dps:                         7        11             11                   6
    IPv6 Unicast:                     0         0              0                   0
    EVPN:                             4        21             21                  10
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
  Outbound RCF function for L2VPN EVPN is NH_LOC()
  Additional-paths send mode:
    Dps: any
Local AS is 65000, local router ID 10.255.255.4
TTL is 255
Local TCP address is 10.255.255.4, local port is 179
Remote TCP address is 10.255.255.1, remote port is 44253
Local next hop for next hop self:
  Dps: 10.255.255.4
  L2VPN EVPN: 10.255.255.4
BFD is enabled with configured transmit interval 1000ms, receive interval 1000ms, multiplier 3 and state is Down
TCP Socket Information:
  TCP state is ESTABLISHED
  Recv-Q: 0/32768
  Send-Q: 2101/46080
  Outgoing Maximum Segment Size (MSS): 1448
  Total Number of TCP retransmissions: 20
  Options:
    Timestamps enabled: yes
    Selective Acknowledgments enabled: yes
    Window Scale enabled: yes
    Explicit Congestion Notification (ECN) enabled: no
  Socket Statistics:
    Window Scale (wscale): 7,7
    Retransmission Timeout (rto): 66208.0ms
    Round-trip Time (rtt/rtvar): 1792.2ms/3196.5ms
    Delayed Ack Timeout (ato): 40.0ms
    Congestion Window (cwnd): 1
    Slow-start Threshold (ssthresh): 2
    TCP Throughput: 0.01 Mbps
    Advertised Recv Window (rcv_space): 14600

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
  Connect timer is active, time left: 00:00:00
  Connection interval is 20 seconds
  Failed connection attempts is 384
  Idle-restart timer is inactive
  BGP state is Connect
  Number of transitions to established: 0
  Last state was Active
  Last event was ConnectRetry
  Last sent socket-error:Connect (Network is unreachable), Last time 02:26:39, First time 02:27:05, Repeats 2
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
  Outbound RCF function for L2VPN EVPN is NH_LOC()
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
  Total Number of TCP retransmissions: 4
  Options:
    Timestamps enabled: no
    Selective Acknowledgments enabled: no
    Window Scale enabled: no
    Explicit Congestion Notification (ECN) enabled: no
  Socket Statistics:
    Window Scale (wscale): 0,0
    Retransmission Timeout (rto): 16000.0ms
    Round-trip Time (rtt/rtvar): 0.0ms/250.0ms
    Delayed Ack Timeout (ato): 0.0ms
    Congestion Window (cwnd): 1
    Slow-start Threshold (ssthresh): 7

BGP neighbor is 10.255.255.3, remote AS 65000, internal link
  BGP version 4, remote router ID 10.255.255.3, VRF default
  Inherits configuration from and member of peer-group PEER_TRANSIT
  Last read 00:04:50, last write 00:04:50
  Hold time is 180, keepalive interval is 60 seconds
  Configured hold time is 180, keepalive interval is 60 seconds
  Effective minimum hold time is 3 seconds
  Send failure hold time is 0 seconds
  Hold timer is inactive
  Keepalive timer is inactive
  Connect timer is active, time left: 00:00:20
  Connection interval is 20 seconds
  Failed connection attempts is 97
  Idle-restart timer is inactive
  BGP state is Connect
  Number of transitions to established: 1
  Last state was Active
  Last event was ConnectRetry
  Last sent notification:Hold Timer Expired Error/None, Last time 02:21:20
  Last rcvd notification:Cease/connection rejected, Last time 00:04:50, First time 02:20:55, Repeats 46
  Last sent socket-error:Connect (Network is unreachable), Last time 02:26:39, First time 02:27:05, Repeats 3
  Types of communities advertised: standard extended large
  Neighbor is a route reflector client
  Neighbor is using global cluster ID 10.255.255.4
  Neighbor Capabilities:
    Multiprotocol IPv4 Unicast: advertised and received
    Multiprotocol Dps: advertised and received
    Multiprotocol L2VPN EVPN: advertised and received
    Four Octet ASN: advertised and received
    Route Refresh: advertised and received
    Enhanced route refresh: advertised and received
    Send End-of-RIB messages: advertised and received
    Additional-paths recv capability:
      IPv4 Unicast: advertised
      Dps: advertised
      L2VPN EVPN: advertised
    Additional-paths send capability:
      IPv4 Unicast: received
      Dps: advertised
      L2VPN EVPN: received
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
    Opens:                 48         1
    Notifications:          1        47
    Updates:               77        17
    Keepalives:             2         2
    Route Refresh:          0         0
    Total messages:       128        67
  Prefix Statistics:
                                   Sent      Rcvd     Best Paths     Best ECMP Paths
    IPv4 Unicast:                     0         0              0                   0
    IPv6 Unicast:                     0         0              0                   0
  Configured maximum total number of routes is 256000, warning limit is 204800
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
  Inbound route map for L2VPN EVPN is SET_COMMUNITY_TRANSIT
  Outbound RCF function for L2VPN EVPN is NH_LOC2()
Local AS is 65000, local router ID 10.255.255.4
TTL is 255
Local TCP address is 10.255.255.4
Remote TCP address is 10.255.255.3, remote port is 179
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

BGP neighbor is 10.255.255.8, remote AS 65000, internal link
  BGP version 4, remote router ID 10.255.255.8, VRF default
  Inherits configuration from and member of peer-group autovpnEdges
  Last read 00:00:00, last write 00:00:01
  Hold time is 180, keepalive interval is 60 seconds
  Configured hold time is 180, keepalive interval is 60 seconds
  Effective minimum hold time is 3 seconds
  Send failure hold time is 0 seconds
  Hold timer is active, time left: 00:03:00
  Keepalive timer is active, time left: 00:00:53
  Connect timer is inactive
  Idle-restart timer is inactive
  BGP state is Established, up for 00:00:01
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
      Received 00:00:00
      Number of stale paths removed after graceful restart: 0
    L2VPN EVPN End-of-RIB received: Yes
      Received 00:00:00
      Number of stale paths removed after graceful restart: 0
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
    Updates:                         0         6
    Keepalives:                      2         2
    Enhanced Route Refresh:          0         0
    Begin of Route Refresh:          0         0
    End of Route Refresh:            0         0
    Total messages:                  3         9
  Prefix Statistics:
                                   Sent      Rcvd     Best Paths     Best ECMP Paths
    IPv4 Unicast:                     0         0              0                   0
    IPv4 Dps:                        16         0              2                   0
    IPv6 Unicast:                     0         0              0                   0
    EVPN:                            25         0              4                   0
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
  Outbound RCF function for L2VPN EVPN is NH_LOC()
  Additional-paths send mode:
    Dps: any
Local AS is 65000, local router ID 10.255.255.4
TTL is 255
Local TCP address is 10.255.255.4, local port is 179
Remote TCP address is 10.255.255.8, remote port is 32861
Local next hop for next hop self:
  Dps: 10.255.255.4
  L2VPN EVPN: 10.255.255.4
BFD is enabled with configured transmit interval 1000ms, receive interval 1000ms, multiplier 3 and state is Up
TCP Socket Information:
  TCP state is ESTABLISHED
  Recv-Q: 0/32768
  Send-Q: 0/46080
  Outgoing Maximum Segment Size (MSS): 1284
  Total Number of TCP retransmissions: 1
  Options:
    Timestamps enabled: yes
    Selective Acknowledgments enabled: yes
    Window Scale enabled: yes
    Explicit Congestion Notification (ECN) enabled: no
  Socket Statistics:
    Window Scale (wscale): 7,7
    Retransmission Timeout (rto): 216.0ms
    Round-trip Time (rtt/rtvar): 12.4ms/14.0ms
    Delayed Ack Timeout (ato): 40.0ms
    Congestion Window (cwnd): 10
    TCP Throughput: 8.31 Mbps
    Recv Round-trip Time (rcv_rtt): 3.0ms
    Advertised Recv Window (rcv_space): 14600

BGP neighbor is 10.255.255.11, remote AS 65000, internal link
  BGP version 4, remote router ID 10.255.255.11, VRF default
  Inherits configuration from and member of peer-group autovpnEdges
  Last read 00:00:01, last write 00:00:02
  Hold time is 180, keepalive interval is 60 seconds
  Configured hold time is 180, keepalive interval is 60 seconds
  Effective minimum hold time is 3 seconds
  Send failure hold time is 0 seconds
  Hold timer is active, time left: 00:02:59
  Keepalive timer is active, time left: 00:00:49
  Connect timer is inactive
  Idle-restart timer is inactive
  BGP state is Established, up for 00:00:02
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
      Received 00:00:01
      Number of stale paths removed after graceful restart: 0
      Number of paths received before End-of-RIB: 2
    L2VPN EVPN End-of-RIB received: Yes
      Received 00:00:01
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
    Updates:                         0         6
    Keepalives:                      2         2
    Enhanced Route Refresh:          0         0
    Begin of Route Refresh:          0         0
    End of Route Refresh:            0         0
    Total messages:                  3         9
  Prefix Statistics:
                                   Sent      Rcvd     Best Paths     Best ECMP Paths
    IPv4 Unicast:                     0         0              0                   0
    IPv4 Dps:                        16         2              2                   0
    IPv6 Unicast:                     0         0              0                   0
    EVPN:                            25         3              3                   0
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
  Outbound RCF function for L2VPN EVPN is NH_LOC()
  Additional-paths send mode:
    Dps: any
Local AS is 65000, local router ID 10.255.255.4
TTL is 255
Local TCP address is 10.255.255.4, local port is 179
Remote TCP address is 10.255.255.11, remote port is 42739
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
    Retransmission Timeout (rto): 208.0ms
    Round-trip Time (rtt/rtvar): 7.4ms/7.0ms
    Delayed Ack Timeout (ato): 40.0ms
    Congestion Window (cwnd): 10
    TCP Throughput: 14.79 Mbps
    Recv Round-trip Time (rcv_rtt): 4.0ms
    Advertised Recv Window (rcv_space): 14600

BGP neighbor is 10.255.255.12, remote AS 65000, internal link
  BGP version 4, remote router ID 10.255.255.12, VRF default
  Inherits configuration from and member of peer-group autovpnEdges
  Last read 00:00:00, last write 00:00:01
  Hold time is 180, keepalive interval is 60 seconds
  Configured hold time is 180, keepalive interval is 60 seconds
  Effective minimum hold time is 3 seconds
  Send failure hold time is 0 seconds
  Hold timer is active, time left: 00:03:00
  Keepalive timer is active, time left: 00:00:48
  Connect timer is inactive
  Idle-restart timer is inactive
  BGP state is Established, up for 00:00:01
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
      Received 00:00:00
      Number of stale paths removed after graceful restart: 0
    L2VPN EVPN End-of-RIB received: Yes
      Received 00:00:00
      Number of stale paths removed after graceful restart: 0
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
    Updates:                         0         6
    Keepalives:                      2         2
    Enhanced Route Refresh:          0         0
    Begin of Route Refresh:          0         0
    End of Route Refresh:            0         0
    Total messages:                  3         9
  Prefix Statistics:
                                   Sent      Rcvd     Best Paths     Best ECMP Paths
    IPv4 Unicast:                     0         0              0                   0
    IPv4 Dps:                        16         0              2                   0
    IPv6 Unicast:                     0         0              0                   0
    EVPN:                            25         0              3                   0
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
  Outbound RCF function for L2VPN EVPN is NH_LOC()
  Additional-paths send mode:
    Dps: any
Local AS is 65000, local router ID 10.255.255.4
TTL is 255
Local TCP address is 10.255.255.4, local port is 179
Remote TCP address is 10.255.255.12, remote port is 33783
Local next hop for next hop self:
  Dps: 10.255.255.4
  L2VPN EVPN: 10.255.255.4
BFD is enabled with configured transmit interval 1000ms, receive interval 1000ms, multiplier 3 and state is Down
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
    Retransmission Timeout (rto): 208.0ms
    Round-trip Time (rtt/rtvar): 4.7ms/5.3ms
    Delayed Ack Timeout (ato): 40.0ms
    Congestion Window (cwnd): 10
    TCP Throughput: 23.15 Mbps
    Advertised Recv Window (rcv_space): 14600

```

## show bgp path-selection detail

```text
BGP routing table information for VRF default
Router identifier 10.255.255.4, local AS number 65000
Bgp routing table entry for ipv4Dps VTEP 10.255.255.5/32
 Paths: 1 available
  Local (Received from a RR-client)
    :: from 10.255.255.1 (10.255.255.1)
      Origin IGP, metric -, localpref 100, weight 0, received 00:06:31 ago, valid, internal
      Tunnel encapsulation attribute: Dynamic path selection
        Endpoint: 172.16.0.1, Path group name: VZ_OFF, WAN ID: 1, UDP port: 4500
Bgp routing table entry for ipv4Dps VTEP 10.255.255.8/32
 Paths: 2 available
  Local (Received from a RR-client)
    :: from 10.255.255.1 (10.255.255.1)
      Origin IGP, metric -, localpref 100, weight 0, received 00:06:31 ago, valid, internal
      Tunnel encapsulation attribute: Dynamic path selection
        Endpoint: 172.16.1.2, Path group name: VZ_NEAR, WAN ID: 1, UDP port: 4500
  Local (Received from a RR-client)
    :: from 10.255.255.8 (10.255.255.8)
      Origin IGP, metric -, localpref 100, weight 0, received 00:00:01 ago, valid, internal
      Tunnel encapsulation attribute: Dynamic path selection
        Endpoint: 172.16.1.2, Path group name: VZ_NEAR, WAN ID: 1, UDP port: 4500
Bgp routing table entry for ipv4Dps VTEP 10.255.255.10/32
 Paths: 1 available
  Local (Received from a RR-client)
    :: from 10.255.255.1 (10.255.255.1)
      Origin IGP, metric -, localpref 100, weight 0, received 00:06:31 ago, valid, internal
      Tunnel encapsulation attribute: Dynamic path selection
        Endpoint: 172.16.1.7, Path group name: VZ_NEAR, WAN ID: 1, UDP port: 4500
Bgp routing table entry for ipv4Dps VTEP 10.255.255.11/32
 Paths: 2 available
  Local (Received from a RR-client)
    :: from 10.255.255.1 (10.255.255.1)
      Origin IGP, metric -, localpref 100, weight 0, received 00:06:31 ago, valid, internal
      Tunnel encapsulation attribute: Dynamic path selection
        Endpoint: 172.16.0.9, Path group name: VZ_OFF, WAN ID: 2, UDP port: 4500
  Local (Received from a RR-client)
    :: from 10.255.255.11 (10.255.255.11)
      Origin IGP, metric -, localpref 100, weight 0, received 00:00:02 ago, valid, internal
      Tunnel encapsulation attribute: Dynamic path selection
        Endpoint: 172.16.0.9, Path group name: VZ_OFF, WAN ID: 2, UDP port: 4500
Bgp routing table entry for ipv4Dps VTEP 10.255.255.12/32
 Paths: 2 available
  Local (Received from a RR-client)
    :: from 10.255.255.1 (10.255.255.1)
      Origin IGP, metric -, localpref 100, weight 0, received 00:06:31 ago, valid, internal
      Tunnel encapsulation attribute: Dynamic path selection
        Endpoint: 172.16.0.11, Path group name: VZ_OFF, WAN ID: 2, UDP port: 4500
  Local (Received from a RR-client)
    :: from 10.255.255.12 (10.255.255.12)
      Origin IGP, metric -, localpref 100, weight 0, received 00:00:01 ago, valid, internal
      Tunnel encapsulation attribute: Dynamic path selection
        Endpoint: 172.16.0.11, Path group name: VZ_OFF, WAN ID: 2, UDP port: 4500
Bgp routing table entry for ipv4Ipsec VTEP 10.255.255.1/32
 Paths: 1 available
  Local (Received from a RR-client)
    :: from 10.255.255.1 (10.255.255.1)
      Origin IGP, metric -, localpref 100, weight 0, received 00:06:31 ago, valid, internal
      Tunnel encapsulation attribute: IP security
        Initial contact: false, Rekey counter: 0, Nonce length: 32
        DH group: 14, DH key length: 256
        Encryption algo: aes256, Authentication algo: sha256
Bgp routing table entry for ipv4Ipsec VTEP 10.255.255.4/32
 Paths: 1 available
  Local
    - from - (0.0.0.0)
      Origin IGP, metric -, localpref -, weight 0, received 02:02:22 ago, valid, local
      Tunnel encapsulation attribute: IP security
        Initial contact: false, Rekey counter: 0, Nonce length: 32
        DH group: 14, DH key length: 256
        Encryption algo: aes256, Authentication algo: sha256
Bgp routing table entry for ipv4Ipsec VTEP 10.255.255.5/32
 Paths: 1 available
  Local (Received from a RR-client)
    :: from 10.255.255.1 (10.255.255.1)
      Origin IGP, metric -, localpref 100, weight 0, received 00:06:31 ago, valid, internal
      Tunnel encapsulation attribute: IP security
        Initial contact: false, Rekey counter: 0, Nonce length: 32
        DH group: 14, DH key length: 256
        Encryption algo: aes256, Authentication algo: sha256
Bgp routing table entry for ipv4Ipsec VTEP 10.255.255.8/32
 Paths: 2 available
  Local (Received from a RR-client)
    :: from 10.255.255.1 (10.255.255.1)
      Origin IGP, metric -, localpref 100, weight 0, received 00:06:31 ago, valid, internal
      Tunnel encapsulation attribute: IP security
        Initial contact: false, Rekey counter: 5, Nonce length: 32
        DH group: 14, DH key length: 256
        Encryption algo: aes256, Authentication algo: sha256
  Local (Received from a RR-client)
    :: from 10.255.255.8 (10.255.255.8)
      Origin IGP, metric -, localpref 100, weight 0, received 00:00:01 ago, valid, internal
      Tunnel encapsulation attribute: IP security
        Initial contact: false, Rekey counter: 5, Nonce length: 32
        DH group: 14, DH key length: 256
        Encryption algo: aes256, Authentication algo: sha256
Bgp routing table entry for ipv4Ipsec VTEP 10.255.255.10/32
 Paths: 1 available
  Local (Received from a RR-client)
    :: from 10.255.255.1 (10.255.255.1)
      Origin IGP, metric -, localpref 100, weight 0, received 00:06:31 ago, valid, internal
      Tunnel encapsulation attribute: IP security
        Initial contact: false, Rekey counter: 2, Nonce length: 32
        DH group: 14, DH key length: 256
        Encryption algo: aes256, Authentication algo: sha256
Bgp routing table entry for ipv4Ipsec VTEP 10.255.255.11/32
 Paths: 2 available
  Local (Received from a RR-client)
    :: from 10.255.255.1 (10.255.255.1)
      Origin IGP, metric -, localpref 100, weight 0, received 00:06:31 ago, valid, internal
      Tunnel encapsulation attribute: IP security
        Initial contact: false, Rekey counter: 3, Nonce length: 32
        DH group: 14, DH key length: 256
        Encryption algo: aes256, Authentication algo: sha256
  Local (Received from a RR-client)
    :: from 10.255.255.11 (10.255.255.11)
      Origin IGP, metric -, localpref 100, weight 0, received 00:00:02 ago, valid, internal
      Tunnel encapsulation attribute: IP security
        Initial contact: false, Rekey counter: 3, Nonce length: 32
        DH group: 14, DH key length: 256
        Encryption algo: aes256, Authentication algo: sha256
Bgp routing table entry for ipv4Ipsec VTEP 10.255.255.12/32
 Paths: 2 available
  Local (Received from a RR-client)
    :: from 10.255.255.1 (10.255.255.1)
      Origin IGP, metric -, localpref 100, weight 0, received 00:06:31 ago, valid, internal
      Tunnel encapsulation attribute: IP security
        Initial contact: false, Rekey counter: 5, Nonce length: 32
        DH group: 14, DH key length: 256
        Encryption algo: aes256, Authentication algo: sha256
  Local (Received from a RR-client)
    :: from 10.255.255.12 (10.255.255.12)
      Origin IGP, metric -, localpref 100, weight 0, received 00:00:01 ago, valid, internal
      Tunnel encapsulation attribute: IP security
        Initial contact: false, Rekey counter: 5, Nonce length: 32
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
>C    10.255.255.4/32 [0 pref/0 metric] updated 02:27:10 ago
         via Loopback0, directly connected
>C    172.16.0.6/31 [0 pref/0 metric] updated 00:00:20 ago
         via Ethernet1/4, directly connected
>C    172.16.1.4/31 [0 pref/0 metric] updated 00:00:20 ago
         via Ethernet1/3, directly connected
>C    172.16.255.0/31 [0 pref/0 metric] updated 00:00:20 ago
         via Ethernet1/2, directly connected
>C    172.28.128.0/20 [0 pref/0 metric] updated 02:26:41 ago
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
>S    10.80.0.0/12 [1 pref/0 metric] updated 02:26:41 ago
         via 172.28.128.1 [0 pref/0 metric] type ipv4
            via 172.28.128.1, Management1/1
>S    10.224.0.0/12 [1 pref/0 metric] updated 02:26:41 ago
         via 172.28.128.1 [0 pref/0 metric] type ipv4
            via 172.28.128.1, Management1/1
>S    10.240.0.0/12 [1 pref/0 metric] updated 02:26:41 ago
         via 172.28.128.1 [0 pref/0 metric] type ipv4
            via 172.28.128.1, Management1/1
>S    172.16.0.0/12 [1 pref/0 metric] updated 02:26:41 ago
         via 172.28.128.1 [0 pref/0 metric] type ipv4
            via 172.28.128.1, Management1/1
>S    172.16.0.0/24 [1 pref/0 metric] updated 00:00:20 ago
         via 172.16.0.6 [0 pref/0 metric] type ipv4
            via 172.16.0.6, Ethernet1/4
>S    172.16.1.0/24 [1 pref/0 metric] updated 00:00:20 ago
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
>P    0.0.0.0/8 [1 pref/0 metric] updated 02:27:10 ago
         via Null0, directly connected [NF]
>P    10.255.255.1/32 [1 pref/0 metric] updated 00:00:18 ago
         via 10.255.255.1, Dps1
>P    10.255.255.3/32 [1 pref/0 metric] updated 00:00:14 ago
         via 10.255.255.3, Dps1
>P    10.255.255.5/32 [1 pref/0 metric] updated 00:00:17 ago
         via 10.255.255.5, Dps1
>P    10.255.255.8/32 [1 pref/0 metric] updated 00:00:16 ago
         via 10.255.255.8, Dps1
>P    10.255.255.11/32 [1 pref/0 metric] updated 00:00:17 ago
         via 10.255.255.11, Dps1
>P    10.255.255.12/32 [1 pref/0 metric] updated 00:00:17 ago
         via 10.255.255.12, Dps1
>P    127.0.0.0/8 [1 pref/0 metric] updated 02:27:10 ago
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
>P    ::/96 [1 pref/0 metric] updated 02:26:12 ago
         via Null0, directly connected [NF]
>P    ::ffff:127.0.0.0/104 [1 pref/0 metric] updated 02:26:12 ago
         via :: [1 pref/1 metric] type ipv6
            via , directly connected
>P    fe80::/10 [1 pref/0 metric] updated 02:26:12 ago
```

