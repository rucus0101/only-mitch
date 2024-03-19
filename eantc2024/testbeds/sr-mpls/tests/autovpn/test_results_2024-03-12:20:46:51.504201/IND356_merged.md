# Test results for IND356

## show version

```text
Arista AWE-5510-F
Hardware version: 11.01
Serial number: WTW23160930
Hardware MAC address: ec8a.4804.f569
System MAC address: ec8a.4804.f569

Software image version: 4.31.2F
Architecture: x86_64
Internal build version: 4.31.2F-35442176.4312F
Internal build ID: 500c58e3-5beb-4481-afe9-8ad77245cc44
Image format version: 3.0
Image optimization: Default

Uptime: 1 hour and 52 minutes
Total memory: 65396488 kB
Free memory: 39980780 kB

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
Ethernet1/1      172.16.2.0/31        up         up              9000          
Ethernet1/2      172.16.3.1/31        up         up              1500          
Loopback0        10.255.255.2/32      up         up             65535          
Management1/1    172.28.137.227/20    up         up              1500          

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

Gateway of last resort is not set

 S        10.80.0.0/12 [1/0]
           via 172.28.128.1, Management1/1
 S        10.239.0.0/16 [1/0]
           via 172.28.128.1, Management1/1
 S        10.240.0.0/13 [1/0]
           via 172.28.128.1, Management1/1
 C        10.255.255.2/32
           directly connected, Loopback0
 S        10.255.255.3/32
           directly connected, Dps1
 S        10.255.255.7/32
           directly connected, Dps1
 S        10.255.255.9/32
           directly connected, Dps1
 C        172.16.2.0/31
           directly connected, Ethernet1/1
 S        172.16.2.0/24 [1/0]
           via 172.16.2.1, Ethernet1/1
 C        172.16.3.0/31
           directly connected, Ethernet1/2
 S        172.16.3.0/24 [1/0]
           via 172.16.3.0, Ethernet1/2
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
 S        10.239.0.0/16 [1/0]
           via 172.28.128.1, Management1/1
 S        10.240.0.0/13 [1/0]
           via 172.28.128.1, Management1/1
 C        10.255.255.2/32
           directly connected, Loopback0
 S        10.255.255.3/32
           directly connected, Dps1
 S        10.255.255.7/32
           directly connected, Dps1
 S        10.255.255.9/32
           directly connected, Dps1
 C        172.16.2.0/31
           directly connected, Ethernet1/1
 S        172.16.2.0/24 [1/0]
           via 172.16.2.1, Ethernet1/1
 C        172.16.3.0/31
           directly connected, Ethernet1/2
 S        172.16.3.0/24 [1/0]
           via 172.16.3.0, Ethernet1/2
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
Router identifier 10.255.255.2, local AS number 65000
Route status codes: * - valid, > - active, S - Stale, E - ECMP head, e - ECMP
                    c - Contributing to ECMP, % - Pending best path selection
Origin codes: i - IGP, e - EGP, ? - incomplete
AS Path Attributes: Or-ID - Originator ID, C-LST - Cluster List, LL Nexthop - Link Local Nexthop

          Network                Next Hop              Metric  LocPref Weight  Path
 * >      RD: 10.255.255.3:1 ip-prefix 10.0.255.0/31
                                 10.255.255.3          -       100     0       i
 * >      RD: 10.255.255.3:1 ip-prefix 10.0.255.2/31
                                 10.255.255.3          -       100     0       i
 * >      RD: 10.255.255.3:1 ip-prefix 10.1.255.0/31
                                 10.255.255.3          -       100     0       i
 * >Ec    RD: 10.255.255.7:1 ip-prefix 10.2.255.0/31
                                 10.255.255.7          -       100     0       i
 *  ec    RD: 10.255.255.7:1 ip-prefix 10.2.255.0/31
                                 10.255.255.7          -       100     0       i Or-ID: 10.255.255.7 C-LST: 10.255.255.3 
 * >Ec    RD: 10.255.255.9:1 ip-prefix 10.4.255.0/31
                                 10.255.255.9          -       100     0       i
 *  ec    RD: 10.255.255.9:1 ip-prefix 10.4.255.0/31
                                 10.255.255.9          -       100     0       i Or-ID: 10.255.255.9 C-LST: 10.255.255.3 
 * >Ec    RD: 10.255.255.9:1 ip-prefix 10.4.255.2/31
                                 10.255.255.9          -       100     0       i
 *  ec    RD: 10.255.255.9:1 ip-prefix 10.4.255.2/31
                                 10.255.255.9          -       100     0       i Or-ID: 10.255.255.9 C-LST: 10.255.255.3 
 * >      RD: 10.255.255.3:1 ip-prefix 10.5.255.0/31
                                 10.255.255.3          -       100     0       i
 * >      RD: 10.255.255.3:1 ip-prefix 10.5.255.2/31
                                 10.255.255.3          -       100     0       i
 * >      RD: 10.255.255.3:1 ip-prefix 10.6.255.0/31
                                 10.255.255.3          -       100     0       i
 * >      RD: 10.255.255.3:1 ip-prefix 10.6.255.2/31
                                 10.255.255.3          -       100     0       i
 * >      RD: 10.255.255.3:1 ip-prefix 10.255.254.1/32
                                 10.255.255.3          -       100     0       i
 * >      RD: 10.255.255.3:1 ip-prefix 10.255.254.2/32
                                 10.255.255.3          -       100     0       i
 * >Ec    RD: 10.255.255.7:1 ip-prefix 10.255.254.3/32
                                 10.255.255.7          -       100     0       i
 *  ec    RD: 10.255.255.7:1 ip-prefix 10.255.254.3/32
                                 10.255.255.7          -       100     0       i Or-ID: 10.255.255.7 C-LST: 10.255.255.3 
 * >      RD: 10.255.255.3:1 ip-prefix 10.255.254.4/32
                                 10.255.255.3          -       100     0       i
 * >Ec    RD: 10.255.255.9:1 ip-prefix 10.255.254.5/32
                                 10.255.255.9          -       100     0       i
 *  ec    RD: 10.255.255.9:1 ip-prefix 10.255.254.5/32
                                 10.255.255.9          -       100     0       i Or-ID: 10.255.255.9 C-LST: 10.255.255.3 
 * >      RD: 10.255.255.3:1 ip-prefix 10.255.254.6/32
                                 10.255.255.3          -       100     0       i
 * >      RD: 10.255.255.3:1 ip-prefix 172.16.255.0/31
                                 10.255.255.3          -       100     0       i
 * >      RD: 10.255.255.3:1 ip-prefix 192.168.0.0/24
                                 10.255.255.3          -       100     0       i
 * >      RD: 10.255.255.3:1 ip-prefix 192.168.1.0/24
                                 10.255.255.3          -       100     0       i
 * >Ec    RD: 10.255.255.7:1 ip-prefix 192.168.3.0/24
                                 10.255.255.7          -       100     0       i
 *  ec    RD: 10.255.255.7:1 ip-prefix 192.168.3.0/24
                                 10.255.255.7          -       100     0       i Or-ID: 10.255.255.7 C-LST: 10.255.255.3 
 * >Ec    RD: 10.255.255.9:1 ip-prefix 192.168.4.0/24
                                 10.255.255.9          -       100     0       i
 *  ec    RD: 10.255.255.9:1 ip-prefix 192.168.4.0/24
                                 10.255.255.9          -       100     0       i Or-ID: 10.255.255.9 C-LST: 10.255.255.3 
 * >      RD: 10.255.255.3:1 ip-prefix 192.168.5.0/24
                                 10.255.255.3          -       100     0       i
```

