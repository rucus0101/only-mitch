# Test results for IND517

## show version

```text
Arista AWE-5510-F
Hardware version: 11.01
Serial number: WTW23250084
Hardware MAC address: ec8a.4804.ff6e
System MAC address: ec8a.4804.ff6e

Software image version: 4.31.2F
Architecture: x86_64
Internal build version: 4.31.2F-35442176.4312F
Internal build ID: 500c58e3-5beb-4481-afe9-8ad77245cc44
Image format version: 3.0
Image optimization: Default

Uptime: 17 hours and 1 minute
Total memory: 65396488 kB
Free memory: 39958536 kB

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
Ethernet1/1      10.5.255.0/31        up         up              1500          
Ethernet1/2      172.16.255.0/31      up         up              9000          
Ethernet1/3      172.16.3.3/31        up         up              1500          
Ethernet1/4      172.16.2.5/31        up         up              9000          
Loopback0        10.255.255.3/32      up         up             65535          
Management1/1    172.28.138.223/20    up         up              1500          

```

## show interfaces counters rates | nz

```text
Port      Name      Intvl  In Mbps      %  In Kpps Out Mbps      % Out Kpps
Et1/1                5:00    174.8   1.8%       21     58.3   0.6%        7
Et1/2                5:00      0.0   0.0%        0    126.3   1.3%       15
Et1/4     ATT        5:00     62.9   0.6%        7     52.4   0.5%        6
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
 S        10.255.255.2/32
           directly connected, Dps1
 C        10.255.255.3/32
           directly connected, Loopback0
 S        10.255.255.4/32
           directly connected, Dps1
 S        10.255.255.7/32
           directly connected, Dps1
 S        10.255.255.9/32
           directly connected, Dps1
 S        10.240.0.0/12 [1/0]
           via 172.28.128.1, Management1/1
 C        172.16.2.4/31
           directly connected, Ethernet1/4
 S        172.16.2.0/24 [1/0]
           via 172.16.2.4, Ethernet1/4
 C        172.16.3.2/31
           directly connected, Ethernet1/3
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
 S        10.255.255.2/32
           directly connected, Dps1
 C        10.255.255.3/32
           directly connected, Loopback0
 S        10.255.255.4/32
           directly connected, Dps1
 S        10.255.255.7/32
           directly connected, Dps1
 S        10.255.255.9/32
           directly connected, Dps1
 S        10.240.0.0/12 [1/0]
           via 172.28.128.1, Management1/1
 C        172.16.2.4/31
           directly connected, Ethernet1/4
 S        172.16.2.0/24 [1/0]
           via 172.16.2.4, Ethernet1/4
 C        172.16.3.2/31
           directly connected, Ethernet1/3
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
           via 172.16.255.1, Ethernet1/2
 B I      10.0.255.2/31 [20/0]
           via 172.16.255.1, Ethernet1/2
 B I      10.1.255.0/31 [20/0]
           via 172.16.255.1, Ethernet1/2
 B I      10.1.255.2/31 [20/0]
           via VTEP 10.255.255.2 VNI 201 router-mac ec:8a:48:04:f5:69
 B I      10.2.255.0/31 [20/0]
           via VTEP 10.255.255.7 VNI 201 router-mac ec:8a:48:04:2b:da
 B I      10.2.255.2/31 [20/0]
           via 172.16.255.1, Ethernet1/2
 B I      10.4.255.0/31 [20/0]
           via VTEP 10.255.255.9 VNI 201 router-mac 00:50:56:47:de:91
 B I      10.4.255.2/31 [20/0]
           via 172.16.255.1, Ethernet1/2
 C        10.5.255.0/31
           directly connected, Ethernet1/1
 B I      10.5.255.2/31 [20/0]
           via 172.16.255.1, Ethernet1/2
 B I      10.6.255.0/31 [20/0]
           via 172.16.255.1, Ethernet1/2
 B I      10.6.255.2/31 [20/0]
           via 172.16.255.1, Ethernet1/2
 B I      10.255.254.1/32 [20/0]
           via 172.16.255.1, Ethernet1/2
 B I      10.255.254.2/32 [20/0]
           via VTEP 10.255.255.2 VNI 201 router-mac ec:8a:48:04:f5:69
 B I      10.255.254.3/32 [20/0]
           via VTEP 10.255.255.7 VNI 201 router-mac ec:8a:48:04:2b:da
 B I      10.255.254.4/32 [20/0]
           via 172.16.255.1, Ethernet1/2
 B I      10.255.254.5/32 [20/0]
           via VTEP 10.255.255.9 VNI 201 router-mac 00:50:56:47:de:91
 O        10.255.254.6/32 [110/20]
           via 10.5.255.1, Ethernet1/1
 C        172.16.255.0/31
           directly connected, Ethernet1/2
 B I      172.16.255.2/31 [20/0]
           via VTEP 10.255.255.2 VNI 201 router-mac ec:8a:48:04:f5:69
 B I      192.168.0.0/24 [20/0]
           via 172.16.255.1, Ethernet1/2
 B I      192.168.1.0/24 [20/0]
           via VTEP 10.255.255.2 VNI 201 router-mac ec:8a:48:04:f5:69
 B I      192.168.3.0/24 [20/0]
           via VTEP 10.255.255.7 VNI 201 router-mac ec:8a:48:04:2b:da
 O        192.168.5.0/24 [110/20]
           via 10.5.255.1, Ethernet1/1
 B I      192.168.6.0/24 [20/0]
           via 172.16.255.1, Ethernet1/2
 B I      192.168.40.0/24 [20/0]
           via VTEP 10.255.255.9 VNI 201 router-mac 00:50:56:47:de:91

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
Router identifier 10.255.255.3, local AS number 65000
Route status codes: * - valid, > - active, S - Stale, E - ECMP head, e - ECMP
                    c - Contributing to ECMP, % - Pending best path selection
Origin codes: i - IGP, e - EGP, ? - incomplete
AS Path Attributes: Or-ID - Originator ID, C-LST - Cluster List, LL Nexthop - Link Local Nexthop

          Network                Next Hop              Metric  LocPref Weight  Path
 * >      RD: 10.255.255.2:1 ip-prefix 10.0.255.0/31
                                 10.255.255.2          -       5       0       i Or-ID: 10.255.255.5 C-LST: 10.255.255.2 172.16.255.3 10.255.255.4 
 * >      RD: 10.255.255.3:1 ip-prefix 10.0.255.0/31
                                 -                     -       5       0       i
 * >      RD: 10.255.255.2:1 ip-prefix 10.0.255.2/31
                                 10.255.255.2          -       5       0       i Or-ID: 10.255.255.6 C-LST: 10.255.255.2 172.16.255.3 10.255.255.4 
 * >      RD: 10.255.255.3:1 ip-prefix 10.0.255.2/31
                                 -                     -       5       0       i
 * >      RD: 10.255.255.2:1 ip-prefix 10.1.255.0/31
                                 10.255.255.2          -       5       0       i
 * >      RD: 10.255.255.3:1 ip-prefix 10.1.255.0/31
                                 -                     -       5       0       i
 * >      RD: 10.255.255.2:1 ip-prefix 10.1.255.2/31
                                 10.255.255.2          -       100     0       i
 * >Ec    RD: 10.255.255.7:1 ip-prefix 10.2.255.0/31
                                 10.255.255.7          -       100     0       i Or-ID: 10.255.255.7 C-LST: 10.255.255.2 
 *  ec    RD: 10.255.255.7:1 ip-prefix 10.2.255.0/31
                                 10.255.255.7          -       100     0       i
 * >      RD: 10.255.255.2:1 ip-prefix 10.2.255.2/31
                                 10.255.255.2          -       5       0       i
 * >      RD: 10.255.255.3:1 ip-prefix 10.2.255.2/31
                                 -                     -       5       0       i Or-ID: 10.255.255.8 C-LST: 10.5.255.2 10.255.255.1 
 * >Ec    RD: 10.255.255.9:1 ip-prefix 10.4.255.0/31
                                 10.255.255.9          -       100     0       i Or-ID: 10.255.255.9 C-LST: 10.255.255.2 
 *  ec    RD: 10.255.255.9:1 ip-prefix 10.4.255.0/31
                                 10.255.255.9          -       100     0       i
 * >      RD: 10.255.255.2:1 ip-prefix 10.4.255.2/31
                                 10.255.255.2          -       5       0       i
 * >      RD: 10.255.255.3:1 ip-prefix 10.4.255.2/31
                                 -                     -       5       0       i Or-ID: 10.255.255.10 C-LST: 10.5.255.2 10.255.255.1 
 * >      RD: 10.255.255.3:1 ip-prefix 10.5.255.0/31
                                 -                     -       -       0       i
 * >      RD: 10.255.255.2:1 ip-prefix 10.5.255.2/31
                                 10.255.255.2          -       5       0       i
 * >      RD: 10.255.255.3:1 ip-prefix 10.5.255.2/31
                                 -                     -       5       0       i
 * >      RD: 10.255.255.2:1 ip-prefix 10.6.255.0/31
                                 10.255.255.2          -       5       0       i Or-ID: 10.255.255.11 C-LST: 10.255.255.2 172.16.255.3 10.255.255.4 
 * >      RD: 10.255.255.3:1 ip-prefix 10.6.255.0/31
                                 -                     -       5       0       i
 * >      RD: 10.255.255.2:1 ip-prefix 10.6.255.2/31
                                 10.255.255.2          -       5       0       i
 * >      RD: 10.255.255.3:1 ip-prefix 10.6.255.2/31
                                 -                     -       5       0       i Or-ID: 10.255.255.12 C-LST: 10.5.255.2 10.255.255.1 
 * >      RD: 10.255.255.2:1 ip-prefix 10.255.254.1/32
                                 10.255.255.2          -       5       0       i Or-ID: 10.255.255.5 C-LST: 10.255.255.2 172.16.255.3 10.255.255.4 
 * >      RD: 10.255.255.3:1 ip-prefix 10.255.254.1/32
                                 -                     -       5       0       i
 * >      RD: 10.255.255.2:1 ip-prefix 10.255.254.2/32
                                 10.255.255.2          -       100     0       i
 * >      RD: 10.255.255.3:1 ip-prefix 10.255.254.2/32
                                 -                     -       5       0       i
 * >      RD: 10.255.255.2:1 ip-prefix 10.255.254.3/32
                                 10.255.255.2          -       5       0       i
 * >      RD: 10.255.255.3:1 ip-prefix 10.255.254.3/32
                                 -                     -       5       0       i
 * >Ec    RD: 10.255.255.7:1 ip-prefix 10.255.254.3/32
                                 10.255.255.7          -       100     0       i Or-ID: 10.255.255.7 C-LST: 10.255.255.2 
 *  ec    RD: 10.255.255.7:1 ip-prefix 10.255.254.3/32
                                 10.255.255.7          -       100     0       i
 * >      RD: 10.255.255.2:1 ip-prefix 10.255.254.4/32
                                 10.255.255.2          -       5       0       i
 * >      RD: 10.255.255.3:1 ip-prefix 10.255.254.4/32
                                 -                     -       5       0       i Or-ID: 10.255.255.12 C-LST: 10.5.255.2 10.255.255.1 
 * >      RD: 10.255.255.2:1 ip-prefix 10.255.254.5/32
                                 10.255.255.2          -       5       0       i
 * >      RD: 10.255.255.3:1 ip-prefix 10.255.254.5/32
                                 -                     -       5       0       i
 * >Ec    RD: 10.255.255.9:1 ip-prefix 10.255.254.5/32
                                 10.255.255.9          -       100     0       i
 *  ec    RD: 10.255.255.9:1 ip-prefix 10.255.254.5/32
                                 10.255.255.9          -       100     0       i Or-ID: 10.255.255.9 C-LST: 10.255.255.2 
          RD: 10.255.255.2:1 ip-prefix 10.255.254.6/32
                                 PolicyReject          -       -       0       i
 * >      RD: 10.255.255.3:1 ip-prefix 10.255.254.6/32
                                 -                     -       -       0       i
 * >      RD: 10.255.255.2:1 ip-prefix 172.16.255.0/31
                                 10.255.255.2          -       5       0       i
 * >      RD: 10.255.255.3:1 ip-prefix 172.16.255.0/31
                                 -                     -       -       0       i
 *        RD: 10.255.255.3:1 ip-prefix 172.16.255.0/31
                                 -                     -       5       0       i
 * >      RD: 10.255.255.2:1 ip-prefix 172.16.255.2/31
                                 10.255.255.2          -       100     0       i
 * >      RD: 10.255.255.3:1 ip-prefix 172.16.255.2/31
                                 -                     -       5       0       i
 * >      RD: 10.255.255.2:1 ip-prefix 192.168.0.0/24
                                 10.255.255.2          -       5       0       i Or-ID: 10.255.255.5 C-LST: 10.255.255.2 172.16.255.3 10.255.255.4 
 * >      RD: 10.255.255.3:1 ip-prefix 192.168.0.0/24
                                 -                     -       5       0       i
 * >      RD: 10.255.255.2:1 ip-prefix 192.168.1.0/24
                                 10.255.255.2          -       100     0       i
 * >      RD: 10.255.255.3:1 ip-prefix 192.168.1.0/24
                                 -                     -       5       0       i
 * >      RD: 10.255.255.2:1 ip-prefix 192.168.3.0/24
                                 10.255.255.2          -       5       0       i
 * >      RD: 10.255.255.3:1 ip-prefix 192.168.3.0/24
                                 -                     -       5       0       i
 * >Ec    RD: 10.255.255.7:1 ip-prefix 192.168.3.0/24
                                 10.255.255.7          -       100     0       i Or-ID: 10.255.255.7 C-LST: 10.255.255.2 
 *  ec    RD: 10.255.255.7:1 ip-prefix 192.168.3.0/24
                                 10.255.255.7          -       100     0       i
          RD: 10.255.255.2:1 ip-prefix 192.168.5.0/24
                                 PolicyReject          -       -       0       i
 * >      RD: 10.255.255.3:1 ip-prefix 192.168.5.0/24
                                 -                     -       -       0       i
 * >      RD: 10.255.255.2:1 ip-prefix 192.168.6.0/24
                                 10.255.255.2          -       5       0       i
 * >      RD: 10.255.255.3:1 ip-prefix 192.168.6.0/24
                                 -                     -       5       0       i Or-ID: 10.255.255.12 C-LST: 10.5.255.2 10.255.255.1 
 * >      RD: 10.255.255.2:1 ip-prefix 192.168.40.0/24
                                 10.255.255.2          -       5       0       i
 * >      RD: 10.255.255.3:1 ip-prefix 192.168.40.0/24
                                 -                     -       5       0       i
 * >Ec    RD: 10.255.255.9:1 ip-prefix 192.168.40.0/24
                                 10.255.255.9          -       100     0       i
 *  ec    RD: 10.255.255.9:1 ip-prefix 192.168.40.0/24
                                 10.255.255.9          -       100     0       i Or-ID: 10.255.255.9 C-LST: 10.255.255.2 
```

