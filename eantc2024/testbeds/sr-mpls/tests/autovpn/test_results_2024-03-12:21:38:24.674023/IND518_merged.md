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

Uptime: 3 days, 22 hours and 18 minutes
Total memory: 65396488 kB
Free memory: 39976860 kB

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
Ethernet1/2      172.16.255.1/31      up         up               900          
Ethernet1/3      172.16.1.5/31        up         up              9000          
Ethernet1/4      172.16.0.7/31        up         up              9000          
Loopback0        10.255.255.4/32      up         up             65535          
Management1/1    172.28.138.224/20    up         up              1500          

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
 S        10.224.0.0/12 [1/0]
           via 172.28.128.1, Management1/1
 S        10.255.255.1/32
           directly connected, Dps1
 C        10.255.255.4/32
           directly connected, Loopback0
 S        10.255.255.5/32
           directly connected, Dps1
 S        10.255.255.6/32
           directly connected, Dps1
 S        10.255.255.8/32
           directly connected, Dps1
 S        10.255.255.10/32
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
 C        10.255.255.4/32
           directly connected, Loopback0
 S        10.255.255.5/32
           directly connected, Dps1
 S        10.255.255.6/32
           directly connected, Dps1
 S        10.255.255.8/32
           directly connected, Dps1
 S        10.255.255.10/32
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
 B I      10.0.255.2/31 [20/0]
           via VTEP 10.255.255.5 VNI 201 router-mac ec:8a:48:04:21:53
 B I      10.1.255.0/31 [20/0]
           via VTEP 10.255.255.1 VNI 201 router-mac ec:8a:48:04:f5:30
 B I      10.2.255.0/31 [20/0]
           via 172.16.255.0, Ethernet1/2
 B I      10.4.255.0/31 [20/0]
           via 172.16.255.0, Ethernet1/2
 B I      10.4.255.2/31 [20/0]
           via 172.16.255.0, Ethernet1/2
 B I      10.5.255.0/31 [20/0]
           via 172.16.255.0, Ethernet1/2
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
           via 172.16.255.0, Ethernet1/2
 B I      10.255.254.4/32 [20/0]
           via VTEP 10.255.255.12 VNI 201 router-mac 00:0c:29:78:c5:2d
 B I      10.255.254.5/32 [20/0]
           via 172.16.255.0, Ethernet1/2
 B I      10.255.254.6/32 [20/0]
           via 172.16.255.0, Ethernet1/2
 C        172.16.255.0/31
           directly connected, Ethernet1/2
 B I      192.168.0.0/24 [20/0]
           via VTEP 10.255.255.5 VNI 201 router-mac ec:8a:48:04:21:53
 B I      192.168.1.0/24 [20/0]
           via VTEP 10.255.255.1 VNI 201 router-mac ec:8a:48:04:f5:30
 B I      192.168.3.0/24 [20/0]
           via 172.16.255.0, Ethernet1/2
 B I      192.168.4.0/24 [20/0]
           via 172.16.255.0, Ethernet1/2
 B I      192.168.5.0/24 [20/0]
           via 172.16.255.0, Ethernet1/2

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
                                 10.255.255.5          -       100     0       i
 * >Ec    RD: 10.255.255.5:1 ip-prefix 10.0.255.2/31
                                 10.255.255.5          -       100     0       i
 *  ec    RD: 10.255.255.5:1 ip-prefix 10.0.255.2/31
                                 10.255.255.5          -       100     0       i Or-ID: 10.255.255.5 C-LST: 10.255.255.1 
 * >      RD: 10.255.255.1:1 ip-prefix 10.1.255.0/31
                                 10.255.255.1          -       100     0       i
 * >      RD: 10.255.255.4:1 ip-prefix 10.2.255.0/31
                                 -                     -       100     0       i
 * >      RD: 10.255.255.4:1 ip-prefix 10.4.255.0/31
                                 -                     -       100     0       i
 * >      RD: 10.255.255.4:1 ip-prefix 10.4.255.2/31
                                 -                     -       100     0       i
 * >      RD: 10.255.255.4:1 ip-prefix 10.5.255.0/31
                                 -                     -       100     0       i
 * >      RD: 10.255.255.4:1 ip-prefix 10.5.255.2/31
                                 -                     -       -       0       i
 * >Ec    RD: 10.255.255.11:1 ip-prefix 10.6.255.0/31
                                 10.255.255.11         -       100     0       i Or-ID: 10.255.255.11 C-LST: 10.255.255.1 
 *  ec    RD: 10.255.255.11:1 ip-prefix 10.6.255.0/31
                                 10.255.255.11         -       100     0       i
 * >Ec    RD: 10.255.255.12:1 ip-prefix 10.6.255.2/31
                                 10.255.255.12         -       100     0       i
 *  ec    RD: 10.255.255.12:1 ip-prefix 10.6.255.2/31
                                 10.255.255.12         -       100     0       i Or-ID: 10.255.255.12 C-LST: 10.255.255.1 
 * >Ec    RD: 10.255.255.5:1 ip-prefix 10.255.254.1/32
                                 10.255.255.5          -       100     0       i
 *  ec    RD: 10.255.255.5:1 ip-prefix 10.255.254.1/32
                                 10.255.255.5          -       100     0       i Or-ID: 10.255.255.5 C-LST: 10.255.255.1 
 * >      RD: 10.255.255.1:1 ip-prefix 10.255.254.2/32
                                 10.255.255.1          -       100     0       i
 * >      RD: 10.255.255.4:1 ip-prefix 10.255.254.3/32
                                 -                     -       100     0       i
 * >Ec    RD: 10.255.255.12:1 ip-prefix 10.255.254.4/32
                                 10.255.255.12         -       100     0       i
 *  ec    RD: 10.255.255.12:1 ip-prefix 10.255.254.4/32
                                 10.255.255.12         -       100     0       i Or-ID: 10.255.255.12 C-LST: 10.255.255.1 
 * >      RD: 10.255.255.4:1 ip-prefix 10.255.254.5/32
                                 -                     -       100     0       i
 * >      RD: 10.255.255.4:1 ip-prefix 10.255.254.6/32
                                 -                     -       100     0       i
 * >      RD: 10.255.255.4:1 ip-prefix 172.16.255.0/31
                                 -                     -       -       0       i
 *        RD: 10.255.255.4:1 ip-prefix 172.16.255.0/31
                                 -                     -       100     0       i
 * >Ec    RD: 10.255.255.5:1 ip-prefix 192.168.0.0/24
                                 10.255.255.5          -       100     0       i
 *  ec    RD: 10.255.255.5:1 ip-prefix 192.168.0.0/24
                                 10.255.255.5          -       100     0       i Or-ID: 10.255.255.5 C-LST: 10.255.255.1 
 * >      RD: 10.255.255.1:1 ip-prefix 192.168.1.0/24
                                 10.255.255.1          -       100     0       i
 * >      RD: 10.255.255.4:1 ip-prefix 192.168.3.0/24
                                 -                     -       100     0       i
 * >      RD: 10.255.255.4:1 ip-prefix 192.168.4.0/24
                                 -                     -       100     0       i
 * >      RD: 10.255.255.4:1 ip-prefix 192.168.5.0/24
                                 -                     -       100     0       i
