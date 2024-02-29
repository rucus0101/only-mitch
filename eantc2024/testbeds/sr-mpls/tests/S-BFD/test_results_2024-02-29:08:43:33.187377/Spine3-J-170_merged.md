# Test results for Spine3-J-170

## show version

```text
Arista DCS-7280SR-48C6-F
Hardware version: 10.01
Serial number: JPE17131942
Hardware MAC address: 2899.3a06.b4e1
System MAC address: 2899.3a06.b4e1

Software image version: 4.31.2F
Architecture: i686
Internal build version: 4.31.2F-35442146.4312F
Internal build ID: 635a071a-386e-447f-942c-bcc34d9ffd3c
Image format version: 3.0
Image optimization: Sand-4GB

Uptime: 2 days, 17 hours and 46 minutes
Total memory: 8051592 kB
Free memory: 5813148 kB

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
Interface       IP Address           Status        Protocol       MTU   Owner  
--------------- -------------------- ------------- ----------- -------- -------
Ethernet1       20.170.171.170/24    up            up            1500          
Ethernet3       20.47.170.170/24     down          down          1500          
Ethernet25      20.19.170.170/24     up            up            1500          
Ethernet43      20.32.170.170/24     up            up            1500          
Ethernet45      20.57.170.170/24     up            up            1500          
Ethernet48      20.170.254.170/24    down          down          1500          
Ethernet49/1    20.170.179.170/24    up            up            1500          
Ethernet49/2    20.170.212.170/24    up            up            1500          
Ethernet50/1    20.5.170.170/24      up            up            1500          
Ethernet51/1    20.155.170.170/24    up            up            1500          
Ethernet52/1    20.170.172.170/24    down          down          1500          
Ethernet53/1    20.24.170.170/24     up            up            1500          
Ethernet54/1    20.59.170.170/24     down          down          1500          
Loopback0       10.0.0.170/32        up            up           65535          
Management1     192.168.20.170/23    up            up            1500          

```

## show interfaces counters rates | nz

```text
Port      Name            Intvl  In Mbps      %  In Kpps Out Mbps      %
Et25      H3C_19           0:01     40.2   0.4%        5      0.1   0.0%
Et43      RIBBON_32        0:01      0.2   0.0%        0     40.2   0.4%
Et45      Nokia_57         0:01      0.1   0.0%        0      0.2   0.0%
Et49/1    Juniper_379      0:01      0.1   0.0%        0      0.0   0.0%
Et51/1    Cisco_355        0:01      0.0   0.0%        0      0.1   0.0%
Et53/1    H3C_24           0:01      0.1   0.0%        0      0.0   0.0%
Ma1                        0:01      0.0   0.0%        0      0.1   0.0%

Port      Out Kpps
Et43             5
```

## show isis neighbors

```text
 
Instance  VRF      System Id        Type Interface          SNPA              State Hold time   Circuit Id          
IGP       default  h3c_19_CR16010E-F L2   Ethernet25         P2P               UP    24          01                  
IGP       default  h3c_24_S12500R-48C6D L2   Ethernet53/1       P2P               UP    24          01                  
IGP       default  Ribbon-32        L2   Ethernet43         P2P               UP    88          00                  
IGP       default  h55-8201-24H8FH  L2   Ethernet51/1       P2P               UP    21          00                  
IGP       default  juniper_379_MX304 L2   Ethernet49/1       P2P               UP    26          01                  
IGP       default  JNPR-312-ACX7100-48L L2   Ethernet49/2       P2P               UP    21          01                  
IGP       default  0000.0010.0005   L2   Ethernet50/1       P2P               UP    26          01                  
IGP       default  NOKIA-SR2-57     L2   Ethernet45         P2P               UP    26          00                  
IGP       default  PE31-J2-171      L2   Ethernet1          P2P               UP    29          50                  
```

## show isis database detail

