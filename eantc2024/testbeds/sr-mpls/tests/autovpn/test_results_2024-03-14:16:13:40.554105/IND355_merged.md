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

Uptime: 1 hour and 16 minutes
Total memory: 65396488 kB
Free memory: 39990136 kB

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
Loopback0        10.255.255.1/32      up         up             65535          
Management1/1    172.28.137.226/20    up         up              1500          

```

## show interfaces counters rates | nz

```text
Port      Name      Intvl  In Mbps      %  In Kpps Out Mbps      % Out Kpps
Et1/1     CE         5:00      0.4   0.0%        0      0.5   0.0%        0
Et1/2     VZ_OFF     5:00      0.1   0.0%        0      0.1   0.0%        0
Et1/3     VZ_NEAR    5:00      0.5   0.0%        0      0.3   0.0%        0
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
 S        10.255.255.4/32
           directly connected, Dps1
 S        10.255.255.5/32
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
 S        10.255.255.4/32
           directly connected, Dps1
 S        10.255.255.5/32
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
 C        10.1.255.0/31
           directly connected, Ethernet1/1
 O        10.1.255.2/31 [110/20]
           via 10.1.255.0, Ethernet1/1
 B I      10.2.255.0/31 [20/0]
           via VTEP 10.255.255.8 VNI 201 router-mac ec:8a:48:04:2c:53
 B I      10.2.255.2/31 [20/0]
           via VTEP 10.255.255.8 VNI 201 router-mac ec:8a:48:04:2c:53
 B I      10.4.255.0/31 [20/0]
           via VTEP 10.255.255.10 VNI 201 router-mac 00:0c:29:d5:32:d4
 B I      10.4.255.2/31 [20/0]
           via VTEP 10.255.255.10 VNI 201 router-mac 00:0c:29:d5:32:d4
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
 O        10.255.254.2/32 [110/20]
           via 10.1.255.0, Ethernet1/1
 B I      10.255.254.3/32 [20/0]
           via VTEP 10.255.255.8 VNI 201 router-mac ec:8a:48:04:2c:53
 B I      10.255.254.4/32 [20/0]
           via VTEP 10.255.255.11 VNI 201 router-mac 00:0c:29:ba:2d:5e
           via VTEP 10.255.255.12 VNI 201 router-mac 00:0c:29:78:c5:2d
 B I      10.255.254.5/32 [20/0]
           via VTEP 10.255.255.10 VNI 201 router-mac 00:0c:29:d5:32:d4
 B I      10.255.254.6/32 [20/0]
           via VTEP 10.255.255.4 VNI 201 router-mac ec:8a:48:04:ff:5b
 B I      192.168.0.0/24 [20/0]
           via VTEP 10.255.255.5 VNI 201 router-mac ec:8a:48:04:21:53
 O        192.168.1.0/24 [110/20]
           via 10.1.255.0, Ethernet1/1
 B I      192.168.3.0/24 [20/0]
           via VTEP 10.255.255.8 VNI 201 router-mac ec:8a:48:04:2c:53
 B I      192.168.5.0/24 [20/0]
           via VTEP 10.255.255.4 VNI 201 router-mac ec:8a:48:04:ff:5b
 B I      192.168.6.0/24 [20/0]
           via VTEP 10.255.255.11 VNI 201 router-mac 00:0c:29:ba:2d:5e
           via VTEP 10.255.255.12 VNI 201 router-mac 00:0c:29:78:c5:2d
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
 * >      RD: 10.255.255.1:1 ip-prefix 10.1.255.0/31
                                 -                     -       -       0       i
 * >      RD: 10.255.255.1:1 ip-prefix 10.1.255.2/31
                                 -                     -       -       0       i
 * >      RD: 10.255.255.7:1 ip-prefix 10.2.255.0/31
                                 10.255.255.8          -       100     0       i
 * >      RD: 10.255.255.7:1 ip-prefix 10.2.255.2/31
                                 10.255.255.8          -       100     0       i
 * >      RD: 10.255.255.10:1 ip-prefix 10.4.255.0/31
                                 10.255.255.10         -       100     0       i
 * >      RD: 10.255.255.10:1 ip-prefix 10.4.255.2/31
                                 10.255.255.10         -       100     0       i
 * >      RD: 10.255.255.4:1 ip-prefix 10.5.255.0/31
                                 10.255.255.4          -       100     0       i
 * >      RD: 10.255.255.4:1 ip-prefix 10.5.255.2/31
                                 10.255.255.4          -       100     0       i
 * >      RD: 10.255.255.11:1 ip-prefix 10.6.255.0/31
                                 10.255.255.11         -       100     0       i
 * >      RD: 10.255.255.12:1 ip-prefix 10.6.255.2/31
                                 10.255.255.12         -       100     0       i
 * >      RD: 10.255.255.5:1 ip-prefix 10.255.254.1/32
                                 10.255.255.5          -       100     0       i
 * >      RD: 10.255.255.1:1 ip-prefix 10.255.254.2/32
                                 -                     -       -       0       i
 * >      RD: 10.255.255.7:1 ip-prefix 10.255.254.3/32
                                 10.255.255.8          -       100     0       i
 * >      RD: 10.255.255.11:1 ip-prefix 10.255.254.4/32
                                 10.255.255.11         -       100     0       i
 * >      RD: 10.255.255.12:1 ip-prefix 10.255.254.4/32
                                 10.255.255.12         -       100     0       i
 * >      RD: 10.255.255.10:1 ip-prefix 10.255.254.5/32
                                 10.255.255.10         -       100     0       i
 * >      RD: 10.255.255.4:1 ip-prefix 10.255.254.6/32
                                 10.255.255.4          -       100     0       i
 * >      RD: 10.255.255.5:1 ip-prefix 192.168.0.0/24
                                 10.255.255.5          -       100     0       i
 * >      RD: 10.255.255.1:1 ip-prefix 192.168.1.0/24
                                 -                     -       -       0       i
 * >      RD: 10.255.255.7:1 ip-prefix 192.168.3.0/24
                                 10.255.255.8          -       100     0       i
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
path3:
  Source address: 172.16.0.4, Destination address: 172.16.0.1
  State: established
  Uptime: 21 minutes, 4 seconds
  VRF: default
  Type: static
  Remote IP: 10.255.255.5
  Role: responder
  Inbound SPI: 0xca65b6:
    Request ID: 32, Mode: transport, Replay window size: 16384, Seq: 0x0
    Errors:
      Packets outside replay window: 0, Replay: 0, Integrity failed: 0
    Lifetime config:
      Soft byte limit: 4812327985499, Hard byte limit: 6442450944000
      Soft packet limit: 2306078949, Hard packet limit: 4000000000
      Soft time limit: 2940 secs, Hard time limit: 3600 secs
    Lifetime current:
      Current bytes: 1232916
      Current packets: 2881
      SA add time: Thu Mar 14 08:52:41 2024
      SA last use time: Thu Mar 14 09:14:19 2024
  Outbound SPI: 0xcad56a:
    Request ID: 32, Mode: transport, Replay window size: 0, Seq: 0x0
    Errors:
      Packets outside replay window: 0, Replay: 0, Integrity failed: 0
    Lifetime config:
      Soft byte limit: 4313388141749, Hard byte limit: 6442450944000
      Soft packet limit: 2504976808, Hard packet limit: 4000000000
      Soft time limit: 2694 secs, Hard time limit: 3600 secs
    Lifetime current:
      Current bytes: 2197590
      Current packets: 6002
      SA add time: Thu Mar 14 08:52:41 2024
      SA last use time: Thu Mar 14 09:14:19 2024