```

## show ip security connection detail

```text
path1:
  Source address: 172.16.0.7, Destination address: 172.16.0.1
  State: established
  Uptime: 36 minutes, 52 seconds
  VRF: default
  Type: static
  Remote IP: 10.255.255.10
  Role: responder
  Inbound SPI: 0xcd0e90:
    Request ID: 34, Mode: transport, Replay window size: 16384, Seq: 0x0
    Errors:
      Packets outside replay window: 0, Replay: 0, Integrity failed: 0
    Lifetime config:
      Soft byte limit: 3779159765249, Hard byte limit: 6442450944000
      Soft packet limit: 2900920738, Hard packet limit: 4000000000
      Soft time limit: 2874 secs, Hard time limit: 3600 secs
    Lifetime current:
      Current bytes: 2321712
      Current packets: 7324
      SA add time: Tue Mar 12 14:01:37 2024
      SA last use time: Tue Mar 12 14:35:03 2024
  Outbound SPI: 0xcd0c98:
    Request ID: 34, Mode: transport, Replay window size: 0, Seq: 0x0
    Errors:
      Packets outside replay window: 0, Replay: 0, Integrity failed: 0
    Lifetime config:
      Soft byte limit: 3260370813749, Hard byte limit: 6442450944000
      Soft packet limit: 2953987180, Hard packet limit: 4000000000
      Soft time limit: 2952 secs, Hard time limit: 3600 secs
    Lifetime current:
      Current bytes: 3691959
      Current packets: 15024
      SA add time: Tue Mar 12 14:01:37 2024
      SA last use time: Tue Mar 12 14:35:02 2024
path2:
  Source address: 172.16.1.5, Destination address: 172.16.0.1
  State: idle
  Uptime: N/A
  VRF: default
  Type: static
  Remote IP: 10.255.255.10
  Role: responder
path3:
  Source address: 172.16.0.7, Destination address: 172.16.0.3
  State: established
  Uptime: 6 hours, 24 minutes, 49 seconds
  VRF: default
  Type: static
  Remote IP: 10.255.255.10
  Role: responder
  Inbound SPI: 0xc50294:
    Request ID: 5, Mode: transport, Replay window size: 16384, Seq: 0x0
    Errors:
      Packets outside replay window: 0, Replay: 0, Integrity failed: 0
    Lifetime config:
      Soft byte limit: 4548272511749, Hard byte limit: 6442450944000
      Soft packet limit: 2374168726, Hard packet limit: 4000000000
      Soft time limit: 2785 secs, Hard time limit: 3600 secs
    Lifetime current:
      Current bytes: 1856412
      Current packets: 6483
      SA add time: Tue Mar 12 14:05:36 2024
      SA last use time: Tue Mar 12 14:35:03 2024
  Outbound SPI: 0xc17f52:
    Request ID: 5, Mode: transport, Replay window size: 0, Seq: 0x0
    Errors:
      Packets outside replay window: 0, Replay: 0, Integrity failed: 0
    Lifetime config:
      Soft byte limit: 3602849670749, Hard byte limit: 6442450944000
      Soft packet limit: 2819306823, Hard packet limit: 4000000000
      Soft time limit: 2865 secs, Hard time limit: 3600 secs
    Lifetime current:
      Current bytes: 2828794
      Current packets: 13232
      SA add time: Tue Mar 12 14:05:36 2024
      SA last use time: Tue Mar 12 14:35:02 2024
path4:
  Source address: 172.16.1.5, Destination address: 172.16.0.3
  State: idle
  Uptime: N/A
  VRF: default
  Type: static
  Remote IP: 10.255.255.10
  Role: responder
path5:
  Source address: 172.16.0.7, Destination address: 172.16.1.2
  State: idle
  Uptime: N/A
  VRF: default
  Type: static
  Remote IP: 10.255.255.10
  Role: responder
path6:
  Source address: 172.16.1.5, Destination address: 172.16.1.2
  State: established
  Uptime: 5 hours, 45 minutes, 53 seconds
  VRF: default
  Type: static
  Remote IP: 10.255.255.10
  Role: responder
  Inbound SPI: 0xccc323:
    Request ID: 22, Mode: transport, Replay window size: 16384, Seq: 0x0
    Errors:
      Packets outside replay window: 0, Replay: 0, Integrity failed: 0
    Lifetime config:
      Soft byte limit: 4196579582249, Hard byte limit: 6442450944000
      Soft packet limit: 2753122581, Hard packet limit: 4000000000
      Soft time limit: 2524 secs, Hard time limit: 3600 secs
    Lifetime current:
      Current bytes: 2355080
      Current packets: 7622
      SA add time: Tue Mar 12 13:59:59 2024
      SA last use time: Tue Mar 12 14:35:03 2024
  Outbound SPI: 0xcd148e:
    Request ID: 22, Mode: transport, Replay window size: 0, Seq: 0x0
    Errors:
      Packets outside replay window: 0, Replay: 0, Integrity failed: 0
    Lifetime config:
      Soft byte limit: 4698079031249, Hard byte limit: 6442450944000
      Soft packet limit: 2276821377, Hard packet limit: 4000000000
      Soft time limit: 2717 secs, Hard time limit: 3600 secs
    Lifetime current:
      Current bytes: 3705275
      Current packets: 15616
      SA add time: Tue Mar 12 13:59:59 2024
      SA last use time: Tue Mar 12 14:35:03 2024
path7:
  Source address: 172.16.0.7, Destination address: 172.16.0.9
  State: established
  Uptime: 45 minutes, 58 seconds
  VRF: default
  Type: static
  Remote IP: 10.255.255.10
  Role: responder
  Inbound SPI: 0xc8216f:
    Request ID: 31, Mode: transport, Replay window size: 16384, Seq: 0x0
    Errors:
      Packets outside replay window: 0, Replay: 0, Integrity failed: 0
    Lifetime config:
      Soft byte limit: 4085881340999, Hard byte limit: 6442450944000
      Soft packet limit: 2190322510, Hard packet limit: 4000000000
      Soft time limit: 2834 secs, Hard time limit: 3600 secs
    Lifetime current:
      Current bytes: 260724
      Current packets: 665
      SA add time: Tue Mar 12 14:35:12 2024
      SA last use time: Tue Mar 12 14:35:03 2024
  Outbound SPI: 0xcc9f69:
    Request ID: 31, Mode: transport, Replay window size: 0, Seq: 0x0
    Errors:
      Packets outside replay window: 0, Replay: 0, Integrity failed: 0
    Lifetime config:
      Soft byte limit: 3767262726749, Hard byte limit: 6442450944000
      Soft packet limit: 2214627136, Hard packet limit: 4000000000
      Soft time limit: 2780 secs, Hard time limit: 3600 secs
    Lifetime current:
      Current bytes: 218906
      Current packets: 1378
      SA add time: Tue Mar 12 14:35:12 2024
      SA last use time: Tue Mar 12 14:35:03 2024
