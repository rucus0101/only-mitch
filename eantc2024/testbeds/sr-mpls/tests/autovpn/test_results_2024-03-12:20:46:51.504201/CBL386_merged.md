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

Uptime: 5 hours and 47 minutes
Total memory: 32470188 kB
Free memory: 21210132 kB

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
Ethernet1/7      172.16.0.1/31        up         up              1500          
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
 O        10.0.255.2/31 [110/20]
           via 10.0.255.1, Ethernet1/5
 B I      10.1.255.0/31 [20/0]
           via VTEP 10.255.255.1 VNI 201 router-mac ec:8a:48:04:f5:30
 B I      10.2.255.0/31 [20/0]
           via VTEP 10.255.255.4 VNI 201 router-mac ec:8a:48:04:ff:5b
 B I      10.4.255.0/31 [20/0]
           via VTEP 10.255.255.4 VNI 201 router-mac ec:8a:48:04:ff:5b
 B I      10.4.255.2/31 [20/0]
           via VTEP 10.255.255.4 VNI 201 router-mac ec:8a:48:04:ff:5b
 B I      10.5.255.0/31 [20/0]
           via VTEP 10.255.255.4 VNI 201 router-mac ec:8a:48:04:ff:5b
 B I      10.5.255.2/31 [20/0]
           via VTEP 10.255.255.4 VNI 201 router-mac ec:8a:48:04:ff:5b
 B I      10.6.255.0/31 [20/0]
           via VTEP 10.255.255.12 VNI 201 router-mac 00:0c:29:78:c5:2d
 B I      10.6.255.2/31 [20/0]
           via VTEP 10.255.255.12 VNI 201 router-mac 00:0c:29:78:c5:2d
 O        10.255.254.1/32 [110/20]
           via 10.0.255.1, Ethernet1/5
 B I      10.255.254.2/32 [20/0]
           via VTEP 10.255.255.1 VNI 201 router-mac ec:8a:48:04:f5:30
 B I      10.255.254.3/32 [20/0]
           via VTEP 10.255.255.4 VNI 201 router-mac ec:8a:48:04:ff:5b
 B I      10.255.254.4/32 [20/0]
           via VTEP 10.255.255.12 VNI 201 router-mac 00:0c:29:78:c5:2d
 B I      10.255.254.5/32 [20/0]
           via VTEP 10.255.255.4 VNI 201 router-mac ec:8a:48:04:ff:5b
 B I      10.255.254.6/32 [20/0]
           via VTEP 10.255.255.4 VNI 201 router-mac ec:8a:48:04:ff:5b
 B I      172.16.255.0/31 [20/0]
           via VTEP 10.255.255.4 VNI 201 router-mac ec:8a:48:04:ff:5b
 O        192.168.0.0/24 [110/20]
           via 10.0.255.1, Ethernet1/5
 B I      192.168.1.0/24 [20/0]
           via VTEP 10.255.255.1 VNI 201 router-mac ec:8a:48:04:f5:30
 B I      192.168.3.0/24 [20/0]
           via VTEP 10.255.255.4 VNI 201 router-mac ec:8a:48:04:ff:5b
 B I      192.168.4.0/24 [20/0]
           via VTEP 10.255.255.4 VNI 201 router-mac ec:8a:48:04:ff:5b
 B I      192.168.5.0/24 [20/0]
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
 * >      RD: 10.255.255.5:1 ip-prefix 10.0.255.2/31
                                 -                     -       -       0       i
 * >Ec    RD: 10.255.255.1:1 ip-prefix 10.1.255.0/31
                                 10.255.255.1          -       100     0       i
 *  ec    RD: 10.255.255.1:1 ip-prefix 10.1.255.0/31
                                 10.255.255.1          -       100     0       i Or-ID: 10.255.255.1 C-LST: 10.255.255.4 
 * >Ec    RD: 10.255.255.4:1 ip-prefix 10.2.255.0/31
                                 10.255.255.4          -       100     0       i
 *  ec    RD: 10.255.255.4:1 ip-prefix 10.2.255.0/31
                                 10.255.255.4          -       100     0       i Or-ID: 10.255.255.4 C-LST: 10.255.255.1 10.255.255.4 10.5.255.0 
 * >Ec    RD: 10.255.255.4:1 ip-prefix 10.4.255.0/31
                                 10.255.255.4          -       100     0       i
 *  ec    RD: 10.255.255.4:1 ip-prefix 10.4.255.0/31
                                 10.255.255.4          -       100     0       i Or-ID: 10.255.255.4 C-LST: 10.255.255.1 10.255.255.4 10.5.255.0 
 * >Ec    RD: 10.255.255.4:1 ip-prefix 10.4.255.2/31
                                 10.255.255.4          -       100     0       i
 *  ec    RD: 10.255.255.4:1 ip-prefix 10.4.255.2/31
                                 10.255.255.4          -       100     0       i Or-ID: 10.255.255.4 C-LST: 10.255.255.1 10.255.255.4 10.5.255.0 
 * >Ec    RD: 10.255.255.4:1 ip-prefix 10.5.255.0/31
                                 10.255.255.4          -       100     0       i
 *  ec    RD: 10.255.255.4:1 ip-prefix 10.5.255.0/31
                                 10.255.255.4          -       100     0       i Or-ID: 10.255.255.4 C-LST: 10.255.255.1 10.255.255.4 
 * >Ec    RD: 10.255.255.4:1 ip-prefix 10.5.255.2/31
                                 10.255.255.4          -       100     0       i
 *  ec    RD: 10.255.255.4:1 ip-prefix 10.5.255.2/31
                                 10.255.255.4          -       100     0       i Or-ID: 10.255.255.4 C-LST: 10.255.255.1 
 * >Ec    RD: 10.255.255.12:1 ip-prefix 10.6.255.0/31
                                 10.255.255.12         -       100     0       i Or-ID: 10.255.255.12 C-LST: 10.255.255.4 
 *  ec    RD: 10.255.255.12:1 ip-prefix 10.6.255.0/31
                                 10.255.255.12         -       100     0       i Or-ID: 10.255.255.12 C-LST: 10.255.255.1 
 * >Ec    RD: 10.255.255.12:1 ip-prefix 10.6.255.2/31
                                 10.255.255.12         -       100     0       i Or-ID: 10.255.255.12 C-LST: 10.255.255.4 
 *  ec    RD: 10.255.255.12:1 ip-prefix 10.6.255.2/31
                                 10.255.255.12         -       100     0       i Or-ID: 10.255.255.12 C-LST: 10.255.255.1 
 * >      RD: 10.255.255.5:1 ip-prefix 10.255.254.1/32
                                 -                     -       -       0       i
 * >Ec    RD: 10.255.255.1:1 ip-prefix 10.255.254.2/32
                                 10.255.255.1          -       100     0       i
 *  ec    RD: 10.255.255.1:1 ip-prefix 10.255.254.2/32
                                 10.255.255.1          -       100     0       i Or-ID: 10.255.255.1 C-LST: 10.255.255.4 
 * >Ec    RD: 10.255.255.4:1 ip-prefix 10.255.254.3/32
                                 10.255.255.4          -       100     0       i
 *  ec    RD: 10.255.255.4:1 ip-prefix 10.255.254.3/32
                                 10.255.255.4          -       100     0       i Or-ID: 10.255.255.4 C-LST: 10.255.255.1 10.255.255.4 10.5.255.0 
 * >Ec    RD: 10.255.255.12:1 ip-prefix 10.255.254.4/32
                                 10.255.255.12         -       100     0       i Or-ID: 10.255.255.12 C-LST: 10.255.255.4 
 *  ec    RD: 10.255.255.12:1 ip-prefix 10.255.254.4/32
                                 10.255.255.12         -       100     0       i Or-ID: 10.255.255.12 C-LST: 10.255.255.1 
 * >Ec    RD: 10.255.255.4:1 ip-prefix 10.255.254.5/32
                                 10.255.255.4          -       100     0       i
 *  ec    RD: 10.255.255.4:1 ip-prefix 10.255.254.5/32
                                 10.255.255.4          -       100     0       i Or-ID: 10.255.255.4 C-LST: 10.255.255.1 10.255.255.4 10.5.255.0 
 * >Ec    RD: 10.255.255.4:1 ip-prefix 10.255.254.6/32
                                 10.255.255.4          -       100     0       i
 *  ec    RD: 10.255.255.4:1 ip-prefix 10.255.254.6/32
                                 10.255.255.4          -       100     0       i Or-ID: 10.255.255.4 C-LST: 10.255.255.1 10.255.255.4 
 * >Ec    RD: 10.255.255.4:1 ip-prefix 172.16.255.0/31
                                 10.255.255.4          -       100     0       i
 *  ec    RD: 10.255.255.4:1 ip-prefix 172.16.255.0/31
                                 10.255.255.4          -       100     0       i Or-ID: 10.255.255.4 C-LST: 10.255.255.1 
 * >      RD: 10.255.255.5:1 ip-prefix 192.168.0.0/24
                                 -                     -       -       0       i
 * >Ec    RD: 10.255.255.1:1 ip-prefix 192.168.1.0/24
                                 10.255.255.1          -       100     0       i
 *  ec    RD: 10.255.255.1:1 ip-prefix 192.168.1.0/24
                                 10.255.255.1          -       100     0       i Or-ID: 10.255.255.1 C-LST: 10.255.255.4 
 * >Ec    RD: 10.255.255.4:1 ip-prefix 192.168.3.0/24
                                 10.255.255.4          -       100     0       i
 *  ec    RD: 10.255.255.4:1 ip-prefix 192.168.3.0/24
                                 10.255.255.4          -       100     0       i Or-ID: 10.255.255.4 C-LST: 10.255.255.1 10.255.255.4 10.5.255.0 
 * >Ec    RD: 10.255.255.4:1 ip-prefix 192.168.4.0/24
                                 10.255.255.4          -       100     0       i
 *  ec    RD: 10.255.255.4:1 ip-prefix 192.168.4.0/24
                                 10.255.255.4          -       100     0       i Or-ID: 10.255.255.4 C-LST: 10.255.255.1 10.255.255.4 10.5.255.0 
 * >Ec    RD: 10.255.255.4:1 ip-prefix 192.168.5.0/24
                                 10.255.255.4          -       100     0       i
 *  ec    RD: 10.255.255.4:1 ip-prefix 192.168.5.0/24
                                 10.255.255.4          -       100     0       i Or-ID: 10.255.255.4 C-LST: 10.255.255.1 10.255.255.4 
