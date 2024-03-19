# Test results for IND355

## show version

```text
Arista AWE-5510-F
Hardware version: 11.01
Serial number: WTW23160927
Hardware MAC address: ec8a.4804.f530
System MAC address: ec8a.4804.f530

Software image version: 4.31.2F
Architecture: x86_64
Internal build version: 4.31.2F-35442176.4312F
Internal build ID: 500c58e3-5beb-4481-afe9-8ad77245cc44
Image format version: 3.0
Image optimization: Default

Uptime: 18 minutes
Total memory: 65396488 kB
Free memory: 39968032 kB

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
Ethernet1/1      10.1.255.1/31        up         up              1500          
Ethernet1/2      172.16.0.4/31        up         up              9000          
Ethernet1/3      172.16.1.0/31        up         up              9000          
Ethernet1/15     172.16.255.3/31      up         up              9000          
Loopback0        10.255.255.1/32      up         up             65535          
Management1/1    172.28.137.226/20    up         up              1500          

```

## show interfaces counters rates | nz

```text
Port      Name      Intvl  In Mbps      %  In Kpps Out Mbps      % Out Kpps
Et1/1     CE         5:00    120.9   1.2%       15    324.0   3.3%       40
Et1/2     VZ_OFF     5:00    290.3   3.0%       33    261.0   2.7%       30
Et1/3     VZ_NEAR    5:00    251.0   2.6%       29    184.7   1.9%       21
Et1/15               5:00    312.8   3.2%       39    198.2   2.0%       24
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
           via 172.16.0.5, Ethernet1/2

 S        10.80.0.0/12 [1/0]
           via 172.28.128.1, Management1/1
 S        10.224.0.0/12 [1/0]
           via 172.28.128.1, Management1/1
 C        10.255.255.1/32
           directly connected, Loopback0
 S        10.255.255.2/32
           directly connected, Dps1
 S        10.255.255.4/32
           directly connected, Dps1
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
 C        172.16.0.4/31
           directly connected, Ethernet1/2
 S        172.16.0.0/24 [1/0]
           via 172.16.0.5, Ethernet1/2
 C        172.16.1.0/31
           directly connected, Ethernet1/3
 S        172.16.1.0/24 [1/0]
           via 172.16.1.1, Ethernet1/3
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
           via 172.16.0.5, Ethernet1/2

 S        10.80.0.0/12 [1/0]
           via 172.28.128.1, Management1/1
 S        10.224.0.0/12 [1/0]
           via 172.28.128.1, Management1/1
 C        10.255.255.1/32
           directly connected, Loopback0
 S        10.255.255.2/32
           directly connected, Dps1
 S        10.255.255.4/32
           directly connected, Dps1
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
 C        172.16.0.4/31
           directly connected, Ethernet1/2
 S        172.16.0.0/24 [1/0]
           via 172.16.0.5, Ethernet1/2
 C        172.16.1.0/31
           directly connected, Ethernet1/3
 S        172.16.1.0/24 [1/0]
           via 172.16.1.1, Ethernet1/3
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
           via VTEP 10.255.255.6 VNI 201 router-mac ec:8a:48:04:2b:ae
 C        10.1.255.0/31
           directly connected, Ethernet1/1
 B I      10.1.255.2/31 [20/0]
           via 172.16.255.2, Ethernet1/15
 B I      10.2.255.0/31 [20/0]
           via 172.16.255.2, Ethernet1/15
 B I      10.2.255.2/31 [20/0]
           via VTEP 10.255.255.8 VNI 201 router-mac ec:8a:48:04:2c:53
 B I      10.4.255.0/31 [20/0]
           via 172.16.255.2, Ethernet1/15
 B I      10.4.255.2/31 [20/0]
           via VTEP 10.255.255.10 VNI 201 router-mac 00:0c:29:d5:32:d4
 B I      10.5.255.0/31 [20/0]
           via 172.16.255.2, Ethernet1/15
 B I      10.5.255.2/31 [20/0]
           via VTEP 10.255.255.4 VNI 201 router-mac ec:8a:48:04:ff:5b
 B I      10.6.255.0/31 [20/0]
           via VTEP 10.255.255.11 VNI 201 router-mac 00:0c:29:ba:2d:5e
 B I      10.6.255.2/31 [20/0]
           via VTEP 10.255.255.12 VNI 201 router-mac 00:0c:29:78:c5:2d
 B I      10.255.254.1/32 [20/0]
           via VTEP 10.255.255.6 VNI 201 router-mac ec:8a:48:04:2b:ae
           via VTEP 10.255.255.5 VNI 201 router-mac ec:8a:48:04:21:53
 O        10.255.254.2/32 [110/20]
           via 10.1.255.0, Ethernet1/1
 B I      10.255.254.3/32 [20/0]
           via VTEP 10.255.255.8 VNI 201 router-mac ec:8a:48:04:2c:53
 B I      10.255.254.4/32 [20/0]
           via VTEP 10.255.255.12 VNI 201 router-mac 00:0c:29:78:c5:2d
           via VTEP 10.255.255.11 VNI 201 router-mac 00:0c:29:ba:2d:5e
 B I      10.255.254.5/32 [20/0]
           via VTEP 10.255.255.10 VNI 201 router-mac 00:0c:29:d5:32:d4
 B I      10.255.254.6/32 [20/0]
           via VTEP 10.255.255.4 VNI 201 router-mac ec:8a:48:04:ff:5b
 B I      172.16.255.0/31 [20/0]
           via VTEP 10.255.255.4 VNI 201 router-mac ec:8a:48:04:ff:5b
 C        172.16.255.2/31
           directly connected, Ethernet1/15
 B I      192.168.0.0/24 [20/0]
           via VTEP 10.255.255.6 VNI 201 router-mac ec:8a:48:04:2b:ae
           via VTEP 10.255.255.5 VNI 201 router-mac ec:8a:48:04:21:53
 O        192.168.1.0/24 [110/20]
           via 10.1.255.0, Ethernet1/1
 B I      192.168.3.0/24 [20/0]
           via VTEP 10.255.255.8 VNI 201 router-mac ec:8a:48:04:2c:53
 B I      192.168.5.0/24 [20/0]
           via VTEP 10.255.255.4 VNI 201 router-mac ec:8a:48:04:ff:5b
 B I      192.168.6.0/24 [20/0]
           via VTEP 10.255.255.12 VNI 201 router-mac 00:0c:29:78:c5:2d
           via VTEP 10.255.255.11 VNI 201 router-mac 00:0c:29:ba:2d:5e
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
Router identifier 10.255.255.1, local AS number 65000
Route status codes: * - valid, > - active, S - Stale, E - ECMP head, e - ECMP
                    c - Contributing to ECMP, % - Pending best path selection
Origin codes: i - IGP, e - EGP, ? - incomplete
AS Path Attributes: Or-ID - Originator ID, C-LST - Cluster List, LL Nexthop - Link Local Nexthop

          Network                Next Hop              Metric  LocPref Weight  Path
 * >      RD: 10.255.255.5:1 ip-prefix 10.0.255.0/31
                                 10.255.255.5          -       100     0       i
 * >      RD: 10.255.255.6:1 ip-prefix 10.0.255.2/31
                                 10.255.255.6          -       100     0       i
 * >      RD: 10.255.255.1:1 ip-prefix 10.1.255.0/31
                                 -                     -       -       0       i
 * >      RD: 10.255.255.1:1 ip-prefix 10.1.255.2/31
                                 -                     -       5       0       i
 * >      RD: 10.255.255.4:1 ip-prefix 10.1.255.2/31
                                 10.255.255.4          -       5       0       i
 * >      RD: 10.255.255.1:1 ip-prefix 10.2.255.0/31
                                 -                     -       5       0       i
 * >      RD: 10.255.255.4:1 ip-prefix 10.2.255.0/31
                                 10.255.255.4          -       5       0       i
 * >      RD: 10.255.255.7:1 ip-prefix 10.2.255.2/31
                                 10.255.255.8          -       100     0       i
 * >      RD: 10.255.255.1:1 ip-prefix 10.4.255.0/31
                                 -                     -       5       0       i
 * >      RD: 10.255.255.4:1 ip-prefix 10.4.255.0/31
                                 10.255.255.4          -       5       0       i Or-ID: 10.255.255.9 C-LST: 10.255.255.4 172.16.255.0 10.255.255.2 
 * >      RD: 10.255.255.10:1 ip-prefix 10.4.255.2/31
                                 10.255.255.10         -       100     0       i
 * >      RD: 10.255.255.1:1 ip-prefix 10.5.255.0/31
                                 -                     -       5       0       i
 * >      RD: 10.255.255.4:1 ip-prefix 10.5.255.0/31
                                 10.255.255.4          -       5       0       i
 * >      RD: 10.255.255.4:1 ip-prefix 10.5.255.2/31
                                 10.255.255.4          -       100     0       i
 * >      RD: 10.255.255.11:1 ip-prefix 10.6.255.0/31
                                 10.255.255.11         -       100     0       i
 * >      RD: 10.255.255.12:1 ip-prefix 10.6.255.2/31
                                 10.255.255.12         -       100     0       i
 * >      RD: 10.255.255.5:1 ip-prefix 10.255.254.1/32
                                 10.255.255.5          -       100     0       i
 * >Ec    RD: 10.255.255.6:1 ip-prefix 10.255.254.1/32
                                 10.255.255.6          -       100     0       i
 *  ec    RD: 10.255.255.6:1 ip-prefix 10.255.254.1/32
                                 10.255.255.6          -       100     0       i Or-ID: 10.255.255.6 C-LST: 10.255.255.4 
 * >      RD: 10.255.255.1:1 ip-prefix 10.255.254.2/32
                                 -                     -       -       0       i
          RD: 10.255.255.4:1 ip-prefix 10.255.254.2/32
                                 PolicyReject          -       -       0       i
 * >      RD: 10.255.255.1:1 ip-prefix 10.255.254.3/32
                                 -                     -       5       0       i
 * >      RD: 10.255.255.4:1 ip-prefix 10.255.254.3/32
                                 10.255.255.4          -       5       0       i
 * >Ec    RD: 10.255.255.7:1 ip-prefix 10.255.254.3/32
                                 10.255.255.8          -       100     0       i
 *  ec    RD: 10.255.255.7:1 ip-prefix 10.255.254.3/32
                                 10.255.255.8          -       100     0       i Or-ID: 10.255.255.8 C-LST: 10.255.255.4 
 * >      RD: 10.255.255.11:1 ip-prefix 10.255.254.4/32
                                 10.255.255.11         -       100     0       i
 * >      RD: 10.255.255.12:1 ip-prefix 10.255.254.4/32
                                 10.255.255.12         -       100     0       i
 * >      RD: 10.255.255.10:1 ip-prefix 10.255.254.5/32
                                 10.255.255.10         -       100     0       i
 * >      RD: 10.255.255.1:1 ip-prefix 10.255.254.6/32
                                 -                     -       5       0       i
 * >      RD: 10.255.255.4:1 ip-prefix 10.255.254.6/32
                                 10.255.255.4          -       100     0       i
 * >      RD: 10.255.255.1:1 ip-prefix 172.16.255.0/31
                                 -                     -       5       0       i
 * >      RD: 10.255.255.4:1 ip-prefix 172.16.255.0/31
                                 10.255.255.4          -       100     0       i
 * >      RD: 10.255.255.1:1 ip-prefix 172.16.255.2/31
                                 -                     -       -       0       i
 *        RD: 10.255.255.1:1 ip-prefix 172.16.255.2/31
                                 -                     -       5       0       i
 * >      RD: 10.255.255.4:1 ip-prefix 172.16.255.2/31
                                 10.255.255.4          -       5       0       i
 * >      RD: 10.255.255.5:1 ip-prefix 192.168.0.0/24
                                 10.255.255.5          -       100     0       i
 * >Ec    RD: 10.255.255.6:1 ip-prefix 192.168.0.0/24
                                 10.255.255.6          -       100     0       i
 *  ec    RD: 10.255.255.6:1 ip-prefix 192.168.0.0/24
                                 10.255.255.6          -       100     0       i Or-ID: 10.255.255.6 C-LST: 10.255.255.4 
 * >      RD: 10.255.255.1:1 ip-prefix 192.168.1.0/24
                                 -                     -       -       0       i
          RD: 10.255.255.4:1 ip-prefix 192.168.1.0/24
                                 PolicyReject          -       -       0       i
 * >      RD: 10.255.255.1:1 ip-prefix 192.168.3.0/24
                                 -                     -       5       0       i
 * >      RD: 10.255.255.4:1 ip-prefix 192.168.3.0/24
                                 10.255.255.4          -       5       0       i
 * >Ec    RD: 10.255.255.7:1 ip-prefix 192.168.3.0/24
                                 10.255.255.8          -       100     0       i
 *  ec    RD: 10.255.255.7:1 ip-prefix 192.168.3.0/24
                                 10.255.255.8          -       100     0       i Or-ID: 10.255.255.8 C-LST: 10.255.255.4 
 * >      RD: 10.255.255.1:1 ip-prefix 192.168.5.0/24
                                 -                     -       5       0       i
 * >      RD: 10.255.255.4:1 ip-prefix 192.168.5.0/24
                                 10.255.255.4          -       100     0       i
 * >      RD: 10.255.255.11:1 ip-prefix 192.168.6.0/24
                                 10.255.255.11         -       100     0       i
 * >      RD: 10.255.255.12:1 ip-prefix 192.168.6.0/24
                                 10.255.255.12         -       100     0       i
 * >      RD: 10.255.255.10:1 ip-prefix 192.168.40.0/24
                                 10.255.255.10         -       100     0       i
```