path8:
  Source address: 172.16.1.5, Destination address: 172.16.0.9
  State: idle
  Uptime: N/A
  VRF: default
  Type: static
  Remote IP: 10.255.255.10
  Role: responder
path9:
  Source address: 172.16.0.7, Destination address: 172.16.0.11
  State: established
  Uptime: 5 hours, 37 minutes, 18 seconds
  VRF: default
  Type: static
  Remote IP: 10.255.255.10
  Role: responder
  Inbound SPI: 0xc2401c:
    Request ID: 25, Mode: transport, Replay window size: 16384, Seq: 0x0
    Errors:
      Packets outside replay window: 0, Replay: 0, Integrity failed: 0
    Lifetime config:
      Soft byte limit: 3407052848249, Hard byte limit: 6442450944000
      Soft packet limit: 2315943631, Hard packet limit: 4000000000
      Soft time limit: 2709 secs, Hard time limit: 3600 secs
    Lifetime current:
      Current bytes: 1802420
      Current packets: 6017
      SA add time: Tue Mar 12 14:07:41 2024
      SA last use time: Tue Mar 12 14:35:02 2024
  Outbound SPI: 0xc78726:
    Request ID: 25, Mode: transport, Replay window size: 0, Seq: 0x0
    Errors:
      Packets outside replay window: 0, Replay: 0, Integrity failed: 0
    Lifetime config:
      Soft byte limit: 3511600210499, Hard byte limit: 6442450944000
      Soft packet limit: 2370309335, Hard packet limit: 4000000000
      Soft time limit: 3002 secs, Hard time limit: 3600 secs
    Lifetime current:
      Current bytes: 1448415
      Current packets: 12320
      SA add time: Tue Mar 12 14:07:41 2024
      SA last use time: Tue Mar 12 14:35:02 2024
path10:
  Source address: 172.16.1.5, Destination address: 172.16.0.11
  State: idle
  Uptime: N/A
  VRF: default
  Type: static
  Remote IP: 10.255.255.10
  Role: responder
path11:
  Source address: 172.16.0.7, Destination address: 172.16.1.7
  State: idle
  Uptime: N/A
  VRF: default
  Type: static
  Remote IP: 10.255.255.10
  Role: responder
path12:
  Source address: 172.16.1.5, Destination address: 172.16.1.7
  State: established
  Uptime: 4 hours, 27 minutes, 30 seconds
  VRF: default
  Type: static
  Remote IP: 10.255.255.10
  Role: responder
  Inbound SPI: 0xc646b3:
    Request ID: 27, Mode: transport, Replay window size: 16384, Seq: 0x0
    Errors:
      Packets outside replay window: 0, Replay: 0, Integrity failed: 0
    Lifetime config:
      Soft byte limit: 4770552498749, Hard byte limit: 6442450944000
      Soft packet limit: 2567089930, Hard packet limit: 4000000000
      Soft time limit: 2773 secs, Hard time limit: 3600 secs
    Lifetime current:
      Current bytes: 158788
      Current packets: 1165
      SA add time: Tue Mar 12 14:32:28 2024
      SA last use time: Tue Mar 12 14:35:02 2024
  Outbound SPI: 0xc05281:
    Request ID: 27, Mode: transport, Replay window size: 0, Seq: 0x0
    Errors:
      Packets outside replay window: 0, Replay: 0, Integrity failed: 0
    Lifetime config:
      Soft byte limit: 4636793321999, Hard byte limit: 6442450944000
      Soft packet limit: 2843911309, Hard packet limit: 4000000000
      Soft time limit: 2971 secs, Hard time limit: 3600 secs
    Lifetime current:
      Current bytes: 253157
      Current packets: 2408
      SA add time: Tue Mar 12 14:32:28 2024
      SA last use time: Tue Mar 12 14:35:03 2024
path13:
  Source address: 172.16.0.7, Destination address: 172.16.1.0
  State: idle
  Uptime: N/A
  VRF: default
  Type: static
  Remote IP: 10.255.255.10
  Role: responder
path14:
  Source address: 172.16.1.5, Destination address: 172.16.1.0
  State: established
  Uptime: 3 hours, 4 minutes, 37 seconds
  VRF: default
  Type: static
  Remote IP: 10.255.255.10
  Role: responder
  Inbound SPI: 0xc9c4dc:
    Request ID: 29, Mode: transport, Replay window size: 16384, Seq: 0x0
    Errors:
      Packets outside replay window: 0, Replay: 0, Integrity failed: 0
    Lifetime config:
      Soft byte limit: 3572189301749, Hard byte limit: 6442450944000
      Soft packet limit: 2370428977, Hard packet limit: 4000000000
      Soft time limit: 2995 secs, Hard time limit: 3600 secs
    Lifetime current:
      Current bytes: 376292
      Current packets: 1653
      SA add time: Tue Mar 12 14:29:57 2024
      SA last use time: Tue Mar 12 14:35:02 2024
  Outbound SPI: 0xc25a01:
    Request ID: 29, Mode: transport, Replay window size: 0, Seq: 0x0
    Errors:
      Packets outside replay window: 0, Replay: 0, Integrity failed: 0
    Lifetime config:
      Soft byte limit: 3795198388499, Hard byte limit: 6442450944000
      Soft packet limit: 2813967348, Hard packet limit: 4000000000
      Soft time limit: 2767 secs, Hard time limit: 3600 secs
    Lifetime current:
      Current bytes: 509726
      Current packets: 3356
      SA add time: Tue Mar 12 14:29:58 2024
      SA last use time: Tue Mar 12 14:35:02 2024
```

## show stun client translations detail

```text
Current System Time: Tue Mar 12 14:38:30 2024
```

## show stun server bindings detail

```text
Current System Time: Tue Mar 12 14:38:31 2024
Transaction ID 000000010affff0500000000
Public Address: 172.16.0.1:4500
Number of Attributes: 3
Timeout Interval: 0:00:40
Timeout: 0:00:22
Attribute Type   Length Value           
---------------- ------ ----------------
PATH_GROUP            6 VZ_OFF          
VTEP_IP               4 10.255.255.5    
WAN_ID                4 1               

Transaction ID 000000010affff0600000000
Public Address: 172.16.0.3:4500
Number of Attributes: 3
Timeout Interval: 0:00:40
Timeout: 0:00:06
Attribute Type   Length Value           
---------------- ------ ----------------
PATH_GROUP            6 VZ_OFF          
VTEP_IP               4 10.255.255.6    
WAN_ID                4 1               

