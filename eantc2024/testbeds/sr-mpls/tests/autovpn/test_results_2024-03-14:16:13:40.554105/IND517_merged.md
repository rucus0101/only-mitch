# Test results for IND517

## show version

```text
Arista AWE-5510-F
Hardware version: 11.01
Serial number: WTW23250084
Hardware MAC address: ec8a.4804.ff6e
System MAC address: ec8a.4804.ff6e

Software image version: 4.31.2F
Architecture: x86_64
Internal build version: 4.31.2F-35442176.4312F
Internal build ID: 500c58e3-5beb-4481-afe9-8ad77245cc44
Image format version: 3.0
Image optimization: Default

Uptime: 2 hours and 29 minutes
Total memory: 65396488 kB
Free memory: 39908416 kB

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
Ethernet1/1      10.5.255.0/31        up         up              1500          
Ethernet1/2      172.16.255.0/31      up         up              9000          
Ethernet1/3      172.16.3.3/31        up         up              1500          
Ethernet1/4      172.16.2.5/31        up         up              9000          
Loopback0        10.255.255.3/32      up         up             65535          
Management1/1    172.28.138.223/20    up         up              1500          

```

## show interfaces counters rates | nz

```text
Port      Name      Intvl  In Mbps      %  In Kpps Out Mbps      % Out Kpps
Et1/1                5:00     42.8   0.4%        5     32.6   0.3%        4
Et1/4     ATT        5:00     17.0   0.2%        1     20.0   0.2%        2
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
 C        10.255.255.3/32
           directly connected, Loopback0
 S        10.255.255.4/32
           directly connected, Dps1
 S        10.255.255.7/32
           directly connected, Dps1
 S        10.255.255.9/32
           directly connected, Dps1
 S        10.240.0.0/12 [1/0]
           via 172.28.128.1, Management1/1
 C        172.16.2.4/31
           directly connected, Ethernet1/4
 S        172.16.2.0/24 [1/0]
           via 172.16.2.4, Ethernet1/4
 C        172.16.3.2/31
           directly connected, Ethernet1/3
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
 S        10.255.255.2/32
           directly connected, Dps1
 C        10.255.255.3/32
           directly connected, Loopback0
 S        10.255.255.4/32
           directly connected, Dps1
 S        10.255.255.7/32
           directly connected, Dps1
 S        10.255.255.9/32
           directly connected, Dps1
 S        10.240.0.0/12 [1/0]
           via 172.28.128.1, Management1/1
 C        172.16.2.4/31
           directly connected, Ethernet1/4
 S        172.16.2.0/24 [1/0]
           via 172.16.2.4, Ethernet1/4
 C        172.16.3.2/31
           directly connected, Ethernet1/3
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

 O E2     10.0.255.0/31 [110/1]
           via 10.5.255.1, Ethernet1/1
 B I      10.1.255.0/31 [20/0]
           via VTEP 10.255.255.2 VNI 201 router-mac ec:8a:48:04:f5:69
 B I      10.1.255.2/31 [20/0]
           via VTEP 10.255.255.2 VNI 201 router-mac ec:8a:48:04:f5:69
 O E2     10.2.255.0/31 [110/1]
           via 10.5.255.1, Ethernet1/1
 O E2     10.2.255.2/31 [110/1]
           via 10.5.255.1, Ethernet1/1
 B I      10.4.255.0/31 [20/0]
           via VTEP 10.255.255.9 VNI 201 router-mac 00:50:56:47:de:91
 B I      10.4.255.2/31 [20/0]
           via VTEP 10.255.255.9 VNI 201 router-mac 00:50:56:47:de:91
 C        10.5.255.0/31
           directly connected, Ethernet1/1
 O        10.5.255.2/31 [110/20]
           via 10.5.255.1, Ethernet1/1
 O E2     10.6.255.0/31 [110/1]
           via 10.5.255.1, Ethernet1/1
 O E2     10.6.255.2/31 [110/1]
           via 10.5.255.1, Ethernet1/1
 O E2     10.255.254.1/32 [110/1]
           via 10.5.255.1, Ethernet1/1
 B I      10.255.254.2/32 [20/0]
           via VTEP 10.255.255.2 VNI 201 router-mac ec:8a:48:04:f5:69
 O E2     10.255.254.3/32 [110/1]
           via 10.5.255.1, Ethernet1/1
 O E2     10.255.254.4/32 [110/1]
           via 10.5.255.1, Ethernet1/1
 B I      10.255.254.5/32 [20/0]
           via VTEP 10.255.255.9 VNI 201 router-mac 00:50:56:47:de:91
 O        10.255.254.6/32 [110/20]
           via 10.5.255.1, Ethernet1/1
 O E2     192.168.0.0/24 [110/1]
           via 10.5.255.1, Ethernet1/1
 B I      192.168.1.0/24 [20/0]
           via VTEP 10.255.255.2 VNI 201 router-mac ec:8a:48:04:f5:69
 O E2     192.168.3.0/24 [110/1]
           via 10.5.255.1, Ethernet1/1
 O        192.168.5.0/24 [110/20]
           via 10.5.255.1, Ethernet1/1
 O E2     192.168.6.0/24 [110/1]
           via 10.5.255.1, Ethernet1/1
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
Router identifier 10.255.255.3, local AS number 65000
Route status codes: * - valid, > - active, S - Stale, E - ECMP head, e - ECMP
                    c - Contributing to ECMP, % - Pending best path selection
Origin codes: i - IGP, e - EGP, ? - incomplete
AS Path Attributes: Or-ID - Originator ID, C-LST - Cluster List, LL Nexthop - Link Local Nexthop

          Network                Next Hop              Metric  LocPref Weight  Path
 * >      RD: 10.255.255.2:1 ip-prefix 10.1.255.0/31
                                 10.255.255.2          -       100     0       i
 * >      RD: 10.255.255.2:1 ip-prefix 10.1.255.2/31
                                 10.255.255.2          -       100     0       i
 * >Ec    RD: 10.255.255.9:1 ip-prefix 10.4.255.0/31
                                 10.255.255.9          -       100     0       i
 *  ec    RD: 10.255.255.9:1 ip-prefix 10.4.255.0/31
                                 10.255.255.9          -       100     0       i Or-ID: 10.255.255.9 C-LST: 10.255.255.2 
 * >Ec    RD: 10.255.255.9:1 ip-prefix 10.4.255.2/31
                                 10.255.255.9          -       100     0       i
 *  ec    RD: 10.255.255.9:1 ip-prefix 10.4.255.2/31
                                 10.255.255.9          -       100     0       i Or-ID: 10.255.255.9 C-LST: 10.255.255.2 
 * >      RD: 10.255.255.3:1 ip-prefix 10.5.255.0/31
                                 -                     -       -       0       i
 * >      RD: 10.255.255.3:1 ip-prefix 10.5.255.2/31
                                 -                     -       -       0       i
 * >      RD: 10.255.255.2:1 ip-prefix 10.255.254.2/32
                                 10.255.255.2          -       100     0       i
 * >Ec    RD: 10.255.255.9:1 ip-prefix 10.255.254.5/32
                                 10.255.255.9          -       100     0       i
 *  ec    RD: 10.255.255.9:1 ip-prefix 10.255.254.5/32
                                 10.255.255.9          -       100     0       i Or-ID: 10.255.255.9 C-LST: 10.255.255.2 
 * >      RD: 10.255.255.3:1 ip-prefix 10.255.254.6/32
                                 -                     -       -       0       i
 * >      RD: 10.255.255.2:1 ip-prefix 192.168.1.0/24
                                 10.255.255.2          -       100     0       i
 * >      RD: 10.255.255.3:1 ip-prefix 192.168.5.0/24
                                 -                     -       -       0       i
 * >Ec    RD: 10.255.255.9:1 ip-prefix 192.168.40.0/24
                                 10.255.255.9          -       100     0       i
 *  ec    RD: 10.255.255.9:1 ip-prefix 192.168.40.0/24
                                 10.255.255.9          -       100     0       i Or-ID: 10.255.255.9 C-LST: 10.255.255.2 
```

