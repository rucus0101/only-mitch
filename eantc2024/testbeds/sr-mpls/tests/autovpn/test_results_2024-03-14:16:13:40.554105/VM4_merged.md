# Test results for VM4

## show version

```text
Arista vEOS
Hardware version: 
Serial number: 59F53F681319991A9AF269BA2A23256F
Hardware MAC address: 000c.29d5.32d4
System MAC address: 000c.29d5.32d4

Software image version: 4.31.2F-cloud
Architecture: i686
Internal build version: 4.31.2F-cloud-35442146.4312F
Internal build ID: 635a071a-386e-447f-942c-bcc34d9ffd3c
Image format version: 1.0
Image optimization: None

Uptime: 17 hours and 59 minutes
Total memory: 16264236 kB
Free memory: 10327528 kB

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
Ethernet1       172.16.1.7/31         up         up              9000          
Ethernet2       10.4.255.2/31         up         up              1500          
Loopback0       10.255.255.10/32      up         up             65535          
Management1     172.28.138.243/20     up         up              1500          

```

## show interfaces counters rates | nz

```text
Port      Name      Intvl  In Mbps      %  In Kpps Out Mbps      % Out Kpps
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
           via 172.16.1.6, Ethernet1

 S        10.255.255.1/32
           directly connected, Dps1
 S        10.255.255.4/32
           directly connected, Dps1
 S        10.255.255.8/32
           directly connected, Dps1
 C        10.255.255.10/32
           directly connected, Loopback0
 C        172.16.1.6/31
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
           via 172.16.1.6, Ethernet1

 S        10.255.255.1/32
           directly connected, Dps1
 S        10.255.255.4/32
           directly connected, Dps1
 S        10.255.255.8/32
           directly connected, Dps1
 C        10.255.255.10/32
           directly connected, Loopback0
 C        172.16.1.6/31
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
 B I      10.1.255.0/31 [20/0]
           via VTEP 10.255.255.1 VNI 201 router-mac ec:8a:48:04:f5:30
 B I      10.1.255.2/31 [20/0]
           via VTEP 10.255.255.1 VNI 201 router-mac ec:8a:48:04:f5:30
 B I      10.2.255.0/31 [20/0]
           via VTEP 10.255.255.8 VNI 201 router-mac ec:8a:48:04:2c:53
 B I      10.2.255.2/31 [20/0]
           via VTEP 10.255.255.8 VNI 201 router-mac ec:8a:48:04:2c:53
 O        10.4.255.0/31 [110/20]
           via 10.4.255.3, Ethernet2
 C        10.4.255.2/31
           directly connected, Ethernet2
 B I      10.5.255.0/31 [20/0]
           via VTEP 10.255.255.4 VNI 201 router-mac ec:8a:48:04:ff:5b
 B I      10.5.255.2/31 [20/0]
           via VTEP 10.255.255.4 VNI 201 router-mac ec:8a:48:04:ff:5b
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
           via VTEP 10.255.255.11 VNI 201 router-mac 00:0c:29:ba:2d:5e
           via VTEP 10.255.255.12 VNI 201 router-mac 00:0c:29:78:c5:2d
 O        10.255.254.5/32 [110/20]
           via 10.4.255.3, Ethernet2
 B I      10.255.254.6/32 [20/0]
           via VTEP 10.255.255.4 VNI 201 router-mac ec:8a:48:04:ff:5b
 B I      192.168.0.0/24 [20/0]
           via VTEP 10.255.255.5 VNI 201 router-mac ec:8a:48:04:21:53
 B I      192.168.1.0/24 [20/0]
           via VTEP 10.255.255.1 VNI 201 router-mac ec:8a:48:04:f5:30
 B I      192.168.3.0/24 [20/0]
           via VTEP 10.255.255.8 VNI 201 router-mac ec:8a:48:04:2c:53
 B I      192.168.5.0/24 [20/0]
           via VTEP 10.255.255.4 VNI 201 router-mac ec:8a:48:04:ff:5b
 B I      192.168.6.0/24 [20/0]
           via VTEP 10.255.255.11 VNI 201 router-mac 00:0c:29:ba:2d:5e
           via VTEP 10.255.255.12 VNI 201 router-mac 00:0c:29:78:c5:2d
 O        192.168.40.0/24 [110/20]
           via 10.4.255.3, Ethernet2

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
Router identifier 10.255.255.10, local AS number 65000
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
                                 -                     -       -       0       i
 * >      RD: 10.255.255.10:1 ip-prefix 10.4.255.2/31
                                 -                     -       -       0       i
 * >      RD: 10.255.255.4:1 ip-prefix 10.5.255.0/31
                                 10.255.255.4          -       100     0       i Or-ID: 10.255.255.4 C-LST: 10.255.255.1 
 * >      RD: 10.255.255.4:1 ip-prefix 10.5.255.2/31
                                 10.255.255.4          -       100     0       i Or-ID: 10.255.255.4 C-LST: 10.255.255.1 
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
                                 -                     -       -       0       i
 * >      RD: 10.255.255.4:1 ip-prefix 10.255.254.6/32
                                 10.255.255.4          -       100     0       i Or-ID: 10.255.255.4 C-LST: 10.255.255.1 
 * >      RD: 10.255.255.5:1 ip-prefix 192.168.0.0/24
                                 10.255.255.5          -       100     0       i Or-ID: 10.255.255.5 C-LST: 10.255.255.1 
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
                                 -                     -       -       0       i
```