```text
Legend:
H - hostname conflict
U - node unreachable

IS-IS Instance: IGP VRF: default
  IS-IS Level 2 Link State Database
    LSPID                   Seq Num  Cksum  Life Length IS  Received LSPID        Flags
    h3c_19_CR16010E-F.00-00      1448  61530   980    411 L2  0000.0000.0019.00-00  <>
      Remaining lifetime received: 1199 s Modified to: 1200 s
      NLPID: 0xCC(IPv4)
      Hostname: h3c_19_CR16010E-F
      Area addresses: 49
      Interface address: 10.0.0.19
      Interface address: 20.19.149.19
      Interface address: 20.19.170.19
      IS Neighbor          : h49-N540-24Q8L2DD.00 Metric: 10
        IPv4 Neighbor Address: 20.19.149.149
        IPv4 Interface Address: 20.19.149.19
        Adj-sid: 1145 flags: [L V] weight: 0x0
      IS Neighbor          : Spine3-J-170.00     Metric: 10
        IPv4 Neighbor Address: 20.19.170.170
        IPv4 Interface Address: 20.19.170.19
        Adj-sid: 1144 flags: [L V] weight: 0x0
      Reachability         : 10.0.0.19/32 Metric: 0 Type: 1 Up
        SR Prefix-SID: 19 Flags: [N] Algorithm: 0
      Reachability         : 20.19.149.0/24 Metric: 10 Type: 1 Up
      Reachability         : 20.19.170.0/24 Metric: 10 Type: 1 Up
      Reachability         : 31.9.1.0/24 Metric: 0 Type: 1 Up
      Reachability         : 192.168.0.0/19 Metric: 0 Type: 1 Up
      Router Capabilities: Router Id: 10.0.0.19 Flags: []
        Maximum SID depth:
          Base MPLS imposition (MSD type 1):  13
        SR Capability: Flags: [I]
          SRGB Base: 20000 Range: 2000
    h3c_24_S12500R-48C6D.00-00       893  10643  1013    433 L2  0000.0000.0024.00-00  <>
      Remaining lifetime received: 1199 s Modified to: 1200 s
      NLPID: 0xCC(IPv4)
      Hostname: h3c_24_S12500R-48C6D
      Area addresses: 49
      Interface address: 10.0.0.24
      Interface address: 20.24.149.24
      Interface address: 20.24.170.24
      Interface address: 20.24.238.24
      IS Neighbor          : h49-N540-24Q8L2DD.00 Metric: 10
        IPv4 Neighbor Address: 20.24.149.149
        IPv4 Interface Address: 20.24.149.24
        Adj-sid: 56121 flags: [L V] weight: 0x0
      IS Neighbor          : Spine3-J-170.00     Metric: 10
        IPv4 Neighbor Address: 20.24.170.170
        IPv4 Interface Address: 20.24.170.24
        Adj-sid: 56120 flags: [L V] weight: 0x0
      Reachability         : 10.0.0.24/32 Metric: 0 Type: 1 Up
        SR Prefix-SID: 24 Flags: [N P] Algorithm: 0
      Reachability         : 20.24.149.0/24 Metric: 10 Type: 1 Up
      Reachability         : 20.24.170.0/24 Metric: 10 Type: 1 Up
      Reachability         : 20.24.238.0/24 Metric: 10 Type: 1 Up
      Router Capabilities: Router Id: 10.0.0.24 Flags: []
        SR Local Block:
          SRLB Base: 15000 Range: 1000
        Maximum SID depth:
          Base MPLS imposition (MSD type 1):  10
        SR Capability: Flags: [I]
          SRGB Base: 20000 Range: 2000
    Ribbon-32.00-00              83  47973   404     79 L2  0000.0000.0032.00-00  <>
      NLPID: 0xCC(IPv4)
      Area addresses: 49.0001
      Router Capabilities: Router Id: 10.0.0.32 Flags: []
        SR Local Block:
          SRLB Base: 16 Range: 15344
        Maximum SID depth:
          Base MPLS imposition (MSD type 1):  10
        SR Capability: Flags: [I]
          SRGB Base: 20000 Range: 2000
      Unsupported TLV: Type: 14 Length: 2
    Ribbon-32.00-03              76  64252  1060     38 L2  0000.0000.0032.00-03  <>
      Hostname: Ribbon-32
    Ribbon-32.00-04              85  46189   717    285 L2  0000.0000.0032.00-04  <>
      Interface address: 10.0.0.32
      Interface address: 20.32.149.32
      Interface address: 20.32.170.32
      IS Neighbor          : h49-N540-24Q8L2DD.00 Metric: 10
        IPv4 Neighbor Address: 20.32.149.149
        IPv4 Interface Address: 20.32.149.32
        Adj-sid: 756641 flags: [L V] weight: 0x0
        Adj-sid: 756642 flags: [L V B] weight: 0x0
      IS Neighbor          : Spine3-J-170.00     Metric: 10
        IPv4 Neighbor Address: 20.32.170.170
        IPv4 Interface Address: 20.32.170.32
        Adj-sid: 756643 flags: [L V] weight: 0x0
        Adj-sid: 756644 flags: [L V B] weight: 0x0
      Reachability         : 10.0.0.32/32 Metric: 0 Type: 1 Up
        SR Prefix-SID: 32 Flags: [N] Algorithm: 0
      Reachability         : 20.32.149.0/24 Metric: 10 Type: 1 Up
      Reachability         : 20.32.170.0/24 Metric: 10 Type: 1 Up
    h43-9901.00-00              343  10807  1178    186 L2  0000.0000.0343.00-00  <>
      Remaining lifetime received: 1199 s Modified to: 1200 s
      NLPID: 0xCC(IPv4)
      Hostname: h43-9901
      Area addresses: 49
      Interface address: 10.0.1.43
      IS Neighbor          : h49-N540-24Q8L2DD.00 Metric: 10
        IPv4 Neighbor Address: 20.143.149.149
        IPv4 Interface Address: 20.143.149.143
        Adj-sid: 24001 flags: [L V] weight: 0x0
      Reachability         : 10.0.1.43/32 Metric: 0 Type: 1 Up
        SR Prefix-SID: 343 Flags: [N] Algorithm: 0
      Reachability         : 20.143.149.0/24 Metric: 10 Type: 1 Up
      Router Capabilities: Router Id: 10.0.1.43 Flags: []
        SR Local Block:
          SRLB Base: 15000 Range: 1000
        Maximum SID depth:
          Base MPLS imposition (MSD type 1):  10
        SR Capability: Flags: [I]
          SRGB Base: 20000 Range: 2000
        Algorithms:  0, 1
      Unsupported TLV: Type: 14 Length: 2
    h49-N540-24Q8L2DD.00-00       441    598   925   1289 L2  0000.0000.0349.00-00  <>
      Remaining lifetime received: 1199 s Modified to: 1200 s
      NLPID: 0xCC(IPv4)
      Hostname: h49-N540-24Q8L2DD
      Area addresses: 49
      Interface address: 10.0.1.49
      IS Neighbor          : h3c_19_CR16010E-F.00 Metric: 10
        IPv4 Neighbor Address: 20.19.149.19
        IPv4 Interface Address: 20.19.149.149
        Adj-sid: 24015 flags: [L V] weight: 0x0
      IS Neighbor          : h3c_24_S12500R-48C6D.00 Metric: 10
        IPv4 Neighbor Address: 20.24.149.24
        IPv4 Interface Address: 20.24.149.149
        Adj-sid: 24005 flags: [L V] weight: 0x0
      IS Neighbor          : 0000.0010.0005.00   Metric: 10
        IPv4 Neighbor Address: 20.5.149.5
        IPv4 Interface Address: 20.5.149.149
        Adj-sid: 24003 flags: [L V] weight: 0x0
      IS Neighbor          : PE31-J2-171.00      Metric: 10
        IPv4 Neighbor Address: 20.149.171.171
        IPv4 Interface Address: 20.149.171.149
        Adj-sid: 24009 flags: [L V] weight: 0x0
      IS Neighbor          : h43-9901.00         Metric: 10
        IPv4 Neighbor Address: 20.143.149.143
        IPv4 Interface Address: 20.143.149.149
        Adj-sid: 24011 flags: [L V] weight: 0x0
      IS Neighbor          : h55-8201-24H8FH.00  Metric: 10
        IPv4 Neighbor Address: 20.149.155.155
        IPv4 Interface Address: 20.149.155.149
        Adj-sid: 24000 flags: [L V B] weight: 0x0
        Adj-sid: 24001 flags: [L V] weight: 0x0
      IS Neighbor          : Ribbon-32.00        Metric: 10
        IPv4 Neighbor Address: 20.32.149.32
        IPv4 Interface Address: 20.32.149.149
        Adj-sid: 24007 flags: [L V] weight: 0x0
      IS Neighbor          : juniper_379_MX304.00 Metric: 10
        IPv4 Neighbor Address: 20.149.179.179
        IPv4 Interface Address: 20.149.179.149
        Adj-sid: 24012 flags: [L V B] weight: 0x0
        Adj-sid: 24013 flags: [L V] weight: 0x0
      IS Neighbor          : NOKIA-SR2-57.00     Metric: 10
        IPv4 Neighbor Address: 20.57.149.57
        IPv4 Interface Address: 20.57.149.149
        Adj-sid: 24018 flags: [L V B] weight: 0x0
        Adj-sid: 24019 flags: [L V] weight: 0x0
      Reachability         : 10.0.1.49/32 Metric: 0 Type: 1 Up
        SR Prefix-SID: 349 Flags: [N] Algorithm: 0
        SR Prefix-SID: 1449 Flags: [N] Algorithm: 129
        SR Prefix-SID: 1549 Flags: [N] Algorithm: 130
        SR Prefix-SID: 1649 Flags: [N] Algorithm: 131
        SR Prefix-SID: 1749 Flags: [N] Algorithm: 132
        SR Prefix-SID: 449 Flags: [N] Algorithm: 140
        SR Prefix-SID: 549 Flags: [N] Algorithm: 141
        SR Prefix-SID: 649 Flags: [N] Algorithm: 142
      Reachability         : 20.5.149.0/24 Metric: 10 Type: 1 Up
      Reachability         : 20.19.149.0/24 Metric: 10 Type: 1 Up
      Reachability         : 20.24.149.0/24 Metric: 10 Type: 1 Up
      Reachability         : 20.32.149.0/24 Metric: 10 Type: 1 Up
      Reachability         : 20.57.149.0/24 Metric: 10 Type: 1 Up
      Reachability         : 20.111.149.0/24 Metric: 10 Type: 1 Up
      Reachability         : 20.143.149.0/24 Metric: 10 Type: 1 Up
      Reachability         : 20.149.155.0/24 Metric: 10 Type: 1 Up
      Reachability         : 20.149.171.0/24 Metric: 10 Type: 1 Up
      Reachability         : 20.149.179.0/24 Metric: 10 Type: 1 Up
      Router Capabilities: Router Id: 10.0.1.49 Flags: []
        SR Local Block:
          SRLB Base: 15000 Range: 1000
        Maximum SID depth:
          Base MPLS imposition (MSD type 1):  12
        SR Capability: Flags: [I]
          SRGB Base: 20000 Range: 2000
        Algorithms:  0, 1, 128, 129, 130, 131, 132, 140, 141, 142
        Flex Algo: Algorithm: 129 Metric: TE Metric (2) Calc: SPF (0) Prio: 255
        Flex Algo: Algorithm: 130 Metric: IGP Metric (0) Calc: SPF (0) Prio: 255
          Exclude admin groups: 1
        Flex Algo: Algorithm: 131 Metric: IGP Metric (0) Calc: SPF (0) Prio: 255
          Exclude admin groups: 127
        Flex Algo: Algorithm: 132 Metric: IGP Metric (0) Calc: SPF (0) Prio: 255
          Exclude admin groups: 255
        Flex Algo: Algorithm: 140 Metric: IGP Metric (0) Calc: SPF (0) Prio: 255
        Flex Algo: Algorithm: 141 Metric: IGP Metric (0) Calc: SPF (0) Prio: 255
        Flex Algo: Algorithm: 142 Metric: IGP Metric (0) Calc: SPF (0) Prio: 255
      Unsupported TLV: Type: 14 Length: 2
    h55-8201-24H8FH.00-00       352  14968  1105    560 L2  0000.0000.0355.00-00  <>
      NLPID: 0xCC(IPv4)
      Hostname: h55-8201-24H8FH
      Area addresses: 49
      Interface address: 10.0.1.55
      IS Neighbor          : h49-N540-24Q8L2DD.00 Metric: 10
        IPv4 Neighbor Address: 20.149.155.149
        IPv4 Interface Address: 20.149.155.155
        Adj-sid: 24001 flags: [L V] weight: 0x0
      IS Neighbor          : Spine3-J-170.00     Metric: 10
        IPv4 Neighbor Address: 20.155.170.170
        IPv4 Interface Address: 20.155.170.155
        Adj-sid: 24007 flags: [L V] weight: 0x0
      Reachability         : 10.0.1.55/32 Metric: 0 Type: 1 Up
        SR Prefix-SID: 355 Flags: [N] Algorithm: 0
        SR Prefix-SID: 1355 Flags: [N] Algorithm: 128
        SR Prefix-SID: 1455 Flags: [N] Algorithm: 129
        SR Prefix-SID: 1555 Flags: [N] Algorithm: 130
        SR Prefix-SID: 1655 Flags: [N] Algorithm: 131
        SR Prefix-SID: 1755 Flags: [N] Algorithm: 132
        SR Prefix-SID: 455 Flags: [N] Algorithm: 140
        SR Prefix-SID: 555 Flags: [N] Algorithm: 141
        SR Prefix-SID: 655 Flags: [N] Algorithm: 142
      Reachability         : 20.32.155.0/24 Metric: 10 Type: 1 Up
      Reachability         : 20.57.155.0/24 Metric: 10 Type: 1 Up
      Reachability         : 20.149.155.0/24 Metric: 10 Type: 1 Up
      Reachability         : 20.155.170.0/24 Metric: 10 Type: 1 Up
      Reachability         : 209.209.209.209/32 Metric: 0 Type: 1 Up
        SR Prefix-SID: 209 Flags: [] Algorithm: 0
      Router Capabilities: Router Id: 10.0.1.55 Flags: []
        SR Local Block:
          SRLB Base: 15000 Range: 1000
        Maximum SID depth:
          Base MPLS imposition (MSD type 1):  7
        SR Capability: Flags: [I]
          SRGB Base: 20000 Range: 2000
        Algorithms:  0, 1, 128, 129, 130, 131, 132, 140, 141, 142
        Flex Algo: Algorithm: 128 Metric: Min Unidirectional Delay Metric (1) Calc: SPF (0) Prio: 10
        Flex Algo: Algorithm: 129 Metric: TE Metric (2) Calc: SPF (0) Prio: 10
        Flex Algo: Algorithm: 130 Metric: IGP Metric (0) Calc: SPF (0) Prio: 10
          Exclude admin groups: 1
        Flex Algo: Algorithm: 131 Metric: IGP Metric (0) Calc: SPF (0) Prio: 10
          Exclude admin groups: 127
        Flex Algo: Algorithm: 132 Metric: IGP Metric (0) Calc: SPF (0) Prio: 10
          Exclude admin groups: 255
        Flex Algo: Algorithm: 140 Metric: IGP Metric (0) Calc: SPF (0) Prio: 10
        Flex Algo: Algorithm: 141 Metric: IGP Metric (0) Calc: SPF (0) Prio: 10
        Flex Algo: Algorithm: 142 Metric: IGP Metric (0) Calc: SPF (0) Prio: 10
      Unsupported TLV: Type: 14 Length: 2
    juniper_379_MX304.00-00      1230  33978   733    323 L2  0000.0001.7900.00-00  <>
      Remaining lifetime received: 1198 s Modified to: 1200 s
      NLPID: 0xCC(IPv4) 0x8E(IPv6)
      Hostname: juniper_379_MX304
      Area addresses: 49.0001.00
      Interface address: 10.0.0.179
      Interface address: 209.209.209.209
      Interface address: 127.0.0.1
      IS Neighbor          : h49-N540-24Q8L2DD.00 Metric: 100
        IPv4 Neighbor Address: 20.149.179.149
        IPv4 Interface Address: 20.149.179.179
        Adj-sid: 23 flags: [L V B] weight: 0x0
      IS Neighbor          : Spine3-J-170.00     Metric: 10
        IPv4 Neighbor Address: 20.170.179.170
        IPv4 Interface Address: 20.170.179.179
        Adj-sid: 27 flags: [L V] weight: 0x0
      Reachability         : 30.155.179.0/24 Metric: 10 Type: 1 Up
      Reachability         : 10.0.0.179/32 Metric: 0 Type: 1 Up
        SR Prefix-SID: 379 Flags: [N] Algorithm: 0
        SR Prefix-SID: 1379 Flags: [N] Algorithm: 130
        SR Prefix-SID: 1279 Flags: [N] Algorithm: 129
        SR Prefix-SID: 1179 Flags: [N] Algorithm: 128
      Reachability         : 209.209.209.209/32 Metric: 0 Type: 1 Up
        SR Prefix-SID: 209 Flags: [] Algorithm: 0
      Reachability         : 127.0.0.1/32 Metric: 0 Type: 1 Up
      Reachability         : 20.149.179.0/24 Metric: 100 Type: 1 Up
      Reachability         : 20.170.179.0/24 Metric: 10 Type: 1 Up
      Router Capabilities: Router Id: 10.0.0.179 Flags: []
        Maximum SID depth:
          Base MPLS imposition (MSD type 1):  4
        SR Capability: Flags: [I V]
          SRGB Base: 20000 Range: 2000
        Algorithms:  0, 1, 128, 129, 130
      Unsupported TLV: Type: 14 Length: 2
    JNPR-312-ACX7100-48L.00-00       368    598  1128    178 L2  0000.0003.1200.00-00  <>
      Remaining lifetime received: 1198 s Modified to: 1200 s
      NLPID: 0xCC(IPv4) 0x8E(IPv6)
      Hostname: JNPR-312-ACX7100-48L
      Area addresses: 49.0001.00
      Interface address: 10.0.0.212
      IS Neighbor          : Spine3-J-170.00     Metric: 10
        IPv4 Neighbor Address: 20.170.212.170
        IPv4 Interface Address: 20.170.212.212
        Adj-sid: 17 flags: [L V B] weight: 0x0
      Reachability         : 10.0.0.212/32 Metric: 0 Type: 1 Up
        SR Prefix-SID: 212 Flags: [N P E] Algorithm: 0
      Reachability         : 20.170.212.0/24 Metric: 10 Type: 1 Up
      Router Capabilities: Router Id: 10.0.0.212 Flags: []
        Maximum SID depth:
          Base MPLS imposition (MSD type 1):  4
        SR Capability: Flags: [I V]
          SRGB Base: 20000 Range: 2000
        Algorithms:  0, 1
      Unsupported TLV: Type: 14 Length: 2
    0000.0010.0005.00-00        294  10679  1057    319 L2  0000.0010.0005.00-00  <>
      Remaining lifetime received: 1199 s Modified to: 1200 s
      NLPID: 0xCC(IPv4)
      Area addresses: 49.0000
      Interface address: 20.5.149.5
      IS Neighbor          : h49-N540-24Q8L2DD.00 Metric: 10
        IPv4 Neighbor Address: 20.5.149.149
        IPv4 Interface Address: 20.5.149.5
        Adj-sid: 16000 flags: [L V] weight: 0x0
      IS Neighbor          : Spine3-J-170.00     Metric: 10
        IPv4 Neighbor Address: 20.5.170.170
        IPv4 Interface Address: 20.5.170.5
        Adj-sid: 16001 flags: [L V] weight: 0x0
      Reachability         : 10.0.0.5/32 Metric: 0 Type: 1 Up
        SR Prefix-SID: 5 Flags: [N P] Algorithm: 0
      Reachability         : 20.5.149.0/24 Metric: 10 Type: 1 Up
      Reachability         : 20.5.170.0/24 Metric: 10 Type: 1 Up
      Reachability          : 2002::5/128 Metric: 0 Type: 1 Up
      Router Capabilities: Router Id: 10.0.0.5 Flags: []
        SR Capability: Flags: [I]
          SRGB Base: 20000 Range: 2000
        Algorithms:  0
    NOKIA-SR2-57.00-00        12677  41780  1146    348 L2  0100.0000.0057.00-00  <>
      NLPID: 0xCC(IPv4) 0x8E(IPv6)
      Hostname: NOKIA-SR2-57
      Area addresses: 49.0000.0000.0057.00
      Interface address: 10.0.0.57
      Interface address: 20.57.149.57
      Interface address: 20.57.170.57
      Interface address: 2002::57
      IS Neighbor          : h49-N540-24Q8L2DD.00 Metric: 10
        IPv4 Neighbor Address: 20.57.149.149
        IPv4 Interface Address: 20.57.149.57
        Adj-sid: 30149 flags: [L V B] weight: 0x0
      IS Neighbor          : Spine3-J-170.00     Metric: 10
        IPv4 Neighbor Address: 20.57.170.170
        IPv4 Interface Address: 20.57.170.57
        Adj-sid: 30170 flags: [L V B] weight: 0x0
      Reachability         : 10.0.0.57/32 Metric: 0 Type: 1 Up
        SR Prefix-SID: 57 Flags: [N P] Algorithm: 0
      Reachability         : 20.57.149.0/24 Metric: 10 Type: 1 Up
      Reachability         : 20.57.170.0/24 Metric: 10 Type: 1 Up
      Reachability          : 2002::57/128 Metric: 0 Type: 1 Up
        SR Prefix-SID: 157 Flags: [N P] Algorithm: 0
      Router Capabilities: Router Id: 10.0.0.57 Flags: []
        Maximum SID depth:
          Base MPLS imposition (MSD type 1):  12
        SR Capability: Flags: [I V]
          SRGB Base: 20000 Range: 2000
        Algorithms:  0
    Spine3-J-170.00-00          847  13870   471    570 L2  0100.0000.0170.00-00  <>
      LSP generation remaining wait time: 0 ms
      Time remaining until refresh: 171 s
      NLPID: 0xCC(IPv4)
      Hostname: Spine3-J-170
      Area addresses: 49.0000
      Interface address: 20.5.170.170
      Interface address: 20.32.170.170
      Interface address: 20.24.170.170
      Interface address: 20.170.212.170
      Interface address: 20.170.179.170
      Interface address: 20.19.170.170
      Interface address: 20.170.171.170
      Interface address: 20.57.170.170
      Interface address: 20.155.170.170
      Interface address: 10.0.0.170
      IS Neighbor          : 0000.0010.0005.00   Metric: 10
        IPv4 Neighbor Address: 20.5.170.5
        IPv4 Interface Address: 20.5.170.170
        Adj-sid: 362153 flags: [L V] weight: 0x0
      IS Neighbor          : juniper_379_MX304.00 Metric: 10
        IPv4 Neighbor Address: 20.170.179.179
        IPv4 Interface Address: 20.170.179.170
        Adj-sid: 362291 flags: [L V] weight: 0x0
      IS Neighbor          : h3c_24_S12500R-48C6D.00 Metric: 100
        IPv4 Neighbor Address: 20.24.170.24
        IPv4 Interface Address: 20.24.170.170
        Adj-sid: 362154 flags: [L V] weight: 0x0
      IS Neighbor          : JNPR-312-ACX7100-48L.00 Metric: 10
        IPv4 Neighbor Address: 20.170.212.212
        IPv4 Interface Address: 20.170.212.170
        Adj-sid: 362149 flags: [L V] weight: 0x0
      IS Neighbor          : NOKIA-SR2-57.00     Metric: 1
        IPv4 Neighbor Address: 20.57.170.57
        IPv4 Interface Address: 20.57.170.170
        Adj-sid: 362163 flags: [L V] weight: 0x0
      IS Neighbor          : h3c_19_CR16010E-F.00 Metric: 10
        IPv4 Neighbor Address: 20.19.170.19
        IPv4 Interface Address: 20.19.170.170
        Adj-sid: 362158 flags: [L V] weight: 0x0
      IS Neighbor          : h55-8201-24H8FH.00  Metric: 20
        IPv4 Neighbor Address: 20.155.170.155
        IPv4 Interface Address: 20.155.170.170
        Adj-sid: 362144 flags: [L V] weight: 0x0
      IS Neighbor          : Ribbon-32.00        Metric: 12
        IPv4 Neighbor Address: 20.32.170.32
        IPv4 Interface Address: 20.32.170.170
        Adj-sid: 362152 flags: [L V] weight: 0x0
      IS Neighbor          : PE31-J2-171.00      Metric: 10
        IPv4 Neighbor Address: 20.170.171.171
        IPv4 Interface Address: 20.170.171.170
        Adj-sid: 362156 flags: [L V] weight: 0x0
      Reachability         : 20.5.170.0/24 Metric: 10 Type: 1 Up
      Reachability         : 20.32.170.0/24 Metric: 12 Type: 1 Up
      Reachability         : 20.24.170.0/24 Metric: 100 Type: 1 Up
      Reachability         : 20.170.212.0/24 Metric: 10 Type: 1 Up
      Reachability         : 20.170.179.0/24 Metric: 10 Type: 1 Up
      Reachability         : 20.19.170.0/24 Metric: 10 Type: 1 Up
      Reachability         : 20.170.171.0/24 Metric: 10 Type: 1 Up
      Reachability         : 20.57.170.0/24 Metric: 1 Type: 1 Up
      Reachability         : 20.155.170.0/24 Metric: 20 Type: 1 Up
      Reachability         : 10.0.0.170/32 Metric: 0 Type: 1 Up
        SR Prefix-SID: 170 Flags: [N] Algorithm: 0
      Router Capabilities: Router Id: 10.0.0.170 Flags: []
        SR Local Block:
          SRLB Base: 965536 Range: 65536
        Area leader priority: 250 algorithm: 0
        Maximum SID depth:
          Base MPLS imposition (MSD type 1):  6
        SR Capability: Flags: [I]
          SRGB Base: 20000 Range: 2000
        Algorithms:  0, 128, 129, 130, 131
        Flex Algo: Algorithm: 131 Metric: IGP Metric (0) Calc: SPF (0) Prio: 237
          Exclude admin groups: 127
        Flex Algo: Algorithm: 130 Metric: IGP Metric (0) Calc: SPF (0) Prio: 237
        Flex Algo: Algorithm: 129 Metric: TE Metric (2) Calc: SPF (0) Prio: 237
        Flex Algo: Algorithm: 128 Metric: Min Unidirectional Delay Metric (1) Calc: SPF (0) Prio: 237
    PE31-J2-171.00-00           365  10524   494    323 L2  0100.0000.0171.00-00  <>
      Remaining lifetime received: 1199 s Modified to: 1200 s
      NLPID: 0xCC(IPv4)
      Hostname: PE31-J2-171
      Area addresses: 49.0000
      Interface address: 20.170.171.171
      Interface address: 20.149.171.171
      Interface address: 10.0.0.171
      IS Neighbor          : h49-N540-24Q8L2DD.00 Metric: 11
        IPv4 Neighbor Address: 20.149.171.149
        IPv4 Interface Address: 20.149.171.171
        Adj-sid: 362144 flags: [L V] weight: 0x0
      IS Neighbor          : Spine3-J-170.00     Metric: 30
        IPv4 Neighbor Address: 20.170.171.170
        IPv4 Interface Address: 20.170.171.171
        Adj-sid: 362145 flags: [L V] weight: 0x0
      Reachability         : 10.0.0.171/32 Metric: 0 Type: 1 Up
        SR Prefix-SID: 171 Flags: [N] Algorithm: 0
        SR Prefix-SID: 1171 Flags: [N] Algorithm: 128
        SR Prefix-SID: 1271 Flags: [N] Algorithm: 129
        SR Prefix-SID: 1371 Flags: [N] Algorithm: 130
        SR Prefix-SID: 1471 Flags: [N] Algorithm: 131
      Reachability         : 20.170.171.0/24 Metric: 30 Type: 1 Up
      Reachability         : 20.149.171.0/24 Metric: 11 Type: 1 Up
      Router Capabilities: Router Id: 10.0.0.171 Flags: []
        SR Local Block:
          SRLB Base: 965536 Range: 65536
        Area leader priority: 250 algorithm: 0
        Maximum SID depth:
          Base MPLS imposition (MSD type 1):  12
        SR Capability: Flags: [I]
          SRGB Base: 20000 Range: 2000
        Algorithms:  0, 128, 129, 130, 131
        Flex Algo: Algorithm: 131 Metric: IGP Metric (0) Calc: SPF (0) Prio: 237
          Exclude admin groups: 127
        Flex Algo: Algorithm: 130 Metric: IGP Metric (0) Calc: SPF (0) Prio: 237
        Flex Algo: Algorithm: 129 Metric: TE Metric (2) Calc: SPF (0) Prio: 237
        Flex Algo: Algorithm: 128 Metric: Min Unidirectional Delay Metric (1) Calc: SPF (0) Prio: 237
```