## show ip security connection detail

```text
path5:
  Source address: 172.16.2.5, Destination address: 172.16.2.7
  State: established
  Uptime: 16 minutes, 9 seconds
  VRF: default
  Type: static
  Remote IP: 10.255.255.2
  Role: responder
  Inbound SPI: 0xc16c20:
    Request ID: 40, Mode: transport, Replay window size: 16384, Seq: 0x0
    Errors:
      Packets outside replay window: 0, Replay: 0, Integrity failed: 0
    Lifetime config:
      Soft byte limit: 3787783812749, Hard byte limit: 6442450944000
      Soft packet limit: 2406716999, Hard packet limit: 4000000000
      Soft time limit: 2553 secs, Hard time limit: 3600 secs
    Lifetime current:
      Current bytes: 1160020
      Current packets: 3469
      SA add time: Thu Mar 14 08:57:36 2024
      SA last use time: Thu Mar 14 09:14:16 2024
  Outbound SPI: 0xc01f5d:
    Request ID: 40, Mode: transport, Replay window size: 0, Seq: 0x0
    Errors:
      Packets outside replay window: 0, Replay: 0, Integrity failed: 0
    Lifetime config:
      Soft byte limit: 4620460719749, Hard byte limit: 6442450944000
      Soft packet limit: 2928568215, Hard packet limit: 4000000000
      Soft time limit: 2537 secs, Hard time limit: 3600 secs
    Lifetime current:
      Current bytes: 1005030
      Current packets: 7188
      SA add time: Thu Mar 14 08:57:36 2024
      SA last use time: Thu Mar 14 09:14:16 2024
path6:
  Source address: 172.16.2.5, Destination address: 172.16.2.2
  State: established
  Uptime: 6 minutes, 50 seconds
  VRF: default
  Type: static
  Remote IP: 10.255.255.2
  Role: responder
  Inbound SPI: 0xc8d929:
    Request ID: 46, Mode: transport, Replay window size: 16384, Seq: 0x0
    Errors:
      Packets outside replay window: 0, Replay: 0, Integrity failed: 0
    Lifetime config:
      Soft byte limit: 4514364875999, Hard byte limit: 6442450944000
      Soft packet limit: 2549881492, Hard packet limit: 4000000000
      Soft time limit: 2888 secs, Hard time limit: 3600 secs
    Lifetime current:
      Current bytes: 827473832
      Current packets: 781466
      SA add time: Thu Mar 14 09:06:54 2024
      SA last use time: Thu Mar 14 09:13:41 2024
  Outbound SPI: 0xc83dc6:
    Request ID: 46, Mode: transport, Replay window size: 0, Seq: 0x0
    Errors:
      Packets outside replay window: 0, Replay: 0, Integrity failed: 0
    Lifetime config:
      Soft byte limit: 4697430494999, Hard byte limit: 6442450944000
      Soft packet limit: 2671740450, Hard packet limit: 4000000000
      Soft time limit: 2765 secs, Hard time limit: 3600 secs
    Lifetime current:
      Current bytes: 965689320
      Current packets: 1898262
      SA add time: Thu Mar 14 09:06:54 2024
      SA last use time: Thu Mar 14 09:14:16 2024
path7:
  Source address: 172.16.3.3, Destination address: 172.16.2.7
  State: idle
  Uptime: N/A
  VRF: default
  Type: static
  Remote IP: 10.255.255.2
  Role: responder
path8:
  Source address: 172.16.3.3, Destination address: 172.16.2.2
  State: idle
  Uptime: N/A
  VRF: default
  Type: static
  Remote IP: 10.255.255.2
  Role: responder
path9:
  Source address: 172.16.3.3, Destination address: 172.16.2.0
  State: idle
  Uptime: N/A
  VRF: default
  Type: static
  Remote IP: 10.255.255.2
  Role: responder
path10:
  Source address: 172.16.2.5, Destination address: 172.16.2.0
  State: established
  Uptime: 17 minutes, 11 seconds
  VRF: default
  Type: static
  Remote IP: 10.255.255.2
  Role: responder
  Inbound SPI: 0xc09696:
    Request ID: 37, Mode: transport, Replay window size: 16384, Seq: 0x0
    Errors:
      Packets outside replay window: 0, Replay: 0, Integrity failed: 0
    Lifetime config:
      Soft byte limit: 4260868192499, Hard byte limit: 6442450944000
      Soft packet limit: 2500568514, Hard packet limit: 4000000000
      Soft time limit: 2604 secs, Hard time limit: 3600 secs
    Lifetime current:
      Current bytes: 1201604
      Current packets: 3617
      SA add time: Thu Mar 14 08:56:34 2024
      SA last use time: Thu Mar 14 09:14:16 2024
  Outbound SPI: 0xc326be:
    Request ID: 37, Mode: transport, Replay window size: 0, Seq: 0x0
    Errors:
      Packets outside replay window: 0, Replay: 0, Integrity failed: 0
    Lifetime config:
      Soft byte limit: 3942000894749, Hard byte limit: 6442450944000
      Soft packet limit: 2970777530, Hard packet limit: 4000000000
      Soft time limit: 2865 secs, Hard time limit: 3600 secs
    Lifetime current:
      Current bytes: 1889523
      Current packets: 7590
      SA add time: Thu Mar 14 08:56:34 2024
      SA last use time: Thu Mar 14 09:14:16 2024
path11:
  Source address: 172.16.255.0, Destination address: 172.16.2.2
  State: idle
  Uptime: N/A
  VRF: default
  Type: static
  Remote IP: 10.255.255.2
  Role: responder
path12:
  Source address: 172.16.255.0, Destination address: 172.16.2.7
  State: idle
  Uptime: N/A
  VRF: default
  Type: static
  Remote IP: 10.255.255.2
  Role: responder
path13:
  Source address: 172.16.255.0, Destination address: 172.16.2.0
  State: idle
  Uptime: N/A
  VRF: default
  Type: static
  Remote IP: 10.255.255.2
  Role: responder
path14:
  Source address: 172.16.255.0, Destination address: 172.16.255.1
  State: established
  Uptime: 0 seconds
  VRF: default
  Type: static
  Remote IP: 10.255.255.2
  Role: responder
  Inbound SPI: 0xc5edb7:
    Request ID: 36, Mode: transport, Replay window size: 16384, Seq: 0x0
    Errors:
      Packets outside replay window: 0, Replay: 0, Integrity failed: 0
    Lifetime config:
      Soft byte limit: 3911730380249, Hard byte limit: 6442450944000
      Soft packet limit: 2550779613, Hard packet limit: 4000000000
      Soft time limit: 2597 secs, Hard time limit: 3600 secs
    Lifetime current:
      Current bytes: 448
      Current packets: 4
      SA add time: Thu Mar 14 09:13:45 2024
      SA last use time: Thu Mar 14 09:14:16 2024
  Outbound SPI: 0xc22e7d:
    Request ID: 36, Mode: transport, Replay window size: 0, Seq: 0x0
    Errors:
      Packets outside replay window: 0, Replay: 0, Integrity failed: 0
    Lifetime config:
      Soft byte limit: 3356216183249, Hard byte limit: 6442450944000
      Soft packet limit: 2875097007, Hard packet limit: 4000000000
      Soft time limit: 2665 secs, Hard time limit: 3600 secs
    Lifetime current:
      Current bytes: 402150
      Current packets: 126
      SA add time: Thu Mar 14 09:13:45 2024
      SA last use time: Thu Mar 14 09:14:16 2024
```