Transaction ID 000000010affff0800000000
Public Address: 172.16.1.2:4500
Number of Attributes: 3
Timeout Interval: 0:00:40
Timeout: 0:00:14
Attribute Type   Length Value           
---------------- ------ ----------------
PATH_GROUP            7 VZ_NEAR         
VTEP_IP               4 10.255.255.8    
WAN_ID                4 1               

Transaction ID 000000010affff0a00000000
Public Address: 172.16.1.7:4500
Number of Attributes: 3
Timeout Interval: 0:00:40
Timeout: 0:00:05
Attribute Type   Length Value           
---------------- ------ ----------------
PATH_GROUP            7 VZ_NEAR         
VTEP_IP               4 10.255.255.10   
WAN_ID                4 1               

Transaction ID 000000020affff0100000000
Public Address: 172.16.1.0:4500
Number of Attributes: 3
Timeout Interval: 0:00:40
Timeout: 0:00:32
Attribute Type   Length Value           
---------------- ------ ----------------
PATH_GROUP            7 VZ_NEAR         
VTEP_IP               4 10.255.255.1    
WAN_ID                4 2               

Transaction ID 000000020affff0b00000000
Public Address: 172.16.0.9:4500
Number of Attributes: 3
Timeout Interval: 0:00:40
Timeout: 0:00:16
Attribute Type   Length Value           
---------------- ------ ----------------
PATH_GROUP            6 VZ_OFF          
VTEP_IP               4 10.255.255.11   
WAN_ID                4 2               

Transaction ID 000000020affff0c00000000
Public Address: 172.16.0.11:4500
Number of Attributes: 3
Timeout Interval: 0:00:40
Timeout: 0:00:06
Attribute Type   Length Value           
---------------- ------ ----------------
PATH_GROUP            6 VZ_OFF          
VTEP_IP               4 10.255.255.12   
WAN_ID                4 2               

```

## show path-selection paths detail

```text
Peer: 10.255.255.1, Path group VZ_NEAR
Path name: path14, dynamic, Label: 14
Source: 172.16.1.5, Port: 4500, WAN ID: 2
Destination: 172.16.1.0, Port: 4500, WAN ID: 2
Local interface: Ethernet1/3
Route state: IPsec established
Traffic class 0: active (3:04:28)
MTU: 8914

Peer: 10.255.255.5, Path group VZ_OFF
Path name: path1, dynamic, Label: 1
Source: 172.16.0.7, Port: 4500, WAN ID: 1
Destination: 172.16.0.1, Port: 4500, WAN ID: 1
Local interface: Ethernet1/4
Route state: IPsec established
Traffic class 0: active (0:36:51)
MTU: 8914

Peer: 10.255.255.6, Path group VZ_OFF
Path name: path3, dynamic, Label: 3
Source: 172.16.0.7, Port: 4500, WAN ID: 1
Destination: 172.16.0.3, Port: 4500, WAN ID: 1
Local interface: Ethernet1/4
Route state: IPsec established
Traffic class 0: active (6:24:33)
MTU: 8914

Peer: 10.255.255.8, Path group VZ_NEAR
Path name: path6, dynamic, Label: 6
Source: 172.16.1.5, Port: 4500, WAN ID: 2
Destination: 172.16.1.2, Port: 4500, WAN ID: 1
Local interface: Ethernet1/3
Route state: IPsec established
Traffic class 0: active (5:45:38)
MTU: 8914

Peer: 10.255.255.10, Path group VZ_NEAR
Path name: path12, dynamic, Label: 12
Source: 172.16.1.5, Port: 4500, WAN ID: 2
Destination: 172.16.1.7, Port: 4500, WAN ID: 1
Local interface: Ethernet1/3
Route state: IPsec established
Traffic class 0: active (4:27:19)
MTU: 1424

Peer: 10.255.255.11, Path group VZ_OFF
Path name: path7, dynamic, Label: 7
Source: 172.16.0.7, Port: 4500, WAN ID: 1
Destination: 172.16.0.9, Port: 4500, WAN ID: 2
Local interface: Ethernet1/4
Route state: IPsec established
Traffic class 0: active (0:45:56)
MTU: 1424

Peer: 10.255.255.12, Path group VZ_OFF
Path name: path9, dynamic, Label: 9
Source: 172.16.0.7, Port: 4500, WAN ID: 1
Destination: 172.16.0.11, Port: 4500, WAN ID: 2
Local interface: Ethernet1/4
Route state: IPsec established
Traffic class 0: active (5:37:04)
MTU: 1424

```

## show bgp neighbors

```text
BGP neighbor is 10.255.255.1, remote AS 65000, internal link
  BGP version 4, remote router ID 10.255.255.1, VRF default
  Inherits configuration from and member of peer-group autovpnEdges
  Last read 00:00:18, last write 00:00:05
  Hold time is 180, keepalive interval is 60 seconds
  Configured hold time is 180, keepalive interval is 60 seconds
  Effective minimum hold time is 3 seconds
  Send failure hold time is 0 seconds
  Hold timer is active, time left: 00:02:42
  Keepalive timer is active, time left: 00:00:49
  Connect timer is inactive
  Idle-restart timer is inactive
  BGP state is Established, up for 02:08:42
  Number of transitions to established: 2
  Last state was OpenConfirm
  Last event was RecvKeepAlive
  Last rcvd notification:Cease/administrative reset, Last time 02:08:43
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
      Received 02:08:41
      Number of stale paths removed after graceful restart: 0
      Number of paths received before End-of-RIB: 12
    L2VPN EVPN End-of-RIB received: Yes
      Received 02:08:41
      Number of stale paths removed after graceful restart: 0
      Number of paths received before End-of-RIB: 6
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
    Updates:                        59        52
    Keepalives:                    213       215
    Enhanced Route Refresh:          0         0
    Begin of Route Refresh:          0         0
    End of Route Refresh:            0         0
    Total messages:                274       270
  Prefix Statistics:
                                   Sent      Rcvd     Best Paths     Best ECMP Paths
    IPv4 Unicast:                     0         0              0                   0
    IPv4 Dps:                        12        12             12                   2
    IPv6 Unicast:                     0         0              0                   0
    EVPN:                            18         9              9                   1
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
Local AS is 65000, local router ID 10.255.255.4
TTL is 255
Local TCP address is 10.255.255.4, local port is 179
Remote TCP address is 10.255.255.1, remote port is 39583
Local next hop for next hop self:
  Dps: 10.255.255.4
  L2VPN EVPN: 10.255.255.4
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
    Round-trip Time (rtt/rtvar): 4.0ms/1.4ms
    Delayed Ack Timeout (ato): 40.0ms
    Congestion Window (cwnd): 10
    TCP Throughput: 28.77 Mbps
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
  Connect timer is active, time left: 00:00:06
  Connection interval is 20 seconds
  Failed connection attempts is 3726
  Idle-restart timer is inactive
  BGP state is Connect
  Number of transitions to established: 0
  Last state was Active
  Last event was ConnectRetry
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
  BGP version 4, remote router ID 0.0.0.0, VRF default
  Inherits configuration from and member of peer-group autovpnEdges
  Last read never, last write never
  Hold time is 0, keepalive interval is 0 seconds
  Configured hold time is 180, keepalive interval is 60 seconds
  Effective minimum hold time is 3 seconds
  Send failure hold time is 0 seconds
  Hold timer is inactive
  Keepalive timer is inactive
  Connect timer is active, time left: 00:00:03
  Connection interval is 20 seconds
  Failed connection attempts is 3735
  Idle-restart timer is inactive
  BGP state is Connect
  Number of transitions to established: 0
  Last state was Active
  Last event was ConnectRetry
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
Local AS is 65000, local router ID 10.255.255.4
TTL is 255
Local TCP address is 10.255.255.4
Remote TCP address is 10.255.255.3, remote port is 179
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

