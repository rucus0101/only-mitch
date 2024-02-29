# Test results for PE32-J2-171

## show version

```text
Arista DCS-7280SR3K-48YC8-F
Hardware version: 11.02
Serial number: JPE21241259
Hardware MAC address: 2cdd.e996.1ab3
System MAC address: 2cdd.e996.1ab3

Software image version: 4.31.2F-35649835.comcasteftfeb24 (engineering build)
Architecture: x86_64
Internal build version: 4.31.2F-35649835.comcasteftfeb24
Internal build ID: 99d2ae30-8d92-4936-8f11-3c8d90acdcf0
Image format version: 3.0
Image optimization: Default

Uptime: 1 day, 22 hours and 21 minutes
Total memory: 65734516 kB
Free memory: 61592092 kB

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
Interface       IP Address          Status       Protocol         MTU   Owner  
--------------- ------------------- ------------ ------------- -------- -------
Ethernet1       20.170.171.171/24   up           up              1500          
Ethernet5.128   20.111.171.171/24   up           up              1500          
Ethernet5.129   20.111.171.171/24   up           up              1500          
Ethernet5.130   20.111.171.171/24   up           up              1500          
Ethernet5.131   20.111.171.171/24   up           up              1500          
Ethernet5.209   20.111.171.171/24   up           up              1500          
Ethernet7       20.32.171.171/24    down         down            1500          
Ethernet9       20.171.254.171/24   admin down   down            1500          
Ethernet24      20.149.171.171/24   up           up              1500          
Ethernet25      20.171.179.171/24   admin down   down            1500          
Ethernet46      20.155.171.171/24   admin down   down            1500          
Ethernet47      20.171.172.171/24   down         down            1500          
Loopback0       10.0.0.171/32       up           up             65535          
Management1     192.168.20.171/23   up           up              1500          

```

## show interfaces counters rates | nz

```text
Port      Name             Intvl  In Mbps      %  In Kpps Out Mbps      %
Et24      Cisco_Spine_349   0:01      0.1   0.0%        0      0.0   0.0%
Ma1                         0:01      0.0   0.0%        0      0.2   0.0%

Port      Out Kpps
```

## show isis neighbors

```text
 
Instance  VRF      System Id        Type Interface          SNPA              State Hold time   Circuit Id          
IGP       default  h49-N540-24Q8L2DD L2   Ethernet24         P2P               UP    26          00                  
IGP       default  Spine3-J-170     L2   Ethernet1          P2P               UP    22          40                  
```

## show isis database detail

```text
Legend:
H - hostname conflict
U - node unreachable

IS-IS Instance: IGP VRF: default
  IS-IS Level 2 Link State Database
    LSPID                   Seq Num  Cksum  Life Length IS  Received LSPID        Flags
    h3c_19_CR16010E-F.00-00      1129  29209  1142    411 L2  0000.0000.0019.00-00  <>
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
    h3c_24_S12500R-48C6D.00-00       772  18538   647    421 L2  0000.0000.0024.00-00  <>
      NLPID: 0xCC(IPv4)
      Hostname: h3c_24_S12500R-48C6D
      Area addresses: 49
      Interface address: 10.0.0.24
      Interface address: 20.24.149.24
      Interface address: 20.24.170.24
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
      Router Capabilities: Router Id: 10.0.0.24 Flags: []
        SR Local Block:
          SRLB Base: 15000 Range: 1000
        Maximum SID depth:
          Base MPLS imposition (MSD type 1):  10
        SR Capability: Flags: [I]
          SRGB Base: 20000 Range: 2000
    Ribbon-32.00-00             212  47334   501     79 L2  0000.0000.0032.00-00  <>
      Remaining lifetime received: 1199 s Modified to: 1200 s
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
    Ribbon-32.00-01             211  63354  1129     38 L2  0000.0000.0032.00-01  <>
      Hostname: Ribbon-32
    Ribbon-32.00-02             230  12946   473    421 L2  0000.0000.0032.00-02  <>
      Interface address: 20.32.149.32
      Interface address: 20.32.170.32
      Interface address: 10.0.0.32
      Interface address: 20.32.179.32
      IS Neighbor          : h49-N540-24Q8L2DD.00 Metric: 10
        IPv4 Neighbor Address: 20.32.149.149
        IPv4 Interface Address: 20.32.149.32
        Adj-sid: 756644 flags: [L V] weight: 0x0
        Adj-sid: 756645 flags: [L V B] weight: 0x0
      IS Neighbor          : Spine3-J-170.00     Metric: 11
        IPv4 Neighbor Address: 20.32.170.170
        IPv4 Interface Address: 20.32.170.32
        Adj-sid: 756646 flags: [L V] weight: 0x0
        Adj-sid: 756647 flags: [L V B] weight: 0x0
      IS Neighbor          : juniper_379_MX304.00 Metric: 10
        IPv4 Neighbor Address: 20.32.179.179
        IPv4 Interface Address: 20.32.179.32
        Adj-sid: 756641 flags: [L V] weight: 0x0
        Adj-sid: 756643 flags: [L V B] weight: 0x0
      Reachability         : 20.32.149.0/24 Metric: 10 Type: 1 Up
      Reachability         : 20.32.170.0/24 Metric: 11 Type: 1 Up
      Reachability         : 10.0.0.32/32 Metric: 0 Type: 1 Up
        SR Prefix-SID: 32 Flags: [N] Algorithm: 0
      Reachability         : 20.32.179.0/24 Metric: 10 Type: 1 Up
 U  R6676-50.00-00              244  36733   433    145 L2  0000.0000.0050.00-00  <>
      NLPID: 0xCC(IPv4)
      Hostname: R6676-50
      Area addresses: 49.0000
      Interface address: 10.0.0.50
      IS Neighbor          : h49-N540-24Q8L2DD.00 Metric: 10
        IPv4 Interface Address: 20.50.149.50
      Reachability         : 10.0.0.50/32 Metric: 10 Type: 1 Up
        SR Prefix-SID: 50 Flags: [N P] Algorithm: 0
      Reachability         : 20.50.149.0/24 Metric: 10 Type: 1 Up
      Router Capabilities: Router Id: 10.0.0.50 Flags: []
        Maximum SID depth:
          Base MPLS imposition (MSD type 1):  8
        SR Capability: Flags: [I]
          SRGB Base: 20000 Range: 2000
        Algorithms:  0
    huawei_254_NetEngine_8000_F8.00-00       154  53642  1126    216 L2  0000.0000.0254.00-00  <>
      Remaining lifetime received: 1199 s Modified to: 1200 s
      NLPID: 0xCC(IPv4)
      Hostname: huawei_254_NetEngine_8000_F8
      Area addresses: 49
      Interface address: 10.0.0.254
      Interface address: 20.149.254.254
      Interface address: 20.170.254.254
      IS Neighbor          : h49-N540-24Q8L2DD.00 Metric: 10
        IPv4 Neighbor Address: 20.149.254.149
        IPv4 Interface Address: 20.149.254.254
        Adj-sid: 48030 flags: [L V] weight: 0x0
      IS Neighbor          : Spine3-J-170.00     Metric: 10
        IPv4 Neighbor Address: 20.170.254.170
        IPv4 Interface Address: 20.170.254.254
        Adj-sid: 48032 flags: [L V] weight: 0x0
      Reachability         : 10.0.0.254/32 Metric: 0 Type: 1 Up
        SR Prefix-SID: 254 Flags: [N] Algorithm: 0
        SR Prefix-SID: 1283 Flags: [N] Algorithm: 128
      Reachability         : 20.149.254.0/24 Metric: 10 Type: 1 Up
      Reachability         : 20.170.254.0/24 Metric: 10 Type: 1 Up
      Router Capabilities: Router Id: 10.0.0.254 Flags: []
        Maximum SID depth:
          Base MPLS imposition (MSD type 1):  10
        SR Capability: Flags: [I]
          SRGB Base: 20000 Range: 2000
        Algorithms:  0, 128
    h43-9901.00-00              254  56796   658    186 L2  0000.0000.0343.00-00  <>
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
    h49-N540-24Q8L2DD.00-00       334  30061   881   1345 L2  0000.0000.0349.00-00  <>
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
      IS Neighbor          : huawei_254_NetEngine_8000_F8.00 Metric: 10
        IPv4 Neighbor Address: 20.149.254.254
        IPv4 Interface Address: 20.149.254.149
        Adj-sid: 24028 flags: [L V] weight: 0x0
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
      IS Neighbor          : juniper_379_MX304.00 Metric: 10
        IPv4 Neighbor Address: 20.149.179.179
        IPv4 Interface Address: 20.149.179.149
        Adj-sid: 24012 flags: [L V B] weight: 0x0
        Adj-sid: 24013 flags: [L V] weight: 0x0
      IS Neighbor          : 0000.0010.0005.00   Metric: 10
        IPv4 Neighbor Address: 20.5.149.5
        IPv4 Interface Address: 20.5.149.149
        Adj-sid: 24003 flags: [L V] weight: 0x0
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
      Reachability         : 20.149.172.0/24 Metric: 10 Type: 1 Up
      Reachability         : 20.149.179.0/24 Metric: 10 Type: 1 Up
      Reachability         : 20.149.254.0/24 Metric: 10 Type: 1 Up
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
    h49-N540-24Q8L2DD.00-01       269  36962   796    124 L2  0000.0000.0349.00-01  <>
      IS Neighbor          : Ribbon-32.00        Metric: 10
        IPv4 Neighbor Address: 20.32.149.32
        IPv4 Interface Address: 20.32.149.149
        Adj-sid: 24025 flags: [L V] weight: 0x0
    h55-8201-24H8FH.00-00       262  43940   371    552 L2  0000.0000.0355.00-00  <>
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
          Base MPLS imposition (MSD type 1):  8
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
    juniper_379_MX304.00-00       691  16480  1141    172 L2  0000.0001.7900.00-00  <>
      Remaining lifetime received: 1199 s Modified to: 1200 s
      NLPID: 0xCC(IPv4) 0x8E(IPv6)
      Hostname: juniper_379_MX304
      Area addresses: 49.0001.00
      Interface address: 10.0.0.179
      Interface address: 209.209.209.209
      Interface address: 127.0.0.1
      IS Neighbor          : Ribbon-32.00        Metric: 10
        IPv4 Neighbor Address: 20.32.179.32
        IPv4 Interface Address: 20.32.179.179
      Reachability         : 10.0.0.179/32 Metric: 0 Type: 1 Up
      Reachability         : 209.209.209.209/32 Metric: 0 Type: 1 Up
      Reachability         : 127.0.0.1/32 Metric: 0 Type: 1 Up
      Reachability         : 20.32.179.0/24 Metric: 10 Type: 1 Up
      Router Capabilities: Router Id: 10.0.0.179 Flags: []
        Maximum SID depth:
          Base MPLS imposition (MSD type 1):  4
      Unsupported TLV: Type: 14 Length: 2
    JNPR-312-ACX7100-48L.00-00       277  47354   495    178 L2  0000.0003.1200.00-00  <>
      Remaining lifetime received: 1199 s Modified to: 1200 s
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
    0000.0010.0005.00-00        213  60423   934    373 L2  0000.0010.0005.00-00  <>
      Remaining lifetime received: 1199 s Modified to: 1200 s
      NLPID: 0xCC(IPv4)
      Area addresses: 49.0000
      Interface address: 20.5.170.5
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
      Reachability         : 20.5.170.0/24 Metric: 10 Type: 1 Up
      Reachability         : 20.5.149.0/24 Metric: 10 Type: 1 Up
      Reachability          : 2002::5/128 Metric: 0 Type: 1 Up
      Router Capabilities: Router Id: 10.0.0.5 Flags: []
        SR Capability: Flags: [I]
          SRGB Base: 20000 Range: 2000
        Algorithms:  0
    NOKIA-SR2-57.00-00        10443  12904  1168    348 L2  0100.0000.0057.00-00  <>
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
    Spine3-J-170.00-00          590  46155  1141    605 L2  0100.0000.0170.00-00  <>
      Remaining lifetime received: 1199 s Modified to: 1200 s
      NLPID: 0xCC(IPv4)
      Hostname: Spine3-J-170
      Area addresses: 49.0000
      Interface address: 20.170.212.170
      Interface address: 20.170.254.170
      Interface address: 20.170.179.170
      Interface address: 20.5.170.170
      Interface address: 20.19.170.170
      Interface address: 20.24.170.170
      Interface address: 20.170.171.170
      Interface address: 20.170.172.170
      Interface address: 20.32.170.170
      Interface address: 20.57.170.170
      Interface address: 20.155.170.170
      Interface address: 10.0.0.170
      IS Neighbor          : juniper_379_MX304.00 Metric: 10
      IS Neighbor          : 0000.0010.0005.00   Metric: 10
        IPv4 Neighbor Address: 20.5.170.5
        IPv4 Interface Address: 20.5.170.170
        Adj-sid: 362153 flags: [L V] weight: 0x0
      IS Neighbor          : JNPR-312-ACX7100-48L.00 Metric: 10
        IPv4 Neighbor Address: 20.170.212.212
        IPv4 Interface Address: 20.170.212.170
        Adj-sid: 362149 flags: [L V] weight: 0x0
      IS Neighbor          : NOKIA-SR2-57.00     Metric: 1
        IPv4 Neighbor Address: 20.57.170.57
        IPv4 Interface Address: 20.57.170.170
        Adj-sid: 362163 flags: [L V] weight: 0x0
      IS Neighbor          : h3c_24_S12500R-48C6D.00 Metric: 10
        IPv4 Neighbor Address: 20.24.170.24
        IPv4 Interface Address: 20.24.170.170
        Adj-sid: 362154 flags: [L V] weight: 0x0
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
      IS Neighbor          : huawei_254_NetEngine_8000_F8.00 Metric: 10
        IPv4 Neighbor Address: 20.170.254.254
        IPv4 Interface Address: 20.170.254.170
        Adj-sid: 362147 flags: [L V] weight: 0x0
      Reachability         : 20.170.212.0/24 Metric: 10 Type: 1 Up
      Reachability         : 20.170.254.0/24 Metric: 10 Type: 1 Up
      Reachability         : 20.170.179.0/24 Metric: 10 Type: 1 Up
      Reachability         : 20.5.170.0/24 Metric: 10 Type: 1 Up
      Reachability         : 20.19.170.0/24 Metric: 10 Type: 1 Up
      Reachability         : 20.24.170.0/24 Metric: 10 Type: 1 Up
      Reachability         : 20.170.171.0/24 Metric: 10 Type: 1 Up
      Reachability         : 20.170.172.0/24 Metric: 100 Type: 1 Up
      Reachability         : 20.32.170.0/24 Metric: 12 Type: 1 Up
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
    PE31-J2-171.00-00           271  45595   350    323 L2  0100.0000.0171.00-00  <>
      LSP generation remaining wait time: 0 ms
      Time remaining until refresh: 50 s
      NLPID: 0xCC(IPv4)
      Hostname: PE31-J2-171
      Area addresses: 49.0000
      Interface address: 20.170.171.171
      Interface address: 20.149.171.171
      Interface address: 10.0.0.171
      IS Neighbor          : h49-N540-24Q8L2DD.00 Metric: 10
        IPv4 Neighbor Address: 20.149.171.149
        IPv4 Interface Address: 20.149.171.171
        Adj-sid: 362144 flags: [L V] weight: 0x0
      IS Neighbor          : Spine3-J-170.00     Metric: 10
        IPv4 Neighbor Address: 20.170.171.170
        IPv4 Interface Address: 20.170.171.171
        Adj-sid: 362145 flags: [L V] weight: 0x0
      Reachability         : 10.0.0.171/32 Metric: 0 Type: 1 Up
        SR Prefix-SID: 171 Flags: [N] Algorithm: 0
        SR Prefix-SID: 1171 Flags: [N] Algorithm: 128
        SR Prefix-SID: 1271 Flags: [N] Algorithm: 129
        SR Prefix-SID: 1371 Flags: [N] Algorithm: 130
        SR Prefix-SID: 1471 Flags: [N] Algorithm: 131
      Reachability         : 20.170.171.0/24 Metric: 10 Type: 1 Up
      Reachability         : 20.149.171.0/24 Metric: 10 Type: 1 Up
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
    h3c_19_CR16010E-F.00-00      1129  29209  1142    411 L2  0000.0000.0019.00-00  <>
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
    h3c_24_S12500R-48C6D.00-00       772  18538   647    421 L2  0000.0000.0024.00-00  <>
      NLPID: 0xCC(IPv4)
      Hostname: h3c_24_S12500R-48C6D
      TE IPv4 router ID: 10.0.0.24
      Area addresses: 49
      Interface address: 10.0.0.24
      Interface address: 20.24.149.24
      Interface address: 20.24.170.24
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
      Router Capabilities: Router Id: 10.0.0.24 Flags: []
        SR Local Block:
          SRLB Base: 15000 Range: 1000
        Maximum SID depth:
          Base MPLS imposition (MSD type 1):  10
        SR Capability: Flags: [I]
          SRGB Base: 20000 Range: 2000
    Ribbon-32.00-00             212  47334   501     79 L2  0000.0000.0032.00-00  <>
      Remaining lifetime received: 1199 s Modified to: 1200 s
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
    Ribbon-32.00-01             211  63354  1129     38 L2  0000.0000.0032.00-01  <>
      Hostname: Ribbon-32
    Ribbon-32.00-02             230  12946   473    421 L2  0000.0000.0032.00-02  <>
      Interface address: 20.32.149.32
      Interface address: 20.32.170.32
      Interface address: 10.0.0.32
      Interface address: 20.32.179.32
      IS Neighbor          : h49-N540-24Q8L2DD.00 Metric: 10
        IPv4 Neighbor Address: 20.32.149.149
        IPv4 Interface Address: 20.32.149.32
        Adj-sid: 756644 flags: [L V] weight: 0x0
        Adj-sid: 756645 flags: [L V B] weight: 0x0
        TE default metric: 10
        Maximum link BW: 1.00 Gbps
        Maximum reservable link BW: 1.00 Gbps
        Unreserved BW:
            TE class 0: 1.00 Gbps	TE class 1: 1.00 Gbps	TE class 2: 1.00 Gbps
            TE class 3: 1.00 Gbps	TE class 4: 1.00 Gbps	TE class 5: 1.00 Gbps
            TE class 6: 1.00 Gbps	TE class 7: 1.00 Gbps
        Min/Max unidirectional link delay: 11/11 us
      IS Neighbor          : Spine3-J-170.00     Metric: 11
        IPv4 Neighbor Address: 20.32.170.170
        IPv4 Interface Address: 20.32.170.32
        Adj-sid: 756646 flags: [L V] weight: 0x0
        Adj-sid: 756647 flags: [L V B] weight: 0x0
        TE default metric: 11
        Maximum link BW: 10.00 Gbps
        Maximum reservable link BW: 10.00 Gbps
        Unreserved BW:
            TE class 0: 10.00 Gbps	TE class 1: 10.00 Gbps	TE class 2: 10.00 Gbps
            TE class 3: 10.00 Gbps	TE class 4: 10.00 Gbps	TE class 5: 10.00 Gbps
            TE class 6: 10.00 Gbps	TE class 7: 10.00 Gbps
        Min/Max unidirectional link delay: 11/11 us
      IS Neighbor          : juniper_379_MX304.00 Metric: 10
        IPv4 Neighbor Address: 20.32.179.179
        IPv4 Interface Address: 20.32.179.32
        Adj-sid: 756641 flags: [L V] weight: 0x0
        Adj-sid: 756643 flags: [L V B] weight: 0x0
        TE default metric: 10
        Maximum link BW: 0.00 bps
        Maximum reservable link BW: 0.00 bps
        Unreserved BW:
            TE class 0: 0.00 bps	TE class 1: 0.00 bps	TE class 2: 0.00 bps
            TE class 3: 0.00 bps	TE class 4: 0.00 bps	TE class 5: 0.00 bps
            TE class 6: 0.00 bps	TE class 7: 0.00 bps
      Reachability         : 20.32.149.0/24 Metric: 10 Type: 1 Up
      Reachability         : 20.32.170.0/24 Metric: 11 Type: 1 Up
      Reachability         : 10.0.0.32/32 Metric: 0 Type: 1 Up
        SR Prefix-SID: 32 Flags: [N] Algorithm: 0
      Reachability         : 20.32.179.0/24 Metric: 10 Type: 1 Up
 U  R6676-50.00-00              244  36733   433    145 L2  0000.0000.0050.00-00  <>
      NLPID: 0xCC(IPv4)
      Hostname: R6676-50
      TE IPv4 router ID: 10.0.0.50
      Area addresses: 49.0000
      Interface address: 10.0.0.50
      IS Neighbor          : h49-N540-24Q8L2DD.00 Metric: 10
        IPv4 Interface Address: 20.50.149.50
      Reachability         : 10.0.0.50/32 Metric: 10 Type: 1 Up
        SR Prefix-SID: 50 Flags: [N P] Algorithm: 0
      Reachability         : 20.50.149.0/24 Metric: 10 Type: 1 Up
      Router Capabilities: Router Id: 10.0.0.50 Flags: []
        Maximum SID depth:
          Base MPLS imposition (MSD type 1):  8
        SR Capability: Flags: [I]
          SRGB Base: 20000 Range: 2000
        Algorithms:  0
    huawei_254_NetEngine_8000_F8.00-00       154  53642  1126    216 L2  0000.0000.0254.00-00  <>
      Remaining lifetime received: 1199 s Modified to: 1200 s
      NLPID: 0xCC(IPv4)
      Hostname: huawei_254_NetEngine_8000_F8
      TE IPv4 router ID: 10.0.0.254
      Area addresses: 49
      Interface address: 10.0.0.254
      Interface address: 20.149.254.254
      Interface address: 20.170.254.254
      IS Neighbor          : h49-N540-24Q8L2DD.00 Metric: 10
        IPv4 Neighbor Address: 20.149.254.149
        IPv4 Interface Address: 20.149.254.254
        Adj-sid: 48030 flags: [L V] weight: 0x0
      IS Neighbor          : Spine3-J-170.00     Metric: 10
        IPv4 Neighbor Address: 20.170.254.170
        IPv4 Interface Address: 20.170.254.254
        Adj-sid: 48032 flags: [L V] weight: 0x0
      Reachability         : 10.0.0.254/32 Metric: 0 Type: 1 Up
        SR Prefix-SID: 254 Flags: [N] Algorithm: 0
        SR Prefix-SID: 1283 Flags: [N] Algorithm: 128
      Reachability         : 20.149.254.0/24 Metric: 10 Type: 1 Up
      Reachability         : 20.170.254.0/24 Metric: 10 Type: 1 Up
      Router Capabilities: Router Id: 10.0.0.254 Flags: []
        Maximum SID depth:
          Base MPLS imposition (MSD type 1):  10
        SR Capability: Flags: [I]
          SRGB Base: 20000 Range: 2000
        Algorithms:  0, 128
    h43-9901.00-00              254  56796   657    186 L2  0000.0000.0343.00-00  <>
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
    h49-N540-24Q8L2DD.00-00       334  30061   880   1345 L2  0000.0000.0349.00-00  <>
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
        Average unidirectional link delay: 11 us
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
        Average unidirectional link delay: 11 us
        Application Specific Link Attributes:
          Standard applications: Flex-Algo
          User-defined applications: APP3
            TE default metric: 12
            Maximum link BW: 100.00 Gbps
            Min/Max unidirectional link delay: 11/11 us
      IS Neighbor          : huawei_254_NetEngine_8000_F8.00 Metric: 10
        IPv4 Neighbor Address: 20.149.254.254
        IPv4 Interface Address: 20.149.254.149
        Adj-sid: 24028 flags: [L V] weight: 0x0
        Maximum link BW: 10.00 Gbps
        Min/Max unidirectional link delay: 11/11 us
        Average unidirectional link delay: 11 us
        Application Specific Link Attributes:
          Standard applications: Flex-Algo
          User-defined applications: APP3
            TE default metric: 12
            Maximum link BW: 10.00 Gbps
            Min/Max unidirectional link delay: 11/11 us
      IS Neighbor          : PE31-J2-171.00      Metric: 10
        IPv4 Neighbor Address: 20.149.171.171
        IPv4 Interface Address: 20.149.171.149
        Adj-sid: 24009 flags: [L V] weight: 0x0
        Maximum link BW: 10.00 Gbps
        Min/Max unidirectional link delay: 1/1 us
        Average unidirectional link delay: 1 us
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
        Average unidirectional link delay: 11 us
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
        Average unidirectional link delay: 2 us
        Application Specific Link Attributes:
          Standard applications: Flex-Algo
          User-defined applications: APP3
            TE default metric: 12
            Maximum link BW: 100.00 Gbps
            Min/Max unidirectional link delay: 2/2 us
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
      IS Neighbor          : 0000.0010.0005.00   Metric: 10
        IPv4 Neighbor Address: 20.5.149.5
        IPv4 Interface Address: 20.5.149.149
        Adj-sid: 24003 flags: [L V] weight: 0x0
        Maximum link BW: 10.00 Gbps
        Min/Max unidirectional link delay: 11/11 us
        Average unidirectional link delay: 11 us
        Application Specific Link Attributes:
          Standard applications: Flex-Algo
          User-defined applications: APP3
            TE default metric: 12
            Maximum link BW: 10.00 Gbps
            Min/Max unidirectional link delay: 11/11 us
      IS Neighbor          : NOKIA-SR2-57.00     Metric: 10
        IPv4 Neighbor Address: 20.57.149.57
        IPv4 Interface Address: 20.57.149.149
        Adj-sid: 24018 flags: [L V B] weight: 0x0
        Adj-sid: 24019 flags: [L V] weight: 0x0
        Maximum link BW: 10.00 Gbps
        Min/Max unidirectional link delay: 11/11 us
        Average unidirectional link delay: 11 us
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
      Reachability         : 20.149.172.0/24 Metric: 10 Type: 1 Up
      Reachability         : 20.149.179.0/24 Metric: 10 Type: 1 Up
      Reachability         : 20.149.254.0/24 Metric: 10 Type: 1 Up
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
    h49-N540-24Q8L2DD.00-01       269  36962   796    124 L2  0000.0000.0349.00-01  <>
      IS Neighbor          : Ribbon-32.00        Metric: 10
        IPv4 Neighbor Address: 20.32.149.32
        IPv4 Interface Address: 20.32.149.149
        Adj-sid: 24025 flags: [L V] weight: 0x0
        Maximum link BW: 1.00 Gbps
        Min/Max unidirectional link delay: 11/11 us
        Average unidirectional link delay: 11 us
        Application Specific Link Attributes:
          Standard applications: Flex-Algo
          User-defined applications: APP3
            TE default metric: 12
            Maximum link BW: 1.00 Gbps
            Min/Max unidirectional link delay: 11/11 us
    h55-8201-24H8FH.00-00       262  43940   370    552 L2  0000.0000.0355.00-00  <>
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
        Average unidirectional link delay: 2 us
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
          Base MPLS imposition (MSD type 1):  8
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
    juniper_379_MX304.00-00       691  16480  1141    172 L2  0000.0001.7900.00-00  <>
      Remaining lifetime received: 1199 s Modified to: 1200 s
      NLPID: 0xCC(IPv4) 0x8E(IPv6)
      Hostname: juniper_379_MX304
      TE IPv4 router ID: 10.0.0.179
      Area addresses: 49.0001.00
      Interface address: 10.0.0.179
      Interface address: 209.209.209.209
      Interface address: 127.0.0.1
      IS Neighbor          : Ribbon-32.00        Metric: 10
        IPv4 Neighbor Address: 20.32.179.32
        IPv4 Interface Address: 20.32.179.179
      Reachability         : 10.0.0.179/32 Metric: 0 Type: 1 Up
      Reachability         : 209.209.209.209/32 Metric: 0 Type: 1 Up
      Reachability         : 127.0.0.1/32 Metric: 0 Type: 1 Up
      Reachability         : 20.32.179.0/24 Metric: 10 Type: 1 Up
      Router Capabilities: Router Id: 10.0.0.179 Flags: []
        Maximum SID depth:
          Base MPLS imposition (MSD type 1):  4
      Unsupported TLV: Type: 14 Length: 2
    JNPR-312-ACX7100-48L.00-00       277  47354   495    178 L2  0000.0003.1200.00-00  <>
      Remaining lifetime received: 1199 s Modified to: 1200 s
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
    0000.0010.0005.00-00        213  60423   934    373 L2  0000.0010.0005.00-00  <>
      Remaining lifetime received: 1199 s Modified to: 1200 s
      NLPID: 0xCC(IPv4)
      TE IPv4 router ID: 10.0.0.5
      Area addresses: 49.0000
      Interface address: 20.5.170.5
      IS Neighbor          : h49-N540-24Q8L2DD.00 Metric: 10
        IPv4 Neighbor Address: 20.5.149.149
        IPv4 Interface Address: 20.5.149.5
        Adj-sid: 16000 flags: [L V] weight: 0x0
        TE default metric: 100
        Maximum link BW: 10.00 Gbps
        Maximum reservable link BW: 10.00 Gbps
        Unreserved BW:
            TE class 0: 10.00 Gbps	TE class 1: 10.00 Gbps	TE class 2: 10.00 Gbps
            TE class 3: 10.00 Gbps	TE class 4: 10.00 Gbps	TE class 5: 10.00 Gbps
            TE class 6: 10.00 Gbps	TE class 7: 10.00 Gbps
        Min/Max unidirectional link delay: 11/11 us
        Average unidirectional link delay: 11 us
        Application Specific Link Attributes:
          Standard applications: RSVP-TE SR-TE LFA Flex-Algo
            TE default metric: 100
            Min/Max unidirectional link delay: 11/11 us
            Average unidirectional link delay: 11 us
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
      Reachability         : 20.5.170.0/24 Metric: 10 Type: 1 Up
      Reachability         : 20.5.149.0/24 Metric: 10 Type: 1 Up
      Reachability          : 2002::5/128 Metric: 0 Type: 1 Up
      Router Capabilities: Router Id: 10.0.0.5 Flags: []
        SR Capability: Flags: [I]
          SRGB Base: 20000 Range: 2000
        Algorithms:  0
    NOKIA-SR2-57.00-00        10443  12904  1168    348 L2  0100.0000.0057.00-00  <>
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
    Spine3-J-170.00-00          590  46155  1141    605 L2  0100.0000.0170.00-00  <>
      Remaining lifetime received: 1199 s Modified to: 1200 s
      NLPID: 0xCC(IPv4)
      Hostname: Spine3-J-170
      TE IPv4 router ID: 10.0.0.170
      Area addresses: 49.0000
      Interface address: 20.170.212.170
      Interface address: 20.170.254.170
      Interface address: 20.170.179.170
      Interface address: 20.5.170.170
      Interface address: 20.19.170.170
      Interface address: 20.24.170.170
      Interface address: 20.170.171.170
      Interface address: 20.170.172.170
      Interface address: 20.32.170.170
      Interface address: 20.57.170.170
      Interface address: 20.155.170.170
      Interface address: 10.0.0.170
      IS Neighbor          : juniper_379_MX304.00 Metric: 10
      IS Neighbor          : 0000.0010.0005.00   Metric: 10
        IPv4 Neighbor Address: 20.5.170.5
        IPv4 Interface Address: 20.5.170.170
        Adj-sid: 362153 flags: [L V] weight: 0x0
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
      IS Neighbor          : h3c_24_S12500R-48C6D.00 Metric: 10
        IPv4 Neighbor Address: 20.24.170.24
        IPv4 Interface Address: 20.24.170.170
        Adj-sid: 362154 flags: [L V] weight: 0x0
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
      IS Neighbor          : huawei_254_NetEngine_8000_F8.00 Metric: 10
        IPv4 Neighbor Address: 20.170.254.254
        IPv4 Interface Address: 20.170.254.170
        Adj-sid: 362147 flags: [L V] weight: 0x0
      Reachability         : 20.170.212.0/24 Metric: 10 Type: 1 Up
      Reachability         : 20.170.254.0/24 Metric: 10 Type: 1 Up
      Reachability         : 20.170.179.0/24 Metric: 10 Type: 1 Up
      Reachability         : 20.5.170.0/24 Metric: 10 Type: 1 Up
      Reachability         : 20.19.170.0/24 Metric: 10 Type: 1 Up
      Reachability         : 20.24.170.0/24 Metric: 10 Type: 1 Up
      Reachability         : 20.170.171.0/24 Metric: 10 Type: 1 Up
      Reachability         : 20.170.172.0/24 Metric: 100 Type: 1 Up
      Reachability         : 20.32.170.0/24 Metric: 12 Type: 1 Up
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
    PE31-J2-171.00-00           271  45595   349    323 L2  0100.0000.0171.00-00  <>
      LSP generation remaining wait time: 0 ms
      Time remaining until refresh: 49 s
      NLPID: 0xCC(IPv4)
      Hostname: PE31-J2-171
      Area addresses: 49.0000
      Interface address: 20.170.171.171
      Interface address: 20.149.171.171
      Interface address: 10.0.0.171
      IS Neighbor          : h49-N540-24Q8L2DD.00 Metric: 10
        IPv4 Neighbor Address: 20.149.171.149
        IPv4 Interface Address: 20.149.171.171
        Adj-sid: 362144 flags: [L V] weight: 0x0
        Application Specific Link Attributes:
          Standard applications: Flex-Algo
            Administrative group (Color): 127
            TE default metric: 12
            Min/Max unidirectional link delay: 2/2 us
      IS Neighbor          : Spine3-J-170.00     Metric: 10
        IPv4 Neighbor Address: 20.170.171.170
        IPv4 Interface Address: 20.170.171.171
        Adj-sid: 362145 flags: [L V] weight: 0x0
      Reachability         : 10.0.0.171/32 Metric: 0 Type: 1 Up
        SR Prefix-SID: 171 Flags: [N] Algorithm: 0
        SR Prefix-SID: 1171 Flags: [N] Algorithm: 128
        SR Prefix-SID: 1271 Flags: [N] Algorithm: 129
        SR Prefix-SID: 1371 Flags: [N] Algorithm: 130
        SR Prefix-SID: 1471 Flags: [N] Algorithm: 131
      Reachability         : 20.170.171.0/24 Metric: 10 Type: 1 Up
      Reachability         : 20.149.171.0/24 Metric: 10 Type: 1 Up
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
Request sequence number: 138
Response sequence number: 138
Number of times path updated: 138
Last updated: 0:00:58 ago
Next Hop Interface
-------- ---------

Destination: PE31-J2-171
Path ID: 641
Path constraints: algo MIN-TE
                  metric type TE
Request sequence number: 18
Response sequence number: 18
Number of times path updated: 18
Last updated: 0:05:18 ago
Next Hop Interface
-------- ---------

Destination: PE31-J2-171
Path ID: 642
Path constraints: algo MIN-IGP
                  metric type IGP
                  administrative-group exclude 1
Request sequence number: 18
Response sequence number: 18
Number of times path updated: 18
Last updated: 0:05:18 ago
Next Hop Interface
-------- ---------

Destination: PE31-J2-171
Path ID: 643
Path constraints: algo MIN-IGP-ADMIN
                  metric type IGP
                  administrative-group exclude 127
Request sequence number: 17
Response sequence number: 17
Number of times path updated: 17
Last updated: 0:05:18 ago
Next Hop Interface
-------- ---------

Destination: h49-N540-24Q8L2DD
Path ID: 641
Path constraints: algo MIN-TE
                  metric type TE
Request sequence number: 25
Response sequence number: 25
Number of times path updated: 18
Last updated: 0:05:18 ago
Metric: 12
Next Hop       Interface 
-------------- ----------
20.149.171.149 Ethernet24

Destination: h49-N540-24Q8L2DD
Path ID: 642
Path constraints: algo MIN-IGP
                  metric type IGP
                  administrative-group exclude 1
Request sequence number: 22
Response sequence number: 22
Number of times path updated: 18
Last updated: 0:05:18 ago
Metric: 10
Next Hop       Interface 
-------------- ----------
20.149.171.149 Ethernet24

Destination: h49-N540-24Q8L2DD
Path ID: 643
Path constraints: algo MIN-IGP-ADMIN
                  metric type IGP
                  administrative-group exclude 127
Request sequence number: 19
Response sequence number: 19
Number of times path updated: 18
Last updated: 0:05:18 ago
Metric: 40
Next Hop       Interface
-------------- ---------
20.170.171.170 Ethernet1

Destination: h55-8201-24H8FH
Path ID: 640
Path constraints: algo MIN-LATENCY
                  metric type MIN-DELAY
Request sequence number: 147
Response sequence number: 147
Number of times path updated: 139
Last updated: 0:00:58 ago
Metric: 4
Next Hop       Interface 
-------------- ----------
20.149.171.149 Ethernet24

Destination: h55-8201-24H8FH
Path ID: 641
Path constraints: algo MIN-TE
                  metric type TE
Request sequence number: 25
Response sequence number: 25
Number of times path updated: 18
Last updated: 0:05:18 ago
Metric: 24
Next Hop       Interface 
-------------- ----------
20.149.171.149 Ethernet24

Destination: h55-8201-24H8FH
Path ID: 642
Path constraints: algo MIN-IGP
                  metric type IGP
                  administrative-group exclude 1
Request sequence number: 22
Response sequence number: 22
Number of times path updated: 18
Last updated: 0:05:18 ago
Metric: 20
Next Hop       Interface 
-------------- ----------
20.149.171.149 Ethernet24

Destination: h55-8201-24H8FH
Path ID: 643
Path constraints: algo MIN-IGP-ADMIN
                  metric type IGP
                  administrative-group exclude 127
Request sequence number: 19
Response sequence number: 19
Number of times path updated: 18
Last updated: 0:05:18 ago
Metric: 30
Next Hop       Interface
-------------- ---------
20.170.171.170 Ethernet1

Destination: huawei_254_NetEngine_8000_F8
Path ID: 640
Path constraints: algo MIN-LATENCY
                  metric type MIN-DELAY
Request sequence number: 147
Response sequence number: 147
Number of times path updated: 139
Last updated: 0:00:58 ago
Metric: 13
Next Hop       Interface 
-------------- ----------
20.149.171.149 Ethernet24

```