```

## show ip security connection detail

```text
path1:
  Source address: 172.16.0.1, Destination address: 172.16.0.4
  State: established
  Uptime: 5 hours, 5 minutes, 38 seconds
  VRF: default
  Type: static
  Remote IP: 10.255.255.4
  Role: responder
  Inbound SPI: 0xcdf3e5:
    Request ID: 2, Mode: transport, Replay window size: 16384, Seq: 0x0
    Errors:
      Packets outside replay window: 0, Replay: 0, Integrity failed: 0
    Lifetime config:
      Soft byte limit: 4117000668749, Hard byte limit: 6442450944000
      Soft packet limit: 2242214249, Hard packet limit: 4000000000
      Soft time limit: 2802 secs, Hard time limit: 3600 secs
    Lifetime current:
      Current bytes: 2358764
      Current packets: 7655
      SA add time: Tue Mar 12 13:08:07 2024
      SA last use time: Tue Mar 12 13:46:01 2024
  Outbound SPI: 0xc180cb:
    Request ID: 2, Mode: transport, Replay window size: 0, Seq: 0x0
    Errors:
      Packets outside replay window: 0, Replay: 0, Integrity failed: 0
    Lifetime config:
      Soft byte limit: 4175237387249, Hard byte limit: 6442450944000
      Soft packet limit: 2410241581, Hard packet limit: 4000000000
      Soft time limit: 2870 secs, Hard time limit: 3600 secs
    Lifetime current:
      Current bytes: 1730553
      Current packets: 15598
      SA add time: Tue Mar 12 13:08:07 2024
      SA last use time: Tue Mar 12 13:46:01 2024