## show ip security connection detail

```text
path1:
  Source address: 172.16.0.4, Destination address: 172.16.0.3
  State: established
  Uptime: 15 minutes, 51 seconds
  VRF: default
  Type: static
  Remote IP: 10.255.255.8
  Role: responder
  Inbound SPI: 0xca96bc:
    Request ID: 7, Mode: transport, Replay window size: 16384, Seq: 0x0
    Errors:
      Packets outside replay window: 0, Replay: 0, Integrity failed: 0
    Lifetime config:
      Soft byte limit: 4238608643249, Hard byte limit: 6442450944000
      Soft packet limit: 2473979280, Hard packet limit: 4000000000
      Soft time limit: 3057 secs, Hard time limit: 3600 secs
    Lifetime current:
      Current bytes: 10686452588
      Current packets: 10112567
      SA add time: Thu Mar 14 13:18:38 2024
      SA last use time: Thu Mar 14 13:35:06 2024
  Outbound SPI: 0xca07fc:
    Request ID: 7, Mode: transport, Replay window size: 0, Seq: 0x0
    Errors:
      Packets outside replay window: 0, Replay: 0, Integrity failed: 0
    Lifetime config:
      Soft byte limit: 4346704283999, Hard byte limit: 6442450944000
      Soft packet limit: 2690550040, Hard packet limit: 4000000000
      Soft time limit: 2729 secs, Hard time limit: 3600 secs
    Lifetime current:
      Current bytes: 7851600100
      Current packets: 15668320
      SA add time: Thu Mar 14 13:18:38 2024
      SA last use time: Thu Mar 14 13:35:06 2024
path2:
  Source address: 172.16.1.0, Destination address: 172.16.0.3
  State: idle
  Uptime: N/A
  VRF: default
  Type: static
  Remote IP: 10.255.255.8
  Role: responder
path3:
  Source address: 172.16.0.4, Destination address: 172.16.0.1
  State: established
  Uptime: 14 minutes, 55 seconds
  VRF: default
  Type: static
  Remote IP: 10.255.255.8
  Role: responder
  Inbound SPI: 0xcd8f85:
    Request ID: 4, Mode: transport, Replay window size: 16384, Seq: 0x0
    Errors:
      Packets outside replay window: 0, Replay: 0, Integrity failed: 0
    Lifetime config:
      Soft byte limit: 4785594401999, Hard byte limit: 6442450944000
      Soft packet limit: 2953730307, Hard packet limit: 4000000000
      Soft time limit: 2625 secs, Hard time limit: 3600 secs
    Lifetime current:
      Current bytes: 10306261276
      Current packets: 9748367
      SA add time: Thu Mar 14 13:19:34 2024
      SA last use time: Thu Mar 14 13:35:06 2024
  Outbound SPI: 0xcd0c98:
    Request ID: 4, Mode: transport, Replay window size: 0, Seq: 0x0
    Errors:
      Packets outside replay window: 0, Replay: 0, Integrity failed: 0
    Lifetime config:
      Soft byte limit: 4177179128249, Hard byte limit: 6442450944000
      Soft packet limit: 2869902184, Hard packet limit: 4000000000
      Soft time limit: 3051 secs, Hard time limit: 3600 secs
    Lifetime current:
      Current bytes: 8402853322
      Current packets: 16645490
      SA add time: Thu Mar 14 13:19:34 2024
      SA last use time: Thu Mar 14 13:35:06 2024
path4:
  Source address: 172.16.1.0, Destination address: 172.16.0.1
  State: idle
  Uptime: N/A
  VRF: default
  Type: static
  Remote IP: 10.255.255.8
  Role: responder
path5:
  Source address: 172.16.1.0, Destination address: 172.16.1.2
  State: established
  Uptime: 14 minutes, 45 seconds
  VRF: default
  Type: static
  Remote IP: 10.255.255.8
  Role: responder
  Inbound SPI: 0xc3aaa6:
    Request ID: 9, Mode: transport, Replay window size: 16384, Seq: 0x0
    Errors:
      Packets outside replay window: 0, Replay: 0, Integrity failed: 0
    Lifetime config:
      Soft byte limit: 3806482929749, Hard byte limit: 6442450944000
      Soft packet limit: 2636823941, Hard packet limit: 4000000000
      Soft time limit: 2610 secs, Hard time limit: 3600 secs
    Lifetime current:
      Current bytes: 7194067704
      Current packets: 6815266
      SA add time: Thu Mar 14 13:19:44 2024
      SA last use time: Thu Mar 14 13:35:06 2024
  Outbound SPI: 0xc637d0:
    Request ID: 9, Mode: transport, Replay window size: 0, Seq: 0x0
    Errors:
      Packets outside replay window: 0, Replay: 0, Integrity failed: 0
    Lifetime config:
      Soft byte limit: 4473213318749, Hard byte limit: 6442450944000
      Soft packet limit: 2773145227, Hard packet limit: 4000000000
      Soft time limit: 3002 secs, Hard time limit: 3600 secs
    Lifetime current:
      Current bytes: 2003157246
      Current packets: 3983324
      SA add time: Thu Mar 14 13:19:44 2024
      SA last use time: Thu Mar 14 13:35:06 2024
path6:
  Source address: 172.16.0.4, Destination address: 172.16.1.2
  State: idle
  Uptime: N/A
  VRF: default
  Type: static
  Remote IP: 10.255.255.8
  Role: responder
path7:
  Source address: 172.16.1.0, Destination address: 172.16.0.9
  State: idle
  Uptime: N/A
  VRF: default
  Type: static
  Remote IP: 10.255.255.8
  Role: responder
path8:
  Source address: 172.16.0.4, Destination address: 172.16.0.9
  State: established
  Uptime: 13 minutes
  VRF: default
  Type: static
  Remote IP: 10.255.255.8
  Role: responder
  Inbound SPI: 0xc81075:
    Request ID: 12, Mode: transport, Replay window size: 16384, Seq: 0x0
    Errors:
      Packets outside replay window: 0, Replay: 0, Integrity failed: 0
    Lifetime config:
      Soft byte limit: 3612744434999, Hard byte limit: 6442450944000
      Soft packet limit: 2105427405, Hard packet limit: 4000000000
      Soft time limit: 2535 secs, Hard time limit: 3600 secs
    Lifetime current:
      Current bytes: 7495186496
      Current packets: 7083592
      SA add time: Thu Mar 14 13:21:30 2024
      SA last use time: Thu Mar 14 13:35:06 2024
  Outbound SPI: 0xc337f9:
    Request ID: 12, Mode: transport, Replay window size: 0, Seq: 0x0
    Errors:
      Packets outside replay window: 0, Replay: 0, Integrity failed: 0
    Lifetime config:
      Soft byte limit: 4630127605499, Hard byte limit: 6442450944000
      Soft packet limit: 2579406687, Hard packet limit: 4000000000
      Soft time limit: 2532 secs, Hard time limit: 3600 secs
    Lifetime current:
      Current bytes: 6676995889
      Current packets: 13195188
      SA add time: Thu Mar 14 13:21:30 2024
      SA last use time: Thu Mar 14 13:35:06 2024
path9:
  Source address: 172.16.1.0, Destination address: 172.16.0.11
  State: idle
  Uptime: N/A
  VRF: default
  Type: static
  Remote IP: 10.255.255.8
  Role: responder
path10:
  Source address: 172.16.0.4, Destination address: 172.16.0.11
  State: established
  Uptime: 16 minutes, 4 seconds
  VRF: default
  Type: static
  Remote IP: 10.255.255.8
  Role: responder
  Inbound SPI: 0xcaec24:
    Request ID: 2, Mode: transport, Replay window size: 16384, Seq: 0x0
    Errors:
      Packets outside replay window: 0, Replay: 0, Integrity failed: 0
    Lifetime config:
      Soft byte limit: 3699799382999, Hard byte limit: 6442450944000
      Soft packet limit: 2845861196, Hard packet limit: 4000000000
      Soft time limit: 2700 secs, Hard time limit: 3600 secs
    Lifetime current:
      Current bytes: 13515520180
      Current packets: 12783765
      SA add time: Thu Mar 14 13:18:25 2024
      SA last use time: Thu Mar 14 13:35:06 2024
  Outbound SPI: 0xcc651c:
    Request ID: 2, Mode: transport, Replay window size: 0, Seq: 0x0
    Errors:
      Packets outside replay window: 0, Replay: 0, Integrity failed: 0
    Lifetime config:
      Soft byte limit: 4659315887249, Hard byte limit: 6442450944000
      Soft packet limit: 2264190142, Hard packet limit: 4000000000
      Soft time limit: 2563 secs, Hard time limit: 3600 secs
    Lifetime current:
      Current bytes: 12806052302
      Current packets: 25390634
      SA add time: Thu Mar 14 13:18:25 2024
      SA last use time: Thu Mar 14 13:35:06 2024
path11:
  Source address: 172.16.1.0, Destination address: 172.16.1.7
  State: established
  Uptime: 14 minutes, 10 seconds
  VRF: default
  Type: static
  Remote IP: 10.255.255.8
  Role: responder
  Inbound SPI: 0xc6e5be:
    Request ID: 10, Mode: transport, Replay window size: 16384, Seq: 0x0
    Errors:
      Packets outside replay window: 0, Replay: 0, Integrity failed: 0
    Lifetime config:
      Soft byte limit: 4575253817249, Hard byte limit: 6442450944000
      Soft packet limit: 2133035624, Hard packet limit: 4000000000
      Soft time limit: 2881 secs, Hard time limit: 3600 secs
    Lifetime current:
      Current bytes: 7761494836
      Current packets: 7343037
      SA add time: Thu Mar 14 13:20:19 2024
      SA last use time: Thu Mar 14 13:35:06 2024
  Outbound SPI: 0xcbead8:
    Request ID: 10, Mode: transport, Replay window size: 0, Seq: 0x0
    Errors:
      Packets outside replay window: 0, Replay: 0, Integrity failed: 0
    Lifetime config:
      Soft byte limit: 3443214991499, Hard byte limit: 6442450944000
      Soft packet limit: 2978896822, Hard packet limit: 4000000000
      Soft time limit: 2522 secs, Hard time limit: 3600 secs
    Lifetime current:
      Current bytes: 11654898229
      Current packets: 23168460
      SA add time: Thu Mar 14 13:20:19 2024
      SA last use time: Thu Mar 14 13:35:06 2024
path12:
  Source address: 172.16.0.4, Destination address: 172.16.1.7
  State: idle
  Uptime: N/A
  VRF: default
  Type: static
  Remote IP: 10.255.255.8
  Role: responder
path13:
  Source address: 172.16.1.0, Destination address: 172.16.1.5
  State: established
  Uptime: 16 minutes, 10 seconds
  VRF: default
  Type: static
  Remote IP: 10.255.255.8
  Role: responder
  Inbound SPI: 0xc62e26:
    Request ID: 1, Mode: transport, Replay window size: 16384, Seq: 0x0
    Errors:
      Packets outside replay window: 0, Replay: 74, Integrity failed: 0
    Lifetime config:
      Soft byte limit: 3887955860999, Hard byte limit: 6442450944000
      Soft packet limit: 2136321284, Hard packet limit: 4000000000
      Soft time limit: 2910 secs, Hard time limit: 3600 secs
    Lifetime current:
      Current bytes: 34266913976
      Current packets: 32369258
      SA add time: Thu Mar 14 13:18:20 2024
      SA last use time: Thu Mar 14 13:35:06 2024
  Outbound SPI: 0xc922bc:
    Request ID: 1, Mode: transport, Replay window size: 0, Seq: 0x0
    Errors:
      Packets outside replay window: 0, Replay: 0, Integrity failed: 0
    Lifetime config:
      Soft byte limit: 4659401918999, Hard byte limit: 6442450944000
      Soft packet limit: 2067546214, Hard packet limit: 4000000000
      Soft time limit: 2932 secs, Hard time limit: 3600 secs
    Lifetime current:
      Current bytes: 22806523428
      Current packets: 44831702
      SA add time: Thu Mar 14 13:18:20 2024
      SA last use time: Thu Mar 14 13:35:06 2024
```