BGP neighbor is 10.255.255.5, remote AS 65000, internal link
  BGP version 4, remote router ID 10.255.255.5, VRF default
  Inherits configuration from and member of peer-group autovpnEdges
  Last read 00:00:17, last write 00:00:48
  Hold time is 180, keepalive interval is 60 seconds
  Configured hold time is 180, keepalive interval is 60 seconds
  Effective minimum hold time is 3 seconds
  Send failure hold time is 0 seconds
  Hold timer is active, time left: 00:02:43
  Keepalive timer is active, time left: 00:00:00
  Connect timer is inactive
  Idle-restart timer is inactive
  BGP state is Established, up for 00:36:51
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
      Received 00:36:50
      Number of stale paths removed after graceful restart: 0
      Number of paths received before End-of-RIB: 2
    L2VPN EVPN End-of-RIB received: Yes
      Received 00:36:50
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
    Updates:                        30         6
    Keepalives:                     44        45
    Enhanced Route Refresh:          0         0
    Begin of Route Refresh:          0         0
    End of Route Refresh:            0         0
    Total messages:                 75        52
  Prefix Statistics:
                                   Sent      Rcvd     Best Paths     Best ECMP Paths
    IPv4 Unicast:                     0         0              0                   0
    IPv4 Dps:                        22         2              2                   2
    IPv6 Unicast:                     0         0              0                   0
    EVPN:                            18         4              4                   3
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
Local AS is 65000, local router ID 10.255.255.4
TTL is 255
Local TCP address is 10.255.255.4, local port is 179
Remote TCP address is 10.255.255.5, remote port is 45931
Local next hop for next hop self:
  Dps: 10.255.255.4
  L2VPN EVPN: 10.255.255.4
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
    Round-trip Time (rtt/rtvar): 5.4ms/0.9ms
    Delayed Ack Timeout (ato): 40.0ms
    Congestion Window (cwnd): 10
    TCP Throughput: 21.46 Mbps
    Recv Round-trip Time (rcv_rtt): 4.0ms
    Advertised Recv Window (rcv_space): 14600

BGP neighbor is 10.255.255.6, remote AS 65000, internal link
  BGP version 4, remote router ID 10.255.255.6, VRF default
  Inherits configuration from and member of peer-group autovpnEdges
  Last read 00:00:38, last write 00:00:47
  Hold time is 180, keepalive interval is 60 seconds
  Configured hold time is 180, keepalive interval is 60 seconds
  Effective minimum hold time is 3 seconds
  Send failure hold time is 0 seconds
  Hold timer is active, time left: 00:02:22
  Keepalive timer is active, time left: 00:00:07
  Connect timer is inactive
  Idle-restart timer is inactive
  BGP state is Established, up for 06:24:37
  Number of transitions to established: 1
  Last state was OpenConfirm
  Last event was RecvKeepAlive
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
      Received 06:24:36
      Number of stale paths removed after graceful restart: 0
      Number of paths received before End-of-RIB: 2
    L2VPN EVPN End-of-RIB received: Yes
      Received 06:24:37
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
    Updates:                       104         5
    Keepalives:                    436       447
    Enhanced Route Refresh:          0         0
    Begin of Route Refresh:          0         0
    End of Route Refresh:            0         0
    Total messages:                541       453
  Prefix Statistics:
                                   Sent      Rcvd     Best Paths     Best ECMP Paths
    IPv4 Unicast:                     0         0              0                   0
    IPv4 Dps:                        22         2              2                   2
    IPv6 Unicast:                     0         0              0                   0
    EVPN:                            22         0              0                   0
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
Local AS is 65000, local router ID 10.255.255.4
TTL is 255
Local TCP address is 10.255.255.4, local port is 179
Remote TCP address is 10.255.255.6, remote port is 43927
Local next hop for next hop self:
  Dps: 10.255.255.4
  L2VPN EVPN: 10.255.255.4
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
    Round-trip Time (rtt/rtvar): 4.6ms/1.2ms
    Delayed Ack Timeout (ato): 40.0ms
    Congestion Window (cwnd): 10
    TCP Throughput: 24.94 Mbps
    Advertised Recv Window (rcv_space): 14600

BGP neighbor is 10.255.255.8, remote AS 65000, internal link
  BGP version 4, remote router ID 10.255.255.8, VRF default
  Inherits configuration from and member of peer-group autovpnEdges
  Last read 00:00:19, last write 00:00:29
  Hold time is 180, keepalive interval is 60 seconds
  Configured hold time is 180, keepalive interval is 60 seconds
  Effective minimum hold time is 3 seconds
  Send failure hold time is 0 seconds
  Hold timer is active, time left: 00:02:41
  Keepalive timer is active, time left: 00:00:28
  Connect timer is inactive
  Idle-restart timer is inactive
  BGP state is Established, up for 05:45:52
  Number of transitions to established: 1
  Last state was OpenConfirm
  Last event was RecvKeepAlive
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
      Received 05:45:02
      Number of stale paths removed after graceful restart: 0
      Number of paths received before End-of-RIB: 2
    L2VPN EVPN End-of-RIB received: Yes
      Received 05:45:02
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
    Updates:                        91         8
    Keepalives:                    395       404
    Enhanced Route Refresh:          0         0
    Begin of Route Refresh:          0         0
    End of Route Refresh:            0         0
    Total messages:                487       413
  Prefix Statistics:
                                   Sent      Rcvd     Best Paths     Best ECMP Paths
    IPv4 Unicast:                     0         0              0                   0
    IPv4 Dps:                        22         2              2                   2
    IPv6 Unicast:                     0         0              0                   0
    EVPN:                            22         0              0                   0
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
Local AS is 65000, local router ID 10.255.255.4
TTL is 255
Local TCP address is 10.255.255.4, local port is 179
Remote TCP address is 10.255.255.8, remote port is 38825
Local next hop for next hop self:
  Dps: 10.255.255.4
  L2VPN EVPN: 10.255.255.4
