# Test results for PE32-J2-172

## show version

```text
Arista DCS-7280SR3-48YC8-F
Hardware version: 12.01
Serial number: JPE21210788
Hardware MAC address: 2cdd.e996.3abb
System MAC address: 2cdd.e996.3abb

Software image version: 4.31.2F
Architecture: i686
Internal build version: 4.31.2F-35442146.4312F
Internal build ID: 635a071a-386e-447f-942c-bcc34d9ffd3c
Image format version: 3.0
Image optimization: Default

Uptime: 1 day, 22 hours and 15 minutes
Total memory: 8099732 kB
Free memory: 5581436 kB

```

## show mac address-table

```text
          Mac Address Table
------------------------------------------------------------------

Vlan    Mac Address       Type        Ports      Moves   Last Move
----    -----------       ----        -----      -----   ---------
Total Mac Addresses for this criterion: 0

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
Ethernet5.2     20.111.172.172/24     up         up              1500          
Ethernet45      20.172.211.172/24     up         up              1500          
Loopback0       10.0.0.172/32         up         up             65535          
Management1     192.168.20.172/23     up         up              1500          

```

## show interfaces counters rates | nz

```text
Port      Name        Intvl  In Mbps      %  In Kpps Out Mbps      % Out Kpps
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

## show isis flex-algo path detail

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

 O        10.0.0.57/32 [110/11]
           via 20.172.211.211, Ethernet45
 O        10.0.0.147/32 [110/12]
           via 20.172.211.211, Ethernet45
 C        10.0.0.172/32
           directly connected, Loopback0
 O        10.0.0.211/32 [110/10]
           via 20.172.211.211, Ethernet45
 O        10.0.0.233/32 [110/11]
           via 20.172.211.211, Ethernet45
 O        10.0.1.43/32 [110/12]
           via 20.172.211.211, Ethernet45
 O        10.0.2.47/32 [110/12]
           via 20.172.211.211, Ethernet45
 O        20.5.211.0/24 [110/11]
           via 20.172.211.211, Ethernet45
 O        20.32.211.0/24 [110/11]
           via 20.172.211.211, Ethernet45
 O        20.47.211.0/24 [110/11]
           via 20.172.211.211, Ethernet45
 O        20.57.211.0/24 [110/11]
           via 20.172.211.211, Ethernet45
 O        20.111.211.0/24 [110/11]
           via 20.172.211.211, Ethernet45
 O        20.143.211.0/24 [110/11]
           via 20.172.211.211, Ethernet45
 C        20.172.211.0/24
           directly connected, Ethernet45
 O        20.211.233.0/24 [110/11]
           via 20.172.211.211, Ethernet45

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

 O        10.0.0.57/32 [110/11]
           via 20.172.211.211, Ethernet45
 O        10.0.0.147/32 [110/12]
           via 20.172.211.211, Ethernet45
 C        10.0.0.172/32
           directly connected, Loopback0
 O        10.0.0.211/32 [110/10]
           via 20.172.211.211, Ethernet45
 O        10.0.0.233/32 [110/11]
           via 20.172.211.211, Ethernet45
 O        10.0.1.43/32 [110/12]
           via 20.172.211.211, Ethernet45
 O        10.0.2.47/32 [110/12]
           via 20.172.211.211, Ethernet45
 O        20.5.211.0/24 [110/11]
           via 20.172.211.211, Ethernet45
 O        20.32.211.0/24 [110/11]
           via 20.172.211.211, Ethernet45
 O        20.47.211.0/24 [110/11]
           via 20.172.211.211, Ethernet45
 O        20.57.211.0/24 [110/11]
           via 20.172.211.211, Ethernet45
 O        20.111.211.0/24 [110/11]
           via 20.172.211.211, Ethernet45
 O        20.143.211.0/24 [110/11]
           via 20.172.211.211, Ethernet45
 C        20.172.211.0/24
           directly connected, Ethernet45
 O        20.211.233.0/24 [110/11]
           via 20.172.211.211, Ethernet45


VRF: OSPF-SR-L3VPN
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

 B I      20.57.112.0/24 [200/0]
           via 10.0.0.57/32, OSPF SR tunnel index 7, label 524285
              via 20.172.211.211, Ethernet45, label 20057
 B I      20.111.143.0/24 [200/0]
           via 10.0.1.43/32, OSPF SR tunnel index 3, label 24001
              via 20.172.211.211, Ethernet45, label 20343
 C        20.111.172.0/24
           directly connected, Ethernet5.2
 B I      20.111.233.0/24 [200/0]
           via 10.0.0.233/32, OSPF SR tunnel index 5, label 17
              via 20.172.211.211, Ethernet45, label 20233


VRF: mgmt
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
           via 192.168.20.1, Management1

 C        192.168.20.0/23
           directly connected, Management1

! IP routing not enabled
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


```