## show isis segment-routing tunnel

```text
 Index    Endpoint              Next Hop/Tunnel Index    Interface    Labels   
-------- --------------------- ------------------------ ------------- ---------
 1        10.0.1.49/32          TI-LFA (4)               -            [ 3 ]    
 2        10.0.1.43/32          TI-LFA (1)               -            [ 20343 ]
 3        10.0.0.19/32          20.149.171.149           Ethernet24   [ 20019 ]
                                20.170.171.170           Ethernet1    [ 20019 ]
 4        10.0.1.55/32          TI-LFA (1)               -            [ 20355 ]
 6        10.0.0.254/32         20.149.171.149           Ethernet24   [ 20254 ]
                                20.170.171.170           Ethernet1    [ 20254 ]
 8        10.0.0.24/32          20.149.171.149           Ethernet24   [ 20024 ]
                                20.170.171.170           Ethernet1    [ 20024 ]
 9        10.0.0.5/32           20.149.171.149           Ethernet24   [ 20005 ]
                                20.170.171.170           Ethernet1    [ 20005 ]
 10       209.209.209.209/32    TI-LFA (1)               -            [ 20209 ]
 13       10.0.0.57/32          TI-LFA (8)               -            [ 20057 ]
 14       10.0.0.32/32          TI-LFA (1)               -            [ 20032 ]
 16       10.0.0.170/32         TI-LFA (0)               -            [ 3 ]    
 17       10.0.0.212/32         TI-LFA (3)               -            [ 20212 ]

```

## show isis segment-routing prefix-segments

