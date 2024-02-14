# Test results for L2

## show version

```text
Arista DCS-7280SR3K-48YC8-F
Hardware version: 11.02
Serial number: JPE21043549
Hardware MAC address: 948e.d351.e000
System MAC address: 948e.d351.e000

Software image version: 4.31.1F
Architecture: x86_64
Internal build version: 4.31.1F-34556000.4311F
Internal build ID: 48c47833-3f4a-4a14-9783-0017c2f42e54
Image format version: 3.0
Image optimization: Default

Uptime: 6 minutes
Total memory: 65734516 kB
Free memory: 61620464 kB

```

## show mac address-table

```text
          Mac Address Table
------------------------------------------------------------------

Vlan    Mac Address       Type        Ports      Moves   Last Move
----    -----------       ----        -----      -----   ---------
  10    001c.7300.0001    STATIC      Router
  10    948e.d351.7c10    STATIC      Po2000
  10    948e.d351.e000    STATIC      Router
  20    001c.7300.0001    STATIC      Router
  20    948e.d351.7c10    STATIC      Po2000
  20    948e.d351.e000    STATIC      Router
  30    001c.7300.0001    STATIC      Router
  30    948e.d351.7c10    STATIC      Po2000
  30    948e.d351.e000    STATIC      Router
  40    001c.7300.0001    STATIC      Router
  40    948e.d351.7c10    STATIC      Po2000
  40    948e.d351.e000    STATIC      Router
4094    001c.7300.0001    STATIC      Router
4094    948e.d351.7c10    STATIC      Po2000
4094    948e.d351.e000    STATIC      Router
Total Mac Addresses for this criterion: 15

          Multicast Mac Address Table
------------------------------------------------------------------

Vlan    Mac Address       Type        Ports
----    -----------       ----        -----
Total Mac Addresses for this criterion: 0
```

## show ip interface brief | exclude una

```text
                                                                        Address
Interface       IP Address            Status     Protocol         MTU   Owner  
--------------- --------------------- ---------- ------------ --------- -------
Ethernet1       10.1.1.11/31          up         up              9214          
Ethernet2       10.2.2.11/31          up         up              9214          
Loopback0       10.255.3.2/32         up         up             65535          
Loopback2100    223.255.255.255/32    up         up             65535          
Management1     100.64.64.114/24      up         up              1500          
Vlan10          10.10.12.3/24         up         up              9000          
Vlan20          10.20.22.3/24         up         up              9000          
Vlan30          10.30.32.3/24         up         up              9000          
Vlan40          10.40.42.3/24         up         up              9000          
Vlan4094        1.1.1.2/30            up         up              1500          

```

## show interfaces counters rates | nz

```text
Port      Name               Intvl  In Mbps      %  In Kpps Out Mbps      %

Port      Out Kpps
```

## show isis neighbors

```text
```

## show isis database detail

```text
```

## show isis flex-algo

```text
```

## show isis segment-routing tunnel

```text
   Index       Endpoint       Next Hop/Tunnel Index       Interface    Labels
----------- -------------- --------------------------- --------------- ------

```

## show isis segment-routing prefix-segments

```text
```

## show ip route

```text

VRF: default
Codes: C - connected, S - static, K - kernel, 
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

 C        1.1.1.0/30 is directly connected, Vlan4094
 C        10.1.1.10/31 is directly connected, Ethernet1
 C        10.2.2.10/31 is directly connected, Ethernet2
 B E      10.10.10.0/24 [200/0] via 10.1.1.10, Ethernet1
                                via 10.2.2.10, Ethernet2
 B E      10.10.11.0/24 [200/0] via 10.1.1.10, Ethernet1
                                via 10.2.2.10, Ethernet2
 C        10.10.12.0/24 is directly connected, Vlan10
 B E      10.10.13.0/24 [200/0] via 10.1.1.10, Ethernet1
                                via 10.2.2.10, Ethernet2
 B E      10.20.20.0/24 [200/0] via 10.1.1.10, Ethernet1
                                via 10.2.2.10, Ethernet2
 B E      10.20.21.0/24 [200/0] via 10.1.1.10, Ethernet1
                                via 10.2.2.10, Ethernet2
 C        10.20.22.0/24 is directly connected, Vlan20
 B E      10.20.23.0/24 [200/0] via 10.1.1.10, Ethernet1
                                via 10.2.2.10, Ethernet2
 B E      10.30.30.0/24 [200/0] via 10.1.1.10, Ethernet1
                                via 10.2.2.10, Ethernet2
 B E      10.30.31.0/24 [200/0] via 10.1.1.10, Ethernet1
                                via 10.2.2.10, Ethernet2
 C        10.30.32.0/24 is directly connected, Vlan30
 B E      10.30.33.0/24 [200/0] via 10.1.1.10, Ethernet1
                                via 10.2.2.10, Ethernet2
 B E      10.40.40.0/24 [200/0] via 10.1.1.10, Ethernet1
                                via 10.2.2.10, Ethernet2
 B E      10.40.41.0/24 [200/0] via 10.1.1.10, Ethernet1
                                via 10.2.2.10, Ethernet2
 C        10.40.42.0/24 is directly connected, Vlan40
 B E      10.40.43.0/24 [200/0] via 10.1.1.10, Ethernet1
                                via 10.2.2.10, Ethernet2
 B E      10.255.1.1/32 [200/0] via 10.1.1.10, Ethernet1
                                via 10.2.2.10, Ethernet2
 B E      10.255.1.2/32 [200/0] via 10.1.1.10, Ethernet1
                                via 10.2.2.10, Ethernet2
 B E      10.255.2.1/32 [200/0] via 10.1.1.10, Ethernet1
                                via 10.2.2.10, Ethernet2
 B E      10.255.2.2/32 [200/0] via 10.1.1.10, Ethernet1
                                via 10.2.2.10, Ethernet2
 B I      10.255.3.1/32 [200/0] via 1.1.1.1, Vlan4094
 C        10.255.3.2/32 is directly connected, Loopback0
 B E      10.255.4.1/32 [200/0] via 10.1.1.10, Ethernet1
                                via 10.2.2.10, Ethernet2
 B E      10.255.4.2/32 [200/0] via 10.1.1.10, Ethernet1
                                via 10.2.2.10, Ethernet2
 B E      10.255.255.1/32 [200/0] via 10.1.1.10, Ethernet1
 B E      10.255.255.2/32 [200/0] via 10.2.2.10, Ethernet2
 C        223.255.255.255/32 is directly connected, Loopback2100

```