## show isis database traffic-engineering

```text
Legend:
H - hostname conflict
U - node unreachable

IS-IS Instance: IGP VRF: default
  IS-IS Level 2 Link State Database
    LSPID                   Seq Num  Cksum  Life Length IS  Received LSPID        Flags
    h3c_19_CR16010E-F.00-00      1448  61530   980    411 L2  0000.0000.0019.00-00  <>
      Remaining lifetime received: 1199 s Modified to: 1200 s
      NLPID: 0xCC(IPv4)
      Hostname: h3c_19_CR16010E-F
      TE IPv4 router ID: 10.0.0.19
      Area addresses: 49
      Interface address: 10.0.0.19
      Interface address: 20.19.149.19
      Interface address: 20.19.170.19
      IS Neighbor          : h49-N540-24Q8L2DD.00 Metric: 10
        IPv4 Neighbor Address: 20.19.149.149
        IPv4 Interface Address: 20.19.149.19
        Adj-sid: 1145 flags: [L V] weight: 0x0
        TE default metric: 100
        Maximum link BW: 0.00 bps
        Maximum reservable link BW: 0.00 bps
        Unreserved BW:
            TE class 0: 0.00 bps	TE class 1: 0.00 bps	TE class 2: 0.00 bps
            TE class 3: 0.00 bps	TE class 4: 0.00 bps	TE class 5: 0.00 bps
            TE class 6: 0.00 bps	TE class 7: 0.00 bps
      IS Neighbor          : Spine3-J-170.00     Metric: 10
        IPv4 Neighbor Address: 20.19.170.170
        IPv4 Interface Address: 20.19.170.19
        Adj-sid: 1144 flags: [L V] weight: 0x0
        TE default metric: 10
        Maximum link BW: 0.00 bps
        Maximum reservable link BW: 0.00 bps
        Unreserved BW:
            TE class 0: 0.00 bps	TE class 1: 0.00 bps	TE class 2: 0.00 bps
            TE class 3: 0.00 bps	TE class 4: 0.00 bps	TE class 5: 0.00 bps
            TE class 6: 0.00 bps	TE class 7: 0.00 bps
      Reachability         : 10.0.0.19/32 Metric: 0 Type: 1 Up
        SR Prefix-SID: 19 Flags: [N] Algorithm: 0
      Reachability         : 20.19.149.0/24 Metric: 10 Type: 1 Up
      Reachability         : 20.19.170.0/24 Metric: 10 Type: 1 Up
      Reachability         : 31.9.1.0/24 Metric: 0 Type: 1 Up
      Reachability         : 192.168.0.0/19 Metric: 0 Type: 1 Up
      Router Capabilities: Router Id: 10.0.0.19 Flags: []
        Maximum SID depth:
          Base MPLS imposition (MSD type 1):  13
        SR Capability: Flags: [I]
          SRGB Base: 20000 Range: 2000
    h3c_24_S12500R-48C6D.00-00       893  10643  1013    433 L2  0000.0000.0024.00-00  <>
      Remaining lifetime received: 1199 s Modified to: 1200 s
      NLPID: 0xCC(IPv4)
      Hostname: h3c_24_S12500R-48C6D
      TE IPv4 router ID: 10.0.0.24
      Area addresses: 49
      Interface address: 10.0.0.24
      Interface address: 20.24.149.24
      Interface address: 20.24.170.24
      Interface address: 20.24.238.24
      IS Neighbor          : h49-N540-24Q8L2DD.00 Metric: 10
        IPv4 Neighbor Address: 20.24.149.149
        IPv4 Interface Address: 20.24.149.24
        Adj-sid: 56121 flags: [L V] weight: 0x0
        TE default metric: 10
        Maximum link BW: 0.00 bps
        Maximum reservable link BW: 0.00 bps
        Unreserved BW:
            TE class 0: 0.00 bps	TE class 1: 0.00 bps	TE class 2: 0.00 bps
            TE class 3: 0.00 bps	TE class 4: 0.00 bps	TE class 5: 0.00 bps
            TE class 6: 0.00 bps	TE class 7: 0.00 bps
      IS Neighbor          : Spine3-J-170.00     Metric: 10
        IPv4 Neighbor Address: 20.24.170.170
        IPv4 Interface Address: 20.24.170.24
        Adj-sid: 56120 flags: [L V] weight: 0x0
        TE default metric: 10
        Maximum link BW: 0.00 bps
        Maximum reservable link BW: 0.00 bps
        Unreserved BW:
            TE class 0: 0.00 bps	TE class 1: 0.00 bps	TE class 2: 0.00 bps
            TE class 3: 0.00 bps	TE class 4: 0.00 bps	TE class 5: 0.00 bps
            TE class 6: 0.00 bps	TE class 7: 0.00 bps
      Reachability         : 10.0.0.24/32 Metric: 0 Type: 1 Up
        SR Prefix-SID: 24 Flags: [N P] Algorithm: 0
      Reachability         : 20.24.149.0/24 Metric: 10 Type: 1 Up
      Reachability         : 20.24.170.0/24 Metric: 10 Type: 1 Up
      Reachability         : 20.24.238.0/24 Metric: 10 Type: 1 Up
      Router Capabilities: Router Id: 10.0.0.24 Flags: []
        SR Local Block:
          SRLB Base: 15000 Range: 1000
        Maximum SID depth:
          Base MPLS imposition (MSD type 1):  10
        SR Capability: Flags: [I]
          SRGB Base: 20000 Range: 2000
    Ribbon-32.00-00              83  47973   403     79 L2  0000.0000.0032.00-00  <>
      NLPID: 0xCC(IPv4)
      TE IPv4 router ID: 10.0.0.32
      Area addresses: 49.0001
      Router Capabilities: Router Id: 10.0.0.32 Flags: []
        SR Local Block:
          SRLB Base: 16 Range: 15344
        Maximum SID depth:
          Base MPLS imposition (MSD type 1):  10
        SR Capability: Flags: [I]
          SRGB Base: 20000 Range: 2000
      Unsupported TLV: Type: 14 Length: 2
    Ribbon-32.00-03              76  64252  1060     38 L2  0000.0000.0032.00-03  <>
      Hostname: Ribbon-32
    Ribbon-32.00-04              85  46189   716    285 L2  0000.0000.0032.00-04  <>
      Interface address: 10.0.0.32
      Interface address: 20.32.149.32
      Interface address: 20.32.170.32
      IS Neighbor          : h49-N540-24Q8L2DD.00 Metric: 10
        IPv4 Neighbor Address: 20.32.149.149
        IPv4 Interface Address: 20.32.149.32
        Adj-sid: 756641 flags: [L V] weight: 0x0
        Adj-sid: 756642 flags: [L V B] weight: 0x0
        TE default metric: 10
        Maximum link BW: 1.00 Gbps
        Maximum reservable link BW: 1.00 Gbps
        Unreserved BW:
            TE class 0: 1.00 Gbps	TE class 1: 1.00 Gbps	TE class 2: 1.00 Gbps
            TE class 3: 1.00 Gbps	TE class 4: 1.00 Gbps	TE class 5: 1.00 Gbps
            TE class 6: 1.00 Gbps	TE class 7: 1.00 Gbps
      IS Neighbor          : Spine3-J-170.00     Metric: 10
        IPv4 Neighbor Address: 20.32.170.170
        IPv4 Interface Address: 20.32.170.32
        Adj-sid: 756643 flags: [L V] weight: 0x0
        Adj-sid: 756644 flags: [L V B] weight: 0x0
        TE default metric: 10
        Maximum link BW: 10.00 Gbps
        Maximum reservable link BW: 10.00 Gbps
        Unreserved BW:
            TE class 0: 10.00 Gbps	TE class 1: 10.00 Gbps	TE class 2: 10.00 Gbps
            TE class 3: 10.00 Gbps	TE class 4: 10.00 Gbps	TE class 5: 10.00 Gbps
            TE class 6: 10.00 Gbps	TE class 7: 10.00 Gbps
      Reachability         : 10.0.0.32/32 Metric: 0 Type: 1 Up
        SR Prefix-SID: 32 Flags: [N] Algorithm: 0
      Reachability         : 20.32.149.0/24 Metric: 10 Type: 1 Up
      Reachability         : 20.32.170.0/24 Metric: 10 Type: 1 Up
    h43-9901.00-00              343  10807  1178    186 L2  0000.0000.0343.00-00  <>
      Remaining lifetime received: 1199 s Modified to: 1200 s
      NLPID: 0xCC(IPv4)
      Hostname: h43-9901
      TE IPv4 router ID: 10.0.1.43
      Area addresses: 49
      Interface address: 10.0.1.43
      IS Neighbor          : h49-N540-24Q8L2DD.00 Metric: 10
        IPv4 Neighbor Address: 20.143.149.149
        IPv4 Interface Address: 20.143.149.143
        Adj-sid: 24001 flags: [L V] weight: 0x0
        Maximum link BW: 10.00 Gbps
      Reachability         : 10.0.1.43/32 Metric: 0 Type: 1 Up
        SR Prefix-SID: 343 Flags: [N] Algorithm: 0
      Reachability         : 20.143.149.0/24 Metric: 10 Type: 1 Up
      Router Capabilities: Router Id: 10.0.1.43 Flags: []
        SR Local Block:
          SRLB Base: 15000 Range: 1000
        Maximum SID depth:
          Base MPLS imposition (MSD type 1):  10
        SR Capability: Flags: [I]
          SRGB Base: 20000 Range: 2000
        Algorithms:  0, 1
      Unsupported TLV: Type: 14 Length: 2
    h49-N540-24Q8L2DD.00-00       441    598   924   1289 L2  0000.0000.0349.00-00  <>
      Remaining lifetime received: 1199 s Modified to: 1200 s
      NLPID: 0xCC(IPv4)
      Hostname: h49-N540-24Q8L2DD
      TE IPv4 router ID: 10.0.1.49
      Area addresses: 49
      Interface address: 10.0.1.49
      IS Neighbor          : h3c_19_CR16010E-F.00 Metric: 10
        IPv4 Neighbor Address: 20.19.149.19
        IPv4 Interface Address: 20.19.149.149
        Adj-sid: 24015 flags: [L V] weight: 0x0
        Maximum link BW: 10.00 Gbps
        Min/Max unidirectional link delay: 11/11 us
        Application Specific Link Attributes:
          Standard applications: Flex-Algo
          User-defined applications: APP3
            TE default metric: 12
            Maximum link BW: 10.00 Gbps
            Min/Max unidirectional link delay: 11/11 us
      IS Neighbor          : h3c_24_S12500R-48C6D.00 Metric: 10
        IPv4 Neighbor Address: 20.24.149.24
        IPv4 Interface Address: 20.24.149.149
        Adj-sid: 24005 flags: [L V] weight: 0x0
        Maximum link BW: 100.00 Gbps
        Min/Max unidirectional link delay: 11/11 us
        Application Specific Link Attributes:
          Standard applications: Flex-Algo
          User-defined applications: APP3
            TE default metric: 12
            Maximum link BW: 100.00 Gbps
            Min/Max unidirectional link delay: 11/11 us
      IS Neighbor          : 0000.0010.0005.00   Metric: 10
        IPv4 Neighbor Address: 20.5.149.5
        IPv4 Interface Address: 20.5.149.149
        Adj-sid: 24003 flags: [L V] weight: 0x0
        Maximum link BW: 10.00 Gbps
        Application Specific Link Attributes:
          Standard applications: Flex-Algo
          User-defined applications: APP3
            TE default metric: 12
            Maximum link BW: 10.00 Gbps
      IS Neighbor          : PE31-J2-171.00      Metric: 10
        IPv4 Neighbor Address: 20.149.171.171
        IPv4 Interface Address: 20.149.171.149
        Adj-sid: 24009 flags: [L V] weight: 0x0
        Maximum link BW: 10.00 Gbps
        Min/Max unidirectional link delay: 1/1 us
        Application Specific Link Attributes:
          Standard applications: Flex-Algo
          User-defined applications: APP3
            Administrative group (Color): 127
            TE default metric: 12
            Maximum link BW: 10.00 Gbps
            Min/Max unidirectional link delay: 1/1 us
      IS Neighbor          : h43-9901.00         Metric: 10
        IPv4 Neighbor Address: 20.143.149.143
        IPv4 Interface Address: 20.143.149.149
        Adj-sid: 24011 flags: [L V] weight: 0x0
        Maximum link BW: 10.00 Gbps
        Min/Max unidirectional link delay: 11/11 us
        Application Specific Link Attributes:
          Standard applications: Flex-Algo
          User-defined applications: APP3
            TE default metric: 12
            Maximum link BW: 10.00 Gbps
            Min/Max unidirectional link delay: 11/11 us
      IS Neighbor          : h55-8201-24H8FH.00  Metric: 10
        IPv4 Neighbor Address: 20.149.155.155
        IPv4 Interface Address: 20.149.155.149
        Adj-sid: 24000 flags: [L V B] weight: 0x0
        Adj-sid: 24001 flags: [L V] weight: 0x0
        Maximum link BW: 100.00 Gbps
        Min/Max unidirectional link delay: 2/2 us
        Application Specific Link Attributes:
          Standard applications: Flex-Algo
          User-defined applications: APP3
            TE default metric: 12
            Maximum link BW: 100.00 Gbps
            Min/Max unidirectional link delay: 2/2 us
      IS Neighbor          : Ribbon-32.00        Metric: 10
        IPv4 Neighbor Address: 20.32.149.32
        IPv4 Interface Address: 20.32.149.149
        Adj-sid: 24007 flags: [L V] weight: 0x0
        Maximum link BW: 1.00 Gbps
        Min/Max unidirectional link delay: 11/11 us
        Application Specific Link Attributes:
          Standard applications: Flex-Algo
          User-defined applications: APP3
            TE default metric: 12
            Maximum link BW: 1.00 Gbps
            Min/Max unidirectional link delay: 11/11 us
      IS Neighbor          : juniper_379_MX304.00 Metric: 10
        IPv4 Neighbor Address: 20.149.179.179
        IPv4 Interface Address: 20.149.179.149
        Adj-sid: 24012 flags: [L V B] weight: 0x0
        Adj-sid: 24013 flags: [L V] weight: 0x0
        Maximum link BW: 10.00 Gbps
        Application Specific Link Attributes:
          Standard applications: Flex-Algo
          User-defined applications: APP3
            Maximum link BW: 10.00 Gbps
      IS Neighbor          : NOKIA-SR2-57.00     Metric: 10
        IPv4 Neighbor Address: 20.57.149.57
        IPv4 Interface Address: 20.57.149.149
        Adj-sid: 24018 flags: [L V B] weight: 0x0
        Adj-sid: 24019 flags: [L V] weight: 0x0
        Maximum link BW: 10.00 Gbps
        Min/Max unidirectional link delay: 11/11 us
        Application Specific Link Attributes:
          Standard applications: Flex-Algo
          User-defined applications: APP3
            Administrative group (Color): 127
            TE default metric: 12
            Maximum link BW: 10.00 Gbps
            Min/Max unidirectional link delay: 11/11 us
      Reachability         : 10.0.1.49/32 Metric: 0 Type: 1 Up
        SR Prefix-SID: 349 Flags: [N] Algorithm: 0
        SR Prefix-SID: 1449 Flags: [N] Algorithm: 129
        SR Prefix-SID: 1549 Flags: [N] Algorithm: 130
        SR Prefix-SID: 1649 Flags: [N] Algorithm: 131
        SR Prefix-SID: 1749 Flags: [N] Algorithm: 132
        SR Prefix-SID: 449 Flags: [N] Algorithm: 140
        SR Prefix-SID: 549 Flags: [N] Algorithm: 141
        SR Prefix-SID: 649 Flags: [N] Algorithm: 142
      Reachability         : 20.5.149.0/24 Metric: 10 Type: 1 Up
      Reachability         : 20.19.149.0/24 Metric: 10 Type: 1 Up
      Reachability         : 20.24.149.0/24 Metric: 10 Type: 1 Up
      Reachability         : 20.32.149.0/24 Metric: 10 Type: 1 Up
      Reachability         : 20.57.149.0/24 Metric: 10 Type: 1 Up
      Reachability         : 20.111.149.0/24 Metric: 10 Type: 1 Up
      Reachability         : 20.143.149.0/24 Metric: 10 Type: 1 Up
      Reachability         : 20.149.155.0/24 Metric: 10 Type: 1 Up
      Reachability         : 20.149.171.0/24 Metric: 10 Type: 1 Up
      Reachability         : 20.149.179.0/24 Metric: 10 Type: 1 Up
      Router Capabilities: Router Id: 10.0.1.49 Flags: []
        SR Local Block:
          SRLB Base: 15000 Range: 1000
        Maximum SID depth:
          Base MPLS imposition (MSD type 1):  12
        SR Capability: Flags: [I]
          SRGB Base: 20000 Range: 2000
        Algorithms:  0, 1, 128, 129, 130, 131, 132, 140, 141, 142
        Flex Algo: Algorithm: 129 Metric: TE Metric (2) Calc: SPF (0) Prio: 255
        Flex Algo: Algorithm: 130 Metric: IGP Metric (0) Calc: SPF (0) Prio: 255
          Exclude admin groups: 1
        Flex Algo: Algorithm: 131 Metric: IGP Metric (0) Calc: SPF (0) Prio: 255
          Exclude admin groups: 127
        Flex Algo: Algorithm: 132 Metric: IGP Metric (0) Calc: SPF (0) Prio: 255
          Exclude admin groups: 255
        Flex Algo: Algorithm: 140 Metric: IGP Metric (0) Calc: SPF (0) Prio: 255
        Flex Algo: Algorithm: 141 Metric: IGP Metric (0) Calc: SPF (0) Prio: 255
        Flex Algo: Algorithm: 142 Metric: IGP Metric (0) Calc: SPF (0) Prio: 255
      Unsupported TLV: Type: 14 Length: 2
    h55-8201-24H8FH.00-00       352  14968  1104    560 L2  0000.0000.0355.00-00  <>
      NLPID: 0xCC(IPv4)
      Hostname: h55-8201-24H8FH
      TE IPv4 router ID: 10.0.1.55
      Area addresses: 49
      Interface address: 10.0.1.55
      IS Neighbor          : h49-N540-24Q8L2DD.00 Metric: 10
        IPv4 Neighbor Address: 20.149.155.149
        IPv4 Interface Address: 20.149.155.155
        Adj-sid: 24001 flags: [L V] weight: 0x0
        Maximum link BW: 100.00 Gbps
        Min/Max unidirectional link delay: 2/2 us
        Application Specific Link Attributes:
          Standard applications: Flex-Algo
          User-defined applications: APP3
            TE default metric: 12
            Maximum link BW: 100.00 Gbps
            Min/Max unidirectional link delay: 2/2 us
      IS Neighbor          : Spine3-J-170.00     Metric: 10
        IPv4 Neighbor Address: 20.155.170.170
        IPv4 Interface Address: 20.155.170.155
        Adj-sid: 24007 flags: [L V] weight: 0x0
        Maximum link BW: 100.00 Gbps
        Application Specific Link Attributes:
          Standard applications: Flex-Algo
          User-defined applications: APP3
            Maximum link BW: 100.00 Gbps
      Reachability         : 10.0.1.55/32 Metric: 0 Type: 1 Up
        SR Prefix-SID: 355 Flags: [N] Algorithm: 0
        SR Prefix-SID: 1355 Flags: [N] Algorithm: 128
        SR Prefix-SID: 1455 Flags: [N] Algorithm: 129
        SR Prefix-SID: 1555 Flags: [N] Algorithm: 130
        SR Prefix-SID: 1655 Flags: [N] Algorithm: 131
        SR Prefix-SID: 1755 Flags: [N] Algorithm: 132
        SR Prefix-SID: 455 Flags: [N] Algorithm: 140
        SR Prefix-SID: 555 Flags: [N] Algorithm: 141
        SR Prefix-SID: 655 Flags: [N] Algorithm: 142
      Reachability         : 20.32.155.0/24 Metric: 10 Type: 1 Up
      Reachability         : 20.57.155.0/24 Metric: 10 Type: 1 Up
      Reachability         : 20.149.155.0/24 Metric: 10 Type: 1 Up
      Reachability         : 20.155.170.0/24 Metric: 10 Type: 1 Up
      Reachability         : 209.209.209.209/32 Metric: 0 Type: 1 Up
        SR Prefix-SID: 209 Flags: [] Algorithm: 0
      Router Capabilities: Router Id: 10.0.1.55 Flags: []
        SR Local Block:
          SRLB Base: 15000 Range: 1000
        Maximum SID depth:
          Base MPLS imposition (MSD type 1):  7
        SR Capability: Flags: [I]
          SRGB Base: 20000 Range: 2000
        Algorithms:  0, 1, 128, 129, 130, 131, 132, 140, 141, 142
        Flex Algo: Algorithm: 128 Metric: Min Unidirectional Delay Metric (1) Calc: SPF (0) Prio: 10
        Flex Algo: Algorithm: 129 Metric: TE Metric (2) Calc: SPF (0) Prio: 10
        Flex Algo: Algorithm: 130 Metric: IGP Metric (0) Calc: SPF (0) Prio: 10
          Exclude admin groups: 1
        Flex Algo: Algorithm: 131 Metric: IGP Metric (0) Calc: SPF (0) Prio: 10
          Exclude admin groups: 127
        Flex Algo: Algorithm: 132 Metric: IGP Metric (0) Calc: SPF (0) Prio: 10
          Exclude admin groups: 255
        Flex Algo: Algorithm: 140 Metric: IGP Metric (0) Calc: SPF (0) Prio: 10
        Flex Algo: Algorithm: 141 Metric: IGP Metric (0) Calc: SPF (0) Prio: 10
        Flex Algo: Algorithm: 142 Metric: IGP Metric (0) Calc: SPF (0) Prio: 10
      Unsupported TLV: Type: 14 Length: 2
    juniper_379_MX304.00-00      1230  33978   733    323 L2  0000.0001.7900.00-00  <>
      Remaining lifetime received: 1198 s Modified to: 1200 s
      NLPID: 0xCC(IPv4) 0x8E(IPv6)
      Hostname: juniper_379_MX304
      TE IPv4 router ID: 10.0.0.179
      Area addresses: 49.0001.00
      Interface address: 10.0.0.179
      Interface address: 209.209.209.209
      Interface address: 127.0.0.1
      IS Neighbor          : h49-N540-24Q8L2DD.00 Metric: 100
        IPv4 Neighbor Address: 20.149.179.149
        IPv4 Interface Address: 20.149.179.179
        Adj-sid: 23 flags: [L V B] weight: 0x0
        Administrative group (Color): 7
        Maximum link BW: 10.00 Gbps
      IS Neighbor          : Spine3-J-170.00     Metric: 10
        IPv4 Neighbor Address: 20.170.179.170
        IPv4 Interface Address: 20.170.179.179
        Adj-sid: 27 flags: [L V] weight: 0x0
        Administrative group (Color): 6
        Maximum link BW: 10.00 Gbps
      Reachability         : 30.155.179.0/24 Metric: 10 Type: 1 Up
      Reachability         : 10.0.0.179/32 Metric: 0 Type: 1 Up
        SR Prefix-SID: 379 Flags: [N] Algorithm: 0
        SR Prefix-SID: 1379 Flags: [N] Algorithm: 130
        SR Prefix-SID: 1279 Flags: [N] Algorithm: 129
        SR Prefix-SID: 1179 Flags: [N] Algorithm: 128
      Reachability         : 209.209.209.209/32 Metric: 0 Type: 1 Up
        SR Prefix-SID: 209 Flags: [] Algorithm: 0
      Reachability         : 127.0.0.1/32 Metric: 0 Type: 1 Up
      Reachability         : 20.149.179.0/24 Metric: 100 Type: 1 Up
      Reachability         : 20.170.179.0/24 Metric: 10 Type: 1 Up
      Router Capabilities: Router Id: 10.0.0.179 Flags: []
        Maximum SID depth:
          Base MPLS imposition (MSD type 1):  4
        SR Capability: Flags: [I V]
          SRGB Base: 20000 Range: 2000
        Algorithms:  0, 1, 128, 129, 130
      Unsupported TLV: Type: 14 Length: 2
    JNPR-312-ACX7100-48L.00-00       368    598  1128    178 L2  0000.0003.1200.00-00  <>
      Remaining lifetime received: 1198 s Modified to: 1200 s
      NLPID: 0xCC(IPv4) 0x8E(IPv6)
      Hostname: JNPR-312-ACX7100-48L
      TE IPv4 router ID: 10.0.0.212
      Area addresses: 49.0001.00
      Interface address: 10.0.0.212
      IS Neighbor          : Spine3-J-170.00     Metric: 10
        IPv4 Neighbor Address: 20.170.212.170
        IPv4 Interface Address: 20.170.212.212
        Adj-sid: 17 flags: [L V B] weight: 0x0
      Reachability         : 10.0.0.212/32 Metric: 0 Type: 1 Up
        SR Prefix-SID: 212 Flags: [N P E] Algorithm: 0
      Reachability         : 20.170.212.0/24 Metric: 10 Type: 1 Up
      Router Capabilities: Router Id: 10.0.0.212 Flags: []
        Maximum SID depth:
          Base MPLS imposition (MSD type 1):  4
        SR Capability: Flags: [I V]
          SRGB Base: 20000 Range: 2000
        Algorithms:  0, 1
      Unsupported TLV: Type: 14 Length: 2
    0000.0010.0005.00-00        294  10679  1056    319 L2  0000.0010.0005.00-00  <>
      Remaining lifetime received: 1199 s Modified to: 1200 s
      NLPID: 0xCC(IPv4)
      TE IPv4 router ID: 10.0.0.5
      Area addresses: 49.0000
      Interface address: 20.5.149.5
      IS Neighbor          : h49-N540-24Q8L2DD.00 Metric: 10
        IPv4 Neighbor Address: 20.5.149.149
        IPv4 Interface Address: 20.5.149.5
        Adj-sid: 16000 flags: [L V] weight: 0x0
        Maximum link BW: 10.00 Gbps
        Maximum reservable link BW: 10.00 Gbps
        Unreserved BW:
            TE class 0: 10.00 Gbps	TE class 1: 10.00 Gbps	TE class 2: 10.00 Gbps
            TE class 3: 10.00 Gbps	TE class 4: 10.00 Gbps	TE class 5: 10.00 Gbps
            TE class 6: 10.00 Gbps	TE class 7: 10.00 Gbps
        Application Specific Link Attributes:
          Standard applications: [L] RSVP-TE SR-TE LFA Flex-Algo
      IS Neighbor          : Spine3-J-170.00     Metric: 10
        IPv4 Neighbor Address: 20.5.170.170
        IPv4 Interface Address: 20.5.170.5
        Adj-sid: 16001 flags: [L V] weight: 0x0
        Maximum link BW: 100.00 Gbps
        Maximum reservable link BW: 100.00 Gbps
        Unreserved BW:
            TE class 0: 100.00 Gbps	TE class 1: 100.00 Gbps	TE class 2: 100.00 Gbps
            TE class 3: 100.00 Gbps	TE class 4: 100.00 Gbps	TE class 5: 100.00 Gbps
            TE class 6: 100.00 Gbps	TE class 7: 100.00 Gbps
        Application Specific Link Attributes:
          Standard applications: [L] RSVP-TE SR-TE LFA Flex-Algo
      Reachability         : 10.0.0.5/32 Metric: 0 Type: 1 Up
        SR Prefix-SID: 5 Flags: [N P] Algorithm: 0
      Reachability         : 20.5.149.0/24 Metric: 10 Type: 1 Up
      Reachability         : 20.5.170.0/24 Metric: 10 Type: 1 Up
      Reachability          : 2002::5/128 Metric: 0 Type: 1 Up
      Router Capabilities: Router Id: 10.0.0.5 Flags: []
        SR Capability: Flags: [I]
          SRGB Base: 20000 Range: 2000
        Algorithms:  0
    NOKIA-SR2-57.00-00        12677  41780  1146    348 L2  0100.0000.0057.00-00  <>
      NLPID: 0xCC(IPv4) 0x8E(IPv6)
      Hostname: NOKIA-SR2-57
      TE IPv4 router ID: 10.0.0.57
      TE IPv6 router ID: 2002::57
      Area addresses: 49.0000.0000.0057.00
      Interface address: 10.0.0.57
      Interface address: 20.57.149.57
      Interface address: 20.57.170.57
      Interface address: 2002::57
      IS Neighbor          : h49-N540-24Q8L2DD.00 Metric: 10
        IPv4 Neighbor Address: 20.57.149.149
        IPv4 Interface Address: 20.57.149.57
        Adj-sid: 30149 flags: [L V B] weight: 0x0
        Application Specific Link Attributes:
          Standard applications: SR-TE
            Administrative group (Color): 11
            Maximum link BW: 10.00 Gbps
        Application Specific Link Attributes:
          Standard applications: Flex-Algo
            Administrative group (Color): 127
            Min/Max unidirectional link delay: 11/11 us
      IS Neighbor          : Spine3-J-170.00     Metric: 10
        IPv4 Neighbor Address: 20.57.170.170
        IPv4 Interface Address: 20.57.170.57
        Adj-sid: 30170 flags: [L V B] weight: 0x0
        Application Specific Link Attributes:
          Standard applications: SR-TE
            Administrative group (Color): 10
            Maximum link BW: 10.00 Gbps
      Reachability         : 10.0.0.57/32 Metric: 0 Type: 1 Up
        SR Prefix-SID: 57 Flags: [N P] Algorithm: 0
      Reachability         : 20.57.149.0/24 Metric: 10 Type: 1 Up
      Reachability         : 20.57.170.0/24 Metric: 10 Type: 1 Up
      Reachability          : 2002::57/128 Metric: 0 Type: 1 Up
        SR Prefix-SID: 157 Flags: [N P] Algorithm: 0
      Router Capabilities: Router Id: 10.0.0.57 Flags: []
        Maximum SID depth:
          Base MPLS imposition (MSD type 1):  12
        SR Capability: Flags: [I V]
          SRGB Base: 20000 Range: 2000
        Algorithms:  0
    Spine3-J-170.00-00          847  13870   471    570 L2  0100.0000.0170.00-00  <>
      LSP generation remaining wait time: 0 ms
      Time remaining until refresh: 171 s
      NLPID: 0xCC(IPv4)
      Hostname: Spine3-J-170
      TE IPv4 router ID: 10.0.0.170
      Area addresses: 49.0000
      Interface address: 20.5.170.170
      Interface address: 20.32.170.170
      Interface address: 20.24.170.170
      Interface address: 20.170.212.170
      Interface address: 20.170.179.170
      Interface address: 20.19.170.170
      Interface address: 20.170.171.170
      Interface address: 20.57.170.170
      Interface address: 20.155.170.170
      Interface address: 10.0.0.170
      IS Neighbor          : 0000.0010.0005.00   Metric: 10
        IPv4 Neighbor Address: 20.5.170.5
        IPv4 Interface Address: 20.5.170.170
        Adj-sid: 362153 flags: [L V] weight: 0x0
      IS Neighbor          : juniper_379_MX304.00 Metric: 10
        IPv4 Neighbor Address: 20.170.179.179
        IPv4 Interface Address: 20.170.179.170
        Adj-sid: 362291 flags: [L V] weight: 0x0
      IS Neighbor          : h3c_24_S12500R-48C6D.00 Metric: 100
        IPv4 Neighbor Address: 20.24.170.24
        IPv4 Interface Address: 20.24.170.170
        Adj-sid: 362154 flags: [L V] weight: 0x0
      IS Neighbor          : JNPR-312-ACX7100-48L.00 Metric: 10
        IPv4 Neighbor Address: 20.170.212.212
        IPv4 Interface Address: 20.170.212.170
        Adj-sid: 362149 flags: [L V] weight: 0x0
      IS Neighbor          : NOKIA-SR2-57.00     Metric: 1
        IPv4 Neighbor Address: 20.57.170.57
        IPv4 Interface Address: 20.57.170.170
        Adj-sid: 362163 flags: [L V] weight: 0x0
        Application Specific Link Attributes:
          Standard applications: Flex-Algo
            TE default metric: 555
      IS Neighbor          : h3c_19_CR16010E-F.00 Metric: 10
        IPv4 Neighbor Address: 20.19.170.19
        IPv4 Interface Address: 20.19.170.170
        Adj-sid: 362158 flags: [L V] weight: 0x0
      IS Neighbor          : h55-8201-24H8FH.00  Metric: 20
        IPv4 Neighbor Address: 20.155.170.155
        IPv4 Interface Address: 20.155.170.170
        Adj-sid: 362144 flags: [L V] weight: 0x0
      IS Neighbor          : Ribbon-32.00        Metric: 12
        IPv4 Neighbor Address: 20.32.170.32
        IPv4 Interface Address: 20.32.170.170
        Adj-sid: 362152 flags: [L V] weight: 0x0
      IS Neighbor          : PE31-J2-171.00      Metric: 10
        IPv4 Neighbor Address: 20.170.171.171
        IPv4 Interface Address: 20.170.171.170
        Adj-sid: 362156 flags: [L V] weight: 0x0
        Application Specific Link Attributes:
          Standard applications: Flex-Algo
            TE default metric: 10
      Reachability         : 20.5.170.0/24 Metric: 10 Type: 1 Up
      Reachability         : 20.32.170.0/24 Metric: 12 Type: 1 Up
      Reachability         : 20.24.170.0/24 Metric: 100 Type: 1 Up
      Reachability         : 20.170.212.0/24 Metric: 10 Type: 1 Up
      Reachability         : 20.170.179.0/24 Metric: 10 Type: 1 Up
      Reachability         : 20.19.170.0/24 Metric: 10 Type: 1 Up
      Reachability         : 20.170.171.0/24 Metric: 10 Type: 1 Up
      Reachability         : 20.57.170.0/24 Metric: 1 Type: 1 Up
      Reachability         : 20.155.170.0/24 Metric: 20 Type: 1 Up
      Reachability         : 10.0.0.170/32 Metric: 0 Type: 1 Up
        SR Prefix-SID: 170 Flags: [N] Algorithm: 0
      Router Capabilities: Router Id: 10.0.0.170 Flags: []
        SR Local Block:
          SRLB Base: 965536 Range: 65536
        Area leader priority: 250 algorithm: 0
        Maximum SID depth:
          Base MPLS imposition (MSD type 1):  6
        SR Capability: Flags: [I]
          SRGB Base: 20000 Range: 2000
        Algorithms:  0, 128, 129, 130, 131
        Flex Algo: Algorithm: 131 Metric: IGP Metric (0) Calc: SPF (0) Prio: 237
          Exclude admin groups: 127
        Flex Algo: Algorithm: 130 Metric: IGP Metric (0) Calc: SPF (0) Prio: 237
        Flex Algo: Algorithm: 129 Metric: TE Metric (2) Calc: SPF (0) Prio: 237
        Flex Algo: Algorithm: 128 Metric: Min Unidirectional Delay Metric (1) Calc: SPF (0) Prio: 237
    PE31-J2-171.00-00           365  10524   493    323 L2  0100.0000.0171.00-00  <>
      Remaining lifetime received: 1199 s Modified to: 1200 s
      NLPID: 0xCC(IPv4)
      Hostname: PE31-J2-171
      Area addresses: 49.0000
      Interface address: 20.170.171.171
      Interface address: 20.149.171.171
      Interface address: 10.0.0.171
      IS Neighbor          : h49-N540-24Q8L2DD.00 Metric: 11
        IPv4 Neighbor Address: 20.149.171.149
        IPv4 Interface Address: 20.149.171.171
        Adj-sid: 362144 flags: [L V] weight: 0x0
        Application Specific Link Attributes:
          Standard applications: Flex-Algo
            Administrative group (Color): 127
            TE default metric: 12
            Min/Max unidirectional link delay: 2/2 us
      IS Neighbor          : Spine3-J-170.00     Metric: 30
        IPv4 Neighbor Address: 20.170.171.170
        IPv4 Interface Address: 20.170.171.171
        Adj-sid: 362145 flags: [L V] weight: 0x0
      Reachability         : 10.0.0.171/32 Metric: 0 Type: 1 Up
        SR Prefix-SID: 171 Flags: [N] Algorithm: 0
        SR Prefix-SID: 1171 Flags: [N] Algorithm: 128
        SR Prefix-SID: 1271 Flags: [N] Algorithm: 129
        SR Prefix-SID: 1371 Flags: [N] Algorithm: 130
        SR Prefix-SID: 1471 Flags: [N] Algorithm: 131
      Reachability         : 20.170.171.0/24 Metric: 30 Type: 1 Up
      Reachability         : 20.149.171.0/24 Metric: 11 Type: 1 Up
      Router Capabilities: Router Id: 10.0.0.171 Flags: []
        SR Local Block:
          SRLB Base: 965536 Range: 65536
        Area leader priority: 250 algorithm: 0
        Maximum SID depth:
          Base MPLS imposition (MSD type 1):  12
        SR Capability: Flags: [I]
          SRGB Base: 20000 Range: 2000
        Algorithms:  0, 128, 129, 130, 131
        Flex Algo: Algorithm: 131 Metric: IGP Metric (0) Calc: SPF (0) Prio: 237
          Exclude admin groups: 127
        Flex Algo: Algorithm: 130 Metric: IGP Metric (0) Calc: SPF (0) Prio: 237
        Flex Algo: Algorithm: 129 Metric: TE Metric (2) Calc: SPF (0) Prio: 237
        Flex Algo: Algorithm: 128 Metric: Min Unidirectional Delay Metric (1) Calc: SPF (0) Prio: 237
```

