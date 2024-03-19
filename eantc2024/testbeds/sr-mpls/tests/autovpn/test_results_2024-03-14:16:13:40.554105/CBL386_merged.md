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

Uptime: 1 hour and 16 minutes
Total memory: 32470188 kB
Free memory: 21215868 kB

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
Ma1/1                0:01      0.0   0.0%        0      0.1   0.0%        0
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
 B I      10.5.255.0/31 [20/0]
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
           via VTEP 10.255.255.10 VNI 201 router-mac 00:0c:29:d5:32:d4
 B I      10.255.254.6/32 [20/0]
           via VTEP 10.255.255.4 VNI 201 router-mac ec:8a:48:04:ff:5b
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
                                 10.255.255.4          -       100     0       i Or-ID: 10.255.255.4 C-LST: 10.255.255.1 
 * >      RD: 10.255.255.4:1 ip-prefix 10.5.255.2/31
                                 10.255.255.4          -       100     0       i Or-ID: 10.255.255.4 C-LST: 10.255.255.1 
 * >      RD: 10.255.255.11:1 ip-prefix 10.6.255.0/31
                                 10.255.255.11         -       100     0       i Or-ID: 10.255.255.11 C-LST: 10.255.255.1 
 * >      RD: 10.255.255.12:1 ip-prefix 10.6.255.2/31
                                 10.255.255.12         -       100     0       i Or-ID: 10.255.255.12 C-LST: 10.255.255.1 
 * >      RD: 10.255.255.5:1 ip-prefix 10.255.254.1/32
                                 -                     -       -       0       i
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
                                 10.255.255.4          -       100     0       i Or-ID: 10.255.255.4 C-LST: 10.255.255.1 
 * >      RD: 10.255.255.5:1 ip-prefix 192.168.0.0/24
                                 -                     -       -       0       i
 * >      RD: 10.255.255.1:1 ip-prefix 192.168.1.0/24
                                 10.255.255.1          -       100     0       i
 * >      RD: 10.255.255.7:1 ip-prefix 192.168.3.0/24
                                 10.255.255.8          -       100     0       i Or-ID: 10.255.255.8 C-LST: 10.255.255.1 
 * >      RD: 10.255.255.4:1 ip-prefix 192.168.5.0/24
                                 10.255.255.4          -       100     0       i Or-ID: 10.255.255.4 C-LST: 10.255.255.1 
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
  Source address: 172.16.0.1, Destination address: 172.16.0.4
  State: established
  Uptime: 21 minutes, 4 seconds
  VRF: default
  Type: static
  Remote IP: 10.255.255.1
  Role: initiator
  Inbound SPI: 0xcad56a:
    Request ID: 7, Mode: transport, Replay window size: 16384, Seq: 0x0
    Errors:
      Packets outside replay window: 0, Replay: 0, Integrity failed: 0
    Lifetime config:
      Soft byte limit: 3648677989499, Hard byte limit: 6442450944000
      Soft packet limit: 2343716224, Hard packet limit: 4000000000
      Soft time limit: 2878 secs, Hard time limit: 3600 secs
    Lifetime current:
      Current bytes: 1268664
      Current packets: 2882
      SA add time: Thu Mar 14 08:52:41 2024
      SA last use time: Thu Mar 14 09:14:14 2024
  Outbound SPI: 0xca65b6:
    Request ID: 7, Mode: transport, Replay window size: 0, Seq: 0x0
    Errors:
      Packets outside replay window: 0, Replay: 0, Integrity failed: 0
    Lifetime config:
      Soft byte limit: 4105998860999, Hard byte limit: 6442450944000
      Soft packet limit: 2799155838, Hard packet limit: 4000000000
      Soft time limit: 2635 secs, Hard time limit: 3600 secs
    Lifetime current:
      Current bytes: 2162723
      Current packets: 3002
      SA add time: Thu Mar 14 08:52:41 2024
      SA last use time: -