```text

System ID: PE31-J2-171			Instance: 'IGP'
SR supported Data-plane: MPLS			SR Router ID: 10.0.0.171

Node: 33     Proxy-Node: 0      Prefix: 1       Total Segments: 34

Flag Descriptions: R: Re-advertised, N: Node Segment, P: no-PHP
                   E: Explicit-NULL, V: Value, L: Local
Segment status codes: * - Self originated Prefix, L1 - level 1, L2 - level 2, ! - SR-unreachable,
                      # - Some IS-IS next-hops are SR-unreachable
   Prefix                      SID   Label Type       Flags                        System ID       Level Protection  Algorithm   
   ------------------------- ----- ------- ---------- ---------------------------- --------------- ----- ----------- -------------
   10.0.0.5/32                   5   20005 Node       R:0 N:1 P:1 E:0 V:0 L:0      0000.0010.0005  L2    unprotected SPF         
   10.0.0.19/32                 19   20019 Node       R:0 N:1 P:0 E:0 V:0 L:0      h3c_19_CR16010E-F L2    unprotected SPF         
   10.0.0.24/32                 24   20024 Node       R:0 N:1 P:1 E:0 V:0 L:0      h3c_24_S12500R-48C6D L2    unprotected SPF         
   10.0.0.32/32                 32   20032 Node       R:0 N:1 P:0 E:0 V:0 L:0      Ribbon-32       L2    node        SPF         
   10.0.0.57/32                 57   20057 Node       R:0 N:1 P:1 E:0 V:0 L:0      NOKIA-SR2-57    L2    node        SPF         
   10.0.0.170/32               170   20170 Node       R:0 N:1 P:0 E:0 V:0 L:0      Spine3-J-170    L2    node        SPF         
*  10.0.0.171/32               171   20171 Node       R:0 N:1 P:0 E:0 V:0 L:0      PE31-J2-171     L2    unprotected SPF         
*  10.0.0.171/32              1171   21171 Node       R:0 N:1 P:0 E:0 V:0 L:0      PE31-J2-171     L2    unprotected MIN-LATENCY 
*  10.0.0.171/32              1271   21271 Node       R:0 N:1 P:0 E:0 V:0 L:0      PE31-J2-171     L2    unprotected MIN-TE      
*  10.0.0.171/32              1371   21371 Node       R:0 N:1 P:0 E:0 V:0 L:0      PE31-J2-171     L2    unprotected MIN-IGP     
*  10.0.0.171/32              1471   21471 Node       R:0 N:1 P:0 E:0 V:0 L:0      PE31-J2-171     L2    unprotected MIN-IGP-ADMIN
   10.0.0.212/32               212   20212 Node       R:0 N:1 P:1 E:1 V:0 L:0      JNPR-312-ACX7100-48L L2    node        SPF         
   10.0.0.254/32               254   20254 Node       R:0 N:1 P:0 E:0 V:0 L:0      huawei_254_NetEngine_8000_F8 L2    unprotected SPF         
   10.0.0.254/32              1283   21283 Node       R:0 N:1 P:0 E:0 V:0 L:0      huawei_254_NetEngine_8000_F8 L2    node        MIN-LATENCY 
   10.0.1.43/32                343   20343 Node       R:0 N:1 P:0 E:0 V:0 L:0      h43-9901        L2    node        SPF         
   10.0.1.49/32                349   20349 Node       R:0 N:1 P:0 E:0 V:0 L:0      h49-N540-24Q8L2DD L2    node        SPF         
   10.0.1.49/32               1449   21449 Node       R:0 N:1 P:0 E:0 V:0 L:0      h49-N540-24Q8L2DD L2    node        MIN-TE      
   10.0.1.49/32               1549   21549 Node       R:0 N:1 P:0 E:0 V:0 L:0      h49-N540-24Q8L2DD L2    node        MIN-IGP     
   10.0.1.49/32               1649   21649 Node       R:0 N:1 P:0 E:0 V:0 L:0      h49-N540-24Q8L2DD L2    node        MIN-IGP-ADMIN
   10.0.1.49/32               1749   21749 Node       R:0 N:1 P:0 E:0 V:0 L:0      h49-N540-24Q8L2DD L2    unprotected 132         
   10.0.1.49/32                449   20449 Node       R:0 N:1 P:0 E:0 V:0 L:0      h49-N540-24Q8L2DD L2    unprotected 140         
   10.0.1.49/32                549   20549 Node       R:0 N:1 P:0 E:0 V:0 L:0      h49-N540-24Q8L2DD L2    unprotected 141         
   10.0.1.49/32                649   20649 Node       R:0 N:1 P:0 E:0 V:0 L:0      h49-N540-24Q8L2DD L2    unprotected 142         
   10.0.1.55/32                355   20355 Node       R:0 N:1 P:0 E:0 V:0 L:0      h55-8201-24H8FH L2    node        SPF         
   10.0.1.55/32               1355   21355 Node       R:0 N:1 P:0 E:0 V:0 L:0      h55-8201-24H8FH L2    node        MIN-LATENCY 
   10.0.1.55/32               1455   21455 Node       R:0 N:1 P:0 E:0 V:0 L:0      h55-8201-24H8FH L2    node        MIN-TE      
   10.0.1.55/32               1555   21555 Node       R:0 N:1 P:0 E:0 V:0 L:0      h55-8201-24H8FH L2    node        MIN-IGP     
   10.0.1.55/32               1655   21655 Node       R:0 N:1 P:0 E:0 V:0 L:0      h55-8201-24H8FH L2    node        MIN-IGP-ADMIN
   10.0.1.55/32               1755   21755 Node       R:0 N:1 P:0 E:0 V:0 L:0      h55-8201-24H8FH L2    unprotected 132         
   10.0.1.55/32                455   20455 Node       R:0 N:1 P:0 E:0 V:0 L:0      h55-8201-24H8FH L2    unprotected 140         
   10.0.1.55/32                555   20555 Node       R:0 N:1 P:0 E:0 V:0 L:0      h55-8201-24H8FH L2    unprotected 141         
   10.0.1.55/32                655   20655 Node       R:0 N:1 P:0 E:0 V:0 L:0      h55-8201-24H8FH L2    unprotected 142         
   209.209.209.209/32          209   20209 Prefix     R:0 N:0 P:0 E:0 V:0 L:0      h55-8201-24H8FH L2    node        SPF         
   2002::57/128                157   20157 Node       R:0 N:1 P:1 E:0 V:0 L:0      NOKIA-SR2-57    L2    unprotected SPF         
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
 B I      0.0.0.0/0 [200/0]
           via 20.149.171.149, Ethernet24

 I L2     10.0.0.5/32 [115/20]
           via 20.170.171.170, Ethernet1
           via 20.149.171.149, Ethernet24
 I L2     10.0.0.19/32 [115/20]
           via 20.170.171.170, Ethernet1
           via 20.149.171.149, Ethernet24
 I L2     10.0.0.24/32 [115/20]
           via 20.170.171.170, Ethernet1
           via 20.149.171.149, Ethernet24
 I L2     10.0.0.32/32 [115/20]
           via 20.149.171.149, Ethernet24
 I L2     10.0.0.57/32 [115/11]
           via 20.170.171.170, Ethernet1
 I L2     10.0.0.170/32 [115/10]
           via 20.170.171.170, Ethernet1
 C        10.0.0.171/32
           directly connected, Loopback0
 I L2     10.0.0.179/32 [115/30]
           via 20.149.171.149, Ethernet24
 I L2     10.0.0.212/32 [115/20]
           via 20.170.171.170, Ethernet1
 I L2     10.0.0.254/32 [115/20]
           via 20.170.171.170, Ethernet1
           via 20.149.171.149, Ethernet24
 I L2     10.0.1.43/32 [115/20]
           via 20.149.171.149, Ethernet24
 I L2     10.0.1.49/32 [115/10]
           via 20.149.171.149, Ethernet24
 I L2     10.0.1.55/32 [115/20]
           via 20.149.171.149, Ethernet24
 I L2     20.5.149.0/24 [115/20]
           via 20.149.171.149, Ethernet24
 I L2     20.5.170.0/24 [115/20]
           via 20.170.171.170, Ethernet1
 I L2     20.19.149.0/24 [115/20]
           via 20.149.171.149, Ethernet24
 I L2     20.19.170.0/24 [115/20]
           via 20.170.171.170, Ethernet1
 I L2     20.24.149.0/24 [115/20]
           via 20.149.171.149, Ethernet24
 I L2     20.24.170.0/24 [115/20]
           via 20.170.171.170, Ethernet1
 I L2     20.32.149.0/24 [115/20]
           via 20.149.171.149, Ethernet24
 I L2     20.32.155.0/24 [115/30]
           via 20.149.171.149, Ethernet24
 I L2     20.32.170.0/24 [115/22]
           via 20.170.171.170, Ethernet1
 I L2     20.32.179.0/24 [115/30]
           via 20.149.171.149, Ethernet24
 I L2     20.57.149.0/24 [115/20]
           via 20.149.171.149, Ethernet24
 I L2     20.57.155.0/24 [115/30]
           via 20.149.171.149, Ethernet24
 I L2     20.57.170.0/24 [115/11]
           via 20.170.171.170, Ethernet1
 I L2     20.111.149.0/24 [115/20]
           via 20.149.171.149, Ethernet24
 B I      20.111.179.0/24 [200/0]
           via 20.149.171.149, Ethernet24
 I L2     20.143.149.0/24 [115/20]
           via 20.149.171.149, Ethernet24
 I L2     20.149.155.0/24 [115/20]
           via 20.149.171.149, Ethernet24
 C        20.149.171.0/24
           directly connected, Ethernet24
 I L2     20.149.172.0/24 [115/20]
           via 20.149.171.149, Ethernet24
 I L2     20.149.179.0/24 [115/20]
           via 20.149.171.149, Ethernet24
 I L2     20.149.254.0/24 [115/20]
           via 20.149.171.149, Ethernet24
 I L2     20.155.170.0/24 [115/30]
           via 20.170.171.170, Ethernet1
           via 20.149.171.149, Ethernet24
 C        20.170.171.0/24
           directly connected, Ethernet1
 I L2     20.170.172.0/24 [115/110]
           via 20.170.171.170, Ethernet1
 I L2     20.170.179.0/24 [115/20]
           via 20.170.171.170, Ethernet1
 I L2     20.170.212.0/24 [115/20]
           via 20.170.171.170, Ethernet1
 I L2     20.170.254.0/24 [115/20]
           via 20.170.171.170, Ethernet1
 I L2     31.9.1.0/24 [115/20]
           via 20.170.171.170, Ethernet1
           via 20.149.171.149, Ethernet24
 B I      192.168.20.0/23 [200/0]
           via 20.149.171.149, Ethernet24
 B I      192.168.24.0/25 [200/0]
           via 20.149.171.149, Ethernet24
 I L2     192.168.0.0/19 [115/20]
           via 20.170.171.170, Ethernet1
           via 20.149.171.149, Ethernet24
 I L2     209.209.209.209/32 [115/20]
           via 20.149.171.149, Ethernet24

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
 B I      0.0.0.0/0 [200/0]
           via 20.149.171.149, Ethernet24

 I L2     10.0.0.5/32 [115/20]
           via 20.170.171.170, Ethernet1
           via 20.149.171.149, Ethernet24
 I L2     10.0.0.19/32 [115/20]
           via 20.170.171.170, Ethernet1
           via 20.149.171.149, Ethernet24
 I L2     10.0.0.24/32 [115/20]
           via 20.170.171.170, Ethernet1
           via 20.149.171.149, Ethernet24
 I L2     10.0.0.32/32 [115/20]
           via 20.149.171.149, Ethernet24
 I L2     10.0.0.57/32 [115/11]
           via 20.170.171.170, Ethernet1
 I L2     10.0.0.170/32 [115/10]
           via 20.170.171.170, Ethernet1
 C        10.0.0.171/32
           directly connected, Loopback0
 I L2     10.0.0.179/32 [115/30]
           via 20.149.171.149, Ethernet24
 I L2     10.0.0.212/32 [115/20]
           via 20.170.171.170, Ethernet1
 I L2     10.0.0.254/32 [115/20]
           via 20.170.171.170, Ethernet1
           via 20.149.171.149, Ethernet24
 I L2     10.0.1.43/32 [115/20]
           via 20.149.171.149, Ethernet24
 I L2     10.0.1.49/32 [115/10]
           via 20.149.171.149, Ethernet24
 I L2     10.0.1.55/32 [115/20]
           via 20.149.171.149, Ethernet24
 I L2     20.5.149.0/24 [115/20]
           via 20.149.171.149, Ethernet24
 I L2     20.5.170.0/24 [115/20]
           via 20.170.171.170, Ethernet1
 I L2     20.19.149.0/24 [115/20]
           via 20.149.171.149, Ethernet24
 I L2     20.19.170.0/24 [115/20]
           via 20.170.171.170, Ethernet1
 I L2     20.24.149.0/24 [115/20]
           via 20.149.171.149, Ethernet24
 I L2     20.24.170.0/24 [115/20]
           via 20.170.171.170, Ethernet1
 I L2     20.32.149.0/24 [115/20]
           via 20.149.171.149, Ethernet24
 I L2     20.32.155.0/24 [115/30]
           via 20.149.171.149, Ethernet24
 I L2     20.32.170.0/24 [115/22]
           via 20.170.171.170, Ethernet1
 I L2     20.32.179.0/24 [115/30]
           via 20.149.171.149, Ethernet24
 I L2     20.57.149.0/24 [115/20]
           via 20.149.171.149, Ethernet24
 I L2     20.57.155.0/24 [115/30]
           via 20.149.171.149, Ethernet24
 I L2     20.57.170.0/24 [115/11]
           via 20.170.171.170, Ethernet1
 I L2     20.111.149.0/24 [115/20]
           via 20.149.171.149, Ethernet24
 B I      20.111.179.0/24 [200/0]
           via 20.149.171.149, Ethernet24
 I L2     20.143.149.0/24 [115/20]
           via 20.149.171.149, Ethernet24
 I L2     20.149.155.0/24 [115/20]
           via 20.149.171.149, Ethernet24
 C        20.149.171.0/24
           directly connected, Ethernet24
 I L2     20.149.172.0/24 [115/20]
           via 20.149.171.149, Ethernet24
 I L2     20.149.179.0/24 [115/20]
           via 20.149.171.149, Ethernet24
 I L2     20.149.254.0/24 [115/20]
           via 20.149.171.149, Ethernet24
 I L2     20.155.170.0/24 [115/30]
           via 20.170.171.170, Ethernet1
           via 20.149.171.149, Ethernet24
 C        20.170.171.0/24
           directly connected, Ethernet1
 I L2     20.170.172.0/24 [115/110]
           via 20.170.171.170, Ethernet1
 I L2     20.170.179.0/24 [115/20]
           via 20.170.171.170, Ethernet1
 I L2     20.170.212.0/24 [115/20]
           via 20.170.171.170, Ethernet1
 I L2     20.170.254.0/24 [115/20]
           via 20.170.171.170, Ethernet1
 I L2     31.9.1.0/24 [115/20]
           via 20.170.171.170, Ethernet1
           via 20.149.171.149, Ethernet24
 B I      192.168.20.0/23 [200/0]
           via 20.149.171.149, Ethernet24
 B I      192.168.24.0/25 [200/0]
           via 20.149.171.149, Ethernet24
 I L2     192.168.0.0/19 [115/20]
           via 20.170.171.170, Ethernet1
           via 20.149.171.149, Ethernet24
 I L2     209.209.209.209/32 [115/20]
           via 20.149.171.149, Ethernet24


VRF: ISIS-SR-FLEXALGO-MIN-DELAY
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

 B I      20.57.111.0/24 [200/0]
           via 10.0.0.57/32, IS-IS SR tunnel index 13, label 524286
              via TI-LFA tunnel index 8, label 20057
                 via 20.170.171.170, Ethernet1, label imp-null(3)
                 backup via 20.149.171.149, Ethernet24, label imp-null(3)
 B I      20.111.155.0/24 [200/0]
           via 10.0.1.55/32, IS-IS SR tunnel index 4, label 24013
              via TI-LFA tunnel index 1, label 20355
                 via 20.149.171.149, Ethernet24, label imp-null(3)
                 backup via 20.170.171.170, Ethernet1, label imp-null(3)
 C        20.111.171.0/24
           directly connected, Ethernet5.128


VRF: ISIS-SR-FLEXALGO-MIN-IGP
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

 B I      20.57.111.0/24 [200/0]
           via 10.0.0.57/32, IS-IS SR tunnel index 13, label 524284
              via TI-LFA tunnel index 8, label 20057
                 via 20.170.171.170, Ethernet1, label imp-null(3)
                 backup via 20.149.171.149, Ethernet24, label imp-null(3)
 B I      20.111.155.0/24 [200/0]
           via 10.0.1.55/32, IS-IS SR tunnel index 4, label 24005
              via TI-LFA tunnel index 1, label 20355
                 via 20.149.171.149, Ethernet24, label imp-null(3)
                 backup via 20.170.171.170, Ethernet1, label imp-null(3)
 C        20.111.171.0/24
           directly connected, Ethernet5.130
 B I      55.55.55.130/32 [200/0]
           via 10.0.1.55/32, IS-IS SR tunnel index 4, label 24005
              via TI-LFA tunnel index 1, label 20355
                 via 20.149.171.149, Ethernet24, label imp-null(3)
                 backup via 20.170.171.170, Ethernet1, label imp-null(3)


VRF: ISIS-SR-FLEXALGO-MIN-IGP-ADMIN
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

 B I      20.57.111.0/24 [200/0]
           via 10.0.0.57/32, IS-IS SR tunnel index 13, label 524283
              via TI-LFA tunnel index 8, label 20057
                 via 20.170.171.170, Ethernet1, label imp-null(3)
                 backup via 20.149.171.149, Ethernet24, label imp-null(3)
 B I      20.111.155.0/24 [200/0]
           via 10.0.1.55/32, IS-IS SR tunnel index 4, label 24019
              via TI-LFA tunnel index 1, label 20355
                 via 20.149.171.149, Ethernet24, label imp-null(3)
                 backup via 20.170.171.170, Ethernet1, label imp-null(3)
 C        20.111.171.0/24
           directly connected, Ethernet5.131


VRF: ISIS-SR-FLEXALGO-MIN-TE
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

 B I      20.57.111.0/24 [200/0]
           via 10.0.0.57/32, IS-IS SR tunnel index 13, label 524285
              via TI-LFA tunnel index 8, label 20057
                 via 20.170.171.170, Ethernet1, label imp-null(3)
                 backup via 20.149.171.149, Ethernet24, label imp-null(3)
 B I      20.111.155.0/24 [200/0]
           via 10.0.1.55/32, IS-IS SR tunnel index 4, label 24015
              via TI-LFA tunnel index 1, label 20355
                 via 20.149.171.149, Ethernet24, label imp-null(3)
                 backup via 20.170.171.170, Ethernet1, label imp-null(3)
 C        20.111.171.0/24
           directly connected, Ethernet5.129


VRF: ISIS-SR-L3VPN
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

 B I      20.32.111.0/24 [200/0]
           via 10.0.0.32/32, IS-IS SR tunnel index 14, label 756640
              via TI-LFA tunnel index 1, label 20032
                 via 20.149.171.149, Ethernet24, label imp-null(3)
                 backup via 20.170.171.170, Ethernet1, label imp-null(3)
 B I      20.57.111.0/24 [200/0]
           via 10.0.0.57/32, IS-IS SR tunnel index 13, label 524252
              via TI-LFA tunnel index 8, label 20057
                 via 20.170.171.170, Ethernet1, label imp-null(3)
                 backup via 20.149.171.149, Ethernet24, label imp-null(3)
 B I      20.111.155.0/24 [200/0]
           via 10.0.1.55/32, IS-IS SR tunnel index 4, label 24021
              via TI-LFA tunnel index 1, label 20355
                 via 20.149.171.149, Ethernet24, label imp-null(3)
                 backup via 20.170.171.170, Ethernet1, label imp-null(3)
 C        20.111.171.0/24
           directly connected, Ethernet5.209
 B I      20.111.254.0/24 [200/0]
           via 10.0.0.254/32, IS-IS SR tunnel index 6, label 48090
              via 20.149.171.149, Ethernet24, label 20254
              via 20.170.171.170, Ethernet1, label 20254


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
MPLS forwarding table (Label [metric] Vias) - 32 routes 
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
                via M, forward
                    EgressACL: apply
                    20.149.171.149 Ethernet24
                    20.170.171.170 Ethernet1
 20019   A[1]
                via M, forward
                    EgressACL: apply
                    20.149.171.149 Ethernet24
                    20.170.171.170 Ethernet1
 20024   A[1]
                via M, forward
                    EgressACL: apply
                    20.149.171.149 Ethernet24
                    20.170.171.170 Ethernet1
 20032   A[1]
                via M, ::, forward
                    EgressACL: apply
                  via TI-LFA tunnel index 1
                    via 20.149.171.149, Ethernet24, label imp-null(3)
                    backup via 20.170.171.170, Ethernet1, label imp-null(3)
 20057   A[1]
                via M, ::, forward
                    EgressACL: apply
                  via TI-LFA tunnel index 8
                    via 20.170.171.170, Ethernet1, label imp-null(3)
                    backup via 20.149.171.149, Ethernet24, label imp-null(3)
 20170   A[1]
                via M, ::, pop
                    EgressACL: apply
                  via TI-LFA tunnel index 0
                    via 20.170.171.170, Ethernet1, label imp-null(3)
                    backup via 20.149.171.149, Ethernet24, label 20254 20170
 20209   A[1]
                via M, ::, forward
                    EgressACL: apply
                  via TI-LFA tunnel index 1
                    via 20.149.171.149, Ethernet24, label imp-null(3)
                    backup via 20.170.171.170, Ethernet1, label imp-null(3)
 20212   A[1]
                via M, ::, forward
                    EgressACL: apply
                  via TI-LFA tunnel index 3
                    via 20.170.171.170, Ethernet1, label imp-null(3)
                    backup via 20.149.171.149, Ethernet24, label 20024
 20254   A[1]
                via M, forward
                    EgressACL: apply
                    20.149.171.149 Ethernet24
                    20.170.171.170 Ethernet1
 20343   A[1]
                via M, ::, forward
                    EgressACL: apply
                  via TI-LFA tunnel index 1
                    via 20.149.171.149, Ethernet24, label imp-null(3)
                    backup via 20.170.171.170, Ethernet1, label imp-null(3)
 20349   A[1]
                via M, ::, pop
                    EgressACL: apply
                  via TI-LFA tunnel index 4
                    via 20.149.171.149, Ethernet24, label imp-null(3)
                    backup via 20.170.171.170, Ethernet1, label 20349
 20355   A[1]
                via M, ::, forward
                    EgressACL: apply
                  via TI-LFA tunnel index 1
                    via 20.149.171.149, Ethernet24, label imp-null(3)
                    backup via 20.170.171.170, Ethernet1, label imp-null(3)
 21283   A[1]
                via M, forward
                    EgressACL: apply
                    20.149.171.149 Ethernet24
 21355   A[1]
                via M, forward
                    EgressACL: apply
                    20.149.171.149 Ethernet24
 21449   A[1]
                via M, pop
                    EgressACL: apply
                    20.149.171.149 Ethernet24
 21455   A[1]
                via M, forward
                    EgressACL: apply
                    20.149.171.149 Ethernet24
 21549   A[1]
                via M, ::, pop
                    EgressACL: apply
                  via TI-LFA tunnel index 2
                    via 20.149.171.149, Ethernet24, label imp-null(3)
                    backup via 20.170.171.170, Ethernet1, label 21555 21549
 21555   A[1]
                via M, ::, forward
                    EgressACL: apply
                  via TI-LFA tunnel index 1
                    via 20.149.171.149, Ethernet24, label imp-null(3)
                    backup via 20.170.171.170, Ethernet1, label imp-null(3)
 21649   A[1]
                via M, forward
                    EgressACL: apply
                    20.170.171.170 Ethernet1
 21655   A[1]
                via M, forward
                    EgressACL: apply
                    20.170.171.170 Ethernet1
 362144  A[1]
                via M, 20.149.171.149, pop
                    EgressACL: apply
                    directly connected, Ethernet24
                    c0:f8:7f:6a:4e:1c, vlan 1007
 362145  A[1]
                via M, 20.170.171.170, pop
                    EgressACL: apply
                    directly connected, Ethernet1
                    28:99:3a:06:b4:e1, vlan 1006
 378528   [0]
                via I, ipv4, vrf ISIS-SR-FLEXALGO-MIN-IGP-ADMIN
 378530   [0]
                via I, ipv4, vrf ISIS-SR-FLEXALGO-MIN-TE
 378531   [0]
                via I, ipv4, vrf ISIS-SR-FLEXALGO-MIN-DELAY
 378532   [0]
                via I, ipv4, vrf ISIS-SR-FLEXALGO-MIN-IGP
 378533   [0]
                via I, ipv4, vrf ISIS-SR-L3VPN
 1000001 A[1]
                SR-TE Policy 10.0.1.55, color 10, pop
                    EgressACL: apply
                  via SR-TE tunnel index 5
                    via TI-LFA tunnel index 0, label 20355
                       via 20.170.171.170, Ethernet1, label imp-null(3)
                       backup via 20.149.171.149, Ethernet24, label 20254 20170
 1000004 A[1]
                SR-TE Policy 10.0.0.32, color 211, pop
                    EgressACL: apply
                  via SR-TE tunnel index 1
                    via TI-LFA tunnel index 0, label 20032
                       via 20.170.171.170, Ethernet1, label imp-null(3)
                       backup via 20.149.171.149, Ethernet24, label 20254 20170
 1000009 A[1]
                SR-TE Policy 10.0.0.5, color 211, pop
                    EgressACL: apply
                  via SR-TE tunnel index 14
                    via TI-LFA tunnel index 0, label 20005
                       via 20.170.171.170, Ethernet1, label imp-null(3)
                       backup via 20.149.171.149, Ethernet24, label 20254 20170
 1000011 A[1]
                SR-TE Policy 10.0.1.55, color 20, pop
                    EgressACL: apply
                  via SR-TE tunnel index 16
                    via TI-LFA tunnel index 4, label 20355
                       via 20.149.171.149, Ethernet24, label imp-null(3)
                       backup via 20.170.171.170, Ethernet1, label 20349
 1000019 A[1]
                SR-TE Policy 10.0.0.57, color 40, pop
                    EgressACL: apply
                  via SR-TE tunnel index 18
                    via TI-LFA tunnel index 0, label 20057
                       via 20.170.171.170, Ethernet1, label imp-null(3)
                       backup via 20.149.171.149, Ethernet24, label 20254 20170
```

## show mpls lfib route

