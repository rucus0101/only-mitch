# Test results for S1

## show version

```text
Arista DCS-7280SRA-48C6-F
Hardware version: 21.00
Serial number: SSJ18197397
Hardware MAC address: 7483.ef6c.bea5
System MAC address: 7483.ef6c.bea5

Software image version: 4.31.1F
Architecture: x86_64
Internal build version: 4.31.1F-34556000.4311F
Internal build ID: 48c47833-3f4a-4a14-9783-0017c2f42e54
Image format version: 3.0
Image optimization: Sand-4GB

Uptime: 38 minutes
Total memory: 8051592 kB
Free memory: 5267140 kB

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

 C        10.1.1.0/31 is directly connected, Ethernet1
 C        10.1.1.2/31 is directly connected, Ethernet2
 C        10.1.1.4/31 is directly connected, Ethernet3
 C        10.1.1.6/31 is directly connected, Ethernet4
 C        10.1.1.8/31 is directly connected, Ethernet7
 C        10.1.1.10/31 is directly connected, Ethernet8
 C        10.1.1.12/31 is directly connected, Ethernet9
 C        10.1.1.14/31 is directly connected, Ethernet10
 B E      10.10.10.0/24 [200/0] via 10.1.1.1, Ethernet1
                                via 10.1.1.3, Ethernet2
 B E      10.10.11.0/24 [200/0] via 10.1.1.5, Ethernet3
                                via 10.1.1.7, Ethernet4
 B E      10.10.12.0/24 [200/0] via 10.1.1.9, Ethernet7
                                via 10.1.1.11, Ethernet8
 B E      10.10.13.0/24 [200/0] via 10.1.1.13, Ethernet9
                                via 10.1.1.15, Ethernet10
 B E      10.20.20.0/24 [200/0] via 10.1.1.1, Ethernet1
                                via 10.1.1.3, Ethernet2
 B E      10.20.21.0/24 [200/0] via 10.1.1.5, Ethernet3
                                via 10.1.1.7, Ethernet4
 B E      10.20.22.0/24 [200/0] via 10.1.1.9, Ethernet7
                                via 10.1.1.11, Ethernet8
 B E      10.20.23.0/24 [200/0] via 10.1.1.13, Ethernet9
                                via 10.1.1.15, Ethernet10
 B E      10.30.30.0/24 [200/0] via 10.1.1.1, Ethernet1
                                via 10.1.1.3, Ethernet2
 B E      10.30.31.0/24 [200/0] via 10.1.1.5, Ethernet3
                                via 10.1.1.7, Ethernet4
 B E      10.30.32.0/24 [200/0] via 10.1.1.9, Ethernet7
                                via 10.1.1.11, Ethernet8
 B E      10.30.33.0/24 [200/0] via 10.1.1.13, Ethernet9
                                via 10.1.1.15, Ethernet10
 B E      10.40.40.0/24 [200/0] via 10.1.1.1, Ethernet1
                                via 10.1.1.3, Ethernet2
 B E      10.40.41.0/24 [200/0] via 10.1.1.5, Ethernet3
                                via 10.1.1.7, Ethernet4
 B E      10.40.42.0/24 [200/0] via 10.1.1.9, Ethernet7
                                via 10.1.1.11, Ethernet8
 B E      10.40.43.0/24 [200/0] via 10.1.1.13, Ethernet9
                                via 10.1.1.15, Ethernet10
 B E      10.255.1.1/32 [200/0] via 10.1.1.1, Ethernet1
                                via 10.1.1.3, Ethernet2
 B E      10.255.1.2/32 [200/0] via 10.1.1.1, Ethernet1
                                via 10.1.1.3, Ethernet2
 B E      10.255.2.1/32 [200/0] via 10.1.1.5, Ethernet3
                                via 10.1.1.7, Ethernet4
 B E      10.255.2.2/32 [200/0] via 10.1.1.5, Ethernet3
                                via 10.1.1.7, Ethernet4
 B E      10.255.3.1/32 [200/0] via 10.1.1.9, Ethernet7
                                via 10.1.1.11, Ethernet8
 B E      10.255.3.2/32 [200/0] via 10.1.1.9, Ethernet7
                                via 10.1.1.11, Ethernet8
 B E      10.255.4.1/32 [200/0] via 10.1.1.13, Ethernet9
                                via 10.1.1.15, Ethernet10
 B E      10.255.4.2/32 [200/0] via 10.1.1.13, Ethernet9
                                via 10.1.1.15, Ethernet10
 C        10.255.255.1/32 is directly connected, Loopback0
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
Router identifier 10.255.255.1, local AS number 65001
Route status codes: * - valid, > - active, S - Stale, E - ECMP head, e - ECMP
                    c - Contributing to ECMP, % - Pending best path selection
Origin codes: i - IGP, e - EGP, ? - incomplete
AS Path Attributes: Or-ID - Originator ID, C-LST - Cluster List, LL Nexthop - Link Local Nexthop

          Network                Next Hop              Metric  LocPref Weight  Path
```