## show isis flex-algo

```text

IS-IS Instance: IGP VRF: default

Algorithm     Advertised Level Metric    Selected         
------------- ---------- ----- --------- -----------------
MIN-LATENCY   yes        L2    min-delay PE31-J2-171      
MIN-TE        yes        L2    TE        h49-N540-24Q8L2DD
MIN-IGP       yes        L2    default   h49-N540-24Q8L2DD
MIN-IGP-ADMIN yes        L2    default   h49-N540-24Q8L2DD

```

## show isis flex-algo path detail

```text
Flex algo paths for IPv4 address family
Topology ID: Level-2
Destination: PE31-J2-171
Path ID: 640
Path constraints: algo MIN-LATENCY
                  metric type MIN-DELAY
Request sequence number: 153
Response sequence number: 153
Number of times path updated: 145
Last updated: 0:11:47 ago
Next Hop Interface
-------- ---------

Destination: PE31-J2-171
Path ID: 641
Path constraints: algo MIN-TE
                  metric type TE
Request sequence number: 163
Response sequence number: 163
Number of times path updated: 154
Last updated: 0:04:35 ago
Metric: 10
Next Hop       Interface
-------------- ---------
20.170.171.171 Ethernet1

Destination: PE31-J2-171
Path ID: 642
Path constraints: algo MIN-IGP
                  metric type IGP
                  administrative-group exclude 1
Request sequence number: 163
Response sequence number: 163
Number of times path updated: 153
Last updated: 0:04:35 ago
Metric: 10
Next Hop       Interface
-------------- ---------
20.170.171.171 Ethernet1

Destination: PE31-J2-171
Path ID: 643
Path constraints: algo MIN-IGP-ADMIN
                  metric type IGP
                  administrative-group exclude 127
Request sequence number: 150
Response sequence number: 150
Number of times path updated: 143
Last updated: 0:04:35 ago
Metric: 10
Next Hop       Interface
-------------- ---------
20.170.171.171 Ethernet1

Destination: h49-N540-24Q8L2DD
Path ID: 641
Path constraints: algo MIN-TE
                  metric type TE
Request sequence number: 174
Response sequence number: 174
Number of times path updated: 160
Last updated: 0:04:35 ago
Metric: 22
Next Hop       Interface
-------------- ---------
20.170.171.171 Ethernet1

Destination: h49-N540-24Q8L2DD
Path ID: 642
Path constraints: algo MIN-IGP
                  metric type IGP
                  administrative-group exclude 1
Request sequence number: 171
Response sequence number: 171
Number of times path updated: 162
Last updated: 0:04:35 ago
Metric: 21
Next Hop       Interface
-------------- ---------
20.170.171.171 Ethernet1

Destination: h49-N540-24Q8L2DD
Path ID: 643
Path constraints: algo MIN-IGP-ADMIN
                  metric type IGP
                  administrative-group exclude 127
Request sequence number: 155
Response sequence number: 155
Number of times path updated: 150
Last updated: 0:04:35 ago
Metric: 30
Next Hop       Interface   
-------------- ------------
20.155.170.155 Ethernet51/1

Destination: h55-8201-24H8FH
Path ID: 640
Path constraints: algo MIN-LATENCY
                  metric type MIN-DELAY
Request sequence number: 162
Response sequence number: 162
Number of times path updated: 147
Last updated: 0:11:47 ago
Next Hop Interface
-------- ---------

Destination: h55-8201-24H8FH
Path ID: 641
Path constraints: algo MIN-TE
                  metric type TE
Request sequence number: 174
Response sequence number: 174
Number of times path updated: 160
Last updated: 0:04:35 ago
Metric: 34
Next Hop       Interface
-------------- ---------
20.170.171.171 Ethernet1

Destination: h55-8201-24H8FH
Path ID: 642
Path constraints: algo MIN-IGP
                  metric type IGP
                  administrative-group exclude 1
Request sequence number: 171
Response sequence number: 171
Number of times path updated: 158
Last updated: 0:04:35 ago
Metric: 20
Next Hop       Interface   
-------------- ------------
20.155.170.155 Ethernet51/1

Destination: h55-8201-24H8FH
Path ID: 643
Path constraints: algo MIN-IGP-ADMIN
                  metric type IGP
                  administrative-group exclude 127
Request sequence number: 155
Response sequence number: 155
Number of times path updated: 146
Last updated: 0:04:35 ago
Metric: 20
Next Hop       Interface   
-------------- ------------
20.155.170.155 Ethernet51/1

Destination: juniper_379_MX304
Path ID: 640
Path constraints: algo MIN-LATENCY
                  metric type MIN-DELAY
Request sequence number: 88
Response sequence number: 88
Number of times path updated: 87
Last updated: 0:11:47 ago
Next Hop Interface
-------- ---------

Destination: juniper_379_MX304
Path ID: 641
Path constraints: algo MIN-TE
                  metric type TE
Request sequence number: 92
Response sequence number: 92
Number of times path updated: 90
Last updated: 0:04:35 ago
Next Hop Interface
-------- ---------

Destination: juniper_379_MX304
Path ID: 642
Path constraints: algo MIN-IGP
                  metric type IGP
                  administrative-group exclude 1
Request sequence number: 92
Response sequence number: 92
Number of times path updated: 90
Last updated: 0:04:35 ago
Metric: 10
Next Hop       Interface   
-------------- ------------
20.170.179.179 Ethernet49/1

```