## show ip security connection detail

```text
path5:
  Source address: 172.16.2.5, Destination address: 172.16.2.7
  State: established
  Uptime: 16 hours, 58 minutes, 40 seconds
  VRF: default
  Type: static
  Remote IP: 10.255.255.2
  Role: initiator
  Inbound SPI: 0xcda7f1:
    Request ID: 3, Mode: transport, Replay window size: 16384, Seq: 0x0
    Errors:
      Packets outside replay window: 0, Replay: 0, Integrity failed: 0
    Lifetime config:
      Soft byte limit: 3268285337249, Hard byte limit: 6442450944000
      Soft packet limit: 2553330719, Hard packet limit: 4000000000
      Soft time limit: 2953 secs, Hard time limit: 3600 secs
    Lifetime current:
      Current bytes: 638144
      Current packets: 2328
      SA add time: Fri Mar 15 06:05:11 2024
      SA last use time: Fri Mar 15 06:17:06 2024
  Outbound SPI: 0xc32c69:
    Request ID: 3, Mode: transport, Replay window size: 0, Seq: 0x0
    Errors:
      Packets outside replay window: 0, Replay: 0, Integrity failed: 0
    Lifetime config:
      Soft byte limit: 3631998194999, Hard byte limit: 6442450944000
      Soft packet limit: 2180476621, Hard packet limit: 4000000000
      Soft time limit: 3056 secs, Hard time limit: 3600 secs
    Lifetime current:
      Current bytes: 504415
      Current packets: 4756
      SA add time: Fri Mar 15 06:05:11 2024
      SA last use time: Fri Mar 15 06:17:06 2024
path6:
  Source address: 172.16.2.5, Destination address: 172.16.2.2
  State: established
  Uptime: 13 hours, 30 minutes, 38 seconds
  VRF: default
  Type: static
  Remote IP: 10.255.255.2
  Role: initiator
  Inbound SPI: 0xc72ac4:
    Request ID: 9, Mode: transport, Replay window size: 16384, Seq: 0x0
    Errors:
      Packets outside replay window: 0, Replay: 0, Integrity failed: 0
    Lifetime config:
      Soft byte limit: 4565185597499, Hard byte limit: 6442450944000
      Soft packet limit: 2650031824, Hard packet limit: 4000000000
      Soft time limit: 2751 secs, Hard time limit: 3600 secs
    Lifetime current:
      Current bytes: 5285847560
      Current packets: 4988146
      SA add time: Fri Mar 15 06:05:44 2024
      SA last use time: Fri Mar 15 06:17:06 2024
  Outbound SPI: 0xc3627c:
    Request ID: 9, Mode: transport, Replay window size: 0, Seq: 0x0
    Errors:
      Packets outside replay window: 0, Replay: 0, Integrity failed: 0
    Lifetime config:
      Soft byte limit: 4278675421499, Hard byte limit: 6442450944000
      Soft packet limit: 2470644277, Hard packet limit: 4000000000
      Soft time limit: 2665 secs, Hard time limit: 3600 secs
    Lifetime current:
      Current bytes: 4231077777
      Current packets: 8314560
      SA add time: Fri Mar 15 06:05:44 2024
      SA last use time: Fri Mar 15 06:17:06 2024
path7:
  Source address: 172.16.3.3, Destination address: 172.16.2.7
  State: idle
  Uptime: N/A
  VRF: default
  Type: static
  Remote IP: 10.255.255.2
  Role: initiator
path8:
  Source address: 172.16.3.3, Destination address: 172.16.2.2
  State: idle
  Uptime: N/A
  VRF: default
  Type: static
  Remote IP: 10.255.255.2
  Role: initiator
path9:
  Source address: 172.16.3.3, Destination address: 172.16.2.0
  State: idle
  Uptime: N/A
  VRF: default
  Type: static
  Remote IP: 10.255.255.2
  Role: initiator
path10:
  Source address: 172.16.2.5, Destination address: 172.16.2.0
  State: established
  Uptime: 16 hours, 58 minutes, 43 seconds
  VRF: default
  Type: static
  Remote IP: 10.255.255.2
  Role: initiator
  Inbound SPI: 0xc714be:
    Request ID: 1, Mode: transport, Replay window size: 16384, Seq: 0x0
    Errors:
      Packets outside replay window: 0, Replay: 0, Integrity failed: 0
    Lifetime config:
      Soft byte limit: 3842590649999, Hard byte limit: 6442450944000
      Soft packet limit: 2687585170, Hard packet limit: 4000000000
      Soft time limit: 2634 secs, Hard time limit: 3600 secs
    Lifetime current:
      Current bytes: 1158500
      Current packets: 3649
      SA add time: Fri Mar 15 05:58:37 2024
      SA last use time: Fri Mar 15 06:17:06 2024
  Outbound SPI: 0xc06392:
    Request ID: 1, Mode: transport, Replay window size: 0, Seq: 0x0
    Errors:
      Packets outside replay window: 0, Replay: 0, Integrity failed: 0
    Lifetime config:
      Soft byte limit: 4399825032749, Hard byte limit: 6442450944000
      Soft packet limit: 2627735927, Hard packet limit: 4000000000
      Soft time limit: 2773 secs, Hard time limit: 3600 secs
    Lifetime current:
      Current bytes: 1841954
      Current packets: 7506
      SA add time: Fri Mar 15 05:58:37 2024
      SA last use time: Fri Mar 15 06:17:06 2024
```