```text
MPLS forwarding table (Label [metric] Vias) - 32 routes 
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
                via M, 20.149.171.149, forward
                 payload autoDecide, ttlMode uniform, dscpMode uniform, apply egress-acl
                 interface Ethernet24
                via M, 20.170.171.170, forward
                 payload autoDecide, ttlMode uniform, dscpMode uniform, apply egress-acl
                 interface Ethernet1
 IP    20019    [1], 10.0.0.19/32
                via M, 20.149.171.149, forward
                 payload autoDecide, ttlMode uniform, dscpMode uniform, apply egress-acl
                 interface Ethernet24
                via M, 20.170.171.170, forward
                 payload autoDecide, ttlMode uniform, dscpMode uniform, apply egress-acl
                 interface Ethernet1
 IP    20024    [1], 10.0.0.24/32
                via M, 20.149.171.149, forward
                 payload autoDecide, ttlMode uniform, dscpMode uniform, apply egress-acl
                 interface Ethernet24
                via M, 20.170.171.170, forward
                 payload autoDecide, ttlMode uniform, dscpMode uniform, apply egress-acl
                 interface Ethernet1
 IP    20032    [1], 10.0.0.32/32
                via TI-LFA tunnel index 1, forward
                 payload autoDecide, ttlMode uniform, dscpMode uniform, apply egress-acl
                    via 20.149.171.149, Ethernet24, label imp-null(3)
                    backup via 20.170.171.170, Ethernet1, label imp-null(3)
 IP    20057    [1], 10.0.0.57/32
                via TI-LFA tunnel index 8, forward
                 payload autoDecide, ttlMode uniform, dscpMode uniform, apply egress-acl
                    via 20.170.171.170, Ethernet1, label imp-null(3)
                    backup via 20.149.171.149, Ethernet24, label imp-null(3)
 IP    20170    [1], 10.0.0.170/32
                via TI-LFA tunnel index 0, pop
                 payload autoDecide, ttlMode uniform, dscpMode uniform, apply egress-acl
                    via 20.170.171.170, Ethernet1, label imp-null(3)
                    backup via 20.149.171.149, Ethernet24, label 20254 20170
 IP    20209    [1], 209.209.209.209/32
                via TI-LFA tunnel index 1, forward
                 payload autoDecide, ttlMode uniform, dscpMode uniform, apply egress-acl
                    via 20.149.171.149, Ethernet24, label imp-null(3)
                    backup via 20.170.171.170, Ethernet1, label imp-null(3)
 IP    20212    [1], 10.0.0.212/32
                via TI-LFA tunnel index 3, forward
                 payload autoDecide, ttlMode uniform, dscpMode uniform, apply egress-acl
                    via 20.170.171.170, Ethernet1, label imp-null(3)
                    backup via 20.149.171.149, Ethernet24, label 20024
 IP    20254    [1], 10.0.0.254/32
                via M, 20.149.171.149, forward
                 payload autoDecide, ttlMode uniform, dscpMode uniform, apply egress-acl
                 interface Ethernet24
                via M, 20.170.171.170, forward
                 payload autoDecide, ttlMode uniform, dscpMode uniform, apply egress-acl
                 interface Ethernet1
 IP    20343    [1], 10.0.1.43/32
                via TI-LFA tunnel index 1, forward
                 payload autoDecide, ttlMode uniform, dscpMode uniform, apply egress-acl
                    via 20.149.171.149, Ethernet24, label imp-null(3)
                    backup via 20.170.171.170, Ethernet1, label imp-null(3)
 IP    20349    [1], 10.0.1.49/32
                via TI-LFA tunnel index 4, pop
                 payload autoDecide, ttlMode uniform, dscpMode uniform, apply egress-acl
                    via 20.149.171.149, Ethernet24, label imp-null(3)
                    backup via 20.170.171.170, Ethernet1, label 20349
 IP    20355    [1], 10.0.1.55/32
                via TI-LFA tunnel index 1, forward
                 payload autoDecide, ttlMode uniform, dscpMode uniform, apply egress-acl
                    via 20.149.171.149, Ethernet24, label imp-null(3)
                    backup via 20.170.171.170, Ethernet1, label imp-null(3)
 IP    21283    [1], 10.0.0.254/32, algorithm MIN-LATENCY
                via M, 20.149.171.149, forward
                 payload autoDecide, ttlMode uniform, dscpMode uniform, apply egress-acl
                 interface Ethernet24
 IP    21355    [1], 10.0.1.55/32, algorithm MIN-LATENCY
                via M, 20.149.171.149, forward
                 payload autoDecide, ttlMode uniform, dscpMode uniform, apply egress-acl
                 interface Ethernet24
 IP    21449    [1], 10.0.1.49/32, algorithm MIN-TE
                via M, 20.149.171.149, pop
                 payload autoDecide, ttlMode uniform, dscpMode uniform, apply egress-acl
                 interface Ethernet24
 IP    21455    [1], 10.0.1.55/32, algorithm MIN-TE
                via M, 20.149.171.149, forward
                 payload autoDecide, ttlMode uniform, dscpMode uniform, apply egress-acl
                 interface Ethernet24
 IP    21549    [1], 10.0.1.49/32, algorithm MIN-IGP
                via TI-LFA tunnel index 2, pop
                 payload autoDecide, ttlMode uniform, dscpMode uniform, apply egress-acl
                    via 20.149.171.149, Ethernet24, label imp-null(3)
                    backup via 20.170.171.170, Ethernet1, label 21555 21549
 IP    21555    [1], 10.0.1.55/32, algorithm MIN-IGP
                via TI-LFA tunnel index 1, forward
                 payload autoDecide, ttlMode uniform, dscpMode uniform, apply egress-acl
                    via 20.149.171.149, Ethernet24, label imp-null(3)
                    backup via 20.170.171.170, Ethernet1, label imp-null(3)
 IP    21649    [1], 10.0.1.49/32, algorithm MIN-IGP-ADMIN
                via M, 20.170.171.170, forward
                 payload autoDecide, ttlMode uniform, dscpMode uniform, apply egress-acl
                 interface Ethernet1
 IP    21655    [1], 10.0.1.55/32, algorithm MIN-IGP-ADMIN
                via M, 20.170.171.170, forward
                 payload autoDecide, ttlMode uniform, dscpMode uniform, apply egress-acl
                 interface Ethernet1
 IA    362144   [1]
                via M, 20.149.171.149, pop
                 payload autoDecide, ttlMode uniform, apply egress-acl
                 interface Ethernet24
 IA    362145   [1]
                via M, 20.170.171.170, pop
                 payload autoDecide, ttlMode uniform, apply egress-acl
                 interface Ethernet1
 B3    378528   [0]
                via I, ipv4, vrf ISIS-SR-FLEXALGO-MIN-IGP-ADMIN
 B3    378530   [0]
                via I, ipv4, vrf ISIS-SR-FLEXALGO-MIN-TE
 B3    378531   [0]
                via I, ipv4, vrf ISIS-SR-FLEXALGO-MIN-DELAY
 B3    378532   [0]
                via I, ipv4, vrf ISIS-SR-FLEXALGO-MIN-IGP
 B3    378533   [0]
                via I, ipv4, vrf ISIS-SR-L3VPN
 ST    1000001  [1], SR-TE Policy 10.0.1.55, color 10
                via SR-TE tunnel index 5, pop
                 payload autoDecide, ttlMode uniform, dscpMode uniform, apply egress-acl
                    via TI-LFA tunnel index 0, label 20355
                       via 20.170.171.170, Ethernet1, label imp-null(3)
                       backup via 20.149.171.149, Ethernet24, label 20254 20170
 ST    1000004  [1], SR-TE Policy 10.0.0.32, color 211
                via SR-TE tunnel index 1, pop
                 payload autoDecide, ttlMode uniform, dscpMode uniform, apply egress-acl
                    via TI-LFA tunnel index 0, label 20032
                       via 20.170.171.170, Ethernet1, label imp-null(3)
                       backup via 20.149.171.149, Ethernet24, label 20254 20170
 ST    1000009  [1], SR-TE Policy 10.0.0.5, color 211
                via SR-TE tunnel index 14, pop
                 payload autoDecide, ttlMode uniform, dscpMode uniform, apply egress-acl
                    via TI-LFA tunnel index 0, label 20005
                       via 20.170.171.170, Ethernet1, label imp-null(3)
                       backup via 20.149.171.149, Ethernet24, label 20254 20170
 ST    1000011  [1], SR-TE Policy 10.0.1.55, color 20
                via SR-TE tunnel index 16, pop
                 payload autoDecide, ttlMode uniform, dscpMode uniform, apply egress-acl
                    via TI-LFA tunnel index 4, label 20355
                       via 20.149.171.149, Ethernet24, label imp-null(3)
                       backup via 20.170.171.170, Ethernet1, label 20349
 ST    1000019  [1], SR-TE Policy 10.0.0.57, color 40
                via SR-TE tunnel index 18, pop
                 payload autoDecide, ttlMode uniform, dscpMode uniform, apply egress-acl
                    via TI-LFA tunnel index 0, label 20057
                       via 20.170.171.170, Ethernet1, label imp-null(3)
                       backup via 20.149.171.149, Ethernet24, label 20254 20170
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
Router identifier 10.0.0.171, local AS number 65000
Route status codes: * - valid, > - active, S - Stale, E - ECMP head, e - ECMP
                    c - Contributing to ECMP, % - Pending best path selection
Origin codes: i - IGP, e - EGP, ? - incomplete
AS Path Attributes: Or-ID - Originator ID, C-LST - Cluster List, LL Nexthop - Link Local Nexthop

          Network                Next Hop              Metric  LocPref Weight  Path
```

## show bgp vpn-ipv4

```text
BGP routing table information for VRF default
Router identifier 10.0.0.171, local AS number 65000
Route status codes: s - suppressed contributor, * - valid, > - active, E - ECMP head, e - ECMP
                    S - Stale, c - Contributing to ECMP, b - backup, L - labeled-unicast
                    % - Pending best path selection
Origin codes: i - IGP, e - EGP, ? - incomplete
AS Path Attributes: Or-ID - Originator ID, C-LST - Cluster List, LL Nexthop - Link Local Nexthop

          Network                Next Hop              Metric  LocPref Weight  Path
 * >      RD: 65000:1 IPv4 prefix 20.32.111.0/24
                                 10.0.0.32             -       100     0       i
 * >      RD: 10.0.0.57:10000 IPv4 prefix 20.54.1.0/24
                                 10.0.0.57             -       100     0       i
 * >      RD: 10.0.0.57:1 IPv4 prefix 20.57.111.0/24
                                 10.0.0.57             -       100     0       i
 * >      RD: 10.0.0.57:128 IPv4 prefix 20.57.111.0/24
                                 10.0.0.57             -       100     0       i
 * >      RD: 10.0.0.57:129 IPv4 prefix 20.57.111.0/24
                                 10.0.0.57             -       100     0       i
 * >      RD: 10.0.0.57:130 IPv4 prefix 20.57.111.0/24
                                 10.0.0.57             -       100     0       i
 * >      RD: 10.0.0.57:131 IPv4 prefix 20.57.111.0/24
                                 10.0.0.57             -       100     0       i
 * >      RD: 10.0.0.57:132 IPv4 prefix 20.57.111.0/24
                                 10.0.0.57             -       100     0       i
 * >      RD: 10.0.0.57:211 IPv4 prefix 20.57.111.0/24
                                 10.0.0.57             -       100     0       i
 * >      RD: 65000:140 IPv4 prefix 20.111.155.0/24
                                 10.0.1.55             0       100     0       ?
 * >      RD: 65000:141 IPv4 prefix 20.111.155.0/24
                                 10.0.1.55             0       100     0       ?
 * >      RD: 65000:142 IPv4 prefix 20.111.155.0/24
                                 10.0.1.55             0       100     0       ?
 * >      RD: 10.0.1.55:128 IPv4 prefix 20.111.155.0/24
                                 10.0.1.55             0       100     0       ?
 * >      RD: 10.0.1.55:129 IPv4 prefix 20.111.155.0/24
                                 10.0.1.55             0       100     0       ?
 * >      RD: 10.0.1.55:130 IPv4 prefix 20.111.155.0/24
                                 10.0.1.55             0       100     0       ?
 * >      RD: 10.0.1.55:131 IPv4 prefix 20.111.155.0/24
                                 10.0.1.55             0       100     0       ?
 * >      RD: 10.0.1.55:132 IPv4 prefix 20.111.155.0/24
                                 10.0.1.55             0       100     0       ?
 * >      RD: 10.0.1.55:211 IPv4 prefix 20.111.155.0/24
                                 10.0.1.55             0       100     0       ?
 * >      RD: 10.0.0.171:1 IPv4 prefix 20.111.171.0/24
                                 -                     -       -       0       i
 * >      RD: 10.0.0.171:128 IPv4 prefix 20.111.171.0/24
                                 -                     -       -       0       i
 * >      RD: 10.0.0.171:129 IPv4 prefix 20.111.171.0/24
                                 -                     -       -       0       i
 * >      RD: 10.0.0.171:130 IPv4 prefix 20.111.171.0/24
                                 -                     -       -       0       i
 * >      RD: 10.0.0.171:131 IPv4 prefix 20.111.171.0/24
                                 -                     -       -       0       i
          RD: 10.0.0.179:1812 IPv4 prefix 20.111.179.0/24
                                 10.0.0.179            -       100     0       i
          RD: 10.0.0.179:1813 IPv4 prefix 20.111.179.0/24
                                 10.0.0.179            -       100     0       i
          RD: 10.0.0.179:1814 IPv4 prefix 20.111.179.0/24
                                 10.0.0.179            -       100     0       i
          RD: 10.0.0.179:1815 IPv4 prefix 20.111.179.0/24
                                 10.0.0.179            -       100     0       i
          RD: 10.0.0.179:1816 IPv4 prefix 20.111.179.0/24
                                 10.0.0.179            -       100     0       i
          RD: 10.0.0.179:1817 IPv4 prefix 20.111.179.0/24
                                 10.0.0.179            -       100     0       i
          RD: 10.0.0.179:1823 IPv4 prefix 20.111.179.0/24
                                 10.0.0.179            -       100     0       i
 * >      RD: 10.0.0.212:51 IPv4 prefix 20.111.212.0/24
                                 10.0.0.212            -       100     0       65001 i
 * >      RD: 65000:20254 IPv4 prefix 20.111.254.0/24
                                 10.0.0.254            0       100     0       ?
 * >      RD: 10.0.1.55:130 IPv4 prefix 55.55.55.130/32
                                 10.0.1.55             0       100     0       ?
 * >      RD: 10.0.0.57:6001 IPv4 prefix 57.1.0.0/24
                                 10.0.0.57             -       100     0       i
 * >      RD: 65000:140 IPv4 prefix 155.155.155.140/32
                                 10.0.1.55             0       100     0       ?
 * >      RD: 65000:141 IPv4 prefix 155.155.155.141/32
                                 10.0.1.55             0       100     0       ?
 * >      RD: 65000:142 IPv4 prefix 155.155.155.142/32
                                 10.0.1.55             0       100     0       ?
```

## show bgp vpn-ipv6

```text
BGP routing table information for VRF default
Router identifier 10.0.0.171, local AS number 65000
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
Router identifier 10.0.0.171, local AS number 65000
Route status codes: s - suppressed contributor, * - valid, > - active, E - ECMP head, e - ECMP
                    S - Stale, c - Contributing to ECMP, b - backup, L - labeled-unicast
                    % - Pending best path selection
Origin codes: i - IGP, e - EGP, ? - incomplete
AS Path Attributes: Or-ID - Originator ID, C-LST - Cluster List, LL Nexthop - Link Local Nexthop

          Network                Next Hop              Metric  AIGP       LocPref Weight  Path
 * >  L   10.0.0.171/32          -                     -       -          -       0       i
```

## show bgp neighbors