## show ip security connection detail

```text
path1:
  Source address: 172.16.1.7, Destination address: 172.16.1.0
  State: established
  Uptime: 42 minutes, 2 seconds
  VRF: default
  Type: static
  Remote IP: 10.255.255.8
  Role: responder
  Inbound SPI: 0xc5b611:
    Request ID: 12, Mode: transport, Replay window size: 16384, Seq: 0x0
    Errors:
      Packets outside replay window: 0, Replay: 0, Integrity failed: 0
    Lifetime config:
      Soft byte limit: 4605381017999, Hard byte limit: 6442450944000
      Soft packet limit: 2281731478, Hard packet limit: 4000000000
      Soft time limit: 2795 secs, Hard time limit: 3600 secs
    Lifetime current:
      Current bytes: 1818022052
      Current packets: 1719809
      SA add time: Thu Mar 14 15:35:13 2024
      SA last use time: Thu Mar 14 16:16:44 2024
  Outbound SPI: 0xc42597:
    Request ID: 12, Mode: transport, Replay window size: 0, Seq: 0x0
    Errors:
      Packets outside replay window: 0, Replay: 0, Integrity failed: 0
    Lifetime config:
      Soft byte limit: 3663565470749, Hard byte limit: 6442450944000
      Soft packet limit: 2782128057, Hard packet limit: 4000000000
      Soft time limit: 2773 secs, Hard time limit: 3600 secs
    Lifetime current:
      Current bytes: 4179204511
      Current packets: 8219746
      SA add time: Thu Mar 14 15:35:13 2024
      SA last use time: Thu Mar 14 16:16:44 2024
path2:
  Source address: 172.16.1.7, Destination address: 172.16.1.5
  State: idle
  Uptime: N/A
  VRF: default
  Type: static
  Remote IP: 10.255.255.8
  Role: responder
path3:
  Source address: 172.16.1.7, Destination address: 172.16.1.2
  State: established
  Uptime: 15 minutes, 55 seconds
  VRF: default
  Type: dynamic
  Remote IP: 10.255.255.8
  Role: responder
  Packets in: 0, Packets out: 0
  Last known rekey count: 0
  Dynamic state: established
  Last established time: Thu Mar 14 16:01:34 2024
  DH crypto:
    Local rekey: 2, Peer rekey: 5, In SPI: 0x1199b992, Out SPI: 0x7af27082
  DH state:
    Local rekey: 2, Peer rekey: 5, DH rekey state: not rekeying, Role: not rekeying
  SA rekey role: not rekeying
  SA state:
    SA type: ingress , SPI: 0x83f490da
      Role: responder, SA rekey state: initial, Peer nonce type: init
      Add time: Thu Mar 14 16:01:19 2024, Packets: 1602, Pair SPI: 0x1a9bd9ea
    SA type: egress , SPI: 0x1a9bd9ea
      Role: responder, SA rekey state: initial, Peer nonce type: init
      Add time: Thu Mar 14 16:01:19 2024, Packets: 3944, Pair SPI: 0x83f490da
  Inbound SPI: 0x83f490da:
    Request ID: 30, Mode: transport, Replay window size: 0, Seq: 0x0
    Errors:
      Packets outside replay window: 0, Replay: 0, Integrity failed: 0
    Lifetime config:
      Soft byte limit: 4797796629750, Hard byte limit: 6442450944000
      Soft packet limit: 2975411875, Hard packet limit: 4000000000
      Soft time limit: 2547 secs, Hard time limit: 3600 secs
    Lifetime current:
      Current bytes: 299912
      Current packets: 1602
      SA add time: Thu Mar 14 16:01:19 2024
      SA last use time: Thu Mar 14 16:16:43 2024
  Outbound SPI: 0x1a9bd9ea:
    Request ID: 30, Mode: transport, Replay window size: 0, Seq: 0x0
    Errors:
      Packets outside replay window: 0, Replay: 0, Integrity failed: 0
    Lifetime config:
      Soft byte limit: 4701213653625, Hard byte limit: 6442450944000
      Soft packet limit: 2944135982, Hard packet limit: 4000000000
      Soft time limit: 2653 secs, Hard time limit: 3600 secs
    Lifetime current:
      Current bytes: 1700208
      Current packets: 3944
      SA add time: Thu Mar 14 16:01:19 2024
      SA last use time: Thu Mar 14 16:16:43 2024
```