## show stun client translations detail

```text
Current System Time: Fri Mar 15 06:17:05 2024
```

## show stun server bindings detail

```text
Current System Time: Fri Mar 15 06:17:05 2024
Transaction ID 000000010affff0200000000
Public Address: 172.16.2.0:4500
Number of Attributes: 3
Timeout Interval: 0:00:40
Timeout: 0:00:23
Attribute Type   Length Value           
---------------- ------ ----------------
PATH_GROUP            3 ATT             
VTEP_IP               4 10.255.255.2    
WAN_ID                4 1               

Transaction ID 000000010affff0700000000
Public Address: 172.16.2.2:4500
Number of Attributes: 3
Timeout Interval: 0:00:40
Timeout: 0:00:36
Attribute Type   Length Value           
---------------- ------ ----------------
PATH_GROUP            3 ATT             
VTEP_IP               4 10.255.255.7    
WAN_ID                4 1               

Transaction ID 000000020affff0900000000
Public Address: 172.16.2.7:4500
Number of Attributes: 3
Timeout Interval: 0:00:40
Timeout: 0:00:37
Attribute Type   Length Value           
---------------- ------ ----------------
PATH_GROUP            3 ATT             
VTEP_IP               4 10.255.255.9    
WAN_ID                4 2               

```

## show path-selection paths detail