```text
BGP neighbor is 10.0.0.5, remote AS 65000, internal link
  BGP version 4, remote router ID 10.0.0.5, VRF default
  Inherits configuration from and member of peer-group BGP-LU
  Last read 1d03h, last write 1d03h
  Hold time is 180, keepalive interval is 60 seconds
  Configured hold time is 180, keepalive interval is 60 seconds
  Effective minimum hold time is 3 seconds
  Send failure hold time is 0 seconds
  Hold timer is inactive
  Keepalive timer is inactive
  Connect timer is inactive
  Idle-restart timer is inactive
  BGP state is Idle, Administratively shut down
  Peering failure hint: Administratively shut down
  Number of transitions to established: 5
  Last state was Established
  Last event was Open
  Last sent notification:Cease/connection rejected, Last time 00:00:04, First time 1d03h, Repeats 3612
  Last rcvd notification:Cease/administrative reset, Last time 1d20h
  Last rcvd socket-error:Connection reset by peer, Last time 1d04h, First time 1d20h, Repeats 1
  Types of communities advertised: standard extended large
  Neighbor Capabilities:
    Multiprotocol IPv4 Unicast: advertised
    Multiprotocol IPv4 with MPLS Labels: advertised and received
    Four Octet ASN: advertised
    Route Refresh: advertised and received
    Enhanced route refresh: advertised
    Send End-of-RIB messages: advertised and received
    Additional-paths recv capability:
      IPv4 Unicast: advertised
      IPv4 with MPLS Labels: advertised
    Additional-paths send capability:
    Graceful Restart received:
      Restart-time is 0
      Restart-State bit: no
      Graceful notification: no
      IPv4 with MPLS Labels is enabled, Forwarding State is not preserved
    Multiple labels capability:
      IPv4 with MPLS Labels: advertised with count 13
  Restart timer is inactive
  End of rib timer is inactive
  AIGP attribute send and receive for IPv4 Unicast are enabled
  AIGP attribute send and receive for IPv4 with MPLS Labels are enabled
  AIGP attribute send and receive for IPv6 Unicast are enabled
  AIGP attribute send and receive for IPv6 with MPLS Labels are enabled
  BGP session driven failover for IPv4 Unicast is disabled
  BGP session driven failover for IPv6 Unicast is disabled
  Message Statistics:
                         Sent      Rcvd
    Opens:                  7      4534
    Notifications:       4532         2
    Updates:               10        32
    Keepalives:          1105       930
    Route Refresh:          0         0
    Total messages:      5654      5498
  Prefix Statistics:
                                   Sent      Rcvd     Best Paths     Best ECMP Paths
    IPv4 Unicast:                     0         0              0                   0
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
Local AS is 65000, local router ID 10.0.0.171
TTL is 255
Remote TCP address is 10.0.0.5

BGP neighbor is 10.0.0.19, remote AS 65000, internal link
  BGP version 4, remote router ID 10.0.0.19, VRF default
  Inherits configuration from and member of peer-group OPTION-C-VPN
  Last read 19:40:26, last write 19:41:16
  Hold time is 180, keepalive interval is 60 seconds
  Configured hold time is 180, keepalive interval is 60 seconds
  Effective minimum hold time is 3 seconds
  Send failure hold time is 0 seconds
  Hold timer is inactive
  Keepalive timer is inactive
  Connect timer is active, time left: 00:01:44
  Connection interval is 148 seconds
  Failed connection attempts is 424
  Idle-restart timer is inactive
  BGP state is Active
  Number of transitions to established: 1
  Last state was Connect
  Last event was TransportError
  Last sent notification:Open Message Error/bad AS number, Last time 20:28:36
  Last rcvd notification:Cease/other configuration change, Last time 19:40:26
  Last sent socket-error:Connect (Connection refused), Last time 00:01:18, First time 20:28:56, Repeats 429
  Types of communities advertised: standard extended large
  Neighbor Capabilities:
    Multiprotocol IPv4 Unicast: advertised
    Multiprotocol VPN-IPv4: advertised and received
    Four Octet ASN: advertised and received
    Route Refresh: advertised and received
    Enhanced route refresh: advertised
    Send End-of-RIB messages: advertised
    Additional-paths recv capability:
      IPv4 Unicast: advertised
      VPN-IPv4: advertised
    Additional-paths send capability:
  Restart timer is inactive
  End of rib timer is inactive
  AIGP attribute send and receive for IPv4 Unicast are enabled
  AIGP attribute send and receive for IPv4 with MPLS Labels are enabled
  AIGP attribute send and receive for IPv6 Unicast are enabled
  AIGP attribute send and receive for IPv6 with MPLS Labels are enabled
  BGP session driven failover for IPv4 Unicast is disabled
  BGP session driven failover for IPv6 Unicast is disabled
  Message Statistics:
                         Sent      Rcvd
    Opens:                  2         2
    Notifications:          1         1
    Updates:                7         6
    Keepalives:            58        62
    Route Refresh:          0         0
    Total messages:        68        71
  Prefix Statistics:
                                   Sent      Rcvd     Best Paths     Best ECMP Paths
    IPv4 Unicast:                     0         0              0                   0
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
  Outbound route map for VPN-IPv4 is SET_COLOR171
Local AS is 65000, local router ID 10.0.0.171
TTL is 255
Local TCP address is 10.0.0.171
Remote TCP address is 10.0.0.19, remote port is 179

BGP neighbor is 10.0.0.32, remote AS 65000, internal link
  BGP version 4, remote router ID 10.0.0.32, VRF default
  Inherits configuration from and member of peer-group OPTION-C-VPN
  Last read 00:00:18, last write 00:00:21
  Hold time is 180, keepalive interval is 60 seconds
  Configured hold time is 180, keepalive interval is 60 seconds
  Effective minimum hold time is 3 seconds
  Send failure hold time is 0 seconds
  Hold timer is active, time left: 00:02:42
  Keepalive timer is active, time left: 00:00:30
  Connect timer is inactive
  Idle-restart timer is inactive
  BGP state is Established, up for 1d00h
  Number of transitions to established: 5
  Last state was OpenConfirm
  Last event was ReapplyOutboundPolicy
  Last sent notification:Open Message Error/unsupported capability, Last time 1d00h, First time 1d00h, Repeats 4
    Sent data: 0x010400010001010400010004
  Last sent socket-error:Connect (Connection refused), Last time 1d00h, First time 1d02h, Repeats 40
  Last rcvd socket-error:Connection reset by peer, Last time 1d02h, First time 1d20h, Repeats 4
  Types of communities advertised: standard extended large
  Enhanced route refresh stale path removal disabled
  Outbound enhanced route refresh enabled
  Neighbor Capabilities:
    Multiprotocol IPv4 Unicast: advertised
    Multiprotocol VPN-IPv4: advertised and received and negotiated
    Four Octet ASN: advertised and received and negotiated
    Route Refresh: advertised and received and negotiated
    Enhanced route refresh: advertised and received and negotiated
    Send End-of-RIB messages: advertised
    Additional-paths recv capability:
      IPv4 Unicast: advertised
      VPN-IPv4: advertised
    Additional-paths send capability:
  Restart timer is inactive
  End of rib timer is inactive
    VPN-IPv4 End-of-RIB received: No
      Number of stale paths removed after graceful restart: 0
  AIGP attribute send and receive for IPv4 Unicast are enabled
  AIGP attribute send and receive for IPv4 with MPLS Labels are enabled
  AIGP attribute send and receive for IPv6 Unicast are enabled
  AIGP attribute send and receive for IPv6 with MPLS Labels are enabled
  BGP session driven failover for IPv4 Unicast is disabled
  BGP session driven failover for IPv6 Unicast is disabled
  Message Statistics:
                                  Sent      Rcvd
    Opens:                          14      3875
    Notifications:                3873         0
    Updates:                      1315        36
    Keepalives:                   1865      4463
    Enhanced Route Refresh:          0         4
    Begin of Route Refresh:          4         0
    End of Route Refresh:            4         0
    Total messages:               7075      8378
  Prefix Statistics:
                                   Sent      Rcvd     Best Paths     Best ECMP Paths
    IPv4 Unicast:                     0         0              0                   0
    VPN-IPv4:                         6         1              1                   0
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
  Outbound route map for VPN-IPv4 is SET_COLOR_211
Local AS is 65000, local router ID 10.0.0.171
TTL is 255
Local TCP address is 10.0.0.171, local port is 37477
Remote TCP address is 10.0.0.32, remote port is 179
Local next hop for next hop self:
  VPN-IPv4: 10.0.0.171
TCP Socket Information:
  TCP state is ESTABLISHED
  Recv-Q: 0/32768
  Send-Q: 0/46080
  Outgoing Maximum Segment Size (MSS): 1448
  Total Number of TCP retransmissions: 6
  Options:
    Timestamps enabled: yes
    Selective Acknowledgments enabled: yes
    Window Scale enabled: yes
    Explicit Congestion Notification (ECN) enabled: no
  Socket Statistics:
    Window Scale (wscale): 9,7
    Retransmission Timeout (rto): 204.0ms
    Round-trip Time (rtt/rtvar): 0.2ms/0.0ms
    Delayed Ack Timeout (ato): 40.0ms
    Congestion Window (cwnd): 3
    Slow-start Threshold (ssthresh): 7
    TCP Throughput: 155.14 Mbps
    Recv Round-trip Time (rcv_rtt): 500813.1ms
    Advertised Recv Window (rcv_space): 64305

BGP neighbor is 10.0.0.47, remote AS 65001, external link
  BGP version 4, remote router ID 10.0.0.47, VRF default
  Inherits configuration from and member of peer-group OPTION-C-VPN
  Last read 02:34:40, last write 02:31:40
  Hold time is 180, keepalive interval is 60 seconds
  Configured hold time is 180, keepalive interval is 60 seconds
  Effective minimum hold time is 3 seconds
  Send failure hold time is 0 seconds
  Hold timer is inactive
  Keepalive timer is inactive
  Connect timer is active, time left: 00:00:35
  Connection interval is 148 seconds
  Failed connection attempts is 73
  Idle-restart timer is inactive
  BGP state is Active
  Number of transitions to established: 8
  Last state was Connect
  Last event was TransportError
  Last sent notification:Hold Timer Expired Error/None, Last time 02:31:40, First time 1d20h, Repeats 5
  Last sent socket-error:Connect (Network is unreachable), Last time 00:01:53, First time 1d22h, Repeats 118
  Last rcvd socket-error:Connection reset by peer, Last time 02:50:53, First time 02:51:17, Repeats 6
  Types of communities advertised: standard extended large
  Neighbor Capabilities:
    Multiprotocol IPv4 Unicast: advertised
    Multiprotocol VPN-IPv4: advertised and received
    Four Octet ASN: advertised and received
    Route Refresh: advertised and received
    Enhanced route refresh: advertised and received
    Send End-of-RIB messages: advertised and received
    Additional-paths recv capability:
      IPv4 Unicast: advertised
      VPN-IPv4: advertised
    Additional-paths send capability:
    Graceful Restart received:
      Restart-time is 120
      Restart-State bit: yes
      Graceful notification: no
      VPN-IPv4 is enabled, Forwarding State is preserved
  Restart timer is inactive
  End of rib timer is inactive
  AIGP attribute send and receive for IPv4 Unicast are disabled
  AIGP attribute send and receive for IPv4 with MPLS Labels are disabled
  AIGP attribute send and receive for IPv6 Unicast are disabled
  AIGP attribute send and receive for IPv6 with MPLS Labels are disabled
  BGP session driven failover for IPv4 Unicast is disabled
  BGP session driven failover for IPv6 Unicast is disabled
  Message Statistics:
                         Sent      Rcvd
    Opens:                 14         8
    Notifications:          6         0
    Updates:            87447        17
    Keepalives:          2887      2518
    Route Refresh:          0         0
    Total messages:     90354      2543
  Prefix Statistics:
                                   Sent      Rcvd     Best Paths     Best ECMP Paths
    IPv4 Unicast:                     0         0              0                   0
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
Local AS is 65000, local router ID 10.0.0.171
TTL is 10, external peer can be 10 hops away
Local TCP address is 10.0.0.171
Remote TCP address is 10.0.0.47, remote port is 179

BGP neighbor is 10.0.0.57, remote AS 65000, internal link
  BGP version 4, remote router ID 10.0.0.57, VRF default
  Inherits configuration from and member of peer-group OPTION-C-VPN
  Last read 00:00:28, last write 00:00:24
  Hold time is 90, keepalive interval is 30 seconds
  Configured hold time is 180, keepalive interval is 60 seconds
  Effective minimum hold time is 3 seconds
  Send failure hold time is 0 seconds
  Hold timer is active, time left: 00:01:02
  Keepalive timer is active, time left: 00:00:00
  Connect timer is inactive
  Idle-restart timer is inactive
  BGP state is Established, up for 03:45:58
  Number of transitions to established: 3
  Last state was OpenConfirm
  Last event was RecvRtRefresh
  Last sent notification:Cease/connection rejected, Last time 1d04h, First time 1d04h, Repeats 3
  Last rcvd notification:Cease/administrative shutdown, Last time 1d02h
  Last sent socket-error:Broken pipe, Last time 03:51:12, First time 1d02h, Repeats 471
  Last rcvd socket-error:Connection reset by peer, Last time 06:13:37, First time 1d03h, Repeats 11
  Types of communities advertised: standard extended large
  Neighbor Capabilities:
    Multiprotocol IPv4 Unicast: advertised
    Multiprotocol VPN-IPv4: advertised and received and negotiated
    Four Octet ASN: advertised and received and negotiated
    Route Refresh: advertised and received and negotiated
    Enhanced route refresh: advertised
    Send End-of-RIB messages: advertised and received and negotiated
    Additional-paths recv capability:
      IPv4 Unicast: advertised
      VPN-IPv4: advertised
    Additional-paths send capability:
  Restart timer is inactive
  End of rib timer is inactive
    VPN-IPv4 End-of-RIB received: Yes
      Received 03:45:25
      Number of stale paths removed after graceful restart: 0
      Number of paths received before End-of-RIB: 9
  AIGP attribute send and receive for IPv4 Unicast are enabled
  AIGP attribute send and receive for IPv4 with MPLS Labels are enabled
  AIGP attribute send and receive for IPv6 Unicast are enabled
  AIGP attribute send and receive for IPv6 with MPLS Labels are enabled
  BGP session driven failover for IPv4 Unicast is disabled
  BGP session driven failover for IPv6 Unicast is disabled
  Message Statistics:
                         Sent      Rcvd
    Opens:                527        80
    Notifications:         78         1
    Updates:               25        25
    Keepalives:           688       586
    Route Refresh:          0         1
    Total messages:      1318       693
  Prefix Statistics:
                                   Sent      Rcvd     Best Paths     Best ECMP Paths
    IPv4 Unicast:                     0         0              0                   0
    VPN-IPv4:                         6         9              9                   0
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
  Outbound route map for VPN-IPv4 is SET_COLOR_57
Local AS is 65000, local router ID 10.0.0.171
TTL is 255
Local TCP address is 10.0.0.171, local port is 179
Remote TCP address is 10.0.0.57, remote port is 55234
Local next hop for next hop self:
  VPN-IPv4: 10.0.0.171
TCP Socket Information:
  TCP state is ESTABLISHED
  Recv-Q: 0/32768
  Send-Q: 0/46080
  Outgoing Maximum Segment Size (MSS): 1012
  Total Number of TCP retransmissions: 0
  Options:
    Timestamps enabled: yes
    Selective Acknowledgments enabled: no
    Window Scale enabled: yes
    Explicit Congestion Notification (ECN) enabled: no
  Socket Statistics:
    Window Scale (wscale): 0,7
    Retransmission Timeout (rto): 204.0ms
    Round-trip Time (rtt/rtvar): 0.4ms/0.1ms
    Delayed Ack Timeout (ato): 40.0ms
    Congestion Window (cwnd): 10
    TCP Throughput: 193.22 Mbps
    Recv Round-trip Time (rcv_rtt): 2813.0ms
    Advertised Recv Window (rcv_space): 14600

BGP neighbor is 10.0.0.59, remote AS 65001, external link
  BGP version 4, remote router ID 10.0.0.59, VRF default
  Inherits configuration from and member of peer-group OPTION-C-VPN
  Last read 21:02:59, last write 21:01:29
  Hold time is 90, keepalive interval is 30 seconds
  Configured hold time is 180, keepalive interval is 60 seconds
  Effective minimum hold time is 3 seconds
  Send failure hold time is 0 seconds
  Hold timer is inactive
  Keepalive timer is inactive
  Connect timer is active, time left: 00:00:09
  Connection interval is 20 seconds
  Failed connection attempts is 464
  Idle-restart timer is inactive
  BGP state is Connect
  Number of transitions to established: 8
  Last state was Active
  Last event was ConnectRetry
  Last sent notification:Hold Timer Expired Error/None, Last time 21:01:29, First time 1d20h, Repeats 5
  Last sent socket-error:Connect (Network is unreachable), Last time 00:04:02, First time 1d22h, Repeats 521
  Types of communities advertised: standard extended large
  Neighbor Capabilities:
    Multiprotocol IPv4 Unicast: advertised
    Multiprotocol VPN-IPv4: advertised and received
    Four Octet ASN: advertised and received
    Route Refresh: advertised and received
    Enhanced route refresh: advertised
    Send End-of-RIB messages: advertised and received
    Additional-paths recv capability:
      IPv4 Unicast: advertised
      VPN-IPv4: advertised
    Additional-paths send capability:
  Restart timer is inactive
  End of rib timer is inactive
  AIGP attribute send and receive for IPv4 Unicast are disabled
  AIGP attribute send and receive for IPv4 with MPLS Labels are disabled
  AIGP attribute send and receive for IPv6 Unicast are disabled
  AIGP attribute send and receive for IPv6 with MPLS Labels are disabled
  BGP session driven failover for IPv4 Unicast is disabled
  BGP session driven failover for IPv6 Unicast is disabled
  Message Statistics:
                         Sent      Rcvd
    Opens:                  8         8
    Notifications:          6         0
    Updates:             5179       576
    Keepalives:          3267      2790
    Route Refresh:          0         0
    Total messages:      8460      3374
  Prefix Statistics:
                                   Sent      Rcvd     Best Paths     Best ECMP Paths
    IPv4 Unicast:                     0         0              0                   0
    IPv6 Unicast:                     0         0              0                   0
  Configured maximum total number of routes is 256000, warning limit is 204800
  Inbound updates dropped by reason:
    AS path loop detection: 7
    Cluster ID loop detection: 0
    Enforced First AS: 0
    Malformed MPBGP routes: 102
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
Local AS is 65000, local router ID 10.0.0.171
TTL is 10, external peer can be 10 hops away
Local TCP address is 10.0.0.171
Remote TCP address is 10.0.0.59, remote port is 179
TCP Socket Information:
  TCP state is SYN-SENT
  Recv-Q: 0/131072
  Send-Q: 0/16384
  Outgoing Maximum Segment Size (MSS): 524
  Total Number of TCP retransmissions: 3
  Options:
    Timestamps enabled: no
    Selective Acknowledgments enabled: no
    Window Scale enabled: no
    Explicit Congestion Notification (ECN) enabled: no
  Socket Statistics:
    Window Scale (wscale): 0,0
    Retransmission Timeout (rto): 8000.0ms
    Round-trip Time (rtt/rtvar): 0.0ms/250.0ms
    Delayed Ack Timeout (ato): 0.0ms
    Congestion Window (cwnd): 1
    Slow-start Threshold (ssthresh): 7

BGP neighbor is 10.0.0.172, remote AS 65000, internal link
  BGP version 4, remote router ID 10.0.0.172, VRF default
  Inherits configuration from and member of peer-group BGP-LU
  Last read 04:10:48, last write 04:07:48
  Hold time is 180, keepalive interval is 60 seconds
  Configured hold time is 180, keepalive interval is 60 seconds
  Effective minimum hold time is 3 seconds
  Send failure hold time is 0 seconds
  Hold timer is inactive
  Keepalive timer is inactive
  Connect timer is active, time left: 00:00:00
  Connection interval is 20 seconds
  Failed connection attempts is 110
  Idle-restart timer is inactive
  BGP state is Connect
  Number of transitions to established: 13
  Last state was Active
  Last event was ConnectRetry
  Last sent notification:Hold Timer Expired Error/None, Last time 04:07:48
  Last rcvd notification:Cease/administrative reset, Last time 1d21h, First time 1d22h, Repeats 9
  Last sent socket-error:Connect (Network is unreachable), Last time 00:05:05, First time 1d22h, Repeats 96
  Types of communities advertised: standard extended large
  Neighbor Capabilities:
    Multiprotocol IPv4 Unicast: advertised and received
    Multiprotocol IPv4 with MPLS Labels: advertised and received
    Four Octet ASN: advertised and received
    Route Refresh: advertised and received
    Enhanced route refresh: advertised and received
    Send End-of-RIB messages: advertised and received
    Additional-paths recv capability:
      IPv4 Unicast: advertised
      IPv4 with MPLS Labels: advertised
    Additional-paths send capability:
      IPv4 Unicast: received
      IPv4 with MPLS Labels: received
    Multiple labels capability:
      IPv4 with MPLS Labels: advertised with count 13
      IPv4 with MPLS Labels: received with count 13
  Restart timer is inactive
  End of rib timer is inactive
  AIGP attribute send and receive for IPv4 Unicast are enabled
  AIGP attribute send and receive for IPv4 with MPLS Labels are enabled
  AIGP attribute send and receive for IPv6 Unicast are enabled
  AIGP attribute send and receive for IPv6 with MPLS Labels are enabled
  BGP session driven failover for IPv4 Unicast is disabled
  BGP session driven failover for IPv6 Unicast is disabled
  Message Statistics:
                         Sent      Rcvd
    Opens:                 13       385
    Notifications:        375        10
    Updates:               35       280
    Keepalives:          1801      1781
    Route Refresh:          0         0
    Total messages:      2224      2456
  Prefix Statistics:
                                   Sent      Rcvd     Best Paths     Best ECMP Paths
    IPv4 Unicast:                     0         0              0                   0
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
Local AS is 65000, local router ID 10.0.0.171
TTL is 255
Local TCP address is 10.0.0.171
Remote TCP address is 10.0.0.172, remote port is 179
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

BGP neighbor is 10.0.0.179, remote AS 65000, internal link
  BGP version 4, remote router ID 10.0.0.179, VRF default
  Inherits configuration from and member of peer-group OPTION-C-VPN
  Last read 00:00:30, last write 00:00:02
  Hold time is 90, keepalive interval is 30 seconds
  Configured hold time is 180, keepalive interval is 60 seconds
  Effective minimum hold time is 3 seconds
  Send failure hold time is 0 seconds
  Hold timer is active, time left: 00:01:00
  Keepalive timer is active, time left: 00:00:19
  Connect timer is inactive
  Idle-restart timer is inactive
  BGP state is Established, up for 21:34:04
  Number of transitions to established: 5
  Last state was OpenConfirm
  Last event was RecvRtRefresh
  Last sent notification:Open Message Error/bad AS number, Last time 21:37:03, First time 23:32:15, Repeats 61
  Last rcvd notification:Cease/peer de-configured, Last time 22:25:11, First time 23:32:16, Repeats 1
  Last sent socket-error:Connect (Network is unreachable), Last time 1d22h, First time 1d22h, Repeats 6
  Types of communities advertised: standard extended large
  Neighbor Capabilities:
    Multiprotocol IPv4 Unicast: advertised and received and negotiated
    Multiprotocol VPN-IPv4: advertised and received and negotiated
    Four Octet ASN: advertised and received and negotiated
    Route Refresh: advertised and received and negotiated
    Enhanced route refresh: advertised
    Send End-of-RIB messages: advertised and received and negotiated
    Additional-paths recv capability:
      IPv4 Unicast: advertised
      VPN-IPv4: advertised
    Additional-paths send capability:
    Long Lived Graceful Restart received:
      Helper only
  Restart timer is inactive
  End of rib timer is inactive
    IPv4 Unicast End-of-RIB received: Yes
      Received 21:34:04
      Number of stale paths removed after graceful restart: 0
    VPN-IPv4 End-of-RIB received: Yes
      Received 21:34:04
      Number of stale paths removed after graceful restart: 0
      Number of paths received before End-of-RIB: 7
  AIGP attribute send and receive for IPv4 Unicast are enabled
  AIGP attribute send and receive for IPv4 with MPLS Labels are enabled
  AIGP attribute send and receive for IPv6 Unicast are enabled
  AIGP attribute send and receive for IPv6 with MPLS Labels are enabled
  BGP session driven failover for IPv4 Unicast is disabled
  BGP session driven failover for IPv6 Unicast is disabled
  Message Statistics:
                         Sent      Rcvd
    Opens:                 67       510
    Notifications:        507         2
    Updates:             1361       865
    Keepalives:          3839      3550
    Route Refresh:          0        23
    Total messages:      5774      4950
  Prefix Statistics:
                                   Sent      Rcvd     Best Paths     Best ECMP Paths
    IPv4 Unicast:                     0        46             46                   0
    VPN-IPv4:                         6         7              0                   0
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
    IPv4 unicast NLRIs dropped due to martian prefix: 6
    IPv4 unicast NLRIs dropped due to maximum route limit violation: 0
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
  Outbound route map for VPN-IPv4 is SET_COLOR_33
Local AS is 65000, local router ID 10.0.0.171
TTL is 255
Local TCP address is 10.0.0.171, local port is 179
Remote TCP address is 10.0.0.179, remote port is 50358
Local next hop for next hop self:
  IPv4 Unicast: 10.0.0.171
  VPN-IPv4: 10.0.0.171
TCP Socket Information:
  TCP state is ESTABLISHED
  Recv-Q: 0/32768
  Send-Q: 0/46080
  Outgoing Maximum Segment Size (MSS): 1448
  Total Number of TCP retransmissions: 5
  Options:
    Timestamps enabled: yes
    Selective Acknowledgments enabled: yes
    Window Scale enabled: yes
    Explicit Congestion Notification (ECN) enabled: no
  Socket Statistics:
    Window Scale (wscale): 0,7
    Retransmission Timeout (rto): 308.0ms
    Round-trip Time (rtt/rtvar): 104.5ms/1.7ms
    Delayed Ack Timeout (ato): 40.0ms
    Congestion Window (cwnd): 2
    Slow-start Threshold (ssthresh): 2
    TCP Throughput: 0.22 Mbps
    Recv Round-trip Time (rcv_rtt): 1273.8ms
    Advertised Recv Window (rcv_space): 58154

BGP neighbor is 10.0.0.212, remote AS 65001, external link
  BGP version 4, remote router ID 10.0.0.212, VRF default
  Inherits configuration from and member of peer-group OPTION-C-VPN
  Last read 00:00:05, last write 00:00:14
  Hold time is 90, keepalive interval is 30 seconds
  Configured hold time is 180, keepalive interval is 60 seconds
  Effective minimum hold time is 3 seconds
  Send failure hold time is 0 seconds
  Hold timer is active, time left: 00:01:25
  Keepalive timer is active, time left: 00:00:15
  Connect timer is inactive
  Idle-restart timer is inactive
  BGP state is Established, up for 01:11:31
  Number of transitions to established: 10
  Last state was OpenConfirm
  Last event was RecvUpdate
  Last sent notification:Hold Timer Expired Error/None, Last time 01:14:21, First time 1d04h, Repeats 4
  Last rcvd notification:Hold Timer Expired Error/None, Last time 1d03h
  Last sent socket-error:Connect (Network is unreachable), Last time 01:12:39, First time 1d04h, Repeats 23
  Types of communities advertised: standard extended large
  Neighbor Capabilities:
    Multiprotocol IPv4 Unicast: advertised
    Multiprotocol VPN-IPv4: advertised and received and negotiated
    Four Octet ASN: advertised and received and negotiated
    Route Refresh: advertised and received and negotiated
    Enhanced route refresh: advertised
    Send End-of-RIB messages: advertised and received and negotiated
    Additional-paths recv capability:
      IPv4 Unicast: advertised
      VPN-IPv4: advertised
    Additional-paths send capability:
    Long Lived Graceful Restart received:
      Helper only
  Restart timer is inactive
  End of rib timer is inactive
    VPN-IPv4 End-of-RIB received: Yes
      Received 01:11:30
      Number of stale paths removed after graceful restart: 0
      Number of paths received before End-of-RIB: 1
  AIGP attribute send and receive for IPv4 Unicast are disabled
  AIGP attribute send and receive for IPv4 with MPLS Labels are disabled
  AIGP attribute send and receive for IPv6 Unicast are disabled
  AIGP attribute send and receive for IPv6 with MPLS Labels are disabled
  BGP session driven failover for IPv4 Unicast is disabled
  BGP session driven failover for IPv6 Unicast is disabled
  Message Statistics:
                         Sent      Rcvd
    Opens:                 32        32
    Notifications:         23         7
    Updates:            66006        20
    Keepalives:          6329      6043
    Route Refresh:          0         0
    Total messages:     72390      6102
  Prefix Statistics:
                                   Sent      Rcvd     Best Paths     Best ECMP Paths
    IPv4 Unicast:                     0         0              0                   0
    VPN-IPv4:                        29         1              1                   0
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
Local AS is 65000, local router ID 10.0.0.171
TTL is 10, external peer can be 10 hops away
Local TCP address is 10.0.0.171, local port is 42321
Remote TCP address is 10.0.0.212, remote port is 179
Local next hop for next hop self:
  VPN-IPv4: 10.0.0.171
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
    Round-trip Time (rtt/rtvar): 0.5ms/0.1ms
    Delayed Ack Timeout (ato): 40.0ms
    Congestion Window (cwnd): 10
    TCP Throughput: 251.83 Mbps
    Advertised Recv Window (rcv_space): 14480

BGP neighbor is 10.0.0.254, remote AS 65000, internal link
  BGP version 4, remote router ID 10.0.0.254, VRF default
  Inherits configuration from and member of peer-group OPTION-C-VPN
  Last read 00:00:04, last write 00:00:09
  Hold time is 180, keepalive interval is 60 seconds
  Configured hold time is 180, keepalive interval is 60 seconds
  Effective minimum hold time is 3 seconds
  Send failure hold time is 0 seconds
  Hold timer is active, time left: 00:02:56
  Keepalive timer is active, time left: 00:00:38
  Connect timer is inactive
  Idle-restart timer is inactive
  BGP state is Established, up for 21:44:44
  Number of transitions to established: 2
  Last state was OpenConfirm
  Last event was RecvRtRefresh
  Last sent notification:Open Message Error/bad AS number, Last time 21:44:54, First time 21:45:03, Repeats 1
  Last rcvd socket-error:Connection reset by peer, Last time 21:44:49, First time 21:45:04, Repeats 2
  Types of communities advertised: standard extended large
  Neighbor Capabilities:
    Multiprotocol IPv4 Unicast: advertised and received and negotiated
    Multiprotocol VPN-IPv4: advertised and received and negotiated
    Four Octet ASN: advertised and received and negotiated
    Route Refresh: advertised and received and negotiated
    Enhanced route refresh: advertised
    Send End-of-RIB messages: advertised
    Additional-paths recv capability:
      IPv4 Unicast: advertised
      VPN-IPv4: advertised
    Additional-paths send capability:
  Restart timer is inactive
  End of rib timer is inactive
    IPv4 Unicast End-of-RIB received: No
      Number of stale paths removed after graceful restart: 0
    VPN-IPv4 End-of-RIB received: No
      Number of stale paths removed after graceful restart: 0
  AIGP attribute send and receive for IPv4 Unicast are enabled
  AIGP attribute send and receive for IPv4 with MPLS Labels are enabled
  AIGP attribute send and receive for IPv6 Unicast are enabled
  AIGP attribute send and receive for IPv6 with MPLS Labels are enabled
  BGP session driven failover for IPv4 Unicast is disabled
  BGP session driven failover for IPv6 Unicast is disabled
  Message Statistics:
                         Sent      Rcvd
    Opens:                  7      6522
    Notifications:       6521         0
    Updates:             1196        24
    Keepalives:          1583      1583
    Route Refresh:          0         3
    Total messages:      9307      8132
  Prefix Statistics:
                                   Sent      Rcvd     Best Paths     Best ECMP Paths
    IPv4 Unicast:                     0         0              0                   0
    VPN-IPv4:                         6         1              1                   0
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
    VPN-IPv4 NLRIs dropped due to maximum route limit violation: 0
    VPN-IPv6 NLRIs dropped due to route import match failure: 0
    L2VPN EVPN NLRIs dropped due to route import match failure: 0
    L2VPN EVPN NLRIs dropped due to unsupported route type: 0
    Link-state NLRIs dropped because reception is unsupported: 0
    RT Membership NLRIs dropped due to local origin ASN received from external peer: 0
  Outbound paths dropped by reason:
    IPv4 local address not available: 0
    IPv6 local address not available: 0
  Outbound route map for VPN-IPv4 is SET_COLOR171
Local AS is 65000, local router ID 10.0.0.171
TTL is 255
Local TCP address is 10.0.0.171, local port is 179
Remote TCP address is 10.0.0.254, remote port is 54799
Local next hop for next hop self:
  IPv4 Unicast: 10.0.0.171
  VPN-IPv4: 10.0.0.171
TCP Socket Information:
  TCP state is ESTABLISHED
  Recv-Q: 0/32768
  Send-Q: 0/46080
  Outgoing Maximum Segment Size (MSS): 1460
  Total Number of TCP retransmissions: 24
  Options:
    Timestamps enabled: no
    Selective Acknowledgments enabled: no
    Window Scale enabled: no
    Explicit Congestion Notification (ECN) enabled: no
  Socket Statistics:
    Window Scale (wscale): 0,0
    Retransmission Timeout (rto): 436.0ms
    Round-trip Time (rtt/rtvar): 174.2ms/58.0ms
    Delayed Ack Timeout (ato): 40.0ms
    Congestion Window (cwnd): 2
    Slow-start Threshold (ssthresh): 2
    TCP Throughput: 0.13 Mbps
    Advertised Recv Window (rcv_space): 14600

BGP neighbor is 10.0.1.49, remote AS 65000, internal link
  BGP version 4, remote router ID 0.0.0.0, VRF default
  Inherits configuration from and member of peer-group IBGP-PEER
  Last read never, last write never
  Hold time is 0, keepalive interval is 0 seconds
  Configured hold time is 180, keepalive interval is 60 seconds
  Effective minimum hold time is 3 seconds
  Send failure hold time is 0 seconds
  Hold timer is inactive
  Keepalive timer is inactive
  Connect timer is active, time left: 00:02:22
  Connection interval is 148 seconds
  Failed connection attempts is 633
  Idle-restart timer is inactive
  BGP state is Active
  Number of transitions to established: 0
  Last state was Connect
  Last event was TransportError
  Last sent socket-error:Connect (Connection refused), Last time 00:00:22, First time 1d05h, Repeats 632
  Types of communities advertised: standard extended large
  Neighbor Capabilities:
  Restart timer is inactive
  End of rib timer is inactive
  AIGP attribute send and receive for IPv4 Unicast are enabled
  AIGP attribute send and receive for IPv4 with MPLS Labels are enabled
  AIGP attribute send and receive for IPv6 Unicast are enabled
  AIGP attribute send and receive for IPv6 with MPLS Labels are enabled
  BGP session driven failover for IPv4 Unicast is disabled
  BGP session driven failover for IPv6 Unicast is disabled
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
    VPN-IPv6 NLRIs dropped due to route import match failure: 0
    L2VPN EVPN NLRIs dropped due to route import match failure: 0
    L2VPN EVPN NLRIs dropped due to unsupported route type: 0
    Link-state NLRIs dropped because reception is unsupported: 0
    RT Membership NLRIs dropped due to local origin ASN received from external peer: 0
  Outbound paths dropped by reason:
    IPv4 local address not available: 0
    IPv6 local address not available: 0
  Outbound route map is RM-FLEXALGO
Local AS is 65000, local router ID 10.0.0.171
TTL is 255
Local TCP address is 10.0.0.171
Remote TCP address is 10.0.1.49, remote port is 179

BGP neighbor is 10.0.1.55, remote AS 65000, internal link
  BGP version 4, remote router ID 10.0.1.55, VRF default
  Inherits configuration from and member of peer-group OPTION-C-VPN
  Last read 00:00:40, last write 00:00:23
  Hold time is 180, keepalive interval is 60 seconds
  Configured hold time is 180, keepalive interval is 60 seconds
  Effective minimum hold time is 3 seconds
  Send failure hold time is 0 seconds
  Hold timer is active, time left: 00:02:20
  Keepalive timer is active, time left: 00:00:24
  Connect timer is inactive
  Idle-restart timer is inactive
  BGP state is Established, up for 03:50:14
  Number of transitions to established: 6
  Last state was OpenConfirm
  Last event was RecvRtRefresh
  Last sent notification:Hold Timer Expired Error/None, Last time 22:46:52
  Last rcvd notification:Cease/other configuration change, Last time 03:50:20
  Last sent socket-error:Connect (Network is unreachable), Last time 1d22h, First time 1d22h, Repeats 7
  Last rcvd socket-error:Connection reset by peer, Last time 03:50:19, First time 1d00h, Repeats 2
  Types of communities advertised: standard extended large
  Neighbor Capabilities:
    Multiprotocol IPv4 Unicast: advertised
    Multiprotocol VPN-IPv4: advertised and received and negotiated
    Four Octet ASN: advertised and received and negotiated
    Route Refresh: advertised and received and negotiated
    Enhanced route refresh: advertised
    Send End-of-RIB messages: advertised
    Additional-paths recv capability:
      IPv4 Unicast: advertised
      VPN-IPv4: advertised
    Additional-paths send capability:
    Extended Next-Hop Capability:
      IPv4 Unicast: received
      VPN-IPv4: received
  Restart timer is inactive
  End of rib timer is inactive
    VPN-IPv4 End-of-RIB received: No
      Number of stale paths removed after graceful restart: 0
  AIGP attribute send and receive for IPv4 Unicast are enabled
  AIGP attribute send and receive for IPv4 with MPLS Labels are enabled
  AIGP attribute send and receive for IPv6 Unicast are enabled
  AIGP attribute send and receive for IPv6 with MPLS Labels are enabled
  BGP session driven failover for IPv4 Unicast is disabled
  BGP session driven failover for IPv6 Unicast is disabled
  Message Statistics:
                         Sent      Rcvd
    Opens:                 31      2687
    Notifications:       2685         1
    Updates:             1294        70
    Keepalives:          2017      1749
    Route Refresh:          0         6
    Total messages:      6027      4513
  Prefix Statistics:
                                   Sent      Rcvd     Best Paths     Best ECMP Paths
    IPv4 Unicast:                     0         0              0                   0
    VPN-IPv4:                         6        13             13                   0
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
Local AS is 65000, local router ID 10.0.0.171
TTL is 255
Local TCP address is 10.0.0.171, local port is 42695
Remote TCP address is 10.0.1.55, remote port is 179
Local next hop for next hop self:
  VPN-IPv4: 10.0.0.171
TCP Socket Information:
  TCP state is ESTABLISHED
  Recv-Q: 0/32768
  Send-Q: 0/46080
  Outgoing Maximum Segment Size (MSS): 1240
  Total Number of TCP retransmissions: 1
  Options:
    Timestamps enabled: no
    Selective Acknowledgments enabled: no
    Window Scale enabled: yes
    Explicit Congestion Notification (ECN) enabled: no
  Socket Statistics:
    Window Scale (wscale): 0,7
    Retransmission Timeout (rto): 404.0ms
    Round-trip Time (rtt/rtvar): 202.7ms/1.0ms
    Delayed Ack Timeout (ato): 40.0ms
    Congestion Window (cwnd): 2
    Slow-start Threshold (ssthresh): 7
    TCP Throughput: 0.10 Mbps
    Advertised Recv Window (rcv_space): 14600

BGP neighbor is 2002::59, remote AS 65000, internal link
  BGP version 4, remote router ID 0.0.0.0, VRF default
  Inherits configuration from and member of peer-group IBGP-IPV6
  Last read never, last write never
  Hold time is 0, keepalive interval is 0 seconds
  Configured hold time is 180, keepalive interval is 60 seconds
  Effective minimum hold time is 3 seconds
  Send failure hold time is 0 seconds
  Hold timer is inactive
  Keepalive timer is inactive
  Connect timer is inactive
  Idle-restart timer is inactive
  BGP state is Idle, Administratively shut down
  Peering failure hint: Administratively shut down
  Number of transitions to established: 0
  Last state was Idle
  Last event was AdminShutdown
  Types of communities advertised: standard extended large
  Neighbor Capabilities:
  Restart timer is inactive
  End of rib timer is inactive
  AIGP attribute send and receive for IPv4 Unicast are enabled
  AIGP attribute send and receive for IPv4 with MPLS Labels are enabled
  AIGP attribute send and receive for IPv6 Unicast are enabled
  AIGP attribute send and receive for IPv6 with MPLS Labels are enabled
  BGP session driven failover for IPv4 Unicast is disabled
  BGP session driven failover for IPv6 Unicast is disabled
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
    VPN-IPv6 NLRIs dropped due to route import match failure: 0
    L2VPN EVPN NLRIs dropped due to route import match failure: 0
    L2VPN EVPN NLRIs dropped due to unsupported route type: 0
    Link-state NLRIs dropped because reception is unsupported: 0
    RT Membership NLRIs dropped due to local origin ASN received from external peer: 0
  Outbound paths dropped by reason:
    IPv4 local address not available: 0
    IPv6 local address not available: 0
Local AS is 65000, local router ID 10.0.0.171
TTL is 255

BGP neighbor is 2002::304, remote AS 65000, internal link
  BGP version 4, remote router ID 0.0.0.0, VRF default
  Inherits configuration from and member of peer-group IBGP-IPV6
  Last read never, last write never
  Hold time is 0, keepalive interval is 0 seconds
  Configured hold time is 180, keepalive interval is 60 seconds
  Effective minimum hold time is 3 seconds
  Send failure hold time is 0 seconds
  Hold timer is inactive
  Keepalive timer is inactive
  Connect timer is inactive
  Idle-restart timer is inactive
  BGP state is Idle, Administratively shut down
  Peering failure hint: Administratively shut down
  Number of transitions to established: 0
  Last state was Idle
  Last event was AdminShutdown
  Types of communities advertised: standard extended large
  Neighbor Capabilities:
  Restart timer is inactive
  End of rib timer is inactive
  AIGP attribute send and receive for IPv4 Unicast are enabled
  AIGP attribute send and receive for IPv4 with MPLS Labels are enabled
  AIGP attribute send and receive for IPv6 Unicast are enabled
  AIGP attribute send and receive for IPv6 with MPLS Labels are enabled
  BGP session driven failover for IPv4 Unicast is disabled
  BGP session driven failover for IPv6 Unicast is disabled
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
    VPN-IPv6 NLRIs dropped due to route import match failure: 0
    L2VPN EVPN NLRIs dropped due to route import match failure: 0
    L2VPN EVPN NLRIs dropped due to unsupported route type: 0
    Link-state NLRIs dropped because reception is unsupported: 0
    RT Membership NLRIs dropped due to local origin ASN received from external peer: 0
  Outbound paths dropped by reason:
    IPv4 local address not available: 0
    IPv6 local address not available: 0
Local AS is 65000, local router ID 10.0.0.171
TTL is 255

```