path4:
  Source address: 172.16.1.0, Destination address: 172.16.0.1
  State: idle
  Uptime: N/A
  VRF: default
  Type: static
  Remote IP: 10.255.255.5
  Role: responder
path5:
  Source address: 172.16.1.0, Destination address: 172.16.1.2
  State: established
  Uptime: 24 seconds
  VRF: default
  Type: static
  Remote IP: 10.255.255.5
  Role: responder
  Inbound SPI: 0xcbca06:
    Request ID: 25, Mode: transport, Replay window size: 16384, Seq: 0x0
    Errors:
      Packets outside replay window: 0, Replay: 0, Integrity failed: 0
    Lifetime config:
      Soft byte limit: 3754262384999, Hard byte limit: 6442450944000
      Soft packet limit: 2364322129, Hard packet limit: 4000000000
      Soft time limit: 2879 secs, Hard time limit: 3600 secs
    Lifetime current:
      Current bytes: 196068
      Current packets: 113
      SA add time: Thu Mar 14 09:13:21 2024
      SA last use time: Thu Mar 14 09:14:19 2024
  Outbound SPI: 0xcbee70:
    Request ID: 25, Mode: transport, Replay window size: 0, Seq: 0x0
    Errors:
      Packets outside replay window: 0, Replay: 0, Integrity failed: 0
    Lifetime config:
      Soft byte limit: 4540382977499, Hard byte limit: 6442450944000
      Soft packet limit: 2556639449, Hard packet limit: 4000000000
      Soft time limit: 3010 secs, Hard time limit: 3600 secs
    Lifetime current:
      Current bytes: 404782
      Current packets: 222
      SA add time: Thu Mar 14 09:13:21 2024
      SA last use time: Thu Mar 14 09:14:19 2024
path6:
  Source address: 172.16.0.4, Destination address: 172.16.1.2
  State: idle
  Uptime: N/A
  VRF: default
  Type: static
  Remote IP: 10.255.255.5
  Role: responder
path7:
  Source address: 172.16.1.0, Destination address: 172.16.0.9
  State: idle
  Uptime: N/A
  VRF: default
  Type: static
  Remote IP: 10.255.255.5
  Role: responder
path8:
  Source address: 172.16.0.4, Destination address: 172.16.0.9
  State: established
  Uptime: 42 minutes, 1 second
  VRF: default
  Type: static
  Remote IP: 10.255.255.5
  Role: responder
  Inbound SPI: 0xc8000b:
    Request ID: 29, Mode: transport, Replay window size: 16384, Seq: 0x0
    Errors:
      Packets outside replay window: 0, Replay: 0, Integrity failed: 0
    Lifetime config:
      Soft byte limit: 4363680170249, Hard byte limit: 6442450944000
      Soft packet limit: 2713036326, Hard packet limit: 4000000000
      Soft time limit: 2723 secs, Hard time limit: 3600 secs
    Lifetime current:
      Current bytes: 1017548192
      Current packets: 965888
      SA add time: Thu Mar 14 08:31:44 2024
      SA last use time: Thu Mar 14 09:14:18 2024
  Outbound SPI: 0xca12e4:
    Request ID: 29, Mode: transport, Replay window size: 0, Seq: 0x0
    Errors:
      Packets outside replay window: 0, Replay: 0, Integrity failed: 0
    Lifetime config:
      Soft byte limit: 4522709290499, Hard byte limit: 6442450944000
      Soft packet limit: 2344466329, Hard packet limit: 4000000000
      Soft time limit: 2519 secs, Hard time limit: 3600 secs
    Lifetime current:
      Current bytes: 1450936962
      Current packets: 2858478
      SA add time: Thu Mar 14 08:31:44 2024
      SA last use time: Thu Mar 14 09:14:18 2024
path9:
  Source address: 172.16.1.0, Destination address: 172.16.0.11
  State: idle
  Uptime: N/A
  VRF: default
  Type: static
  Remote IP: 10.255.255.5
  Role: responder