## show isis segment-routing tunnel

```text
 Index   Endpoint             Next Hop/Tunnel Index    Interface      Labels   
------- -------------------- ------------------------ --------------- ---------
 1       10.0.1.55/32         TI-LFA (13)              -              [ 3 ]    
 2       209.209.209.209/32   TI-LFA (0)               -              [ 3 ]    
 4       10.0.0.57/32         TI-LFA (15)              -              [ 20057 ]
 7       10.0.0.212/32        20.170.212.212           Ethernet49/2   [ 0 ]    
 8       10.0.0.179/32        TI-LFA (5)               -              [ 3 ]    
 10      10.0.0.32/32         TI-LFA (4)               -              [ 3 ]    
 11      10.0.0.5/32          TI-LFA (3)               -              [ 20005 ]
 12      10.0.0.19/32         TI-LFA (1)               -              [ 3 ]    
 13      10.0.1.49/32         TI-LFA (12)              -              [ 20349 ]
 14      10.0.1.43/32         TI-LFA (12)              -              [ 20343 ]
 16      10.0.0.24/32         TI-LFA (12)              -              [ 20024 ]
 17      10.0.0.171/32        TI-LFA (17)              -              [ 3 ]    

```

## show isis segment-routing prefix-segments

```text

System ID: Spine3-J-170			Instance: 'IGP'
SR supported Data-plane: MPLS			SR Router ID: 10.0.0.170

Node: 35     Proxy-Node: 0      Prefix: 1       Total Segments: 36

Flag Descriptions: R: Re-advertised, N: Node Segment, P: no-PHP
                   E: Explicit-NULL, V: Value, L: Local
Segment status codes: * - Self originated Prefix, L1 - level 1, L2 - level 2, ! - SR-unreachable,
                      # - Some IS-IS next-hops are SR-unreachable
   Prefix                      SID Type       Flags                        System ID       Level Protection  Algorithm   
   ------------------------- ----- ---------- ---------------------------- --------------- ----- ----------- -------------
   10.0.0.5/32                   5 Node       R:0 N:1 P:1 E:0 V:0 L:0      0000.0010.0005  L2    node        SPF         
   10.0.0.19/32                 19 Node       R:0 N:1 P:0 E:0 V:0 L:0      h3c_19_CR16010E-F L2    node        SPF         
   10.0.0.24/32                 24 Node       R:0 N:1 P:1 E:0 V:0 L:0      h3c_24_S12500R-48C6D L2    node        SPF         
   10.0.0.32/32                 32 Node       R:0 N:1 P:0 E:0 V:0 L:0      Ribbon-32       L2    node        SPF         
   10.0.0.57/32                 57 Node       R:0 N:1 P:1 E:0 V:0 L:0      NOKIA-SR2-57    L2    node        SPF         
*  10.0.0.170/32               170 Node       R:0 N:1 P:0 E:0 V:0 L:0      Spine3-J-170    L2    unprotected SPF         
   10.0.0.171/32               171 Node       R:0 N:1 P:0 E:0 V:0 L:0      PE31-J2-171     L2    node        SPF         
   10.0.0.171/32              1171 Node       R:0 N:1 P:0 E:0 V:0 L:0      PE31-J2-171     L2    unprotected MIN-LATENCY 
   10.0.0.171/32              1271 Node       R:0 N:1 P:0 E:0 V:0 L:0      PE31-J2-171     L2    node        MIN-TE      
   10.0.0.171/32              1371 Node       R:0 N:1 P:0 E:0 V:0 L:0      PE31-J2-171     L2    node        MIN-IGP     
   10.0.0.171/32              1471 Node       R:0 N:1 P:0 E:0 V:0 L:0      PE31-J2-171     L2    node        MIN-IGP-ADMIN
   10.0.0.179/32               379 Node       R:0 N:1 P:0 E:0 V:0 L:0      juniper_379_MX304 L2    node        SPF         
   10.0.0.179/32              1179 Node       R:0 N:1 P:0 E:0 V:0 L:0      juniper_379_MX304 L2    unprotected MIN-LATENCY 
   10.0.0.179/32              1279 Node       R:0 N:1 P:0 E:0 V:0 L:0      juniper_379_MX304 L2    unprotected MIN-TE      
   10.0.0.179/32              1379 Node       R:0 N:1 P:0 E:0 V:0 L:0      juniper_379_MX304 L2    node        MIN-IGP     
   10.0.0.212/32               212 Node       R:0 N:1 P:1 E:1 V:0 L:0      JNPR-312-ACX7100-48L L2    node        SPF         
   10.0.1.43/32                343 Node       R:0 N:1 P:0 E:0 V:0 L:0      h43-9901        L2    node        SPF         
   10.0.1.49/32                349 Node       R:0 N:1 P:0 E:0 V:0 L:0      h49-N540-24Q8L2DD L2    node        SPF         
   10.0.1.49/32               1449 Node       R:0 N:1 P:0 E:0 V:0 L:0      h49-N540-24Q8L2DD L2    node        MIN-TE      
   10.0.1.49/32               1549 Node       R:0 N:1 P:0 E:0 V:0 L:0      h49-N540-24Q8L2DD L2    node        MIN-IGP     
   10.0.1.49/32               1649 Node       R:0 N:1 P:0 E:0 V:0 L:0      h49-N540-24Q8L2DD L2    node        MIN-IGP-ADMIN
   10.0.1.49/32               1749 Node       R:0 N:1 P:0 E:0 V:0 L:0      h49-N540-24Q8L2DD L2    unprotected 132         
   10.0.1.49/32                449 Node       R:0 N:1 P:0 E:0 V:0 L:0      h49-N540-24Q8L2DD L2    unprotected 140         
   10.0.1.49/32                549 Node       R:0 N:1 P:0 E:0 V:0 L:0      h49-N540-24Q8L2DD L2    unprotected 141         
   10.0.1.49/32                649 Node       R:0 N:1 P:0 E:0 V:0 L:0      h49-N540-24Q8L2DD L2    unprotected 142         
   10.0.1.55/32                355 Node       R:0 N:1 P:0 E:0 V:0 L:0      h55-8201-24H8FH L2    node        SPF         
   10.0.1.55/32               1355 Node       R:0 N:1 P:0 E:0 V:0 L:0      h55-8201-24H8FH L2    unprotected MIN-LATENCY 
   10.0.1.55/32               1455 Node       R:0 N:1 P:0 E:0 V:0 L:0      h55-8201-24H8FH L2    node        MIN-TE      
   10.0.1.55/32               1555 Node       R:0 N:1 P:0 E:0 V:0 L:0      h55-8201-24H8FH L2    node        MIN-IGP     
   10.0.1.55/32               1655 Node       R:0 N:1 P:0 E:0 V:0 L:0      h55-8201-24H8FH L2    node        MIN-IGP-ADMIN
   10.0.1.55/32               1755 Node       R:0 N:1 P:0 E:0 V:0 L:0      h55-8201-24H8FH L2    unprotected 132         
   10.0.1.55/32                455 Node       R:0 N:1 P:0 E:0 V:0 L:0      h55-8201-24H8FH L2    unprotected 140         
   10.0.1.55/32                555 Node       R:0 N:1 P:0 E:0 V:0 L:0      h55-8201-24H8FH L2    unprotected 141         
   10.0.1.55/32                655 Node       R:0 N:1 P:0 E:0 V:0 L:0      h55-8201-24H8FH L2    unprotected 142         
   209.209.209.209/32          209 Prefix     R:0 N:0 P:0 E:0 V:0 L:0      juniper_379_MX304 L2    node        SPF         
   209.209.209.209/32          209 Prefix     R:0 N:0 P:0 E:0 V:0 L:0      h55-8201-24H8FH L2    node        SPF         
   2002::57/128                157 Node       R:0 N:1 P:1 E:0 V:0 L:0      NOKIA-SR2-57    L2    unprotected SPF         
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

 I L2     10.0.0.5/32 [115/10]
           via 20.5.170.5, Ethernet50/1
 I L2     10.0.0.19/32 [115/10]
           via 20.19.170.19, Ethernet25
 I L2     10.0.0.24/32 [115/21]
           via 20.57.170.57, Ethernet45
 I L2     10.0.0.32/32 [115/12]
           via 20.32.170.32, Ethernet43
 I L2     10.0.0.57/32 [115/1]
           via 20.57.170.57, Ethernet45
 C        10.0.0.170/32
           directly connected, Loopback0
 I L2     10.0.0.171/32 [115/10]
           via 20.170.171.171, Ethernet1
 I L2     10.0.0.179/32 [115/10]
           via 20.170.179.179, Ethernet49/1
 I L2     10.0.0.212/32 [115/10]
           via 20.170.212.212, Ethernet49/2
 I L2     10.0.1.43/32 [115/21]
           via 20.57.170.57, Ethernet45
 I L2     10.0.1.49/32 [115/11]
           via 20.57.170.57, Ethernet45
 I L2     10.0.1.55/32 [115/20]
           via 20.155.170.155, Ethernet51/1
 I L2     20.5.149.0/24 [115/20]
           via 20.5.170.5, Ethernet50/1
 C        20.5.170.0/24
           directly connected, Ethernet50/1
 I L2     20.19.149.0/24 [115/20]
           via 20.19.170.19, Ethernet25
 C        20.19.170.0/24
           directly connected, Ethernet25
 I L2     20.24.149.0/24 [115/21]
           via 20.57.170.57, Ethernet45
 C        20.24.170.0/24
           directly connected, Ethernet53/1
 I L2     20.24.238.0/24 [115/31]
           via 20.57.170.57, Ethernet45
 I L2     20.32.149.0/24 [115/21]
           via 20.57.170.57, Ethernet45
 I L2     20.32.155.0/24 [115/30]
           via 20.155.170.155, Ethernet51/1
 C        20.32.170.0/24
           directly connected, Ethernet43
 I L2     20.57.149.0/24 [115/11]
           via 20.57.170.57, Ethernet45
 I L2     20.57.155.0/24 [115/30]
           via 20.155.170.155, Ethernet51/1
 C        20.57.170.0/24
           directly connected, Ethernet45
 I L2     20.111.149.0/24 [115/21]
           via 20.57.170.57, Ethernet45
 I L2     20.143.149.0/24 [115/21]
           via 20.57.170.57, Ethernet45
 I L2     20.149.155.0/24 [115/21]
           via 20.57.170.57, Ethernet45
 I L2     20.149.171.0/24 [115/21]
           via 20.170.171.171, Ethernet1
           via 20.57.170.57, Ethernet45
 I L2     20.149.179.0/24 [115/21]
           via 20.57.170.57, Ethernet45
 C        20.155.170.0/24
           directly connected, Ethernet51/1
 C        20.170.171.0/24
           directly connected, Ethernet1
 C        20.170.179.0/24
           directly connected, Ethernet49/1
 C        20.170.212.0/24
           directly connected, Ethernet49/2
 I L2     30.155.179.0/24 [115/20]
           via 20.170.179.179, Ethernet49/1
 I L2     31.9.1.0/24 [115/10]
           via 20.19.170.19, Ethernet25
 I L2     192.168.0.0/19 [115/10]
           via 20.19.170.19, Ethernet25
 I L2     209.209.209.209/32 [115/10]
           via 20.170.179.179, Ethernet49/1

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

 I L2     10.0.0.5/32 [115/10]
           via 20.5.170.5, Ethernet50/1
 I L2     10.0.0.19/32 [115/10]
           via 20.19.170.19, Ethernet25
 I L2     10.0.0.24/32 [115/21]
           via 20.57.170.57, Ethernet45
 I L2     10.0.0.32/32 [115/12]
           via 20.32.170.32, Ethernet43
 I L2     10.0.0.57/32 [115/1]
           via 20.57.170.57, Ethernet45
 C        10.0.0.170/32
           directly connected, Loopback0
 I L2     10.0.0.171/32 [115/10]
           via 20.170.171.171, Ethernet1
 I L2     10.0.0.179/32 [115/10]
           via 20.170.179.179, Ethernet49/1
 I L2     10.0.0.212/32 [115/10]
           via 20.170.212.212, Ethernet49/2
 I L2     10.0.1.43/32 [115/21]
           via 20.57.170.57, Ethernet45
 I L2     10.0.1.49/32 [115/11]
           via 20.57.170.57, Ethernet45
 I L2     10.0.1.55/32 [115/20]
           via 20.155.170.155, Ethernet51/1
 I L2     20.5.149.0/24 [115/20]
           via 20.5.170.5, Ethernet50/1
 C        20.5.170.0/24
           directly connected, Ethernet50/1
 I L2     20.19.149.0/24 [115/20]
           via 20.19.170.19, Ethernet25
 C        20.19.170.0/24
           directly connected, Ethernet25
 I L2     20.24.149.0/24 [115/21]
           via 20.57.170.57, Ethernet45
 C        20.24.170.0/24
           directly connected, Ethernet53/1
 I L2     20.24.238.0/24 [115/31]
           via 20.57.170.57, Ethernet45
 I L2     20.32.149.0/24 [115/21]
           via 20.57.170.57, Ethernet45
 I L2     20.32.155.0/24 [115/30]
           via 20.155.170.155, Ethernet51/1
 C        20.32.170.0/24
           directly connected, Ethernet43
 I L2     20.57.149.0/24 [115/11]
           via 20.57.170.57, Ethernet45
 I L2     20.57.155.0/24 [115/30]
           via 20.155.170.155, Ethernet51/1
 C        20.57.170.0/24
           directly connected, Ethernet45
 I L2     20.111.149.0/24 [115/21]
           via 20.57.170.57, Ethernet45
 I L2     20.143.149.0/24 [115/21]
           via 20.57.170.57, Ethernet45
 I L2     20.149.155.0/24 [115/21]
           via 20.57.170.57, Ethernet45
 I L2     20.149.171.0/24 [115/21]
           via 20.170.171.171, Ethernet1
           via 20.57.170.57, Ethernet45
 I L2     20.149.179.0/24 [115/21]
           via 20.57.170.57, Ethernet45
 C        20.155.170.0/24
           directly connected, Ethernet51/1
 C        20.170.171.0/24
           directly connected, Ethernet1
 C        20.170.179.0/24
           directly connected, Ethernet49/1
 C        20.170.212.0/24
           directly connected, Ethernet49/2
 I L2     30.155.179.0/24 [115/20]
           via 20.170.179.179, Ethernet49/1
 I L2     31.9.1.0/24 [115/10]
           via 20.19.170.19, Ethernet25
 I L2     192.168.0.0/19 [115/10]
           via 20.19.170.19, Ethernet25
 I L2     209.209.209.209/32 [115/10]
           via 20.170.179.179, Ethernet49/1


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
MPLS forwarding table (Label [metric] Vias) - 31 routes 
MPLS next-hop resolution allow default route: False
Metric Codes:
          A - Active metric
Via Type Codes:
          M - MPLS via, P - Pseudowire via,
          I - IP lookup via, V - VLAN via,
          VA - EVPN VLAN aware via, ES - EVPN ethernet segment via,
          VF - EVPN VLAN flood via, AF - EVPN VLAN aware flood via,
          NG - Nexthop group via

 20005   A[1]
                via M, ::, forward
                    EgressACL: apply
                  via TI-LFA tunnel index 3
                    via 20.5.170.5, Ethernet50/1, label imp-null(3)
                    backup via 20.57.170.57, Ethernet45, label 20349
 20019   A[1]
                via M, ::, pop
                    EgressACL: apply
                  via TI-LFA tunnel index 1
                    via 20.19.170.19, Ethernet25, label imp-null(3)
                    backup via 20.57.170.57, Ethernet45, label 20349 20019
 20024   A[1]
                via M, ::, forward
                    EgressACL: apply
                  via TI-LFA tunnel index 12
                    via 20.57.170.57, Ethernet45, label imp-null(3)
                    backup via 20.19.170.19, Ethernet25, label imp-null(3)
 20032   A[1]
                via M, ::, pop
                    EgressACL: apply
                  via TI-LFA tunnel index 4
                    via 20.32.170.32, Ethernet43, label imp-null(3)
                    backup via 20.57.170.57, Ethernet45, label 20032
 20057   A[1]
                via M, ::, forward
                    EgressACL: apply
                  via TI-LFA tunnel index 15
                    via 20.57.170.57, Ethernet45, label imp-null(3)
                    backup via 20.19.170.19, Ethernet25, label 20349
 20171   A[1]
                via M, ::, pop
                    EgressACL: apply
                  via TI-LFA tunnel index 17
                    via 20.170.171.171, Ethernet1, label imp-null(3)
                    backup via 20.57.170.57, Ethernet45, label 20349 20171
 20209   A[1]
                via M, ::, pop
                    EgressACL: apply
                  via TI-LFA tunnel index 0
                    via 20.170.179.179, Ethernet49/1, label imp-null(3)
                    backup via 20.155.170.155, Ethernet51/1, label imp-null(3)
 20212   A[1]
                via M, 20.170.212.212, swap 0
                    EgressACL: apply
                    directly connected, Ethernet49/2
                    68:22:8e:16:e3:10, vlan 1016
 20343   A[1]
                via M, ::, forward
                    EgressACL: apply
                  via TI-LFA tunnel index 12
                    via 20.57.170.57, Ethernet45, label imp-null(3)
                    backup via 20.19.170.19, Ethernet25, label imp-null(3)
 20349   A[1]
                via M, ::, forward
                    EgressACL: apply
                  via TI-LFA tunnel index 12
                    via 20.57.170.57, Ethernet45, label imp-null(3)
                    backup via 20.19.170.19, Ethernet25, label imp-null(3)
 20355   A[1]
                via M, ::, pop
                    EgressACL: apply
                  via TI-LFA tunnel index 13
                    via 20.155.170.155, Ethernet51/1, label imp-null(3)
                    backup via 20.57.170.57, Ethernet45, label 20355
 20379   A[1]
                via M, ::, pop
                    EgressACL: apply
                  via TI-LFA tunnel index 5
                    via 20.170.179.179, Ethernet49/1, label imp-null(3)
                    backup via 20.57.170.57, Ethernet45, label 20349 20379
 21271   A[1]
                via M, pop
                    EgressACL: apply
                    20.170.171.171 Ethernet1
 21371   A[1]
                via M, ::, pop
                    EgressACL: apply
                  via TI-LFA tunnel index 2
                    via 20.170.171.171, Ethernet1, label imp-null(3)
                    backup via 20.155.170.155, Ethernet51/1, label 21549 21371
 21379   A[1]
                via M, ::, pop
                    EgressACL: apply
                  via TI-LFA tunnel index 8
                    via 20.170.179.179, Ethernet49/1, label imp-null(3)
                    backup via 20.170.171.171, Ethernet1, label 21379
 21449   A[1]
                via M, forward
                    EgressACL: apply
                    20.170.171.171 Ethernet1
 21455   A[1]
                via M, forward
                    EgressACL: apply
                    20.170.171.171 Ethernet1
 21471   A[1]
                via M, pop
                    EgressACL: apply
                    20.170.171.171 Ethernet1
 21549   A[1]
                via M, ::, forward
                    EgressACL: apply
                  via TI-LFA tunnel index 10
                    via 20.170.171.171, Ethernet1, label imp-null(3)
                    backup via 20.155.170.155, Ethernet51/1, label imp-null(3)
 21555   A[1]
                via M, ::, pop
                    EgressACL: apply
                  via TI-LFA tunnel index 9
                    via 20.155.170.155, Ethernet51/1, label imp-null(3)
                    backup via 20.170.171.171, Ethernet1, label 21555
 21649   A[1]
                via M, forward
                    EgressACL: apply
                    20.155.170.155 Ethernet51/1
 21655   A[1]
                via M, pop
                    EgressACL: apply
                    20.155.170.155 Ethernet51/1
 362144  A[1]
                via M, 20.155.170.155, pop
                    EgressACL: apply
                    directly connected, Ethernet51/1
                    34:88:18:bf:4a:3c, vlan 1011
 362149  A[1]
                via M, 20.170.212.212, pop
                    EgressACL: apply
                    directly connected, Ethernet49/2
                    68:22:8e:16:e3:10, vlan 1016
 362152  A[1]
                via M, 20.32.170.32, pop
                    EgressACL: apply
                    directly connected, Ethernet43
                    30:c5:07:1f:33:09, vlan 1010
 362153  A[1]
                via M, 20.5.170.5, pop
                    EgressACL: apply
                    directly connected, Ethernet50/1
                    e4:6d:7f:d7:36:04, vlan 1007
 362154  A[1]
                via M, 20.24.170.24, pop
                    EgressACL: apply
                    directly connected, Ethernet53/1
                    6c:87:20:89:ed:81, vlan 1017
 362156  A[1]
                via M, 20.170.171.171, pop
                    EgressACL: apply
                    directly connected, Ethernet1
                    2c:dd:e9:96:1a:b3, vlan 1006
 362158  A[1]
                via M, 20.19.170.19, pop
                    EgressACL: apply
                    directly connected, Ethernet25
                    c4:07:78:58:80:99, vlan 1018
 362163  A[1]
                via M, 20.57.170.57, pop
                    EgressACL: apply
                    directly connected, Ethernet45
                    c0:14:b8:21:ca:74, vlan 1015
 362291  A[1]
                via M, 20.170.179.179, pop
                    EgressACL: apply
                    directly connected, Ethernet49/1
                    60:c7:8d:2d:3c:c7, vlan 1012
```