## show stun client translations detail

```text
Current System Time: Thu Mar 14 09:13:46 2024
Transaction ID 000000080affff0300000000
Agent Name: dps
Source Address: 172.16.255.0:4500
Public Address: 172.16.255.0:4500
Number of Attributes: 3
Timeout Interval: 0:03:00
Last Refreshed: 0:00:08 ago
Attribute Type   Length Value           
---------------- ------ ----------------
PATH_GROUP            4 PEER            
VTEP_IP               4 10.255.255.3    
WAN_ID                4 8               

```

## show stun server bindings detail

```text
Current System Time: Thu Mar 14 09:13:46 2024
Transaction ID 000000010affff0200000000
Public Address: 172.16.2.0:4500
Number of Attributes: 3
Timeout Interval: 0:00:40
Timeout: 0:00:07
Attribute Type   Length Value           
---------------- ------ ----------------
PATH_GROUP            3 ATT             
VTEP_IP               4 10.255.255.2    
WAN_ID                4 1               

Transaction ID 000000010affff0700000000
Public Address: 172.16.2.2:4500
Number of Attributes: 3
Timeout Interval: 0:00:40
Timeout: 0:00:02
Attribute Type   Length Value           
---------------- ------ ----------------
PATH_GROUP            3 ATT             
VTEP_IP               4 10.255.255.7    
WAN_ID                4 1               

Transaction ID 000000020affff0900000000
Public Address: 172.16.2.7:4500
Number of Attributes: 3
Timeout Interval: 0:00:40
Timeout: 0:00:33
Attribute Type   Length Value           
---------------- ------ ----------------
PATH_GROUP            3 ATT             
VTEP_IP               4 10.255.255.9    
WAN_ID                4 2               

```