path4:
  Source address: 172.16.0.1, Destination address: 172.16.0.7
  State: established
  Uptime: 1 hour, 11 minutes, 5 seconds
  VRF: default
  Type: static
  Remote IP: 10.255.255.1
  Role: initiator
  Inbound SPI: 0xc39b0a:
    Request ID: 8, Mode: transport, Replay window size: 16384, Seq: 0x0
    Errors:
      Packets outside replay window: 0, Replay: 0, Integrity failed: 0
    Lifetime config:
      Soft byte limit: 4099638848999, Hard byte limit: 6442450944000
      Soft packet limit: 2371318106, Hard packet limit: 4000000000
      Soft time limit: 3005 secs, Hard time limit: 3600 secs
    Lifetime current:
      Current bytes: 292612
      Current packets: 921
      SA add time: Thu Mar 14 08:50:08 2024
      SA last use time: Thu Mar 14 08:55:16 2024
  Outbound SPI: 0xc7e3b6:
    Request ID: 8, Mode: transport, Replay window size: 0, Seq: 0x0
    Errors:
      Packets outside replay window: 0, Replay: 0, Integrity failed: 0
    Lifetime config:
      Soft byte limit: 3476653360499, Hard byte limit: 6442450944000
      Soft packet limit: 2139323900, Hard packet limit: 4000000000
      Soft time limit: 3038 secs, Hard time limit: 3600 secs
    Lifetime current:
      Current bytes: 486726
      Current packets: 1779
      SA add time: Thu Mar 14 08:50:08 2024
      SA last use time: -
path5:
  Source address: 172.16.0.1, Destination address: 172.16.0.9
  State: established
  Uptime: 1 hour, 11 minutes, 8 seconds
  VRF: default
  Type: dynamic
  Remote IP: 10.255.255.11
  Role: initiator
  Packets in: 4958517, Packets out: 3966477
  Last known rekey count: 0
  Dynamic state: established
  Last established time: Thu Mar 14 08:45:30 2024
  DH crypto:
    Local rekey: 0, Peer rekey: 3, In SPI: 0x5687a559, Out SPI: 0x684a725a
  DH state:
    Local rekey: 0, Peer rekey: 3, DH rekey state: not rekeying, Role: not rekeying
  SA crypto:
    Local rekey: 0, Peer rekey: 3, In SPI 0x39d3a1af, Out SPI 0x492bbf27
  SA rekey role: not rekeying
  SA state:
    SA type: ingress , SPI: 0x532bdf7f
      Role: initiator, SA rekey state: initial, Peer nonce type: init
      Add time: Thu Mar 14 08:43:27 2024, Packets: 3854, Pair SPI: 0x43d3c107
    SA type: egress , SPI: 0x43d3c107
      Role: initiator, SA rekey state: initial, Peer nonce type: init
      Add time: Thu Mar 14 08:43:35 2024, Packets: 3996, Pair SPI: 0x532bdf7f
  Inbound SPI: 0x532bdf7f:
    Request ID: 5, Mode: transport, Replay window size: 0, Seq: 0x0
    Errors:
      Packets outside replay window: 0, Replay: 0, Integrity failed: 0
    Lifetime config:
      Soft byte limit: 4739842240950, Hard byte limit: 6442450944000
      Soft packet limit: 2938729482, Hard packet limit: 4000000000
      Soft time limit: 2584 secs, Hard time limit: 3600 secs
    Lifetime current:
      Current bytes: 1516464
      Current packets: 3860
      SA add time: Thu Mar 14 08:43:27 2024
      SA last use time: Thu Mar 14 09:14:14 2024
  Outbound SPI: 0x43d3c107:
    Request ID: 5, Mode: transport, Replay window size: 0, Seq: 0x0
    Errors:
      Packets outside replay window: 0, Replay: 0, Integrity failed: 0
    Lifetime config:
      Soft byte limit: 4747253677050, Hard byte limit: 6442450944000
      Soft packet limit: 2931683209, Hard packet limit: 4000000000
      Soft time limit: 2629 secs, Hard time limit: 3600 secs
    Lifetime current:
      Current bytes: 1258884
      Current packets: 4002
      SA add time: Thu Mar 14 08:43:35 2024
      SA last use time: -