## show mpls lfib route

```text
MPLS forwarding table (Label [metric] Vias) - 31 routes 
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

 IP    20005    [1], 10.0.0.5/32
                via TI-LFA tunnel index 3, forward
                 payload autoDecide, ttlMode uniform, dscpMode uniform, apply egress-acl
                    via 20.5.170.5, Ethernet50/1, label imp-null(3)
                    backup via 20.57.170.57, Ethernet45, label 20349
 IP    20019    [1], 10.0.0.19/32
                via TI-LFA tunnel index 1, pop
                 payload autoDecide, ttlMode uniform, dscpMode uniform, apply egress-acl
                    via 20.19.170.19, Ethernet25, label imp-null(3)
                    backup via 20.57.170.57, Ethernet45, label 20349 20019
 IP    20024    [1], 10.0.0.24/32
                via TI-LFA tunnel index 12, forward
                 payload autoDecide, ttlMode uniform, dscpMode uniform, apply egress-acl
                    via 20.57.170.57, Ethernet45, label imp-null(3)
                    backup via 20.19.170.19, Ethernet25, label imp-null(3)
 IP    20032    [1], 10.0.0.32/32
                via TI-LFA tunnel index 4, pop
                 payload autoDecide, ttlMode uniform, dscpMode uniform, apply egress-acl
                    via 20.32.170.32, Ethernet43, label imp-null(3)
                    backup via 20.57.170.57, Ethernet45, label 20032
 IP    20057    [1], 10.0.0.57/32
                via TI-LFA tunnel index 15, forward
                 payload autoDecide, ttlMode uniform, dscpMode uniform, apply egress-acl
                    via 20.57.170.57, Ethernet45, label imp-null(3)
                    backup via 20.19.170.19, Ethernet25, label 20349
 IP    20171    [1], 10.0.0.171/32
                via TI-LFA tunnel index 17, pop
                 payload autoDecide, ttlMode uniform, dscpMode uniform, apply egress-acl
                    via 20.170.171.171, Ethernet1, label imp-null(3)
                    backup via 20.57.170.57, Ethernet45, label 20349 20171
 IP    20209    [1], 209.209.209.209/32
                via TI-LFA tunnel index 0, pop
                 payload autoDecide, ttlMode uniform, dscpMode uniform, apply egress-acl
                    via 20.170.179.179, Ethernet49/1, label imp-null(3)
                    backup via 20.155.170.155, Ethernet51/1, label imp-null(3)
 IP    20212    [1], 10.0.0.212/32
                via M, 20.170.212.212, swap 0
                 payload autoDecide, ttlMode uniform, apply egress-acl
                 interface Ethernet49/2
 IP    20343    [1], 10.0.1.43/32
                via TI-LFA tunnel index 12, forward
                 payload autoDecide, ttlMode uniform, dscpMode uniform, apply egress-acl
                    via 20.57.170.57, Ethernet45, label imp-null(3)
                    backup via 20.19.170.19, Ethernet25, label imp-null(3)
 IP    20349    [1], 10.0.1.49/32
                via TI-LFA tunnel index 12, forward
                 payload autoDecide, ttlMode uniform, dscpMode uniform, apply egress-acl
                    via 20.57.170.57, Ethernet45, label imp-null(3)
                    backup via 20.19.170.19, Ethernet25, label imp-null(3)
 IP    20355    [1], 10.0.1.55/32
                via TI-LFA tunnel index 13, pop
                 payload autoDecide, ttlMode uniform, dscpMode uniform, apply egress-acl
                    via 20.155.170.155, Ethernet51/1, label imp-null(3)
                    backup via 20.57.170.57, Ethernet45, label 20355
 IP    20379    [1], 10.0.0.179/32
                via TI-LFA tunnel index 5, pop
                 payload autoDecide, ttlMode uniform, dscpMode uniform, apply egress-acl
                    via 20.170.179.179, Ethernet49/1, label imp-null(3)
                    backup via 20.57.170.57, Ethernet45, label 20349 20379
 IP    21271    [1], 10.0.0.171/32, algorithm MIN-TE
                via M, 20.170.171.171, pop
                 payload autoDecide, ttlMode uniform, dscpMode uniform, apply egress-acl
                 interface Ethernet1
 IP    21371    [1], 10.0.0.171/32, algorithm MIN-IGP
                via TI-LFA tunnel index 2, pop
                 payload autoDecide, ttlMode uniform, dscpMode uniform, apply egress-acl
                    via 20.170.171.171, Ethernet1, label imp-null(3)
                    backup via 20.155.170.155, Ethernet51/1, label 21549 21371
 IP    21379    [1], 10.0.0.179/32, algorithm MIN-IGP
                via TI-LFA tunnel index 8, pop
                 payload autoDecide, ttlMode uniform, dscpMode uniform, apply egress-acl
                    via 20.170.179.179, Ethernet49/1, label imp-null(3)
                    backup via 20.170.171.171, Ethernet1, label 21379
 IP    21449    [1], 10.0.1.49/32, algorithm MIN-TE
                via M, 20.170.171.171, forward
                 payload autoDecide, ttlMode uniform, dscpMode uniform, apply egress-acl
                 interface Ethernet1
 IP    21455    [1], 10.0.1.55/32, algorithm MIN-TE
                via M, 20.170.171.171, forward
                 payload autoDecide, ttlMode uniform, dscpMode uniform, apply egress-acl
                 interface Ethernet1
 IP    21471    [1], 10.0.0.171/32, algorithm MIN-IGP-ADMIN
                via M, 20.170.171.171, pop
                 payload autoDecide, ttlMode uniform, dscpMode uniform, apply egress-acl
                 interface Ethernet1
 IP    21549    [1], 10.0.1.49/32, algorithm MIN-IGP
                via TI-LFA tunnel index 10, forward
                 payload autoDecide, ttlMode uniform, dscpMode uniform, apply egress-acl
                    via 20.170.171.171, Ethernet1, label imp-null(3)
                    backup via 20.155.170.155, Ethernet51/1, label imp-null(3)
 IP    21555    [1], 10.0.1.55/32, algorithm MIN-IGP
                via TI-LFA tunnel index 9, pop
                 payload autoDecide, ttlMode uniform, dscpMode uniform, apply egress-acl
                    via 20.155.170.155, Ethernet51/1, label imp-null(3)
                    backup via 20.170.171.171, Ethernet1, label 21555
 IP    21649    [1], 10.0.1.49/32, algorithm MIN-IGP-ADMIN
                via M, 20.155.170.155, forward
                 payload autoDecide, ttlMode uniform, dscpMode uniform, apply egress-acl
                 interface Ethernet51/1
 IP    21655    [1], 10.0.1.55/32, algorithm MIN-IGP-ADMIN
                via M, 20.155.170.155, pop
                 payload autoDecide, ttlMode uniform, dscpMode uniform, apply egress-acl
                 interface Ethernet51/1
 IA    362144   [1]
                via M, 20.155.170.155, pop
                 payload autoDecide, ttlMode uniform, apply egress-acl
                 interface Ethernet51/1
 IA    362149   [1]
                via M, 20.170.212.212, pop
                 payload autoDecide, ttlMode uniform, apply egress-acl
                 interface Ethernet49/2
 IA    362152   [1]
                via M, 20.32.170.32, pop
                 payload autoDecide, ttlMode uniform, apply egress-acl
                 interface Ethernet43
 IA    362153   [1]
                via M, 20.5.170.5, pop
                 payload autoDecide, ttlMode uniform, apply egress-acl
                 interface Ethernet50/1
 IA    362154   [1]
                via M, 20.24.170.24, pop
                 payload autoDecide, ttlMode uniform, apply egress-acl
                 interface Ethernet53/1
 IA    362156   [1]
                via M, 20.170.171.171, pop
                 payload autoDecide, ttlMode uniform, apply egress-acl
                 interface Ethernet1
 IA    362158   [1]
                via M, 20.19.170.19, pop
                 payload autoDecide, ttlMode uniform, apply egress-acl
                 interface Ethernet25
 IA    362163   [1]
                via M, 20.57.170.57, pop
                 payload autoDecide, ttlMode uniform, apply egress-acl
                 interface Ethernet45
 IA    362291   [1]
                via M, 20.170.179.179, pop
                 payload autoDecide, ttlMode uniform, apply egress-acl
                 interface Ethernet49/1
```