path10:
  Source address: 172.16.0.4, Destination address: 172.16.0.11
  State: established
  Uptime: 42 minutes
  VRF: default
  Type: static
  Remote IP: 10.255.255.5
  Role: responder
  Inbound SPI: 0xc75220:
    Request ID: 30, Mode: transport, Replay window size: 16384, Seq: 0x0
    Errors:
      Packets outside replay window: 0, Replay: 0, Integrity failed: 0
    Lifetime config:
      Soft byte limit: 4332898364249, Hard byte limit: 6442450944000
      Soft packet limit: 2198897858, Hard packet limit: 4000000000
      Soft time limit: 2813 secs, Hard time limit: 3600 secs
    Lifetime current:
      Current bytes: 1526686280
      Current packets: 1446214
      SA add time: Thu Mar 14 08:31:45 2024
      SA last use time: Thu Mar 14 09:14:19 2024
  Outbound SPI: 0xc61462:
    Request ID: 30, Mode: transport, Replay window size: 0, Seq: 0x0
    Errors:
      Packets outside replay window: 0, Replay: 0, Integrity failed: 0
    Lifetime config:
      Soft byte limit: 3657253550249, Hard byte limit: 6442450944000
      Soft packet limit: 2290668738, Hard packet limit: 4000000000
      Soft time limit: 2536 secs, Hard time limit: 3600 secs
    Lifetime current:
      Current bytes: 967935828
      Current packets: 1909544
      SA add time: Thu Mar 14 08:31:45 2024
      SA last use time: Thu Mar 14 09:14:19 2024
path11:
  Source address: 172.16.1.0, Destination address: 172.16.1.7
  State: established
  Uptime: 42 minutes, 1 second
  VRF: default
  Type: static
  Remote IP: 10.255.255.5
  Role: responder
  Inbound SPI: 0xc42597:
    Request ID: 26, Mode: transport, Replay window size: 16384, Seq: 0x0
    Errors:
      Packets outside replay window: 0, Replay: 0, Integrity failed: 0
    Lifetime config:
      Soft byte limit: 4712303399999, Hard byte limit: 6442450944000
      Soft packet limit: 2716311782, Hard packet limit: 4000000000
      Soft time limit: 3059 secs, Hard time limit: 3600 secs
    Lifetime current:
      Current bytes: 4348663496
      Current packets: 4108462
      SA add time: Thu Mar 14 08:31:44 2024
      SA last use time: Thu Mar 14 09:14:19 2024
  Outbound SPI: 0xc5b611:
    Request ID: 26, Mode: transport, Replay window size: 0, Seq: 0x0
    Errors:
      Packets outside replay window: 0, Replay: 0, Integrity failed: 0
    Lifetime config:
      Soft byte limit: 3385707402749, Hard byte limit: 6442450944000
      Soft packet limit: 2999665337, Hard packet limit: 4000000000
      Soft time limit: 2613 secs, Hard time limit: 3600 secs
    Lifetime current:
      Current bytes: 1747079262
      Current packets: 3440338
      SA add time: Thu Mar 14 08:31:44 2024
      SA last use time: Thu Mar 14 09:14:19 2024
path12:
  Source address: 172.16.0.4, Destination address: 172.16.1.7
  State: idle
  Uptime: N/A
  VRF: default
  Type: static
  Remote IP: 10.255.255.5
  Role: responder
path13:
  Source address: 172.16.1.0, Destination address: 172.16.1.5
  State: established
  Uptime: 8 seconds
  VRF: default
  Type: static
  Remote IP: 10.255.255.5
  Role: responder
  Inbound SPI: 0xc8931f:
    Request ID: 23, Mode: transport, Replay window size: 16384, Seq: 0x0
    Errors:
      Packets outside replay window: 0, Replay: 0, Integrity failed: 0
    Lifetime config:
      Soft byte limit: 3696844959749, Hard byte limit: 6442450944000
      Soft packet limit: 2320514833, Hard packet limit: 4000000000
      Soft time limit: 2785 secs, Hard time limit: 3600 secs
    Lifetime current:
      Current bytes: 190452
      Current packets: 65
      SA add time: Thu Mar 14 09:13:36 2024
      SA last use time: Thu Mar 14 09:14:19 2024
  Outbound SPI: 0xc25ee3:
    Request ID: 23, Mode: transport, Replay window size: 0, Seq: 0x0
    Errors:
      Packets outside replay window: 0, Replay: 0, Integrity failed: 0
    Lifetime config:
      Soft byte limit: 3698974916999, Hard byte limit: 6442450944000
      Soft packet limit: 2662579334, Hard packet limit: 4000000000
      Soft time limit: 2670 secs, Hard time limit: 3600 secs
    Lifetime current:
      Current bytes: 403162
      Current packets: 162
      SA add time: Thu Mar 14 09:13:36 2024
      SA last use time: Thu Mar 14 09:14:19 2024
```

## show stun client translations detail

```text
Current System Time: Thu Mar 14 09:13:46 2024
Transaction ID 000000020affff0100000000
Agent Name: dps
Source Address: 172.16.1.0:4500
Public Address: 172.16.1.0:4500
Number of Attributes: 3
Timeout Interval: 0:03:00
Last Refreshed: 0:00:14 ago
Attribute Type   Length Value           
---------------- ------ ----------------
PATH_GROUP            7 VZ_NEAR         
VTEP_IP               4 10.255.255.1    
WAN_ID                4 2               

```

## show stun server bindings detail

```text
Current System Time: Thu Mar 14 09:13:46 2024
Transaction ID 000000010affff0500000000
Public Address: 172.16.0.1:4500
Number of Attributes: 3
Timeout Interval: 0:10:00
Timeout: 0:09:00
Attribute Type   Length Value           
---------------- ------ ----------------
PATH_GROUP            6 VZ_OFF          
VTEP_IP               4 10.255.255.5    
WAN_ID                4 1               

Transaction ID 000000010affff0800000000
Public Address: 172.16.1.2:4500
Number of Attributes: 3
Timeout Interval: 0:10:00
Timeout: 0:09:36
Attribute Type   Length Value           
---------------- ------ ----------------
PATH_GROUP            7 VZ_NEAR         
VTEP_IP               4 10.255.255.8    
WAN_ID                4 1               