```text
Peer: 10.255.255.2, Path group ATT
Path name: path10, dynamic, Label: 10
Source: 172.16.2.5, Port: 4500, WAN ID: 6
Destination: 172.16.2.0, Port: 4500, WAN ID: 1
Local interface: Ethernet1/4
Route state: IPsec established
Traffic class 0: active (16:58:08)
MTU: 8914

Peer: 10.255.255.7, Path group ATT
Path name: path6, dynamic, Label: 6
Source: 172.16.2.5, Port: 4500, WAN ID: 6
Destination: 172.16.2.2, Port: 4500, WAN ID: 1
Local interface: Ethernet1/4
Route state: IPsec established
Traffic class 0: active (13:30:10)
MTU: 8914

Peer: 10.255.255.9, Path group ATT
Path name: path5, dynamic, Label: 5
Source: 172.16.2.5, Port: 4500, WAN ID: 6
Destination: 172.16.2.7, Port: 4500, WAN ID: 2
Local interface: Ethernet1/4
Route state: IPsec established
Traffic class 0: active (16:58:05)
MTU: 1424

```

## show bgp neighbors

```text
BGP neighbor is 10.255.255.2, remote AS 65000, internal link
  BGP version 4, remote router ID 10.255.255.2, VRF default
  Inherits configuration from and member of peer-group autovpnEdges
  Last read 00:00:07, last write 00:00:13
  Hold time is 180, keepalive interval is 60 seconds
  Configured hold time is 180, keepalive interval is 60 seconds
  Effective minimum hold time is 3 seconds
  Send failure hold time is 0 seconds
  Hold timer is active, time left: 00:02:53
  Keepalive timer is active, time left: 00:00:37
  Connect timer is inactive
  Idle-restart timer is inactive
  BGP state is Established, up for 16:44:22
  Number of transitions to established: 1
  Last state was OpenConfirm
  Last event was RecvUpdate
  Types of communities advertised: extended
  Enhanced route refresh stale path removal disabled
  Outbound enhanced route refresh enabled
  Neighbor is a route reflector client
  Neighbor is using global cluster ID 10.255.255.3
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
      Received 16:44:21
      Number of stale paths removed after graceful restart: 0
      Number of paths received before End-of-RIB: 5
    L2VPN EVPN End-of-RIB received: Yes
      Received 16:44:21
      Number of stale paths removed after graceful restart: 0
      Number of paths received before End-of-RIB: 25
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
    Updates:                        72        73
    Keepalives:                   1172      1167
    Enhanced Route Refresh:          0         0
    Begin of Route Refresh:          0         0
    End of Route Refresh:            0         0
    Total messages:               1245      1241
  Prefix Statistics:
                                   Sent      Rcvd     Best Paths     Best ECMP Paths
    IPv4 Unicast:                     0         0              0                   0
    IPv4 Dps:                         5         5              5                   2
    IPv6 Unicast:                     0         0              0                   0
    EVPN:                            25        29             27                   4
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
Local AS is 65000, local router ID 10.255.255.3
TTL is 255
Local TCP address is 10.255.255.3, local port is 179
Remote TCP address is 10.255.255.2, remote port is 38611
Local next hop for next hop self:
  Dps: 10.255.255.3
  L2VPN EVPN: 10.255.255.3
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
    Round-trip Time (rtt/rtvar): 3.5ms/1.5ms
    Delayed Ack Timeout (ato): 40.0ms
    Congestion Window (cwnd): 10
    TCP Throughput: 33.13 Mbps
    Advertised Recv Window (rcv_space): 14600

BGP neighbor is 10.255.255.7, remote AS 65000, internal link
  BGP version 4, remote router ID 10.255.255.7, VRF default
  Inherits configuration from and member of peer-group autovpnEdges
  Last read 00:00:30, last write 00:00:42
  Hold time is 180, keepalive interval is 60 seconds
  Configured hold time is 180, keepalive interval is 60 seconds
  Effective minimum hold time is 3 seconds
  Send failure hold time is 0 seconds
  Hold timer is active, time left: 00:02:30
  Keepalive timer is active, time left: 00:00:08
  Connect timer is inactive
  Idle-restart timer is inactive
  BGP state is Established, up for 13:30:34
  Number of transitions to established: 1
  Last state was OpenConfirm
  Last event was RecvUpdate
  Types of communities advertised: extended
  Enhanced route refresh stale path removal disabled
  Outbound enhanced route refresh enabled
  Neighbor is a route reflector client
  Neighbor is using global cluster ID 10.255.255.3
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
      Received 13:30:33
      Number of stale paths removed after graceful restart: 0
      Number of paths received before End-of-RIB: 2
    L2VPN EVPN End-of-RIB received: Yes
      Received 13:30:33
      Number of stale paths removed after graceful restart: 0
      Number of paths received before End-of-RIB: 3
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
    Updates:                        43         8
    Keepalives:                    953       953
    Enhanced Route Refresh:          0         0
    Begin of Route Refresh:          0         0
    End of Route Refresh:            0         0
    Total messages:                997       962
  Prefix Statistics:
                                   Sent      Rcvd     Best Paths     Best ECMP Paths
    IPv4 Unicast:                     0         0              0                   0
    IPv4 Dps:                         8         2              2                   1
    IPv6 Unicast:                     0         0              0                   0
    EVPN:                            50         3              3                   0
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
Local AS is 65000, local router ID 10.255.255.3
TTL is 255
Local TCP address is 10.255.255.3, local port is 179
Remote TCP address is 10.255.255.7, remote port is 33951
Local next hop for next hop self:
  Dps: 10.255.255.3
  L2VPN EVPN: 10.255.255.3
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
    Round-trip Time (rtt/rtvar): 3.6ms/0.9ms
    Delayed Ack Timeout (ato): 40.0ms
    Congestion Window (cwnd): 10
    TCP Throughput: 32.04 Mbps
    Recv Round-trip Time (rcv_rtt): 4.0ms
    Advertised Recv Window (rcv_space): 14600

BGP neighbor is 10.255.255.9, remote AS 65000, internal link
  BGP version 4, remote router ID 10.255.255.9, VRF default
  Inherits configuration from and member of peer-group autovpnEdges
  Last read 00:00:44, last write 00:00:06
  Hold time is 180, keepalive interval is 60 seconds
  Configured hold time is 180, keepalive interval is 60 seconds
  Effective minimum hold time is 3 seconds
  Send failure hold time is 0 seconds
  Hold timer is active, time left: 00:02:16
  Keepalive timer is active, time left: 00:00:36
  Connect timer is inactive
  Idle-restart timer is inactive
  BGP state is Established, up for 16:44:22
  Number of transitions to established: 1
  Last state was OpenConfirm
  Last event was RecvUpdate
  Types of communities advertised: extended
  Enhanced route refresh stale path removal disabled
  Outbound enhanced route refresh enabled
  Neighbor is a route reflector client
  Neighbor is using global cluster ID 10.255.255.3
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
      Received 16:44:21
      Number of stale paths removed after graceful restart: 0
      Number of paths received before End-of-RIB: 2
    L2VPN EVPN End-of-RIB received: Yes
      Received 16:44:21
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
    Updates:                       131        11
    Keepalives:                   1173      1182
    Enhanced Route Refresh:          0         0
    Begin of Route Refresh:          0         0
    End of Route Refresh:            0         0
    Total messages:               1305      1194
  Prefix Statistics:
                                   Sent      Rcvd     Best Paths     Best ECMP Paths
    IPv4 Unicast:                     0         0              0                   0
    IPv4 Dps:                         8         2              2                   1
    IPv6 Unicast:                     0         0              0                   0
    EVPN:                            48         3              3                   2
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
Local AS is 65000, local router ID 10.255.255.3
TTL is 255
Local TCP address is 10.255.255.3, local port is 179
Remote TCP address is 10.255.255.9, remote port is 46465
Local next hop for next hop self:
  Dps: 10.255.255.3
  L2VPN EVPN: 10.255.255.3
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
    Round-trip Time (rtt/rtvar): 4.4ms/0.8ms
    Delayed Ack Timeout (ato): 40.0ms
    Congestion Window (cwnd): 10
    TCP Throughput: 25.15 Mbps
    Advertised Recv Window (rcv_space): 14600

```

