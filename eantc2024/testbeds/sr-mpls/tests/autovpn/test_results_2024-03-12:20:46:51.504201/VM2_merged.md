# Test results for VM2

## show version

```text
Arista vEOS
Hardware version: 
Serial number: 5D0D99A5000E23386CCBB77AFF777B18
Hardware MAC address: 000c.2978.c52d
System MAC address: 000c.2978.c52d

Software image version: 4.31.2F-cloud
Architecture: i686
Internal build version: 4.31.2F-cloud-35442146.4312F
Internal build ID: 635a071a-386e-447f-942c-bcc34d9ffd3c
Image format version: 1.0
Image optimization: None

Uptime: 5 hours and 24 minutes
Total memory: 16264192 kB
Free memory: 12875904 kB

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
Ethernet1       172.16.0.11/31        up         up              9000          
Ethernet2       10.6.255.2/31         up         up              1500          
Loopback0       10.255.255.12/32      up         up             65535          
Management1     172.28.138.241/20     up         up              1500          

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
           via 172.16.0.10, Ethernet1

 S        10.255.255.1/32
           directly connected, Dps1
 S        10.255.255.4/32
           directly connected, Dps1
 S        10.255.255.5/32
           directly connected, Dps1
 S        10.255.255.6/32
           directly connected, Dps1
 S        10.255.255.11/32
           directly connected, Dps1
 C        10.255.255.12/32
           directly connected, Loopback0
 C        172.16.0.10/31
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
           via 172.16.0.10, Ethernet1

 S        10.255.255.1/32
           directly connected, Dps1
 S        10.255.255.4/32
           directly connected, Dps1
 S        10.255.255.5/32
           directly connected, Dps1
 S        10.255.255.6/32
           directly connected, Dps1
 S        10.255.255.11/32
           directly connected, Dps1
 C        10.255.255.12/32
           directly connected, Loopback0
 C        172.16.0.10/31
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
 B I      10.0.255.2/31 [20/0]
           via VTEP 10.255.255.5 VNI 201 router-mac ec:8a:48:04:21:53
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
 O        10.6.255.0/31 [110/20]
           via 10.6.255.3, Ethernet2
 C        10.6.255.2/31
           directly connected, Ethernet2
 B I      10.255.254.1/32 [20/0]
           via VTEP 10.255.255.5 VNI 201 router-mac ec:8a:48:04:21:53
 B I      10.255.254.2/32 [20/0]
           via VTEP 10.255.255.1 VNI 201 router-mac ec:8a:48:04:f5:30
 B I      10.255.254.3/32 [20/0]
           via VTEP 10.255.255.4 VNI 201 router-mac ec:8a:48:04:ff:5b
 O        10.255.254.4/32 [110/20]
           via 10.6.255.3, Ethernet2
 B I      10.255.254.5/32 [20/0]
           via VTEP 10.255.255.4 VNI 201 router-mac ec:8a:48:04:ff:5b
 B I      10.255.254.6/32 [20/0]
           via VTEP 10.255.255.4 VNI 201 router-mac ec:8a:48:04:ff:5b
 B I      172.16.255.0/31 [20/0]
           via VTEP 10.255.255.4 VNI 201 router-mac ec:8a:48:04:ff:5b
 B I      192.168.0.0/24 [20/0]
           via VTEP 10.255.255.5 VNI 201 router-mac ec:8a:48:04:21:53
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
Router identifier 10.255.255.12, local AS number 65000
Route status codes: * - valid, > - active, S - Stale, E - ECMP head, e - ECMP
                    c - Contributing to ECMP, % - Pending best path selection
Origin codes: i - IGP, e - EGP, ? - incomplete
AS Path Attributes: Or-ID - Originator ID, C-LST - Cluster List, LL Nexthop - Link Local Nexthop

          Network                Next Hop              Metric  LocPref Weight  Path
 * >Ec    RD: 10.255.255.5:1 ip-prefix 10.0.255.0/31
                                 10.255.255.5          -       100     0       i Or-ID: 10.255.255.5 C-LST: 10.255.255.4 
 *  ec    RD: 10.255.255.5:1 ip-prefix 10.0.255.0/31
                                 10.255.255.5          -       100     0       i Or-ID: 10.255.255.5 C-LST: 10.255.255.1 10.255.255.4 
 * >Ec    RD: 10.255.255.5:1 ip-prefix 10.0.255.2/31
                                 10.255.255.5          -       100     0       i Or-ID: 10.255.255.5 C-LST: 10.255.255.4 
 *  ec    RD: 10.255.255.5:1 ip-prefix 10.0.255.2/31
                                 10.255.255.5          -       100     0       i Or-ID: 10.255.255.5 C-LST: 10.255.255.1 10.255.255.4 
 * >Ec    RD: 10.255.255.1:1 ip-prefix 10.1.255.0/31
                                 10.255.255.1          -       100     0       i Or-ID: 10.255.255.1 C-LST: 10.255.255.4 
 *  ec    RD: 10.255.255.1:1 ip-prefix 10.1.255.0/31
                                 10.255.255.1          -       100     0       i
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
 * >      RD: 10.255.255.12:1 ip-prefix 10.6.255.0/31
                                 -                     -       -       0       i
 * >      RD: 10.255.255.12:1 ip-prefix 10.6.255.2/31
                                 -                     -       -       0       i
 * >Ec    RD: 10.255.255.5:1 ip-prefix 10.255.254.1/32
                                 10.255.255.5          -       100     0       i Or-ID: 10.255.255.5 C-LST: 10.255.255.4 
 *  ec    RD: 10.255.255.5:1 ip-prefix 10.255.254.1/32
                                 10.255.255.5          -       100     0       i Or-ID: 10.255.255.5 C-LST: 10.255.255.1 10.255.255.4 
 * >Ec    RD: 10.255.255.1:1 ip-prefix 10.255.254.2/32
                                 10.255.255.1          -       100     0       i Or-ID: 10.255.255.1 C-LST: 10.255.255.4 
 *  ec    RD: 10.255.255.1:1 ip-prefix 10.255.254.2/32
                                 10.255.255.1          -       100     0       i
 * >Ec    RD: 10.255.255.4:1 ip-prefix 10.255.254.3/32
                                 10.255.255.4          -       100     0       i
 *  ec    RD: 10.255.255.4:1 ip-prefix 10.255.254.3/32
                                 10.255.255.4          -       100     0       i Or-ID: 10.255.255.4 C-LST: 10.255.255.1 10.255.255.4 10.5.255.0 
 * >      RD: 10.255.255.12:1 ip-prefix 10.255.254.4/32
                                 -                     -       -       0       i
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
 * >Ec    RD: 10.255.255.5:1 ip-prefix 192.168.0.0/24
                                 10.255.255.5          -       100     0       i Or-ID: 10.255.255.5 C-LST: 10.255.255.4 
 *  ec    RD: 10.255.255.5:1 ip-prefix 192.168.0.0/24
                                 10.255.255.5          -       100     0       i Or-ID: 10.255.255.5 C-LST: 10.255.255.1 10.255.255.4 
 * >Ec    RD: 10.255.255.1:1 ip-prefix 192.168.1.0/24
                                 10.255.255.1          -       100     0       i Or-ID: 10.255.255.1 C-LST: 10.255.255.4 
 *  ec    RD: 10.255.255.1:1 ip-prefix 192.168.1.0/24
                                 10.255.255.1          -       100     0       i
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
path3:
  Source address: 172.16.0.11, Destination address: 172.16.0.4
  State: established
  Uptime: 4 hours, 45 minutes, 46 seconds
  VRF: default
  Type: static
  Remote IP: 10.255.255.5
  Role: responder
  Inbound SPI: 0xc7f887:
    Request ID: 3, Mode: transport, Replay window size: 16384, Seq: 0x0
    Errors:
      Packets outside replay window: 0, Replay: 0, Integrity failed: 0
    Lifetime config:
      Soft byte limit: 3374206223999, Hard byte limit: 6442450944000
      Soft packet limit: 2800025102, Hard packet limit: 4000000000
      Soft time limit: 2945 secs, Hard time limit: 3600 secs
    Lifetime current:
      Current bytes: 683352
      Current packets: 4762
      SA add time: Tue Mar 12 20:51:31 2024
      SA last use time: Tue Mar 12 21:05:56 2024
  Outbound SPI: 0xc25451:
    Request ID: 3, Mode: transport, Replay window size: 0, Seq: 0x0
    Errors:
      Packets outside replay window: 0, Replay: 0, Integrity failed: 0
    Lifetime config:
      Soft byte limit: 3760874117999, Hard byte limit: 6442450944000
      Soft packet limit: 2905547326, Hard packet limit: 4000000000
      Soft time limit: 2832 secs, Hard time limit: 3600 secs
    Lifetime current:
      Current bytes: 2321193
      Current packets: 9920
      SA add time: Tue Mar 12 20:51:31 2024
      SA last use time: Tue Mar 12 21:05:56 2024
path4:
  Source address: 172.16.0.11, Destination address: 172.16.0.7
  State: established
  Uptime: 4 hours, 45 minutes, 46 seconds
  VRF: default
  Type: static
  Remote IP: 10.255.255.5
  Role: responder
  Inbound SPI: 0xcaac42:
    Request ID: 4, Mode: transport, Replay window size: 16384, Seq: 0x0
    Errors:
      Packets outside replay window: 0, Replay: 0, Integrity failed: 0
    Lifetime config:
      Soft byte limit: 4558017620249, Hard byte limit: 6442450944000
      Soft packet limit: 2088732151, Hard packet limit: 4000000000
      Soft time limit: 2648 secs, Hard time limit: 3600 secs
    Lifetime current:
      Current bytes: 637616
      Current packets: 4372
      SA add time: Tue Mar 12 20:53:34 2024
      SA last use time: Tue Mar 12 21:05:56 2024
  Outbound SPI: 0xcc02a2:
    Request ID: 4, Mode: transport, Replay window size: 0, Seq: 0x0
    Errors:
      Packets outside replay window: 0, Replay: 0, Integrity failed: 0
    Lifetime config:
      Soft byte limit: 4035193936499, Hard byte limit: 6442450944000
      Soft packet limit: 2804276771, Hard packet limit: 4000000000
      Soft time limit: 2716 secs, Hard time limit: 3600 secs
    Lifetime current:
      Current bytes: 2295690
      Current packets: 9156
      SA add time: Tue Mar 12 20:53:34 2024
      SA last use time: Tue Mar 12 21:05:56 2024
path5:
  Source address: 172.16.0.11, Destination address: 172.16.0.1
  State: established
  Uptime: 4 hours, 44 minutes, 2 seconds
  VRF: default
  Type: dynamic
  Remote IP: 10.255.255.5
  Role: responder
  Packets in: 31956, Packets out: 68100
  Last known rekey count: 0
  Dynamic state: established
  Last established time: Tue Mar 12 20:54:50 2024
  DH crypto:
    Local rekey: 0, Peer rekey: 0, In SPI: 0xc6671aa5, Out SPI: 0x40fc3240
  DH state:
    Local rekey: 0, Peer rekey: 0, DH rekey state: not rekeying, Role: not rekeying
  SA crypto:
    Local rekey: 0, Peer rekey: 0, In SPI 0xf95cbd24, Out SPI 0x82c8a808
  SA rekey role: not rekeying
  SA state:
    SA type: egress , SPI: 0x55ddd7c
      Role: responder, SA rekey state: initial, Peer nonce type: init
      Add time: Tue Mar 12 20:53:37 2024, Packets: 5852, Pair SPI: 0x8ec8c860
    SA type: ingress , SPI: 0x8ec8c860
      Role: responder, SA rekey state: initial, Peer nonce type: init
      Add time: Tue Mar 12 20:53:36 2024, Packets: 2756, Pair SPI: 0x55ddd7c
  Inbound SPI: 0x8ec8c860:
    Request ID: 5, Mode: transport, Replay window size: 0, Seq: 0x0
    Errors:
      Packets outside replay window: 0, Replay: 0, Integrity failed: 0
    Lifetime config:
      Soft byte limit: 4750238319150, Hard byte limit: 6442450944000
      Soft packet limit: 2926050348, Hard packet limit: 4000000000
      Soft time limit: 2637 secs, Hard time limit: 3600 secs
    Lifetime current:
      Current bytes: 387904
      Current packets: 2756
      SA add time: Tue Mar 12 20:53:36 2024
      SA last use time: Tue Mar 12 21:05:56 2024
  Outbound SPI: 0x55ddd7c:
    Request ID: 5, Mode: transport, Replay window size: 0, Seq: 0x0
    Errors:
      Packets outside replay window: 0, Replay: 0, Integrity failed: 0
    Lifetime config:
      Soft byte limit: 4715171571750, Hard byte limit: 6442450944000
      Soft packet limit: 2927192500, Hard packet limit: 4000000000
      Soft time limit: 2529 secs, Hard time limit: 3600 secs
    Lifetime current:
      Current bytes: 1753492
      Current packets: 5852
      SA add time: Tue Mar 12 20:53:37 2024
      SA last use time: Tue Mar 12 21:05:56 2024
path6:
  Source address: 172.16.0.11, Destination address: 172.16.0.9
  State: established
  Uptime: 4 hours, 44 minutes, 2 seconds
  VRF: default
  Type: dynamic
  Remote IP: 10.255.255.11
  Role: responder
  Packets in: 31744, Packets out: 67700
  Last known rekey count: 0
  Dynamic state: established
  Last established time: Tue Mar 12 20:52:50 2024
  DH crypto:
    Local rekey: 0, Peer rekey: 0, In SPI: 0x3841219c, Out SPI: 0x145448d7
  DH state:
    Local rekey: 0, Peer rekey: 0, DH rekey state: not rekeying, Role: not rekeying
  SA crypto:
    Local rekey: 0, Peer rekey: 0, In SPI 0xa1b45f5f, Out SPI 0x8a483790
  SA rekey role: not rekeying
  SA state:
    SA type: ingress , SPI: 0x9e4857e8
      Role: responder, SA rekey state: initial, Peer nonce type: init
      Add time: Tue Mar 12 20:51:28 2024, Packets: 3032, Pair SPI: 0xb5b47fb7
    SA type: egress , SPI: 0xb5b47fb7
      Role: responder, SA rekey state: initial, Peer nonce type: init
      Add time: Tue Mar 12 20:51:28 2024, Packets: 6370, Pair SPI: 0x9e4857e8
  Inbound SPI: 0x9e4857e8:
    Request ID: 6, Mode: transport, Replay window size: 0, Seq: 0x0
    Errors:
      Packets outside replay window: 0, Replay: 0, Integrity failed: 0
    Lifetime config:
      Soft byte limit: 4748845404975, Hard byte limit: 6442450944000
      Soft packet limit: 2984931817, Hard packet limit: 4000000000
      Soft time limit: 2622 secs, Hard time limit: 3600 secs
    Lifetime current:
      Current bytes: 440272
      Current packets: 3032
      SA add time: Tue Mar 12 20:51:28 2024
      SA last use time: Tue Mar 12 21:05:56 2024
  Outbound SPI: 0xb5b47fb7:
    Request ID: 6, Mode: transport, Replay window size: 0, Seq: 0x0
    Errors:
      Packets outside replay window: 0, Replay: 0, Integrity failed: 0
    Lifetime config:
      Soft byte limit: 4737640613250, Hard byte limit: 6442450944000
      Soft packet limit: 2955618524, Hard packet limit: 4000000000
      Soft time limit: 2583 secs, Hard time limit: 3600 secs
    Lifetime current:
      Current bytes: 867590
      Current packets: 6370
      SA add time: Tue Mar 12 20:51:28 2024
      SA last use time: Tue Mar 12 21:05:56 2024
path7:
  Source address: 172.16.0.11, Destination address: 172.16.0.3
  State: established
  Uptime: 4 hours, 44 minutes, 2 seconds
  VRF: default
  Type: dynamic
  Remote IP: 10.255.255.6
  Role: responder
  Packets in: 32414, Packets out: 68926
  Last known rekey count: 0
  Dynamic state: established
  Last established time: Tue Mar 12 20:57:50 2024
  DH crypto:
    Local rekey: 0, Peer rekey: 2, In SPI: 0x4af02b10, Out SPI: 0xe746354c
    Local rekey: 0, Peer rekey: 1, In SPI: 0xbfa99625, Out SPI: 0x54dce5fd
  DH state:
    Local rekey: 0, Peer rekey: 2, DH rekey state: not rekeying, Role: not rekeying
  SA crypto:
    Local rekey: 0, Peer rekey: 2, In SPI 0x8d03da65, Out SPI 0xa9932bb1
  SA rekey role: not rekeying
  SA state:
    SA type: egress , SPI: 0x9b03fabd
      Role: responder, SA rekey state: initial, Peer nonce type: init
      Add time: Tue Mar 12 20:56:05 2024, Packets: 5156, Pair SPI: 0xb7934b09
    SA type: ingress , SPI: 0xb7934b09
      Role: responder, SA rekey state: initial, Peer nonce type: init
      Add time: Tue Mar 12 20:56:04 2024, Packets: 2475, Pair SPI: 0x9b03fabd
  Inbound SPI: 0xb7934b09:
    Request ID: 7, Mode: transport, Replay window size: 0, Seq: 0x0
    Errors:
      Packets outside replay window: 0, Replay: 0, Integrity failed: 0
    Lifetime config:
      Soft byte limit: 4705333663950, Hard byte limit: 6442450944000
      Soft packet limit: 2910593523, Hard packet limit: 4000000000
      Soft time limit: 2685 secs, Hard time limit: 3600 secs
    Lifetime current:
      Current bytes: 368748
      Current packets: 2475
      SA add time: Tue Mar 12 20:56:04 2024
      SA last use time: Tue Mar 12 21:05:56 2024
  Outbound SPI: 0x9b03fabd:
    Request ID: 7, Mode: transport, Replay window size: 0, Seq: 0x0
    Errors:
      Packets outside replay window: 0, Replay: 0, Integrity failed: 0
    Lifetime config:
      Soft byte limit: 4743465798750, Hard byte limit: 6442450944000
      Soft packet limit: 2943895157, Hard packet limit: 4000000000
      Soft time limit: 2613 secs, Hard time limit: 3600 secs
    Lifetime current:
      Current bytes: 1335944
      Current packets: 5156
      SA add time: Tue Mar 12 20:56:05 2024
      SA last use time: Tue Mar 12 21:05:56 2024
```