Transaction ID 000000010affff0a00000000
Public Address: 172.16.1.7:4500
Number of Attributes: 3
Timeout Interval: 0:10:00
Timeout: 0:08:58
Attribute Type   Length Value           
---------------- ------ ----------------
PATH_GROUP            7 VZ_NEAR         
VTEP_IP               4 10.255.255.10   
WAN_ID                4 1               

Transaction ID 000000020affff0b00000000
Public Address: 172.16.0.9:4500
Number of Attributes: 3
Timeout Interval: 0:10:00
Timeout: 0:08:59
Attribute Type   Length Value           
---------------- ------ ----------------
PATH_GROUP            6 VZ_OFF          
VTEP_IP               4 10.255.255.11   
WAN_ID                4 2               

Transaction ID 000000020affff0c00000000
Public Address: 172.16.0.11:4500
Number of Attributes: 3
Timeout Interval: 0:10:00
Timeout: 0:09:00
Attribute Type   Length Value           
---------------- ------ ----------------
PATH_GROUP            6 VZ_OFF          
VTEP_IP               4 10.255.255.12   
WAN_ID                4 2               

```

## show path-selection paths detail

```text
Peer: 10.255.255.4, Path group VZ_NEAR
Path name: path13, static, Label: 8205
Source: 172.16.1.0, Port: 4500, WAN ID: 2
Destination: 172.16.1.5, Port: 4500, WAN ID: 2886729989
Local interface: Ethernet1/3
Route state: IPsec established
Traffic class 0: active (0:00:09)
MTU: 8914

Peer: 10.255.255.5, Path group VZ_OFF
Path name: path3, dynamic, Label: 8195
Source: 172.16.0.4, Port: 4500, WAN ID: 1
Destination: 172.16.0.1, Port: 4500, WAN ID: 1
Local interface: Ethernet1/2
Route state: IPsec established
Traffic class 0: active (0:21:03)
MTU: 8914

Peer: 10.255.255.8, Path group VZ_NEAR
Path name: path5, dynamic, Label: 8197
Source: 172.16.1.0, Port: 4500, WAN ID: 2
Destination: 172.16.1.2, Port: 4500, WAN ID: 1
Local interface: Ethernet1/3
Route state: IPsec established
Traffic class 0: active (0:00:24)
MTU: 8914

Peer: 10.255.255.10, Path group VZ_NEAR
Path name: path11, dynamic, Label: 8203
Source: 172.16.1.0, Port: 4500, WAN ID: 2
Destination: 172.16.1.7, Port: 4500, WAN ID: 1
Local interface: Ethernet1/3
Route state: IPsec established
Traffic class 0: active (0:42:00)
MTU: 1424

Peer: 10.255.255.11, Path group VZ_OFF
Path name: path8, dynamic, Label: 8200
Source: 172.16.0.4, Port: 4500, WAN ID: 1
Destination: 172.16.0.9, Port: 4500, WAN ID: 2
Local interface: Ethernet1/2
Route state: IPsec established
Traffic class 0: active (0:41:59)
MTU: 1424

Peer: 10.255.255.12, Path group VZ_OFF
Path name: path10, dynamic, Label: 8202
Source: 172.16.0.4, Port: 4500, WAN ID: 1
Destination: 172.16.0.11, Port: 4500, WAN ID: 2
Local interface: Ethernet1/2
Route state: IPsec established
Traffic class 0: active (0:41:59)
MTU: 1424

```

## show bgp neighbors

```text
BGP neighbor is 10.255.255.4, remote AS 65000, internal link
  BGP version 4, remote router ID 10.255.255.4, VRF default
  Inherits configuration from and member of peer-group autovpnEdges
  Last read 00:01:55, last write 00:00:53
  Hold time is 180, keepalive interval is 60 seconds
  Configured hold time is 180, keepalive interval is 60 seconds
  Effective minimum hold time is 3 seconds
  Send failure hold time is 0 seconds
  Hold timer is active, time left: 00:01:05
  Keepalive timer is active, time left: 00:00:02
  Connect timer is inactive
  Idle-restart timer is inactive
  BGP state is Established, up for 00:06:31
  Number of transitions to established: 4
  Last state was OpenConfirm
  Last event was RecvUpdate
  Last sent notification:Hold Timer Expired Error/None, Last time 00:07:42, First time 01:10:11, Repeats 2
  Last rcvd notification:Cease/connection collision resolution, Last time 01:09:40, First time 01:09:49, Repeats 2
  Last sent socket-error:Connect (Network is unreachable), Last time 01:14:55, First time 01:15:05, Repeats 2
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
      Received 00:06:30
      Number of stale paths removed after graceful restart: 0
      Number of paths received before End-of-RIB: 5
    L2VPN EVPN End-of-RIB received: Yes
      Received 00:06:30
      Number of stale paths removed after graceful restart: 0
      Number of paths received before End-of-RIB: 12
  AIGP attribute send and receive for IPv4 Unicast are enabled
  AIGP attribute send and receive for IPv4 with MPLS Labels are enabled
  AIGP attribute send and receive for IPv6 Unicast are enabled
  AIGP attribute send and receive for IPv6 with MPLS Labels are enabled
  BGP session driven failover for IPv4 Unicast is disabled
  BGP session driven failover for IPv6 Unicast is disabled
  Message Statistics:
                                  Sent      Rcvd
    Opens:                           7         4
    Notifications:                   3         3
    Updates:                       118       220
    Keepalives:                     79        64
    Enhanced Route Refresh:          0         0
    Begin of Route Refresh:          0         0
    End of Route Refresh:            0         0
    Total messages:                207       291
  Prefix Statistics:
                                   Sent      Rcvd     Best Paths     Best ECMP Paths
    IPv4 Unicast:                     0         0              0                   0
    IPv4 Dps:                        11         1              1                   0
    IPv6 Unicast:                     0         0              0                   0
    EVPN:                            21         4              4                   0
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
  Inbound route map for L2VPN EVPN is DENY-SOO
  Additional-paths send mode:
    Dps: any