path6:
  Source address: 172.16.0.1, Destination address: 172.16.0.11
  State: established
  Uptime: 1 hour, 11 minutes, 8 seconds
  VRF: default
  Type: dynamic
  Remote IP: 10.255.255.12
  Role: initiator
  Packets in: 4958311, Packets out: 5946716
  Last known rekey count: 0
  Dynamic state: established
  Last established time: Thu Mar 14 08:43:30 2024
  DH crypto:
    Local rekey: 0, Peer rekey: 5, In SPI: 0xe49a1988, Out SPI: 0x5fdd5b1c
  DH state:
    Local rekey: 0, Peer rekey: 5, DH rekey state: not rekeying, Role: not rekeying
  SA crypto:
    Local rekey: 0, Peer rekey: 5, In SPI 0xfc308642, Out SPI 0x98b9b92c
  SA rekey role: not rekeying
  SA state:
    SA type: egress , SPI: 0x831a69a
      Role: initiator, SA rekey state: initial, Peer nonce type: init
      Add time: Thu Mar 14 08:41:55 2024, Packets: 4258, Pair SPI: 0xa4b9d984
    SA type: ingress , SPI: 0xa4b9d984
      Role: initiator, SA rekey state: initial, Peer nonce type: init
      Add time: Thu Mar 14 08:41:47 2024, Packets: 4056, Pair SPI: 0x831a69a
  Inbound SPI: 0xa4b9d984:
    Request ID: 6, Mode: transport, Replay window size: 0, Seq: 0x0
    Errors:
      Packets outside replay window: 0, Replay: 0, Integrity failed: 0
    Lifetime config:
      Soft byte limit: 4717641256725, Hard byte limit: 6442450944000
      Soft packet limit: 2997762115, Hard packet limit: 4000000000
      Soft time limit: 2527 secs, Hard time limit: 3600 secs
    Lifetime current:
      Current bytes: 1538296
      Current packets: 4062
      SA add time: Thu Mar 14 08:41:47 2024
      SA last use time: Thu Mar 14 09:14:13 2024
  Outbound SPI: 0x831a69a:
    Request ID: 6, Mode: transport, Replay window size: 0, Seq: 0x0
    Errors:
      Packets outside replay window: 0, Replay: 0, Integrity failed: 0
    Lifetime config:
      Soft byte limit: 4719934974750, Hard byte limit: 6442450944000
      Soft packet limit: 2978340832, Hard packet limit: 4000000000
      Soft time limit: 2628 secs, Hard time limit: 3600 secs
    Lifetime current:
      Current bytes: 1446788
      Current packets: 4264
      SA add time: Thu Mar 14 08:41:55 2024
      SA last use time: -
```

## show stun client translations detail

```text
Current System Time: Thu Mar 14 09:13:46 2024
Transaction ID 000000010affff0500000000
Agent Name: dps
Source Address: 172.16.0.1:4500
Public Address: 172.16.0.1:4500
Number of Attributes: 3
Timeout Interval: 0:03:00
Last Refreshed: 0:00:14 ago
Attribute Type   Length Value           
---------------- ------ ----------------
PATH_GROUP            6 VZ_OFF          
VTEP_IP               4 10.255.255.5    
WAN_ID                4 1               

```

## show stun server bindings detail

```text
Current System Time: Thu Mar 14 09:13:47 2024
```

## show path-selection paths detail

```text
Peer: 10.255.255.1, Path group VZ_OFF
Path name: path1, static, Label: 4097
Source: 172.16.0.1, Port: 4500, WAN ID: 1
Destination: 172.16.0.4, Port: 4500, WAN ID: 2886729732
Local interface: Ethernet1/7
Route state: IPsec established
Traffic class 0: active (0:21:03)
MTU: 8914

Peer: 10.255.255.4, Path group VZ_OFF
Path name: path4, static, Label: 4100
Source: 172.16.0.1, Port: 4500, WAN ID: 1
Destination: 172.16.0.7, Port: 4500, WAN ID: 2886729735
Local interface: Ethernet1/7
Route state: IPsec established
Traffic class 0: inactive
MTU: 8914

Peer: 10.255.255.11, Path group VZ_OFF
Path name: path5, dynamic, Label: 4101
Source: 172.16.0.1, Port: 4500, WAN ID: 1
Destination: 172.16.0.9, Port: 4500, WAN ID: 2
Local interface: Ethernet1/7
Route state: IPsec established
Traffic class 0: active (1:11:04)
MTU: 1424

Peer: 10.255.255.12, Path group VZ_OFF
Path name: path6, dynamic, Label: 4102
Source: 172.16.0.1, Port: 4500, WAN ID: 1
Destination: 172.16.0.11, Port: 4500, WAN ID: 2
Local interface: Ethernet1/7
Route state: IPsec established
Traffic class 0: active (1:11:04)
MTU: 1424