## show ip security connection detail

```text
path1:
  Source address: 172.16.2.0, Destination address: 172.16.2.2
  State: established
  Uptime: 40 minutes, 6 seconds
  VRF: default
  Type: static
  Remote IP: 10.255.255.7
  Role: responder
  Inbound SPI: 0xc0fc49:
    Request ID: 1, Mode: transport, Replay window size: 16384, Seq: 0x0
    Errors:
      Packets outside replay window: 0, Replay: 0, Integrity failed: 0
    Lifetime config:
      Soft byte limit: 4462953910499, Hard byte limit: 6442450944000
      Soft packet limit: 2470678271, Hard packet limit: 4000000000
      Soft time limit: 2621 secs, Hard time limit: 3600 secs
    Lifetime current:
      Current bytes: 2580572
      Current packets: 7975
      SA add time: Tue Mar 12 13:06:50 2024
      SA last use time: Tue Mar 12 13:47:30 2024
  Outbound SPI: 0xc68d82:
    Request ID: 1, Mode: transport, Replay window size: 0, Seq: 0x0
    Errors:
      Packets outside replay window: 0, Replay: 0, Integrity failed: 0
    Lifetime config:
      Soft byte limit: 4389025577249, Hard byte limit: 6442450944000
      Soft packet limit: 2608495228, Hard packet limit: 4000000000
      Soft time limit: 2869 secs, Hard time limit: 3600 secs
    Lifetime current:
      Current bytes: 4129866
      Current packets: 16368
      SA add time: Tue Mar 12 13:06:50 2024
      SA last use time: Tue Mar 12 13:47:30 2024
path2:
  Source address: 172.16.3.1, Destination address: 172.16.2.2
  State: idle
  Uptime: N/A
  VRF: default
  Type: static
  Remote IP: 10.255.255.7
  Role: responder
path3:
  Source address: 172.16.2.0, Destination address: 172.16.2.7
  State: established
  Uptime: 38 minutes, 56 seconds
  VRF: default
  Type: static
  Remote IP: 10.255.255.7
  Role: responder
  Inbound SPI: 0xc30fb9:
    Request ID: 3, Mode: transport, Replay window size: 16384, Seq: 0x0
    Errors:
      Packets outside replay window: 0, Replay: 0, Integrity failed: 0
    Lifetime config:
      Soft byte limit: 3954377267999, Hard byte limit: 6442450944000
      Soft packet limit: 2363418942, Hard packet limit: 4000000000
      Soft time limit: 2999 secs, Hard time limit: 3600 secs
    Lifetime current:
      Current bytes: 1066408
      Current packets: 7570
      SA add time: Tue Mar 12 13:08:00 2024
      SA last use time: Tue Mar 12 13:47:30 2024
  Outbound SPI: 0xcb7806:
    Request ID: 3, Mode: transport, Replay window size: 0, Seq: 0x0
    Errors:
      Packets outside replay window: 0, Replay: 0, Integrity failed: 0
    Lifetime config:
      Soft byte limit: 4763363741249, Hard byte limit: 6442450944000
      Soft packet limit: 2125856251, Hard packet limit: 4000000000
      Soft time limit: 2755 secs, Hard time limit: 3600 secs
    Lifetime current:
      Current bytes: 1913796
      Current packets: 15818
      SA add time: Tue Mar 12 13:08:00 2024
      SA last use time: Tue Mar 12 13:47:30 2024
path4:
  Source address: 172.16.3.1, Destination address: 172.16.2.7
  State: idle
  Uptime: N/A
  VRF: default
  Type: static
  Remote IP: 10.255.255.7
  Role: responder
path5:
  Source address: 172.16.2.0, Destination address: 172.16.2.5
  State: established
  Uptime: 3 minutes
  VRF: default
  Type: static
  Remote IP: 10.255.255.7
  Role: responder
  Inbound SPI: 0xc3d595:
    Request ID: 5, Mode: transport, Replay window size: 16384, Seq: 0x0
    Errors:
      Packets outside replay window: 0, Replay: 0, Integrity failed: 0
    Lifetime config:
      Soft byte limit: 3832852271999, Hard byte limit: 6442450944000
      Soft packet limit: 2719927110, Hard packet limit: 4000000000
      Soft time limit: 2760 secs, Hard time limit: 3600 secs
    Lifetime current:
      Current bytes: 258260
      Current packets: 621
      SA add time: Tue Mar 12 13:43:57 2024
      SA last use time: Tue Mar 12 13:47:30 2024
  Outbound SPI: 0xc167f3:
    Request ID: 5, Mode: transport, Replay window size: 0, Seq: 0x0
    Errors:
      Packets outside replay window: 0, Replay: 0, Integrity failed: 0
    Lifetime config:
      Soft byte limit: 4633810826999, Hard byte limit: 6442450944000
      Soft packet limit: 2534187481, Hard packet limit: 4000000000
      Soft time limit: 2864 secs, Hard time limit: 3600 secs
    Lifetime current:
      Current bytes: 442794
      Current packets: 1288
      SA add time: Tue Mar 12 13:43:57 2024
      SA last use time: Tue Mar 12 13:47:30 2024
```