## show path-selection paths detail

```text
Peer: 10.255.255.2, Path group ATT
Path name: path10, dynamic, Label: 8202
Source: 172.16.2.5, Port: 4500, WAN ID: 6
Destination: 172.16.2.0, Port: 4500, WAN ID: 1
Local interface: Ethernet1/4
Route state: IPsec established
Traffic class 0: active (0:00:46)
MTU: 8914

Peer: 10.255.255.4, Path group PEER
Path name: path14, static, Label: 8206
Source: 172.16.255.0, Port: 4500, WAN ID: 8
Destination: 172.16.255.1, Port: 4500, WAN ID: 2886795009
Local interface: Ethernet1/2
Route state: IPsec established
Traffic class 0: active (0:00:01)
MTU: 8914

Peer: 10.255.255.7, Path group ATT
Path name: path6, dynamic, Label: 8198
Source: 172.16.2.5, Port: 4500, WAN ID: 6
Destination: 172.16.2.2, Port: 4500, WAN ID: 1
Local interface: Ethernet1/4
Route state: IPsec established
Traffic class 0: inactive
MTU: 8914

Peer: 10.255.255.9, Path group ATT
Path name: path5, dynamic, Label: 8197
Source: 172.16.2.5, Port: 4500, WAN ID: 6
Destination: 172.16.2.7, Port: 4500, WAN ID: 2
Local interface: Ethernet1/4
Route state: IPsec established
Traffic class 0: active (0:00:46)
MTU: 1424

```