Local AS is 65000, local router ID 10.255.255.1
TTL is 255
Local TCP address is 10.255.255.1, local port is 44253
Remote TCP address is 10.255.255.4, remote port is 179
Local next hop for next hop self:
  Dps: 10.255.255.1
  L2VPN EVPN: 10.255.255.1
TCP Socket Information:
  TCP state is ESTABLISHED
  Recv-Q: 0/32768
  Send-Q: 38/46080
  Outgoing Maximum Segment Size (MSS): 1448
  Total Number of TCP retransmissions: 10
  Options:
    Timestamps enabled: yes
    Selective Acknowledgments enabled: yes
    Window Scale enabled: yes
    Explicit Congestion Notification (ECN) enabled: no
  Socket Statistics:
    Window Scale (wscale): 7,7
    Retransmission Timeout (rto): 54272.0ms
    Round-trip Time (rtt/rtvar): 12.0ms/14.6ms
    Delayed Ack Timeout (ato): 40.0ms
    Congestion Window (cwnd): 1
    Slow-start Threshold (ssthresh): 7
    TCP Throughput: 0.97 Mbps
    Recv Round-trip Time (rcv_rtt): 952.0ms
    Advertised Recv Window (rcv_space): 14480

BGP neighbor is 10.255.255.5, remote AS 65000, internal link
  BGP version 4, remote router ID 10.255.255.5, VRF default
  Inherits configuration from and member of peer-group autovpnEdges
  Last read 00:00:33, last write 00:00:20
  Hold time is 180, keepalive interval is 60 seconds
  Configured hold time is 180, keepalive interval is 60 seconds
  Effective minimum hold time is 3 seconds
  Send failure hold time is 0 seconds
  Hold timer is active, time left: 00:02:27
  Keepalive timer is active, time left: 00:00:23
  Connect timer is inactive
  Idle-restart timer is inactive
  BGP state is Established, up for 00:21:03
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
      Received 00:21:02
      Number of stale paths removed after graceful restart: 0
      Number of paths received before End-of-RIB: 2
    L2VPN EVPN End-of-RIB received: Yes
      Received 00:21:02
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
    Updates:                       163         6
    Keepalives:                     18        26
    Enhanced Route Refresh:          0         0
    Begin of Route Refresh:          0         0
    End of Route Refresh:            0         0
    Total messages:                182        33
  Prefix Statistics:
                                   Sent      Rcvd     Best Paths     Best ECMP Paths
    IPv4 Unicast:                     0         0              0                   0
    IPv4 Dps:                        10         2              2                   0
    IPv6 Unicast:                     0         0              0                   0
    EVPN:                            22         3              3                   0
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
  Inbound route map for L2VPN EVPN is DENY-SOO
  Additional-paths send mode:
    Dps: any
Local AS is 65000, local router ID 10.255.255.1
TTL is 255
Local TCP address is 10.255.255.1, local port is 179
Remote TCP address is 10.255.255.5, remote port is 33065
Local next hop for next hop self:
  Dps: 10.255.255.1
  L2VPN EVPN: 10.255.255.1
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
    Round-trip Time (rtt/rtvar): 3.3ms/1.3ms
    Delayed Ack Timeout (ato): 40.0ms
    Congestion Window (cwnd): 10
    TCP Throughput: 34.90 Mbps
    Recv Round-trip Time (rcv_rtt): 4.0ms
    Advertised Recv Window (rcv_space): 14600

BGP neighbor is 10.255.255.8, remote AS 65000, internal link
  BGP version 4, remote router ID 10.255.255.8, VRF default
  Inherits configuration from and member of peer-group autovpnEdges
  Last read 00:02:29, last write 00:00:58
  Hold time is 180, keepalive interval is 60 seconds
  Configured hold time is 180, keepalive interval is 60 seconds
  Effective minimum hold time is 3 seconds
  Send failure hold time is 0 seconds
  Hold timer is active, time left: 00:00:31
  Keepalive timer is inactive
  Connect timer is inactive
  Idle-restart timer is inactive
  BGP state is Established, up for 00:15:56
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
      Received 00:15:56
      Number of stale paths removed after graceful restart: 0
      Number of paths received before End-of-RIB: 2
    L2VPN EVPN End-of-RIB received: Yes
      Received 00:15:56
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
    Updates:                       133        14
    Keepalives:                     14        16
    Enhanced Route Refresh:          0         0
    Begin of Route Refresh:          0         0
    End of Route Refresh:            0         0
    Total messages:                148        31
  Prefix Statistics:
                                   Sent      Rcvd     Best Paths     Best ECMP Paths
    IPv4 Unicast:                     0         0              0                   0
    IPv4 Dps:                        10         2              2                   0
    IPv6 Unicast:                     0         0              0                   0
    EVPN:                            21         4              4                   0
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
  Inbound route map for L2VPN EVPN is DENY-SOO
  Additional-paths send mode:
    Dps: any
Local AS is 65000, local router ID 10.255.255.1
TTL is 255
Local TCP address is 10.255.255.1, local port is 179
Remote TCP address is 10.255.255.8, remote port is 42033
Local next hop for next hop self:
  Dps: 10.255.255.1
  L2VPN EVPN: 10.255.255.1
TCP Socket Information:
  TCP state is ESTABLISHED
  Recv-Q: 0/32768
  Send-Q: 1881/46080
  Outgoing Maximum Segment Size (MSS): 1448
  Total Number of TCP retransmissions: 23
  Options:
    Timestamps enabled: yes
    Selective Acknowledgments enabled: yes
    Window Scale enabled: yes
    Explicit Congestion Notification (ECN) enabled: no
  Socket Statistics:
    Window Scale (wscale): 7,7
    Retransmission Timeout (rto): 109568.0ms
    Round-trip Time (rtt/rtvar): 82.6ms/126.9ms
    Delayed Ack Timeout (ato): 40.0ms
    Congestion Window (cwnd): 1
    Slow-start Threshold (ssthresh): 2
    TCP Throughput: 0.14 Mbps
    Recv Round-trip Time (rcv_rtt): 1.0ms
    Advertised Recv Window (rcv_space): 14600