## show stun client translations detail

```text
Current System Time: Tue Mar 12 13:46:57 2024
Transaction ID 000000010affff0200000000
Agent Name: dps
Source Address: 172.16.2.0:4500
Public Address: 172.16.2.0:4500
Number of Attributes: 3
Timeout Interval: 0:03:00
Last Refreshed: 0:00:07 ago
Attribute Type   Length Value           
---------------- ------ ----------------
PATH_GROUP            3 ATT             
VTEP_IP               4 10.255.255.2    
WAN_ID                4 1               

```

## show stun server bindings detail

```text
Current System Time: Tue Mar 12 13:46:58 2024
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
Timeout: 0:00:26
Attribute Type   Length Value           
---------------- ------ ----------------
PATH_GROUP            3 ATT             
VTEP_IP               4 10.255.255.9    
WAN_ID                4 2               

```

## show path-selection paths detail

```text
Peer: 10.255.255.3, Path group ATT
Path name: path5, static, Label: 5
Source: 172.16.2.0, Port: 4500, WAN ID: 1
Destination: 172.16.2.5, Port: 4500, WAN ID: 2886730245
Local interface: Ethernet1/1
Route state: IPsec established
Traffic class 0: active (0:03:00)
MTU: 8914

Peer: 10.255.255.7, Path group ATT
Path name: path1, dynamic, Label: 1
Source: 172.16.2.0, Port: 4500, WAN ID: 1
Destination: 172.16.2.2, Port: 4500, WAN ID: 1
Local interface: Ethernet1/1
Route state: IPsec established
Traffic class 0: active (0:40:05)
MTU: 8914

Peer: 10.255.255.9, Path group ATT
Path name: path3, dynamic, Label: 3
Source: 172.16.2.0, Port: 4500, WAN ID: 1
Destination: 172.16.2.7, Port: 4500, WAN ID: 2
Local interface: Ethernet1/1
Route state: IPsec established
Traffic class 0: active (0:38:56)
MTU: 1414

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
  Connect timer is active, time left: 00:00:31
  Connection interval is 148 seconds
  Failed connection attempts is 22
  Idle-restart timer is inactive
  BGP state is Active
  Number of transitions to established: 0
  Last state was Connect
  Last event was TransportError
  Last sent socket-error:Connect (Network is unreachable), Last time 00:02:15, First time 00:43:06, Repeats 21
  Types of communities advertised: extended
  Neighbor is a route reflector client
  Neighbor is using global cluster ID 10.255.255.2
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
Local AS is 65000, local router ID 10.255.255.2
TTL is 255
Local TCP address is 10.255.255.2
Remote TCP address is 10.255.255.1, remote port is 179
BFD is enabled with configured transmit interval 1000ms, receive interval 1000ms, multiplier 3 and state is Down

BGP neighbor is 10.255.255.3, remote AS 65000, internal link
  BGP version 4, remote router ID 10.255.255.3, VRF default
  Inherits configuration from and member of peer-group autovpnEdges
  Last read 00:00:22, last write 00:00:29
  Hold time is 180, keepalive interval is 60 seconds
  Configured hold time is 180, keepalive interval is 60 seconds
  Effective minimum hold time is 3 seconds
  Send failure hold time is 0 seconds
  Hold timer is active, time left: 00:02:38
  Keepalive timer is active, time left: 00:00:25
  Connect timer is inactive
  Idle-restart timer is inactive
  BGP state is Established, up for 00:02:59
  Number of transitions to established: 1
  Last state was OpenConfirm
  Last event was RecvUpdate
  Last sent socket-error:Connect (Network is unreachable), Last time 00:10:18, First time 00:43:06, Repeats 18
  Types of communities advertised: extended
  Enhanced route refresh stale path removal disabled
  Outbound enhanced route refresh enabled
  Neighbor is a route reflector client
  Neighbor is using global cluster ID 10.255.255.2
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
      Received 00:02:58
      Number of stale paths removed after graceful restart: 0
      Number of paths received before End-of-RIB: 4
    L2VPN EVPN End-of-RIB received: Yes
      Received 00:02:58
      Number of stale paths removed after graceful restart: 0
      Number of paths received before End-of-RIB: 22
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
    Updates:                         8        11
    Keepalives:                      5         5
    Enhanced Route Refresh:          0         0
    Begin of Route Refresh:          0         0
    End of Route Refresh:            0         0
    Total messages:                 14        17
  Prefix Statistics:
                                   Sent      Rcvd     Best Paths     Best ECMP Paths
    IPv4 Unicast:                     0         0              0                   0
    IPv4 Dps:                         4         4              4                   0
    IPv6 Unicast:                     0         0              0                   0
    EVPN:                             7        22             22                   0
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
  Additional-paths send mode:
    Dps: any
Local AS is 65000, local router ID 10.255.255.2
TTL is 255
Local TCP address is 10.255.255.2, local port is 179
Remote TCP address is 10.255.255.3, remote port is 39879
Local next hop for next hop self:
  Dps: 10.255.255.2
  L2VPN EVPN: 10.255.255.2
BFD is enabled with configured transmit interval 1000ms, receive interval 1000ms, multiplier 3 and state is Up
TCP Socket Information:
  TCP state is ESTABLISHED
  Recv-Q: 0/32768
  Send-Q: 0/46080
  Outgoing Maximum Segment Size (MSS): 1448
  Total Number of TCP retransmissions: 1
  Options:
    Timestamps enabled: yes
    Selective Acknowledgments enabled: yes
    Window Scale enabled: yes
    Explicit Congestion Notification (ECN) enabled: no
  Socket Statistics:
    Window Scale (wscale): 7,7
    Retransmission Timeout (rto): 216.0ms
    Round-trip Time (rtt/rtvar): 13.3ms/16.7ms
    Delayed Ack Timeout (ato): 40.0ms
    Congestion Window (cwnd): 10
    TCP Throughput: 8.73 Mbps
    Advertised Recv Window (rcv_space): 14600

BGP neighbor is 10.255.255.4, remote AS 65000, internal link
  BGP version 4, remote router ID 0.0.0.0, VRF default
  Inherits configuration from and member of peer-group autovpnEdges
  Last read never, last write never
  Hold time is 0, keepalive interval is 0 seconds
  Configured hold time is 180, keepalive interval is 60 seconds
  Effective minimum hold time is 3 seconds
  Send failure hold time is 0 seconds
  Hold timer is inactive
  Keepalive timer is inactive
  Connect timer is active, time left: 00:00:19
  Connection interval is 148 seconds
  Failed connection attempts is 22
  Idle-restart timer is inactive
  BGP state is Active
  Number of transitions to established: 0
  Last state was Connect
  Last event was TransportError
  Last sent socket-error:Connect (Network is unreachable), Last time 00:02:28, First time 00:43:06, Repeats 21
  Types of communities advertised: extended
  Neighbor is a route reflector client
  Neighbor is using global cluster ID 10.255.255.2
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
Local AS is 65000, local router ID 10.255.255.2
TTL is 255
Local TCP address is 10.255.255.2
Remote TCP address is 10.255.255.4, remote port is 179
BFD is enabled with configured transmit interval 1000ms, receive interval 1000ms, multiplier 3 and state is Down

BGP neighbor is 10.255.255.7, remote AS 65000, internal link
  BGP version 4, remote router ID 10.255.255.7, VRF default
  Inherits configuration from and member of peer-group autovpnEdges
  Last read 00:00:35, last write 00:00:32
  Hold time is 180, keepalive interval is 60 seconds
  Configured hold time is 180, keepalive interval is 60 seconds
  Effective minimum hold time is 3 seconds
  Send failure hold time is 0 seconds
  Hold timer is active, time left: 00:02:25
  Keepalive timer is active, time left: 00:00:16
  Connect timer is inactive
  Idle-restart timer is inactive
  BGP state is Established, up for 00:40:05
  Number of transitions to established: 1
  Last state was OpenConfirm
  Last event was RecvUpdate
  Types of communities advertised: extended
  Enhanced route refresh stale path removal disabled
  Outbound enhanced route refresh enabled
  Neighbor is a route reflector client
  Neighbor is using global cluster ID 10.255.255.2
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
      Received 00:40:04
      Number of stale paths removed after graceful restart: 0
      Number of paths received before End-of-RIB: 2
    L2VPN EVPN End-of-RIB received: Yes
      Received 00:40:04
      Number of stale paths removed after graceful restart: 0
      Number of paths received before End-of-RIB: 3
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
    Updates:                        12         5
    Keepalives:                     48        47
    Enhanced Route Refresh:          0         0
    Begin of Route Refresh:          0         0
    End of Route Refresh:            0         0
    Total messages:                 61        53
  Prefix Statistics:
                                   Sent      Rcvd     Best Paths     Best ECMP Paths
    IPv4 Unicast:                     0         0              0                   0
    IPv4 Dps:                         6         2              2                   2
    IPv6 Unicast:                     0         0              0                   0
    EVPN:                            19         3              3                   3
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
  Additional-paths send mode:
    Dps: any
Local AS is 65000, local router ID 10.255.255.2
TTL is 255
Local TCP address is 10.255.255.2, local port is 179
Remote TCP address is 10.255.255.7, remote port is 34603
Local next hop for next hop self:
  Dps: 10.255.255.2
  L2VPN EVPN: 10.255.255.2
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
    Round-trip Time (rtt/rtvar): 4.8ms/1.0ms
    Delayed Ack Timeout (ato): 40.0ms
    Congestion Window (cwnd): 4
    TCP Throughput: 8.65 Mbps
    Recv Round-trip Time (rcv_rtt): 5.0ms
    Advertised Recv Window (rcv_space): 14600

BGP neighbor is 10.255.255.9, remote AS 65000, internal link
  BGP version 4, remote router ID 10.255.255.9, VRF default
  Inherits configuration from and member of peer-group autovpnEdges
  Last read 00:00:28, last write 00:00:29
  Hold time is 180, keepalive interval is 60 seconds
  Configured hold time is 180, keepalive interval is 60 seconds
  Effective minimum hold time is 3 seconds
  Send failure hold time is 0 seconds
  Hold timer is active, time left: 00:02:32
  Keepalive timer is active, time left: 00:00:30
  Connect timer is inactive
  Idle-restart timer is inactive
  BGP state is Established, up for 00:38:55
  Number of transitions to established: 1
  Last state was OpenConfirm
  Last event was RecvUpdate
  Types of communities advertised: extended
  Enhanced route refresh stale path removal disabled
  Outbound enhanced route refresh enabled
  Neighbor is a route reflector client
  Neighbor is using global cluster ID 10.255.255.2
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
      Received 00:38:54
      Number of stale paths removed after graceful restart: 0
      Number of paths received before End-of-RIB: 2
    L2VPN EVPN End-of-RIB received: Yes
      Received 00:38:54
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
    Updates:                        12         5
    Keepalives:                     48        47
    Enhanced Route Refresh:          0         0
    Begin of Route Refresh:          0         0
    End of Route Refresh:            0         0
    Total messages:                 61        53
  Prefix Statistics:
                                   Sent      Rcvd     Best Paths     Best ECMP Paths
    IPv4 Unicast:                     0         0              0                   0
    IPv4 Dps:                         6         2              2                   2
    IPv6 Unicast:                     0         0              0                   0
    EVPN:                            18         4              4                   4
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
  Additional-paths send mode:
    Dps: any
Local AS is 65000, local router ID 10.255.255.2
TTL is 255
Local TCP address is 10.255.255.2, local port is 179
Remote TCP address is 10.255.255.9, remote port is 33065
Local next hop for next hop self:
  Dps: 10.255.255.2
  L2VPN EVPN: 10.255.255.2
BFD is enabled with configured transmit interval 1000ms, receive interval 1000ms, multiplier 3 and state is Up
TCP Socket Information:
  TCP state is ESTABLISHED
  Recv-Q: 0/32768
  Send-Q: 0/46080
  Outgoing Maximum Segment Size (MSS): 1362
  Total Number of TCP retransmissions: 0
  Options:
    Timestamps enabled: yes
    Selective Acknowledgments enabled: yes
    Window Scale enabled: yes
    Explicit Congestion Notification (ECN) enabled: no
  Socket Statistics:
    Window Scale (wscale): 7,7
    Retransmission Timeout (rto): 208.0ms
    Round-trip Time (rtt/rtvar): 4.0ms/1.3ms
    Delayed Ack Timeout (ato): 40.0ms
    Congestion Window (cwnd): 10
    TCP Throughput: 27.17 Mbps
    Advertised Recv Window (rcv_space): 14600

```