path3:
  Source address: 172.16.0.1, Destination address: 172.16.0.3
  State: established
  Uptime: 5 hours, 44 minutes, 21 seconds
  VRF: default
  Type: dynamic
  Remote IP: 10.255.255.6
  Role: responder
  Packets in: 41308, Packets out: 85714
  Last known rekey count: 0
  Dynamic state: established
  Last established time: Tue Mar 12 13:27:14 2024
  DH crypto:
    Local rekey: 0, Peer rekey: 1, In SPI: 0xec6f556b, Out SPI: 0x256cc224
    Local rekey: 0, Peer rekey: 2, In SPI: 0x58f74821, Out SPI: 0xda0d440b
  DH state:
    Local rekey: 0, Peer rekey: 2, DH rekey state: not rekeying, Role: not rekeying
  SA crypto:
    Local rekey: 0, Peer rekey: 2, In SPI 0x9b554e93, Out SPI 0x3c9b467b
  SA rekey role: not rekeying
  SA state:
    SA type: egress , SPI: 0x9f556eeb
      Role: responder, SA rekey state: initial, Peer nonce type: init
      Add time: Tue Mar 12 13:25:58 2024, Packets: 5526, Pair SPI: 0x409b66d3
    SA type: ingress , SPI: 0x409b66d3
      Role: responder, SA rekey state: initial, Peer nonce type: init
      Add time: Tue Mar 12 13:25:50 2024, Packets: 2669, Pair SPI: 0x9f556eeb
  Inbound SPI: 0x409b66d3:
    Request ID: 3, Mode: transport, Replay window size: 0, Seq: 0x0
    Errors:
      Packets outside replay window: 0, Replay: 0, Integrity failed: 0
    Lifetime config:
      Soft byte limit: 4768111713675, Hard byte limit: 6442450944000
      Soft packet limit: 2990625303, Hard packet limit: 4000000000
      Soft time limit: 2662 secs, Hard time limit: 3600 secs
    Lifetime current:
      Current bytes: 1021916
      Current packets: 2675
      SA add time: Tue Mar 12 13:25:50 2024
      SA last use time: Tue Mar 12 13:46:01 2024
  Outbound SPI: 0x9f556eeb:
    Request ID: 3, Mode: transport, Replay window size: 0, Seq: 0x0
    Errors:
      Packets outside replay window: 0, Replay: 0, Integrity failed: 0
    Lifetime config:
      Soft byte limit: 4730550173325, Hard byte limit: 6442450944000
      Soft packet limit: 2999714741, Hard packet limit: 4000000000
      Soft time limit: 2542 secs, Hard time limit: 3600 secs
    Lifetime current:
      Current bytes: 844750
      Current packets: 5538
      SA add time: Tue Mar 12 13:25:58 2024
      SA last use time: Tue Mar 12 13:46:01 2024
path4:
  Source address: 172.16.0.1, Destination address: 172.16.0.7
  State: established
  Uptime: 5 hours, 39 minutes, 3 seconds
  VRF: default
  Type: static
  Remote IP: 10.255.255.4
  Role: responder
  Inbound SPI: 0xc011bf:
    Request ID: 1, Mode: transport, Replay window size: 16384, Seq: 0x0
    Errors:
      Packets outside replay window: 0, Replay: 0, Integrity failed: 0
    Lifetime config:
      Soft byte limit: 3820873234499, Hard byte limit: 6442450944000
      Soft packet limit: 2371453438, Hard packet limit: 4000000000
      Soft time limit: 2617 secs, Hard time limit: 3600 secs
    Lifetime current:
      Current bytes: 1783040
      Current packets: 5860
      SA add time: Tue Mar 12 13:17:14 2024
      SA last use time: Tue Mar 12 13:46:01 2024
  Outbound SPI: 0xc0124c:
    Request ID: 1, Mode: transport, Replay window size: 0, Seq: 0x0
    Errors:
      Packets outside replay window: 0, Replay: 0, Integrity failed: 0
    Lifetime config:
      Soft byte limit: 3648281387999, Hard byte limit: 6442450944000
      Soft packet limit: 2636460085, Hard packet limit: 4000000000
      Soft time limit: 2676 secs, Hard time limit: 3600 secs
    Lifetime current:
      Current bytes: 1438233
      Current packets: 12016
      SA add time: Tue Mar 12 13:17:14 2024
      SA last use time: Tue Mar 12 13:46:01 2024
path5:
  Source address: 172.16.0.1, Destination address: 172.16.0.9
  State: established
  Uptime: 4 hours, 48 minutes, 30 seconds
  VRF: default
  Type: dynamic
  Remote IP: 10.255.255.11
  Role: responder
  Packets in: 32083, Packets out: 68512
  Last known rekey count: 0
  Dynamic state: established
  Last established time: Tue Mar 12 13:18:14 2024
  DH crypto:
    Local rekey: 0, Peer rekey: 0, In SPI: 0x726f70d7, Out SPI: 0x9177baa3
  DH state:
    Local rekey: 0, Peer rekey: 0, DH rekey state: not rekeying, Role: not rekeying
  SA crypto:
    Local rekey: 0, Peer rekey: 0, In SPI 0xa7f0a9bf, Out SPI 0xe4df87d7
  SA rekey role: not rekeying
  SA state:
    SA type: egress , SPI: 0xb1f0c917
      Role: responder, SA rekey state: initial, Peer nonce type: init
      Add time: Tue Mar 12 13:16:53 2024, Packets: 7956, Pair SPI: 0xeedfa72f
    SA type: ingress , SPI: 0xeedfa72f
      Role: responder, SA rekey state: initial, Peer nonce type: init
      Add time: Tue Mar 12 13:16:52 2024, Packets: 3724, Pair SPI: 0xb1f0c917
  Inbound SPI: 0xeedfa72f:
    Request ID: 4, Mode: transport, Replay window size: 0, Seq: 0x0
    Errors:
      Packets outside replay window: 0, Replay: 0, Integrity failed: 0
    Lifetime config:
      Soft byte limit: 4733005385175, Hard byte limit: 6442450944000
      Soft packet limit: 2932448526, Hard packet limit: 4000000000
      Soft time limit: 2591 secs, Hard time limit: 3600 secs
    Lifetime current:
      Current bytes: 538632
      Current packets: 3730
      SA add time: Tue Mar 12 13:16:52 2024
      SA last use time: Tue Mar 12 13:46:01 2024
  Outbound SPI: 0xb1f0c917:
    Request ID: 4, Mode: transport, Replay window size: 0, Seq: 0x0
    Errors:
      Packets outside replay window: 0, Replay: 0, Integrity failed: 0
    Lifetime config:
      Soft byte limit: 4735255498275, Hard byte limit: 6442450944000
      Soft packet limit: 2917110778, Hard packet limit: 4000000000
      Soft time limit: 2687 secs, Hard time limit: 3600 secs
    Lifetime current:
      Current bytes: 1257960
      Current packets: 7968
      SA add time: Tue Mar 12 13:16:53 2024
      SA last use time: Tue Mar 12 13:46:01 2024