## show ip ospf segment-routing

```text
```

## show ip ospf segment-routing global-blocks

```text
```

## show ip ospf segment-routing bindings

```text
```

## show bgp evpn

```text
BGP routing table information for VRF default
Router identifier 10.0.0.170, local AS number 1
Route status codes: * - valid, > - active, S - Stale, E - ECMP head, e - ECMP
                    c - Contributing to ECMP, % - Pending best path selection
Origin codes: i - IGP, e - EGP, ? - incomplete
AS Path Attributes: Or-ID - Originator ID, C-LST - Cluster List, LL Nexthop - Link Local Nexthop

          Network                Next Hop              Metric  LocPref Weight  Path
```

## show bgp vpn-ipv4

```text
BGP routing table information for VRF default
Router identifier 10.0.0.170, local AS number 1
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
Router identifier 10.0.0.170, local AS number 1
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
Router identifier 10.0.0.170, local AS number 1
Route status codes: s - suppressed contributor, * - valid, > - active, E - ECMP head, e - ECMP
                    S - Stale, c - Contributing to ECMP, b - backup, L - labeled-unicast
                    % - Pending best path selection
Origin codes: i - IGP, e - EGP, ? - incomplete
AS Path Attributes: Or-ID - Originator ID, C-LST - Cluster List, LL Nexthop - Link Local Nexthop

          Network                Next Hop              Metric  AIGP       LocPref Weight  Path
```