## show stun client translations detail

```text
Current System Time: Thu Mar 14 13:34:30 2024
Transaction ID 000000020affff0100000000
Agent Name: dps
Source Address: 172.16.1.0:4500
Public Address: 172.16.1.0:4500
Number of Attributes: 3
Timeout Interval: 0:03:00
Last Refreshed: 0:01:21 ago
Attribute Type   Length Value           
---------------- ------ ----------------
PATH_GROUP            7 VZ_NEAR         
VTEP_IP               4 10.255.255.1    
WAN_ID                4 2               

```

## show stun server bindings detail

```text
Current System Time: Thu Mar 14 13:34:31 2024
Transaction ID 000000010affff0500000000
Public Address: 172.16.0.1:4500
Number of Attributes: 3
Timeout Interval: 0:10:00
Timeout: 0:08:57
Attribute Type   Length Value           
---------------- ------ ----------------
PATH_GROUP            6 VZ_OFF          
VTEP_IP               4 10.255.255.5    
WAN_ID                4 1               

Transaction ID 000000010affff0600000000
Public Address: 172.16.0.3:4500
Number of Attributes: 3
Timeout Interval: 0:10:00
Timeout: 0:09:04
Attribute Type   Length Value           
---------------- ------ ----------------
PATH_GROUP            6 VZ_OFF          
VTEP_IP               4 10.255.255.6    
WAN_ID                4 1               

Transaction ID 000000010affff0800000000
Public Address: 172.16.1.2:4500
Number of Attributes: 3
Timeout Interval: 0:10:00
Timeout: 0:09:02
Attribute Type   Length Value           
---------------- ------ ----------------
PATH_GROUP            7 VZ_NEAR         
VTEP_IP               4 10.255.255.8    
WAN_ID                4 1               

Transaction ID 000000010affff0a00000000
Public Address: 172.16.1.7:4500
Number of Attributes: 3
Timeout Interval: 0:10:00
Timeout: 0:09:51
Attribute Type   Length Value           
---------------- ------ ----------------
PATH_GROUP            7 VZ_NEAR         
VTEP_IP               4 10.255.255.10   
WAN_ID                4 1               

Transaction ID 000000020affff0b00000000
Public Address: 172.16.0.9:4500
Number of Attributes: 3
Timeout Interval: 0:10:00
Timeout: 0:08:00
Attribute Type   Length Value           
---------------- ------ ----------------
PATH_GROUP            6 VZ_OFF          
VTEP_IP               4 10.255.255.11   
WAN_ID                4 2               

Transaction ID 000000020affff0c00000000
Public Address: 172.16.0.11:4500
Number of Attributes: 3
Timeout Interval: 0:10:00
Timeout: 0:08:02
Attribute Type   Length Value           
---------------- ------ ----------------
PATH_GROUP            6 VZ_OFF          
VTEP_IP               4 10.255.255.12   
WAN_ID                4 2               

```