## show mpls route

```text
MPLS forwarding table (Label [metric] Vias) - 7 routes 
MPLS next-hop resolution allow default route: False
Metric Codes:
          A - Active metric
Via Type Codes:
          M - MPLS via, P - Pseudowire via,
          I - IP lookup via, V - VLAN via,
          VA - EVPN VLAN aware via, ES - EVPN ethernet segment via,
          VF - EVPN VLAN flood via, AF - EVPN VLAN aware flood via,
          NG - Nexthop group via

 20047   A[1]
                via M, forward
                    EgressACL: apply
                    20.172.211.211 Ethernet45
 20057   A[1]
                via M, forward
                    EgressACL: apply
                    20.172.211.211 Ethernet45
 20211   A[1]
                via M, pop
                    EgressACL: apply
                    20.172.211.211 Ethernet45
 20233   A[1]
                via M, forward
                    EgressACL: apply
                    20.172.211.211 Ethernet45
 20343   A[1]
                via M, forward
                    EgressACL: apply
                    20.172.211.211 Ethernet45
 362144  A[1]
                via M, 20.172.211.211, pop
                    EgressACL: apply
                    directly connected, Ethernet45
                    ac:78:d1:2c:d7:38, vlan 1006
 378534   [0]
                via I, ipv4, vrf OSPF-SR-L3VPN
```

## show mpls lfib route

```text
MPLS forwarding table (Label [metric] Vias) - 7 routes 
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

 OP    20047    [1], 10.0.0.147/32
                via M, 20.172.211.211, forward
                 payload autoDecide, ttlMode uniform, dscpMode uniform, apply egress-acl
                 interface Ethernet45
 OP    20057    [1], 10.0.0.57/32
                via M, 20.172.211.211, forward
                 payload autoDecide, ttlMode uniform, dscpMode uniform, apply egress-acl
                 interface Ethernet45
 OP    20211    [1], 10.0.0.211/32
                via M, 20.172.211.211, pop
                 payload autoDecide, ttlMode uniform, dscpMode uniform, apply egress-acl
                 interface Ethernet45
 OP    20233    [1], 10.0.0.233/32
                via M, 20.172.211.211, forward
                 payload autoDecide, ttlMode uniform, dscpMode uniform, apply egress-acl
                 interface Ethernet45
 OP    20343    [1], 10.0.1.43/32
                via M, 20.172.211.211, forward
                 payload autoDecide, ttlMode uniform, dscpMode uniform, apply egress-acl
                 interface Ethernet45
 OA    362144   [1]
                via M, 20.172.211.211, pop
                 payload autoDecide, ttlMode uniform, apply egress-acl
                 interface Ethernet45
 B3    378534   [0]
                via I, ipv4, vrf OSPF-SR-L3VPN
```

## show ip ospf segment-routing

```text
OSPF Instance ID: 1
SR supported Data-plane: MPLS			SR Router ID: 10.0.0.172
SR Global Block( SRGB ): Base: 20000           	Size: 2000            

OSPF Reachability Algorithm : SPF (0)

Number of OSPF segment routing capable nodes excluding self: 6

Self-Originated Segment Statistics:
Node-Segments       : 1
Prefix-Segments     : 0
Proxy-Node-Segments : 0
Adjacency Segments  : 1

```