## show ipv6 route

```text

VRF: default
Displaying 0 of 3 IPv6 routing table entries
Codes: C - connected, S - static, K - kernel, O3 - OSPFv3,
       B - Other BGP Routes, A B - BGP Aggregate, R - RIP,
       I L1 - IS-IS level 1, I L2 - IS-IS level 2, DH - DHCP,
       NG - Nexthop Group Static Route, M - Martian,
       DP - Dynamic Policy Route, L - VRF Leaked,
       G  - gRIBI, RC - Route Cache Route,
       CL - CBF Leaked Route


! IPv6 routing not enabled
```

## show mpls route

```text
! Mpls routing is not enabled
MPLS forwarding table (Label [metric] Vias) - 0 routes 
MPLS next-hop resolution allow default route: False
Metric Codes:
          A - Active metric
Via Type Codes:
          M - MPLS via, P - Pseudowire via,
          I - IP lookup via, V - VLAN via,
          VA - EVPN VLAN aware via, ES - EVPN ethernet segment via,
          VF - EVPN VLAN flood via, AF - EVPN VLAN aware flood via,
          NG - Nexthop group via

```

## show mpls lfib route

```text
! Mpls routing is not enabled
MPLS forwarding table (Label [metric] Vias) - 0 routes 
MPLS next-hop resolution allow default route: False
Via Type Codes:
          M - MPLS via, P - Pseudowire via,
          I - IP lookup via, V - VLAN via,
          VA - EVPN VLAN aware via, ES - EVPN ethernet segment via,
          VF - EVPN VLAN flood via, AF - EVPN VLAN aware flood via,
          NG - Nexthop group via
Source Codes:
          G - gRIBI, S - Static MPLS route,
          B2 - BGP L2 EVPN, B3 - BGP L3 VPN,
          R - RSVP, LP - LDP pseudowire,
          L - LDP, M - MLDP,
          I>BL - IS-IS SR to BGP LU, IP - IS-IS SR prefix segment,
          IA - IS-IS SR adjacency segment, I>L - IS-IS SR to LDP,
          L>I - LDP to IS-IS SR, OP - Ospf SR prefix segment,
          OA - Ospf SR adjacency segment, OL - Ospf SR segment to LDP,
          L0 - LDP to Ospf SR segment, BL - BGP LU,
          BL>L - BGP LU to LDP, L>BL - LDP to BGP LU,
          ST - SR TE policy, SMP - SR P2MP,
          BL>I - BGP LU to IS-IS SR, DE - Debug LFIB

```

## show bgp evpn

```text
BGP routing table information for VRF default
Router identifier 10.255.3.2, local AS number 65301
Route status codes: * - valid, > - active, S - Stale, E - ECMP head, e - ECMP
                    c - Contributing to ECMP, % - Pending best path selection
Origin codes: i - IGP, e - EGP, ? - incomplete
AS Path Attributes: Or-ID - Originator ID, C-LST - Cluster List, LL Nexthop - Link Local Nexthop

          Network                Next Hop              Metric  LocPref Weight  Path
```

## show bgp vpn-ipv4

```text
BGP routing table information for VRF default
Router identifier 10.255.3.2, local AS number 65301
Route status codes: s - suppressed contributor, * - valid, > - active, E - ECMP head, e - ECMP
                    S - Stale, c - Contributing to ECMP, b - backup, L - labeled-unicast
                    % - Pending best path selection
Origin codes: i - IGP, e - EGP, ? - incomplete
AS Path Attributes: Or-ID - Originator ID, C-LST - Cluster List, LL Nexthop - Link Local Nexthop

          Network                Next Hop              Metric  LocPref Weight  Path
```

## show bgp vpn-ipv6

```text
BGP routing table information for VRF default
Router identifier 10.255.3.2, local AS number 65301
Route status codes: s - suppressed contributor, * - valid, > - active, E - ECMP head, e - ECMP
                    S - Stale, c - Contributing to ECMP, b - backup, L - labeled-unicast
                    % - Pending best path selection
Origin codes: i - IGP, e - EGP, ? - incomplete
AS Path Attributes: Or-ID - Originator ID, C-LST - Cluster List, LL Nexthop - Link Local Nexthop

          Network                Next Hop              Metric  LocPref Weight  Path
```

## show bgp ipv4 labeled-unicast

```text
BGP routing table information for VRF default
Router identifier 10.255.3.2, local AS number 65301
Route status codes: s - suppressed contributor, * - valid, > - active, E - ECMP head, e - ECMP
                    S - Stale, c - Contributing to ECMP, b - backup, L - labeled-unicast
                    % - Pending best path selection
Origin codes: i - IGP, e - EGP, ? - incomplete
AS Path Attributes: Or-ID - Originator ID, C-LST - Cluster List, LL Nexthop - Link Local Nexthop

          Network                Next Hop              Metric  AIGP       LocPref Weight  Path
```

## show bgp neighbors