## show stun client translations detail

```text
Current System Time: Thu Mar 14 16:17:15 2024
Transaction ID 000000010affff0a00000000
Agent Name: dps
Source Address: 172.16.1.7:4500
Public Address: 172.16.1.7:4500
Number of Attributes: 3
Timeout Interval: 0:03:00
Last Refreshed: 0:01:01 ago
Attribute Type   Length Value           
---------------- ------ ----------------
PATH_GROUP            7 VZ_NEAR         
VTEP_IP               4 10.255.255.10   
WAN_ID                4 1               

```

## show stun server bindings detail

```text
Current System Time: Thu Mar 14 16:17:16 2024
```

## show path-selection paths detail

```text
Peer: 10.255.255.1, Path group VZ_NEAR
Path name: path1, static, Label: 1
Source: 172.16.1.7, Port: 4500, WAN ID: 1
Destination: 172.16.1.0, Port: 4500, WAN ID: 2886729984
Local interface: Ethernet1
Route state: IPsec established
Traffic class 0: active (0:42:00)
MTU: 8914

Peer: 10.255.255.4, Path group VZ_NEAR
Path name: path2, static, Label: 2
Source: 172.16.1.7, Port: 4500, WAN ID: 1
Destination: 172.16.1.5, Port: 4500, WAN ID: 2886729989
Local interface: Ethernet1
Route state: IPsec pending
Traffic class 0: inactive
MTU: 0

Peer: 10.255.255.8, Path group VZ_NEAR
Path name: path3, dynamic, Label: 3
Source: 172.16.1.7, Port: 4500, WAN ID: 1
Destination: 172.16.1.2, Port: 4500, WAN ID: 1
Local interface: Ethernet1
Route state: IPsec established
Traffic class 0: active (0:00:26)
MTU: 8914

```

## show bgp neighbors