BFD is enabled with configured transmit interval 1000ms, receive interval 1000ms, multiplier 3 and state is Up
TCP Socket Information:
  TCP state is ESTABLISHED
  Recv-Q: 0/32768
  Send-Q: 0/46080
  Outgoing Maximum Segment Size (MSS): 1448
  Total Number of TCP retransmissions: 2
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
    Congestion Window (cwnd): 4
    TCP Throughput: 11.18 Mbps
    Recv Round-trip Time (rcv_rtt): 4.0ms
    Advertised Recv Window (rcv_space): 14600

BGP neighbor is 10.255.255.10, remote AS 65000, internal link
  BGP version 4, remote router ID 10.255.255.10, VRF default
  Inherits configuration from and member of peer-group autovpnEdges
  Last read 00:00:07, last write 00:00:42
  Hold time is 180, keepalive interval is 60 seconds
  Configured hold time is 180, keepalive interval is 60 seconds
  Effective minimum hold time is 3 seconds
  Send failure hold time is 0 seconds
  Hold timer is active, time left: 00:02:53
  Keepalive timer is active, time left: 00:00:07
  Connect timer is inactive
  Idle-restart timer is inactive
  BGP state is Established, up for 04:27:29
  Number of transitions to established: 1
  Last state was OpenConfirm
  Last event was RecvKeepAlive
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
      Received 04:27:22
      Number of stale paths removed after graceful restart: 0
      Number of paths received before End-of-RIB: 2
    L2VPN EVPN End-of-RIB received: Yes
      Received 04:27:22
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
    Updates:                        94         4
    Keepalives:                    300       316
    Enhanced Route Refresh:          0         0
    Begin of Route Refresh:          0         0
    End of Route Refresh:            0         0
    Total messages:                395       321
  Prefix Statistics:
                                   Sent      Rcvd     Best Paths     Best ECMP Paths
    IPv4 Unicast:                     0         0              0                   0
    IPv4 Dps:                        22         2              2                   2
    IPv6 Unicast:                     0         0              0                   0
    EVPN:                            22         0              0                   0
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
Local AS is 65000, local router ID 10.255.255.4
TTL is 255
Local TCP address is 10.255.255.4, local port is 179
Remote TCP address is 10.255.255.10, remote port is 35991
Local next hop for next hop self:
  Dps: 10.255.255.4
  L2VPN EVPN: 10.255.255.4
BFD is enabled with configured transmit interval 1000ms, receive interval 1000ms, multiplier 3 and state is Up
TCP Socket Information:
  TCP state is ESTABLISHED
  Recv-Q: 0/32768
  Send-Q: 0/46080
  Outgoing Maximum Segment Size (MSS): 1362
  Total Number of TCP retransmissions: 1
  Options:
    Timestamps enabled: yes
    Selective Acknowledgments enabled: yes
    Window Scale enabled: yes
    Explicit Congestion Notification (ECN) enabled: no
  Socket Statistics:
    Window Scale (wscale): 7,7
    Retransmission Timeout (rto): 208.0ms
    Round-trip Time (rtt/rtvar): 4.3ms/0.9ms
    Delayed Ack Timeout (ato): 40.0ms
    Congestion Window (cwnd): 10
    TCP Throughput: 25.34 Mbps
    Advertised Recv Window (rcv_space): 14600

BGP neighbor is 10.255.255.11, remote AS 65000, internal link
  BGP version 4, remote router ID 10.255.255.11, VRF default
  Inherits configuration from and member of peer-group autovpnEdges
  Last read 00:00:17, last write 00:00:40
  Hold time is 180, keepalive interval is 60 seconds
  Configured hold time is 180, keepalive interval is 60 seconds
  Effective minimum hold time is 3 seconds
  Send failure hold time is 0 seconds
  Hold timer is active, time left: 00:02:43
  Keepalive timer is active, time left: 00:00:10
  Connect timer is inactive
  Idle-restart timer is inactive
  BGP state is Established, up for 00:45:57
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
      Received 00:45:56
      Number of stale paths removed after graceful restart: 0
      Number of paths received before End-of-RIB: 2
    L2VPN EVPN End-of-RIB received: Yes
      Received 00:45:56
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
    Updates:                        42         5
    Keepalives:                     53        56
    Enhanced Route Refresh:          0         0
    Begin of Route Refresh:          0         0
    End of Route Refresh:            0         0
    Total messages:                 96        62
  Prefix Statistics:
                                   Sent      Rcvd     Best Paths     Best ECMP Paths
    IPv4 Unicast:                     0         0              0                   0
    IPv4 Dps:                        22         2              2                   0
    IPv6 Unicast:                     0         0              0                   0
    EVPN:                            22         1              1                   0
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
Local AS is 65000, local router ID 10.255.255.4
TTL is 255
Local TCP address is 10.255.255.4, local port is 179
Remote TCP address is 10.255.255.11, remote port is 34371
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
    Retransmission Timeout (rto): 204.0ms
    Round-trip Time (rtt/rtvar): 4.0ms/0.9ms
    Delayed Ack Timeout (ato): 40.0ms
    Congestion Window (cwnd): 10
    TCP Throughput: 27.50 Mbps
    Advertised Recv Window (rcv_space): 14600

BGP neighbor is 10.255.255.12, remote AS 65000, internal link
  BGP version 4, remote router ID 10.255.255.12, VRF default
  Inherits configuration from and member of peer-group autovpnEdges
  Last read 00:00:34, last write 00:00:19
  Hold time is 180, keepalive interval is 60 seconds
  Configured hold time is 180, keepalive interval is 60 seconds
  Effective minimum hold time is 3 seconds
  Send failure hold time is 0 seconds
  Hold timer is active, time left: 00:02:26
  Keepalive timer is active, time left: 00:00:23
  Connect timer is inactive
  Idle-restart timer is inactive
  BGP state is Established, up for 05:35:37
  Number of transitions to established: 1
  Last state was OpenConfirm
  Last event was RecvKeepAlive
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
      Received 05:35:20
      Number of stale paths removed after graceful restart: 0
      Number of paths received before End-of-RIB: 2
    L2VPN EVPN End-of-RIB received: Yes
      Received 05:35:20
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
    Updates:                        89         9
    Keepalives:                    381       394
    Enhanced Route Refresh:          0         0
    Begin of Route Refresh:          0         0
    End of Route Refresh:            0         0
    Total messages:                471       404
  Prefix Statistics:
                                   Sent      Rcvd     Best Paths     Best ECMP Paths
    IPv4 Unicast:                     0         0              0                   0
    IPv4 Dps:                        22         2              2                   2
    IPv6 Unicast:                     0         0              0                   0
    EVPN:                            20         2              2                   2
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
Local AS is 65000, local router ID 10.255.255.4
TTL is 255
Local TCP address is 10.255.255.4, local port is 179
Remote TCP address is 10.255.255.12, remote port is 44173
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
    Round-trip Time (rtt/rtvar): 4.2ms/0.8ms
    Delayed Ack Timeout (ato): 40.0ms
    Congestion Window (cwnd): 10
    TCP Throughput: 26.25 Mbps
    Recv Round-trip Time (rcv_rtt): 5.0ms
    Advertised Recv Window (rcv_space): 14600