```text
BGP neighbor is 1.1.1.1, remote AS 65301, internal link
  BGP version 4, remote router ID 10.255.3.1, VRF default
  Inherits configuration from and member of peer-group MLAG-PEER
  Last read 00:00:24, last write 00:00:24
  Hold time is 180, keepalive interval is 60 seconds
  Configured hold time is 180, keepalive interval is 60 seconds
  Effective minimum hold time is 3 seconds
  Hold timer is active, time left: 00:02:36
  Keepalive timer is active, time left: 00:00:21
  Connect timer is inactive
  Idle-restart timer is inactive
  BGP state is Established, up for 00:02:29
  Number of transitions to established: 1
  Last state was OpenConfirm
  Last event was Established
  Last sent socket-error:Connect (Network is unreachable), Last time 00:02:35, First time 00:04:20, Repeats 6
  Types of communities advertised: standard extended
  Enhanced route refresh stale path removal disabled
  Outbound enhanced route refresh enabled
  Neighbor Capabilities:
    Multiprotocol IPv4 Unicast: advertised and received and negotiated
    Four Octet ASN: advertised and received and negotiated
    Route Refresh: advertised and received and negotiated
    Enhanced route refresh: advertised and received and negotiated
    Send End-of-RIB messages: advertised and received and negotiated
    Additional-paths recv capability:
      IPv4 Unicast: advertised
    Additional-paths send capability:
      IPv4 Unicast: received
  Restart timer is inactive
  End of rib timer is inactive
    IPv4 Unicast End-of-RIB received: Yes
      Received 00:02:16
      Number of stale paths removed after graceful restart: 0
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
    Updates:                        12         9
    Keepalives:                      4         4
    Enhanced Route Refresh:          0         0
    Begin of Route Refresh:          0         0
    End of Route Refresh:            0         0
    Total messages:                 17        14
  Prefix Statistics:
                                   Sent      Rcvd     Best Paths     Best ECMP Paths
    IPv4 Unicast:                    25        25              1                   0
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
    IPv4 unicast NLRIs dropped due to maximum route limit violation: 0
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
  Soft reconfiguration inbound is "All"
Local AS is 65301, local router ID 10.255.3.2
TTL is 255
Local TCP address is 1.1.1.2, local port is 179
Remote TCP address is 1.1.1.1, remote port is 38496
Local next hop for next hop self:
  IPv4 Unicast: 1.1.1.2
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
    Round-trip Time (rtt/rtvar): 6.2ms/11.3ms
    Delayed Ack Timeout (ato): 40.0ms
    Congestion Window (cwnd): 10
    TCP Throughput: 18.64 Mbps
    Advertised Recv Window (rcv_space): 14600

BGP neighbor is 10.1.1.10, remote AS 65001, external link
  BGP version 4, remote router ID 10.255.255.1, VRF default
  Inherits configuration from and member of peer-group SPINES
  Last read 00:00:02, last write 00:00:40
  Hold time is 180, keepalive interval is 60 seconds
  Configured hold time is 180, keepalive interval is 60 seconds
  Effective minimum hold time is 3 seconds
  Hold timer is active, time left: 00:02:58
  Keepalive timer is active, time left: 00:00:09
  Connect timer is inactive
  Idle-restart timer is inactive
  BGP state is Established, up for 00:02:16
  Number of transitions to established: 1
  Last state was OpenConfirm
  Last event was Established
  Types of communities advertised: standard extended
  Enhanced route refresh stale path removal disabled
  Outbound enhanced route refresh enabled
  Neighbor Capabilities:
    Multiprotocol IPv4 Unicast: advertised and received and negotiated
    Four Octet ASN: advertised and received and negotiated
    Route Refresh: advertised and received and negotiated
    Enhanced route refresh: advertised and received and negotiated
    Send End-of-RIB messages: advertised and received and negotiated
    Additional-paths recv capability:
      IPv4 Unicast: advertised
    Additional-paths send capability:
      IPv4 Unicast: received
  Restart timer is inactive
  End of rib timer is inactive
    IPv4 Unicast End-of-RIB received: Yes
      Received 00:00:49
      Number of stale paths removed after graceful restart: 0
  AIGP attribute send and receive for IPv4 Unicast are disabled
  AIGP attribute send and receive for IPv4 with MPLS Labels are disabled
  AIGP attribute send and receive for IPv6 Unicast are disabled
  AIGP attribute send and receive for IPv6 with MPLS Labels are disabled
  BGP session driven failover for IPv4 Unicast is disabled
  BGP session driven failover for IPv6 Unicast is disabled
  Message Statistics:
                                  Sent      Rcvd
    Opens:                           1         1
    Notifications:                   0         0
    Updates:                         7         6
    Keepalives:                      4         4
    Enhanced Route Refresh:          0         0
    Begin of Route Refresh:          0         0
    End of Route Refresh:            0         0
    Total messages:                 12        11
  Prefix Statistics:
                                   Sent      Rcvd     Best Paths     Best ECMP Paths
    IPv4 Unicast:                    25        25             19                   0
    IPv6 Unicast:                     0         0              0                   0
  Configured maximum total number of routes is 256000, warning limit is 204800
  Inbound updates dropped by reason:
    AS path loop detection: 1
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
    IPv4 unicast NLRIs dropped due to maximum route limit violation: 0
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
  Soft reconfiguration inbound is "All"
Local AS is 65301, local router ID 10.255.3.2
TTL is 1
Local TCP address is 10.1.1.11, local port is 42257
Remote TCP address is 10.1.1.10, remote port is 179
Local next hop for next hop self:
  IPv4 Unicast: 10.1.1.11
TCP Socket Information:
  TCP state is ESTABLISHED
  Recv-Q: 0/32768
  Send-Q: 0/332800
  Outgoing Maximum Segment Size (MSS): 9162
  Total Number of TCP retransmissions: 0
  Options:
    Timestamps enabled: yes
    Selective Acknowledgments enabled: yes
    Window Scale enabled: yes
    Explicit Congestion Notification (ECN) enabled: no
  Socket Statistics:
    Window Scale (wscale): 7,7
    Retransmission Timeout (rto): 212.0ms
    Round-trip Time (rtt/rtvar): 11.4ms/9.7ms
    Delayed Ack Timeout (ato): 40.0ms
    Congestion Window (cwnd): 10
    TCP Throughput: 64.49 Mbps
    Advertised Recv Window (rcv_space): 56374

BGP neighbor is 10.2.2.10, remote AS 65001, external link
  BGP version 4, remote router ID 10.255.255.2, VRF default
  Inherits configuration from and member of peer-group SPINES
  Last read 00:00:09, last write 00:00:30
  Hold time is 180, keepalive interval is 60 seconds
  Configured hold time is 180, keepalive interval is 60 seconds
  Effective minimum hold time is 3 seconds
  Hold timer is active, time left: 00:02:51
  Keepalive timer is active, time left: 00:00:20
  Connect timer is inactive
  Idle-restart timer is inactive
  BGP state is Established, up for 00:02:21
  Number of transitions to established: 1
  Last state was OpenConfirm
  Last event was Established
  Types of communities advertised: standard extended
  Enhanced route refresh stale path removal disabled
  Outbound enhanced route refresh enabled
  Neighbor Capabilities:
    Multiprotocol IPv4 Unicast: advertised and received and negotiated
    Four Octet ASN: advertised and received and negotiated
    Route Refresh: advertised and received and negotiated
    Enhanced route refresh: advertised and received and negotiated
    Send End-of-RIB messages: advertised and received and negotiated
    Additional-paths recv capability:
      IPv4 Unicast: advertised
    Additional-paths send capability:
      IPv4 Unicast: received
  Restart timer is inactive
  End of rib timer is inactive
    IPv4 Unicast End-of-RIB received: Yes
      Received 00:00:55
      Number of stale paths removed after graceful restart: 0
  AIGP attribute send and receive for IPv4 Unicast are disabled
  AIGP attribute send and receive for IPv4 with MPLS Labels are disabled
  AIGP attribute send and receive for IPv6 Unicast are disabled
  AIGP attribute send and receive for IPv6 with MPLS Labels are disabled
  BGP session driven failover for IPv4 Unicast is disabled
  BGP session driven failover for IPv6 Unicast is disabled
  Message Statistics:
                                  Sent      Rcvd
    Opens:                           1         1
    Notifications:                   0         0
    Updates:                         4         6
    Keepalives:                      4         4
    Enhanced Route Refresh:          0         0
    Begin of Route Refresh:          0         0
    End of Route Refresh:            0         0
    Total messages:                  9        11
  Prefix Statistics:
                                   Sent      Rcvd     Best Paths     Best ECMP Paths
    IPv4 Unicast:                     7        25             19                  18
    IPv6 Unicast:                     0         0              0                   0
  Configured maximum total number of routes is 256000, warning limit is 204800
  Inbound updates dropped by reason:
    AS path loop detection: 1
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
    IPv4 unicast NLRIs dropped due to maximum route limit violation: 0
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
  Soft reconfiguration inbound is "All"
Local AS is 65301, local router ID 10.255.3.2
TTL is 1
Local TCP address is 10.2.2.11, local port is 37063
Remote TCP address is 10.2.2.10, remote port is 179
Local next hop for next hop self:
  IPv4 Unicast: 10.2.2.11
TCP Socket Information:
  TCP state is ESTABLISHED
  Recv-Q: 0/32768
  Send-Q: 0/332800
  Outgoing Maximum Segment Size (MSS): 9162
  Total Number of TCP retransmissions: 0
  Options:
    Timestamps enabled: yes
    Selective Acknowledgments enabled: yes
    Window Scale enabled: yes
    Explicit Congestion Notification (ECN) enabled: no
  Socket Statistics:
    Window Scale (wscale): 7,7
    Retransmission Timeout (rto): 204.0ms
    Round-trip Time (rtt/rtvar): 3.8ms/7.0ms
    Delayed Ack Timeout (ato): 40.0ms
    Congestion Window (cwnd): 10
    TCP Throughput: 194.32 Mbps
    Advertised Recv Window (rcv_space): 56374

```