```text
BGP neighbor is 10.255.255.1, remote AS 65000, internal link
  BGP version 4, remote router ID 10.255.255.1, VRF default
  Inherits configuration from and member of peer-group PATHFINDER
  Last read 00:00:18, last write 00:00:21
  Hold time is 180, keepalive interval is 60 seconds
  Configured hold time is 180, keepalive interval is 60 seconds
  Effective minimum hold time is 3 seconds
  Send failure hold time is 0 seconds
  Hold timer is active, time left: 00:02:42
  Keepalive timer is active, time left: 00:00:22
  Connect timer is inactive
  Idle-restart timer is inactive
  BGP state is Established, up for 01:08:33
  Number of transitions to established: 46
  Last state was OpenConfirm
  Last event was RecvUpdate
  Last sent notification:Hold Timer Expired Error/None, Last time 01:09:39, First time 03:03:14, Repeats 6
  Last rcvd notification:Cease/BFD down, Last time 03:23:53, First time 03:48:52, Repeats 4
  Last sent socket-error:Connect (Network is unreachable), Last time 17:58:48
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
      Received 01:08:32
      Number of stale paths removed after graceful restart: 0
      Number of paths received before End-of-RIB: 14
    L2VPN EVPN End-of-RIB received: Yes
      Received 01:08:32
      Number of stale paths removed after graceful restart: 0
      Number of paths received before End-of-RIB: 17
  AIGP attribute send and receive for IPv4 Unicast are enabled
  AIGP attribute send and receive for IPv4 with MPLS Labels are enabled
  AIGP attribute send and receive for IPv6 Unicast are enabled
  AIGP attribute send and receive for IPv6 with MPLS Labels are enabled
  BGP session driven failover for IPv6 Unicast is disabled
  BGP session driven failover for IPv4 Unicast is disabled
  Message Statistics:
                                  Sent      Rcvd
    Opens:                          46        46
    Notifications:                  40         5
    Updates:                       235      2647
    Keepalives:                   1285      1203
    Enhanced Route Refresh:          0         0
    Begin of Route Refresh:          0         0
    End of Route Refresh:            0         0
    Total messages:               1606      3901
  Prefix Statistics:
                                   Sent      Rcvd     Best Paths     Best ECMP Paths
    IPv4 Unicast:                     0         0              0                   0
    IPv4 Dps:                         2        10             10                   0
    IPv6 Unicast:                     0         0              0                   0
    EVPN:                             4        21             21                   0
  Configured maximum total number of routes is 12000
  Inbound updates dropped by reason:
    AS path loop detection: 0
    Cluster ID loop detection: 0
    Enforced First AS: 0
    Malformed MPBGP routes: 0
    Originator ID matches local router ID: 28
    Nexthop matches local IP address: 1
    Unexpected IPv6 nexthop for IPv4 routes: 0
  Inbound updates with attribute errors:
    Resulting in removal of all paths in update (treat as withdraw): 1
    Resulting in AFI/SAFI disable: 0
    Resulting in attribute ignore: 0
    Disabled AFI/SAFIs: None
    Last treat-as-withdraw attribute error: Nexthop is local address
    Last update with error received at: 01:08:32
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
Local AS is 65000, local router ID 10.255.255.10
TTL is 255
Local TCP address is 10.255.255.10, local port is 38375
Remote TCP address is 10.255.255.1, remote port is 179
Local next hop for next hop self:
  Dps: 10.255.255.10
  L2VPN EVPN: 10.255.255.10
BFD is enabled with configured transmit interval 1000ms, receive interval 1000ms, multiplier 3 and state is Down
TCP Socket Information:
  TCP state is ESTABLISHED
  Recv-Q: 0/32768
  Send-Q: 0/46080
  Outgoing Maximum Segment Size (MSS): 1448
  Total Number of TCP retransmissions: 10
  Options:
    Timestamps enabled: yes
    Selective Acknowledgments enabled: yes
    Window Scale enabled: yes
    Explicit Congestion Notification (ECN) enabled: no
  Socket Statistics:
    Window Scale (wscale): 7,7
    Retransmission Timeout (rto): 204.0ms
    Round-trip Time (rtt/rtvar): 3.9ms/0.8ms
    Delayed Ack Timeout (ato): 40.0ms
    Congestion Window (cwnd): 2
    Slow-start Threshold (ssthresh): 7
    TCP Throughput: 5.97 Mbps
    Recv Round-trip Time (rcv_rtt): 8.0ms
    Advertised Recv Window (rcv_space): 29971

BGP neighbor is 10.255.255.4, remote AS 65000, internal link
  BGP version 4, remote router ID 10.255.255.4, VRF default
  Inherits configuration from and member of peer-group PATHFINDER
  Last read 00:02:16, last write 00:02:11
  Hold time is 180, keepalive interval is 60 seconds
  Configured hold time is 180, keepalive interval is 60 seconds
  Effective minimum hold time is 3 seconds
  Send failure hold time is 0 seconds
  Hold timer is inactive
  Keepalive timer is inactive
  Connect timer is active, time left: 00:00:04
  Connection interval is 20 seconds
  Failed connection attempts is 6
  Idle-restart timer is inactive
  BGP state is Connect
  Peering failure hint: Cease/BFD down
  Number of transitions to established: 55
  Last state was Active
  Last event was ConnectRetry
  Last sent notification:Cease/BFD down, Last time 00:02:11, First time 00:56:57, Repeats 10
  Last rcvd notification:Cease/BFD down, Last time 00:02:18, First time 16:59:39, Repeats 8
  Last sent socket-error:Connect (Network is unreachable), Last time 17:58:48
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
    Opens:                 58        55
    Notifications:         49         9
    Updates:              274      3053
    Keepalives:          1280      1208
    Route Refresh:          0         0
    Total messages:      1661      4325
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
    Originator ID matches local router ID: 2
    Nexthop matches local IP address: 1
    Unexpected IPv6 nexthop for IPv4 routes: 0
  Inbound updates with attribute errors:
    Resulting in removal of all paths in update (treat as withdraw): 1
    Resulting in AFI/SAFI disable: 0
    Resulting in attribute ignore: 0
    Disabled AFI/SAFIs: None
    Last treat-as-withdraw attribute error: Nexthop is local address
    Last update with error received at: 00:02:16
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
Local AS is 65000, local router ID 10.255.255.10
TTL is 255
Local TCP address is 10.255.255.10
Remote TCP address is 10.255.255.4, remote port is 179
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

```