BGP neighbor is 10.255.255.10, remote AS 65000, internal link
  BGP version 4, remote router ID 10.255.255.10, VRF default
  Inherits configuration from and member of peer-group autovpnEdges
  Last read 00:00:21, last write 00:00:17
  Hold time is 180, keepalive interval is 60 seconds
  Configured hold time is 180, keepalive interval is 60 seconds
  Effective minimum hold time is 3 seconds
  Send failure hold time is 0 seconds
  Hold timer is active, time left: 00:02:39
  Keepalive timer is active, time left: 00:00:29
  Connect timer is inactive
  Idle-restart timer is inactive
  BGP state is Established, up for 01:08:33
  Number of transitions to established: 1
  Last state was OpenConfirm
  Last event was ReapplyInboundPolicy
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
      Received 01:08:32
      Number of stale paths removed after graceful restart: 0
      Number of paths received before End-of-RIB: 2
    L2VPN EVPN End-of-RIB received: Yes
      Received 01:08:32
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
    Updates:                       221         6
    Keepalives:                     63        84
    Enhanced Route Refresh:          0         0
    Begin of Route Refresh:          0         0
    End of Route Refresh:            0         0
    Total messages:                285        91
  Prefix Statistics:
                                   Sent      Rcvd     Best Paths     Best ECMP Paths
    IPv4 Unicast:                     0         0              0                   0
    IPv4 Dps:                        10         2              2                   0
    IPv6 Unicast:                     0         0              0                   0
    EVPN:                            21         4              4                   0
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
  Inbound route map for L2VPN EVPN is DENY-SOO
  Additional-paths send mode:
    Dps: any
Local AS is 65000, local router ID 10.255.255.1
TTL is 255
Local TCP address is 10.255.255.1, local port is 179
Remote TCP address is 10.255.255.10, remote port is 38375
Local next hop for next hop self:
  Dps: 10.255.255.1
  L2VPN EVPN: 10.255.255.1
TCP Socket Information:
  TCP state is ESTABLISHED
  Recv-Q: 0/32768
  Send-Q: 0/46080
  Outgoing Maximum Segment Size (MSS): 1372
  Total Number of TCP retransmissions: 12
  Options:
    Timestamps enabled: yes
    Selective Acknowledgments enabled: yes
    Window Scale enabled: yes
    Explicit Congestion Notification (ECN) enabled: no
  Socket Statistics:
    Window Scale (wscale): 7,7
    Retransmission Timeout (rto): 204.0ms
    Round-trip Time (rtt/rtvar): 3.0ms/1.2ms
    Delayed Ack Timeout (ato): 40.0ms
    Congestion Window (cwnd): 4
    Slow-start Threshold (ssthresh): 7
    TCP Throughput: 14.79 Mbps
    Advertised Recv Window (rcv_space): 14600

BGP neighbor is 10.255.255.11, remote AS 65000, internal link
  BGP version 4, remote router ID 10.255.255.11, VRF default
  Inherits configuration from and member of peer-group autovpnEdges
  Last read 00:00:44, last write 00:00:16
  Hold time is 180, keepalive interval is 60 seconds
  Configured hold time is 180, keepalive interval is 60 seconds
  Effective minimum hold time is 3 seconds
  Send failure hold time is 0 seconds
  Hold timer is active, time left: 00:02:16
  Keepalive timer is active, time left: 00:00:34
  Connect timer is inactive
  Idle-restart timer is inactive
  BGP state is Established, up for 01:08:31
  Number of transitions to established: 1
  Last state was OpenConfirm
  Last event was ReapplyInboundPolicy
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
      Received 01:08:29
      Number of stale paths removed after graceful restart: 0
      Number of paths received before End-of-RIB: 2
    L2VPN EVPN End-of-RIB received: Yes
      Received 01:08:29
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
    Updates:                       221         6
    Keepalives:                     60        81
    Enhanced Route Refresh:          0         0
    Begin of Route Refresh:          0         0
    End of Route Refresh:            0         0
    Total messages:                282        88
  Prefix Statistics:
                                   Sent      Rcvd     Best Paths     Best ECMP Paths
    IPv4 Unicast:                     0         0              0                   0
    IPv4 Dps:                        10         2              2                   0
    IPv6 Unicast:                     0         0              0                   0
    EVPN:                            22         3              3                   0
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
  Inbound route map for L2VPN EVPN is DENY-SOO
  Additional-paths send mode:
    Dps: any
Local AS is 65000, local router ID 10.255.255.1
TTL is 255
Local TCP address is 10.255.255.1, local port is 179
Remote TCP address is 10.255.255.11, remote port is 38521
Local next hop for next hop self:
  Dps: 10.255.255.1
  L2VPN EVPN: 10.255.255.1
TCP Socket Information:
  TCP state is ESTABLISHED
  Recv-Q: 0/32768
  Send-Q: 0/46080
  Outgoing Maximum Segment Size (MSS): 1372
  Total Number of TCP retransmissions: 10
  Options:
    Timestamps enabled: yes
    Selective Acknowledgments enabled: yes
    Window Scale enabled: yes
    Explicit Congestion Notification (ECN) enabled: no
  Socket Statistics:
    Window Scale (wscale): 7,7
    Retransmission Timeout (rto): 208.0ms
    Round-trip Time (rtt/rtvar): 4.5ms/1.3ms
    Delayed Ack Timeout (ato): 40.0ms
    Congestion Window (cwnd): 4
    Slow-start Threshold (ssthresh): 7
    TCP Throughput: 9.65 Mbps
    Recv Round-trip Time (rcv_rtt): 4.0ms
    Advertised Recv Window (rcv_space): 14600