## show stun client translations detail

```text
Current System Time: Tue Mar 12 21:16:18 2024
Transaction ID 000000020affff0c00000000
Agent Name: dps
Source Address: 172.16.0.11:4500
Public Address: 172.16.0.11:4500
Number of Attributes: 3
Timeout Interval: 0:03:00
Last Refreshed: 0:00:50 ago
Attribute Type   Length Value           
---------------- ------ ----------------
PATH_GROUP            6 VZ_OFF          
VTEP_IP               4 10.255.255.12   
WAN_ID                4 2               

```

## show stun server bindings detail

```text
Current System Time: Tue Mar 12 21:16:18 2024
```

## show path-selection paths detail

```text
Peer: 10.255.255.1, Path group VZ_OFF
Path name: path3, static, Label: 3
Source: 172.16.0.11, Port: 4500, WAN ID: 2
Destination: 172.16.0.4, Port: 4500, WAN ID: 2886729732
Local interface: Ethernet1
Route state: IPsec established
Traffic class 0: active (4:36:33)
MTU: 8914

Peer: 10.255.255.4, Path group VZ_OFF
Path name: path4, static, Label: 4
Source: 172.16.0.11, Port: 4500, WAN ID: 2
Destination: 172.16.0.7, Port: 4500, WAN ID: 2886729735
Local interface: Ethernet1
Route state: IPsec established
Traffic class 0: active (4:36:33)
MTU: 8914

Peer: 10.255.255.5, Path group VZ_OFF
Path name: path5, dynamic, Label: 5
Source: 172.16.0.11, Port: 4500, WAN ID: 2
Destination: 172.16.0.1, Port: 4500, WAN ID: 1
Local interface: Ethernet1
Route state: IPsec established
Traffic class 0: active (4:34:54)
MTU: 8914

Peer: 10.255.255.6, Path group VZ_OFF
Path name: path7, dynamic, Label: 7
Source: 172.16.0.11, Port: 4500, WAN ID: 2
Destination: 172.16.0.3, Port: 4500, WAN ID: 1
Local interface: Ethernet1
Route state: IPsec established
Traffic class 0: active (4:34:54)
MTU: 8914

Peer: 10.255.255.11, Path group VZ_OFF
Path name: path6, dynamic, Label: 6
Source: 172.16.0.11, Port: 4500, WAN ID: 2
Destination: 172.16.0.9, Port: 4500, WAN ID: 2
Local interface: Ethernet1
Route state: IPsec established
Traffic class 0: active (4:34:54)
MTU: 1424

```