## show path-selection paths detail

```text
Peer: 10.255.255.4, Path group VZ_NEAR
Path name: path13, static, Label: 13
Source: 172.16.1.0, Port: 4500, WAN ID: 2
Destination: 172.16.1.5, Port: 4500, WAN ID: 2886729989
Local interface: Ethernet1/3
Route state: IPsec established
Traffic class 0: active (0:16:08)
MTU: 8914

Peer: 10.255.255.5, Path group VZ_OFF
Path name: path3, dynamic, Label: 3
Source: 172.16.0.4, Port: 4500, WAN ID: 1
Destination: 172.16.0.1, Port: 4500, WAN ID: 1
Local interface: Ethernet1/2
Route state: IPsec established
Traffic class 0: active (0:14:54)
MTU: 8914

Peer: 10.255.255.6, Path group VZ_OFF
Path name: path1, dynamic, Label: 1
Source: 172.16.0.4, Port: 4500, WAN ID: 1
Destination: 172.16.0.3, Port: 4500, WAN ID: 1
Local interface: Ethernet1/2
Route state: IPsec established
Traffic class 0: active (0:15:50)
MTU: 8914

Peer: 10.255.255.8, Path group VZ_NEAR
Path name: path5, dynamic, Label: 5
Source: 172.16.1.0, Port: 4500, WAN ID: 2
Destination: 172.16.1.2, Port: 4500, WAN ID: 1
Local interface: Ethernet1/3
Route state: IPsec established
Traffic class 0: active (0:14:43)
MTU: 8914

Peer: 10.255.255.10, Path group VZ_NEAR
Path name: path11, dynamic, Label: 11
Source: 172.16.1.0, Port: 4500, WAN ID: 2
Destination: 172.16.1.7, Port: 4500, WAN ID: 1
Local interface: Ethernet1/3
Route state: IPsec established
Traffic class 0: active (0:14:09)
MTU: 1424

Peer: 10.255.255.11, Path group VZ_OFF
Path name: path8, dynamic, Label: 8
Source: 172.16.0.4, Port: 4500, WAN ID: 1
Destination: 172.16.0.9, Port: 4500, WAN ID: 2
Local interface: Ethernet1/2
Route state: IPsec established
Traffic class 0: active (0:13:00)
MTU: 1424

Peer: 10.255.255.12, Path group VZ_OFF
Path name: path10, dynamic, Label: 10
Source: 172.16.0.4, Port: 4500, WAN ID: 1
Destination: 172.16.0.11, Port: 4500, WAN ID: 2
Local interface: Ethernet1/2
Route state: IPsec established
Traffic class 0: active (0:16:04)
MTU: 1424

```

## show bgp neighbors