## show tunnel rib system-tunnel-rib brief

```text
Tunnel RIB: system-tunnel-rib
Endpoint Tunnel Type  Index(es)  Tunnel Preference  IGP Preference  IGP Metric 
-------- ------------ ---------- ------------------ --------------- -----------

Metric Type
-----------

```

## show tunnel rib colored brief

```text
Tunnel RIB: system-colored-tunnel-rib
 Endpoint     Color     Tunnel Type     Index(es)     Tunnel Preference     IGP Preference     IGP Metric   Metric Type
----------- --------- --------------- ------------- --------------------- ------------------ -------------- -----------

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
>C    1.1.1.0/30 [0 pref/0 metric] updated 00:02:32 ago
         via Vlan4094, directly connected
>C    10.1.1.10/31 [0 pref/0 metric] updated 00:02:19 ago
         via Ethernet1, directly connected
>C    10.2.2.10/31 [0 pref/0 metric] updated 00:02:24 ago
         via Ethernet2, directly connected
>C    10.10.12.0/24 [0 pref/0 metric] updated 00:02:30 ago
         via Vlan10, directly connected
>C    10.20.22.0/24 [0 pref/0 metric] updated 00:02:30 ago
         via Vlan20, directly connected
>C    10.30.32.0/24 [0 pref/0 metric] updated 00:02:30 ago
         via Vlan30, directly connected
>C    10.40.42.0/24 [0 pref/0 metric] updated 00:02:30 ago
         via Vlan40, directly connected
>C    10.255.3.2/32 [0 pref/0 metric] updated 00:04:45 ago
         via Loopback0, directly connected
>C    223.255.255.255/32 [0 pref/0 metric] updated 00:04:45 ago
         via Loopback2100, directly connected
VRF: default, Protocol: bgp
Codes: C - Connected, S - Static, P - Route Input, G - Gribi
       B - BGP, O - Ospf, O3 - Ospf3, I - Isis, R - Rip, VL - VRF Leak
       > - Best Route, * - Unresolved Next hop
       EM - Exact match of the SR-TE Policy
       NM - Null endpoint match of the SR-TE Policy
       AM - Any endpoint match of the SR-TE Policy
       L - Part of a recursive route resolution loop
       A - Next hop not resolved in ARP/ND
       NF - Not in FEC
>B    10.10.10.0/24 [200 pref/0 MED] updated 00:02:17 ago
         via 10.2.2.10 [0 pref/0 metric] type ipv4
            via 10.2.2.10, Ethernet2
         via 10.1.1.10 [0 pref/0 metric] type ipv4
            via 10.1.1.10, Ethernet1
>B    10.10.11.0/24 [200 pref/0 MED] updated 00:02:17 ago
         via 10.2.2.10 [0 pref/0 metric] type ipv4
            via 10.2.2.10, Ethernet2
         via 10.1.1.10 [0 pref/0 metric] type ipv4
            via 10.1.1.10, Ethernet1
 B    10.10.12.0/24 [200 pref/0 MED] updated 00:02:31 ago
         via 1.1.1.1 [0 pref/0 metric] type ipv4
            via 1.1.1.1, Vlan4094
>B    10.10.13.0/24 [200 pref/0 MED] updated 00:02:17 ago
         via 10.2.2.10 [0 pref/0 metric] type ipv4
            via 10.2.2.10, Ethernet2
         via 10.1.1.10 [0 pref/0 metric] type ipv4
            via 10.1.1.10, Ethernet1
>B    10.20.20.0/24 [200 pref/0 MED] updated 00:02:17 ago
         via 10.2.2.10 [0 pref/0 metric] type ipv4
            via 10.2.2.10, Ethernet2
         via 10.1.1.10 [0 pref/0 metric] type ipv4
            via 10.1.1.10, Ethernet1
>B    10.20.21.0/24 [200 pref/0 MED] updated 00:02:17 ago
         via 10.2.2.10 [0 pref/0 metric] type ipv4
            via 10.2.2.10, Ethernet2
         via 10.1.1.10 [0 pref/0 metric] type ipv4
            via 10.1.1.10, Ethernet1
 B    10.20.22.0/24 [200 pref/0 MED] updated 00:02:31 ago
         via 1.1.1.1 [0 pref/0 metric] type ipv4
            via 1.1.1.1, Vlan4094
>B    10.20.23.0/24 [200 pref/0 MED] updated 00:02:17 ago
         via 10.2.2.10 [0 pref/0 metric] type ipv4
            via 10.2.2.10, Ethernet2
         via 10.1.1.10 [0 pref/0 metric] type ipv4
            via 10.1.1.10, Ethernet1
>B    10.30.30.0/24 [200 pref/0 MED] updated 00:02:17 ago
         via 10.2.2.10 [0 pref/0 metric] type ipv4
            via 10.2.2.10, Ethernet2
         via 10.1.1.10 [0 pref/0 metric] type ipv4
            via 10.1.1.10, Ethernet1
>B    10.30.31.0/24 [200 pref/0 MED] updated 00:02:17 ago
         via 10.2.2.10 [0 pref/0 metric] type ipv4
            via 10.2.2.10, Ethernet2
         via 10.1.1.10 [0 pref/0 metric] type ipv4
            via 10.1.1.10, Ethernet1
 B    10.30.32.0/24 [200 pref/0 MED] updated 00:02:31 ago
         via 1.1.1.1 [0 pref/0 metric] type ipv4
            via 1.1.1.1, Vlan4094
>B    10.30.33.0/24 [200 pref/0 MED] updated 00:02:17 ago
         via 10.2.2.10 [0 pref/0 metric] type ipv4
            via 10.2.2.10, Ethernet2
         via 10.1.1.10 [0 pref/0 metric] type ipv4
            via 10.1.1.10, Ethernet1
>B    10.40.40.0/24 [200 pref/0 MED] updated 00:02:17 ago
         via 10.2.2.10 [0 pref/0 metric] type ipv4
            via 10.2.2.10, Ethernet2
         via 10.1.1.10 [0 pref/0 metric] type ipv4
            via 10.1.1.10, Ethernet1
>B    10.40.41.0/24 [200 pref/0 MED] updated 00:02:17 ago
         via 10.2.2.10 [0 pref/0 metric] type ipv4
            via 10.2.2.10, Ethernet2
         via 10.1.1.10 [0 pref/0 metric] type ipv4
            via 10.1.1.10, Ethernet1
 B    10.40.42.0/24 [200 pref/0 MED] updated 00:02:31 ago
         via 1.1.1.1 [0 pref/0 metric] type ipv4
            via 1.1.1.1, Vlan4094
>B    10.40.43.0/24 [200 pref/0 MED] updated 00:02:17 ago
         via 10.2.2.10 [0 pref/0 metric] type ipv4
            via 10.2.2.10, Ethernet2
         via 10.1.1.10 [0 pref/0 metric] type ipv4
            via 10.1.1.10, Ethernet1
>B    10.255.1.1/32 [200 pref/0 MED] updated 00:02:17 ago
         via 10.2.2.10 [0 pref/0 metric] type ipv4
            via 10.2.2.10, Ethernet2
         via 10.1.1.10 [0 pref/0 metric] type ipv4
            via 10.1.1.10, Ethernet1
>B    10.255.1.2/32 [200 pref/0 MED] updated 00:02:17 ago
         via 10.2.2.10 [0 pref/0 metric] type ipv4
            via 10.2.2.10, Ethernet2
         via 10.1.1.10 [0 pref/0 metric] type ipv4
            via 10.1.1.10, Ethernet1
>B    10.255.2.1/32 [200 pref/0 MED] updated 00:02:17 ago
         via 10.2.2.10 [0 pref/0 metric] type ipv4
            via 10.2.2.10, Ethernet2
         via 10.1.1.10 [0 pref/0 metric] type ipv4
            via 10.1.1.10, Ethernet1
>B    10.255.2.2/32 [200 pref/0 MED] updated 00:02:17 ago
         via 10.2.2.10 [0 pref/0 metric] type ipv4
            via 10.2.2.10, Ethernet2
         via 10.1.1.10 [0 pref/0 metric] type ipv4
            via 10.1.1.10, Ethernet1
>B    10.255.3.1/32 [200 pref/0 MED] updated 00:02:31 ago
         via 1.1.1.1 [0 pref/0 metric] type ipv4
            via 1.1.1.1, Vlan4094
>B    10.255.4.1/32 [200 pref/0 MED] updated 00:02:17 ago
         via 10.2.2.10 [0 pref/0 metric] type ipv4
            via 10.2.2.10, Ethernet2
         via 10.1.1.10 [0 pref/0 metric] type ipv4
            via 10.1.1.10, Ethernet1
>B    10.255.4.2/32 [200 pref/0 MED] updated 00:02:17 ago
         via 10.2.2.10 [0 pref/0 metric] type ipv4
            via 10.2.2.10, Ethernet2
         via 10.1.1.10 [0 pref/0 metric] type ipv4
            via 10.1.1.10, Ethernet1
>B    10.255.255.1/32 [200 pref/0 MED] updated 00:02:17 ago
         via 10.1.1.10 [0 pref/0 metric] type ipv4
            via 10.1.1.10, Ethernet1
>B    10.255.255.2/32 [200 pref/0 MED] updated 00:02:22 ago
         via 10.2.2.10 [0 pref/0 metric] type ipv4
            via 10.2.2.10, Ethernet2
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
>P    0.0.0.0/8 [1 pref/0 metric] updated 00:04:41 ago
         via Null0, directly connected [NF]
>P    127.0.0.0/8 [1 pref/0 metric] updated 00:04:41 ago
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
>P    ::/96 [1 pref/0 metric] updated 00:04:41 ago
         via Null0, directly connected [NF]
>P    ::ffff:127.0.0.0/104 [1 pref/0 metric] updated 00:04:41 ago
         via :: [1 pref/1 metric] type ipv6
            via , directly connected
>P    fe80::/10 [1 pref/0 metric] updated 00:04:41 ago
```