```

## show bgp path-selection detail

```text
BGP routing table information for VRF default
Router identifier 10.255.255.4, local AS number 65000
Bgp routing table entry for ipv4Dps VTEP 10.255.255.5/32
 Paths: 2 available
  Local (Received from a RR-client)
    :: from 10.255.255.5 (10.255.255.5)
      Origin IGP, metric -, localpref 100, weight 0, received 00:36:52 ago, valid, internal
      Tunnel encapsulation attribute: Dynamic path selection
        Endpoint: 172.16.0.1, Path group name: VZ_OFF, WAN ID: 1, UDP port: 4500
  Local (Received from a RR-client)
    :: from 10.255.255.1 (10.255.255.1)
      Origin IGP, metric -, localpref 100, weight 0, received 00:36:51 ago, valid, internal
      Tunnel encapsulation attribute: Dynamic path selection
        Endpoint: 172.16.0.1, Path group name: VZ_OFF, WAN ID: 1, UDP port: 4500
Bgp routing table entry for ipv4Dps VTEP 10.255.255.6/32
 Paths: 2 available
  Local (Received from a RR-client)
    :: from 10.255.255.6 (10.255.255.6)
      Origin IGP, metric -, localpref 100, weight 0, received 06:24:38 ago, valid, internal
      Tunnel encapsulation attribute: Dynamic path selection
        Endpoint: 172.16.0.3, Path group name: VZ_OFF, WAN ID: 1, UDP port: 4500
  Local (Received from a RR-client)
    :: from 10.255.255.1 (10.255.255.1)
      Origin IGP, metric -, localpref 100, weight 0, received 02:08:42 ago, valid, internal
      Tunnel encapsulation attribute: Dynamic path selection
        Endpoint: 172.16.0.3, Path group name: VZ_OFF, WAN ID: 1, UDP port: 4500
Bgp routing table entry for ipv4Dps VTEP 10.255.255.8/32
 Paths: 2 available
  Local (Received from a RR-client)
    :: from 10.255.255.8 (10.255.255.8)
      Origin IGP, metric -, localpref 100, weight 0, received 05:45:53 ago, valid, internal
      Tunnel encapsulation attribute: Dynamic path selection
        Endpoint: 172.16.1.2, Path group name: VZ_NEAR, WAN ID: 1, UDP port: 4500
  Local (Received from a RR-client)
    :: from 10.255.255.1 (10.255.255.1)
      Origin IGP, metric -, localpref 100, weight 0, received 02:08:42 ago, valid, internal
      Tunnel encapsulation attribute: Dynamic path selection
        Endpoint: 172.16.1.2, Path group name: VZ_NEAR, WAN ID: 1, UDP port: 4500
Bgp routing table entry for ipv4Dps VTEP 10.255.255.10/32
 Paths: 2 available
  Local (Received from a RR-client)
    :: from 10.255.255.10 (10.255.255.10)
      Origin IGP, metric -, localpref 100, weight 0, received 04:27:30 ago, valid, internal
      Tunnel encapsulation attribute: Dynamic path selection
        Endpoint: 172.16.1.7, Path group name: VZ_NEAR, WAN ID: 1, UDP port: 4500
  Local (Received from a RR-client)
    :: from 10.255.255.1 (10.255.255.1)
      Origin IGP, metric -, localpref 100, weight 0, received 02:08:42 ago, valid, internal
      Tunnel encapsulation attribute: Dynamic path selection
        Endpoint: 172.16.1.7, Path group name: VZ_NEAR, WAN ID: 1, UDP port: 4500
Bgp routing table entry for ipv4Dps VTEP 10.255.255.11/32
 Paths: 2 available
  Local (Received from a RR-client)
    :: from 10.255.255.1 (10.255.255.1)
      Origin IGP, metric -, localpref 100, weight 0, received 00:45:59 ago, valid, internal
      Tunnel encapsulation attribute: Dynamic path selection
        Endpoint: 172.16.0.9, Path group name: VZ_OFF, WAN ID: 2, UDP port: 4500
  Local (Received from a RR-client)
    :: from 10.255.255.11 (10.255.255.11)
      Origin IGP, metric -, localpref 100, weight 0, received 00:45:58 ago, valid, internal
      Tunnel encapsulation attribute: Dynamic path selection
        Endpoint: 172.16.0.9, Path group name: VZ_OFF, WAN ID: 2, UDP port: 4500
Bgp routing table entry for ipv4Dps VTEP 10.255.255.12/32
 Paths: 2 available
  Local (Received from a RR-client)
    :: from 10.255.255.12 (10.255.255.12)
      Origin IGP, metric -, localpref 100, weight 0, received 05:35:39 ago, valid, internal
      Tunnel encapsulation attribute: Dynamic path selection
        Endpoint: 172.16.0.11, Path group name: VZ_OFF, WAN ID: 2, UDP port: 4500
  Local (Received from a RR-client)
    :: from 10.255.255.1 (10.255.255.1)
      Origin IGP, metric -, localpref 100, weight 0, received 02:08:42 ago, valid, internal
      Tunnel encapsulation attribute: Dynamic path selection
        Endpoint: 172.16.0.11, Path group name: VZ_OFF, WAN ID: 2, UDP port: 4500
Bgp routing table entry for ipv4Ipsec VTEP 10.255.255.5/32
 Paths: 2 available
  Local (Received from a RR-client)
    :: from 10.255.255.5 (10.255.255.5)
      Origin IGP, metric -, localpref 100, weight 0, received 00:36:52 ago, valid, internal
      Tunnel encapsulation attribute: IP security
        Initial contact: false, Rekey counter: 0, Nonce length: 32
        DH group: 14, DH key length: 256
        Encryption algo: aes256, Authentication algo: sha256
  Local (Received from a RR-client)
    :: from 10.255.255.1 (10.255.255.1)
      Origin IGP, metric -, localpref 100, weight 0, received 00:36:51 ago, valid, internal
      Tunnel encapsulation attribute: IP security
        Initial contact: false, Rekey counter: 0, Nonce length: 32
        DH group: 14, DH key length: 256
        Encryption algo: aes256, Authentication algo: sha256
Bgp routing table entry for ipv4Ipsec VTEP 10.255.255.6/32
 Paths: 2 available
  Local (Received from a RR-client)
    :: from 10.255.255.6 (10.255.255.6)
      Origin IGP, metric -, localpref 100, weight 0, received 04:06:14 ago, valid, internal
      Tunnel encapsulation attribute: IP security
        Initial contact: false, Rekey counter: 2, Nonce length: 32
        DH group: 14, DH key length: 256
        Encryption algo: aes256, Authentication algo: sha256
  Local (Received from a RR-client)
    :: from 10.255.255.1 (10.255.255.1)
      Origin IGP, metric -, localpref 100, weight 0, received 02:08:42 ago, valid, internal
      Tunnel encapsulation attribute: IP security
        Initial contact: false, Rekey counter: 2, Nonce length: 32
        DH group: 14, DH key length: 256
        Encryption algo: aes256, Authentication algo: sha256