## show ip ospf segment-routing global-blocks

```text
OSPF Instance ID: 1
SR supported Data-plane: MPLS			SR Router ID: 10.0.0.172
Number of OSPF segment routing capable nodes excluding self: 6

    Router ID        Base    Size
---------------- ----------- ----
   10.0.0.172       20000    2000
    10.0.0.19       16000    8001
    10.0.0.47       20000    2000
    10.0.0.57       20000    2000
   10.0.0.211       20000    2000
   10.0.0.233       20000    2000
    10.0.1.43       20000    2000

```

## show ip ospf segment-routing bindings

```text
10.0.0.57/32
   Local binding:  Label: 20057
   Remote binding: Peer ID: 10.0.0.211, Label: 20057
10.0.0.147/32
   Local binding:  Label: 20047
   Remote binding: Peer ID: 10.0.0.211, Label: 20047
10.0.0.172/32
   Local binding:  Label: imp-null
   Remote binding: Peer ID: 10.0.0.211, Label: 20172
10.0.0.211/32
   Local binding:  Label: 20211
   Remote binding: Peer ID: 10.0.0.211, Label: imp-null
10.0.0.233/32
   Local binding:  Label: 20233
   Remote binding: Peer ID: 10.0.0.211, Label: 20233
10.0.1.43/32
   Local binding:  Label: 20343
   Remote binding: Peer ID: 10.0.0.211, Label: 20343
```

## show bgp evpn

```text
BGP routing table information for VRF default
Router identifier 10.0.0.172, local AS number 65000
Route status codes: * - valid, > - active, S - Stale, E - ECMP head, e - ECMP
                    c - Contributing to ECMP, % - Pending best path selection
Origin codes: i - IGP, e - EGP, ? - incomplete
AS Path Attributes: Or-ID - Originator ID, C-LST - Cluster List, LL Nexthop - Link Local Nexthop

          Network                Next Hop              Metric  LocPref Weight  Path
```

## show bgp vpn-ipv4

```text
BGP routing table information for VRF default
Router identifier 10.0.0.172, local AS number 65000
Route status codes: s - suppressed contributor, * - valid, > - active, E - ECMP head, e - ECMP
                    S - Stale, c - Contributing to ECMP, b - backup, L - labeled-unicast
                    % - Pending best path selection
Origin codes: i - IGP, e - EGP, ? - incomplete
AS Path Attributes: Or-ID - Originator ID, C-LST - Cluster List, LL Nexthop - Link Local Nexthop

          Network                Next Hop              Metric  LocPref Weight  Path
 * >      RD: 10.0.0.57:1 IPv4 prefix 20.57.111.0/24
                                 10.0.0.57             -       100     0       i Or-ID: 10.0.0.57 C-LST: 10.0.0.211 
 * >      RD: 10.0.0.57:128 IPv4 prefix 20.57.111.0/24
                                 10.0.0.57             -       100     0       i Or-ID: 10.0.0.57 C-LST: 10.0.0.211 
 * >      RD: 10.0.0.57:129 IPv4 prefix 20.57.111.0/24
                                 10.0.0.57             -       100     0       i Or-ID: 10.0.0.57 C-LST: 10.0.0.211 
 * >      RD: 10.0.0.57:130 IPv4 prefix 20.57.111.0/24
                                 10.0.0.57             -       100     0       i Or-ID: 10.0.0.57 C-LST: 10.0.0.211 
 * >      RD: 10.0.0.57:131 IPv4 prefix 20.57.111.0/24
                                 10.0.0.57             -       100     0       i Or-ID: 10.0.0.57 C-LST: 10.0.0.211 
 * >      RD: 10.0.0.57:132 IPv4 prefix 20.57.111.0/24
                                 10.0.0.57             -       100     0       i Or-ID: 10.0.0.57 C-LST: 10.0.0.211 
 * >      RD: 10.0.0.57:2 IPv4 prefix 20.57.112.0/24
                                 10.0.0.57             -       100     0       i Or-ID: 10.0.0.57 C-LST: 10.0.0.211 
 * >      RD: 10.0.1.43:2 IPv4 prefix 20.111.143.0/24
                                 10.0.1.43             0       100     0       ? Or-ID: 10.0.1.43 C-LST: 10.0.0.211 
 * >      RD: 10.0.0.172:2 IPv4 prefix 20.111.172.0/24
                                 -                     -       -       0       i
 * >      RD: 10.0.0.233:52 IPv4 prefix 20.111.233.0/24
                                 10.0.0.233            -       100     0       i Or-ID: 10.0.0.233 C-LST: 10.0.0.211 
```