## show platform sand l3 summary

```text
Number of vrfs: 2

Ipv4:
  Routes:       57  backlog:  0  unprogrammed:  0
  Adjacencies:  31  backlog:  0  unprogrammed:  0
Ipv6:
  Routes:       0   backlog:  0  unprogrammed:  0
  Adjacencies:  31  backlog:  0  unprogrammed:  0
Mpls:
  Routes:       0  backlog:  0  unprogrammed:  0
  Adjacencies:  0  backlog:  0  unprogrammed:  0

Jericho2 Ip Fecs:
  Non-ecmp fecs:  4105  ecmp fecs:  1  fec entries:  4107
Jericho2 Mpls Fecs:
  Non-ecmp fecs:  0  ecmp fecs:  0  fec entries:  0
Jericho2 Vxlan Tunnel Fecs:
  Non-ecmp fecs:  0  ecmp fecs:  0  fec entries:  0
  Number of vxlan tunnels configured: 0

Jericho2 Lpm Routes:
  Routes:   57  unprogrammed:   0   
  Routes6:  1   unprogrammed6:  0   
  Backlog:  0 

Jericho2 Lpm:
  TCAM entries used:   2  Percent free:  99  ADS2 entries used:   2  Percent free:  99
  Pivot buckets used:  2  Rows used:     1   Entries Per Bucket:  1  Percent free:  99
  Route buckets used:  9  Rows used:     1   Entries Per Bucket:  6  Percent free:  99

Lem:
  IPv4  Host in Lem:            disabled
  IPv4  Prefix-lengths in Lem:  None    
  IPv6  Host in Lem:            disabled
  IPv6  Prefix-lengths in Lem:  None    
  Number of downloads:        0
  Number of overflow events:  0

Egress Arp rewrite entries in use (in each fap):
  FixedSystem: 3
Egress Arp remote rewrite entries in use (in each fap):
  FixedSystem: 0
Egress Ip tunnel rewrite entries in use (in each fap):
  FixedSystem: 0
Egress Mpls (for outer 2 labels) rewrite entries in use (in each fap):
  FixedSystem: 0
Egress Mpls (for inner 2 labels) rewrite entries in use (in each fap):
  FixedSystem: 0
Egress Sflow rewrite entries in use (in each fap):
  FixedSystem: 0

Egress rewrite chains in backlog: resource-full 0, no-interface 0

Glem entries used per fap :
  FixedSystem: 4099

Jericho2 Fec:
  Maximum FEC hierarchy levels:  2
  ReusedEcmp:  0  allocs:  8  frees:  0  shuffles:  0  cmds:  0
  Zombies:     0    purges:    0
  Quarantine:  0/0  shuffles:  0  deletes:  0   
  Fec insertion failures:  0
  Level1  Fecs:
    Non-ecmp fecs:            0    ecmp fecs:            1 
    Non-ecmp (Percent free):  100  ecmp (Percent free):  99
  Level2  Fecs:
    Non-ecmp fecs:            9   ecmp fecs:            1 
    Non-ecmp (Percent free):  99  ecmp (Percent free):  99
  Level3  Fecs:
    Non-ecmp fecs:            0    ecmp fecs:            0  
    Non-ecmp (Percent free):  100  ecmp (Percent free):  100

Lpm Detail:
  Requests:  115  cleanses:  18  batches:  18  avg batch size:  6

Jericho Arp:
  ArpTable writes:      16869  queued      0   
  IngressTable writes:  75162  queued      0   
  Coprocessors:         1      in CmdRing

Tunnel Counter Status
  Number of MPLS tunnels:                  0    
  Number of uncountable MPLS tunnels:      0    
  Number of MPLSoGRE tunnels:              0    
  Number of uncountable MPLSoGRE tunnels:  0    
  Number of IP tunnels:                    0    
  Number of uncountable IP tunnels:        0    
  Shuffle tunnel enabled:                  False
```