path6:
  Source address: 172.16.0.1, Destination address: 172.16.0.11
  State: established
  Uptime: 4 hours, 44 minutes, 3 seconds
  VRF: default
  Type: dynamic
  Remote IP: 10.255.255.12
  Role: initiator
  Packets in: 32836, Packets out: 68338
  Last known rekey count: 0
  Dynamic state: established
  Last established time: Tue Mar 12 13:26:14 2024
  DH crypto:
    Local rekey: 0, Peer rekey: 0, In SPI: 0x40fc3240, Out SPI: 0xc6671aa5
  DH state:
    Local rekey: 0, Peer rekey: 0, DH rekey state: not rekeying, Role: not rekeying
  SA crypto:
    Local rekey: 0, Peer rekey: 0, In SPI 0x82c8a808, Out SPI 0xf95cbd24
  SA rekey role: not rekeying
  SA state:
    SA type: egress , SPI: 0x8ec8c860
      Role: initiator, SA rekey state: initial, Peer nonce type: init
      Add time: Tue Mar 12 13:24:18 2024, Packets: 5838, Pair SPI: 0x55ddd7c
    SA type: ingress , SPI: 0x55ddd7c
      Role: initiator, SA rekey state: initial, Peer nonce type: init
      Add time: Tue Mar 12 13:24:10 2024, Packets: 2825, Pair SPI: 0x8ec8c860
  Inbound SPI: 0x55ddd7c:
    Request ID: 5, Mode: transport, Replay window size: 0, Seq: 0x0
    Errors:
      Packets outside replay window: 0, Replay: 0, Integrity failed: 0
    Lifetime config:
      Soft byte limit: 4676509148625, Hard byte limit: 6442450944000
      Soft packet limit: 2967004903, Hard packet limit: 4000000000
      Soft time limit: 2615 secs, Hard time limit: 3600 secs
    Lifetime current:
      Current bytes: 1039116
      Current packets: 2831
      SA add time: Tue Mar 12 13:24:10 2024
      SA last use time: Tue Mar 12 13:46:01 2024
  Outbound SPI: 0x8ec8c860:
    Request ID: 5, Mode: transport, Replay window size: 0, Seq: 0x0
    Errors:
      Packets outside replay window: 0, Replay: 0, Integrity failed: 0
    Lifetime config:
      Soft byte limit: 4800886239450, Hard byte limit: 6442450944000
      Soft packet limit: 2938851784, Hard packet limit: 4000000000
      Soft time limit: 2653 secs, Hard time limit: 3600 secs
    Lifetime current:
      Current bytes: 852822
      Current packets: 5850
      SA add time: Tue Mar 12 13:24:18 2024
      SA last use time: Tue Mar 12 13:46:01 2024
```

## show stun client translations detail

```text
Current System Time: Tue Mar 12 13:46:58 2024
Transaction ID 000000010affff0500000000
Agent Name: dps
Source Address: 172.16.0.1:4500
Public Address: 172.16.0.1:4500
Number of Attributes: 3
Timeout Interval: 0:03:00
Last Refreshed: 0:02:41 ago
Attribute Type   Length Value           
---------------- ------ ----------------
PATH_GROUP            6 VZ_OFF          
VTEP_IP               4 10.255.255.5    
WAN_ID                4 1               

```

## show stun server bindings detail

```text
Current System Time: Tue Mar 12 13:46:58 2024
```

## show path-selection paths detail

```text
Peer: 10.255.255.1, Path group VZ_OFF
Path name: path1, static, Label: 1
Source: 172.16.0.1, Port: 4500, WAN ID: 1
Destination: 172.16.0.4, Port: 4500, WAN ID: 2886729732
Local interface: Ethernet1/7
Route state: IPsec established
Traffic class 0: active (5:04:20)
MTU: 1414

Peer: 10.255.255.4, Path group VZ_OFF
Path name: path4, static, Label: 4
Source: 172.16.0.1, Port: 4500, WAN ID: 1
Destination: 172.16.0.7, Port: 4500, WAN ID: 2886729735
Local interface: Ethernet1/7
Route state: IPsec established
Traffic class 0: active (5:37:37)
MTU: 1414

Peer: 10.255.255.6, Path group VZ_OFF
Path name: path3, dynamic, Label: 3
Source: 172.16.0.1, Port: 4500, WAN ID: 1
Destination: 172.16.0.3, Port: 4500, WAN ID: 1
Local interface: Ethernet1/7
Route state: IPsec established
Traffic class 0: active (5:42:54)
MTU: 1414

Peer: 10.255.255.11, Path group VZ_OFF
Path name: path5, dynamic, Label: 5
Source: 172.16.0.1, Port: 4500, WAN ID: 1
Destination: 172.16.0.9, Port: 4500, WAN ID: 2
Local interface: Ethernet1/7
Route state: IPsec established
Traffic class 0: active (4:47:16)
MTU: 1414

Peer: 10.255.255.12, Path group VZ_OFF
Path name: path6, dynamic, Label: 6
Source: 172.16.0.1, Port: 4500, WAN ID: 1
Destination: 172.16.0.11, Port: 4500, WAN ID: 2
Local interface: Ethernet1/7
Route state: IPsec established
Traffic class 0: active (4:42:50)
MTU: 1414