## show bgp vpn-ipv6

```text
BGP routing table information for VRF default
Router identifier 10.0.0.172, local AS number 65000
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
Router identifier 10.0.0.172, local AS number 65000
Route status codes: s - suppressed contributor, * - valid, > - active, E - ECMP head, e - ECMP
                    S - Stale, c - Contributing to ECMP, b - backup, L - labeled-unicast
                    % - Pending best path selection
Origin codes: i - IGP, e - EGP, ? - incomplete
AS Path Attributes: Or-ID - Originator ID, C-LST - Cluster List, LL Nexthop - Link Local Nexthop

          Network                Next Hop              Metric  AIGP       LocPref Weight  Path
```

## show bgp neighbors

```text
BGP neighbor is 10.0.0.211, remote AS 65000, internal link
  BGP version 4, remote router ID 10.0.0.211, VRF default
  Inherits configuration from and member of peer-group IBGP-PEER
  Last read 00:00:16, last write 00:00:22
  Hold time is 90, keepalive interval is 30 seconds
  Configured hold time is 180, keepalive interval is 60 seconds
  Effective minimum hold time is 3 seconds
  Send failure hold time is 0 seconds
  Hold timer is active, time left: 00:01:14
  Keepalive timer is active, time left: 00:00:03
  Connect timer is inactive
  Idle-restart timer is inactive
  BGP state is Established, up for 23:38:52
  Number of transitions to established: 1
  Last state was OpenConfirm
  Last event was RecvUpdate
  Last sent socket-error:Connect (Network is unreachable), Last time 23:38:59, First time 23:39:22, Repeats 5
  Types of communities advertised: standard extended large
  Neighbor Capabilities:
    Multiprotocol IPv4 Unicast: advertised
    Multiprotocol VPN-IPv4: advertised and received and negotiated
    Multiprotocol L2VPN EVPN: advertised
    Four Octet ASN: advertised and received and negotiated
    Route Refresh: advertised and received and negotiated
    Enhanced route refresh: advertised
    Send End-of-RIB messages: advertised and received and negotiated
    Additional-paths recv capability:
      IPv4 Unicast: advertised
      VPN-IPv4: advertised
      L2VPN EVPN: advertised
    Additional-paths send capability:
    Long Lived Graceful Restart received:
      Helper only
  Restart timer is inactive
  End of rib timer is inactive
    VPN-IPv4 End-of-RIB received: Yes
      Received 23:38:51
      Number of stale paths removed after graceful restart: 0
      Number of paths received before End-of-RIB: 2
  AIGP attribute send and receive for IPv4 Unicast are enabled
  AIGP attribute send and receive for IPv4 with MPLS Labels are enabled
  AIGP attribute send and receive for IPv6 Unicast are enabled
  AIGP attribute send and receive for IPv6 with MPLS Labels are enabled
  BGP session driven failover for IPv6 Unicast is disabled
  BGP session driven failover for IPv4 Unicast is disabled
  Message Statistics:
                         Sent      Rcvd
    Opens:                  1         1
    Notifications:          0         0
    Updates:                4       179
    Keepalives:          3336      3034
    Route Refresh:          0         0
    Total messages:      3341      3214
  Prefix Statistics:
                                   Sent      Rcvd     Best Paths     Best ECMP Paths
    IPv4 Unicast:                     0         0              0                   0
    VPN-IPv4:                         1         9              9                   0
    IPv6 Unicast:                     0         0              0                   0
  Configured maximum total number of routes is 0
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
    VPN-IPv4 NLRIs dropped due to maximum route limit violation: 0
    VPN-IPv6 NLRIs dropped due to route import match failure: 0
    L2VPN EVPN NLRIs dropped due to route import match failure: 0
    L2VPN EVPN NLRIs dropped due to unsupported route type: 0
    Link-state NLRIs dropped because reception is unsupported: 0
    RT Membership NLRIs dropped due to local origin ASN received from external peer: 0
  Outbound paths dropped by reason:
    IPv4 local address not available: 0
    IPv6 local address not available: 0
Local AS is 65000, local router ID 10.0.0.172
TTL is 255
Local TCP address is 10.0.0.172, local port is 46117
Remote TCP address is 10.0.0.211, remote port is 179
Local next hop for next hop self:
  VPN-IPv4: 10.0.0.172
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
    Window Scale (wscale): 0,7
    Retransmission Timeout (rto): 204.0ms
    Round-trip Time (rtt/rtvar): 0.4ms/0.0ms
    Delayed Ack Timeout (ato): 40.0ms
    Congestion Window (cwnd): 10
    TCP Throughput: 272.56 Mbps
    Recv Round-trip Time (rcv_rtt): 91363.8ms
    Advertised Recv Window (rcv_space): 64325

```