## show tunnel rib system-tunnel-rib brief

```text
Tunnel RIB: system-tunnel-rib
Endpoint           Tunnel Type    Index(es)  Tunnel Preference  IGP Preference 
------------------ -------------- ---------- ------------------ ---------------
10.0.0.5/32        IS-IS SR IPv4  9          10                 115            
10.0.0.19/32       IS-IS SR IPv4  3          10                 115            
10.0.0.24/32       IS-IS SR IPv4  8          10                 115            
10.0.0.32/32       IS-IS SR IPv4  14         10                 115            
10.0.0.57/32       IS-IS SR IPv4  13         10                 115            
10.0.0.170/32      IS-IS SR IPv4  16         10                 115            
10.0.0.212/32      IS-IS SR IPv4  17         10                 115            
10.0.0.254/32      IS-IS SR IPv4  6          10                 115            
10.0.1.43/32       IS-IS SR IPv4  2          10                 115            
10.0.1.49/32       IS-IS SR IPv4  1          10                 115            
10.0.1.55/32       IS-IS SR IPv4  4          10                 115            
209.209.209.209/32 IS-IS SR IPv4  10         10                 115            

   IGP Metric    Metric Type
---------------- -----------
   20            metric     
   20            metric     
   20            metric     
   20            metric     
   11            metric     
   10            metric     
   20            metric     
   20            metric     
   20            metric     
   10            metric     
   20            metric     
   20            metric     

```

## show tunnel rib colored brief