```

## show bgp neighbors

```text
BGP neighbor is 10.255.255.1, remote AS 65000, internal link
  BGP version 4, remote router ID 10.255.255.1, VRF default
  Inherits configuration from and member of peer-group PATHFINDER
  Last read 00:00:21, last write 00:00:33
  Hold time is 180, keepalive interval is 60 seconds
  Configured hold time is 180, keepalive interval is 60 seconds
  Effective minimum hold time is 3 seconds
  Send failure hold time is 0 seconds
  Hold timer is active, time left: 00:02:39
  Keepalive timer is active, time left: 00:00:22
  Connect timer is inactive
  Idle-restart timer is inactive
  BGP state is Established, up for 00:21:03
  Number of transitions to established: 3
  Last state was OpenConfirm
  Last event was RecvUpdate
  Last sent notification:Hold Timer Expired Error/None, Last time 00:40:55, First time 01:10:55, Repeats 1
  Last sent socket-error:Connect (Network is unreachable), Last time 01:14:15, First time 01:14:36, Repeats 1
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
      Received 00:21:02
      Number of stale paths removed after graceful restart: 0
      Number of paths received before End-of-RIB: 18
    L2VPN EVPN End-of-RIB received: Yes
      Received 00:21:02
      Number of stale paths removed after graceful restart: 0
      Number of paths received before End-of-RIB: 22
  AIGP attribute send and receive for IPv4 Unicast are enabled
  AIGP attribute send and receive for IPv4 with MPLS Labels are enabled
  AIGP attribute send and receive for IPv6 Unicast are enabled
  AIGP attribute send and receive for IPv6 with MPLS Labels are enabled
  BGP session driven failover for IPv6 Unicast is disabled
  BGP session driven failover for IPv4 Unicast is disabled
  Message Statistics:
                                  Sent      Rcvd
    Opens:                           3         3
    Notifications:                   2         0
    Updates:                        24       244
    Keepalives:                     67        47
    Enhanced Route Refresh:          0         0
    Begin of Route Refresh:          0         0
    End of Route Refresh:            0         0
    Total messages:                 96       294
  Prefix Statistics:
                                   Sent      Rcvd     Best Paths     Best ECMP Paths
    IPv4 Unicast:                     0         0              0                   0
    IPv4 Dps:                         2        10             10                   0
    IPv6 Unicast:                     0         0              0                   0
    EVPN:                             3        22             22                   0
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
    Last update with error received at: 00:21:02
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
Local TCP address is 10.255.255.5, local port is 33065
Remote TCP address is 10.255.255.1, remote port is 179
Local next hop for next hop self:
  Dps: 10.255.255.5
  L2VPN EVPN: 10.255.255.5
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
    Round-trip Time (rtt/rtvar): 4.1ms/1.1ms
    Delayed Ack Timeout (ato): 40.0ms
    Congestion Window (cwnd): 10
    TCP Throughput: 28.34 Mbps
    Recv Round-trip Time (rcv_rtt): 799.9ms
    Advertised Recv Window (rcv_space): 14480

BGP neighbor is 10.255.255.4, remote AS 65000, internal link
  BGP version 4, remote router ID 10.255.255.4, VRF default
  Inherits configuration from and member of peer-group PATHFINDER
  Last read 00:19:05, last write 00:16:05
  Hold time is 180, keepalive interval is 60 seconds
  Configured hold time is 180, keepalive interval is 60 seconds
  Effective minimum hold time is 3 seconds
  Send failure hold time is 0 seconds
  Hold timer is inactive
  Keepalive timer is inactive
  Connect timer is active, time left: 00:00:18
  Connection interval is 20 seconds
  Failed connection attempts is 43
  Idle-restart timer is inactive
  BGP state is Connect
  Number of transitions to established: 1
  Last state was Active
  Last event was ConnectRetry
  Last sent notification:Hold Timer Expired Error/None, Last time 00:16:05
  Last sent socket-error:Connect (Network is unreachable), Last time 01:14:15, First time 01:14:36, Repeats 1
  Types of communities advertised: standard extended large
  Neighbor Capabilities:
    Multiprotocol Dps: advertised and received
    Multiprotocol L2VPN EVPN: advertised and received
    Four Octet ASN: advertised and received
    Route Refresh: advertised and received
    Enhanced route refresh: advertised and received
    Send End-of-RIB messages: advertised and received
    Additional-paths recv capability:
      Dps: advertised
      L2VPN EVPN: advertised
    Additional-paths send capability:
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
    Opens:                  1         1
    Notifications:          1         0
    Updates:               12       105
    Keepalives:            71        52
    Route Refresh:          0         0
    Total messages:        85       158
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
    Originator ID matches local router ID: 6
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
  Inbound route map for L2VPN EVPN is DENY-SOO