```text
BGP neighbor is 10.255.255.4, remote AS 65000, internal link
  BGP version 4, remote router ID 10.255.255.4, VRF default
  Inherits configuration from and member of peer-group autovpnEdges
  Last read 00:00:02, last write 00:00:03
  Hold time is 180, keepalive interval is 60 seconds
  Configured hold time is 180, keepalive interval is 60 seconds
  Effective minimum hold time is 3 seconds
  Send failure hold time is 0 seconds
  Hold timer is active, time left: 00:02:58
  Keepalive timer is active, time left: 00:00:42
  Connect timer is inactive
  Idle-restart timer is inactive
  BGP state is Established, up for 00:16:05
  Number of transitions to established: 1
  Last state was OpenConfirm
  Last event was Established
  Types of communities advertised: extended
  Enhanced route refresh stale path removal disabled
  Outbound enhanced route refresh enabled
  Neighbor is a route reflector client
  Neighbor is using global cluster ID 10.255.255.1
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
      Received 00:14:36
      Number of stale paths removed after graceful restart: 0
      Number of paths received before End-of-RIB: 7
    L2VPN EVPN End-of-RIB received: Yes
      Received 00:14:36
      Number of stale paths removed after graceful restart: 0
      Number of paths received before End-of-RIB: 14
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
    Updates:                     34408     12793
    Keepalives:                     14        12
    Enhanced Route Refresh:          0         0
    Begin of Route Refresh:          0         0
    End of Route Refresh:            0         0
    Total messages:              34423     12806
  Prefix Statistics:
                                   Sent      Rcvd     Best Paths     Best ECMP Paths
    IPv4 Unicast:                     0         0              0                   0
    IPv4 Dps:                        13        13             13                   0
    IPv6 Unicast:                     0         0              0                   0
    EVPN:                            31        17             15                   0
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
  Additional-paths send mode:
    Dps: any
Local AS is 65000, local router ID 10.255.255.1
TTL is 255
Local TCP address is 10.255.255.1, local port is 179
Remote TCP address is 10.255.255.4, remote port is 34325
Local next hop for next hop self:
  Dps: 10.255.255.1
  L2VPN EVPN: 10.255.255.1
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
    Retransmission Timeout (rto): 212.0ms
    Round-trip Time (rtt/rtvar): 10.6ms/10.1ms
    Delayed Ack Timeout (ato): 40.0ms
    Congestion Window (cwnd): 10
    TCP Throughput: 10.97 Mbps
    Recv Round-trip Time (rcv_rtt): 50.0ms
    Advertised Recv Window (rcv_space): 14600

BGP neighbor is 10.255.255.5, remote AS 65000, internal link
  BGP version 4, remote router ID 10.255.255.5, VRF default
  Inherits configuration from and member of peer-group autovpnEdges
  Last read 00:00:37, last write 00:00:13
  Hold time is 180, keepalive interval is 60 seconds
  Configured hold time is 180, keepalive interval is 60 seconds
  Effective minimum hold time is 3 seconds
  Send failure hold time is 0 seconds
  Hold timer is active, time left: 00:02:23
  Keepalive timer is active, time left: 00:00:44
  Connect timer is inactive
  Idle-restart timer is inactive
  BGP state is Established, up for 00:14:54
  Number of transitions to established: 1
  Last state was OpenConfirm
  Last event was Established
  Types of communities advertised: extended
  Enhanced route refresh stale path removal disabled
  Outbound enhanced route refresh enabled
  Neighbor is a route reflector client
  Neighbor is using global cluster ID 10.255.255.1
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
      Received 00:14:52
      Number of stale paths removed after graceful restart: 0
      Number of paths received before End-of-RIB: 2
    L2VPN EVPN End-of-RIB received: Yes
      Received 00:14:52
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
    Updates:                     34601         7
    Keepalives:                     13        19
    Enhanced Route Refresh:          0         0
    Begin of Route Refresh:          0         0
    End of Route Refresh:            0         0
    Total messages:              34615        27
  Prefix Statistics:
                                   Sent      Rcvd     Best Paths     Best ECMP Paths
    IPv4 Unicast:                     0         0              0                   0
    IPv4 Dps:                        24         2              2                   2
    IPv6 Unicast:                     0         0              0                   0
    EVPN:                            39         3              3                   0
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
  Additional-paths send mode:
    Dps: any
Local AS is 65000, local router ID 10.255.255.1
TTL is 255
Local TCP address is 10.255.255.1, local port is 179
Remote TCP address is 10.255.255.5, remote port is 39221
Local next hop for next hop self:
  Dps: 10.255.255.1
  L2VPN EVPN: 10.255.255.1
BFD is enabled with configured transmit interval 1000ms, receive interval 1000ms, multiplier 3 and state is Up
TCP Socket Information:
  TCP state is ESTABLISHED
  Recv-Q: 0/32768
  Send-Q: 0/46080
  Outgoing Maximum Segment Size (MSS): 1284
  Total Number of TCP retransmissions: 1
  Options:
    Timestamps enabled: yes
    Selective Acknowledgments enabled: yes
    Window Scale enabled: yes
    Explicit Congestion Notification (ECN) enabled: no
  Socket Statistics:
    Window Scale (wscale): 7,7
    Retransmission Timeout (rto): 204.0ms
    Round-trip Time (rtt/rtvar): 2.7ms/0.3ms
    Delayed Ack Timeout (ato): 40.0ms
    Congestion Window (cwnd): 10
    TCP Throughput: 38.43 Mbps
    Recv Round-trip Time (rcv_rtt): 44.0ms
    Advertised Recv Window (rcv_space): 14600

BGP neighbor is 10.255.255.6, remote AS 65000, internal link
  BGP version 4, remote router ID 10.255.255.6, VRF default
  Inherits configuration from and member of peer-group autovpnEdges
  Last read 00:00:40, last write 00:00:04
  Hold time is 180, keepalive interval is 60 seconds
  Configured hold time is 180, keepalive interval is 60 seconds
  Effective minimum hold time is 3 seconds
  Send failure hold time is 0 seconds
  Hold timer is active, time left: 00:02:20
  Keepalive timer is active, time left: 00:00:52
  Connect timer is inactive
  Idle-restart timer is inactive
  BGP state is Established, up for 00:15:51
  Number of transitions to established: 1
  Last state was OpenConfirm
  Last event was Established
  Types of communities advertised: extended
  Enhanced route refresh stale path removal disabled
  Outbound enhanced route refresh enabled
  Neighbor is a route reflector client
  Neighbor is using global cluster ID 10.255.255.1
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
      Received 00:15:51
      Number of stale paths removed after graceful restart: 0
      Number of paths received before End-of-RIB: 2
    L2VPN EVPN End-of-RIB received: Yes
      Received 00:15:51
      Number of stale paths removed after graceful restart: 0
      Number of paths received before End-of-RIB: 1
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
    Updates:                     44831         7
    Keepalives:                     12        19
    Enhanced Route Refresh:          0         0
    Begin of Route Refresh:          0         0
    End of Route Refresh:            0         0
    Total messages:              44844        27
  Prefix Statistics:
                                   Sent      Rcvd     Best Paths     Best ECMP Paths
    IPv4 Unicast:                     0         0              0                   0
    IPv4 Dps:                        24         2              2                   2
    IPv6 Unicast:                     0         0              0                   0
    EVPN:                            39         3              3                   2
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
  Additional-paths send mode:
    Dps: any
Local AS is 65000, local router ID 10.255.255.1
TTL is 255
Local TCP address is 10.255.255.1, local port is 179
Remote TCP address is 10.255.255.6, remote port is 36057
Local next hop for next hop self:
  Dps: 10.255.255.1
  L2VPN EVPN: 10.255.255.1
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
    Round-trip Time (rtt/rtvar): 4.7ms/1.2ms
    Delayed Ack Timeout (ato): 40.0ms
    Congestion Window (cwnd): 10
    TCP Throughput: 24.46 Mbps
    Recv Round-trip Time (rcv_rtt): 46.0ms
    Advertised Recv Window (rcv_space): 14600

BGP neighbor is 10.255.255.8, remote AS 65000, internal link
  BGP version 4, remote router ID 10.255.255.8, VRF default
  Inherits configuration from and member of peer-group autovpnEdges
  Last read 00:00:15, last write 00:00:45
  Hold time is 180, keepalive interval is 60 seconds
  Configured hold time is 180, keepalive interval is 60 seconds
  Effective minimum hold time is 3 seconds
  Send failure hold time is 0 seconds
  Hold timer is active, time left: 00:02:45
  Keepalive timer is active, time left: 00:00:03
  Connect timer is inactive
  Idle-restart timer is inactive
  BGP state is Established, up for 00:14:45
  Number of transitions to established: 1
  Last state was OpenConfirm
  Last event was Established
  Types of communities advertised: extended
  Enhanced route refresh stale path removal disabled
  Outbound enhanced route refresh enabled
  Neighbor is a route reflector client
  Neighbor is using global cluster ID 10.255.255.1
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
      Received 00:14:45
      Number of stale paths removed after graceful restart: 0
      Number of paths received before End-of-RIB: 2
    L2VPN EVPN End-of-RIB received: Yes
      Received 00:14:45
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
    Updates:                     33317         8
    Keepalives:                     11        18
    Enhanced Route Refresh:          0         0
    Begin of Route Refresh:          0         0
    End of Route Refresh:            0         0
    Total messages:              33329        27
  Prefix Statistics:
                                   Sent      Rcvd     Best Paths     Best ECMP Paths
    IPv4 Unicast:                     0         0              0                   0
    IPv4 Dps:                        24         2              2                   2
    IPv6 Unicast:                     0         0              0                   0
    EVPN:                            39         3              3                   2
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
  Additional-paths send mode:
    Dps: any
Local AS is 65000, local router ID 10.255.255.1
TTL is 255
Local TCP address is 10.255.255.1, local port is 179
Remote TCP address is 10.255.255.8, remote port is 43669
Local next hop for next hop self:
  Dps: 10.255.255.1
  L2VPN EVPN: 10.255.255.1
BFD is enabled with configured transmit interval 1000ms, receive interval 1000ms, multiplier 3 and state is Up
TCP Socket Information:
  TCP state is ESTABLISHED
  Recv-Q: 0/32768
  Send-Q: 0/46080
  Outgoing Maximum Segment Size (MSS): 1284
  Total Number of TCP retransmissions: 1
  Options:
    Timestamps enabled: yes
    Selective Acknowledgments enabled: yes
    Window Scale enabled: yes
    Explicit Congestion Notification (ECN) enabled: no
  Socket Statistics:
    Window Scale (wscale): 7,7
    Retransmission Timeout (rto): 208.0ms
    Round-trip Time (rtt/rtvar): 5.1ms/1.2ms
    Delayed Ack Timeout (ato): 40.0ms
    Congestion Window (cwnd): 10
    TCP Throughput: 20.08 Mbps
    Recv Round-trip Time (rcv_rtt): 4.0ms
    Advertised Recv Window (rcv_space): 14600

BGP neighbor is 10.255.255.10, remote AS 65000, internal link
  BGP version 4, remote router ID 10.255.255.10, VRF default
  Inherits configuration from and member of peer-group autovpnEdges
  Last read 00:00:49, last write 00:00:02
  Hold time is 180, keepalive interval is 60 seconds
  Configured hold time is 180, keepalive interval is 60 seconds
  Effective minimum hold time is 3 seconds
  Send failure hold time is 0 seconds
  Hold timer is active, time left: 00:02:11
  Keepalive timer is active, time left: 00:00:46
  Connect timer is inactive
  Idle-restart timer is inactive
  BGP state is Established, up for 00:14:09
  Number of transitions to established: 1
  Last state was OpenConfirm
  Last event was RecvUpdate
  Types of communities advertised: extended
  Enhanced route refresh stale path removal disabled
  Outbound enhanced route refresh enabled
  Neighbor is a route reflector client
  Neighbor is using global cluster ID 10.255.255.1
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
      Received 00:14:08
      Number of stale paths removed after graceful restart: 0
      Number of paths received before End-of-RIB: 2
    L2VPN EVPN End-of-RIB received: Yes
      Received 00:14:08
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
    Updates:                     27330         6
    Keepalives:                     13        18
    Enhanced Route Refresh:          0         0
    Begin of Route Refresh:          0         0
    End of Route Refresh:            0         0
    Total messages:              27344        25
  Prefix Statistics:
                                   Sent      Rcvd     Best Paths     Best ECMP Paths
    IPv4 Unicast:                     0         0              0                   0
    IPv4 Dps:                        24         2              2                   2
    IPv6 Unicast:                     0         0              0                   0
    EVPN:                            39         3              3                   0
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
  Additional-paths send mode:
    Dps: any
Local AS is 65000, local router ID 10.255.255.1
TTL is 255
Local TCP address is 10.255.255.1, local port is 179
Remote TCP address is 10.255.255.10, remote port is 42679
Local next hop for next hop self:
  Dps: 10.255.255.1
  L2VPN EVPN: 10.255.255.1
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
    Round-trip Time (rtt/rtvar): 3.4ms/1.2ms
    Delayed Ack Timeout (ato): 40.0ms
    Congestion Window (cwnd): 10
    TCP Throughput: 32.75 Mbps
    Recv Round-trip Time (rcv_rtt): 8.0ms
    Advertised Recv Window (rcv_space): 14600

BGP neighbor is 10.255.255.11, remote AS 65000, internal link
  BGP version 4, remote router ID 10.255.255.11, VRF default
  Inherits configuration from and member of peer-group autovpnEdges
  Last read 00:00:07, last write 00:00:02
  Hold time is 180, keepalive interval is 60 seconds
  Configured hold time is 180, keepalive interval is 60 seconds
  Effective minimum hold time is 3 seconds
  Send failure hold time is 0 seconds
  Hold timer is active, time left: 00:02:53
  Keepalive timer is active, time left: 00:00:49
  Connect timer is inactive
  Idle-restart timer is inactive
  BGP state is Established, up for 00:13:00
  Number of transitions to established: 1
  Last state was OpenConfirm
  Last event was RecvUpdate
  Types of communities advertised: extended
  Enhanced route refresh stale path removal disabled
  Outbound enhanced route refresh enabled
  Neighbor is a route reflector client
  Neighbor is using global cluster ID 10.255.255.1
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
      Received 00:12:53
      Number of stale paths removed after graceful restart: 0
      Number of paths received before End-of-RIB: 2
    L2VPN EVPN End-of-RIB received: Yes
      Received 00:12:53
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
    Updates:                     16287         7
    Keepalives:                     13        17
    Enhanced Route Refresh:          0         0
    Begin of Route Refresh:          0         0
    End of Route Refresh:            0         0
    Total messages:              16301        25
  Prefix Statistics:
                                   Sent      Rcvd     Best Paths     Best ECMP Paths
    IPv4 Unicast:                     0         0              0                   0
    IPv4 Dps:                        24         2              2                   2
    IPv6 Unicast:                     0         0              0                   0
    EVPN:                            39         3              3                   0
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
  Additional-paths send mode:
    Dps: any
Local AS is 65000, local router ID 10.255.255.1
TTL is 255
Local TCP address is 10.255.255.1, local port is 179
Remote TCP address is 10.255.255.11, remote port is 33995
Local next hop for next hop self:
  Dps: 10.255.255.1
  L2VPN EVPN: 10.255.255.1
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
    Round-trip Time (rtt/rtvar): 3.3ms/1.0ms
    Delayed Ack Timeout (ato): 40.0ms
    Congestion Window (cwnd): 10
    TCP Throughput: 33.48 Mbps
    Recv Round-trip Time (rcv_rtt): 46.0ms
    Advertised Recv Window (rcv_space): 14600

BGP neighbor is 10.255.255.12, remote AS 65000, internal link
  BGP version 4, remote router ID 10.255.255.12, VRF default
  Inherits configuration from and member of peer-group autovpnEdges
  Last read 00:00:12, last write 00:00:05
  Hold time is 180, keepalive interval is 60 seconds
  Configured hold time is 180, keepalive interval is 60 seconds
  Effective minimum hold time is 3 seconds
  Send failure hold time is 0 seconds
  Hold timer is active, time left: 00:02:48
  Keepalive timer is active, time left: 00:00:50
  Connect timer is inactive
  Idle-restart timer is inactive
  BGP state is Established, up for 00:16:04
  Number of transitions to established: 1
  Last state was OpenConfirm
  Last event was Established
  Types of communities advertised: extended
  Enhanced route refresh stale path removal disabled
  Outbound enhanced route refresh enabled
  Neighbor is a route reflector client
  Neighbor is using global cluster ID 10.255.255.1
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
      Received 00:14:35
      Number of stale paths removed after graceful restart: 0
      Number of paths received before End-of-RIB: 2
    L2VPN EVPN End-of-RIB received: Yes
      Received 00:14:35
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
    Updates:                     46839         7
    Keepalives:                     12        19
    Enhanced Route Refresh:          0         0
    Begin of Route Refresh:          0         0
    End of Route Refresh:            0         0
    Total messages:              46852        27
  Prefix Statistics:
                                   Sent      Rcvd     Best Paths     Best ECMP Paths
    IPv4 Unicast:                     0         0              0                   0
    IPv4 Dps:                        24         2              2                   2
    IPv6 Unicast:                     0         0              0                   0
    EVPN:                            39         3              3                   0
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
  Additional-paths send mode:
    Dps: any
Local AS is 65000, local router ID 10.255.255.1
TTL is 255
Local TCP address is 10.255.255.1, local port is 179
Remote TCP address is 10.255.255.12, remote port is 37635
Local next hop for next hop self:
  Dps: 10.255.255.1
  L2VPN EVPN: 10.255.255.1
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
    Round-trip Time (rtt/rtvar): 3.7ms/1.4ms
    Delayed Ack Timeout (ato): 40.0ms
    Congestion Window (cwnd): 10
    TCP Throughput: 29.89 Mbps
    Recv Round-trip Time (rcv_rtt): 4.0ms
    Advertised Recv Window (rcv_space): 14600

```