## show bgp neighbors

```text
```

## show tunnel rib system-tunnel-rib brief

```text
Tunnel RIB: system-tunnel-rib
Endpoint           Tunnel Type    Index(es)  Tunnel Preference  IGP Preference 
------------------ -------------- ---------- ------------------ ---------------
10.0.0.5/32        IS-IS SR IPv4  11         65                 115            
10.0.0.19/32       IS-IS SR IPv4  12         65                 115            
10.0.0.24/32       IS-IS SR IPv4  16         65                 115            
10.0.0.32/32       IS-IS SR IPv4  10         65                 115            
10.0.0.57/32       IS-IS SR IPv4  4          65                 115            
10.0.0.171/32      IS-IS SR IPv4  17         65                 115            
10.0.0.179/32      IS-IS SR IPv4  8          65                 115            
10.0.0.212/32      IS-IS SR IPv4  7          65                 115            
10.0.1.43/32       IS-IS SR IPv4  14         65                 115            
10.0.1.49/32       IS-IS SR IPv4  13         65                 115            
10.0.1.55/32       IS-IS SR IPv4  1          65                 115            
209.209.209.209/32 IS-IS SR IPv4  2          65                 115            

   IGP Metric    Metric Type
---------------- -----------
   10            metric     
   10            metric     
   21            metric     
   12            metric     
   1             metric     
   10            metric     
   10            metric     
   10            metric     
   21            metric     
   11            metric     
   20            metric     
   10            metric     

```

## show tunnel rib colored brief

```text
Tunnel RIB: system-colored-tunnel-rib
 Endpoint        Color   Tunnel Type       Index(es)    Tunnel Preference    IGP Preference    IGP Metric   Metric Type
--------------- ------- ----------------- ------------ -------------------- ----------------- ------------- -----------
 10.0.0.171/32   129     IS-IS FlexAlgo    8            65                   115               10           metric     
 10.0.0.171/32   130     IS-IS FlexAlgo    7            65                   115               10           metric     
 10.0.0.171/32   131     IS-IS FlexAlgo    9            65                   115               10           metric     
 10.0.0.179/32   130     IS-IS FlexAlgo    5            65                   115               10           metric     
 10.0.1.49/32    129     IS-IS FlexAlgo    6            65                   115               22           metric     
 10.0.1.49/32    130     IS-IS FlexAlgo    4            65                   115               21           metric     
 10.0.1.49/32    131     IS-IS FlexAlgo    3            65                   115               30           metric     
 10.0.1.55/32    129     IS-IS FlexAlgo    10           65                   115               34           metric     
 10.0.1.55/32    130     IS-IS FlexAlgo    1            65                   115               20           metric     
 10.0.1.55/32    131     IS-IS FlexAlgo    2            65                   115               20           metric     

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
>C    10.0.0.170/32 [0 pref/0 metric] updated 2d17h ago
         via Loopback0, directly connected
>C    20.5.170.0/24 [0 pref/0 metric] updated 14:34:33 ago
         via Ethernet50/1, directly connected
>C    20.19.170.0/24 [0 pref/0 metric] updated 1d19h ago
         via Ethernet25, directly connected
>C    20.24.170.0/24 [0 pref/0 metric] updated 16:47:35 ago
         via Ethernet53/1, directly connected
>C    20.32.170.0/24 [0 pref/0 metric] updated 16:01:08 ago
         via Ethernet43, directly connected
>C    20.57.170.0/24 [0 pref/0 metric] updated 2d17h ago
         via Ethernet45, directly connected
>C    20.155.170.0/24 [0 pref/0 metric] updated 2d17h ago
         via Ethernet51/1, directly connected
>C    20.170.171.0/24 [0 pref/0 metric] updated 1d21h ago
         via Ethernet1, directly connected
>C    20.170.179.0/24 [0 pref/0 metric] updated 1d15h ago
         via Ethernet49/1, directly connected
>C    20.170.212.0/24 [0 pref/0 metric] updated 20:37:37 ago
         via Ethernet49/2, directly connected
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
>P    0.0.0.0/8 [1 pref/0 metric] updated 2d17h ago
         via Null0, directly connected [NF]
>P    127.0.0.0/8 [1 pref/0 metric] updated 2d17h ago
         via :: [1 pref/1 metric] type ipv4
            via , directly connected
VRF: default, Protocol: isis
Codes: C - Connected, S - Static, P - Route Input, G - Gribi
       B - BGP, O - Ospf, O3 - Ospf3, I - Isis, R - Rip, VL - VRF Leak
       > - Best Route, * - Unresolved Next hop
       EM - Exact match of the SR-TE Policy
       NM - Null endpoint match of the SR-TE Policy
       AM - Any endpoint match of the SR-TE Policy
       L - Part of a recursive route resolution loop
       A - Next hop not resolved in ARP/ND
       NF - Not in FEC
>I    10.0.0.5/32 [115 pref/10 metric] updated 14:34:31 ago
         via 20.5.170.5, Ethernet50/1
>I    10.0.0.19/32 [115 pref/10 metric] updated 1d19h ago
         via 20.19.170.19, Ethernet25
>I    10.0.0.24/32 [115 pref/21 metric] updated 16:53:53 ago
         via 20.57.170.57, Ethernet45
>I    10.0.0.32/32 [115 pref/12 metric] updated 16:00:16 ago
         via 20.32.170.32, Ethernet43
>I    10.0.0.57/32 [115 pref/1 metric] updated 1d16h ago
         via 20.57.170.57, Ethernet45
>I    10.0.0.171/32 [115 pref/10 metric] updated 1d21h ago
         via 20.170.171.171, Ethernet1
>I    10.0.0.179/32 [115 pref/10 metric] updated 17:27:08 ago
         via 20.170.179.179, Ethernet49/1
>I    10.0.0.212/32 [115 pref/10 metric] updated 20:37:29 ago
         via 20.170.212.212, Ethernet49/2
>I    10.0.1.43/32 [115 pref/21 metric] updated 22:45:57 ago
         via 20.57.170.57, Ethernet45
>I    10.0.1.49/32 [115 pref/11 metric] updated 22:45:57 ago
         via 20.57.170.57, Ethernet45
>I    10.0.1.55/32 [115 pref/20 metric] updated 1d21h ago
         via 20.155.170.155, Ethernet51/1
>I    20.5.149.0/24 [115 pref/20 metric] updated 14:34:31 ago
         via 20.5.170.5, Ethernet50/1
>I    20.19.149.0/24 [115 pref/20 metric] updated 1d19h ago
         via 20.19.170.19, Ethernet25
>I    20.24.149.0/24 [115 pref/21 metric] updated 16:53:53 ago
         via 20.57.170.57, Ethernet45
 I    20.24.170.0/24 [115 pref/31 metric] updated 16:46:29 ago
         via 20.57.170.57, Ethernet45
>I    20.24.238.0/24 [115 pref/31 metric] updated 15:54:28 ago
         via 20.57.170.57, Ethernet45
>I    20.32.149.0/24 [115 pref/21 metric] updated 16:01:11 ago
         via 20.57.170.57, Ethernet45
>I    20.32.155.0/24 [115 pref/30 metric] updated 1d21h ago
         via 20.155.170.155, Ethernet51/1
>I    20.57.149.0/24 [115 pref/11 metric] updated 22:45:57 ago
         via 20.57.170.57, Ethernet45
>I    20.57.155.0/24 [115 pref/30 metric] updated 1d21h ago
         via 20.155.170.155, Ethernet51/1
>I    20.111.149.0/24 [115 pref/21 metric] updated 22:45:57 ago
         via 20.57.170.57, Ethernet45
>I    20.143.149.0/24 [115 pref/21 metric] updated 22:45:57 ago
         via 20.57.170.57, Ethernet45
>I    20.149.155.0/24 [115 pref/21 metric] updated 22:45:57 ago
         via 20.57.170.57, Ethernet45
>I    20.149.171.0/24 [115 pref/21 metric] updated 18:55:39 ago
         via 20.57.170.57, Ethernet45
         via 20.170.171.171, Ethernet1
>I    20.149.179.0/24 [115 pref/21 metric] updated 22:45:57 ago
         via 20.57.170.57, Ethernet45
>I    30.155.179.0/24 [115 pref/20 metric] updated 16:17:24 ago
         via 20.170.179.179, Ethernet49/1
>I    31.9.1.0/24 [115 pref/10 metric] updated 1d19h ago
         via 20.19.170.19, Ethernet25
>I    192.168.0.0/19 [115 pref/10 metric] updated 1d19h ago
         via 20.19.170.19, Ethernet25
>I    209.209.209.209/32 [115 pref/10 metric] updated 17:27:08 ago
         via 20.170.179.179, Ethernet49/1
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
>P    ::/96 [1 pref/0 metric] updated 2d17h ago
         via Null0, directly connected [NF]
>P    ::ffff:127.0.0.0/104 [1 pref/0 metric] updated 2d17h ago
         via :: [1 pref/1 metric] type ipv6
            via , directly connected
>P    fe80::/10 [1 pref/0 metric] updated 2d17h ago
```

## show platform sand l3 summary

```text
Number of vrfs: 2

Ipv4:
  Routes:       84  backlog:  0  unprogrammed:  0
  Adjacencies:  81  backlog:  0  unprogrammed:  0
Ipv6:
  Routes:       4   backlog:  0  unprogrammed:  0
  Adjacencies:  81  backlog:  0  unprogrammed:  0
Mpls:
  Routes:       31  backlog:  0  unprogrammed:  0
  Adjacencies:  10  backlog:  0  unprogrammed:  0

Jericho Ip Fecs:
  Non-ecmp fecs:  4131  ecmp fecs:  1  fec entries:  4133
Jericho Mpls Fecs:
  Non-ecmp fecs:  10  ecmp fecs:  0  fec entries:  10
Jericho Vxlan Overlay Fecs:
  Non-ecmp fecs:  0  ecmp fecs:  0  fec entries:  0
Jericho Vxlan Tunnel Fecs:
  Non-ecmp fecs:  0  ecmp fecs:  0  fec entries:  0
  Number of vxlan tunnels configured: 0

Jericho Lpm Routes:
  Routes:   75  unprogrammed:   0   
  Routes6:  4   unprogrammed6:  0   
  Backlog:  0 

Jericho Lpm:
  TCAM pivots used:  3   Percent free:  99
  Buckets used:      14  Rows used:     2   Entries Per Bucket:  5     Percent free:  99  

Lem:
  IPv4  Host in Lem:            enabled
  IPv4  Hosts:                  9      
  IPv4  Prefix-lengths in Lem:  None   
  IPv6  Host in Lem:            enabled
  IPv6  Hosts:                  0      
  IPv6  Prefix-lengths in Lem:  None   
  Number of downloads:        0
  Number of overflow events:  0

Ipv6 Host Tcam Status:
  Compression Tcam banks:             None
  Number of host routes:              0   
  Number of compression map entries:  0   

  Arp Egress Banks in use:                        0   
  Arp Remote Egress Banks in use:                 None
  Ip tunnel Egress Banks in use:                  None
  MPLS (for outer 2 labels) Egress Banks in use:  None
  MPLS (for inner 2 labels) Egress Banks in use:  1,3 
  SVI egress counters Egress Banks in use:        None
  

Egress Arp rewrite entries in use (in each fap):
  FixedSystem: 17
Egress Arp remote rewrite entries in use (in each fap):
  FixedSystem: 0
Egress Ip tunnel rewrite entries in use (in each fap):
  FixedSystem: 0
Egress Mpls (for outer 2 labels) rewrite entries in use (in each fap):
  FixedSystem: 0
Egress Mpls (for inner 2 labels) rewrite entries in use (in each fap):
  FixedSystem: 14
Egress Sflow rewrite entries in use (in each fap):
  FixedSystem: 0

Egress rewrite chains in backlog: resource-full 0, no-interface 0

Glem is disabled

Route Update State:
  v4 route update suspended:  False
  v6 route update suspended:  False

Jericho Fec:
  Maximum FEC hierarchy levels:  2
  Used:                     45  ecmp:                 2   reusedEcmp:  6     allocs:  1420  frees:  1376  shuffles:  0     cmds:  0   
  Non-ecmp (Percent free):  99  ecmp (Percent free):  99
  Zombies:     0    purges:    0
  Quarantine:  0/6  shuffles:  1  deletes:  6   
  Fec insertion failures:  0
  Banks in use (level, used, Percent free):
     2 (2, 45, 99%)

Lpm Detail:
  Requests:  22424  cleanses:  1781  batches:  1781  avg batch size:  12

Lem Cmds:
  Adds:  1343  dels:  1303  mods:  4797  fails:  0  cmds:  7443

Ipv6 Host Routes Status Detail
  Number of host route add:              0
  Number of host route del:              0
  Number of host compression map add:    0
  Number of host compression map del:    0
  Number of host tcam entry add:         0
  Number of host tcam entry del:         0
  Number of host lem entry add:          0
  Number of host lem entry del:          0
  Number of host tcam bank alloc req:    0
  Number of host tcam bank release req:  0
  Number of host routes recovered after restart:           0
  Number of host compression map recovered after restart:  0

Jericho Arp:
  ArpTable writes:      1938   queued      0   
  IngressTable writes:  25677  queued      0   
  Coprocessors:         1      in CmdRing

TopBank To EedbBank Mapping:
None

Tunnel Counter Status
  Number of MPLS tunnels:                  14   
  Number of uncountable MPLS tunnels:      1    
  Number of MPLSoGRE tunnels:              0    
  Number of uncountable MPLSoGRE tunnels:  0    
  Number of IP tunnels:                    0    
  Number of uncountable IP tunnels:        0    
  Shuffle tunnel enabled:                  False
```

## show platform jericho2 ip route

```text
There are no active FAPs of the specified type.
```

## show platform jericho2 fec all

```text
There are no active FAPs of the specified type.
```