## show bgp neighbors

```text
BGP neighbor is 10.255.255.1, remote AS 65000, internal link
  BGP version 4, remote router ID 0.0.0.0, VRF default
  Inherits configuration from and member of peer-group autovpnEdges
  Last read never, last write never
  Hold time is 0, keepalive interval is 0 seconds
  Configured hold time is 180, keepalive interval is 60 seconds
  Effective minimum hold time is 3 seconds
  Send failure hold time is 0 seconds
  Hold timer is inactive
  Keepalive timer is inactive
  Connect timer is active, time left: 00:00:05
  Connection interval is 20 seconds
  Failed connection attempts is 385
  Idle-restart timer is inactive
  BGP state is Connect
  Number of transitions to established: 0
  Last state was Active
  Last event was ConnectRetry
  Last sent socket-error:Connect (Network is unreachable), Last time 02:27:52, First time 02:27:57, Repeats 1
  Types of communities advertised: extended
  Neighbor is a route reflector client
  Neighbor is using global cluster ID 10.255.255.3
  Neighbor Capabilities:
  Restart timer is inactive
  End of rib timer is inactive
  AIGP attribute send and receive for IPv4 Unicast are enabled
  AIGP attribute send and receive for IPv4 with MPLS Labels are enabled
  AIGP attribute send and receive for IPv6 Unicast are enabled
  AIGP attribute send and receive for IPv6 with MPLS Labels are enabled
  BGP session driven failover for IPv4 Unicast is disabled
  BGP session driven failover for IPv6 Unicast is disabled
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
Local AS is 65000, local router ID 10.255.255.3
TTL is 255
Local TCP address is 10.255.255.3
Remote TCP address is 10.255.255.1, remote port is 179
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

BGP neighbor is 10.255.255.2, remote AS 65000, internal link
  BGP version 4, remote router ID 10.255.255.2, VRF default
  Inherits configuration from and member of peer-group autovpnEdges
  Last read 00:00:41, last write 00:00:41
  Hold time is 180, keepalive interval is 60 seconds
  Configured hold time is 180, keepalive interval is 60 seconds
  Effective minimum hold time is 3 seconds
  Send failure hold time is 0 seconds
  Hold timer is active, time left: 00:02:19
  Keepalive timer is active, time left: 00:00:09
  Connect timer is inactive
  Idle-restart timer is inactive
  BGP state is Established, up for 00:00:42
  Number of transitions to established: 27
  Last state was OpenConfirm
  Last event was RecvUpdate
  Last sent notification:Cease/BFD down, Last time 00:00:51, First time 00:01:05, Repeats 1
  Last rcvd notification:Cease/BFD down, Last time 00:39:34, First time 00:45:11, Repeats 1
  Last sent socket-error:Connect (Network is unreachable), Last time 02:27:52, First time 02:27:57, Repeats 1
  Types of communities advertised: extended
  Enhanced route refresh stale path removal disabled
  Outbound enhanced route refresh enabled
  Neighbor is a route reflector client
  Neighbor is using global cluster ID 10.255.255.3
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
      Received 00:00:41
      Number of stale paths removed after graceful restart: 0
      Number of paths received before End-of-RIB: 3
    L2VPN EVPN End-of-RIB received: Yes
      Received 00:00:41
      Number of stale paths removed after graceful restart: 0
      Number of paths received before End-of-RIB: 8
  AIGP attribute send and receive for IPv4 Unicast are enabled
  AIGP attribute send and receive for IPv4 with MPLS Labels are enabled
  AIGP attribute send and receive for IPv6 Unicast are enabled
  AIGP attribute send and receive for IPv6 with MPLS Labels are enabled
  BGP session driven failover for IPv4 Unicast is disabled
  BGP session driven failover for IPv6 Unicast is disabled
  Message Statistics:
                                  Sent      Rcvd
    Opens:                          27        39
    Notifications:                  36         2
    Updates:                       388       341
    Keepalives:                    196       195
    Enhanced Route Refresh:          0         0
    Begin of Route Refresh:          0         0
    End of Route Refresh:            0         0
    Total messages:                647       577
  Prefix Statistics:
                                   Sent      Rcvd     Best Paths     Best ECMP Paths
    IPv4 Unicast:                     0         0              0                   0
    IPv4 Dps:                         3         3              3                   0
    IPv6 Unicast:                     0         0              0                   0
    EVPN:                             8         8              8                   0
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
Local AS is 65000, local router ID 10.255.255.3
TTL is 255
Local TCP address is 10.255.255.3, local port is 43621
Remote TCP address is 10.255.255.2, remote port is 179
Local next hop for next hop self:
  Dps: 10.255.255.3
  L2VPN EVPN: 10.255.255.3
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
    Retransmission Timeout (rto): 216.0ms
    Round-trip Time (rtt/rtvar): 13.0ms/16.7ms
    Delayed Ack Timeout (ato): 40.0ms
    Congestion Window (cwnd): 2
    TCP Throughput: 1.79 Mbps
    Recv Round-trip Time (rcv_rtt): 912.0ms
    Advertised Recv Window (rcv_space): 14480

BGP neighbor is 10.255.255.4, remote AS 65000, internal link
  BGP version 4, remote router ID 10.255.255.4, VRF default
  Inherits configuration from and member of peer-group PEER_TRANSIT
  Last read 02:23:51, last write 02:22:38
  Hold time is 180, keepalive interval is 60 seconds
  Configured hold time is 180, keepalive interval is 60 seconds
  Effective minimum hold time is 3 seconds
  Send failure hold time is 0 seconds
  Hold timer is inactive
  Keepalive timer is inactive
  Connect timer is inactive
  Idle-restart timer is inactive
  BGP state is Idle, Administratively shut down
  Peering failure hint: Administratively shut down
  Number of transitions to established: 1
  Last state was Established
  Last event was Open
  Last sent notification:Cease/connection rejected, Last time 00:04:49, First time 02:20:55, Repeats 46
  Last sent socket-error:Connect (Network is unreachable), Last time 02:27:48, First time 02:27:57, Repeats 2
  Types of communities advertised: standard extended large
  Neighbor is a route reflector client
  Neighbor is using global cluster ID 10.255.255.3
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
  BGP session driven failover for IPv4 Unicast is disabled
  BGP session driven failover for IPv6 Unicast is disabled
  Message Statistics:
                         Sent      Rcvd
    Opens:                  1        48
    Notifications:         48         0
    Updates:               24        63
    Keepalives:             3         2
    Route Refresh:          0         0
    Total messages:        76       113
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
Local AS is 65000, local router ID 10.255.255.3
TTL is 255
Remote TCP address is 10.255.255.4

BGP neighbor is 10.255.255.9, remote AS 65000, internal link
  BGP version 4, remote router ID 10.255.255.9, VRF default
  Inherits configuration from and member of peer-group autovpnEdges
  Last read 00:00:43, last write 00:00:41
  Hold time is 180, keepalive interval is 60 seconds
  Configured hold time is 180, keepalive interval is 60 seconds
  Effective minimum hold time is 3 seconds
  Send failure hold time is 0 seconds
  Hold timer is active, time left: 00:02:17
  Keepalive timer is active, time left: 00:00:02
  Connect timer is inactive
  Idle-restart timer is inactive
  BGP state is Established, up for 00:00:44
  Number of transitions to established: 1
  Last state was OpenConfirm
  Last event was RecvUpdate
  Types of communities advertised: extended
  Enhanced route refresh stale path removal disabled
  Outbound enhanced route refresh enabled
  Neighbor is a route reflector client
  Neighbor is using global cluster ID 10.255.255.3
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
      Received 00:00:43
      Number of stale paths removed after graceful restart: 0
      Number of paths received before End-of-RIB: 2
    L2VPN EVPN End-of-RIB received: Yes
      Received 00:00:43
      Number of stale paths removed after graceful restart: 0
      Number of paths received before End-of-RIB: 4
  AIGP attribute send and receive for IPv4 Unicast are enabled
  AIGP attribute send and receive for IPv4 with MPLS Labels are enabled
  AIGP attribute send and receive for IPv6 Unicast are enabled
  AIGP attribute send and receive for IPv6 with MPLS Labels are enabled
  BGP session driven failover for IPv4 Unicast is disabled
  BGP session driven failover for IPv6 Unicast is disabled
  Message Statistics:
                                  Sent      Rcvd
    Opens:                           1         1
    Notifications:                   0         0
    Updates:                        10         6
    Keepalives:                      2         2
    Enhanced Route Refresh:          0         0
    Begin of Route Refresh:          0         0
    End of Route Refresh:            0         0
    Total messages:                 13         9
  Prefix Statistics:
                                   Sent      Rcvd     Best Paths     Best ECMP Paths
    IPv4 Unicast:                     0         0              0                   0
    IPv4 Dps:                         4         2              2                   2
    IPv6 Unicast:                     0         0              0                   0
    EVPN:                             8         4              4                   4
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
Local AS is 65000, local router ID 10.255.255.3
TTL is 255
Local TCP address is 10.255.255.3, local port is 179
Remote TCP address is 10.255.255.9, remote port is 34139
Local next hop for next hop self:
  Dps: 10.255.255.3
  L2VPN EVPN: 10.255.255.3
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
    Round-trip Time (rtt/rtvar): 6.9ms/7.0ms
    Delayed Ack Timeout (ato): 40.0ms
    Congestion Window (cwnd): 10
    TCP Throughput: 15.97 Mbps
    Recv Round-trip Time (rcv_rtt): 4.0ms
    Advertised Recv Window (rcv_space): 14600

```