BGP neighbor is 10.255.255.12, remote AS 65000, internal link
  BGP version 4, remote router ID 10.255.255.12, VRF default
  Inherits configuration from and member of peer-group autovpnEdges
  Last read 00:00:13, last write 00:00:17
  Hold time is 180, keepalive interval is 60 seconds
  Configured hold time is 180, keepalive interval is 60 seconds
  Effective minimum hold time is 3 seconds
  Send failure hold time is 0 seconds
  Hold timer is active, time left: 00:02:47
  Keepalive timer is active, time left: 00:00:30
  Connect timer is inactive
  Idle-restart timer is inactive
  BGP state is Established, up for 01:08:27
  Number of transitions to established: 1
  Last state was OpenConfirm
  Last event was ReapplyInboundPolicy
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
      Received 01:08:26
      Number of stale paths removed after graceful restart: 0
      Number of paths received before End-of-RIB: 2
    L2VPN EVPN End-of-RIB received: Yes
      Received 01:08:26
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
    Updates:                       221         6
    Keepalives:                     62        81
    Enhanced Route Refresh:          0         0
    Begin of Route Refresh:          0         0
    End of Route Refresh:            0         0
    Total messages:                284        88
  Prefix Statistics:
                                   Sent      Rcvd     Best Paths     Best ECMP Paths
    IPv4 Unicast:                     0         0              0                   0
    IPv4 Dps:                        10         2              2                   0
    IPv6 Unicast:                     0         0              0                   0
    EVPN:                            22         3              3                   0
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
  Inbound route map for L2VPN EVPN is DENY-SOO
  Additional-paths send mode:
    Dps: any
Local AS is 65000, local router ID 10.255.255.1
TTL is 255
Local TCP address is 10.255.255.1, local port is 179
Remote TCP address is 10.255.255.12, remote port is 40095
Local next hop for next hop self:
  Dps: 10.255.255.1
  L2VPN EVPN: 10.255.255.1
TCP Socket Information:
  TCP state is ESTABLISHED
  Recv-Q: 0/32768
  Send-Q: 0/46080
  Outgoing Maximum Segment Size (MSS): 1372
  Total Number of TCP retransmissions: 10
  Options:
    Timestamps enabled: yes
    Selective Acknowledgments enabled: yes
    Window Scale enabled: yes
    Explicit Congestion Notification (ECN) enabled: no
  Socket Statistics:
    Window Scale (wscale): 7,7
    Retransmission Timeout (rto): 204.0ms
    Round-trip Time (rtt/rtvar): 3.2ms/1.3ms
    Delayed Ack Timeout (ato): 40.0ms
    Congestion Window (cwnd): 4
    Slow-start Threshold (ssthresh): 7
    TCP Throughput: 13.92 Mbps
    Advertised Recv Window (rcv_space): 14600

```

## show bgp path-selection detail

```text
BGP routing table information for VRF default
Router identifier 10.255.255.1, local AS number 65000
Bgp routing table entry for ipv4Dps VTEP 10.255.255.5/32
 Paths: 1 available
  Local (Received from a RR-client)
    :: from 10.255.255.5 (10.255.255.5)
      Origin IGP, metric -, localpref 100, weight 0, received 00:21:03 ago, valid, internal
      Tunnel encapsulation attribute: Dynamic path selection
        Endpoint: 172.16.0.1, Path group name: VZ_OFF, WAN ID: 1, UDP port: 4500
Bgp routing table entry for ipv4Dps VTEP 10.255.255.8/32
 Paths: 1 available
  Local (Received from a RR-client)
    :: from 10.255.255.8 (10.255.255.8)
      Origin IGP, metric -, localpref 100, weight 0, received 00:08:28 ago, valid, internal
      Tunnel encapsulation attribute: Dynamic path selection
        Endpoint: 172.16.1.2, Path group name: VZ_NEAR, WAN ID: 1, UDP port: 4500
Bgp routing table entry for ipv4Dps VTEP 10.255.255.10/32
 Paths: 1 available
  Local (Received from a RR-client)
    :: from 10.255.255.10 (10.255.255.10)
      Origin IGP, metric -, localpref 100, weight 0, received 01:08:33 ago, valid, internal
      Tunnel encapsulation attribute: Dynamic path selection
        Endpoint: 172.16.1.7, Path group name: VZ_NEAR, WAN ID: 1, UDP port: 4500
Bgp routing table entry for ipv4Dps VTEP 10.255.255.11/32
 Paths: 1 available
  Local (Received from a RR-client)
    :: from 10.255.255.11 (10.255.255.11)
      Origin IGP, metric -, localpref 100, weight 0, received 01:08:31 ago, valid, internal
      Tunnel encapsulation attribute: Dynamic path selection
        Endpoint: 172.16.0.9, Path group name: VZ_OFF, WAN ID: 2, UDP port: 4500
Bgp routing table entry for ipv4Dps VTEP 10.255.255.12/32
 Paths: 1 available
  Local (Received from a RR-client)
    :: from 10.255.255.12 (10.255.255.12)
      Origin IGP, metric -, localpref 100, weight 0, received 01:08:27 ago, valid, internal
      Tunnel encapsulation attribute: Dynamic path selection
        Endpoint: 172.16.0.11, Path group name: VZ_OFF, WAN ID: 2, UDP port: 4500
Bgp routing table entry for ipv4Ipsec VTEP 10.255.255.1/32
 Paths: 1 available
  Local
    - from - (0.0.0.0)
      Origin IGP, metric -, localpref -, weight 0, received 01:14:10 ago, valid, local
      Tunnel encapsulation attribute: IP security
        Initial contact: false, Rekey counter: 0, Nonce length: 32
        DH group: 14, DH key length: 256
        Encryption algo: aes256, Authentication algo: sha256