## show bgp path-selection detail

```text
BGP routing table information for VRF default
Router identifier 10.255.255.1, local AS number 65000
Bgp routing table entry for ipv4Dps VTEP 10.255.255.5/32
 Paths: 2 available
  Local (Received from a RR-client)
    :: from 10.255.255.5 (10.255.255.5)
      Origin IGP, metric -, localpref 100, weight 0, received 00:14:55 ago, valid, internal
      Tunnel encapsulation attribute: Dynamic path selection
        Endpoint: 172.16.0.1, Path group name: VZ_OFF, WAN ID: 1, UDP port: 4500
  Local (Received from a RR-client)
    :: from 10.255.255.4 (10.255.255.4)
      Origin IGP, metric -, localpref 100, weight 0, received 00:14:52 ago, valid, internal
      Tunnel encapsulation attribute: Dynamic path selection
        Endpoint: 172.16.0.1, Path group name: VZ_OFF, WAN ID: 1, UDP port: 4500
Bgp routing table entry for ipv4Dps VTEP 10.255.255.6/32
 Paths: 2 available
  Local (Received from a RR-client)
    :: from 10.255.255.6 (10.255.255.6)
      Origin IGP, metric -, localpref 100, weight 0, received 00:15:52 ago, valid, internal
      Tunnel encapsulation attribute: Dynamic path selection
        Endpoint: 172.16.0.3, Path group name: VZ_OFF, WAN ID: 1, UDP port: 4500
  Local (Received from a RR-client)
    :: from 10.255.255.4 (10.255.255.4)
      Origin IGP, metric -, localpref 100, weight 0, received 00:15:50 ago, valid, internal
      Tunnel encapsulation attribute: Dynamic path selection
        Endpoint: 172.16.0.3, Path group name: VZ_OFF, WAN ID: 1, UDP port: 4500
Bgp routing table entry for ipv4Dps VTEP 10.255.255.8/32
 Paths: 2 available
  Local (Received from a RR-client)
    :: from 10.255.255.8 (10.255.255.8)
      Origin IGP, metric -, localpref 100, weight 0, received 00:14:46 ago, valid, internal
      Tunnel encapsulation attribute: Dynamic path selection
        Endpoint: 172.16.1.2, Path group name: VZ_NEAR, WAN ID: 1, UDP port: 4500
  Local (Received from a RR-client)
    :: from 10.255.255.4 (10.255.255.4)
      Origin IGP, metric -, localpref 100, weight 0, received 00:14:44 ago, valid, internal
      Tunnel encapsulation attribute: Dynamic path selection
        Endpoint: 172.16.1.2, Path group name: VZ_NEAR, WAN ID: 1, UDP port: 4500
Bgp routing table entry for ipv4Dps VTEP 10.255.255.10/32
 Paths: 2 available
  Local (Received from a RR-client)
    :: from 10.255.255.10 (10.255.255.10)
      Origin IGP, metric -, localpref 100, weight 0, received 00:14:10 ago, valid, internal
      Tunnel encapsulation attribute: Dynamic path selection
        Endpoint: 172.16.1.7, Path group name: VZ_NEAR, WAN ID: 1, UDP port: 4500
  Local (Received from a RR-client)
    :: from 10.255.255.4 (10.255.255.4)
      Origin IGP, metric -, localpref 100, weight 0, received 00:14:09 ago, valid, internal
      Tunnel encapsulation attribute: Dynamic path selection
        Endpoint: 172.16.1.7, Path group name: VZ_NEAR, WAN ID: 1, UDP port: 4500
Bgp routing table entry for ipv4Dps VTEP 10.255.255.11/32
 Paths: 2 available
  Local (Received from a RR-client)
    :: from 10.255.255.11 (10.255.255.11)
      Origin IGP, metric -, localpref 100, weight 0, received 00:13:01 ago, valid, internal
      Tunnel encapsulation attribute: Dynamic path selection
        Endpoint: 172.16.0.9, Path group name: VZ_OFF, WAN ID: 2, UDP port: 4500
  Local (Received from a RR-client)
    :: from 10.255.255.4 (10.255.255.4)
      Origin IGP, metric -, localpref 100, weight 0, received 00:12:54 ago, valid, internal
      Tunnel encapsulation attribute: Dynamic path selection
        Endpoint: 172.16.0.9, Path group name: VZ_OFF, WAN ID: 2, UDP port: 4500
Bgp routing table entry for ipv4Dps VTEP 10.255.255.12/32
 Paths: 2 available
  Local (Received from a RR-client)
    :: from 10.255.255.12 (10.255.255.12)
      Origin IGP, metric -, localpref 100, weight 0, received 00:16:05 ago, valid, internal
      Tunnel encapsulation attribute: Dynamic path selection
        Endpoint: 172.16.0.11, Path group name: VZ_OFF, WAN ID: 2, UDP port: 4500
  Local (Received from a RR-client)
    :: from 10.255.255.4 (10.255.255.4)
      Origin IGP, metric -, localpref 100, weight 0, received 00:12:49 ago, valid, internal
      Tunnel encapsulation attribute: Dynamic path selection
        Endpoint: 172.16.0.11, Path group name: VZ_OFF, WAN ID: 2, UDP port: 4500
Bgp routing table entry for ipv4Ipsec VTEP 10.255.255.1/32
 Paths: 1 available
  Local
    - from - (0.0.0.0)
      Origin IGP, metric -, localpref -, weight 0, received 00:16:25 ago, valid, local
      Tunnel encapsulation attribute: IP security
        Initial contact: false, Rekey counter: 0, Nonce length: 32
        DH group: 14, DH key length: 256
        Encryption algo: aes256, Authentication algo: sha256
Bgp routing table entry for ipv4Ipsec VTEP 10.255.255.4/32
 Paths: 1 available
  Local (Received from a RR-client)
    :: from 10.255.255.4 (10.255.255.4)
      Origin IGP, metric -, localpref 100, weight 0, received 00:16:06 ago, valid, internal
      Tunnel encapsulation attribute: IP security
        Initial contact: false, Rekey counter: 0, Nonce length: 32
        DH group: 14, DH key length: 256
        Encryption algo: aes256, Authentication algo: sha256
Bgp routing table entry for ipv4Ipsec VTEP 10.255.255.5/32
 Paths: 2 available
  Local (Received from a RR-client)
    :: from 10.255.255.5 (10.255.255.5)
      Origin IGP, metric -, localpref 100, weight 0, received 00:14:55 ago, valid, internal
      Tunnel encapsulation attribute: IP security
        Initial contact: false, Rekey counter: 0, Nonce length: 32
        DH group: 14, DH key length: 256
        Encryption algo: aes256, Authentication algo: sha256
  Local (Received from a RR-client)
    :: from 10.255.255.4 (10.255.255.4)
      Origin IGP, metric -, localpref 100, weight 0, received 00:14:52 ago, valid, internal
      Tunnel encapsulation attribute: IP security
        Initial contact: false, Rekey counter: 0, Nonce length: 32
        DH group: 14, DH key length: 256
        Encryption algo: aes256, Authentication algo: sha256
Bgp routing table entry for ipv4Ipsec VTEP 10.255.255.6/32
 Paths: 2 available
  Local (Received from a RR-client)
    :: from 10.255.255.6 (10.255.255.6)
      Origin IGP, metric -, localpref 100, weight 0, received 00:15:52 ago, valid, internal
      Tunnel encapsulation attribute: IP security
        Initial contact: false, Rekey counter: 0, Nonce length: 32
        DH group: 14, DH key length: 256
        Encryption algo: aes256, Authentication algo: sha256
  Local (Received from a RR-client)
    :: from 10.255.255.4 (10.255.255.4)
      Origin IGP, metric -, localpref 100, weight 0, received 00:15:50 ago, valid, internal
      Tunnel encapsulation attribute: IP security
        Initial contact: false, Rekey counter: 0, Nonce length: 32
        DH group: 14, DH key length: 256
        Encryption algo: aes256, Authentication algo: sha256
Bgp routing table entry for ipv4Ipsec VTEP 10.255.255.8/32
 Paths: 2 available
  Local (Received from a RR-client)
    :: from 10.255.255.8 (10.255.255.8)
      Origin IGP, metric -, localpref 100, weight 0, received 00:14:46 ago, valid, internal
      Tunnel encapsulation attribute: IP security
        Initial contact: false, Rekey counter: 0, Nonce length: 32
        DH group: 14, DH key length: 256
        Encryption algo: aes256, Authentication algo: sha256
  Local (Received from a RR-client)
    :: from 10.255.255.4 (10.255.255.4)
      Origin IGP, metric -, localpref 100, weight 0, received 00:14:44 ago, valid, internal
      Tunnel encapsulation attribute: IP security
        Initial contact: false, Rekey counter: 0, Nonce length: 32
        DH group: 14, DH key length: 256
        Encryption algo: aes256, Authentication algo: sha256
Bgp routing table entry for ipv4Ipsec VTEP 10.255.255.10/32
 Paths: 2 available
  Local (Received from a RR-client)
    :: from 10.255.255.10 (10.255.255.10)
      Origin IGP, metric -, localpref 100, weight 0, received 00:14:10 ago, valid, internal
      Tunnel encapsulation attribute: IP security
        Initial contact: false, Rekey counter: 0, Nonce length: 32
        DH group: 14, DH key length: 256
        Encryption algo: aes256, Authentication algo: sha256
  Local (Received from a RR-client)
    :: from 10.255.255.4 (10.255.255.4)
      Origin IGP, metric -, localpref 100, weight 0, received 00:14:09 ago, valid, internal
      Tunnel encapsulation attribute: IP security
        Initial contact: false, Rekey counter: 0, Nonce length: 32
        DH group: 14, DH key length: 256
        Encryption algo: aes256, Authentication algo: sha256
Bgp routing table entry for ipv4Ipsec VTEP 10.255.255.11/32
 Paths: 2 available
  Local (Received from a RR-client)
    :: from 10.255.255.11 (10.255.255.11)
      Origin IGP, metric -, localpref 100, weight 0, received 00:13:01 ago, valid, internal
      Tunnel encapsulation attribute: IP security
        Initial contact: false, Rekey counter: 0, Nonce length: 32
        DH group: 14, DH key length: 256
        Encryption algo: aes256, Authentication algo: sha256
  Local (Received from a RR-client)
    :: from 10.255.255.4 (10.255.255.4)
      Origin IGP, metric -, localpref 100, weight 0, received 00:12:54 ago, valid, internal
      Tunnel encapsulation attribute: IP security
        Initial contact: false, Rekey counter: 0, Nonce length: 32
        DH group: 14, DH key length: 256
        Encryption algo: aes256, Authentication algo: sha256
Bgp routing table entry for ipv4Ipsec VTEP 10.255.255.12/32
 Paths: 2 available
  Local (Received from a RR-client)
    :: from 10.255.255.12 (10.255.255.12)
      Origin IGP, metric -, localpref 100, weight 0, received 00:16:05 ago, valid, internal
      Tunnel encapsulation attribute: IP security
        Initial contact: false, Rekey counter: 0, Nonce length: 32
        DH group: 14, DH key length: 256
        Encryption algo: aes256, Authentication algo: sha256
  Local (Received from a RR-client)
    :: from 10.255.255.4 (10.255.255.4)
      Origin IGP, metric -, localpref 100, weight 0, received 00:12:49 ago, valid, internal
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
>C    10.255.255.1/32 [0 pref/0 metric] updated 00:17:24 ago
         via Loopback0, directly connected
>C    172.16.0.4/31 [0 pref/0 metric] updated 00:16:25 ago
         via Ethernet1/2, directly connected
>C    172.16.1.0/31 [0 pref/0 metric] updated 00:16:25 ago
         via Ethernet1/3, directly connected
>C    172.28.128.0/20 [0 pref/0 metric] updated 00:16:57 ago
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
>S    0.0.0.0/0 [1 pref/0 metric] updated 00:16:25 ago
         via 172.16.0.5 [0 pref/0 metric] type ipv4
            via 172.16.0.5, Ethernet1/2
>S    10.80.0.0/12 [1 pref/0 metric] updated 00:16:57 ago
         via 172.28.128.1 [0 pref/0 metric] type ipv4
            via 172.28.128.1, Management1/1
>S    10.224.0.0/12 [1 pref/0 metric] updated 00:16:57 ago
         via 172.28.128.1 [0 pref/0 metric] type ipv4
            via 172.28.128.1, Management1/1
>S    10.240.0.0/12 [1 pref/0 metric] updated 00:16:57 ago
         via 172.28.128.1 [0 pref/0 metric] type ipv4
            via 172.28.128.1, Management1/1
>S    172.16.0.0/12 [1 pref/0 metric] updated 00:16:57 ago
         via 172.28.128.1 [0 pref/0 metric] type ipv4
            via 172.28.128.1, Management1/1
>S    172.16.0.0/24 [1 pref/0 metric] updated 00:16:25 ago
         via 172.16.0.5 [0 pref/0 metric] type ipv4
            via 172.16.0.5, Ethernet1/2
>S    172.16.1.0/24 [1 pref/0 metric] updated 00:16:25 ago
         via 172.16.1.1 [0 pref/0 metric] type ipv4
            via 172.16.1.1, Ethernet1/3
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
>P    0.0.0.0/8 [1 pref/0 metric] updated 00:17:24 ago
         via Null0, directly connected [NF]
>P    10.255.255.2/32 [1 pref/0 metric] updated 00:16:26 ago
         via 10.255.255.2, Dps1
>P    10.255.255.4/32 [1 pref/0 metric] updated 00:16:26 ago
         via 10.255.255.4, Dps1
>P    10.255.255.5/32 [1 pref/0 metric] updated 00:16:00 ago
         via 10.255.255.5, Dps1
>P    10.255.255.6/32 [1 pref/0 metric] updated 00:15:58 ago
         via 10.255.255.6, Dps1
>P    10.255.255.8/32 [1 pref/0 metric] updated 00:15:51 ago
         via 10.255.255.8, Dps1
>P    10.255.255.10/32 [1 pref/0 metric] updated 00:15:11 ago
         via 10.255.255.10, Dps1
>P    10.255.255.11/32 [1 pref/0 metric] updated 00:14:03 ago
         via 10.255.255.11, Dps1
>P    10.255.255.12/32 [1 pref/0 metric] updated 00:16:21 ago
         via 10.255.255.12, Dps1
>P    127.0.0.0/8 [1 pref/0 metric] updated 00:17:24 ago
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
>P    ::/96 [1 pref/0 metric] updated 00:16:29 ago
         via Null0, directly connected [NF]
>P    ::ffff:127.0.0.0/104 [1 pref/0 metric] updated 00:16:29 ago
         via :: [1 pref/1 metric] type ipv6
            via , directly connected
>P    fe80::/10 [1 pref/0 metric] updated 00:16:29 ago
```