## show bgp vpn-ipv4

```text
BGP routing table information for VRF default
Router identifier 10.255.255.1, local AS number 65001
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
Router identifier 10.255.255.1, local AS number 65001
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
Router identifier 10.255.255.1, local AS number 65001
Route status codes: s - suppressed contributor, * - valid, > - active, E - ECMP head, e - ECMP
                    S - Stale, c - Contributing to ECMP, b - backup, L - labeled-unicast
                    % - Pending best path selection
Origin codes: i - IGP, e - EGP, ? - incomplete
AS Path Attributes: Or-ID - Originator ID, C-LST - Cluster List, LL Nexthop - Link Local Nexthop

          Network                Next Hop              Metric  AIGP       LocPref Weight  Path
```

## show bgp neighbors

```text
BGP neighbor is 10.1.1.1, remote AS 65101, external link
  BGP version 4, remote router ID 10.255.1.1, VRF default
  Inherits configuration from and member of peer-group LEAVES
  Last read 00:00:34, last write 00:00:04
  Hold time is 180, keepalive interval is 60 seconds
  Configured hold time is 180, keepalive interval is 60 seconds
  Effective minimum hold time is 3 seconds
  Hold timer is active, time left: 00:02:26
  Keepalive timer is active, time left: 00:00:45
  Connect timer is inactive
  Idle-restart timer is inactive
  BGP state is Established, up for 00:33:58
  Number of transitions to established: 1
  Last state was OpenConfirm
  Last event was RecvUpdate
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
      Received 00:33:58
      Number of stale paths removed after graceful restart: 0
  AIGP attribute send and receive for IPv4 Unicast are disabled
  AIGP attribute send and receive for IPv4 with MPLS Labels are disabled
  AIGP attribute send and receive for IPv6 Unicast are disabled
  AIGP attribute send and receive for IPv6 with MPLS Labels are disabled
  BGP session driven failover for IPv6 Unicast is disabled
  BGP session driven failover for IPv4 Unicast is disabled
  Message Statistics:
                                  Sent      Rcvd
    Opens:                           1         1
    Notifications:                   0         0
    Updates:                         5        12
    Keepalives:                     41        41
    Enhanced Route Refresh:          0         0
    Begin of Route Refresh:          0         0
    End of Route Refresh:            0         0
    Total messages:                 47        54
  Prefix Statistics:
                                   Sent      Rcvd     Best Paths     Best ECMP Paths
    IPv4 Unicast:                    19        25              6                   6
    IPv6 Unicast:                     0         0              0                   0
  Configured maximum total number of routes is 256000, warning limit is 204800
  Inbound updates dropped by reason:
    AS path loop detection: 8
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
Local AS is 65001, local router ID 10.255.255.1
TTL is 1
Local TCP address is 10.1.1.0, local port is 179
Remote TCP address is 10.1.1.1, remote port is 37703
Local next hop for next hop self:
  IPv4 Unicast: 10.1.1.0
TCP Socket Information:
  TCP state is ESTABLISHED
  Recv-Q: 0/32768
  Send-Q: 0/332800
  Outgoing Maximum Segment Size (MSS): 9162
  Total Number of TCP retransmissions: 5
  Options:
    Timestamps enabled: yes
    Selective Acknowledgments enabled: yes
    Window Scale enabled: yes
    Explicit Congestion Notification (ECN) enabled: no
  Socket Statistics:
    Window Scale (wscale): 7,7
    Retransmission Timeout (rto): 236.0ms
    Round-trip Time (rtt/rtvar): 28.0ms/11.5ms
    Delayed Ack Timeout (ato): 40.0ms
    Congestion Window (cwnd): 10
    TCP Throughput: 26.22 Mbps
    Advertised Recv Window (rcv_space): 56362

BGP neighbor is 10.1.1.3, remote AS 65101, external link
  BGP version 4, remote router ID 10.255.1.2, VRF default
  Inherits configuration from and member of peer-group LEAVES
  Last read 00:00:36, last write 00:00:01
  Hold time is 180, keepalive interval is 60 seconds
  Configured hold time is 180, keepalive interval is 60 seconds
  Effective minimum hold time is 3 seconds
  Hold timer is active, time left: 00:02:24
  Keepalive timer is active, time left: 00:00:56
  Connect timer is inactive
  Idle-restart timer is inactive
  BGP state is Established, up for 00:33:58
  Number of transitions to established: 1
  Last state was OpenConfirm
  Last event was RecvUpdate
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
      Received 00:33:57
      Number of stale paths removed after graceful restart: 0
  AIGP attribute send and receive for IPv4 Unicast are disabled
  AIGP attribute send and receive for IPv4 with MPLS Labels are disabled
  AIGP attribute send and receive for IPv6 Unicast are disabled
  AIGP attribute send and receive for IPv6 with MPLS Labels are disabled
  BGP session driven failover for IPv6 Unicast is disabled
  BGP session driven failover for IPv4 Unicast is disabled
  Message Statistics:
                                  Sent      Rcvd
    Opens:                           1         1
    Notifications:                   0         0
    Updates:                         6         5
    Keepalives:                     42        42
    Enhanced Route Refresh:          0         0
    Begin of Route Refresh:          0         0
    End of Route Refresh:            0         0
    Total messages:                 49        48
  Prefix Statistics:
                                   Sent      Rcvd     Best Paths     Best ECMP Paths
    IPv4 Unicast:                    25         7              6                   0
    IPv6 Unicast:                     0         0              0                   0
  Configured maximum total number of routes is 256000, warning limit is 204800
  Inbound updates dropped by reason:
    AS path loop detection: 2
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
Local AS is 65001, local router ID 10.255.255.1
TTL is 1
Local TCP address is 10.1.1.2, local port is 179
Remote TCP address is 10.1.1.3, remote port is 37375
Local next hop for next hop self:
  IPv4 Unicast: 10.1.1.2
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
    Round-trip Time (rtt/rtvar): 8.2ms/2.7ms
    Delayed Ack Timeout (ato): 40.0ms
    Congestion Window (cwnd): 10
    TCP Throughput: 89.10 Mbps
    Advertised Recv Window (rcv_space): 56362

BGP neighbor is 10.1.1.5, remote AS 65201, external link
  BGP version 4, remote router ID 10.255.2.1, VRF default
  Inherits configuration from and member of peer-group LEAVES
  Last read 00:00:40, last write 00:00:44
  Hold time is 180, keepalive interval is 60 seconds
  Configured hold time is 180, keepalive interval is 60 seconds
  Effective minimum hold time is 3 seconds
  Hold timer is active, time left: 00:02:20
  Keepalive timer is active, time left: 00:00:14
  Connect timer is inactive
  Idle-restart timer is inactive
  BGP state is Established, up for 00:33:58
  Number of transitions to established: 1
  Last state was OpenConfirm
  Last event was RecvUpdate
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
      Received 00:33:58
      Number of stale paths removed after graceful restart: 0
  AIGP attribute send and receive for IPv4 Unicast are disabled
  AIGP attribute send and receive for IPv4 with MPLS Labels are disabled
  AIGP attribute send and receive for IPv6 Unicast are disabled
  AIGP attribute send and receive for IPv6 with MPLS Labels are disabled
  BGP session driven failover for IPv6 Unicast is disabled
  BGP session driven failover for IPv4 Unicast is disabled
  Message Statistics:
                                  Sent      Rcvd
    Opens:                           1         1
    Notifications:                   0         0
    Updates:                         5         4
    Keepalives:                     41        41
    Enhanced Route Refresh:          0         0
    Begin of Route Refresh:          0         0
    End of Route Refresh:            0         0
    Total messages:                 47        46
  Prefix Statistics:
                                   Sent      Rcvd     Best Paths     Best ECMP Paths
    IPv4 Unicast:                    19         7              6                   6
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
Local AS is 65001, local router ID 10.255.255.1
TTL is 1
Local TCP address is 10.1.1.4, local port is 179
Remote TCP address is 10.1.1.5, remote port is 35663
Local next hop for next hop self:
  IPv4 Unicast: 10.1.1.4
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
    Retransmission Timeout (rto): 220.0ms
    Round-trip Time (rtt/rtvar): 17.5ms/8.3ms
    Delayed Ack Timeout (ato): 40.0ms
    Congestion Window (cwnd): 10
    TCP Throughput: 41.93 Mbps
    Advertised Recv Window (rcv_space): 56362

BGP neighbor is 10.1.1.7, remote AS 65201, external link
  BGP version 4, remote router ID 10.255.2.2, VRF default
  Inherits configuration from and member of peer-group LEAVES
  Last read 00:00:37, last write 00:00:37
  Hold time is 180, keepalive interval is 60 seconds
  Configured hold time is 180, keepalive interval is 60 seconds
  Effective minimum hold time is 3 seconds
  Hold timer is active, time left: 00:02:23
  Keepalive timer is active, time left: 00:00:21
  Connect timer is inactive
  Idle-restart timer is inactive
  BGP state is Established, up for 00:33:58
  Number of transitions to established: 1
  Last state was OpenConfirm
  Last event was RecvUpdate
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
      Received 00:33:58
      Number of stale paths removed after graceful restart: 0
  AIGP attribute send and receive for IPv4 Unicast are disabled
  AIGP attribute send and receive for IPv4 with MPLS Labels are disabled
  AIGP attribute send and receive for IPv6 Unicast are disabled
  AIGP attribute send and receive for IPv6 with MPLS Labels are disabled
  BGP session driven failover for IPv6 Unicast is disabled
  BGP session driven failover for IPv4 Unicast is disabled
  Message Statistics:
                                  Sent      Rcvd
    Opens:                           1         1
    Notifications:                   0         0
    Updates:                         6         6
    Keepalives:                     42        41
    Enhanced Route Refresh:          0         0
    Begin of Route Refresh:          0         0
    End of Route Refresh:            0         0
    Total messages:                 49        48
  Prefix Statistics:
                                   Sent      Rcvd     Best Paths     Best ECMP Paths
    IPv4 Unicast:                    25         7              6                   0
    IPv6 Unicast:                     0         0              0                   0
  Configured maximum total number of routes is 256000, warning limit is 204800
  Inbound updates dropped by reason:
    AS path loop detection: 2
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
Local AS is 65001, local router ID 10.255.255.1
TTL is 1
Local TCP address is 10.1.1.6, local port is 179
Remote TCP address is 10.1.1.7, remote port is 35227
Local next hop for next hop self:
  IPv4 Unicast: 10.1.1.6
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
    Retransmission Timeout (rto): 208.0ms
    Round-trip Time (rtt/rtvar): 7.4ms/1.9ms
    Delayed Ack Timeout (ato): 40.0ms
    Congestion Window (cwnd): 10
    TCP Throughput: 99.53 Mbps
    Advertised Recv Window (rcv_space): 56362

BGP neighbor is 10.1.1.9, remote AS 65301, external link
  BGP version 4, remote router ID 10.255.3.1, VRF default
  Inherits configuration from and member of peer-group LEAVES
  Last read 00:00:20, last write 00:00:02
  Hold time is 180, keepalive interval is 60 seconds
  Configured hold time is 180, keepalive interval is 60 seconds
  Effective minimum hold time is 3 seconds
  Hold timer is active, time left: 00:02:40
  Keepalive timer is active, time left: 00:00:46
  Connect timer is inactive
  Idle-restart timer is inactive
  BGP state is Established, up for 00:33:54
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
      Received 00:33:49
      Number of stale paths removed after graceful restart: 0
  AIGP attribute send and receive for IPv4 Unicast are disabled
  AIGP attribute send and receive for IPv4 with MPLS Labels are disabled
  AIGP attribute send and receive for IPv6 Unicast are disabled
  AIGP attribute send and receive for IPv6 with MPLS Labels are disabled
  BGP session driven failover for IPv6 Unicast is disabled
  BGP session driven failover for IPv4 Unicast is disabled
  Message Statistics:
                                  Sent      Rcvd
    Opens:                           1         1
    Notifications:                   0         0
    Updates:                         6        11
    Keepalives:                     40        42
    Enhanced Route Refresh:          0         0
    Begin of Route Refresh:          0         0
    End of Route Refresh:            0         0
    Total messages:                 47        54
  Prefix Statistics:
                                   Sent      Rcvd     Best Paths     Best ECMP Paths
    IPv4 Unicast:                    25         7              6                   0
    IPv6 Unicast:                     0         0              0                   0
  Configured maximum total number of routes is 256000, warning limit is 204800
  Inbound updates dropped by reason:
    AS path loop detection: 6
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
Local AS is 65001, local router ID 10.255.255.1
TTL is 1
Local TCP address is 10.1.1.8, local port is 179
Remote TCP address is 10.1.1.9, remote port is 39457
Local next hop for next hop self:
  IPv4 Unicast: 10.1.1.8
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
    Retransmission Timeout (rto): 208.0ms
    Round-trip Time (rtt/rtvar): 6.8ms/1.9ms
    Delayed Ack Timeout (ato): 40.0ms
    Congestion Window (cwnd): 10
    TCP Throughput: 108.19 Mbps
    Advertised Recv Window (rcv_space): 56362

BGP neighbor is 10.1.1.11, remote AS 65301, external link
  BGP version 4, remote router ID 10.255.3.2, VRF default
  Inherits configuration from and member of peer-group LEAVES
  Last read 00:00:35, last write 00:00:55
  Hold time is 180, keepalive interval is 60 seconds
  Configured hold time is 180, keepalive interval is 60 seconds
  Effective minimum hold time is 3 seconds
  Hold timer is active, time left: 00:02:25
  Keepalive timer is active, time left: 00:00:00
  Connect timer is inactive
  Idle-restart timer is inactive
  BGP state is Established, up for 00:33:56
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
      Received 00:33:51
      Number of stale paths removed after graceful restart: 0
  AIGP attribute send and receive for IPv4 Unicast are disabled
  AIGP attribute send and receive for IPv4 with MPLS Labels are disabled
  AIGP attribute send and receive for IPv6 Unicast are disabled
  AIGP attribute send and receive for IPv6 with MPLS Labels are disabled
  BGP session driven failover for IPv6 Unicast is disabled
  BGP session driven failover for IPv4 Unicast is disabled
  Message Statistics:
                                  Sent      Rcvd
    Opens:                           1         1
    Notifications:                   0         0
    Updates:                         5         4
    Keepalives:                     40        41
    Enhanced Route Refresh:          0         0
    Begin of Route Refresh:          0         0
    End of Route Refresh:            0         0
    Total messages:                 46        46
  Prefix Statistics:
                                   Sent      Rcvd     Best Paths     Best ECMP Paths
    IPv4 Unicast:                    19         7              6                   6
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
Local AS is 65001, local router ID 10.255.255.1
TTL is 1
Local TCP address is 10.1.1.10, local port is 179
Remote TCP address is 10.1.1.11, remote port is 37827
Local next hop for next hop self:
  IPv4 Unicast: 10.1.1.10
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
    Round-trip Time (rtt/rtvar): 8.5ms/2.7ms
    Delayed Ack Timeout (ato): 40.0ms
    Congestion Window (cwnd): 10
    TCP Throughput: 85.95 Mbps
    Advertised Recv Window (rcv_space): 56362

BGP neighbor is 10.1.1.13, remote AS 65401, external link
  BGP version 4, remote router ID 10.255.4.1, VRF default
  Inherits configuration from and member of peer-group LEAVES
  Last read 00:00:02, last write 00:00:52
  Hold time is 180, keepalive interval is 60 seconds
  Configured hold time is 180, keepalive interval is 60 seconds
  Effective minimum hold time is 3 seconds
  Hold timer is active, time left: 00:02:58
  Keepalive timer is active, time left: 00:00:00
  Connect timer is inactive
  Idle-restart timer is inactive
  BGP state is Established, up for 00:33:54
  Number of transitions to established: 1
  Last state was OpenConfirm
  Last event was RecvUpdate
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
      Received 00:33:54
      Number of stale paths removed after graceful restart: 0
  AIGP attribute send and receive for IPv4 Unicast are disabled
  AIGP attribute send and receive for IPv4 with MPLS Labels are disabled
  AIGP attribute send and receive for IPv6 Unicast are disabled
  AIGP attribute send and receive for IPv6 with MPLS Labels are disabled
  BGP session driven failover for IPv6 Unicast is disabled
  BGP session driven failover for IPv4 Unicast is disabled
  Message Statistics:
                                  Sent      Rcvd
    Opens:                           1         1
    Notifications:                   0         0
    Updates:                         5        10
    Keepalives:                     41        41
    Enhanced Route Refresh:          0         0
    Begin of Route Refresh:          0         0
    End of Route Refresh:            0         0
    Total messages:                 47        52
  Prefix Statistics:
                                   Sent      Rcvd     Best Paths     Best ECMP Paths
    IPv4 Unicast:                    19         7              6                   6
    IPv6 Unicast:                     0         0              0                   0
  Configured maximum total number of routes is 256000, warning limit is 204800
  Inbound updates dropped by reason:
    AS path loop detection: 5
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
Local AS is 65001, local router ID 10.255.255.1
TTL is 1
Local TCP address is 10.1.1.12, local port is 179
Remote TCP address is 10.1.1.13, remote port is 35113
Local next hop for next hop self:
  IPv4 Unicast: 10.1.1.12
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
    Round-trip Time (rtt/rtvar): 9.4ms/1.3ms
    Delayed Ack Timeout (ato): 40.0ms
    Congestion Window (cwnd): 10
    TCP Throughput: 77.75 Mbps
    Advertised Recv Window (rcv_space): 56362

BGP neighbor is 10.1.1.15, remote AS 65401, external link
  BGP version 4, remote router ID 10.255.4.2, VRF default
  Inherits configuration from and member of peer-group LEAVES
  Last read 00:00:29, last write 00:00:50
  Hold time is 180, keepalive interval is 60 seconds
  Configured hold time is 180, keepalive interval is 60 seconds
  Effective minimum hold time is 3 seconds
  Hold timer is active, time left: 00:02:31
  Keepalive timer is active, time left: 00:00:07
  Connect timer is inactive
  Idle-restart timer is inactive
  BGP state is Established, up for 00:33:53
  Number of transitions to established: 1
  Last state was OpenConfirm
  Last event was RecvUpdate
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
      Received 00:33:53
      Number of stale paths removed after graceful restart: 0
  AIGP attribute send and receive for IPv4 Unicast are disabled
  AIGP attribute send and receive for IPv4 with MPLS Labels are disabled
  AIGP attribute send and receive for IPv6 Unicast are disabled
  AIGP attribute send and receive for IPv6 with MPLS Labels are disabled
  BGP session driven failover for IPv6 Unicast is disabled
  BGP session driven failover for IPv4 Unicast is disabled
  Message Statistics:
                                  Sent      Rcvd
    Opens:                           1         1
    Notifications:                   0         0
    Updates:                         6         5
    Keepalives:                     40        41
    Enhanced Route Refresh:          0         0
    Begin of Route Refresh:          0         0
    End of Route Refresh:            0         0
    Total messages:                 47        47
  Prefix Statistics:
                                   Sent      Rcvd     Best Paths     Best ECMP Paths
    IPv4 Unicast:                    25         7              6                   0
    IPv6 Unicast:                     0         0              0                   0
  Configured maximum total number of routes is 256000, warning limit is 204800
  Inbound updates dropped by reason:
    AS path loop detection: 2
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
Local AS is 65001, local router ID 10.255.255.1
TTL is 1
Local TCP address is 10.1.1.14, local port is 179
Remote TCP address is 10.1.1.15, remote port is 40159
Local next hop for next hop self:
  IPv4 Unicast: 10.1.1.14
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
    Round-trip Time (rtt/rtvar): 9.7ms/1.0ms
    Delayed Ack Timeout (ato): 40.0ms
    Congestion Window (cwnd): 10
    TCP Throughput: 75.51 Mbps
    Advertised Recv Window (rcv_space): 56362

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
>C    10.1.1.0/31 [0 pref/0 metric] updated 00:34:01 ago
         via Ethernet1, directly connected
>C    10.1.1.2/31 [0 pref/0 metric] updated 00:34:01 ago
         via Ethernet2, directly connected
>C    10.1.1.4/31 [0 pref/0 metric] updated 00:34:01 ago
         via Ethernet3, directly connected
>C    10.1.1.6/31 [0 pref/0 metric] updated 00:34:01 ago
         via Ethernet4, directly connected
>C    10.1.1.8/31 [0 pref/0 metric] updated 00:33:56 ago
         via Ethernet7, directly connected
>C    10.1.1.10/31 [0 pref/0 metric] updated 00:33:58 ago
         via Ethernet8, directly connected
>C    10.1.1.12/31 [0 pref/0 metric] updated 00:33:57 ago
         via Ethernet9, directly connected
>C    10.1.1.14/31 [0 pref/0 metric] updated 00:33:56 ago
         via Ethernet10, directly connected
>C    10.255.255.1/32 [0 pref/0 metric] updated 00:35:45 ago
         via Loopback0, directly connected
>C    223.255.255.255/32 [0 pref/0 metric] updated 00:35:45 ago
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
>B    10.10.10.0/24 [200 pref/0 MED] updated 00:34:00 ago
         via 10.1.1.1 [0 pref/0 metric] type ipv4
            via 10.1.1.1, Ethernet1
         via 10.1.1.3 [0 pref/0 metric] type ipv4
            via 10.1.1.3, Ethernet2
>B    10.10.11.0/24 [200 pref/0 MED] updated 00:34:00 ago
         via 10.1.1.5 [0 pref/0 metric] type ipv4
            via 10.1.1.5, Ethernet3
         via 10.1.1.7 [0 pref/0 metric] type ipv4
            via 10.1.1.7, Ethernet4
>B    10.10.12.0/24 [200 pref/0 MED] updated 00:33:56 ago
         via 10.1.1.11 [0 pref/0 metric] type ipv4
            via 10.1.1.11, Ethernet8
         via 10.1.1.9 [0 pref/0 metric] type ipv4
            via 10.1.1.9, Ethernet7
>B    10.10.13.0/24 [200 pref/0 MED] updated 00:33:55 ago
         via 10.1.1.13 [0 pref/0 metric] type ipv4
            via 10.1.1.13, Ethernet9
         via 10.1.1.15 [0 pref/0 metric] type ipv4
            via 10.1.1.15, Ethernet10
>B    10.20.20.0/24 [200 pref/0 MED] updated 00:34:00 ago
         via 10.1.1.1 [0 pref/0 metric] type ipv4
            via 10.1.1.1, Ethernet1
         via 10.1.1.3 [0 pref/0 metric] type ipv4
            via 10.1.1.3, Ethernet2
>B    10.20.21.0/24 [200 pref/0 MED] updated 00:34:00 ago
         via 10.1.1.5 [0 pref/0 metric] type ipv4
            via 10.1.1.5, Ethernet3
         via 10.1.1.7 [0 pref/0 metric] type ipv4
            via 10.1.1.7, Ethernet4
>B    10.20.22.0/24 [200 pref/0 MED] updated 00:33:56 ago
         via 10.1.1.11 [0 pref/0 metric] type ipv4
            via 10.1.1.11, Ethernet8
         via 10.1.1.9 [0 pref/0 metric] type ipv4
            via 10.1.1.9, Ethernet7
>B    10.20.23.0/24 [200 pref/0 MED] updated 00:33:55 ago
         via 10.1.1.13 [0 pref/0 metric] type ipv4
            via 10.1.1.13, Ethernet9
         via 10.1.1.15 [0 pref/0 metric] type ipv4
            via 10.1.1.15, Ethernet10
>B    10.30.30.0/24 [200 pref/0 MED] updated 00:34:00 ago
         via 10.1.1.1 [0 pref/0 metric] type ipv4
            via 10.1.1.1, Ethernet1
         via 10.1.1.3 [0 pref/0 metric] type ipv4
            via 10.1.1.3, Ethernet2
>B    10.30.31.0/24 [200 pref/0 MED] updated 00:34:00 ago
         via 10.1.1.5 [0 pref/0 metric] type ipv4
            via 10.1.1.5, Ethernet3
         via 10.1.1.7 [0 pref/0 metric] type ipv4
            via 10.1.1.7, Ethernet4
>B    10.30.32.0/24 [200 pref/0 MED] updated 00:33:56 ago
         via 10.1.1.11 [0 pref/0 metric] type ipv4
            via 10.1.1.11, Ethernet8
         via 10.1.1.9 [0 pref/0 metric] type ipv4
            via 10.1.1.9, Ethernet7
>B    10.30.33.0/24 [200 pref/0 MED] updated 00:33:55 ago
         via 10.1.1.13 [0 pref/0 metric] type ipv4
            via 10.1.1.13, Ethernet9
         via 10.1.1.15 [0 pref/0 metric] type ipv4
            via 10.1.1.15, Ethernet10
>B    10.40.40.0/24 [200 pref/0 MED] updated 00:34:00 ago
         via 10.1.1.1 [0 pref/0 metric] type ipv4
            via 10.1.1.1, Ethernet1
         via 10.1.1.3 [0 pref/0 metric] type ipv4
            via 10.1.1.3, Ethernet2
>B    10.40.41.0/24 [200 pref/0 MED] updated 00:34:00 ago
         via 10.1.1.5 [0 pref/0 metric] type ipv4
            via 10.1.1.5, Ethernet3
         via 10.1.1.7 [0 pref/0 metric] type ipv4
            via 10.1.1.7, Ethernet4
>B    10.40.42.0/24 [200 pref/0 MED] updated 00:33:56 ago
         via 10.1.1.11 [0 pref/0 metric] type ipv4
            via 10.1.1.11, Ethernet8
         via 10.1.1.9 [0 pref/0 metric] type ipv4
            via 10.1.1.9, Ethernet7
>B    10.40.43.0/24 [200 pref/0 MED] updated 00:33:55 ago
         via 10.1.1.13 [0 pref/0 metric] type ipv4
            via 10.1.1.13, Ethernet9
         via 10.1.1.15 [0 pref/0 metric] type ipv4
            via 10.1.1.15, Ethernet10
>B    10.255.1.1/32 [200 pref/0 MED] updated 00:34:00 ago
         via 10.1.1.1 [0 pref/0 metric] type ipv4
            via 10.1.1.1, Ethernet1
         via 10.1.1.3 [0 pref/0 metric] type ipv4
            via 10.1.1.3, Ethernet2
>B    10.255.1.2/32 [200 pref/0 MED] updated 00:34:00 ago
         via 10.1.1.1 [0 pref/0 metric] type ipv4
            via 10.1.1.1, Ethernet1
         via 10.1.1.3 [0 pref/0 metric] type ipv4
            via 10.1.1.3, Ethernet2
>B    10.255.2.1/32 [200 pref/0 MED] updated 00:34:00 ago
         via 10.1.1.5 [0 pref/0 metric] type ipv4
            via 10.1.1.5, Ethernet3
         via 10.1.1.7 [0 pref/0 metric] type ipv4
            via 10.1.1.7, Ethernet4
>B    10.255.2.2/32 [200 pref/0 MED] updated 00:34:00 ago
         via 10.1.1.5 [0 pref/0 metric] type ipv4
            via 10.1.1.5, Ethernet3
         via 10.1.1.7 [0 pref/0 metric] type ipv4
            via 10.1.1.7, Ethernet4
>B    10.255.3.1/32 [200 pref/0 MED] updated 00:33:56 ago
         via 10.1.1.11 [0 pref/0 metric] type ipv4
            via 10.1.1.11, Ethernet8
         via 10.1.1.9 [0 pref/0 metric] type ipv4
            via 10.1.1.9, Ethernet7
>B    10.255.3.2/32 [200 pref/0 MED] updated 00:33:56 ago
         via 10.1.1.11 [0 pref/0 metric] type ipv4
            via 10.1.1.11, Ethernet8
         via 10.1.1.9 [0 pref/0 metric] type ipv4
            via 10.1.1.9, Ethernet7
>B    10.255.4.1/32 [200 pref/0 MED] updated 00:33:55 ago
         via 10.1.1.13 [0 pref/0 metric] type ipv4
            via 10.1.1.13, Ethernet9
         via 10.1.1.15 [0 pref/0 metric] type ipv4
            via 10.1.1.15, Ethernet10
>B    10.255.4.2/32 [200 pref/0 MED] updated 00:33:55 ago
         via 10.1.1.13 [0 pref/0 metric] type ipv4
            via 10.1.1.13, Ethernet9
         via 10.1.1.15 [0 pref/0 metric] type ipv4
            via 10.1.1.15, Ethernet10
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
>P    0.0.0.0/8 [1 pref/0 metric] updated 00:35:42 ago
         via Null0, directly connected [NF]
>P    127.0.0.0/8 [1 pref/0 metric] updated 00:35:42 ago
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
>P    ::/96 [1 pref/0 metric] updated 00:35:43 ago
         via Null0, directly connected [NF]
>P    ::ffff:127.0.0.0/104 [1 pref/0 metric] updated 00:35:43 ago
         via :: [1 pref/1 metric] type ipv6
            via , directly connected
>P    fe80::/10 [1 pref/0 metric] updated 00:35:43 ago
```

## 

```text
```

## 

```text
```

## 

```text
```