## show tunnel rib system-tunnel-rib brief

```text
Tunnel RIB: system-tunnel-rib
Endpoint      Tunnel Type Index(es) Tunnel Preference IGP Preference IGP Metric
------------- ----------- --------- ----------------- -------------- ----------
10.0.0.57/32  OSPF SR     7         60                110            11        
10.0.0.147/32 OSPF SR     11        60                110            12        
10.0.0.211/32 OSPF SR     4         60                110            10        
10.0.0.233/32 OSPF SR     5         60                110            11        
10.0.1.43/32  OSPF SR     3         60                110            12        

Metric Type
-----------
metric     
metric     
metric     
metric     
metric     

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
>C    10.0.0.172/32 [0 pref/0 metric] updated 1d00h ago
         via Loopback0, directly connected
>C    20.172.211.0/24 [0 pref/0 metric] updated 1d00h ago
         via Ethernet45, directly connected
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
>P    0.0.0.0/8 [1 pref/0 metric] updated 1d22h ago
         via Null0, directly connected [NF]
>P    127.0.0.0/8 [1 pref/0 metric] updated 1d22h ago
         via :: [1 pref/1 metric] type ipv4
            via , directly connected
VRF: default, Protocol: ospf
Codes: C - Connected, S - Static, P - Route Input, G - Gribi
       B - BGP, O - Ospf, O3 - Ospf3, I - Isis, R - Rip, VL - VRF Leak
       > - Best Route, * - Unresolved Next hop
       EM - Exact match of the SR-TE Policy
       NM - Null endpoint match of the SR-TE Policy
       AM - Any endpoint match of the SR-TE Policy
       L - Part of a recursive route resolution loop
       A - Next hop not resolved in ARP/ND
       NF - Not in FEC
>O    10.0.0.57/32 [110 pref/11 metric] updated 23:10:29 ago
         via 20.172.211.211, Ethernet45
>O    10.0.0.147/32 [110 pref/12 metric] updated 20:18:03 ago
         via 20.172.211.211, Ethernet45
>O    10.0.0.211/32 [110 pref/10 metric] updated 23:38:52 ago
         via 20.172.211.211, Ethernet45
>O    10.0.0.233/32 [110 pref/11 metric] updated 14:48:25 ago
         via 20.172.211.211, Ethernet45
>O    10.0.1.43/32 [110 pref/12 metric] updated 23:38:52 ago
         via 20.172.211.211, Ethernet45
>O    10.0.2.47/32 [110 pref/12 metric] updated 20:21:41 ago
         via 20.172.211.211, Ethernet45
>O    20.5.211.0/24 [110 pref/11 metric] updated 20:09:20 ago
         via 20.172.211.211, Ethernet45
>O    20.32.211.0/24 [110 pref/11 metric] updated 00:29:35 ago
         via 20.172.211.211, Ethernet45
>O    20.47.211.0/24 [110 pref/11 metric] updated 23:38:52 ago
         via 20.172.211.211, Ethernet45
>O    20.57.211.0/24 [110 pref/11 metric] updated 23:22:35 ago
         via 20.172.211.211, Ethernet45
>O    20.111.211.0/24 [110 pref/11 metric] updated 00:13:58 ago
         via 20.172.211.211, Ethernet45
>O    20.143.211.0/24 [110 pref/11 metric] updated 23:38:52 ago
         via 20.172.211.211, Ethernet45
>O    20.211.233.0/24 [110 pref/11 metric] updated 15:05:45 ago
         via 20.172.211.211, Ethernet45
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
>P    ::/96 [1 pref/0 metric] updated 23:07:42 ago
         via Null0, directly connected [NF]
>P    ::ffff:127.0.0.0/104 [1 pref/0 metric] updated 23:07:42 ago
         via :: [1 pref/1 metric] type ipv6
            via , directly connected
>P    fe80::/10 [1 pref/0 metric] updated 23:07:42 ago
```