## show bgp path-selection detail

```text
BGP routing table information for VRF default
Router identifier 10.255.255.3, local AS number 65000
Bgp routing table entry for ipv4Dps VTEP 10.255.255.7/32
 Paths: 2 available
  Local (Received from a RR-client)
    :: from 10.255.255.2 (10.255.255.2)
      Origin IGP, metric -, localpref 100, weight 0, received 13:30:39 ago, valid, internal
      Tunnel encapsulation attribute: Dynamic path selection
        Endpoint: 172.16.2.2, Path group name: ATT, WAN ID: 1, UDP port: 4500
  Local (Received from a RR-client)
    :: from 10.255.255.7 (10.255.255.7)
      Origin IGP, metric -, localpref 100, weight 0, received 13:30:34 ago, valid, internal
      Tunnel encapsulation attribute: Dynamic path selection
        Endpoint: 172.16.2.2, Path group name: ATT, WAN ID: 1, UDP port: 4500
Bgp routing table entry for ipv4Dps VTEP 10.255.255.9/32
 Paths: 2 available
  Local (Received from a RR-client)
    :: from 10.255.255.2 (10.255.255.2)
      Origin IGP, metric -, localpref 100, weight 0, received 16:44:23 ago, valid, internal
      Tunnel encapsulation attribute: Dynamic path selection
        Endpoint: 172.16.2.7, Path group name: ATT, WAN ID: 2, UDP port: 4500
  Local (Received from a RR-client)
    :: from 10.255.255.9 (10.255.255.9)
      Origin IGP, metric -, localpref 100, weight 0, received 16:44:23 ago, valid, internal
      Tunnel encapsulation attribute: Dynamic path selection
        Endpoint: 172.16.2.7, Path group name: ATT, WAN ID: 2, UDP port: 4500
Bgp routing table entry for ipv4Ipsec VTEP 10.255.255.2/32
 Paths: 1 available
  Local (Received from a RR-client)
    :: from 10.255.255.2 (10.255.255.2)
      Origin IGP, metric -, localpref 100, weight 0, received 16:44:23 ago, valid, internal
      Tunnel encapsulation attribute: IP security
        Initial contact: false, Rekey counter: 0, Nonce length: 32
        DH group: 14, DH key length: 256
        Encryption algo: aes256, Authentication algo: sha256
Bgp routing table entry for ipv4Ipsec VTEP 10.255.255.3/32
 Paths: 1 available
  Local
    - from - (0.0.0.0)
      Origin IGP, metric -, localpref -, weight 0, received 16:44:25 ago, valid, local
      Tunnel encapsulation attribute: IP security
        Initial contact: false, Rekey counter: 0, Nonce length: 32
        DH group: 14, DH key length: 256
        Encryption algo: aes256, Authentication algo: sha256
Bgp routing table entry for ipv4Ipsec VTEP 10.255.255.7/32
 Paths: 2 available
  Local (Received from a RR-client)
    :: from 10.255.255.7 (10.255.255.7)
      Origin IGP, metric -, localpref 100, weight 0, received 01:31:22 ago, valid, internal
      Tunnel encapsulation attribute: IP security
        Initial contact: false, Rekey counter: 2, Nonce length: 32
        DH group: 14, DH key length: 256
        Encryption algo: aes256, Authentication algo: sha256
  Local (Received from a RR-client)
    :: from 10.255.255.2 (10.255.255.2)
      Origin IGP, metric -, localpref 100, weight 0, received 01:31:22 ago, valid, internal
      Tunnel encapsulation attribute: IP security
        Initial contact: false, Rekey counter: 2, Nonce length: 32
        DH group: 14, DH key length: 256
        Encryption algo: aes256, Authentication algo: sha256
Bgp routing table entry for ipv4Ipsec VTEP 10.255.255.9/32
 Paths: 2 available
  Local (Received from a RR-client)
    :: from 10.255.255.9 (10.255.255.9)
      Origin IGP, metric -, localpref 100, weight 0, received 01:32:41 ago, valid, internal
      Tunnel encapsulation attribute: IP security
        Initial contact: false, Rekey counter: 2, Nonce length: 32
        DH group: 14, DH key length: 256
        Encryption algo: aes256, Authentication algo: sha256
  Local (Received from a RR-client)
    :: from 10.255.255.2 (10.255.255.2)
      Origin IGP, metric -, localpref 100, weight 0, received 01:32:41 ago, valid, internal
      Tunnel encapsulation attribute: IP security
        Initial contact: false, Rekey counter: 2, Nonce length: 32
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
>C    10.255.255.3/32 [0 pref/0 metric] updated 16:59:57 ago
         via Loopback0, directly connected
>C    172.16.2.4/31 [0 pref/0 metric] updated 16:58:55 ago
         via Ethernet1/4, directly connected
>C    172.16.3.2/31 [0 pref/0 metric] updated 16:58:55 ago
         via Ethernet1/3, directly connected
>C    172.28.128.0/20 [0 pref/0 metric] updated 16:59:27 ago
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
>S    10.80.0.0/12 [1 pref/0 metric] updated 16:59:27 ago
         via 172.28.128.1 [0 pref/0 metric] type ipv4
            via 172.28.128.1, Management1/1
>S    10.224.0.0/12 [1 pref/0 metric] updated 16:59:27 ago
         via 172.28.128.1 [0 pref/0 metric] type ipv4
            via 172.28.128.1, Management1/1
>S    10.240.0.0/12 [1 pref/0 metric] updated 16:59:27 ago
         via 172.28.128.1 [0 pref/0 metric] type ipv4
            via 172.28.128.1, Management1/1
>S    172.16.0.0/12 [1 pref/0 metric] updated 16:59:27 ago
         via 172.28.128.1 [0 pref/0 metric] type ipv4
            via 172.28.128.1, Management1/1
>S    172.16.2.0/24 [1 pref/0 metric] updated 16:58:55 ago
         via 172.16.2.4 [0 pref/0 metric] type ipv4
            via 172.16.2.4, Ethernet1/4
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
>P    0.0.0.0/8 [1 pref/0 metric] updated 16:59:56 ago
         via Null0, directly connected [NF]
>P    10.255.255.2/32 [1 pref/0 metric] updated 16:58:52 ago
         via 10.255.255.2, Dps1
>P    10.255.255.4/32 [1 pref/0 metric] updated 16:58:56 ago
         via 10.255.255.4, Dps1
>P    10.255.255.7/32 [1 pref/0 metric] updated 13:31:36 ago
         via 10.255.255.7, Dps1
>P    10.255.255.9/32 [1 pref/0 metric] updated 16:58:45 ago
         via 10.255.255.9, Dps1
>P    127.0.0.0/8 [1 pref/0 metric] updated 16:59:56 ago
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
>P    ::/96 [1 pref/0 metric] updated 16:58:58 ago
         via Null0, directly connected [NF]
>P    ::ffff:127.0.0.0/104 [1 pref/0 metric] updated 16:58:58 ago
         via :: [1 pref/1 metric] type ipv6
            via , directly connected
>P    fe80::/10 [1 pref/0 metric] updated 16:58:58 ago
```