```text
Tunnel RIB: system-colored-tunnel-rib
 Endpoint        Color   Tunnel Type       Index(es)    Tunnel Preference    IGP Preference    IGP Metric   Metric Type
--------------- ------- ----------------- ------------ -------------------- ----------------- ------------- -----------
 10.0.0.5/32     211     SR-TE Policy      30           35                   3                 0            metric     
 10.0.0.32/32    211     SR-TE Policy      26           35                   3                 0            metric     
 10.0.0.57/32    40      SR-TE Policy      28           35                   3                 0            metric     
 10.0.0.254/32   128     IS-IS FlexAlgo    7            65                   115               13           metric     
 10.0.1.49/32    129     IS-IS FlexAlgo    1            65                   115               12           metric     
 10.0.1.49/32    130     IS-IS FlexAlgo    3            65                   115               10           metric     
 10.0.1.49/32    131     IS-IS FlexAlgo    9            65                   115               40           metric     
 10.0.1.55/32    10      SR-TE Policy      32           35                   3                 0            metric     
 10.0.1.55/32    20      SR-TE Policy      34           35                   3                 0            metric     
 10.0.1.55/32    128     IS-IS FlexAlgo    6            65                   115               4            metric     
 10.0.1.55/32    129     IS-IS FlexAlgo    4            65                   115               24           metric     
 10.0.1.55/32    130     IS-IS FlexAlgo    2            65                   115               20           metric     
 10.0.1.55/32    131     IS-IS FlexAlgo    8            65                   115               30           metric     

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
>C    10.0.0.171/32 [0 pref/0 metric] updated 1d22h ago
         via Loopback0, directly connected
>C    20.149.171.0/24 [0 pref/0 metric] updated 1d22h ago
         via Ethernet24, directly connected
>C    20.170.171.0/24 [0 pref/0 metric] updated 1d01h ago
         via Ethernet1, directly connected
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
>B    0.0.0.0/0 [200 pref/0 MED] updated 20:11:07 ago
         via 192.168.20.1 colors [ 10(EM) ] [200 pref/0 MED] type tunnel
            via 10.0.0.179, IS-IS SR IPv4 Tunnel index 7
               via ::, NextLevelFecId2493952.6 label 20379
 B    10.0.0.5/32 [200 pref/20 MED] updated 00:04:27 ago
         via 20.170.179.170 colors [ 10(EM) ] [115 pref/20 metric] type ipv4
            via 20.170.171.170, Ethernet1
 B    10.0.0.19/32 [200 pref/20 MED] updated 19:41:35 ago
         via 20.170.179.170 colors [ 10(EM) ] [115 pref/20 metric] type ipv4
            via 20.170.171.170, Ethernet1
 B    10.0.0.24/32 [200 pref/20 MED] updated 19:41:35 ago
         via 20.170.179.170 colors [ 10(EM) ] [115 pref/20 metric] type ipv4
            via 20.170.171.170, Ethernet1
 B    10.0.0.32/32 [200 pref/10 MED] updated 00:17:23 ago
         via 20.32.179.32 colors [ 10(EM) ] [115 pref/30 metric] type ipv4
            via 20.149.171.149, Ethernet24
 B    10.0.0.57/32 [200 pref/11 MED] updated 19:41:35 ago
         via 20.170.179.170 colors [ 10(EM) ] [115 pref/20 metric] type ipv4
            via 20.170.171.170, Ethernet1
 B    10.0.0.170/32 [200 pref/10 MED] updated 19:41:35 ago
         via 20.170.179.170 colors [ 10(EM) ] [115 pref/20 metric] type ipv4
            via 20.170.171.170, Ethernet1
 B    10.0.0.171/32 [200 pref/20 MED] updated 19:41:35 ago
         via 20.170.179.170 colors [ 10(EM) ] [115 pref/20 metric] type ipv4
            via 20.170.171.170, Ethernet1
 B    10.0.0.179/32 [200 pref/0 MED] updated 00:17:24 ago
         via 10.0.0.179 colors [ 10(EM) ] [115 pref/20 metric] type tunnel
            via 10.0.0.179, IS-IS SR IPv4 Tunnel index 7
               via ::, NextLevelFecId2493952.6 label 20379
 B    10.0.0.212/32 [200 pref/20 MED] updated 01:12:03 ago
         via 20.170.179.170 colors [ 10(EM) ] [115 pref/20 metric] type ipv4
            via 20.170.171.170, Ethernet1
 B    10.0.0.254/32 [200 pref/20 MED] updated 19:17:19 ago
         via 20.170.179.170 colors [ 10(EM) ] [115 pref/20 metric] type ipv4
            via 20.170.171.170, Ethernet1
 B    10.0.1.43/32 [200 pref/30 MED] updated 00:17:23 ago
         via 20.32.179.32 colors [ 10(EM) ] [115 pref/30 metric] type ipv4
            via 20.149.171.149, Ethernet24
 B    10.0.1.49/32 [200 pref/20 MED] updated 00:17:23 ago
         via 20.32.179.32 colors [ 10(EM) ] [115 pref/30 metric] type ipv4
            via 20.149.171.149, Ethernet24
 B    10.0.1.55/32 [200 pref/30 MED] updated 00:17:23 ago
         via 20.32.179.32 colors [ 10(EM) ] [115 pref/30 metric] type ipv4
            via 20.149.171.149, Ethernet24
 B    20.5.149.0/24 [200 pref/30 MED] updated 00:17:23 ago
         via 20.32.179.32 colors [ 10(EM) ] [115 pref/30 metric] type ipv4
            via 20.149.171.149, Ethernet24
 B    20.5.170.0/24 [200 pref/20 MED] updated 19:41:35 ago
         via 20.170.179.170 colors [ 10(EM) ] [115 pref/20 metric] type ipv4
            via 20.170.171.170, Ethernet1
 B    20.19.149.0/24 [200 pref/30 MED] updated 00:17:23 ago
         via 20.32.179.32 colors [ 10(EM) ] [115 pref/30 metric] type ipv4
            via 20.149.171.149, Ethernet24
 B    20.19.170.0/24 [200 pref/20 MED] updated 19:41:35 ago
         via 20.170.179.170 colors [ 10(EM) ] [115 pref/20 metric] type ipv4
            via 20.170.171.170, Ethernet1
 B    20.24.149.0/24 [200 pref/30 MED] updated 00:17:23 ago
         via 20.32.179.32 colors [ 10(EM) ] [115 pref/30 metric] type ipv4
            via 20.149.171.149, Ethernet24
 B    20.24.170.0/24 [200 pref/20 MED] updated 19:41:35 ago
         via 20.170.179.170 colors [ 10(EM) ] [115 pref/20 metric] type ipv4
            via 20.170.171.170, Ethernet1
 B    20.32.149.0/24 [200 pref/20 MED] updated 00:17:23 ago
         via 20.32.179.32 colors [ 10(EM) ] [115 pref/30 metric] type ipv4
            via 20.149.171.149, Ethernet24
 B    20.32.155.0/24 [200 pref/40 MED] updated 00:17:23 ago
         via 20.32.179.32 colors [ 10(EM) ] [115 pref/30 metric] type ipv4
            via 20.149.171.149, Ethernet24
 B    20.32.170.0/24 [200 pref/21 MED] updated 00:17:23 ago
         via 20.32.179.32 colors [ 10(EM) ] [115 pref/30 metric] type ipv4
            via 20.149.171.149, Ethernet24
 B    20.32.179.0/24 [200 pref/0 MED] updated 00:17:24 ago
         via 10.0.0.179 colors [ 10(EM) ] [115 pref/20 metric] type tunnel
            via 10.0.0.179, IS-IS SR IPv4 Tunnel index 7
               via ::, NextLevelFecId2493952.6 label 20379
 B    20.57.149.0/24 [200 pref/21 MED] updated 03:20:31 ago
         via 20.170.179.170 colors [ 10(EM) ] [115 pref/20 metric] type ipv4
            via 20.170.171.170, Ethernet1
 B    20.57.155.0/24 [200 pref/40 MED] updated 00:17:23 ago
         via 20.32.179.32 colors [ 10(EM) ] [115 pref/30 metric] type ipv4
            via 20.149.171.149, Ethernet24
 B    20.57.170.0/24 [200 pref/11 MED] updated 19:41:35 ago
         via 20.170.179.170 colors [ 10(EM) ] [115 pref/20 metric] type ipv4
            via 20.170.171.170, Ethernet1
 B    20.111.149.0/24 [200 pref/30 MED] updated 00:17:23 ago
         via 20.32.179.32 colors [ 10(EM) ] [115 pref/30 metric] type ipv4
            via 20.149.171.149, Ethernet24
>B    20.111.179.0/24 [200 pref/0 MED] updated 00:17:24 ago
         via 10.0.0.179 colors [ 10(EM) ] [115 pref/20 metric] type tunnel
            via 10.0.0.179, IS-IS SR IPv4 Tunnel index 7
               via ::, NextLevelFecId2493952.6 label 20379
 B    20.143.149.0/24 [200 pref/30 MED] updated 00:17:23 ago
         via 20.32.179.32 colors [ 10(EM) ] [115 pref/30 metric] type ipv4
            via 20.149.171.149, Ethernet24
 B    20.149.155.0/24 [200 pref/30 MED] updated 00:17:23 ago
         via 20.32.179.32 colors [ 10(EM) ] [115 pref/30 metric] type ipv4
            via 20.149.171.149, Ethernet24
 B    20.149.171.0/24 [200 pref/30 MED] updated 00:17:23 ago
         via 20.32.179.32 colors [ 10(EM) ] [115 pref/30 metric] type ipv4
            via 20.149.171.149, Ethernet24
 B    20.149.172.0/24 [200 pref/30 MED] updated 00:17:23 ago
         via 20.32.179.32 colors [ 10(EM) ] [115 pref/30 metric] type ipv4
            via 20.149.171.149, Ethernet24
 B    20.149.179.0/24 [200 pref/0 MED] updated 00:17:24 ago
         via 10.0.0.179 colors [ 10(EM) ] [115 pref/20 metric] type tunnel
            via 10.0.0.179, IS-IS SR IPv4 Tunnel index 7
               via ::, NextLevelFecId2493952.6 label 20379
 B    20.149.254.0/24 [200 pref/30 MED] updated 00:17:23 ago
         via 20.32.179.32 colors [ 10(EM) ] [115 pref/30 metric] type ipv4
            via 20.149.171.149, Ethernet24
 B    20.155.170.0/24 [200 pref/30 MED] updated 19:41:35 ago
         via 20.170.179.170 colors [ 10(EM) ] [115 pref/20 metric] type ipv4
            via 20.170.171.170, Ethernet1
 B    20.170.171.0/24 [200 pref/20 MED] updated 19:41:35 ago
         via 20.170.179.170 colors [ 10(EM) ] [115 pref/20 metric] type ipv4
            via 20.170.171.170, Ethernet1
 B    20.170.172.0/24 [200 pref/110 MED] updated 04:10:18 ago
         via 20.170.179.170 colors [ 10(EM) ] [115 pref/20 metric] type ipv4
            via 20.170.171.170, Ethernet1
 B    20.170.179.0/24 [200 pref/0 MED] updated 00:17:24 ago
         via 10.0.0.179 colors [ 10(EM) ] [115 pref/20 metric] type tunnel
            via 10.0.0.179, IS-IS SR IPv4 Tunnel index 7
               via ::, NextLevelFecId2493952.6 label 20379
 B    20.170.212.0/24 [200 pref/20 MED] updated 01:12:11 ago
         via 20.170.179.170 colors [ 10(EM) ] [115 pref/20 metric] type ipv4
            via 20.170.171.170, Ethernet1
 B    20.170.254.0/24 [200 pref/20 MED] updated 19:17:22 ago
         via 20.170.179.170 colors [ 10(EM) ] [115 pref/20 metric] type ipv4
            via 20.170.171.170, Ethernet1
 B    31.9.1.0/24 [200 pref/20 MED] updated 19:41:35 ago
         via 20.170.179.170 colors [ 10(EM) ] [115 pref/20 metric] type ipv4
            via 20.170.171.170, Ethernet1
 B    192.168.0.0/19 [200 pref/20 MED] updated 19:41:35 ago
         via 20.170.179.170 colors [ 10(EM) ] [115 pref/20 metric] type ipv4
            via 20.170.171.170, Ethernet1
>B    192.168.20.0/23 [200 pref/0 MED] updated 00:17:24 ago
         via 10.0.0.179 colors [ 10(EM) ] [115 pref/20 metric] type tunnel
            via 10.0.0.179, IS-IS SR IPv4 Tunnel index 7
               via ::, NextLevelFecId2493952.6 label 20379
>B    192.168.24.0/25 [200 pref/0 MED] updated 20:11:07 ago
         via 192.168.20.1 colors [ 10(EM) ] [200 pref/0 MED] type tunnel
            via 10.0.0.179, IS-IS SR IPv4 Tunnel index 7
               via ::, NextLevelFecId2493952.6 label 20379
 B    209.209.209.209/32 [200 pref/0 MED] updated 00:17:24 ago
         via 10.0.0.179 colors [ 10(EM) ] [115 pref/20 metric] type tunnel
            via 10.0.0.179, IS-IS SR IPv4 Tunnel index 7
               via ::, NextLevelFecId2493952.6 label 20379
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
>I    10.0.0.5/32 [115 pref/20 metric] updated 00:04:27 ago
         via 20.149.171.149, Ethernet24
         via 20.170.171.170, Ethernet1
>I    10.0.0.19/32 [115 pref/20 metric] updated 23:42:22 ago
         via 20.149.171.149, Ethernet24
         via 20.170.171.170, Ethernet1
>I    10.0.0.24/32 [115 pref/20 metric] updated 21:30:11 ago
         via 20.149.171.149, Ethernet24
         via 20.170.171.170, Ethernet1
>I    10.0.0.32/32 [115 pref/20 metric] updated 22:39:46 ago
         via 20.149.171.149, Ethernet24
>I    10.0.0.57/32 [115 pref/11 metric] updated 20:51:02 ago
         via 20.170.171.170, Ethernet1
>I    10.0.0.170/32 [115 pref/10 metric] updated 21:39:48 ago
         via 20.170.171.170, Ethernet1
>I    10.0.0.179/32 [115 pref/20 metric] updated 00:00:00 ago
         via 20.149.171.149, Ethernet24
         via 20.170.171.170, Ethernet1
>I    10.0.0.212/32 [115 pref/20 metric] updated 01:12:03 ago
         via 20.170.171.170, Ethernet1
>I    10.0.0.254/32 [115 pref/20 metric] updated 19:17:20 ago
         via 20.149.171.149, Ethernet24
         via 20.170.171.170, Ethernet1
>I    10.0.1.43/32 [115 pref/20 metric] updated 1d22h ago
         via 20.149.171.149, Ethernet24
>I    10.0.1.49/32 [115 pref/10 metric] updated 1d22h ago
         via 20.149.171.149, Ethernet24
>I    10.0.1.55/32 [115 pref/20 metric] updated 22:53:30 ago
         via 20.149.171.149, Ethernet24
>I    20.5.149.0/24 [115 pref/20 metric] updated 00:28:47 ago
         via 20.149.171.149, Ethernet24
>I    20.5.170.0/24 [115 pref/20 metric] updated 20:19:05 ago
         via 20.170.171.170, Ethernet1
>I    20.19.149.0/24 [115 pref/20 metric] updated 1d22h ago
         via 20.149.171.149, Ethernet24
>I    20.19.170.0/24 [115 pref/20 metric] updated 23:50:00 ago
         via 20.170.171.170, Ethernet1
>I    20.24.149.0/24 [115 pref/20 metric] updated 1d22h ago
         via 20.149.171.149, Ethernet24
>I    20.24.170.0/24 [115 pref/20 metric] updated 1d01h ago
         via 20.170.171.170, Ethernet1
>I    20.32.149.0/24 [115 pref/20 metric] updated 1d01h ago
         via 20.149.171.149, Ethernet24
>I    20.32.155.0/24 [115 pref/30 metric] updated 22:53:30 ago
         via 20.149.171.149, Ethernet24
>I    20.32.170.0/24 [115 pref/22 metric] updated 22:39:46 ago
         via 20.170.171.170, Ethernet1
>I    20.32.179.0/24 [115 pref/30 metric] updated 00:18:16 ago
         via 20.149.171.149, Ethernet24
>I    20.57.149.0/24 [115 pref/20 metric] updated 1d22h ago
         via 20.149.171.149, Ethernet24
>I    20.57.155.0/24 [115 pref/30 metric] updated 22:53:30 ago
         via 20.149.171.149, Ethernet24
>I    20.57.170.0/24 [115 pref/11 metric] updated 1d01h ago
         via 20.170.171.170, Ethernet1
>I    20.111.149.0/24 [115 pref/20 metric] updated 21:23:08 ago
         via 20.149.171.149, Ethernet24
>I    20.143.149.0/24 [115 pref/20 metric] updated 1d22h ago
         via 20.149.171.149, Ethernet24
>I    20.149.155.0/24 [115 pref/20 metric] updated 22:53:33 ago
         via 20.149.171.149, Ethernet24
>I    20.149.172.0/24 [115 pref/20 metric] updated 1d01h ago
         via 20.149.171.149, Ethernet24
>I    20.149.179.0/24 [115 pref/20 metric] updated 1d22h ago
         via 20.149.171.149, Ethernet24
>I    20.149.254.0/24 [115 pref/20 metric] updated 1d05h ago
         via 20.149.171.149, Ethernet24
>I    20.155.170.0/24 [115 pref/30 metric] updated 22:53:30 ago
         via 20.149.171.149, Ethernet24
         via 20.170.171.170, Ethernet1
>I    20.170.172.0/24 [115 pref/110 metric] updated 04:10:18 ago
         via 20.170.171.170, Ethernet1
>I    20.170.179.0/24 [115 pref/20 metric] updated 19:41:43 ago
         via 20.170.171.170, Ethernet1
>I    20.170.212.0/24 [115 pref/20 metric] updated 01:12:11 ago
         via 20.170.171.170, Ethernet1
>I    20.170.254.0/24 [115 pref/20 metric] updated 19:17:22 ago
         via 20.170.171.170, Ethernet1
>I    31.9.1.0/24 [115 pref/20 metric] updated 23:42:22 ago
         via 20.149.171.149, Ethernet24
         via 20.170.171.170, Ethernet1
>I    192.168.0.0/19 [115 pref/20 metric] updated 23:42:22 ago
         via 20.149.171.149, Ethernet24
         via 20.170.171.170, Ethernet1
>I    209.209.209.209/32 [115 pref/20 metric] updated 00:00:00 ago
         via 20.149.171.149, Ethernet24
         via 20.170.171.170, Ethernet1
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
>P    ::/96 [1 pref/0 metric] updated 03:09:50 ago
         via Null0, directly connected [NF]
>P    ::ffff:127.0.0.0/104 [1 pref/0 metric] updated 03:09:50 ago
         via :: [1 pref/1 metric] type ipv6
            via , directly connected
>P    fe80::/10 [1 pref/0 metric] updated 03:09:50 ago
```

## show platform sand l3 summary