## show platform jericho2 ip route

```text
Tunnel Type: M(mpls), G(gre), MoG(mpls-over-gre), MoU(mpls-over-udp), IPoU(ip-over-udp)
             vxlan-o(vxlan outer-rewrite info), vxlan-i(vxlan inner-rewrite info)
CW  - Control word
FL  - Flow label
EL  - Entropy label
ELI - Entropy label indicator
*   - Routes in LEM
D   - ECMP is divergent across switching chips
 ----------------------------------------------------------------------------------------------------------
|                                 Routing Table                                            |              |
|----------------------------------------------------------------------------------------------------------
|VRF|   Destination    |     |                    |     |        |                   | ECMP|  FEC | Tunnel
| ID|      Subnet      | Cmd |     Destination    | VID | Outlif |   MAC / CPU Code  |Index| Index|T Value
 ----------------------------------------------------------------------------------------------------------
|0  |0.0.0.0/8         |DROP | DROP               |0    |  -     |                   |  -  |288360|   -   
|0  |1.1.1.0/32        |TRAP | CoppSystemIpBcast  |0    |  -     | BcastReceive      |  -  |524288|   -   
|0  |1.1.1.1/32        |ROUTE| Po2000             |4094 |2097151 | 94:8e:d3:51:7c:10 |  -  |288361|   -   
|0  |1.1.1.2/32        |TRAP | CoppSystemIpUcast  |0    |  -     | Receive           |  -  |524291|   -   
|0  |1.1.1.3/32        |TRAP | CoppSystemIpBcast  |0    |  -     | BcastReceive      |  -  |524288|   -   
|0  |1.1.1.0/30        |TRAP | CoppSystemL3DstMiss|4094 |4094    | ArpTrap           |  -  |528388|   -   
|0  |10.1.1.10/32      |ROUTE| Et1                |1007 |103421  | 74:83:ef:6c:be:a5 |  -  |288365|   -   
|0  |10.1.1.11/32      |TRAP | CoppSystemIpUcast  |0    |  -     | Receive           |  -  |524291|   -   
|0  |10.1.1.10/31      |TRAP | CoppSystemL3DstMiss|1007 |1007    | ArpTrap           |  -  |525301|   -   
|0  |10.2.2.10/32      |ROUTE| Et2                |1006 |103422  | 74:83:ef:6c:c1:3f |  -  |288363|   -   
|0  |10.2.2.11/32      |TRAP | CoppSystemIpUcast  |0    |  -     | Receive           |  -  |524291|   -   
|0  |10.2.2.10/31      |TRAP | CoppSystemL3DstMiss|1006 |1006    | ArpTrap           |  -  |525300|   -   
|0  |10.10.10.0/24     |ROUTE| Et1                |1007 |103421  | 74:83:ef:6c:be:a5 |16384|288366|   -   
|0  |10.10.10.0/24     |ROUTE| Et2                |1006 |103422  | 74:83:ef:6c:c1:3f |16384|288367|   -   
|0  |10.10.11.0/24     |ROUTE| Et1                |1007 |103421  | 74:83:ef:6c:be:a5 |16384|288366|   -   
|0  |10.10.11.0/24     |ROUTE| Et2                |1006 |103422  | 74:83:ef:6c:c1:3f |16384|288367|   -   
|0  |10.10.12.0/32     |TRAP | CoppSystemIpBcast  |0    |  -     | BcastReceive      |  -  |524288|   -   
|0  |10.10.12.1/32     |TRAP | CoppSystemIpUcast  |0    |  -     | Receive           |  -  |524291|   -   
|0  |10.10.12.3/32     |TRAP | CoppSystemIpUcast  |0    |  -     | Receive           |  -  |524291|   -   
|0  |10.10.12.255/32   |TRAP | CoppSystemIpBcast  |0    |  -     | BcastReceive      |  -  |524288|   -   
|0  |10.10.12.0/24     |TRAP | CoppSystemL3DstMiss|10   |10      | ArpTrap           |  -  |524304|   -   
|0  |10.10.13.0/24     |ROUTE| Et1                |1007 |103421  | 74:83:ef:6c:be:a5 |16384|288366|   -   
|0  |10.10.13.0/24     |ROUTE| Et2                |1006 |103422  | 74:83:ef:6c:c1:3f |16384|288367|   -   
|0  |10.20.20.0/24     |ROUTE| Et1                |1007 |103421  | 74:83:ef:6c:be:a5 |16384|288366|   -   
|0  |10.20.20.0/24     |ROUTE| Et2                |1006 |103422  | 74:83:ef:6c:c1:3f |16384|288367|   -   
|0  |10.20.21.0/24     |ROUTE| Et1                |1007 |103421  | 74:83:ef:6c:be:a5 |16384|288366|   -   
|0  |10.20.21.0/24     |ROUTE| Et2                |1006 |103422  | 74:83:ef:6c:c1:3f |16384|288367|   -   
|0  |10.20.22.0/32     |TRAP | CoppSystemIpBcast  |0    |  -     | BcastReceive      |  -  |524288|   -   
|0  |10.20.22.1/32     |TRAP | CoppSystemIpUcast  |0    |  -     | Receive           |  -  |524291|   -   
|0  |10.20.22.3/32     |TRAP | CoppSystemIpUcast  |0    |  -     | Receive           |  -  |524291|   -   
|0  |10.20.22.255/32   |TRAP | CoppSystemIpBcast  |0    |  -     | BcastReceive      |  -  |524288|   -   
|0  |10.20.22.0/24     |TRAP | CoppSystemL3DstMiss|20   |20      | ArpTrap           |  -  |524314|   -   
|0  |10.20.23.0/24     |ROUTE| Et1                |1007 |103421  | 74:83:ef:6c:be:a5 |16384|288366|   -   
|0  |10.20.23.0/24     |ROUTE| Et2                |1006 |103422  | 74:83:ef:6c:c1:3f |16384|288367|   -   
|0  |10.30.30.0/24     |ROUTE| Et1                |1007 |103421  | 74:83:ef:6c:be:a5 |16384|288366|   -   
|0  |10.30.30.0/24     |ROUTE| Et2                |1006 |103422  | 74:83:ef:6c:c1:3f |16384|288367|   -   
|0  |10.30.31.0/24     |ROUTE| Et1                |1007 |103421  | 74:83:ef:6c:be:a5 |16384|288366|   -   
|0  |10.30.31.0/24     |ROUTE| Et2                |1006 |103422  | 74:83:ef:6c:c1:3f |16384|288367|   -   
|0  |10.30.32.0/32     |TRAP | CoppSystemIpBcast  |0    |  -     | BcastReceive      |  -  |524288|   -   
|0  |10.30.32.1/32     |TRAP | CoppSystemIpUcast  |0    |  -     | Receive           |  -  |524291|   -   
|0  |10.30.32.3/32     |TRAP | CoppSystemIpUcast  |0    |  -     | Receive           |  -  |524291|   -   
|0  |10.30.32.255/32   |TRAP | CoppSystemIpBcast  |0    |  -     | BcastReceive      |  -  |524288|   -   
|0  |10.30.32.0/24     |TRAP | CoppSystemL3DstMiss|30   |30      | ArpTrap           |  -  |524324|   -   
|0  |10.30.33.0/24     |ROUTE| Et1                |1007 |103421  | 74:83:ef:6c:be:a5 |16384|288366|   -   
|0  |10.30.33.0/24     |ROUTE| Et2                |1006 |103422  | 74:83:ef:6c:c1:3f |16384|288367|   -   
|0  |10.40.40.0/24     |ROUTE| Et1                |1007 |103421  | 74:83:ef:6c:be:a5 |16384|288366|   -   
|0  |10.40.40.0/24     |ROUTE| Et2                |1006 |103422  | 74:83:ef:6c:c1:3f |16384|288367|   -   
|0  |10.40.41.0/24     |ROUTE| Et1                |1007 |103421  | 74:83:ef:6c:be:a5 |16384|288366|   -   
|0  |10.40.41.0/24     |ROUTE| Et2                |1006 |103422  | 74:83:ef:6c:c1:3f |16384|288367|   -   
|0  |10.40.42.0/32     |TRAP | CoppSystemIpBcast  |0    |  -     | BcastReceive      |  -  |524288|   -   
|0  |10.40.42.1/32     |TRAP | CoppSystemIpUcast  |0    |  -     | Receive           |  -  |524291|   -   
|0  |10.40.42.3/32     |TRAP | CoppSystemIpUcast  |0    |  -     | Receive           |  -  |524291|   -   
|0  |10.40.42.255/32   |TRAP | CoppSystemIpBcast  |0    |  -     | BcastReceive      |  -  |524288|   -   
|0  |10.40.42.0/24     |TRAP | CoppSystemL3DstMiss|40   |40      | ArpTrap           |  -  |524334|   -   
|0  |10.40.43.0/24     |ROUTE| Et1                |1007 |103421  | 74:83:ef:6c:be:a5 |16384|288366|   -   
|0  |10.40.43.0/24     |ROUTE| Et2                |1006 |103422  | 74:83:ef:6c:c1:3f |16384|288367|   -   
|0  |10.255.1.1/32     |ROUTE| Et1                |1007 |103421  | 74:83:ef:6c:be:a5 |16384|288366|   -   
|0  |10.255.1.1/32     |ROUTE| Et2                |1006 |103422  | 74:83:ef:6c:c1:3f |16384|288367|   -   
|0  |10.255.1.2/32     |ROUTE| Et1                |1007 |103421  | 74:83:ef:6c:be:a5 |16384|288366|   -   
|0  |10.255.1.2/32     |ROUTE| Et2                |1006 |103422  | 74:83:ef:6c:c1:3f |16384|288367|   -   
|0  |10.255.2.1/32     |ROUTE| Et1                |1007 |103421  | 74:83:ef:6c:be:a5 |16384|288366|   -   
|0  |10.255.2.1/32     |ROUTE| Et2                |1006 |103422  | 74:83:ef:6c:c1:3f |16384|288367|   -   
|0  |10.255.2.2/32     |ROUTE| Et1                |1007 |103421  | 74:83:ef:6c:be:a5 |16384|288366|   -   
|0  |10.255.2.2/32     |ROUTE| Et2                |1006 |103422  | 74:83:ef:6c:c1:3f |16384|288367|   -   
|0  |10.255.3.1/32     |ROUTE| Po2000             |4094 |2097151 | 94:8e:d3:51:7c:10 |  -  |288362|   -   
|0  |10.255.3.2/32     |TRAP | CoppSystemIpUcast  |0    |  -     | Receive           |  -  |524291|   -   
|0  |10.255.4.1/32     |ROUTE| Et1                |1007 |103421  | 74:83:ef:6c:be:a5 |16384|288366|   -   
|0  |10.255.4.1/32     |ROUTE| Et2                |1006 |103422  | 74:83:ef:6c:c1:3f |16384|288367|   -   
|0  |10.255.4.2/32     |ROUTE| Et1                |1007 |103421  | 74:83:ef:6c:be:a5 |16384|288366|   -   
|0  |10.255.4.2/32     |ROUTE| Et2                |1006 |103422  | 74:83:ef:6c:c1:3f |16384|288367|   -   
|0  |10.255.255.1/32   |ROUTE| Et1                |1007 |103421  | 74:83:ef:6c:be:a5 |  -  |288368|   -   
|0  |10.255.255.2/32   |ROUTE| Et2                |1006 |103422  | 74:83:ef:6c:c1:3f |  -  |288364|   -   
|0  |127.0.0.0/8       |TRAP | CoppSystemL3DstMiss|0    |  -     | ArpTrap           |  -  |524294|   -   
|0  |223.255.255.255/32|TRAP | CoppSystemIpUcast  |0    |  -     | Receive           |  -  |524291|   -   
|0  |0.0.0.0/0         |TRAP | CoppSystemL3LpmOver|0    |  -     | SlowReceive       |  -  |524292|   -   

```