## show bgp path-selection detail

```text
BGP routing table information for VRF default
Router identifier 10.255.255.10, local AS number 65000
Bgp routing table entry for ipv4Dps VTEP 10.255.255.5/32
 Paths: 1 available
  Local
    :: from 10.255.255.1 (10.255.255.1)
      Origin IGP, metric -, localpref 100, weight 0, received 00:21:04 ago, valid, internal
      Tunnel encapsulation attribute: Dynamic path selection
        Endpoint: 172.16.0.1, Path group name: VZ_OFF, WAN ID: 1, UDP port: 4500
Bgp routing table entry for ipv4Dps VTEP 10.255.255.8/32
 Paths: 1 available
  Local
    :: from 10.255.255.1 (10.255.255.1)
      Origin IGP, metric -, localpref 100, weight 0, received 00:15:58 ago, valid, internal
      Tunnel encapsulation attribute: Dynamic path selection
        Endpoint: 172.16.1.2, Path group name: VZ_NEAR, WAN ID: 1, UDP port: 4500
Bgp routing table entry for ipv4Dps VTEP 10.255.255.10/32
 Paths: 1 available
  Local
    - from - (0.0.0.0)
      Origin IGP, metric -, localpref -, weight 0, received 16:40:40 ago, valid, local
      Tunnel encapsulation attribute: Dynamic path selection
        Endpoint: 172.16.1.7, Path group name: VZ_NEAR, WAN ID: 1, UDP port: 4500
Bgp routing table entry for ipv4Dps VTEP 10.255.255.11/32
 Paths: 1 available
  Local
    :: from 10.255.255.1 (10.255.255.1)
      Origin IGP, metric -, localpref 100, weight 0, received 01:08:31 ago, valid, internal
      Tunnel encapsulation attribute: Dynamic path selection
        Endpoint: 172.16.0.9, Path group name: VZ_OFF, WAN ID: 2, UDP port: 4500
Bgp routing table entry for ipv4Dps VTEP 10.255.255.12/32
 Paths: 1 available
  Local
    :: from 10.255.255.1 (10.255.255.1)
      Origin IGP, metric -, localpref 100, weight 0, received 01:08:28 ago, valid, internal
      Tunnel encapsulation attribute: Dynamic path selection
        Endpoint: 172.16.0.11, Path group name: VZ_OFF, WAN ID: 2, UDP port: 4500
Bgp routing table entry for ipv4Ipsec VTEP 10.255.255.1/32
 Paths: 1 available
  Local
    :: from 10.255.255.1 (10.255.255.1)
      Origin IGP, metric -, localpref 100, weight 0, received 01:08:33 ago, valid, internal
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
    :: from 10.255.255.1 (10.255.255.1)
      Origin IGP, metric -, localpref 100, weight 0, received 00:21:04 ago, valid, internal
      Tunnel encapsulation attribute: IP security
        Initial contact: false, Rekey counter: 0, Nonce length: 32
        DH group: 14, DH key length: 256
        Encryption algo: aes256, Authentication algo: sha256
Bgp routing table entry for ipv4Ipsec VTEP 10.255.255.8/32
 Paths: 1 available
  Local
    :: from 10.255.255.1 (10.255.255.1)
      Origin IGP, metric -, localpref 100, weight 0, received 00:15:58 ago, valid, internal
      Tunnel encapsulation attribute: IP security
        Initial contact: false, Rekey counter: 5, Nonce length: 32
        DH group: 14, DH key length: 256
        Encryption algo: aes256, Authentication algo: sha256
Bgp routing table entry for ipv4Ipsec VTEP 10.255.255.10/32
 Paths: 1 available
  Local
    - from - (0.0.0.0)
      Origin IGP, metric -, localpref -, weight 0, received 17:58:44 ago, valid, local
      Tunnel encapsulation attribute: IP security
        Initial contact: false, Rekey counter: 2, Nonce length: 32
        DH group: 14, DH key length: 256
        Encryption algo: aes256, Authentication algo: sha256
Bgp routing table entry for ipv4Ipsec VTEP 10.255.255.11/32
 Paths: 1 available
  Local
    :: from 10.255.255.1 (10.255.255.1)
      Origin IGP, metric -, localpref 100, weight 0, received 01:08:31 ago, valid, internal
      Tunnel encapsulation attribute: IP security
        Initial contact: false, Rekey counter: 3, Nonce length: 32
        DH group: 14, DH key length: 256
        Encryption algo: aes256, Authentication algo: sha256
Bgp routing table entry for ipv4Ipsec VTEP 10.255.255.12/32
 Paths: 1 available
  Local
    :: from 10.255.255.1 (10.255.255.1)
      Origin IGP, metric -, localpref 100, weight 0, received 01:08:28 ago, valid, internal
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
>C    10.255.255.10/32 [0 pref/0 metric] updated 17:58:54 ago
         via Loopback0, directly connected
>C    172.16.1.6/31 [0 pref/0 metric] updated 16:40:45 ago
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
>S    0.0.0.0/0 [1 pref/0 metric] updated 16:40:45 ago
         via 172.16.1.6 [0 pref/0 metric] type ipv4
            via 172.16.1.6, Ethernet1
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
>P    0.0.0.0/8 [1 pref/0 metric] updated 17:58:53 ago
         via Null0, directly connected [NF]
>P    10.255.255.1/32 [1 pref/0 metric] updated 17:58:44 ago
         via 10.255.255.1, Dps1
>P    10.255.255.4/32 [1 pref/0 metric] updated 17:58:44 ago
         via 10.255.255.4, Dps1
>P    10.255.255.8/32 [1 pref/0 metric] updated 00:15:58 ago
         via 10.255.255.8, Dps1
>P    127.0.0.0/8 [1 pref/0 metric] updated 17:58:53 ago
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
>P    ::/96 [1 pref/0 metric] updated 17:58:46 ago
         via Null0, directly connected [NF]
>P    ::ffff:127.0.0.0/104 [1 pref/0 metric] updated 17:58:46 ago
         via :: [1 pref/1 metric] type ipv6
            via , directly connected
>P    fe80::/10 [1 pref/0 metric] updated 17:58:46 ago
```