```text
Number of vrfs: 7

Ipv4:
  Routes:       116  backlog:  0  unprogrammed:  0
  Adjacencies:  92   backlog:  0  unprogrammed:  0
Ipv6:
  Routes:       4   backlog:  0  unprogrammed:  0
  Adjacencies:  92  backlog:  0  unprogrammed:  0
Mpls:
  Routes:       29  backlog:  0  unprogrammed:  0
  Adjacencies:  2   backlog:  0  unprogrammed:  0

Jericho2 Ip Fecs:
  Non-ecmp fecs:  4148  ecmp fecs:  2  fec entries:  4152
Jericho2 Mpls Fecs:
  Non-ecmp fecs:  2  ecmp fecs:  0  fec entries:  2
Jericho2 Vxlan Tunnel Fecs:
  Non-ecmp fecs:  0  ecmp fecs:  0  fec entries:  0
  Number of vxlan tunnels configured: 0

Jericho2 Lpm Routes:
  Routes:   116  unprogrammed:   0   
  Routes6:  4    unprogrammed6:  0   
  Backlog:  0  

Jericho2 Lpm:
  TCAM entries used:   3   Percent free:  99  ADS2 entries used:   8  Percent free:  99
  Pivot buckets used:  4   Rows used:     1   Entries Per Bucket:  2  Percent free:  99
  Route buckets used:  20  Rows used:     3   Entries Per Bucket:  6  Percent free:  99

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
  FixedSystem: 3
Egress Mpls (for inner 2 labels) rewrite entries in use (in each fap):
  FixedSystem: 37
Egress Sflow rewrite entries in use (in each fap):
  FixedSystem: 0

Egress rewrite chains in backlog: resource-full 0, no-interface 0

Glem entries used per fap :
  FixedSystem: 4144

Jericho2 Fec:
  Maximum FEC hierarchy levels:  2
  ReusedEcmp:  0  allocs:  873  frees:  815  shuffles:  0  cmds:  0
  Zombies:     4    purges:    4
  Quarantine:  0/0  shuffles:  0  deletes:  0   
  Fec insertion failures:  0
  Level1  Fecs:
    Non-ecmp fecs:            0    ecmp fecs:            1 
    Non-ecmp (Percent free):  100  ecmp (Percent free):  99
  Level2  Fecs:
    Non-ecmp fecs:            46  ecmp fecs:            0  
    Non-ecmp (Percent free):  99  ecmp (Percent free):  100
  Level3  Fecs:
    Non-ecmp fecs:            78  ecmp fecs:            4 
    Non-ecmp (Percent free):  99  ecmp (Percent free):  99

Lpm Detail:
  Requests:  1626  cleanses:  421  batches:  421  avg batch size:  3

Jericho Arp:
  ArpTable writes:      20740  queued      0   
  IngressTable writes:  80623  queued      0   
  Coprocessors:         1      in CmdRing

Tunnel Counter Status
  Number of MPLS tunnels:                  45   
  Number of uncountable MPLS tunnels:      11   
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
|0  |0.0.0.0/8         |DROP | DROP               |0    |  -     |                   |  -  |528512|   -   
|0  |10.0.0.5/32       |ROUTE| Et1                |1006 |103421  | 28:99:3a:06:b4:e1 |24576|528490|   -   
|0  |10.0.0.5/32       |ROUTE| Et24               |1007 |103424  | c0:f8:7f:6a:4e:1c |24576|528491|   -   
|0  |10.0.0.5/32       |ROUTE| Et24               |1007 |103424  | c0:f8:7f:6a:4e:1c |24576|528492|   -   
|0  |10.0.0.5/32       |ROUTE| Et1                |1006 |103421  | 28:99:3a:06:b4:e1 |24576|528493|   -   
|0  |10.0.0.19/32      |ROUTE| Et1                |1006 |103421  | 28:99:3a:06:b4:e1 |24576|528490|   -   
|0  |10.0.0.19/32      |ROUTE| Et24               |1007 |103424  | c0:f8:7f:6a:4e:1c |24576|528491|   -   
|0  |10.0.0.19/32      |ROUTE| Et24               |1007 |103424  | c0:f8:7f:6a:4e:1c |24576|528492|   -   
|0  |10.0.0.19/32      |ROUTE| Et1                |1006 |103421  | 28:99:3a:06:b4:e1 |24576|528493|   -   
|0  |10.0.0.24/32      |ROUTE| Et1                |1006 |103421  | 28:99:3a:06:b4:e1 |24576|528490|   -   
|0  |10.0.0.24/32      |ROUTE| Et24               |1007 |103424  | c0:f8:7f:6a:4e:1c |24576|528491|   -   
|0  |10.0.0.24/32      |ROUTE| Et24               |1007 |103424  | c0:f8:7f:6a:4e:1c |24576|528492|   -   
|0  |10.0.0.24/32      |ROUTE| Et1                |1006 |103421  | 28:99:3a:06:b4:e1 |24576|528493|   -   
|0  |10.0.0.32/32      |ROUTE| Et24               |1007 |103424  | c0:f8:7f:6a:4e:1c |  -  |528508|   -   
|0  |10.0.0.57/32      |ROUTE| Et1                |1006 |103421  | 28:99:3a:06:b4:e1 |  -  |528510|   -   
|0  |10.0.0.170/32     |ROUTE| Et1                |1006 |103421  | 28:99:3a:06:b4:e1 |  -  |528510|   -   
|0  |10.0.0.171/32     |TRAP | CoppSystemIpUcast  |0    |  -     | Receive           |  -  |524291|   -   
|0  |10.0.0.179/32     |ROUTE| Et1                |1006 |103421  | 28:99:3a:06:b4:e1 |24576|528490|   -   
|0  |10.0.0.179/32     |ROUTE| Et24               |1007 |103424  | c0:f8:7f:6a:4e:1c |24576|528491|   -   
|0  |10.0.0.179/32     |ROUTE| Et24               |1007 |103424  | c0:f8:7f:6a:4e:1c |24576|528492|   -   
|0  |10.0.0.179/32     |ROUTE| Et1                |1006 |103421  | 28:99:3a:06:b4:e1 |24576|528493|   -   
|0  |10.0.0.212/32     |ROUTE| Et1                |1006 |103421  | 28:99:3a:06:b4:e1 |  -  |528510|   -   
|0  |10.0.0.254/32     |ROUTE| Et1                |1006 |103421  | 28:99:3a:06:b4:e1 |24576|528490|   -   
|0  |10.0.0.254/32     |ROUTE| Et24               |1007 |103424  | c0:f8:7f:6a:4e:1c |24576|528491|   -   
|0  |10.0.0.254/32     |ROUTE| Et24               |1007 |103424  | c0:f8:7f:6a:4e:1c |24576|528492|   -   
|0  |10.0.0.254/32     |ROUTE| Et1                |1006 |103421  | 28:99:3a:06:b4:e1 |24576|528493|   -   
|0  |10.0.1.43/32      |ROUTE| Et24               |1007 |103424  | c0:f8:7f:6a:4e:1c |  -  |528508|   -   
|0  |10.0.1.49/32      |ROUTE| Et24               |1007 |103424  | c0:f8:7f:6a:4e:1c |  -  |528508|   -   
|0  |10.0.1.55/32      |ROUTE| Et24               |1007 |103424  | c0:f8:7f:6a:4e:1c |  -  |528508|   -   
|0  |20.5.149.0/24     |ROUTE| Et24               |1007 |103424  | c0:f8:7f:6a:4e:1c |  -  |528508|   -   
|0  |20.5.170.0/24     |ROUTE| Et1                |1006 |103421  | 28:99:3a:06:b4:e1 |  -  |528510|   -   
|0  |20.19.149.0/24    |ROUTE| Et24               |1007 |103424  | c0:f8:7f:6a:4e:1c |  -  |528508|   -   
|0  |20.19.170.0/24    |ROUTE| Et1                |1006 |103421  | 28:99:3a:06:b4:e1 |  -  |528510|   -   
|0  |20.24.149.0/24    |ROUTE| Et24               |1007 |103424  | c0:f8:7f:6a:4e:1c |  -  |528508|   -   
|0  |20.24.170.0/24    |ROUTE| Et1                |1006 |103421  | 28:99:3a:06:b4:e1 |  -  |528510|   -   
|0  |20.32.149.0/24    |ROUTE| Et24               |1007 |103424  | c0:f8:7f:6a:4e:1c |  -  |528508|   -   
|0  |20.32.155.0/24    |ROUTE| Et24               |1007 |103424  | c0:f8:7f:6a:4e:1c |  -  |528508|   -   
|0  |20.32.170.0/24    |ROUTE| Et1                |1006 |103421  | 28:99:3a:06:b4:e1 |  -  |528510|   -   
|0  |20.32.179.0/24    |ROUTE| Et24               |1007 |103424  | c0:f8:7f:6a:4e:1c |  -  |528508|   -   
|0  |20.57.149.0/24    |ROUTE| Et24               |1007 |103424  | c0:f8:7f:6a:4e:1c |  -  |528508|   -   
|0  |20.57.155.0/24    |ROUTE| Et24               |1007 |103424  | c0:f8:7f:6a:4e:1c |  -  |528508|   -   
|0  |20.57.170.0/24    |ROUTE| Et1                |1006 |103421  | 28:99:3a:06:b4:e1 |  -  |528510|   -   
|0  |20.111.149.0/24   |ROUTE| Et24               |1007 |103424  | c0:f8:7f:6a:4e:1c |  -  |528508|   -   
|0  |20.111.179.0/24   |ROUTE| FEC 24577          |0    |2097151 | 00:00:00:00:00:00 |  -  |288378|M 20379
|0  |20.143.149.0/24   |ROUTE| Et24               |1007 |103424  | c0:f8:7f:6a:4e:1c |  -  |528508|   -   
|0  |20.149.155.0/24   |ROUTE| Et24               |1007 |103424  | c0:f8:7f:6a:4e:1c |  -  |528508|   -   
|0  |20.149.171.0/32   |TRAP | CoppSystemIpBcast  |0    |  -     | BcastReceive      |  -  |524288|   -   
|0  |20.149.171.149/32 |ROUTE| Et24               |1007 |103424  | c0:f8:7f:6a:4e:1c |  -  |528502|   -   
|0  |20.149.171.171/32 |TRAP | CoppSystemIpUcast  |0    |  -     | Receive           |  -  |524291|   -   
|0  |20.149.171.255/32 |TRAP | CoppSystemIpBcast  |0    |  -     | BcastReceive      |  -  |524288|   -   
|0  |20.149.171.0/24   |TRAP | CoppSystemL3DstMiss|1007 |1007    | ArpTrap           |  -  |525301|   -   
|0  |20.149.172.0/24   |ROUTE| Et24               |1007 |103424  | c0:f8:7f:6a:4e:1c |  -  |528508|   -   
|0  |20.149.179.0/24   |ROUTE| Et24               |1007 |103424  | c0:f8:7f:6a:4e:1c |  -  |528508|   -   
|0  |20.149.254.0/24   |ROUTE| Et24               |1007 |103424  | c0:f8:7f:6a:4e:1c |  -  |528508|   -   
|0  |20.155.170.0/24   |ROUTE| Et1                |1006 |103421  | 28:99:3a:06:b4:e1 |24576|528490|   -   
|0  |20.155.170.0/24   |ROUTE| Et24               |1007 |103424  | c0:f8:7f:6a:4e:1c |24576|528491|   -   
|0  |20.155.170.0/24   |ROUTE| Et24               |1007 |103424  | c0:f8:7f:6a:4e:1c |24576|528492|   -   
|0  |20.155.170.0/24   |ROUTE| Et1                |1006 |103421  | 28:99:3a:06:b4:e1 |24576|528493|   -   
|0  |20.170.171.0/32   |TRAP | CoppSystemIpBcast  |0    |  -     | BcastReceive      |  -  |524288|   -   
|0  |20.170.171.170/32 |ROUTE| Et1                |1006 |103421  | 28:99:3a:06:b4:e1 |  -  |528504|   -   
|0  |20.170.171.171/32 |TRAP | CoppSystemIpUcast  |0    |  -     | Receive           |  -  |524291|   -   
|0  |20.170.171.255/32 |TRAP | CoppSystemIpBcast  |0    |  -     | BcastReceive      |  -  |524288|   -   
|0  |20.170.171.0/24   |TRAP | CoppSystemL3DstMiss|1006 |1006    | ArpTrap           |  -  |525300|   -   
|0  |20.170.172.0/24   |ROUTE| Et1                |1006 |103421  | 28:99:3a:06:b4:e1 |  -  |528510|   -   
|0  |20.170.179.0/24   |ROUTE| Et1                |1006 |103421  | 28:99:3a:06:b4:e1 |  -  |528510|   -   
|0  |20.170.212.0/24   |ROUTE| Et1                |1006 |103421  | 28:99:3a:06:b4:e1 |  -  |528510|   -   
|0  |20.170.254.0/24   |ROUTE| Et1                |1006 |103421  | 28:99:3a:06:b4:e1 |  -  |528510|   -   
|0  |31.9.1.0/24       |ROUTE| Et1                |1006 |103421  | 28:99:3a:06:b4:e1 |24576|528490|   -   
|0  |31.9.1.0/24       |ROUTE| Et24               |1007 |103424  | c0:f8:7f:6a:4e:1c |24576|528491|   -   
|0  |31.9.1.0/24       |ROUTE| Et24               |1007 |103424  | c0:f8:7f:6a:4e:1c |24576|528492|   -   
|0  |31.9.1.0/24       |ROUTE| Et1                |1006 |103421  | 28:99:3a:06:b4:e1 |24576|528493|   -   
|0  |127.0.0.0/8       |TRAP | CoppSystemL3DstMiss|0    |  -     | ArpTrap           |  -  |524294|   -   
|0  |192.168.20.0/23   |ROUTE| FEC 24577          |0    |2097151 | 00:00:00:00:00:00 |  -  |288378|M 20379
|0  |192.168.24.0/25   |ROUTE| FEC 24577          |0    |2097151 | 00:00:00:00:00:00 |  -  |288380|M 20379
|0  |192.168.0.0/19    |ROUTE| Et1                |1006 |103421  | 28:99:3a:06:b4:e1 |24576|528490|   -   
|0  |192.168.0.0/19    |ROUTE| Et24               |1007 |103424  | c0:f8:7f:6a:4e:1c |24576|528491|   -   
|0  |192.168.0.0/19    |ROUTE| Et24               |1007 |103424  | c0:f8:7f:6a:4e:1c |24576|528492|   -   
|0  |192.168.0.0/19    |ROUTE| Et1                |1006 |103421  | 28:99:3a:06:b4:e1 |24576|528493|   -   
|0  |209.209.209.209/32|ROUTE| Et1                |1006 |103421  | 28:99:3a:06:b4:e1 |24576|528490|   -   
|0  |209.209.209.209/32|ROUTE| Et24               |1007 |103424  | c0:f8:7f:6a:4e:1c |24576|528491|   -   
|0  |209.209.209.209/32|ROUTE| Et24               |1007 |103424  | c0:f8:7f:6a:4e:1c |24576|528492|   -   
|0  |209.209.209.209/32|ROUTE| Et1                |1006 |103421  | 28:99:3a:06:b4:e1 |24576|528493|   -   
|0  |0.0.0.0/0         |ROUTE| FEC 24577          |0    |2097151 | 00:00:00:00:00:00 |  -  |288380|M 20379
|1  |0.0.0.0/8         |DROP | DROP               |0    |  -     |                   |  -  |528526|   -   
|1  |20.32.111.0/24    |ROUTE| FEC 528532         |0    |2097144 | 00:00:00:00:00:00 |  -  |288394|M 756640
|1  |20.57.111.0/24    |ROUTE| FEC 528534         |0    |2097138 | 00:00:00:00:00:00 |  -  |288388|M 524252
|1  |20.111.155.0/24   |ROUTE| FEC 528550         |0    |2097142 | 00:00:00:00:00:00 |  -  |288412|M 24021
|1  |20.111.171.0/32   |TRAP | CoppSystemIpBcast  |0    |  -     | BcastReceive      |  -  |524288|   -   
|1  |20.111.171.111/32 |ROUTE| Et5                |1013 |103435  | 00:14:01:00:00:01 |  -  |528506|   -   
|1  |20.111.171.171/32 |TRAP | CoppSystemIpUcast  |0    |  -     | Receive           |  -  |524291|   -   
|1  |20.111.171.255/32 |TRAP | CoppSystemIpBcast  |0    |  -     | BcastReceive      |  -  |524288|   -   
|1  |20.111.171.0/24   |TRAP | CoppSystemL3DstMiss|1013 |1013    | ArpTrap           |  -  |525307|   -   
|1  |20.111.179.0/24   |ROUTE| FEC 24577          |0    |2097135 | 00:00:00:00:00:00 |  -  |288382|M 20379 28
|1  |20.111.254.0/24   |ROUTE| FEC 24577          |0    |2097145 | 00:00:00:00:00:00 |  -  |288374|M 20254 48090
|1  |127.0.0.0/8       |TRAP | CoppSystemL3DstMiss|0    |  -     | ArpTrap           |  -  |524294|   -   
|1  |0.0.0.0/0         |TRAP | CoppSystemL3LpmOver|0    |  -     | SlowReceive       |  -  |524292|   -   
|2  |0.0.0.0/8         |DROP | DROP               |0    |  -     |                   |  -  |528524|   -   
|2  |127.0.0.0/8       |TRAP | CoppSystemL3DstMiss|0    |  -     | ArpTrap           |  -  |524294|   -   
|2  |192.168.20.0/32   |TRAP | CoppSystemIpBcast  |0    |  -     | BcastReceive      |  -  |524288|   -   
|2  |192.168.20.171/32 |TRAP | CoppSystemIpUcast  |0    |  -     | Receive           |  -  |524291|   -   
|2  |192.168.21.255/32 |TRAP | CoppSystemIpBcast  |0    |  -     | BcastReceive      |  -  |524288|   -   
|2  |192.168.20.0/23   |TRAP | CoppSystemL3DstMiss|0    |  -     | ArpTrap           |  -  |524294|   -   
|2  |0.0.0.0/0         |TRAP | CoppSystemL3DstMiss|0    |  -     | ArpTrap           |  -  |524294|   -   
|3  |0.0.0.0/8         |DROP | DROP               |0    |  -     |                   |  -  |528518|   -   
|3  |20.57.111.0/24    |ROUTE| FEC 528534         |0    |2097139 | 00:00:00:00:00:00 |  -  |288386|M 524286
|3  |20.111.155.0/24   |ROUTE| FEC 528550         |0    |2097141 | 00:00:00:00:00:00 |  -  |288414|M 24013
|3  |20.111.171.0/32   |TRAP | CoppSystemIpBcast  |0    |  -     | BcastReceive      |  -  |524288|   -   
|3  |20.111.171.171/32 |TRAP | CoppSystemIpUcast  |0    |  -     | Receive           |  -  |524291|   -   
|3  |20.111.171.255/32 |TRAP | CoppSystemIpBcast  |0    |  -     | BcastReceive      |  -  |524288|   -   
|3  |20.111.171.0/24   |TRAP | CoppSystemL3DstMiss|1019 |1019    | ArpTrap           |  -  |525313|   -   
|3  |20.111.179.0/24   |ROUTE| FEC 24577          |0    |2097131 | 00:00:00:00:00:00 |  -  |288364|M 20379 16
|3  |127.0.0.0/8       |TRAP | CoppSystemL3DstMiss|0    |  -     | ArpTrap           |  -  |524294|   -   
|3  |0.0.0.0/0         |TRAP | CoppSystemL3LpmOver|0    |  -     | SlowReceive       |  -  |524292|   -   
|4  |0.0.0.0/8         |DROP | DROP               |0    |  -     |                   |  -  |528520|   -   
|4  |20.57.111.0/24    |ROUTE| FEC 528534         |0    |2097136 | 00:00:00:00:00:00 |  -  |288392|M 524284
|4  |20.111.155.0/24   |ROUTE| FEC 528550         |0    |2097150 | 00:00:00:00:00:00 |  -  |288408|M 24005
|4  |20.111.171.0/32   |TRAP | CoppSystemIpBcast  |0    |  -     | BcastReceive      |  -  |524288|   -   
|4  |20.111.171.171/32 |TRAP | CoppSystemIpUcast  |0    |  -     | Receive           |  -  |524291|   -   
|4  |20.111.171.255/32 |TRAP | CoppSystemIpBcast  |0    |  -     | BcastReceive      |  -  |524288|   -   
|4  |20.111.171.0/24   |TRAP | CoppSystemL3DstMiss|1020 |1020    | ArpTrap           |  -  |525314|   -   
|4  |20.111.179.0/24   |ROUTE| FEC 24577          |0    |2097133 | 00:00:00:00:00:00 |  -  |288360|M 20379 18
|4  |55.55.55.130/32   |ROUTE| FEC 528550         |0    |2097150 | 00:00:00:00:00:00 |  -  |288408|M 24005
|4  |127.0.0.0/8       |TRAP | CoppSystemL3DstMiss|0    |  -     | ArpTrap           |  -  |524294|   -   
|4  |0.0.0.0/0         |TRAP | CoppSystemL3LpmOver|0    |  -     | SlowReceive       |  -  |524292|   -   
|5  |0.0.0.0/8         |DROP | DROP               |0    |  -     |                   |  -  |528516|   -   
|5  |20.57.111.0/24    |ROUTE| FEC 528534         |0    |2097137 | 00:00:00:00:00:00 |  -  |288390|M 524283
|5  |20.111.155.0/24   |ROUTE| FEC 528550         |0    |2097134 | 00:00:00:00:00:00 |  -  |288416|M 24019
|5  |20.111.171.0/32   |TRAP | CoppSystemIpBcast  |0    |  -     | BcastReceive      |  -  |524288|   -   
|5  |20.111.171.171/32 |TRAP | CoppSystemIpUcast  |0    |  -     | Receive           |  -  |524291|   -   
|5  |20.111.171.255/32 |TRAP | CoppSystemIpBcast  |0    |  -     | BcastReceive      |  -  |524288|   -   
|5  |20.111.171.0/24   |TRAP | CoppSystemL3DstMiss|1008 |1008    | ArpTrap           |  -  |525302|   -   
|5  |127.0.0.0/8       |TRAP | CoppSystemL3DstMiss|0    |  -     | ArpTrap           |  -  |524294|   -   
|5  |0.0.0.0/0         |TRAP | CoppSystemL3LpmOver|0    |  -     | SlowReceive       |  -  |524292|   -   
|6  |0.0.0.0/8         |DROP | DROP               |0    |  -     |                   |  -  |528522|   -   
|6  |20.57.111.0/24    |ROUTE| FEC 528534         |0    |2097140 | 00:00:00:00:00:00 |  -  |288384|M 524285
|6  |20.111.155.0/24   |ROUTE| FEC 528550         |0    |2097143 | 00:00:00:00:00:00 |  -  |288410|M 24015
|6  |20.111.171.0/32   |TRAP | CoppSystemIpBcast  |0    |  -     | BcastReceive      |  -  |524288|   -   
|6  |20.111.171.171/32 |TRAP | CoppSystemIpUcast  |0    |  -     | Receive           |  -  |524291|   -   
|6  |20.111.171.255/32 |TRAP | CoppSystemIpBcast  |0    |  -     | BcastReceive      |  -  |524288|   -   
|6  |20.111.171.0/24   |TRAP | CoppSystemL3DstMiss|1018 |1018    | ArpTrap           |  -  |525312|   -   
|6  |20.111.179.0/24   |ROUTE| FEC 24577          |0    |2097132 | 00:00:00:00:00:00 |  -  |288362|M 20379 17
|6  |127.0.0.0/8       |TRAP | CoppSystemL3DstMiss|0    |  -     | ArpTrap           |  -  |524294|   -   
|6  |0.0.0.0/0         |TRAP | CoppSystemL3LpmOver|0    |  -     | SlowReceive       |  -  |524292|   -   

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
|24576|528490|ROUTE| Et1                |1006 |103421  | 28:99:3a:06:b4:e1 |   -   
|24576|528491|ROUTE| Et24               |1007 |103424  | c0:f8:7f:6a:4e:1c |   -   
|24576|528492|ROUTE| Et24               |1007 |103424  | c0:f8:7f:6a:4e:1c |   -   
|24576|528493|ROUTE| Et1                |1006 |103421  | 28:99:3a:06:b4:e1 |   -   
|24577|528528|ROUTE| Et1                |1006 |103421  | 28:99:3a:06:b4:e1 |   -   
|24577|528529|ROUTE| Et24               |1007 |103424  | c0:f8:7f:6a:4e:1c |   -   
|24577|528530|ROUTE| Et24               |1007 |103424  | c0:f8:7f:6a:4e:1c |   -   
|24577|528531|ROUTE| Et1                |1006 |103421  | 28:99:3a:06:b4:e1 |   -   
|  -  |288374|ROUTE| FEC 24577          |   - |2097145 |                 - |Mpush 20254 48090
|  -  |288384|ROUTE| FEC 528534         |   - |2097140 |                 - |Mpush 524285
|  -  |288386|ROUTE| FEC 528534         |   - |2097139 |                 - |Mpush 524286
|  -  |288388|ROUTE| FEC 528534         |   - |2097138 |                 - |Mpush 524252
|  -  |288390|ROUTE| FEC 528534         |   - |2097137 |                 - |Mpush 524283
|  -  |288392|ROUTE| FEC 528534         |   - |2097136 |                 - |Mpush 524284
|  -  |288394|ROUTE| FEC 528532         |   - |2097144 |                 - |Mpush 756640
|  -  |288398|ROUTE| FEC 528562         |   - |  -     |                   |   -   
|  -  |288400|ROUTE| FEC 528560         |   - |  -     |                   |   -   
|  -  |288402|ROUTE| FEC 528564         |   - |  -     |                   |   -   
|  -  |288404|ROUTE| FEC 528558         |   - |  -     |                   |   -   
|  -  |288406|ROUTE| FEC 528548         |   - |  -     |                   |   -   
|  -  |288408|ROUTE| FEC 528550         |   - |2097150 |                 - |Mpush 24005
|  -  |288410|ROUTE| FEC 528550         |   - |2097143 |                 - |Mpush 24015
|  -  |288412|ROUTE| FEC 528550         |   - |2097142 |                 - |Mpush 24021
|  -  |288414|ROUTE| FEC 528550         |   - |2097141 |                 - |Mpush 24013
|  -  |288416|ROUTE| FEC 528550         |   - |2097134 |                 - |Mpush 24019
|  -  |524288|TRAP | CoppSystemIpBcast  |0    |  -     | BcastReceive      |   -   
|  -  |524291|TRAP | CoppSystemIpUcast  |0    |  -     | Receive           |   -   
|  -  |524292|TRAP | CoppSystemL3LpmOver|0    |  -     | SlowReceive       |   -   
|  -  |524294|TRAP | CoppSystemL3DstMiss|0    |  -     | ArpTrap           |   -   
|  -  |525300|TRAP | CoppSystemL3DstMiss|1006 |1006    | ArpTrap           |   -   
|  -  |525301|TRAP | CoppSystemL3DstMiss|1007 |1007    | ArpTrap           |   -   
|  -  |525302|TRAP | CoppSystemL3DstMiss|1008 |1008    | ArpTrap           |   -   
|  -  |525307|TRAP | CoppSystemL3DstMiss|1013 |1013    | ArpTrap           |   -   
|  -  |525312|TRAP | CoppSystemL3DstMiss|1018 |1018    | ArpTrap           |   -   
|  -  |525313|TRAP | CoppSystemL3DstMiss|1019 |1019    | ArpTrap           |   -   
|  -  |525314|TRAP | CoppSystemL3DstMiss|1020 |1020    | ArpTrap           |   -   
|  -  |528482|ROUTE| Et1                |1006 |103421  | 28:99:3a:06:b4:e1 |   -   
|  -  |528484|ROUTE| Et24               |1007 |103424  | c0:f8:7f:6a:4e:1c |   -   
|  -  |528486|ROUTE| Et24               |1007 |103425  | c0:f8:7f:6a:4e:1c |   -   
|  -  |528487|ROUTE| Et1                |1006 |103426  | 28:99:3a:06:b4:e1 |Mpush 20349
|  -  |528494|ROUTE| Et1                |1006 |103429  | 28:99:3a:06:b4:e1 |   -   
|  -  |528495|ROUTE| Et24               |1007 |103430  | c0:f8:7f:6a:4e:1c |   -   
|  -  |528496|ROUTE| Et24               |1007 |103431  | c0:f8:7f:6a:4e:1c |   -   
|  -  |528497|ROUTE| Et1                |1006 |103432  | 28:99:3a:06:b4:e1 |   -   
|  -  |528498|ROUTE| Et1                |1006 |103422  | 28:99:3a:06:b4:e1 |   -   
|  -  |528499|ROUTE| Et24               |1007 |103423  | c0:f8:7f:6a:4e:1c |Mpush 20024
|  -  |528500|ROUTE| Et24               |1007 |103424  | c0:f8:7f:6a:4e:1c |   -   
|  -  |528502|ROUTE| Et24               |1007 |103424  | c0:f8:7f:6a:4e:1c |   -   
|  -  |528504|ROUTE| Et1                |1006 |103421  | 28:99:3a:06:b4:e1 |   -   
|  -  |528506|ROUTE| Et5                |1013 |103435  | 00:14:01:00:00:01 |   -   
|  -  |528508|ROUTE| Et24               |1007 |103424  | c0:f8:7f:6a:4e:1c |   -   
|  -  |528510|ROUTE| Et1                |1006 |103421  | 28:99:3a:06:b4:e1 |   -   
|  -  |528512|DROP | DROP               |0    |  -     |                   |   -   
|  -  |528514|ROUTE| Et24               |1007 |103424  | c0:f8:7f:6a:4e:1c |   -   
|  -  |528516|DROP | DROP               |0    |  -     |                   |   -   
|  -  |528518|DROP | DROP               |0    |  -     |                   |   -   
|  -  |528520|DROP | DROP               |0    |  -     |                   |   -   
|  -  |528522|DROP | DROP               |0    |  -     |                   |   -   
|  -  |528524|DROP | DROP               |0    |  -     |                   |   -   
|  -  |528526|DROP | DROP               |0    |  -     |                   |   -   
|  -  |528532|ROUTE| Et24               |1007 |103433  | c0:f8:7f:6a:4e:1c |Mpush 20032
|  -  |528533|ROUTE| Et1                |1006 |103434  | 28:99:3a:06:b4:e1 |Mpush 20032
|  -  |528534|ROUTE| Et1                |1006 |103444  | 28:99:3a:06:b4:e1 |Mpush 20057
|  -  |528535|ROUTE| Et24               |1007 |103445  | c0:f8:7f:6a:4e:1c |Mpush 20057
|  -  |528544|DROP | DROP               |0    |  -     |                   |   -   
|  -  |528546|ROUTE| Et24               |1007 |103436  | c0:f8:7f:6a:4e:1c |   -   
|  -  |528547|ROUTE| Et1                |1006 |103437  | 28:99:3a:06:b4:e1 |Mpush 21555 21549
|  -  |528548|ROUTE| Et24               |1007 |103468  | c0:f8:7f:6a:4e:1c |Mpush 20355
|  -  |528549|ROUTE| Et1                |1006 |103469  | 28:99:3a:06:b4:e1 |Mpush 20349 20355
|  -  |528550|ROUTE| Et24               |1007 |103442  | c0:f8:7f:6a:4e:1c |Mpush 20355
|  -  |528551|ROUTE| Et1                |1006 |103443  | 28:99:3a:06:b4:e1 |Mpush 20355
|  -  |528556|ROUTE| Et1                |1006 |103450  | 28:99:3a:06:b4:e1 |   -   
|  -  |528557|ROUTE| Et24               |1007 |103451  | c0:f8:7f:6a:4e:1c |Mpush 20254 20170
|  -  |528558|ROUTE| Et1                |1006 |103466  | 28:99:3a:06:b4:e1 |Mpush 20355
|  -  |528559|ROUTE| Et24               |1007 |103452  | c0:f8:7f:6a:4e:1c |Mpush 20254 20170 20355
|  -  |528560|ROUTE| Et1                |1006 |103458  | 28:99:3a:06:b4:e1 |Mpush 20057
|  -  |528561|ROUTE| Et24               |1007 |103453  | c0:f8:7f:6a:4e:1c |Mpush 20254 20170 20057
|  -  |528562|ROUTE| Et1                |1006 |103456  | 28:99:3a:06:b4:e1 |Mpush 20032
|  -  |528563|ROUTE| Et24               |1007 |103462  | c0:f8:7f:6a:4e:1c |Mpush 20254 20170 20032
|  -  |528564|ROUTE| Et1                |1006 |103464  | 28:99:3a:06:b4:e1 |Mpush 20005
|  -  |528565|ROUTE| Et24               |1007 |103460  | c0:f8:7f:6a:4e:1c |Mpush 20254 20170 20005

```