Local AS is 65000, local router ID 10.255.255.5
TTL is 255
Local TCP address is 10.255.255.5
Remote TCP address is 10.255.255.4, remote port is 179
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

```

## show bgp path-selection detail

```text
BGP routing table information for VRF default
Router identifier 10.255.255.5, local AS number 65000
Bgp routing table entry for ipv4Dps VTEP 10.255.255.5/32
 Paths: 1 available
  Local
    - from - (0.0.0.0)
      Origin IGP, metric -, localpref -, weight 0, received 01:11:06 ago, valid, local
      Tunnel encapsulation attribute: Dynamic path selection
        Endpoint: 172.16.0.1, Path group name: VZ_OFF, WAN ID: 1, UDP port: 4500
Bgp routing table entry for ipv4Dps VTEP 10.255.255.8/32
 Paths: 1 available
  Local
    :: from 10.255.255.1 (10.255.255.1)
      Origin IGP, metric -, localpref 100, weight 0, received 00:15:57 ago, valid, internal
      Tunnel encapsulation attribute: Dynamic path selection
        Endpoint: 172.16.1.2, Path group name: VZ_NEAR, WAN ID: 1, UDP port: 4500
Bgp routing table entry for ipv4Dps VTEP 10.255.255.10/32
 Paths: 1 available
  Local
    :: from 10.255.255.1 (10.255.255.1)
      Origin IGP, metric -, localpref 100, weight 0, received 00:21:03 ago, valid, internal
      Tunnel encapsulation attribute: Dynamic path selection
        Endpoint: 172.16.1.7, Path group name: VZ_NEAR, WAN ID: 1, UDP port: 4500
Bgp routing table entry for ipv4Dps VTEP 10.255.255.11/32
 Paths: 1 available
  Local
    :: from 10.255.255.1 (10.255.255.1)
      Origin IGP, metric -, localpref 100, weight 0, received 00:21:03 ago, valid, internal
      Tunnel encapsulation attribute: Dynamic path selection
        Endpoint: 172.16.0.9, Path group name: VZ_OFF, WAN ID: 2, UDP port: 4500
Bgp routing table entry for ipv4Dps VTEP 10.255.255.12/32
 Paths: 1 available
  Local
    :: from 10.255.255.1 (10.255.255.1)
      Origin IGP, metric -, localpref 100, weight 0, received 00:21:03 ago, valid, internal
      Tunnel encapsulation attribute: Dynamic path selection
        Endpoint: 172.16.0.11, Path group name: VZ_OFF, WAN ID: 2, UDP port: 4500
Bgp routing table entry for ipv4Ipsec VTEP 10.255.255.1/32
 Paths: 1 available
  Local
    :: from 10.255.255.1 (10.255.255.1)
      Origin IGP, metric -, localpref 100, weight 0, received 00:21:03 ago, valid, internal
      Tunnel encapsulation attribute: IP security
        Initial contact: false, Rekey counter: 0, Nonce length: 32
        DH group: 14, DH key length: 256
        Encryption algo: aes256, Authentication algo: sha256
Bgp routing table entry for ipv4Ipsec VTEP 10.255.255.4/32
 Paths: 1 available
  Local
    :: from 10.255.255.1 (10.255.255.1)
      Origin IGP, metric -, localpref 100, weight 0, received 00:06:31 ago, valid, internal
      Tunnel encapsulation attribute: IP security
        Initial contact: false, Rekey counter: 0, Nonce length: 32
        DH group: 14, DH key length: 256
        Encryption algo: aes256, Authentication algo: sha256
Bgp routing table entry for ipv4Ipsec VTEP 10.255.255.5/32
 Paths: 1 available
  Local
    - from - (0.0.0.0)
      Origin IGP, metric -, localpref -, weight 0, received 01:14:16 ago, valid, local
      Tunnel encapsulation attribute: IP security
        Initial contact: false, Rekey counter: 0, Nonce length: 32
        DH group: 14, DH key length: 256
        Encryption algo: aes256, Authentication algo: sha256