Bgp routing table entry for ipv4Ipsec VTEP 10.255.255.4/32
 Paths: 1 available
  Local (Received from a RR-client)
    :: from 10.255.255.4 (10.255.255.4)
      Origin IGP, metric -, localpref 100, weight 0, received 00:06:31 ago, valid, internal
      Tunnel encapsulation attribute: IP security
        Initial contact: false, Rekey counter: 0, Nonce length: 32
        DH group: 14, DH key length: 256
        Encryption algo: aes256, Authentication algo: sha256
Bgp routing table entry for ipv4Ipsec VTEP 10.255.255.5/32
 Paths: 1 available
  Local (Received from a RR-client)
    :: from 10.255.255.5 (10.255.255.5)
      Origin IGP, metric -, localpref 100, weight 0, received 00:21:03 ago, valid, internal
      Tunnel encapsulation attribute: IP security
        Initial contact: false, Rekey counter: 0, Nonce length: 32
        DH group: 14, DH key length: 256
        Encryption algo: aes256, Authentication algo: sha256
Bgp routing table entry for ipv4Ipsec VTEP 10.255.255.8/32
 Paths: 1 available
  Local (Received from a RR-client)
    :: from 10.255.255.8 (10.255.255.8)
      Origin IGP, metric -, localpref 100, weight 0, received 00:15:57 ago, valid, internal
      Tunnel encapsulation attribute: IP security
        Initial contact: false, Rekey counter: 5, Nonce length: 32
        DH group: 14, DH key length: 256
        Encryption algo: aes256, Authentication algo: sha256
Bgp routing table entry for ipv4Ipsec VTEP 10.255.255.10/32
 Paths: 1 available
  Local (Received from a RR-client)
    :: from 10.255.255.10 (10.255.255.10)
      Origin IGP, metric -, localpref 100, weight 0, received 01:08:33 ago, valid, internal
      Tunnel encapsulation attribute: IP security
        Initial contact: false, Rekey counter: 2, Nonce length: 32
        DH group: 14, DH key length: 256
        Encryption algo: aes256, Authentication algo: sha256
Bgp routing table entry for ipv4Ipsec VTEP 10.255.255.11/32
 Paths: 1 available
  Local (Received from a RR-client)
    :: from 10.255.255.11 (10.255.255.11)
      Origin IGP, metric -, localpref 100, weight 0, received 01:08:31 ago, valid, internal
      Tunnel encapsulation attribute: IP security
        Initial contact: false, Rekey counter: 3, Nonce length: 32
        DH group: 14, DH key length: 256
        Encryption algo: aes256, Authentication algo: sha256
Bgp routing table entry for ipv4Ipsec VTEP 10.255.255.12/32
 Paths: 1 available
  Local (Received from a RR-client)
    :: from 10.255.255.12 (10.255.255.12)
      Origin IGP, metric -, localpref 100, weight 0, received 01:08:27 ago, valid, internal
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
>C    10.255.255.1/32 [0 pref/0 metric] updated 01:15:11 ago
         via Loopback0, directly connected
>C    172.16.0.4/31 [0 pref/0 metric] updated 00:42:12 ago
         via Ethernet1/2, directly connected
>C    172.16.1.0/31 [0 pref/0 metric] updated 00:42:12 ago
         via Ethernet1/3, directly connected
>C    172.28.128.0/20 [0 pref/0 metric] updated 01:14:41 ago
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
>S    0.0.0.0/0 [1 pref/0 metric] updated 00:42:12 ago
         via 172.16.0.5 [0 pref/0 metric] type ipv4
            via 172.16.0.5, Ethernet1/2
>S    10.80.0.0/12 [1 pref/0 metric] updated 01:14:41 ago
         via 172.28.128.1 [0 pref/0 metric] type ipv4
            via 172.28.128.1, Management1/1
>S    10.224.0.0/12 [1 pref/0 metric] updated 01:14:41 ago
         via 172.28.128.1 [0 pref/0 metric] type ipv4
            via 172.28.128.1, Management1/1
>S    10.240.0.0/12 [1 pref/0 metric] updated 01:14:41 ago
         via 172.28.128.1 [0 pref/0 metric] type ipv4
            via 172.28.128.1, Management1/1
>S    172.16.0.0/12 [1 pref/0 metric] updated 01:14:41 ago
         via 172.28.128.1 [0 pref/0 metric] type ipv4
            via 172.28.128.1, Management1/1
>S    172.16.0.0/24 [1 pref/0 metric] updated 00:42:12 ago
         via 172.16.0.5 [0 pref/0 metric] type ipv4
            via 172.16.0.5, Ethernet1/2
>S    172.16.1.0/24 [1 pref/0 metric] updated 00:42:12 ago
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
>P    0.0.0.0/8 [1 pref/0 metric] updated 01:15:10 ago
         via Null0, directly connected [NF]
>P    10.255.255.4/32 [1 pref/0 metric] updated 00:42:15 ago
         via 10.255.255.4, Dps1
>P    10.255.255.5/32 [1 pref/0 metric] updated 00:40:38 ago
         via 10.255.255.5, Dps1
>P    10.255.255.8/32 [1 pref/0 metric] updated 00:42:10 ago
         via 10.255.255.8, Dps1
>P    10.255.255.10/32 [1 pref/0 metric] updated 00:42:10 ago
         via 10.255.255.10, Dps1
>P    10.255.255.11/32 [1 pref/0 metric] updated 00:42:09 ago
         via 10.255.255.11, Dps1
>P    10.255.255.12/32 [1 pref/0 metric] updated 00:42:09 ago
         via 10.255.255.12, Dps1
>P    127.0.0.0/8 [1 pref/0 metric] updated 01:15:10 ago
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
>P    ::/96 [1 pref/0 metric] updated 01:14:11 ago
         via Null0, directly connected [NF]
>P    ::ffff:127.0.0.0/104 [1 pref/0 metric] updated 01:14:11 ago
         via :: [1 pref/1 metric] type ipv6
            via , directly connected
>P    fe80::/10 [1 pref/0 metric] updated 01:14:11 ago
```