Bgp routing table entry for ipv4Ipsec VTEP 10.255.255.8/32
 Paths: 2 available
  Local (Received from a RR-client)
    :: from 10.255.255.8 (10.255.255.8)
      Origin IGP, metric -, localpref 100, weight 0, received 05:45:53 ago, valid, internal
      Tunnel encapsulation attribute: IP security
        Initial contact: false, Rekey counter: 0, Nonce length: 32
        DH group: 14, DH key length: 256
        Encryption algo: aes256, Authentication algo: sha256
  Local (Received from a RR-client)
    :: from 10.255.255.1 (10.255.255.1)
      Origin IGP, metric -, localpref 100, weight 0, received 02:08:42 ago, valid, internal
      Tunnel encapsulation attribute: IP security
        Initial contact: false, Rekey counter: 0, Nonce length: 32
        DH group: 14, DH key length: 256
        Encryption algo: aes256, Authentication algo: sha256
Bgp routing table entry for ipv4Ipsec VTEP 10.255.255.10/32
 Paths: 2 available
  Local (Received from a RR-client)
    :: from 10.255.255.10 (10.255.255.10)
      Origin IGP, metric -, localpref 100, weight 0, received 04:27:30 ago, valid, internal
      Tunnel encapsulation attribute: IP security
        Initial contact: false, Rekey counter: 0, Nonce length: 32
        DH group: 14, DH key length: 256
        Encryption algo: aes256, Authentication algo: sha256
  Local (Received from a RR-client)
    :: from 10.255.255.1 (10.255.255.1)
      Origin IGP, metric -, localpref 100, weight 0, received 02:08:42 ago, valid, internal
      Tunnel encapsulation attribute: IP security
        Initial contact: false, Rekey counter: 0, Nonce length: 32
        DH group: 14, DH key length: 256
        Encryption algo: aes256, Authentication algo: sha256
Bgp routing table entry for ipv4Ipsec VTEP 10.255.255.11/32
 Paths: 2 available
  Local (Received from a RR-client)
    :: from 10.255.255.1 (10.255.255.1)
      Origin IGP, metric -, localpref 100, weight 0, received 00:45:59 ago, valid, internal
      Tunnel encapsulation attribute: IP security
        Initial contact: false, Rekey counter: 0, Nonce length: 32
        DH group: 14, DH key length: 256
        Encryption algo: aes256, Authentication algo: sha256
  Local (Received from a RR-client)
    :: from 10.255.255.11 (10.255.255.11)
      Origin IGP, metric -, localpref 100, weight 0, received 00:45:58 ago, valid, internal
      Tunnel encapsulation attribute: IP security
        Initial contact: false, Rekey counter: 0, Nonce length: 32
        DH group: 14, DH key length: 256
        Encryption algo: aes256, Authentication algo: sha256
Bgp routing table entry for ipv4Ipsec VTEP 10.255.255.12/32
 Paths: 2 available
  Local (Received from a RR-client)
    :: from 10.255.255.12 (10.255.255.12)
      Origin IGP, metric -, localpref 100, weight 0, received 05:35:39 ago, valid, internal
      Tunnel encapsulation attribute: IP security
        Initial contact: false, Rekey counter: 0, Nonce length: 32
        DH group: 14, DH key length: 256
        Encryption algo: aes256, Authentication algo: sha256
  Local (Received from a RR-client)
    :: from 10.255.255.1 (10.255.255.1)
      Origin IGP, metric -, localpref 100, weight 0, received 02:08:42 ago, valid, internal
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
>C    10.255.255.4/32 [0 pref/0 metric] updated 1d00h ago
         via Loopback0, directly connected
>C    172.16.0.6/31 [0 pref/0 metric] updated 1d07h ago
         via Ethernet1/4, directly connected
>C    172.16.1.4/31 [0 pref/0 metric] updated 1d07h ago
         via Ethernet1/3, directly connected
>C    172.28.128.0/20 [0 pref/0 metric] updated 3d22h ago
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
>S    10.80.0.0/12 [1 pref/0 metric] updated 3d22h ago
         via 172.28.128.1 [0 pref/0 metric] type ipv4
            via 172.28.128.1, Management1/1
>S    10.224.0.0/12 [1 pref/0 metric] updated 3d22h ago
         via 172.28.128.1 [0 pref/0 metric] type ipv4
            via 172.28.128.1, Management1/1
>S    10.240.0.0/12 [1 pref/0 metric] updated 3d22h ago
         via 172.28.128.1 [0 pref/0 metric] type ipv4
            via 172.28.128.1, Management1/1
>S    172.16.0.0/12 [1 pref/0 metric] updated 3d22h ago
         via 172.28.128.1 [0 pref/0 metric] type ipv4
            via 172.28.128.1, Management1/1
>S    172.16.0.0/24 [1 pref/0 metric] updated 23:13:05 ago
         via 172.16.0.6 [0 pref/0 metric] type ipv4
            via 172.16.0.6, Ethernet1/4
>S    172.16.1.0/24 [1 pref/0 metric] updated 23:16:43 ago
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
>P    0.0.0.0/8 [1 pref/0 metric] updated 3d22h ago
         via Null0, directly connected [NF]
>P    10.255.255.1/32 [1 pref/0 metric] updated 03:05:09 ago
         via 10.255.255.1, Dps1
>P    10.255.255.5/32 [1 pref/0 metric] updated 00:36:59 ago
         via 10.255.255.5, Dps1
>P    10.255.255.6/32 [1 pref/0 metric] updated 06:25:06 ago
         via 10.255.255.6, Dps1
>P    10.255.255.8/32 [1 pref/0 metric] updated 05:46:07 ago
         via 10.255.255.8, Dps1
>P    10.255.255.10/32 [1 pref/0 metric] updated 04:27:36 ago
         via 10.255.255.10, Dps1
>P    10.255.255.11/32 [1 pref/0 metric] updated 00:46:05 ago
         via 10.255.255.11, Dps1
>P    10.255.255.12/32 [1 pref/0 metric] updated 05:37:25 ago
         via 10.255.255.12, Dps1
>P    127.0.0.0/8 [1 pref/0 metric] updated 3d22h ago
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
>P    ::/96 [1 pref/0 metric] updated 23:53:54 ago
         via Null0, directly connected [NF]
>P    ::ffff:127.0.0.0/104 [1 pref/0 metric] updated 23:53:54 ago
         via :: [1 pref/1 metric] type ipv6
            via , directly connected
>P    fe80::/10 [1 pref/0 metric] updated 23:53:54 ago
```

## 

```text
```