```

## show bgp neighbors

```text
BGP neighbor is 10.255.255.1, remote AS 65000, internal link
  BGP version 4, remote router ID 10.255.255.1, VRF default
  Inherits configuration from and member of peer-group PATHFINDER
  Last read 00:00:09, last write 00:00:16
  Hold time is 180, keepalive interval is 60 seconds
  Configured hold time is 180, keepalive interval is 60 seconds
  Effective minimum hold time is 3 seconds
  Send failure hold time is 0 seconds
  Hold timer is active, time left: 00:02:51
  Keepalive timer is active, time left: 00:00:30
  Connect timer is inactive
  Idle-restart timer is inactive
  BGP state is Established, up for 01:17:09
  Number of transitions to established: 3
  Last state was OpenConfirm
  Last event was RecvKeepAlive
  Last sent notification:Hold Timer Expired Error/None, Last time 05:07:15
  Last rcvd notification:Cease/administrative reset, Last time 01:17:10
  Last sent socket-error:Connect (No route to host), Last time 05:44:43
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
      Received 01:17:08
      Number of stale paths removed after graceful restart: 0
      Number of paths received before End-of-RIB: 20
    L2VPN EVPN End-of-RIB received: Yes
      Received 01:17:08
      Number of stale paths removed after graceful restart: 0
      Number of paths received before End-of-RIB: 18
  AIGP attribute send and receive for IPv4 Unicast are enabled
  AIGP attribute send and receive for IPv4 with MPLS Labels are enabled
  AIGP attribute send and receive for IPv6 Unicast are enabled
  AIGP attribute send and receive for IPv6 with MPLS Labels are enabled
  BGP session driven failover for IPv6 Unicast is disabled
  BGP session driven failover for IPv4 Unicast is disabled
  Message Statistics:
                                  Sent      Rcvd
    Opens:                           3         3
    Notifications:                   1         1
    Updates:                        22        76
    Keepalives:                    401       396
    Enhanced Route Refresh:          0         0
    Begin of Route Refresh:          0         0
    End of Route Refresh:            0         0
    Total messages:                427       476
  Prefix Statistics:
                                   Sent      Rcvd     Best Paths     Best ECMP Paths
    IPv4 Unicast:                     0         0              0                   0
    IPv4 Dps:                         2        20             20                   0
    IPv6 Unicast:                     0         0              0                   0
    EVPN:                             4        18             18                   3
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
    Last update with error received at: 01:17:08
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
Local AS is 65000, local router ID 10.255.255.5
TTL is 255
Local TCP address is 10.255.255.5, local port is 46291
Remote TCP address is 10.255.255.1, remote port is 179
Local next hop for next hop self:
  Dps: 10.255.255.5
  L2VPN EVPN: 10.255.255.5
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
    Round-trip Time (rtt/rtvar): 4.7ms/1.1ms
    Delayed Ack Timeout (ato): 40.0ms
    Congestion Window (cwnd): 10
    TCP Throughput: 23.15 Mbps
    Recv Round-trip Time (rcv_rtt): 32.0ms
    Advertised Recv Window (rcv_space): 14480

BGP neighbor is 10.255.255.4, remote AS 65000, internal link
  BGP version 4, remote router ID 10.255.255.4, VRF default
  Inherits configuration from and member of peer-group PATHFINDER
  Last read 00:00:32, last write 00:00:41
  Hold time is 180, keepalive interval is 60 seconds
  Configured hold time is 180, keepalive interval is 60 seconds
  Effective minimum hold time is 3 seconds
  Send failure hold time is 0 seconds
  Hold timer is active, time left: 00:02:28
  Keepalive timer is active, time left: 00:00:03
  Connect timer is inactive
  Idle-restart timer is inactive
  BGP state is Established, up for 05:38:57
  Number of transitions to established: 1
  Last state was OpenConfirm
  Last event was RecvKeepAlive
  Last sent socket-error:Connect (No route to host), Last time 05:44:43
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
      Received 05:37:27
      Number of stale paths removed after graceful restart: 0
    L2VPN EVPN End-of-RIB received: Yes
      Received 05:37:27
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
    Updates:                        12        72
    Keepalives:                    395       388
    Enhanced Route Refresh:          0         0
    Begin of Route Refresh:          0         0
    End of Route Refresh:            0         0
    Total messages:                408       461
  Prefix Statistics:
                                   Sent      Rcvd     Best Paths     Best ECMP Paths
    IPv4 Unicast:                     0         0              0                   0
    IPv4 Dps:                         2        20             20                  10
    IPv6 Unicast:                     0         0              0                   0
    EVPN:                             4        18             18                  15
  Configured maximum total number of routes is 12000
  Inbound updates dropped by reason:
    AS path loop detection: 0
    Cluster ID loop detection: 0
    Enforced First AS: 0
    Malformed MPBGP routes: 0
    Originator ID matches local router ID: 4
    Nexthop matches local IP address: 1
    Unexpected IPv6 nexthop for IPv4 routes: 0
  Inbound updates with attribute errors:
    Resulting in removal of all paths in update (treat as withdraw): 1
    Resulting in AFI/SAFI disable: 0
    Resulting in attribute ignore: 0
    Disabled AFI/SAFIs: None
    Last treat-as-withdraw attribute error: Nexthop is local address
    Last update with error received at: 01:31:02
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
Local AS is 65000, local router ID 10.255.255.5
TTL is 255
Local TCP address is 10.255.255.5, local port is 33967
Remote TCP address is 10.255.255.4, remote port is 179
Local next hop for next hop self:
  Dps: 10.255.255.5
  L2VPN EVPN: 10.255.255.5
BFD is enabled with configured transmit interval 1000ms, receive interval 1000ms, multiplier 3 and state is Up
TCP Socket Information:
  TCP state is ESTABLISHED
  Recv-Q: 0/32768
  Send-Q: 0/46080
  Outgoing Maximum Segment Size (MSS): 1362
  Total Number of TCP retransmissions: 4
  Options:
    Timestamps enabled: yes
    Selective Acknowledgments enabled: yes
    Window Scale enabled: yes
    Explicit Congestion Notification (ECN) enabled: no
  Socket Statistics:
    Window Scale (wscale): 7,7
    Retransmission Timeout (rto): 204.0ms
    Round-trip Time (rtt/rtvar): 2.6ms/0.8ms
    Delayed Ack Timeout (ato): 40.0ms
    Congestion Window (cwnd): 2
    TCP Throughput: 8.31 Mbps
    Recv Round-trip Time (rcv_rtt): 25004.0ms
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
      Origin IGP, metric -, localpref -, weight 0, received 05:44:34 ago, valid, local
      Tunnel encapsulation attribute: Dynamic path selection
        Endpoint: 172.16.0.1, Path group name: VZ_OFF, WAN ID: 1, UDP port: 4500