## show platform sand l3 summary

```text
Number of vrfs: 3

Ipv4:
  Routes:       32  backlog:  0  unprogrammed:  0
  Adjacencies:  25  backlog:  0  unprogrammed:  0
Ipv6:
  Routes:       4   backlog:  0  unprogrammed:  0
  Adjacencies:  25  backlog:  0  unprogrammed:  0
Mpls:
  Routes:       6  backlog:  0  unprogrammed:  0
  Adjacencies:  1  backlog:  0  unprogrammed:  0

Jericho2 Ip Fecs:
  Non-ecmp fecs:  4110  ecmp fecs:  0  fec entries:  4110
Jericho2 Mpls Fecs:
  Non-ecmp fecs:  1  ecmp fecs:  0  fec entries:  1
Jericho2 Vxlan Tunnel Fecs:
  Non-ecmp fecs:  0  ecmp fecs:  0  fec entries:  0
  Number of vxlan tunnels configured: 0

Jericho2 Lpm Routes:
  Routes:   32  unprogrammed:   0   
  Routes6:  4   unprogrammed6:  0   
  Backlog:  0 

Jericho2 Lpm:
  TCAM entries used:   3  Percent free:  99  ADS2 entries used:   3  Percent free:  99
  Pivot buckets used:  4  Rows used:     1   Entries Per Bucket:  0  Percent free:  99
  Route buckets used:  7  Rows used:     2   Entries Per Bucket:  5  Percent free:  99

Lem:
  IPv4  Host in Lem:            disabled
  IPv4  Prefix-lengths in Lem:  None    
  IPv6  Host in Lem:            disabled
  IPv6  Prefix-lengths in Lem:  None    
  Number of downloads:        0
  Number of overflow events:  0

Egress Arp rewrite entries in use (in each fap):
  FixedSystem: 1
Egress Arp remote rewrite entries in use (in each fap):
  FixedSystem: 0
Egress Ip tunnel rewrite entries in use (in each fap):
  FixedSystem: 0
Egress Mpls (for outer 2 labels) rewrite entries in use (in each fap):
  FixedSystem: 0
Egress Mpls (for inner 2 labels) rewrite entries in use (in each fap):
  FixedSystem: 3
Egress Sflow rewrite entries in use (in each fap):
  FixedSystem: 0

Egress rewrite chains in backlog: resource-full 0, no-interface 0

Glem entries used per fap :
  FixedSystem: 4103

Jericho2 Fec:
  Maximum FEC hierarchy levels:  3
  ReusedEcmp:  0  allocs:  133  frees:  120  shuffles:  0  cmds:  0
  Zombies:     0    purges:    0
  Quarantine:  0/0  shuffles:  0  deletes:  0   
  Fec insertion failures:  0
  Level1  Fecs:
    Non-ecmp fecs:            3   ecmp fecs:            1 
    Non-ecmp (Percent free):  99  ecmp (Percent free):  99
  Level2  Fecs:
    Non-ecmp fecs:            9   ecmp fecs:            0  
    Non-ecmp (Percent free):  99  ecmp (Percent free):  100
  Level3  Fecs:
    Non-ecmp fecs:            1   ecmp fecs:            0  
    Non-ecmp (Percent free):  99  ecmp (Percent free):  100

Lpm Detail:
  Requests:  536  cleanses:  407  batches:  407  avg batch size:  1

Jericho Arp:
  ArpTable writes:      17348  queued      0   
  IngressTable writes:  46489  queued      0   
  Coprocessors:         1      in CmdRing

Tunnel Counter Status
  Number of MPLS tunnels:                  6    
  Number of uncountable MPLS tunnels:      6    
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
|0  |10.0.0.57/32      |ROUTE| Et45               |1006 |103421  | ac:78:d1:2c:d7:38 |  -  |288364|   -   
|0  |10.0.0.147/32     |ROUTE| Et45               |1006 |103421  | ac:78:d1:2c:d7:38 |  -  |288364|   -   
|0  |10.0.0.172/32     |TRAP | CoppSystemIpUcast  |0    |  -     | Receive           |  -  |524291|   -   
|0  |10.0.0.211/32     |ROUTE| Et45               |1006 |103421  | ac:78:d1:2c:d7:38 |  -  |288364|   -   
|0  |10.0.0.233/32     |ROUTE| Et45               |1006 |103421  | ac:78:d1:2c:d7:38 |  -  |288364|   -   
|0  |10.0.1.43/32      |ROUTE| Et45               |1006 |103421  | ac:78:d1:2c:d7:38 |  -  |288364|   -   
|0  |10.0.2.47/32      |ROUTE| Et45               |1006 |103421  | ac:78:d1:2c:d7:38 |  -  |288364|   -   
|0  |20.5.211.0/24     |ROUTE| Et45               |1006 |103421  | ac:78:d1:2c:d7:38 |  -  |288364|   -   
|0  |20.32.211.0/24    |ROUTE| Et45               |1006 |103421  | ac:78:d1:2c:d7:38 |  -  |288364|   -   
|0  |20.47.211.0/24    |ROUTE| Et45               |1006 |103421  | ac:78:d1:2c:d7:38 |  -  |288364|   -   
|0  |20.57.211.0/24    |ROUTE| Et45               |1006 |103421  | ac:78:d1:2c:d7:38 |  -  |288364|   -   
|0  |20.111.211.0/24   |ROUTE| Et45               |1006 |103421  | ac:78:d1:2c:d7:38 |  -  |288364|   -   
|0  |20.143.211.0/24   |ROUTE| Et45               |1006 |103421  | ac:78:d1:2c:d7:38 |  -  |288364|   -   
|0  |20.172.211.0/32   |TRAP | CoppSystemIpBcast  |0    |  -     | BcastReceive      |  -  |524288|   -   
|0  |20.172.211.172/32 |TRAP | CoppSystemIpUcast  |0    |  -     | Receive           |  -  |524291|   -   
|0  |20.172.211.211/32 |ROUTE| Et45               |1006 |103421  | ac:78:d1:2c:d7:38 |  -  |288361|   -   
|0  |20.172.211.255/32 |TRAP | CoppSystemIpBcast  |0    |  -     | BcastReceive      |  -  |524288|   -   
|0  |20.172.211.0/24   |TRAP | CoppSystemL3DstMiss|1006 |1006    | ArpTrap           |  -  |525300|   -   
|0  |20.211.233.0/24   |ROUTE| Et45               |1006 |103421  | ac:78:d1:2c:d7:38 |  -  |288364|   -   
|0  |127.0.0.0/8       |TRAP | CoppSystemL3DstMiss|0    |  -     | ArpTrap           |  -  |524294|   -   
|0  |0.0.0.0/0         |TRAP | CoppSystemL3LpmOver|0    |  -     | SlowReceive       |  -  |524292|   -   
|8  |0.0.0.0/8         |DROP | DROP               |0    |  -     |                   |  -  |288362|   -   
|8  |20.57.112.0/24    |ROUTE| FEC 288367         |0    |2097141 | 00:00:00:00:00:00 |  -  |91756 |M 524285
|8  |20.111.143.0/24   |ROUTE| FEC 288365         |0    |2097143 | 00:00:00:00:00:00 |  -  |91752 |M 24001
|8  |20.111.172.0/32   |TRAP | CoppSystemIpBcast  |0    |  -     | BcastReceive      |  -  |524288|   -   
|8  |20.111.172.172/32 |TRAP | CoppSystemIpUcast  |0    |  -     | Receive           |  -  |524291|   -   
|8  |20.111.172.255/32 |TRAP | CoppSystemIpBcast  |0    |  -     | BcastReceive      |  -  |524288|   -   
|8  |20.111.172.0/24   |TRAP | CoppSystemL3DstMiss|1007 |1007    | ArpTrap           |  -  |525301|   -   
|8  |20.111.233.0/24   |ROUTE| FEC 288368         |0    |2097147 | 00:00:00:00:00:00 |  -  |91753 |M 17
|8  |127.0.0.0/8       |TRAP | CoppSystemL3DstMiss|0    |  -     | ArpTrap           |  -  |524294|   -   
|8  |0.0.0.0/0         |TRAP | CoppSystemL3LpmOver|0    |  -     | SlowReceive       |  -  |524292|   -   

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
|  -  |91752 |ROUTE| FEC 288365         |   - |2097143 |                 - |Mpush 24001
|  -  |91753 |ROUTE| FEC 288368         |   - |2097147 |                 - |Mpush 17
|  -  |91756 |ROUTE| FEC 288367         |   - |2097141 |                 - |Mpush 524285
|  -  |288360|DROP | DROP               |0    |  -     |                   |   -   
|  -  |288361|ROUTE| Et45               |1006 |103421  | ac:78:d1:2c:d7:38 |   -   
|  -  |288362|DROP | DROP               |0    |  -     |                   |   -   
|  -  |288363|ROUTE| Et45               |1006 |103421  | ac:78:d1:2c:d7:38 |   -   
|  -  |288364|ROUTE| Et45               |1006 |103421  | ac:78:d1:2c:d7:38 |   -   
|  -  |288365|ROUTE| FEC 528482         |   - |2097144 |                 - |Mpush 20343
|  -  |288367|ROUTE| FEC 528482         |   - |2097142 |                 - |Mpush 20057
|  -  |288368|ROUTE| FEC 528482         |   - |2097148 |                 - |Mpush 20233
|  -  |288370|DROP | DROP               |0    |  -     |                   |   -   
|  -  |524288|TRAP | CoppSystemIpBcast  |0    |  -     | BcastReceive      |   -   
|  -  |524291|TRAP | CoppSystemIpUcast  |0    |  -     | Receive           |   -   
|  -  |524292|TRAP | CoppSystemL3LpmOver|0    |  -     | SlowReceive       |   -   
|  -  |524294|TRAP | CoppSystemL3DstMiss|0    |  -     | ArpTrap           |   -   
|  -  |525300|TRAP | CoppSystemL3DstMiss|1006 |1006    | ArpTrap           |   -   
|  -  |525301|TRAP | CoppSystemL3DstMiss|1007 |1007    | ArpTrap           |   -   
|  -  |528482|ROUTE| Et45               |1006 |103421  | ac:78:d1:2c:d7:38 |   -   

```