## show platform jericho2 fec all

```text
Tunnel Type: Mpop(mpls pop), Mpush(mpls push), Mswap(mpls swap),
             MoG(mpls-over-gre), T(IPv4 tunnels GRE/GUE/VXLAN),
             N(Ipsec tunnel NAT-T [IP,SPORT,DPORT])
CW  - Control word
FL  - Flow label
EL  - Entropy label
ELI - Entropy label indicator
D   - ECMP is divergent across switching chips
 -----------------------------------------------------------------------------------------------
|                                              FEC Entry                                        |
 -----------------------------------------------------------------------------------------------
|     |      |     |                    |     |        |                   |
| ECMP|  FEC |     |                    |     |        |                   |
|Index| Index| Cmd |     Destination    | VID | Outlif |   MAC / CPU Code  |    Tunnel Value
 -----------------------------------------------------------------------------------------------
|16384|288366|ROUTE| Et1                |1007 |103421  | 74:83:ef:6c:be:a5 |   -   
|16384|288367|ROUTE| Et2                |1006 |103422  | 74:83:ef:6c:c1:3f |   -   
|  -  |288360|DROP | DROP               |0    |  -     |                   |   -   
|  -  |288361|ROUTE| Po2000             |4094 |2097151 | 94:8e:d3:51:7c:10 |   -   
|  -  |288362|ROUTE| Po2000             |4094 |2097151 | 94:8e:d3:51:7c:10 |   -   
|  -  |288363|ROUTE| Et2                |1006 |103422  | 74:83:ef:6c:c1:3f |   -   
|  -  |288364|ROUTE| Et2                |1006 |103422  | 74:83:ef:6c:c1:3f |   -   
|  -  |288365|ROUTE| Et1                |1007 |103421  | 74:83:ef:6c:be:a5 |   -   
|  -  |288368|ROUTE| Et1                |1007 |103421  | 74:83:ef:6c:be:a5 |   -   
|  -  |524288|TRAP | CoppSystemIpBcast  |0    |  -     | BcastReceive      |   -   
|  -  |524291|TRAP | CoppSystemIpUcast  |0    |  -     | Receive           |   -   
|  -  |524292|TRAP | CoppSystemL3LpmOver|0    |  -     | SlowReceive       |   -   
|  -  |524293|TRAP | CoppSystemL3LpmOver|0    |  -     | SlowReceive       |   -   
|  -  |524294|TRAP | CoppSystemL3DstMiss|0    |  -     | ArpTrap           |   -   
|  -  |524304|TRAP | CoppSystemL3DstMiss|10   |10      | ArpTrap           |   -   
|  -  |524314|TRAP | CoppSystemL3DstMiss|20   |20      | ArpTrap           |   -   
|  -  |524324|TRAP | CoppSystemL3DstMiss|30   |30      | ArpTrap           |   -   
|  -  |524334|TRAP | CoppSystemL3DstMiss|40   |40      | ArpTrap           |   -   
|  -  |525300|TRAP | CoppSystemL3DstMiss|1006 |1006    | ArpTrap           |   -   
|  -  |525301|TRAP | CoppSystemL3DstMiss|1007 |1007    | ArpTrap           |   -   
|  -  |528388|TRAP | CoppSystemL3DstMiss|4094 |4094    | ArpTrap           |   -   

```

## 

```text
```

## 

```text
```