## show bgp path-selection detail

```text
BGP routing table information for VRF default
Router identifier 10.255.255.2, local AS number 65000
Bgp routing table entry for ipv4Dps VTEP 10.255.255.7/32
 Paths: 2 available
  Local (Received from a RR-client)
    :: from 10.255.255.7 (10.255.255.7)
      Origin IGP, metric -, localpref 100, weight 0, received 00:40:06 ago, valid, internal
      Tunnel encapsulation attribute: Dynamic path selection
        Endpoint: 172.16.2.2, Path group name: ATT, WAN ID: 1, UDP port: 4500
  Local (Received from a RR-client)
    :: from 10.255.255.3 (10.255.255.3)
      Origin IGP, metric -, localpref 100, weight 0, received 00:02:59 ago, valid, internal
      Tunnel encapsulation attribute: Dynamic path selection
        Endpoint: 172.16.2.2, Path group name: ATT, WAN ID: 1, UDP port: 4500
Bgp routing table entry for ipv4Dps VTEP 10.255.255.9/32
 Paths: 2 available
  Local (Received from a RR-client)
    :: from 10.255.255.9 (10.255.255.9)
      Origin IGP, metric -, localpref 100, weight 0, received 00:38:55 ago, valid, internal
      Tunnel encapsulation attribute: Dynamic path selection
        Endpoint: 172.16.2.7, Path group name: ATT, WAN ID: 2, UDP port: 4500
  Local (Received from a RR-client)
    :: from 10.255.255.3 (10.255.255.3)
      Origin IGP, metric -, localpref 100, weight 0, received 00:02:59 ago, valid, internal
      Tunnel encapsulation attribute: Dynamic path selection
        Endpoint: 172.16.2.7, Path group name: ATT, WAN ID: 2, UDP port: 4500
Bgp routing table entry for ipv4Ipsec VTEP 10.255.255.7/32
 Paths: 2 available
  Local (Received from a RR-client)
    :: from 10.255.255.7 (10.255.255.7)
      Origin IGP, metric -, localpref 100, weight 0, received 00:40:06 ago, valid, internal
      Tunnel encapsulation attribute: IP security
        Initial contact: false, Rekey counter: 0, Nonce length: 32
        DH group: 14, DH key length: 256
        Encryption algo: aes256, Authentication algo: sha256
  Local (Received from a RR-client)
    :: from 10.255.255.3 (10.255.255.3)
      Origin IGP, metric -, localpref 100, weight 0, received 00:02:59 ago, valid, internal
      Tunnel encapsulation attribute: IP security
        Initial contact: false, Rekey counter: 0, Nonce length: 32
        DH group: 14, DH key length: 256
        Encryption algo: aes256, Authentication algo: sha256
Bgp routing table entry for ipv4Ipsec VTEP 10.255.255.9/32
 Paths: 2 available
  Local (Received from a RR-client)
    :: from 10.255.255.9 (10.255.255.9)
      Origin IGP, metric -, localpref 100, weight 0, received 00:38:55 ago, valid, internal
      Tunnel encapsulation attribute: IP security
        Initial contact: false, Rekey counter: 0, Nonce length: 32
        DH group: 14, DH key length: 256
        Encryption algo: aes256, Authentication algo: sha256
  Local (Received from a RR-client)
    :: from 10.255.255.3 (10.255.255.3)
      Origin IGP, metric -, localpref 100, weight 0, received 00:02:59 ago, valid, internal
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
>C    10.255.255.2/32 [0 pref/0 metric] updated 00:50:21 ago
         via Loopback0, directly connected
>C    172.16.2.0/31 [0 pref/0 metric] updated 00:54:32 ago
         via Ethernet1/1, directly connected
>C    172.16.3.0/31 [0 pref/0 metric] updated 00:54:17 ago
         via Ethernet1/2, directly connected
>C    172.28.128.0/20 [0 pref/0 metric] updated 01:50:51 ago
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
>S    10.80.0.0/12 [1 pref/0 metric] updated 01:50:51 ago
         via 172.28.128.1 [0 pref/0 metric] type ipv4
            via 172.28.128.1, Management1/1
>S    10.239.0.0/16 [1 pref/0 metric] updated 01:50:51 ago
         via 172.28.128.1 [0 pref/0 metric] type ipv4
            via 172.28.128.1, Management1/1
>S    10.240.0.0/13 [1 pref/0 metric] updated 01:50:51 ago
         via 172.28.128.1 [0 pref/0 metric] type ipv4
            via 172.28.128.1, Management1/1
>S    172.16.0.0/12 [1 pref/0 metric] updated 01:50:51 ago
         via 172.28.128.1 [0 pref/0 metric] type ipv4
            via 172.28.128.1, Management1/1
>S    172.16.2.0/24 [1 pref/0 metric] updated 00:41:20 ago
         via 172.16.2.1 [0 pref/0 metric] type ipv4
            via 172.16.2.1, Ethernet1/1
>S    172.16.3.0/24 [1 pref/0 metric] updated 00:53:36 ago
         via 172.16.3.0 [0 pref/0 metric] type ipv4
            via 172.16.3.0, Ethernet1/2
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
>P    0.0.0.0/8 [1 pref/0 metric] updated 01:51:09 ago
         via Null0, directly connected [NF]
>P    10.255.255.3/32 [1 pref/0 metric] updated 00:08:17 ago
         via 10.255.255.3, Dps1
>P    10.255.255.7/32 [1 pref/0 metric] updated 00:40:20 ago
         via 10.255.255.7, Dps1
>P    10.255.255.9/32 [1 pref/0 metric] updated 00:39:16 ago
         via 10.255.255.9, Dps1
>P    127.0.0.0/8 [1 pref/0 metric] updated 01:51:09 ago
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
>P    ::/96 [1 pref/0 metric] updated 00:43:11 ago
         via Null0, directly connected [NF]
>P    ::ffff:127.0.0.0/104 [1 pref/0 metric] updated 00:43:11 ago
         via :: [1 pref/1 metric] type ipv6
            via , directly connected
>P    fe80::/10 [1 pref/0 metric] updated 00:43:11 ago
```

## 

```text
```