Bgp routing table entry for ipv4Dps VTEP 10.255.255.6/32
 Paths: 4 available
  Local
    :: from 10.255.255.4 (10.255.255.4)
      Origin IGP, metric -, localpref 100, weight 0, received 05:33:05 ago, valid, internal
      Tunnel encapsulation attribute: Dynamic path selection
        Endpoint: 172.16.0.3, Path group name: VZ_OFF, WAN ID: 1, UDP port: 4500
  Local
    :: from 10.255.255.1 (10.255.255.1)
      Origin IGP, metric -, localpref 100, weight 0, received 01:17:09 ago, valid, internal
      Tunnel encapsulation attribute: Dynamic path selection
        Endpoint: 172.16.0.3, Path group name: VZ_OFF, WAN ID: 1, UDP port: 4500
  Local
    :: from 10.255.255.4 (10.255.255.4)
      Origin IGP, metric -, localpref 100, weight 0, received 01:17:09 ago, valid, internal
      Tunnel encapsulation attribute: Dynamic path selection
        Endpoint: 172.16.0.3, Path group name: VZ_OFF, WAN ID: 1, UDP port: 4500
  Local
    :: from 10.255.255.1 (10.255.255.1)
      Origin IGP, metric -, localpref 100, weight 0, received 01:17:09 ago, valid, internal
      Tunnel encapsulation attribute: Dynamic path selection
        Endpoint: 172.16.0.3, Path group name: VZ_OFF, WAN ID: 1, UDP port: 4500
Bgp routing table entry for ipv4Dps VTEP 10.255.255.8/32
 Paths: 4 available
  Local
    :: from 10.255.255.4 (10.255.255.4)
      Origin IGP, metric -, localpref 100, weight 0, received 04:54:20 ago, valid, internal
      Tunnel encapsulation attribute: Dynamic path selection
        Endpoint: 172.16.1.2, Path group name: VZ_NEAR, WAN ID: 1, UDP port: 4500
  Local
    :: from 10.255.255.1 (10.255.255.1)
      Origin IGP, metric -, localpref 100, weight 0, received 01:17:09 ago, valid, internal
      Tunnel encapsulation attribute: Dynamic path selection
        Endpoint: 172.16.1.2, Path group name: VZ_NEAR, WAN ID: 1, UDP port: 4500
  Local
    :: from 10.255.255.1 (10.255.255.1)
      Origin IGP, metric -, localpref 100, weight 0, received 01:17:09 ago, valid, internal
      Tunnel encapsulation attribute: Dynamic path selection
        Endpoint: 172.16.1.2, Path group name: VZ_NEAR, WAN ID: 1, UDP port: 4500
  Local
    :: from 10.255.255.4 (10.255.255.4)
      Origin IGP, metric -, localpref 100, weight 0, received 01:17:09 ago, valid, internal
      Tunnel encapsulation attribute: Dynamic path selection
        Endpoint: 172.16.1.2, Path group name: VZ_NEAR, WAN ID: 1, UDP port: 4500
Bgp routing table entry for ipv4Dps VTEP 10.255.255.10/32
 Paths: 4 available
  Local
    :: from 10.255.255.4 (10.255.255.4)
      Origin IGP, metric -, localpref 100, weight 0, received 03:35:57 ago, valid, internal
      Tunnel encapsulation attribute: Dynamic path selection
        Endpoint: 172.16.1.7, Path group name: VZ_NEAR, WAN ID: 1, UDP port: 4500
  Local
    :: from 10.255.255.1 (10.255.255.1)
      Origin IGP, metric -, localpref 100, weight 0, received 01:17:09 ago, valid, internal
      Tunnel encapsulation attribute: Dynamic path selection
        Endpoint: 172.16.1.7, Path group name: VZ_NEAR, WAN ID: 1, UDP port: 4500
  Local
    :: from 10.255.255.4 (10.255.255.4)
      Origin IGP, metric -, localpref 100, weight 0, received 01:17:09 ago, valid, internal
      Tunnel encapsulation attribute: Dynamic path selection
        Endpoint: 172.16.1.7, Path group name: VZ_NEAR, WAN ID: 1, UDP port: 4500
  Local
    :: from 10.255.255.1 (10.255.255.1)
      Origin IGP, metric -, localpref 100, weight 0, received 01:17:09 ago, valid, internal
      Tunnel encapsulation attribute: Dynamic path selection
        Endpoint: 172.16.1.7, Path group name: VZ_NEAR, WAN ID: 1, UDP port: 4500
Bgp routing table entry for ipv4Dps VTEP 10.255.255.11/32
 Paths: 4 available
  Local
    :: from 10.255.255.4 (10.255.255.4)
      Origin IGP, metric -, localpref 100, weight 0, received 04:48:30 ago, valid, internal
      Tunnel encapsulation attribute: Dynamic path selection
        Endpoint: 172.16.0.9, Path group name: VZ_OFF, WAN ID: 2, UDP port: 4500
  Local
    :: from 10.255.255.1 (10.255.255.1)
      Origin IGP, metric -, localpref 100, weight 0, received 01:17:09 ago, valid, internal
      Tunnel encapsulation attribute: Dynamic path selection
        Endpoint: 172.16.0.9, Path group name: VZ_OFF, WAN ID: 2, UDP port: 4500
  Local
    :: from 10.255.255.1 (10.255.255.1)
      Origin IGP, metric -, localpref 100, weight 0, received 01:17:09 ago, valid, internal
      Tunnel encapsulation attribute: Dynamic path selection
        Endpoint: 172.16.0.9, Path group name: VZ_OFF, WAN ID: 2, UDP port: 4500
  Local
    :: from 10.255.255.4 (10.255.255.4)
      Origin IGP, metric -, localpref 100, weight 0, received 01:17:09 ago, valid, internal
      Tunnel encapsulation attribute: Dynamic path selection
        Endpoint: 172.16.0.9, Path group name: VZ_OFF, WAN ID: 2, UDP port: 4500