## show bgp neighbors

```text
BGP neighbor is 10.255.255.1, remote AS 65000, internal link
  BGP version 4, remote router ID 10.255.255.1, VRF default
  Inherits configuration from and member of peer-group PATHFINDER
  Last read 00:00:29, last write 00:00:45
  Hold time is 180, keepalive interval is 60 seconds
  Configured hold time is 180, keepalive interval is 60 seconds
  Effective minimum hold time is 3 seconds
  Send failure hold time is 0 seconds
  Hold timer is active, time left: 00:02:31
  Keepalive timer is active, time left: 00:00:10
  Connect timer is inactive
  Idle-restart timer is inactive
  BGP state is Established, up for 01:17:10
  Number of transitions to established: 2
  Last state was OpenConfirm
  Last event was RecvKeepAlive
  Last rcvd notification:Cease/administrative reset, Last time 01:17:11
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
      Received 01:17:09
      Number of stale paths removed after graceful restart: 0
      Number of paths received before End-of-RIB: 20
    L2VPN EVPN End-of-RIB received: Yes
      Received 01:17:09
      Number of stale paths removed after graceful restart: 0
      Number of paths received before End-of-RIB: 19
  AIGP attribute send and receive for IPv4 Unicast are enabled
  AIGP attribute send and receive for IPv4 with MPLS Labels are enabled
  AIGP attribute send and receive for IPv6 Unicast are enabled
  AIGP attribute send and receive for IPv6 with MPLS Labels are enabled
  BGP session driven failover for IPv6 Unicast is disabled
  BGP session driven failover for IPv4 Unicast is disabled
  Message Statistics:
                                  Sent      Rcvd
    Opens:                           2         2
    Notifications:                   0         1
    Updates:                        11        75
    Keepalives:                    337       330
    Enhanced Route Refresh:          0         0
    Begin of Route Refresh:          0         0
    End of Route Refresh:            0         0
    Total messages:                350       408
  Prefix Statistics:
                                   Sent      Rcvd     Best Paths     Best ECMP Paths
    IPv4 Unicast:                     0         0              0                   0
    IPv4 Dps:                         2        20             20                   0
    IPv6 Unicast:                     0         0              0                   0
    EVPN:                             3        19             19                   0
  Configured maximum total number of routes is 12000
  Inbound updates dropped by reason:
    AS path loop detection: 0
    Cluster ID loop detection: 0
    Enforced First AS: 0
    Malformed MPBGP routes: 0
    Originator ID matches local router ID: 2
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
Local AS is 65000, local router ID 10.255.255.12
TTL is 255
Local TCP address is 10.255.255.12, local port is 42851
Remote TCP address is 10.255.255.1, remote port is 179
Local next hop for next hop self:
  Dps: 10.255.255.12
  L2VPN EVPN: 10.255.255.12
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
    Retransmission Timeout (rto): 208.0ms
    Round-trip Time (rtt/rtvar): 4.1ms/1.2ms
    Delayed Ack Timeout (ato): 40.0ms
    Congestion Window (cwnd): 10
    TCP Throughput: 28.08 Mbps
    Advertised Recv Window (rcv_space): 14480

BGP neighbor is 10.255.255.4, remote AS 65000, internal link
  BGP version 4, remote router ID 10.255.255.4, VRF default
  Inherits configuration from and member of peer-group PATHFINDER
  Last read 00:00:44, last write 00:00:40
  Hold time is 180, keepalive interval is 60 seconds
  Configured hold time is 180, keepalive interval is 60 seconds
  Effective minimum hold time is 3 seconds
  Send failure hold time is 0 seconds
  Hold timer is active, time left: 00:02:16
  Keepalive timer is active, time left: 00:00:19
  Connect timer is inactive
  Idle-restart timer is inactive
  BGP state is Established, up for 04:44:06
  Number of transitions to established: 1
  Last state was OpenConfirm
  Last event was RecvKeepAlive
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
      Received 04:44:05
      Number of stale paths removed after graceful restart: 0
      Number of paths received before End-of-RIB: 8
    L2VPN EVPN End-of-RIB received: Yes
      Received 04:44:05
      Number of stale paths removed after graceful restart: 0
      Number of paths received before End-of-RIB: 5
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
    Updates:                         6        68
    Keepalives:                    335       323
    Enhanced Route Refresh:          0         0
    Begin of Route Refresh:          0         0
    End of Route Refresh:            0         0
    Total messages:                342       392
  Prefix Statistics:
                                   Sent      Rcvd     Best Paths     Best ECMP Paths
    IPv4 Unicast:                     0         0              0                   0
    IPv4 Dps:                         2        20             20                  10
    IPv6 Unicast:                     0         0              0                   0
    EVPN:                             3        19             19                  19
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
Local AS is 65000, local router ID 10.255.255.12
TTL is 255
Local TCP address is 10.255.255.12, local port is 44173
Remote TCP address is 10.255.255.4, remote port is 179
Local next hop for next hop self:
  Dps: 10.255.255.12
  L2VPN EVPN: 10.255.255.12
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
    Round-trip Time (rtt/rtvar): 3.1ms/1.1ms
    Delayed Ack Timeout (ato): 40.0ms
    Congestion Window (cwnd): 10
    TCP Throughput: 37.86 Mbps
    Advertised Recv Window (rcv_space): 14480

```