## show bgp path-selection detail

```text
BGP routing table information for VRF default
Router identifier 10.255.255.3, local AS number 65000
Bgp routing table entry for ipv4Dps VTEP 10.255.255.9/32
 Paths: 2 available
  Local (Received from a RR-client)
    :: from 10.255.255.9 (10.255.255.9)
      Origin IGP, metric -, localpref 100, weight 0, received 00:00:44 ago, valid, internal
      Tunnel encapsulation attribute: Dynamic path selection
        Endpoint: 172.16.2.7, Path group name: ATT, WAN ID: 2, UDP port: 4500
  Local (Received from a RR-client)
    :: from 10.255.255.2 (10.255.255.2)
      Origin IGP, metric -, localpref 100, weight 0, received 00:00:43 ago, valid, internal
      Tunnel encapsulation attribute: Dynamic path selection
        Endpoint: 172.16.2.7, Path group name: ATT, WAN ID: 2, UDP port: 4500
Bgp routing table entry for ipv4Ipsec VTEP 10.255.255.2/32
 Paths: 1 available
  Local (Received from a RR-client)
    :: from 10.255.255.2 (10.255.255.2)
      Origin IGP, metric -, localpref 100, weight 0, received 00:00:43 ago, valid, internal
      Tunnel encapsulation attribute: IP security
        Initial contact: false, Rekey counter: 0, Nonce length: 32
        DH group: 14, DH key length: 256
        Encryption algo: aes256, Authentication algo: sha256
Bgp routing table entry for ipv4Ipsec VTEP 10.255.255.3/32
 Paths: 1 available
  Local
    - from - (0.0.0.0)
      Origin IGP, metric -, localpref -, weight 0, received 01:49:22 ago, valid, local
      Tunnel encapsulation attribute: IP security
        Initial contact: false, Rekey counter: 0, Nonce length: 32
        DH group: 14, DH key length: 256
        Encryption algo: aes256, Authentication algo: sha256
Bgp routing table entry for ipv4Ipsec VTEP 10.255.255.9/32
 Paths: 2 available
  Local (Received from a RR-client)
    :: from 10.255.255.9 (10.255.255.9)
      Origin IGP, metric -, localpref 100, weight 0, received 00:00:44 ago, valid, internal
      Tunnel encapsulation attribute: IP security
        Initial contact: false, Rekey counter: 2, Nonce length: 32
        DH group: 14, DH key length: 256
        Encryption algo: aes256, Authentication algo: sha256
  Local (Received from a RR-client)
    :: from 10.255.255.2 (10.255.255.2)
      Origin IGP, metric -, localpref 100, weight 0, received 00:00:43 ago, valid, internal
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
>C    10.255.255.3/32 [0 pref/0 metric] updated 02:28:03 ago
         via Loopback0, directly connected
>C    172.16.2.4/31 [0 pref/0 metric] updated 00:17:22 ago
         via Ethernet1/4, directly connected
>C    172.16.3.2/31 [0 pref/0 metric] updated 00:17:22 ago
         via Ethernet1/3, directly connected
>C    172.16.255.0/31 [0 pref/0 metric] updated 00:17:22 ago
         via Ethernet1/2, directly connected
>C    172.28.128.0/20 [0 pref/0 metric] updated 02:27:33 ago
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
>S    10.80.0.0/12 [1 pref/0 metric] updated 02:27:33 ago
         via 172.28.128.1 [0 pref/0 metric] type ipv4
            via 172.28.128.1, Management1/1
>S    10.224.0.0/12 [1 pref/0 metric] updated 02:27:33 ago
         via 172.28.128.1 [0 pref/0 metric] type ipv4
            via 172.28.128.1, Management1/1
>S    10.240.0.0/12 [1 pref/0 metric] updated 02:27:33 ago
         via 172.28.128.1 [0 pref/0 metric] type ipv4
            via 172.28.128.1, Management1/1
>S    172.16.0.0/12 [1 pref/0 metric] updated 02:27:33 ago
         via 172.28.128.1 [0 pref/0 metric] type ipv4
            via 172.28.128.1, Management1/1
>S    172.16.2.0/24 [1 pref/0 metric] updated 00:17:22 ago
         via 172.16.2.4 [0 pref/0 metric] type ipv4
            via 172.16.2.4, Ethernet1/4
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
>P    0.0.0.0/8 [1 pref/0 metric] updated 02:28:02 ago
         via Null0, directly connected [NF]
>P    10.255.255.2/32 [1 pref/0 metric] updated 00:17:19 ago
         via 10.255.255.2, Dps1
>P    10.255.255.4/32 [1 pref/0 metric] updated 00:17:25 ago
         via 10.255.255.4, Dps1
>P    10.255.255.7/32 [1 pref/0 metric] updated 00:07:49 ago
         via 10.255.255.7, Dps1
>P    10.255.255.9/32 [1 pref/0 metric] updated 00:17:15 ago
         via 10.255.255.9, Dps1
>P    127.0.0.0/8 [1 pref/0 metric] updated 02:28:02 ago
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
>P    ::/96 [1 pref/0 metric] updated 02:27:05 ago
         via Null0, directly connected [NF]
>P    ::ffff:127.0.0.0/104 [1 pref/0 metric] updated 02:27:05 ago
         via :: [1 pref/1 metric] type ipv6
            via , directly connected
>P    fe80::/10 [1 pref/0 metric] updated 02:27:05 ago
```