Bgp routing table entry for ipv4Ipsec VTEP 10.255.255.8/32
 Paths: 1 available
  Local
    :: from 10.255.255.1 (10.255.255.1)
      Origin IGP, metric -, localpref 100, weight 0, received 00:15:57 ago, valid, internal
      Tunnel encapsulation attribute: IP security
        Initial contact: false, Rekey counter: 5, Nonce length: 32
        DH group: 14, DH key length: 256
        Encryption algo: aes256, Authentication algo: sha256
Bgp routing table entry for ipv4Ipsec VTEP 10.255.255.10/32
 Paths: 1 available
  Local
    :: from 10.255.255.1 (10.255.255.1)
      Origin IGP, metric -, localpref 100, weight 0, received 00:21:03 ago, valid, internal
      Tunnel encapsulation attribute: IP security
        Initial contact: false, Rekey counter: 2, Nonce length: 32
        DH group: 14, DH key length: 256
        Encryption algo: aes256, Authentication algo: sha256
Bgp routing table entry for ipv4Ipsec VTEP 10.255.255.11/32
 Paths: 1 available
  Local
    :: from 10.255.255.1 (10.255.255.1)
      Origin IGP, metric -, localpref 100, weight 0, received 00:21:03 ago, valid, internal
      Tunnel encapsulation attribute: IP security
        Initial contact: false, Rekey counter: 3, Nonce length: 32
        DH group: 14, DH key length: 256
        Encryption algo: aes256, Authentication algo: sha256
Bgp routing table entry for ipv4Ipsec VTEP 10.255.255.12/32
 Paths: 1 available
  Local
    :: from 10.255.255.1 (10.255.255.1)
      Origin IGP, metric -, localpref 100, weight 0, received 00:21:03 ago, valid, internal
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
>C    10.255.255.5/32 [0 pref/0 metric] updated 01:14:58 ago
         via Loopback0, directly connected
>C    172.16.0.0/31 [0 pref/0 metric] updated 01:11:14 ago
         via Ethernet1/7, directly connected
>C    172.28.128.0/20 [0 pref/0 metric] updated 01:14:37 ago
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
>S    0.0.0.0/0 [1 pref/0 metric] updated 01:11:09 ago
         via 172.16.0.0 [0 pref/0 metric] type ipv4
            via 172.16.0.0, Ethernet1/7
>S    10.80.0.0/12 [1 pref/0 metric] updated 01:14:37 ago
         via 172.28.128.1 [0 pref/0 metric] type ipv4
            via 172.28.128.1, Management1/1
>S    10.239.0.0/16 [1 pref/0 metric] updated 01:14:37 ago
         via 172.28.128.1 [0 pref/0 metric] type ipv4
            via 172.28.128.1, Management1/1
>S    172.16.0.0/12 [1 pref/0 metric] updated 01:14:37 ago
         via 172.28.128.1 [0 pref/0 metric] type ipv4
            via 172.28.128.1, Management1/1
>S    172.16.0.0/24 [1 pref/0 metric] updated 01:11:09 ago
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
>P    0.0.0.0/8 [1 pref/0 metric] updated 01:14:54 ago
         via Null0, directly connected [NF]
>P    10.255.255.1/32 [1 pref/0 metric] updated 01:11:12 ago
         via 10.255.255.1, Dps1
>P    10.255.255.4/32 [1 pref/0 metric] updated 01:11:12 ago
         via 10.255.255.4, Dps1
>P    10.255.255.11/32 [1 pref/0 metric] updated 01:11:12 ago
         via 10.255.255.11, Dps1
>P    10.255.255.12/32 [1 pref/0 metric] updated 01:11:12 ago
         via 10.255.255.12, Dps1
>P    127.0.0.0/8 [1 pref/0 metric] updated 01:14:54 ago
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
>P    ::/96 [1 pref/0 metric] updated 01:14:20 ago
         via Null0, directly connected [NF]
>P    ::ffff:127.0.0.0/104 [1 pref/0 metric] updated 01:14:20 ago
         via :: [1 pref/1 metric] type ipv6
            via , directly connected
>P    fe80::/10 [1 pref/0 metric] updated 01:14:20 ago
```