## show bgp path-selection detail

```text
BGP routing table information for VRF default
Router identifier 10.255.255.12, local AS number 65000
Bgp routing table entry for ipv4Dps VTEP 10.255.255.5/32
 Paths: 4 available
  Local
    :: from 10.255.255.4 (10.255.255.4)
      Origin IGP, metric -, localpref 100, weight 0, received 04:44:06 ago, valid, internal
      Tunnel encapsulation attribute: Dynamic path selection
        Endpoint: 172.16.0.1, Path group name: VZ_OFF, WAN ID: 1, UDP port: 4500
  Local
    :: from 10.255.255.1 (10.255.255.1)
      Origin IGP, metric -, localpref 100, weight 0, received 01:17:10 ago, valid, internal
      Tunnel encapsulation attribute: Dynamic path selection
        Endpoint: 172.16.0.1, Path group name: VZ_OFF, WAN ID: 1, UDP port: 4500
  Local
    :: from 10.255.255.4 (10.255.255.4)
      Origin IGP, metric -, localpref 100, weight 0, received 01:17:10 ago, valid, internal
      Tunnel encapsulation attribute: Dynamic path selection
        Endpoint: 172.16.0.1, Path group name: VZ_OFF, WAN ID: 1, UDP port: 4500
  Local
    :: from 10.255.255.1 (10.255.255.1)
      Origin IGP, metric -, localpref 100, weight 0, received 01:17:10 ago, valid, internal
      Tunnel encapsulation attribute: Dynamic path selection
        Endpoint: 172.16.0.1, Path group name: VZ_OFF, WAN ID: 1, UDP port: 4500
Bgp routing table entry for ipv4Dps VTEP 10.255.255.6/32
 Paths: 4 available
  Local
    :: from 10.255.255.4 (10.255.255.4)
      Origin IGP, metric -, localpref 100, weight 0, received 04:44:06 ago, valid, internal
      Tunnel encapsulation attribute: Dynamic path selection
        Endpoint: 172.16.0.3, Path group name: VZ_OFF, WAN ID: 1, UDP port: 4500
  Local
    :: from 10.255.255.1 (10.255.255.1)
      Origin IGP, metric -, localpref 100, weight 0, received 01:17:10 ago, valid, internal
      Tunnel encapsulation attribute: Dynamic path selection
        Endpoint: 172.16.0.3, Path group name: VZ_OFF, WAN ID: 1, UDP port: 4500
  Local
    :: from 10.255.255.4 (10.255.255.4)
      Origin IGP, metric -, localpref 100, weight 0, received 01:17:10 ago, valid, internal
      Tunnel encapsulation attribute: Dynamic path selection
        Endpoint: 172.16.0.3, Path group name: VZ_OFF, WAN ID: 1, UDP port: 4500
  Local
    :: from 10.255.255.1 (10.255.255.1)
      Origin IGP, metric -, localpref 100, weight 0, received 01:17:10 ago, valid, internal
      Tunnel encapsulation attribute: Dynamic path selection
        Endpoint: 172.16.0.3, Path group name: VZ_OFF, WAN ID: 1, UDP port: 4500
Bgp routing table entry for ipv4Dps VTEP 10.255.255.8/32
 Paths: 4 available
  Local
    :: from 10.255.255.4 (10.255.255.4)
      Origin IGP, metric -, localpref 100, weight 0, received 04:44:06 ago, valid, internal
      Tunnel encapsulation attribute: Dynamic path selection
        Endpoint: 172.16.1.2, Path group name: VZ_NEAR, WAN ID: 1, UDP port: 4500
  Local
    :: from 10.255.255.1 (10.255.255.1)
      Origin IGP, metric -, localpref 100, weight 0, received 01:17:10 ago, valid, internal
      Tunnel encapsulation attribute: Dynamic path selection
        Endpoint: 172.16.1.2, Path group name: VZ_NEAR, WAN ID: 1, UDP port: 4500
  Local
    :: from 10.255.255.1 (10.255.255.1)
      Origin IGP, metric -, localpref 100, weight 0, received 01:17:10 ago, valid, internal
      Tunnel encapsulation attribute: Dynamic path selection
        Endpoint: 172.16.1.2, Path group name: VZ_NEAR, WAN ID: 1, UDP port: 4500
  Local
    :: from 10.255.255.4 (10.255.255.4)
      Origin IGP, metric -, localpref 100, weight 0, received 01:17:10 ago, valid, internal
      Tunnel encapsulation attribute: Dynamic path selection
        Endpoint: 172.16.1.2, Path group name: VZ_NEAR, WAN ID: 1, UDP port: 4500
Bgp routing table entry for ipv4Dps VTEP 10.255.255.10/32
 Paths: 4 available
  Local
    :: from 10.255.255.4 (10.255.255.4)
      Origin IGP, metric -, localpref 100, weight 0, received 03:35:58 ago, valid, internal
      Tunnel encapsulation attribute: Dynamic path selection
        Endpoint: 172.16.1.7, Path group name: VZ_NEAR, WAN ID: 1, UDP port: 4500
  Local
    :: from 10.255.255.1 (10.255.255.1)
      Origin IGP, metric -, localpref 100, weight 0, received 01:17:10 ago, valid, internal
      Tunnel encapsulation attribute: Dynamic path selection
        Endpoint: 172.16.1.7, Path group name: VZ_NEAR, WAN ID: 1, UDP port: 4500
  Local
    :: from 10.255.255.1 (10.255.255.1)
      Origin IGP, metric -, localpref 100, weight 0, received 01:17:10 ago, valid, internal
      Tunnel encapsulation attribute: Dynamic path selection
        Endpoint: 172.16.1.7, Path group name: VZ_NEAR, WAN ID: 1, UDP port: 4500
  Local
    :: from 10.255.255.4 (10.255.255.4)
      Origin IGP, metric -, localpref 100, weight 0, received 01:17:10 ago, valid, internal
      Tunnel encapsulation attribute: Dynamic path selection
        Endpoint: 172.16.1.7, Path group name: VZ_NEAR, WAN ID: 1, UDP port: 4500
Bgp routing table entry for ipv4Dps VTEP 10.255.255.11/32
 Paths: 4 available
  Local
    :: from 10.255.255.4 (10.255.255.4)
      Origin IGP, metric -, localpref 100, weight 0, received 04:44:06 ago, valid, internal
      Tunnel encapsulation attribute: Dynamic path selection
        Endpoint: 172.16.0.9, Path group name: VZ_OFF, WAN ID: 2, UDP port: 4500
  Local
    :: from 10.255.255.1 (10.255.255.1)
      Origin IGP, metric -, localpref 100, weight 0, received 01:17:10 ago, valid, internal
      Tunnel encapsulation attribute: Dynamic path selection
        Endpoint: 172.16.0.9, Path group name: VZ_OFF, WAN ID: 2, UDP port: 4500
  Local
    :: from 10.255.255.1 (10.255.255.1)
      Origin IGP, metric -, localpref 100, weight 0, received 01:17:10 ago, valid, internal
      Tunnel encapsulation attribute: Dynamic path selection
        Endpoint: 172.16.0.9, Path group name: VZ_OFF, WAN ID: 2, UDP port: 4500
  Local
    :: from 10.255.255.4 (10.255.255.4)
      Origin IGP, metric -, localpref 100, weight 0, received 01:17:10 ago, valid, internal
      Tunnel encapsulation attribute: Dynamic path selection
        Endpoint: 172.16.0.9, Path group name: VZ_OFF, WAN ID: 2, UDP port: 4500
Bgp routing table entry for ipv4Dps VTEP 10.255.255.12/32
 Paths: 1 available
  Local
    - from - (0.0.0.0)
      Origin IGP, metric -, localpref -, weight 0, received 04:45:53 ago, valid, local
      Tunnel encapsulation attribute: Dynamic path selection
        Endpoint: 172.16.0.11, Path group name: VZ_OFF, WAN ID: 2, UDP port: 4500
Bgp routing table entry for ipv4Ipsec VTEP 10.255.255.5/32
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
      Origin IGP, metric -, localpref 100, weight 0, received 01:17:10 ago, valid, internal
      Tunnel encapsulation attribute: IP security
        Initial contact: false, Rekey counter: 0, Nonce length: 32
        DH group: 14, DH key length: 256
        Encryption algo: aes256, Authentication algo: sha256
  Local
    :: from 10.255.255.1 (10.255.255.1)
      Origin IGP, metric -, localpref 100, weight 0, received 01:17:10 ago, valid, internal
      Tunnel encapsulation attribute: IP security
        Initial contact: false, Rekey counter: 0, Nonce length: 32
        DH group: 14, DH key length: 256
        Encryption algo: aes256, Authentication algo: sha256
  Local
    :: from 10.255.255.4 (10.255.255.4)
      Origin IGP, metric -, localpref 100, weight 0, received 01:17:10 ago, valid, internal
      Tunnel encapsulation attribute: IP security
        Initial contact: false, Rekey counter: 0, Nonce length: 32
        DH group: 14, DH key length: 256
        Encryption algo: aes256, Authentication algo: sha256
Bgp routing table entry for ipv4Ipsec VTEP 10.255.255.6/32
 Paths: 4 available
  Local
    :: from 10.255.255.4 (10.255.255.4)
      Origin IGP, metric -, localpref 100, weight 0, received 03:14:42 ago, valid, internal
      Tunnel encapsulation attribute: IP security
        Initial contact: false, Rekey counter: 2, Nonce length: 32
        DH group: 14, DH key length: 256
        Encryption algo: aes256, Authentication algo: sha256
  Local
    :: from 10.255.255.1 (10.255.255.1)
      Origin IGP, metric -, localpref 100, weight 0, received 01:17:10 ago, valid, internal
      Tunnel encapsulation attribute: IP security
        Initial contact: false, Rekey counter: 2, Nonce length: 32
        DH group: 14, DH key length: 256
        Encryption algo: aes256, Authentication algo: sha256
  Local
    :: from 10.255.255.4 (10.255.255.4)
      Origin IGP, metric -, localpref 100, weight 0, received 01:17:10 ago, valid, internal
      Tunnel encapsulation attribute: IP security
        Initial contact: false, Rekey counter: 2, Nonce length: 32
        DH group: 14, DH key length: 256
        Encryption algo: aes256, Authentication algo: sha256
  Local
    :: from 10.255.255.1 (10.255.255.1)
      Origin IGP, metric -, localpref 100, weight 0, received 01:17:10 ago, valid, internal
      Tunnel encapsulation attribute: IP security
        Initial contact: false, Rekey counter: 2, Nonce length: 32
        DH group: 14, DH key length: 256
        Encryption algo: aes256, Authentication algo: sha256
Bgp routing table entry for ipv4Ipsec VTEP 10.255.255.8/32
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
      Origin IGP, metric -, localpref 100, weight 0, received 01:17:10 ago, valid, internal
      Tunnel encapsulation attribute: IP security
        Initial contact: false, Rekey counter: 0, Nonce length: 32
        DH group: 14, DH key length: 256
        Encryption algo: aes256, Authentication algo: sha256
  Local
    :: from 10.255.255.1 (10.255.255.1)
      Origin IGP, metric -, localpref 100, weight 0, received 01:17:10 ago, valid, internal
      Tunnel encapsulation attribute: IP security
        Initial contact: false, Rekey counter: 0, Nonce length: 32
        DH group: 14, DH key length: 256
        Encryption algo: aes256, Authentication algo: sha256
  Local
    :: from 10.255.255.4 (10.255.255.4)
      Origin IGP, metric -, localpref 100, weight 0, received 01:17:10 ago, valid, internal
      Tunnel encapsulation attribute: IP security
        Initial contact: false, Rekey counter: 0, Nonce length: 32
        DH group: 14, DH key length: 256
        Encryption algo: aes256, Authentication algo: sha256
Bgp routing table entry for ipv4Ipsec VTEP 10.255.255.10/32
 Paths: 4 available
  Local
    :: from 10.255.255.4 (10.255.255.4)
      Origin IGP, metric -, localpref 100, weight 0, received 03:35:58 ago, valid, internal
      Tunnel encapsulation attribute: IP security
        Initial contact: false, Rekey counter: 0, Nonce length: 32
        DH group: 14, DH key length: 256
        Encryption algo: aes256, Authentication algo: sha256
  Local
    :: from 10.255.255.1 (10.255.255.1)
      Origin IGP, metric -, localpref 100, weight 0, received 01:17:10 ago, valid, internal
      Tunnel encapsulation attribute: IP security
        Initial contact: false, Rekey counter: 0, Nonce length: 32
        DH group: 14, DH key length: 256
        Encryption algo: aes256, Authentication algo: sha256
  Local
    :: from 10.255.255.1 (10.255.255.1)
      Origin IGP, metric -, localpref 100, weight 0, received 01:17:10 ago, valid, internal
      Tunnel encapsulation attribute: IP security
        Initial contact: false, Rekey counter: 0, Nonce length: 32
        DH group: 14, DH key length: 256
        Encryption algo: aes256, Authentication algo: sha256
  Local
    :: from 10.255.255.4 (10.255.255.4)
      Origin IGP, metric -, localpref 100, weight 0, received 01:17:10 ago, valid, internal
      Tunnel encapsulation attribute: IP security
        Initial contact: false, Rekey counter: 0, Nonce length: 32
        DH group: 14, DH key length: 256
        Encryption algo: aes256, Authentication algo: sha256
Bgp routing table entry for ipv4Ipsec VTEP 10.255.255.11/32
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
      Origin IGP, metric -, localpref 100, weight 0, received 01:17:10 ago, valid, internal
      Tunnel encapsulation attribute: IP security
        Initial contact: false, Rekey counter: 0, Nonce length: 32
        DH group: 14, DH key length: 256
        Encryption algo: aes256, Authentication algo: sha256
  Local
    :: from 10.255.255.1 (10.255.255.1)
      Origin IGP, metric -, localpref 100, weight 0, received 01:17:10 ago, valid, internal
      Tunnel encapsulation attribute: IP security
        Initial contact: false, Rekey counter: 0, Nonce length: 32
        DH group: 14, DH key length: 256
        Encryption algo: aes256, Authentication algo: sha256
  Local
    :: from 10.255.255.4 (10.255.255.4)
      Origin IGP, metric -, localpref 100, weight 0, received 01:17:10 ago, valid, internal
      Tunnel encapsulation attribute: IP security
        Initial contact: false, Rekey counter: 0, Nonce length: 32
        DH group: 14, DH key length: 256
        Encryption algo: aes256, Authentication algo: sha256
Bgp routing table entry for ipv4Ipsec VTEP 10.255.255.12/32
 Paths: 1 available
  Local
    - from - (0.0.0.0)
      Origin IGP, metric -, localpref -, weight 0, received 04:59:01 ago, valid, local
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
>C    10.255.255.12/32 [0 pref/0 metric] updated 05:22:46 ago
         via Loopback0, directly connected
>C    172.16.0.10/31 [0 pref/0 metric] updated 05:22:36 ago
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
>S    0.0.0.0/0 [1 pref/0 metric] updated 04:59:07 ago
         via 172.16.0.10 [0 pref/0 metric] type ipv4
            via 172.16.0.10, Ethernet1
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
>P    0.0.0.0/8 [1 pref/0 metric] updated 05:22:45 ago
         via Null0, directly connected [NF]
>P    10.255.255.1/32 [1 pref/0 metric] updated 04:45:54 ago
         via 10.255.255.1, Dps1
>P    10.255.255.4/32 [1 pref/0 metric] updated 04:45:54 ago
         via 10.255.255.4, Dps1
>P    10.255.255.5/32 [1 pref/0 metric] updated 04:44:07 ago
         via 10.255.255.5, Dps1
>P    10.255.255.6/32 [1 pref/0 metric] updated 04:44:07 ago
         via 10.255.255.6, Dps1
>P    10.255.255.11/32 [1 pref/0 metric] updated 04:44:07 ago
         via 10.255.255.11, Dps1
>P    127.0.0.0/8 [1 pref/0 metric] updated 05:22:45 ago
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
>P    ::/96 [1 pref/0 metric] updated 04:59:06 ago
         via Null0, directly connected [NF]
>P    ::ffff:127.0.0.0/104 [1 pref/0 metric] updated 04:59:06 ago
         via :: [1 pref/1 metric] type ipv6
            via , directly connected
>P    fe80::/10 [1 pref/0 metric] updated 04:59:06 ago
```

## 

```text
```