Bgp routing table entry for ipv4Dps VTEP 10.255.255.12/32
 Paths: 4 available
  Local
    :: from 10.255.255.4 (10.255.255.4)
      Origin IGP, metric -, localpref 100, weight 0, received 04:44:06 ago, valid, internal
      Tunnel encapsulation attribute: Dynamic path selection
        Endpoint: 172.16.0.11, Path group name: VZ_OFF, WAN ID: 2, UDP port: 4500
  Local
    :: from 10.255.255.1 (10.255.255.1)
      Origin IGP, metric -, localpref 100, weight 0, received 01:17:09 ago, valid, internal
      Tunnel encapsulation attribute: Dynamic path selection
        Endpoint: 172.16.0.11, Path group name: VZ_OFF, WAN ID: 2, UDP port: 4500
  Local
    :: from 10.255.255.4 (10.255.255.4)
      Origin IGP, metric -, localpref 100, weight 0, received 01:17:09 ago, valid, internal
      Tunnel encapsulation attribute: Dynamic path selection
        Endpoint: 172.16.0.11, Path group name: VZ_OFF, WAN ID: 2, UDP port: 4500
  Local
    :: from 10.255.255.1 (10.255.255.1)
      Origin IGP, metric -, localpref 100, weight 0, received 01:17:09 ago, valid, internal
      Tunnel encapsulation attribute: Dynamic path selection
        Endpoint: 172.16.0.11, Path group name: VZ_OFF, WAN ID: 2, UDP port: 4500
Bgp routing table entry for ipv4Ipsec VTEP 10.255.255.5/32
 Paths: 1 available
  Local
    - from - (0.0.0.0)
      Origin IGP, metric -, localpref -, weight 0, received 05:44:44 ago, valid, local
      Tunnel encapsulation attribute: IP security
        Initial contact: false, Rekey counter: 0, Nonce length: 32
        DH group: 14, DH key length: 256
        Encryption algo: aes256, Authentication algo: sha256
Bgp routing table entry for ipv4Ipsec VTEP 10.255.255.6/32
 Paths: 4 available
  Local
    :: from 10.255.255.4 (10.255.255.4)
      Origin IGP, metric -, localpref 100, weight 0, received 03:14:41 ago, valid, internal
      Tunnel encapsulation attribute: IP security
        Initial contact: false, Rekey counter: 2, Nonce length: 32
        DH group: 14, DH key length: 256
        Encryption algo: aes256, Authentication algo: sha256
  Local
    :: from 10.255.255.1 (10.255.255.1)
      Origin IGP, metric -, localpref 100, weight 0, received 01:17:09 ago, valid, internal
      Tunnel encapsulation attribute: IP security
        Initial contact: false, Rekey counter: 2, Nonce length: 32
        DH group: 14, DH key length: 256
        Encryption algo: aes256, Authentication algo: sha256
  Local
    :: from 10.255.255.4 (10.255.255.4)
      Origin IGP, metric -, localpref 100, weight 0, received 01:17:09 ago, valid, internal
      Tunnel encapsulation attribute: IP security
        Initial contact: false, Rekey counter: 2, Nonce length: 32
        DH group: 14, DH key length: 256
        Encryption algo: aes256, Authentication algo: sha256
  Local
    :: from 10.255.255.1 (10.255.255.1)
      Origin IGP, metric -, localpref 100, weight 0, received 01:17:09 ago, valid, internal
      Tunnel encapsulation attribute: IP security
        Initial contact: false, Rekey counter: 2, Nonce length: 32
        DH group: 14, DH key length: 256
        Encryption algo: aes256, Authentication algo: sha256
Bgp routing table entry for ipv4Ipsec VTEP 10.255.255.8/32
 Paths: 4 available
  Local
    :: from 10.255.255.4 (10.255.255.4)
      Origin IGP, metric -, localpref 100, weight 0, received 04:54:20 ago, valid, internal
      Tunnel encapsulation attribute: IP security
        Initial contact: false, Rekey counter: 0, Nonce length: 32
        DH group: 14, DH key length: 256
        Encryption algo: aes256, Authentication algo: sha256
  Local
    :: from 10.255.255.1 (10.255.255.1)
      Origin IGP, metric -, localpref 100, weight 0, received 01:17:09 ago, valid, internal
      Tunnel encapsulation attribute: IP security
        Initial contact: false, Rekey counter: 0, Nonce length: 32
        DH group: 14, DH key length: 256
        Encryption algo: aes256, Authentication algo: sha256
  Local
    :: from 10.255.255.1 (10.255.255.1)
      Origin IGP, metric -, localpref 100, weight 0, received 01:17:09 ago, valid, internal
      Tunnel encapsulation attribute: IP security
        Initial contact: false, Rekey counter: 0, Nonce length: 32
        DH group: 14, DH key length: 256
        Encryption algo: aes256, Authentication algo: sha256
  Local
    :: from 10.255.255.4 (10.255.255.4)
      Origin IGP, metric -, localpref 100, weight 0, received 01:17:09 ago, valid, internal
      Tunnel encapsulation attribute: IP security
        Initial contact: false, Rekey counter: 0, Nonce length: 32
        DH group: 14, DH key length: 256
        Encryption algo: aes256, Authentication algo: sha256
Bgp routing table entry for ipv4Ipsec VTEP 10.255.255.10/32
 Paths: 4 available
  Local
    :: from 10.255.255.4 (10.255.255.4)
      Origin IGP, metric -, localpref 100, weight 0, received 03:35:57 ago, valid, internal
      Tunnel encapsulation attribute: IP security
        Initial contact: false, Rekey counter: 0, Nonce length: 32
        DH group: 14, DH key length: 256
        Encryption algo: aes256, Authentication algo: sha256
  Local
    :: from 10.255.255.1 (10.255.255.1)
      Origin IGP, metric -, localpref 100, weight 0, received 01:17:09 ago, valid, internal
      Tunnel encapsulation attribute: IP security
        Initial contact: false, Rekey counter: 0, Nonce length: 32
        DH group: 14, DH key length: 256
        Encryption algo: aes256, Authentication algo: sha256
  Local
    :: from 10.255.255.4 (10.255.255.4)
      Origin IGP, metric -, localpref 100, weight 0, received 01:17:09 ago, valid, internal
      Tunnel encapsulation attribute: IP security
        Initial contact: false, Rekey counter: 0, Nonce length: 32
        DH group: 14, DH key length: 256
        Encryption algo: aes256, Authentication algo: sha256
  Local
    :: from 10.255.255.1 (10.255.255.1)
      Origin IGP, metric -, localpref 100, weight 0, received 01:17:09 ago, valid, internal
      Tunnel encapsulation attribute: IP security
        Initial contact: false, Rekey counter: 0, Nonce length: 32
        DH group: 14, DH key length: 256
        Encryption algo: aes256, Authentication algo: sha256
Bgp routing table entry for ipv4Ipsec VTEP 10.255.255.11/32
 Paths: 4 available
  Local
    :: from 10.255.255.4 (10.255.255.4)
      Origin IGP, metric -, localpref 100, weight 0, received 04:48:30 ago, valid, internal
      Tunnel encapsulation attribute: IP security
        Initial contact: false, Rekey counter: 0, Nonce length: 32
        DH group: 14, DH key length: 256
        Encryption algo: aes256, Authentication algo: sha256
  Local
    :: from 10.255.255.1 (10.255.255.1)
      Origin IGP, metric -, localpref 100, weight 0, received 01:17:09 ago, valid, internal
      Tunnel encapsulation attribute: IP security
        Initial contact: false, Rekey counter: 0, Nonce length: 32
        DH group: 14, DH key length: 256
        Encryption algo: aes256, Authentication algo: sha256
  Local
    :: from 10.255.255.1 (10.255.255.1)
      Origin IGP, metric -, localpref 100, weight 0, received 01:17:09 ago, valid, internal
      Tunnel encapsulation attribute: IP security
        Initial contact: false, Rekey counter: 0, Nonce length: 32
        DH group: 14, DH key length: 256
        Encryption algo: aes256, Authentication algo: sha256
  Local
    :: from 10.255.255.4 (10.255.255.4)
      Origin IGP, metric -, localpref 100, weight 0, received 01:17:09 ago, valid, internal
      Tunnel encapsulation attribute: IP security
        Initial contact: false, Rekey counter: 0, Nonce length: 32
        DH group: 14, DH key length: 256
        Encryption algo: aes256, Authentication algo: sha256
Bgp routing table entry for ipv4Ipsec VTEP 10.255.255.12/32
 Paths: 4 available
  Local
    :: from 10.255.255.4 (10.255.255.4)
      Origin IGP, metric -, localpref 100, weight 0, received 04:44:06 ago, valid, internal
      Tunnel encapsulation attribute: IP security
        Initial contact: false, Rekey counter: 0, Nonce length: 32
        DH group: 14, DH key length: 256
        Encryption algo: aes256, Authentication algo: sha256
  Local
    :: from 10.255.255.1 (10.255.255.1)
      Origin IGP, metric -, localpref 100, weight 0, received 01:17:09 ago, valid, internal
      Tunnel encapsulation attribute: IP security
        Initial contact: false, Rekey counter: 0, Nonce length: 32
        DH group: 14, DH key length: 256
        Encryption algo: aes256, Authentication algo: sha256
  Local
    :: from 10.255.255.4 (10.255.255.4)
      Origin IGP, metric -, localpref 100, weight 0, received 01:17:09 ago, valid, internal
      Tunnel encapsulation attribute: IP security
        Initial contact: false, Rekey counter: 0, Nonce length: 32
        DH group: 14, DH key length: 256
        Encryption algo: aes256, Authentication algo: sha256
  Local
    :: from 10.255.255.1 (10.255.255.1)
      Origin IGP, metric -, localpref 100, weight 0, received 01:17:09 ago, valid, internal
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
>C    10.255.255.5/32 [0 pref/0 metric] updated 05:45:28 ago
         via Loopback0, directly connected
>C    172.16.0.0/31 [0 pref/0 metric] updated 05:44:51 ago
         via Ethernet1/7, directly connected
>C    172.28.128.0/20 [0 pref/0 metric] updated 05:45:07 ago
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
>S    0.0.0.0/0 [1 pref/0 metric] updated 05:44:38 ago
         via 172.16.0.0 [0 pref/0 metric] type ipv4
            via 172.16.0.0, Ethernet1/7
>S    10.80.0.0/12 [1 pref/0 metric] updated 05:45:07 ago
         via 172.28.128.1 [0 pref/0 metric] type ipv4
            via 172.28.128.1, Management1/1
>S    10.239.0.0/16 [1 pref/0 metric] updated 05:45:07 ago
         via 172.28.128.1 [0 pref/0 metric] type ipv4
            via 172.28.128.1, Management1/1
>S    172.16.0.0/12 [1 pref/0 metric] updated 05:45:07 ago
         via 172.28.128.1 [0 pref/0 metric] type ipv4
            via 172.28.128.1, Management1/1
>S    172.16.0.0/24 [1 pref/0 metric] updated 05:44:38 ago
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
>P    0.0.0.0/8 [1 pref/0 metric] updated 05:45:24 ago
         via Null0, directly connected [NF]
>P    10.255.255.1/32 [1 pref/0 metric] updated 05:44:45 ago
         via 10.255.255.1, Dps1
>P    10.255.255.4/32 [1 pref/0 metric] updated 05:44:45 ago
         via 10.255.255.4, Dps1
>P    10.255.255.6/32 [1 pref/0 metric] updated 05:44:24 ago
         via 10.255.255.6, Dps1
>P    10.255.255.11/32 [1 pref/0 metric] updated 04:48:33 ago
         via 10.255.255.11, Dps1
>P    10.255.255.12/32 [1 pref/0 metric] updated 04:44:07 ago
         via 10.255.255.12, Dps1
>P    127.0.0.0/8 [1 pref/0 metric] updated 05:45:24 ago
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
>P    ::/96 [1 pref/0 metric] updated 05:44:49 ago
         via Null0, directly connected [NF]
>P    ::ffff:127.0.0.0/104 [1 pref/0 metric] updated 05:44:49 ago
         via :: [1 pref/1 metric] type ipv6
            via , directly connected
>P    fe80::/10 [1 pref/0 metric] updated 05:44:49 ago
```

## 

```text
```

