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

Uptime: 16 hours and 8 minutes
Total memory: 65734516 kB
Free memory: 61635984 kB

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
Ethernet1       20.170.171.171/24   down         down            1500          
Ethernet5.128   20.111.171.171/24   up           up              1500          
Ethernet5.129   20.111.171.171/24   up           up              1500          
Ethernet5.130   20.111.171.171/24   up           up              1500          
Ethernet5.131   20.111.171.171/24   up           up              1500          
Ethernet7       20.32.171.171/24    up           up              1500          
Ethernet9       20.171.254.171/24   admin down   down            1500          
Ethernet24      20.149.171.171/24   admin down   down            1500          
Ethernet25      20.171.179.171/24   admin down   down            1500          
Ethernet46      20.155.171.171/24   admin down   down            1500          
Ethernet47      20.171.172.171/24   up           up              1500          
Ethernet49/1    20.57.171.171/24    up           up              1500          
Loopback0       10.0.0.171/32       up           up             65535          
Management1     192.168.20.171/23   up           up              1500          

```

## show interfaces counters rates | nz

```text
Port      Name             Intvl  In Mbps      %  In Kpps Out Mbps      %
Et5                         0:01     58.9   0.6%        7      0.0   0.0%
Et7       Ribbon            0:01      0.0   0.0%        0     59.2   0.6%
Ma1                         0:01      0.0   0.0%        0      0.2   0.0%

Port      Out Kpps
Et7              7
```

## show isis neighbors

```text
 
Instance  VRF      System Id        Type Interface          SNPA              State Hold time   Circuit Id          
IGP       default  Ribbon-32        L2   Ethernet7          P2P               UP    70          00                  
IGP       default  NOKIA-SR2-57     L2   Ethernet49/1       P2P               UP    20          00                  
IGP       default  PE32-J2-172      L2   Ethernet47         P2P               UP    22          56                  
```

## show isis database detail

```text
Legend:
H - hostname conflict
U - node unreachable

IS-IS Instance: IGP VRF: default
  IS-IS Level 2 Link State Database
    LSPID                   Seq Num  Cksum  Life Length IS  Received LSPID        Flags
    h3c_19_CR16010E-F.00-00      1890  45462  1113    367 L2  0000.0000.0019.00-00  <>
      NLPID: 0xCC(IPv4)
      Hostname: h3c_19_CR16010E-F
      Area addresses: 49
      Interface address: 10.0.0.19
      Interface address: 20.19.149.19
      IS Neighbor          : h49-N540-24Q8L2DD.00 Metric: 10
        IPv4 Neighbor Address: 20.19.149.149
        IPv4 Interface Address: 20.19.149.19
        Adj-sid: 1663 flags: [L V] weight: 0x0
      Reachability         : 10.0.0.19/32 Metric: 0 Type: 1 Up
        SR Prefix-SID: 19 Flags: [N] Algorithm: 0
        SR Prefix-SID: 1019 Flags: [N] Algorithm: 128
        SR Prefix-SID: 1119 Flags: [N] Algorithm: 129
        SR Prefix-SID: 1219 Flags: [N] Algorithm: 130
        SR Prefix-SID: 1319 Flags: [N] Algorithm: 131
      Reachability         : 20.19.149.0/24 Metric: 10 Type: 1 Up
      Reachability         : 192.168.0.0/19 Metric: 0 Type: 1 Up
      Router Capabilities: Router Id: 10.0.0.19 Flags: []
        Maximum SID depth:
          Base MPLS imposition (MSD type 1):  13
        SR Capability: Flags: [I]
          SRGB Base: 20000 Range: 2000
        Algorithms:  0, 128, 129, 130, 131
        Flex Algo: Algorithm: 128 Metric: Min Unidirectional Delay Metric (1) Calc: SPF (0) Prio: 128
          Flags: [] 0x1
        Flex Algo: Algorithm: 129 Metric: TE Metric (2) Calc: SPF (0) Prio: 128
          Flags: [] 0x1
        Flex Algo: Algorithm: 130 Metric: IGP Metric (0) Calc: SPF (0) Prio: 128
          Exclude admin groups: 1
          Flags: [] 0x1
        Flex Algo: Algorithm: 131 Metric: IGP Metric (0) Calc: SPF (0) Prio: 128
          Exclude admin groups: 129
          Flags: [] 0x1
    eantc-jcnr2.00-00           646  33035   870    229 L2  0000.0000.0020.00-00  <>
      NLPID: 0xCC(IPv4) 0x8E(IPv6)
      Hostname: eantc-jcnr2
      Area addresses: 49.0001.00
      Interface address: 10.0.0.83
      IS Neighbor          : h49-N540-24Q8L2DD.00 Metric: 10
        IPv4 Neighbor Address: 20.83.149.149
        IPv4 Interface Address: 20.83.149.83
        Adj-sid: 16 flags: [L V] weight: 0x0
      Reachability         : 20.83.149.0/24 Metric: 10 Type: 1 Up
      Reachability         : 10.0.0.83/32 Metric: 0 Type: 1 Up
        SR Prefix-SID: 83 Flags: [N] Algorithm: 0
      Reachability          : fe80::cc33:4dff:fe3e:5c1d/128 Metric: 0 Type: 1 Up
      Router Capabilities: Router Id: 10.0.0.83 Flags: []
        Maximum SID depth:
          Base MPLS imposition (MSD type 1):  0
        SR Capability: Flags: [I V]
          SRGB Base: 20000 Range: 2000
        Algorithms:  0, 1
      Unsupported TLV: Type: 14 Length: 2
    12502-1.00-00              7685  56666   941    482 L2  0000.0000.0024.00-00  <>
      NLPID: 0xCC(IPv4)
      Hostname: 12502-1
      Area addresses: 49
      Interface address: 10.0.0.24
      Interface address: 20.24.149.24
      IS Neighbor          : h49-N540-24Q8L2DD.00 Metric: 10
        IPv4 Neighbor Address: 20.24.149.149
        IPv4 Interface Address: 20.24.149.24
        Adj-sid: 56639 flags: [L V] weight: 0x0
      Reachability         : 10.0.0.24/32 Metric: 0 Type: 1 Up
        SR Prefix-SID: 24 Flags: [N P] Algorithm: 0
        SR Prefix-SID: 1024 Flags: [N P] Algorithm: 128
        SR Prefix-SID: 1124 Flags: [N P] Algorithm: 129
        SR Prefix-SID: 1224 Flags: [N P] Algorithm: 130
        SR Prefix-SID: 1324 Flags: [N P] Algorithm: 131
      Reachability         : 20.24.149.0/24 Metric: 10 Type: 1 Up
      Reachability         : 192.168.20.0/23 Metric: 0 Type: 1 Up
      Router Capabilities: Router Id: 10.0.0.24 Flags: []
        SR Local Block:
          SRLB Base: 15000 Range: 1000
        Maximum SID depth:
          Base MPLS imposition (MSD type 1):  10
        SR Capability: Flags: [I]
          SRGB Base: 20000 Range: 2000
        Algorithms:  0, 128, 129, 130, 131
        Flex Algo: Algorithm: 128 Metric: Min Unidirectional Delay Metric (1) Calc: SPF (0) Prio: 255
          Flags: [] 0x1
        Flex Algo: Algorithm: 129 Metric: TE Metric (2) Calc: SPF (0) Prio: 255
          Flags: [] 0x1
        Flex Algo: Algorithm: 130 Metric: IGP Metric (0) Calc: SPF (0) Prio: 255
          Exclude admin groups: 129
          Flags: [] 0x1
        Flex Algo: Algorithm: 131 Metric: IGP Metric (0) Calc: SPF (0) Prio: 255
          Exclude admin groups: 128
          Flags: [] 0x1
    Ribbon-32.00-00             209   9444  1129     83 L2  0000.0000.0032.00-00  <>
      Remaining lifetime received: 1195 s Modified to: 1200 s
      NLPID: 0xCC(IPv4)
      Area addresses: 49.0001
      Router Capabilities: Router Id: 10.0.0.32 Flags: []
        SR Local Block:
          SRLB Base: 16 Range: 15344
        Maximum SID depth:
          Base MPLS imposition (MSD type 1):  10
        SR Capability: Flags: [I]
          SRGB Base: 20000 Range: 2000
        Algorithms:  0, 128
      Unsupported TLV: Type: 14 Length: 2
    Ribbon-32.00-01              79    501   936     38 L2  0000.0000.0032.00-01  <>
      Hostname: Ribbon-32
    Ribbon-32.00-02            7006  29172  1184    397 L2  0000.0000.0032.00-02  <>
      Interface address: 10.0.0.32
      Interface address: 20.32.149.32
      Interface address: 20.32.211.32
      Interface address: 20.32.57.32
      Interface address: 20.32.171.32
      IS Neighbor          : NOKIA-SR2-57.00     Metric: 10
        IPv4 Neighbor Address: 20.32.57.57
        IPv4 Interface Address: 20.32.57.32
        Adj-sid: 756646 flags: [L V] weight: 0x0
        Adj-sid: 756647 flags: [L V B] weight: 0x0
      IS Neighbor          : PE31-J2-171.00      Metric: 10
        IPv4 Neighbor Address: 20.32.171.171
        IPv4 Interface Address: 20.32.171.32
        Adj-sid: 756648 flags: [L V] weight: 0x0
        Adj-sid: 756649 flags: [L V B] weight: 0x0
      Reachability         : 10.0.0.32/32 Metric: 0 Type: 1 Up
        SR Prefix-SID: 32 Flags: [N] Algorithm: 0
        SR Prefix-SID: 1032 Flags: [N] Algorithm: 128
      Reachability         : 20.32.149.0/24 Metric: 10 Type: 1 Up
      Reachability         : 20.32.211.0/24 Metric: 10 Type: 1 Up
      Reachability         : 20.32.57.0/24 Metric: 10 Type: 1 Up
      Reachability         : 20.32.171.0/24 Metric: 10 Type: 1 Up
    huawei_254_NetEngine_8000_F8.00-00      7439  24370  1198    266 L2  0000.0000.0254.00-00  <>
      NLPID: 0xCC(IPv4)
      Hostname: huawei_254_NetEngine_8000_F8
      Area addresses: 49
      Interface address: 10.0.0.254
      Interface address: 20.149.254.254
      Interface address: 20.57.254.254
      IS Neighbor          : h49-N540-24Q8L2DD.00 Metric: 10
        IPv4 Neighbor Address: 20.149.254.149
        IPv4 Interface Address: 20.149.254.254
        Adj-sid: 48038 flags: [L V] weight: 0x0
      IS Neighbor          : NOKIA-SR2-57.00     Metric: 10
        IPv4 Neighbor Address: 20.57.254.57
        IPv4 Interface Address: 20.57.254.254
        Adj-sid: 48039 flags: [L V] weight: 0x0
      Reachability         : 10.0.0.254/32 Metric: 0 Type: 1 Up
        SR Prefix-SID: 254 Flags: [N] Algorithm: 0
        SR Prefix-SID: 1254 Flags: [N] Algorithm: 128
      Reachability         : 20.57.254.0/24 Metric: 10 Type: 1 Up
      Reachability         : 20.149.254.0/24 Metric: 10 Type: 1 Up
      Router Capabilities: Router Id: 10.0.0.254 Flags: []
        Flex Algo: Algorithm: 128 Metric: Min Unidirectional Delay Metric (1) Calc: SPF (0) Prio: 128
          Flags: [M] 0x80
      Router Capabilities: Router Id: 10.0.0.254 Flags: []
        Maximum SID depth:
          Base MPLS imposition (MSD type 1):  10
        SR Capability: Flags: [I]
          SRGB Base: 20000 Range: 2000
        Algorithms:  0, 128
    h49-N540-24Q8L2DD.00-00       576  13678  1117    945 L2  0000.0000.0349.00-00  <>
      NLPID: 0xCC(IPv4)
      Hostname: h49-N540-24Q8L2DD
      Area addresses: 49
      Interface address: 10.0.1.49
      IS Neighbor          : h3c_19_CR16010E-F.00 Metric: 10
        IPv4 Neighbor Address: 20.19.149.19
        IPv4 Interface Address: 20.19.149.149
        Adj-sid: 24005 flags: [L V] weight: 0x0
      IS Neighbor          : eantc-jcnr2.00      Metric: 10
        IPv4 Neighbor Address: 20.83.149.83
        IPv4 Interface Address: 20.83.149.149
        Adj-sid: 24021 flags: [L V] weight: 0x0
      IS Neighbor          : 12502-1.00          Metric: 10
        IPv4 Neighbor Address: 20.24.149.24
        IPv4 Interface Address: 20.24.149.149
        Adj-sid: 24019 flags: [L V] weight: 0x0
      IS Neighbor          : huawei_254_NetEngine_8000_F8.00 Metric: 10
        IPv4 Neighbor Address: 20.149.254.254
        IPv4 Interface Address: 20.149.254.149
        Adj-sid: 24001 flags: [L V] weight: 0x0
      IS Neighbor          : h55-8201-24H8FH.00  Metric: 10
        IPv4 Neighbor Address: 20.149.155.155
        IPv4 Interface Address: 20.149.155.149
        Adj-sid: 24013 flags: [L V] weight: 0x0
      IS Neighbor          : 0010.0010.0005.00   Metric: 10
        IPv4 Neighbor Address: 20.5.149.5
        IPv4 Interface Address: 20.5.149.149
        Adj-sid: 24007 flags: [L V] weight: 0x0
      IS Neighbor          : NOKIA-SR2-57.00     Metric: 10
        IPv4 Neighbor Address: 20.57.149.57
        IPv4 Interface Address: 20.57.149.149
        Adj-sid: 24009 flags: [L V] weight: 0x0
      Reachability         : 10.0.1.49/32 Metric: 0 Type: 1 Up
        SR Prefix-SID: 349 Flags: [N] Algorithm: 0
        SR Prefix-SID: 1449 Flags: [N] Algorithm: 129
        SR Prefix-SID: 1649 Flags: [N] Algorithm: 130
        SR Prefix-SID: 1749 Flags: [N] Algorithm: 132
        SR Prefix-SID: 449 Flags: [N] Algorithm: 140
        SR Prefix-SID: 549 Flags: [N] Algorithm: 141
        SR Prefix-SID: 649 Flags: [N] Algorithm: 142
      Reachability         : 20.5.149.0/24 Metric: 10 Type: 1 Up
      Reachability         : 20.19.149.0/24 Metric: 10 Type: 1 Up
      Reachability         : 20.24.149.0/24 Metric: 10 Type: 1 Up
      Reachability         : 20.47.149.0/24 Metric: 10 Type: 1 Up
      Reachability         : 20.57.149.0/24 Metric: 10 Type: 1 Up
      Reachability         : 20.83.149.0/24 Metric: 10 Type: 1 Up
      Reachability         : 20.111.149.0/24 Metric: 10 Type: 1 Up
      Reachability         : 20.149.155.0/24 Metric: 10 Type: 1 Up
      Reachability         : 20.149.254.0/24 Metric: 10 Type: 1 Up
      Unsupported TLV: Type: 14 Length: 2
    h49-N540-24Q8L2DD.00-01        93  27477   920    188 L2  0000.0000.0349.00-01  <>
      Router Capabilities: Router Id: 10.0.1.49 Flags: []
        SR Local Block:
          SRLB Base: 15000 Range: 1000
        Maximum SID depth:
          Base MPLS imposition (MSD type 1):  12
        SR Capability: Flags: [I]
          SRGB Base: 20000 Range: 2000
        Algorithms:  0, 1, 129, 130, 131, 132, 140, 141, 142
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
    h55-8201-24H8FH.00-00       411  28821   800    803 L2  0000.0000.0355.00-00  <>
      NLPID: 0xCC(IPv4)
      Hostname: h55-8201-24H8FH
      Area addresses: 49
      Interface address: 10.0.1.55
      IS Neighbor          : h49-N540-24Q8L2DD.00 Metric: 10
        IPv4 Neighbor Address: 20.149.155.149
        IPv4 Interface Address: 20.149.155.155
        Adj-sid: 24001 flags: [L V] weight: 0x0
      IS Neighbor          : juniper_379_MX304.00 Metric: 10
        IPv4 Neighbor Address: 20.155.179.179
        IPv4 Interface Address: 20.155.179.155
        Adj-sid: 24025 flags: [L V] weight: 0x0
      IS Neighbor          : NOKIA-SR2-57.00     Metric: 10
        IPv4 Neighbor Address: 20.57.155.57
        IPv4 Interface Address: 20.57.155.155
        Adj-sid: 24008 flags: [L V] weight: 0x0
      IS Neighbor          : juniper_379_MX304.00 Metric: 10
        IPv4 Neighbor Address: 30.155.179.179
        IPv4 Interface Address: 30.155.179.155
        Adj-sid: 24045 flags: [L V] weight: 0x0
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
      Reachability         : 20.57.155.0/24 Metric: 10 Type: 1 Up
      Reachability         : 20.149.155.0/24 Metric: 10 Type: 1 Up
      Reachability         : 20.155.179.0/24 Metric: 10 Type: 1 Up
      Reachability         : 30.155.179.0/24 Metric: 10 Type: 1 Up
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
    juniper_379_MX304.00-00        91  57196  1114    568 L2  0000.0001.7900.00-00  <>
      Remaining lifetime received: 1198 s Modified to: 1200 s
      NLPID: 0xCC(IPv4) 0x8E(IPv6)
      Hostname: juniper_379_MX304
      Area addresses: 49.0001.00
      Interface address: 10.0.0.179
      IS Neighbor          : h55-8201-24H8FH.00  Metric: 10
        IPv4 Neighbor Address: 30.155.179.155
        IPv4 Interface Address: 30.155.179.179
        Adj-sid: 25 flags: [L V B] weight: 0x0
      IS Neighbor          : h55-8201-24H8FH.00  Metric: 10
        IPv4 Neighbor Address: 20.155.179.155
        IPv4 Interface Address: 20.155.179.179
        Adj-sid: 24 flags: [L V B] weight: 0x0
      IS Neighbor          : NOKIA-SR2-57.00     Metric: 10
        IPv4 Neighbor Address: 20.57.179.57
        IPv4 Interface Address: 20.57.179.179
        Adj-sid: 23 flags: [L V B] weight: 0x0
      Reachability         : 10.0.0.179/32 Metric: 0 Type: 1 Up
        SR Prefix-SID: 379 Flags: [N] Algorithm: 0
        SR Prefix-SID: 679 Flags: [N] Algorithm: 142
        SR Prefix-SID: 579 Flags: [N] Algorithm: 141
        SR Prefix-SID: 479 Flags: [N] Algorithm: 140
        SR Prefix-SID: 1379 Flags: [N] Algorithm: 130
        SR Prefix-SID: 1279 Flags: [N] Algorithm: 129
        SR Prefix-SID: 1179 Flags: [N] Algorithm: 128
      Reachability         : 20.155.179.0/24 Metric: 10 Type: 1 Up
      Reachability         : 20.57.179.0/24 Metric: 10 Type: 1 Up
      Reachability         : 30.155.179.0/24 Metric: 10 Type: 1 Up
      Router Capabilities: Router Id: 10.0.0.179 Flags: []
        Maximum SID depth:
          Base MPLS imposition (MSD type 1):  4
        SR Capability: Flags: [I V]
          SRGB Base: 20000 Range: 2000
        Algorithms:  0, 1, 128, 129, 130, 140, 141, 142
        Flex Algo: Algorithm: 142 Metric: IGP Metric (0) Calc: SPF (0) Prio: 0
        Flex Algo: Algorithm: 141 Metric: Min Unidirectional Delay Metric (1) Calc: SPF (0) Prio: 0
        Flex Algo: Algorithm: 140 Metric: IGP Metric (0) Calc: SPF (0) Prio: 255
        Flex Algo: Algorithm: 130 Metric: IGP Metric (0) Calc: SPF (0) Prio: 0
          Exclude admin groups: 1
        Flex Algo: Algorithm: 129 Metric: TE Metric (2) Calc: SPF (0) Prio: 0
        Flex Algo: Algorithm: 128 Metric: Min Unidirectional Delay Metric (1) Calc: SPF (0) Prio: 0
      Unsupported TLV: Type: 14 Length: 2
    0010.0010.0005.00-00        207  57832   570    303 L2  0010.0010.0005.00-00  <>
      NLPID: 0xCC(IPv4)
      Area addresses: 49.0005
      Interface address: 10.0.0.5
      IS Neighbor          : h49-N540-24Q8L2DD.00 Metric: 10
        IPv4 Neighbor Address: 20.5.149.149
        IPv4 Interface Address: 20.5.149.5
        Adj-sid: 16000 flags: [L V] weight: 0x0
      Reachability         : 10.0.0.5/32 Metric: 10 Type: 1 Up
        SR Prefix-SID: 5 Flags: [N] Algorithm: 0
        SR Prefix-SID: 1005 Flags: [N] Algorithm: 128
        SR Prefix-SID: 1105 Flags: [N] Algorithm: 129
        SR Prefix-SID: 1205 Flags: [N] Algorithm: 130
        SR Prefix-SID: 1305 Flags: [N] Algorithm: 131
      Reachability         : 20.5.149.0/24 Metric: 10 Type: 1 Up
      Router Capabilities: Router Id: 10.0.0.5 Flags: []
        SR Capability: Flags: [I]
          SRGB Base: 20000 Range: 2000
        Algorithms:  0, 128, 129, 130
        Flex Algo: Algorithm: 128 Metric: Min Unidirectional Delay Metric (1) Calc: SSPF (1) Prio: 128
        Flex Algo: Algorithm: 129 Metric: TE Metric (2) Calc: SSPF (1) Prio: 129
        Flex Algo: Algorithm: 130 Metric: IGP Metric (0) Calc: SSPF (1) Prio: 130
          Exclude admin groups: 1
    NOKIA-SR2-57.00-00        16474  53288  1198   1074 L2  0100.0000.0057.00-00  <>
      NLPID: 0xCC(IPv4) 0x8E(IPv6)
      Hostname: NOKIA-SR2-57
      Area addresses: 49.0000.0000.0057.00
      Interface address: 10.0.0.57
      Interface address: 20.32.57.57
      Interface address: 20.57.149.57
      Interface address: 20.57.155.57
      Interface address: 20.57.171.57
      Interface address: 20.57.172.57
      Interface address: 20.57.179.57
      Interface address: 20.57.211.57
      Interface address: 20.57.254.57
      Interface address: 2002::57
      IS Neighbor (Narrow metrics, unsupported): h49-N540-24Q8L2DD.00 Metric: 10
      IS Neighbor (Narrow metrics, unsupported): h55-8201-24H8FH.00  Metric: 10
      IS Neighbor (Narrow metrics, unsupported): huawei_254_NetEngine_8000_F8.00 Metric: 10
      IS Neighbor (Narrow metrics, unsupported): juniper_379_MX304.00 Metric: 10
      IS Neighbor (Narrow metrics, unsupported): PE32-J2-172.00      Metric: 10
      IS Neighbor (Narrow metrics, unsupported): PE31-J2-171.00      Metric: 10
      IS Neighbor (Narrow metrics, unsupported): Ribbon-32.00        Metric: 10
      IS Neighbor          : h49-N540-24Q8L2DD.00 Metric: 10
        IPv4 Neighbor Address: 20.57.149.149
        IPv4 Interface Address: 20.57.149.57
        Adj-sid: 30149 flags: [L V B] weight: 0x0
      IS Neighbor          : h55-8201-24H8FH.00  Metric: 10
        IPv4 Neighbor Address: 20.57.155.155
        IPv4 Interface Address: 20.57.155.57
        Adj-sid: 30155 flags: [L V B] weight: 0x0
      IS Neighbor          : huawei_254_NetEngine_8000_F8.00 Metric: 10
        IPv4 Neighbor Address: 20.57.254.254
        IPv4 Interface Address: 20.57.254.57
        Adj-sid: 30254 flags: [L V B] weight: 0x0
      IS Neighbor          : juniper_379_MX304.00 Metric: 10
        IPv4 Neighbor Address: 20.57.179.179
        IPv4 Interface Address: 20.57.179.57
        Adj-sid: 30179 flags: [L V B] weight: 0x0
      IS Neighbor          : PE32-J2-172.00      Metric: 10
        IPv4 Neighbor Address: 20.57.172.172
        IPv4 Interface Address: 20.57.172.57
        Adj-sid: 30172 flags: [L V B] weight: 0x0
      IS Neighbor          : PE31-J2-171.00      Metric: 10
        IPv4 Neighbor Address: 20.57.171.171
        IPv4 Interface Address: 20.57.171.57
        Adj-sid: 30171 flags: [L V B] weight: 0x0
      IS Neighbor          : Ribbon-32.00        Metric: 10
        IPv4 Neighbor Address: 20.32.57.32
        IPv4 Interface Address: 20.32.57.57
        Adj-sid: 30032 flags: [L V B] weight: 0x0
      Reachability (Narrow metrics, unsupported): 10.0.0.57/32 Metric: 0 Type: 1
      Reachability (Narrow metrics, unsupported): 20.32.57.0/24 Metric: 10 Type: 1
      Reachability (Narrow metrics, unsupported): 20.57.149.0/24 Metric: 10 Type: 1
      Reachability (Narrow metrics, unsupported): 20.57.155.0/24 Metric: 10 Type: 1
      Reachability (Narrow metrics, unsupported): 20.57.171.0/24 Metric: 10 Type: 1
      Reachability (Narrow metrics, unsupported): 20.57.172.0/24 Metric: 10 Type: 1
      Reachability (Narrow metrics, unsupported): 20.57.179.0/24 Metric: 10 Type: 1
      Reachability (Narrow metrics, unsupported): 20.57.211.0/24 Metric: 10 Type: 1
      Reachability (Narrow metrics, unsupported): 20.57.254.0/24 Metric: 10 Type: 1
      Reachability         : 10.0.0.57/32 Metric: 0 Type: 1 Up
        SR Prefix-SID: 57 Flags: [N P] Algorithm: 0
        SR Prefix-SID: 1057 Flags: [N P] Algorithm: 128
        SR Prefix-SID: 1157 Flags: [N P] Algorithm: 129
        SR Prefix-SID: 1257 Flags: [N P] Algorithm: 130
        SR Prefix-SID: 1357 Flags: [N P] Algorithm: 131
        SR Prefix-SID: 1457 Flags: [N P] Algorithm: 132
      Reachability         : 20.32.57.0/24 Metric: 10 Type: 1 Up
      Reachability         : 20.57.149.0/24 Metric: 10 Type: 1 Up
      Reachability         : 20.57.155.0/24 Metric: 10 Type: 1 Up
      Reachability         : 20.57.171.0/24 Metric: 10 Type: 1 Up
      Reachability         : 20.57.172.0/24 Metric: 10 Type: 1 Up
      Reachability         : 20.57.179.0/24 Metric: 10 Type: 1 Up
      Reachability         : 20.57.211.0/24 Metric: 10 Type: 1 Up
      Reachability         : 20.57.254.0/24 Metric: 10 Type: 1 Up
      Reachability          : 2002::57/128 Metric: 0 Type: 1 Up
      Router Capabilities: Router Id: 10.0.0.57 Flags: []
        Maximum SID depth:
          Base MPLS imposition (MSD type 1):  12
        SR Capability: Flags: [I V]
          SRGB Base: 20000 Range: 2000
        Algorithms:  0, 128, 129, 130, 131, 132
        Flex Algo: Algorithm: 128 Metric: Min Unidirectional Delay Metric (1) Calc: SPF (0) Prio: 255
          Flags: [M] 0x80
        Flex Algo: Algorithm: 129 Metric: TE Metric (2) Calc: SPF (0) Prio: 100
          Flags: [M] 0x80
        Flex Algo: Algorithm: 130 Metric: IGP Metric (0) Calc: SPF (0) Prio: 100
          Exclude admin groups: 1
          Flags: [M] 0x80
        Flex Algo: Algorithm: 131 Metric: IGP Metric (0) Calc: SPF (0) Prio: 100
          Exclude admin groups: 127
          Flags: [M] 0x80
        Flex Algo: Algorithm: 132 Metric: IGP Metric (0) Calc: SPF (0) Prio: 100
          Exclude admin groups: 255
          Flags: [M] 0x80
    PE31-J2-171.00-00           489  51511  1078    413 L2  0100.0000.0171.00-00  <>
      LSP generation remaining wait time: 0 ms
      Time remaining until refresh: 778 s
      NLPID: 0xCC(IPv4)
      Hostname: PE31-J2-171
      Area addresses: 49.0000
      Interface address: 20.32.171.171
      Interface address: 20.57.171.171
      Interface address: 20.171.172.171
      Interface address: 10.0.0.171
      IS Neighbor          : Ribbon-32.00        Metric: 10
        IPv4 Neighbor Address: 20.32.171.32
        IPv4 Interface Address: 20.32.171.171
        Adj-sid: 362148 flags: [L V] weight: 0x0
      IS Neighbor          : NOKIA-SR2-57.00     Metric: 10
        IPv4 Neighbor Address: 20.57.171.57
        IPv4 Interface Address: 20.57.171.171
        Adj-sid: 362147 flags: [L V] weight: 0x0
      IS Neighbor          : PE32-J2-172.00      Metric: 10
        IPv4 Neighbor Address: 20.171.172.172
        IPv4 Interface Address: 20.171.172.171
        Adj-sid: 362146 flags: [L V] weight: 0x0
      Reachability         : 20.32.171.0/24 Metric: 10 Type: 1 Up
      Reachability         : 20.57.171.0/24 Metric: 10 Type: 1 Up
      Reachability         : 20.171.172.0/24 Metric: 10 Type: 1 Up
      Reachability         : 10.0.0.171/32 Metric: 0 Type: 1 Up
        SR Prefix-SID: 171 Flags: [N] Algorithm: 0
        SR Prefix-SID: 1171 Flags: [N] Algorithm: 128
        SR Prefix-SID: 1271 Flags: [N] Algorithm: 129
        SR Prefix-SID: 1371 Flags: [N] Algorithm: 130
        SR Prefix-SID: 1471 Flags: [N] Algorithm: 131
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
          Exclude admin groups: 1
        Flex Algo: Algorithm: 129 Metric: TE Metric (2) Calc: SPF (0) Prio: 237
        Flex Algo: Algorithm: 128 Metric: Min Unidirectional Delay Metric (1) Calc: SPF (0) Prio: 237
    PE32-J2-172.00-00            14   4215   968    310 L2  0100.0000.0172.00-00  <>
      Remaining lifetime received: 1199 s Modified to: 1200 s
      NLPID: 0xCC(IPv4)
      Hostname: PE32-J2-172
      Area addresses: 49.0000
      Interface address: 20.57.172.172
      Interface address: 20.171.172.172
      Interface address: 10.0.0.172
      IS Neighbor          : NOKIA-SR2-57.00     Metric: 10
        IPv4 Neighbor Address: 20.57.172.57
        IPv4 Interface Address: 20.57.172.172
        Adj-sid: 411297 flags: [L V] weight: 0x0
      IS Neighbor          : PE31-J2-171.00      Metric: 10
        IPv4 Neighbor Address: 20.171.172.171
        IPv4 Interface Address: 20.171.172.172
        Adj-sid: 411296 flags: [L V] weight: 0x0
      Reachability         : 10.0.0.172/32 Metric: 0 Type: 1 Up
        SR Prefix-SID: 172 Flags: [N] Algorithm: 0
        SR Prefix-SID: 1272 Flags: [N] Algorithm: 129
        SR Prefix-SID: 1372 Flags: [N] Algorithm: 130
        SR Prefix-SID: 1472 Flags: [N] Algorithm: 131
      Reachability         : 20.57.172.0/24 Metric: 10 Type: 1 Up
      Reachability         : 20.171.172.0/24 Metric: 10 Type: 1 Up
      Router Capabilities: Router Id: 10.0.0.172 Flags: []
        SR Local Block:
          SRLB Base: 965536 Range: 65536
        Area leader priority: 250 algorithm: 0
        Maximum SID depth:
          Base MPLS imposition (MSD type 1):  12
        SR Capability: Flags: [I]
          SRGB Base: 20000 Range: 2000
        Algorithms:  0, 129, 130, 131
        Flex Algo: Algorithm: 131 Metric: IGP Metric (0) Calc: SPF (0) Prio: 237
          Exclude admin groups: 127
        Flex Algo: Algorithm: 130 Metric: IGP Metric (0) Calc: SPF (0) Prio: 237
          Exclude admin groups: 1
        Flex Algo: Algorithm: 129 Metric: TE Metric (2) Calc: SPF (0) Prio: 237
```

## show isis database traffic-engineering

```text
Legend:
H - hostname conflict
U - node unreachable

IS-IS Instance: IGP VRF: default
  IS-IS Level 2 Link State Database
    LSPID                   Seq Num  Cksum  Life Length IS  Received LSPID        Flags
    h3c_19_CR16010E-F.00-00      1890  45462  1112    367 L2  0000.0000.0019.00-00  <>
      NLPID: 0xCC(IPv4)
      Hostname: h3c_19_CR16010E-F
      TE IPv4 router ID: 10.0.0.19
      Area addresses: 49
      Interface address: 10.0.0.19
      Interface address: 20.19.149.19
      IS Neighbor          : h49-N540-24Q8L2DD.00 Metric: 10
        IPv4 Neighbor Address: 20.19.149.149
        IPv4 Interface Address: 20.19.149.19
        Adj-sid: 1663 flags: [L V] weight: 0x0
        Application Specific Link Attributes:
          Standard applications: Flex-Algo
          User-defined applications: APP3
            TE default metric: 100
            Maximum link BW: 0.00 bps
            Maximum reservable link BW: 0.00 bps
            Unreserved BW:
                TE class 0: 0.00 bps	TE class 1: 0.00 bps	TE class 2: 0.00 bps
                TE class 3: 0.00 bps	TE class 4: 0.00 bps	TE class 5: 0.00 bps
                TE class 6: 0.00 bps	TE class 7: 0.00 bps
            Min/Max unidirectional link delay: 11/11 us
      Reachability         : 10.0.0.19/32 Metric: 0 Type: 1 Up
        SR Prefix-SID: 19 Flags: [N] Algorithm: 0
        SR Prefix-SID: 1019 Flags: [N] Algorithm: 128
        SR Prefix-SID: 1119 Flags: [N] Algorithm: 129
        SR Prefix-SID: 1219 Flags: [N] Algorithm: 130
        SR Prefix-SID: 1319 Flags: [N] Algorithm: 131
      Reachability         : 20.19.149.0/24 Metric: 10 Type: 1 Up
      Reachability         : 192.168.0.0/19 Metric: 0 Type: 1 Up
      Router Capabilities: Router Id: 10.0.0.19 Flags: []
        Maximum SID depth:
          Base MPLS imposition (MSD type 1):  13
        SR Capability: Flags: [I]
          SRGB Base: 20000 Range: 2000
        Algorithms:  0, 128, 129, 130, 131
        Flex Algo: Algorithm: 128 Metric: Min Unidirectional Delay Metric (1) Calc: SPF (0) Prio: 128
          Flags: [] 0x1
        Flex Algo: Algorithm: 129 Metric: TE Metric (2) Calc: SPF (0) Prio: 128
          Flags: [] 0x1
        Flex Algo: Algorithm: 130 Metric: IGP Metric (0) Calc: SPF (0) Prio: 128
          Exclude admin groups: 1
          Flags: [] 0x1
        Flex Algo: Algorithm: 131 Metric: IGP Metric (0) Calc: SPF (0) Prio: 128
          Exclude admin groups: 129
          Flags: [] 0x1
    eantc-jcnr2.00-00           646  33035   869    229 L2  0000.0000.0020.00-00  <>
      NLPID: 0xCC(IPv4) 0x8E(IPv6)
      Hostname: eantc-jcnr2
      TE IPv4 router ID: 10.0.0.83
      TE IPv6 router ID: ::7f00:1
      Area addresses: 49.0001.00
      Interface address: 10.0.0.83
      IS Neighbor          : h49-N540-24Q8L2DD.00 Metric: 10
        IPv4 Neighbor Address: 20.83.149.149
        IPv4 Interface Address: 20.83.149.83
        Adj-sid: 16 flags: [L V] weight: 0x0
      Reachability         : 20.83.149.0/24 Metric: 10 Type: 1 Up
      Reachability         : 10.0.0.83/32 Metric: 0 Type: 1 Up
        SR Prefix-SID: 83 Flags: [N] Algorithm: 0
      Reachability          : fe80::cc33:4dff:fe3e:5c1d/128 Metric: 0 Type: 1 Up
      Router Capabilities: Router Id: 10.0.0.83 Flags: []
        Maximum SID depth:
          Base MPLS imposition (MSD type 1):  0
        SR Capability: Flags: [I V]
          SRGB Base: 20000 Range: 2000
        Algorithms:  0, 1
      Unsupported TLV: Type: 14 Length: 2
    12502-1.00-00              7685  56666   941    482 L2  0000.0000.0024.00-00  <>
      NLPID: 0xCC(IPv4)
      Hostname: 12502-1
      TE IPv4 router ID: 10.0.0.24
      Area addresses: 49
      Interface address: 10.0.0.24
      Interface address: 20.24.149.24
      IS Neighbor          : h49-N540-24Q8L2DD.00 Metric: 10
        IPv4 Neighbor Address: 20.24.149.149
        IPv4 Interface Address: 20.24.149.24
        Adj-sid: 56639 flags: [L V] weight: 0x0
        TE default metric: 10
        Maximum link BW: 0.00 bps
        Maximum reservable link BW: 0.00 bps
        Unreserved BW:
            TE class 0: 0.00 bps	TE class 1: 0.00 bps	TE class 2: 0.00 bps
            TE class 3: 0.00 bps	TE class 4: 0.00 bps	TE class 5: 0.00 bps
            TE class 6: 0.00 bps	TE class 7: 0.00 bps
        Application Specific Link Attributes:
          Standard applications: Flex-Algo
          User-defined applications: APP3
            TE default metric: 10
            Maximum link BW: 0.00 bps
            Maximum reservable link BW: 0.00 bps
            Unreserved BW:
                TE class 0: 0.00 bps	TE class 1: 0.00 bps	TE class 2: 0.00 bps
                TE class 3: 0.00 bps	TE class 4: 0.00 bps	TE class 5: 0.00 bps
                TE class 6: 0.00 bps	TE class 7: 0.00 bps
      Reachability         : 10.0.0.24/32 Metric: 0 Type: 1 Up
        SR Prefix-SID: 24 Flags: [N P] Algorithm: 0
        SR Prefix-SID: 1024 Flags: [N P] Algorithm: 128
        SR Prefix-SID: 1124 Flags: [N P] Algorithm: 129
        SR Prefix-SID: 1224 Flags: [N P] Algorithm: 130
        SR Prefix-SID: 1324 Flags: [N P] Algorithm: 131
      Reachability         : 20.24.149.0/24 Metric: 10 Type: 1 Up
      Reachability         : 192.168.20.0/23 Metric: 0 Type: 1 Up
      Router Capabilities: Router Id: 10.0.0.24 Flags: []
        SR Local Block:
          SRLB Base: 15000 Range: 1000
        Maximum SID depth:
          Base MPLS imposition (MSD type 1):  10
        SR Capability: Flags: [I]
          SRGB Base: 20000 Range: 2000
        Algorithms:  0, 128, 129, 130, 131
        Flex Algo: Algorithm: 128 Metric: Min Unidirectional Delay Metric (1) Calc: SPF (0) Prio: 255
          Flags: [] 0x1
        Flex Algo: Algorithm: 129 Metric: TE Metric (2) Calc: SPF (0) Prio: 255
          Flags: [] 0x1
        Flex Algo: Algorithm: 130 Metric: IGP Metric (0) Calc: SPF (0) Prio: 255
          Exclude admin groups: 129
          Flags: [] 0x1
        Flex Algo: Algorithm: 131 Metric: IGP Metric (0) Calc: SPF (0) Prio: 255
          Exclude admin groups: 128
          Flags: [] 0x1
    Ribbon-32.00-00             209   9444  1129     83 L2  0000.0000.0032.00-00  <>
      Remaining lifetime received: 1195 s Modified to: 1200 s
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
        Algorithms:  0, 128
      Unsupported TLV: Type: 14 Length: 2
    Ribbon-32.00-01              79    501   936     38 L2  0000.0000.0032.00-01  <>
      Hostname: Ribbon-32
    Ribbon-32.00-02            7006  29172  1184    397 L2  0000.0000.0032.00-02  <>
      Interface address: 10.0.0.32
      Interface address: 20.32.149.32
      Interface address: 20.32.211.32
      Interface address: 20.32.57.32
      Interface address: 20.32.171.32
      IS Neighbor          : NOKIA-SR2-57.00     Metric: 10
        IPv4 Neighbor Address: 20.32.57.57
        IPv4 Interface Address: 20.32.57.32
        Adj-sid: 756646 flags: [L V] weight: 0x0
        Adj-sid: 756647 flags: [L V B] weight: 0x0
        TE default metric: 12
        Maximum link BW: 10.00 Gbps
        Maximum reservable link BW: 10.00 Gbps
        Unreserved BW:
            TE class 0: 10.00 Gbps	TE class 1: 10.00 Gbps	TE class 2: 10.00 Gbps
            TE class 3: 10.00 Gbps	TE class 4: 10.00 Gbps	TE class 5: 10.00 Gbps
            TE class 6: 10.00 Gbps	TE class 7: 10.00 Gbps
        Min/Max unidirectional link delay: 11/11 us
        Application Specific Link Attributes:
          Standard applications: Flex-Algo
            TE default metric: 12
            Min/Max unidirectional link delay: 11/11 us
      IS Neighbor          : PE31-J2-171.00      Metric: 10
        IPv4 Neighbor Address: 20.32.171.171
        IPv4 Interface Address: 20.32.171.32
        Adj-sid: 756648 flags: [L V] weight: 0x0
        Adj-sid: 756649 flags: [L V B] weight: 0x0
        TE default metric: 12
        Maximum link BW: 10.00 Gbps
        Maximum reservable link BW: 10.00 Gbps
        Unreserved BW:
            TE class 0: 10.00 Gbps	TE class 1: 10.00 Gbps	TE class 2: 10.00 Gbps
            TE class 3: 10.00 Gbps	TE class 4: 10.00 Gbps	TE class 5: 10.00 Gbps
            TE class 6: 10.00 Gbps	TE class 7: 10.00 Gbps
        Min/Max unidirectional link delay: 11/11 us
        Application Specific Link Attributes:
          Standard applications: Flex-Algo
            TE default metric: 12
            Min/Max unidirectional link delay: 11/11 us
      Reachability         : 10.0.0.32/32 Metric: 0 Type: 1 Up
        SR Prefix-SID: 32 Flags: [N] Algorithm: 0
        SR Prefix-SID: 1032 Flags: [N] Algorithm: 128
      Reachability         : 20.32.149.0/24 Metric: 10 Type: 1 Up
      Reachability         : 20.32.211.0/24 Metric: 10 Type: 1 Up
      Reachability         : 20.32.57.0/24 Metric: 10 Type: 1 Up
      Reachability         : 20.32.171.0/24 Metric: 10 Type: 1 Up
    huawei_254_NetEngine_8000_F8.00-00      7439  24370  1198    266 L2  0000.0000.0254.00-00  <>
      NLPID: 0xCC(IPv4)
      Hostname: huawei_254_NetEngine_8000_F8
      Area addresses: 49
      Interface address: 10.0.0.254
      Interface address: 20.149.254.254
      Interface address: 20.57.254.254
      IS Neighbor          : h49-N540-24Q8L2DD.00 Metric: 10
        IPv4 Neighbor Address: 20.149.254.149
        IPv4 Interface Address: 20.149.254.254
        Adj-sid: 48038 flags: [L V] weight: 0x0
        Application Specific Link Attributes:
          Standard applications: Flex-Algo
            TE default metric: 12
            Min/Max unidirectional link delay: 11/11 us
      IS Neighbor          : NOKIA-SR2-57.00     Metric: 10
        IPv4 Neighbor Address: 20.57.254.57
        IPv4 Interface Address: 20.57.254.254
        Adj-sid: 48039 flags: [L V] weight: 0x0
        Application Specific Link Attributes:
          Standard applications: Flex-Algo
            TE default metric: 12
            Min/Max unidirectional link delay: 11/11 us
      Reachability         : 10.0.0.254/32 Metric: 0 Type: 1 Up
        SR Prefix-SID: 254 Flags: [N] Algorithm: 0
        SR Prefix-SID: 1254 Flags: [N] Algorithm: 128
      Reachability         : 20.57.254.0/24 Metric: 10 Type: 1 Up
      Reachability         : 20.149.254.0/24 Metric: 10 Type: 1 Up
      Router Capabilities: Router Id: 10.0.0.254 Flags: []
        Flex Algo: Algorithm: 128 Metric: Min Unidirectional Delay Metric (1) Calc: SPF (0) Prio: 128
          Flags: [M] 0x80
      Router Capabilities: Router Id: 10.0.0.254 Flags: []
        Maximum SID depth:
          Base MPLS imposition (MSD type 1):  10
        SR Capability: Flags: [I]
          SRGB Base: 20000 Range: 2000
        Algorithms:  0, 128
    h49-N540-24Q8L2DD.00-00       576  13678  1117    945 L2  0000.0000.0349.00-00  <>
      NLPID: 0xCC(IPv4)
      Hostname: h49-N540-24Q8L2DD
      TE IPv4 router ID: 10.0.1.49
      Area addresses: 49
      Interface address: 10.0.1.49
      IS Neighbor          : h3c_19_CR16010E-F.00 Metric: 10
        IPv4 Neighbor Address: 20.19.149.19
        IPv4 Interface Address: 20.19.149.149
        Adj-sid: 24005 flags: [L V] weight: 0x0
        Maximum link BW: 10.00 Gbps
        Min/Max unidirectional link delay: 11/11 us
        Average unidirectional link delay: 11 us
        Application Specific Link Attributes:
          Standard applications: Flex-Algo
          User-defined applications: APP3
            TE default metric: 12
            Maximum link BW: 10.00 Gbps
            Min/Max unidirectional link delay: 11/11 us
      IS Neighbor          : eantc-jcnr2.00      Metric: 10
        IPv4 Neighbor Address: 20.83.149.83
        IPv4 Interface Address: 20.83.149.149
        Adj-sid: 24021 flags: [L V] weight: 0x0
        Maximum link BW: 10.00 Gbps
        Min/Max unidirectional link delay: 11/11 us
        Average unidirectional link delay: 11 us
        Application Specific Link Attributes:
          Standard applications: Flex-Algo
          User-defined applications: APP3
            TE default metric: 12
            Maximum link BW: 10.00 Gbps
            Min/Max unidirectional link delay: 11/11 us
      IS Neighbor          : 12502-1.00          Metric: 10
        IPv4 Neighbor Address: 20.24.149.24
        IPv4 Interface Address: 20.24.149.149
        Adj-sid: 24019 flags: [L V] weight: 0x0
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
        Adj-sid: 24001 flags: [L V] weight: 0x0
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
        Adj-sid: 24013 flags: [L V] weight: 0x0
        Maximum link BW: 100.00 Gbps
        Min/Max unidirectional link delay: 2/2 us
        Average unidirectional link delay: 2 us
        Application Specific Link Attributes:
          Standard applications: Flex-Algo
          User-defined applications: APP3
            TE default metric: 12
            Maximum link BW: 100.00 Gbps
            Min/Max unidirectional link delay: 2/2 us
      IS Neighbor          : 0010.0010.0005.00   Metric: 10
        IPv4 Neighbor Address: 20.5.149.5
        IPv4 Interface Address: 20.5.149.149
        Adj-sid: 24007 flags: [L V] weight: 0x0
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
        Adj-sid: 24009 flags: [L V] weight: 0x0
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
        SR Prefix-SID: 1649 Flags: [N] Algorithm: 130
        SR Prefix-SID: 1749 Flags: [N] Algorithm: 132
        SR Prefix-SID: 449 Flags: [N] Algorithm: 140
        SR Prefix-SID: 549 Flags: [N] Algorithm: 141
        SR Prefix-SID: 649 Flags: [N] Algorithm: 142
      Reachability         : 20.5.149.0/24 Metric: 10 Type: 1 Up
      Reachability         : 20.19.149.0/24 Metric: 10 Type: 1 Up
      Reachability         : 20.24.149.0/24 Metric: 10 Type: 1 Up
      Reachability         : 20.47.149.0/24 Metric: 10 Type: 1 Up
      Reachability         : 20.57.149.0/24 Metric: 10 Type: 1 Up
      Reachability         : 20.83.149.0/24 Metric: 10 Type: 1 Up
      Reachability         : 20.111.149.0/24 Metric: 10 Type: 1 Up
      Reachability         : 20.149.155.0/24 Metric: 10 Type: 1 Up
      Reachability         : 20.149.254.0/24 Metric: 10 Type: 1 Up
      Unsupported TLV: Type: 14 Length: 2
    h49-N540-24Q8L2DD.00-01        93  27477   920    188 L2  0000.0000.0349.00-01  <>
      Router Capabilities: Router Id: 10.0.1.49 Flags: []
        SR Local Block:
          SRLB Base: 15000 Range: 1000
        Maximum SID depth:
          Base MPLS imposition (MSD type 1):  12
        SR Capability: Flags: [I]
          SRGB Base: 20000 Range: 2000
        Algorithms:  0, 1, 129, 130, 131, 132, 140, 141, 142
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
    h55-8201-24H8FH.00-00       411  28821   800    803 L2  0000.0000.0355.00-00  <>
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
      IS Neighbor          : juniper_379_MX304.00 Metric: 10
        IPv4 Neighbor Address: 20.155.179.179
        IPv4 Interface Address: 20.155.179.155
        Adj-sid: 24025 flags: [L V] weight: 0x0
        Maximum link BW: 100.00 Gbps
        Min/Max unidirectional link delay: 11/11 us
        Average unidirectional link delay: 11 us
        Application Specific Link Attributes:
          Standard applications: Flex-Algo
          User-defined applications: APP3
            Administrative group (Color): 12
            TE default metric: 12
            Maximum link BW: 100.00 Gbps
            Min/Max unidirectional link delay: 11/11 us
      IS Neighbor          : NOKIA-SR2-57.00     Metric: 10
        IPv4 Neighbor Address: 20.57.155.57
        IPv4 Interface Address: 20.57.155.155
        Adj-sid: 24008 flags: [L V] weight: 0x0
        Maximum link BW: 10.00 Gbps
        Min/Max unidirectional link delay: 6/10 us
        Average unidirectional link delay: 7 us
        Unidirectional link delay variation: 1 us
        Application Specific Link Attributes:
          Standard applications: Flex-Algo
          User-defined applications: APP3
            Administrative group (Color): 255
            TE default metric: 12
            Maximum link BW: 10.00 Gbps
            Min/Max unidirectional link delay: 6/10 us
      IS Neighbor          : juniper_379_MX304.00 Metric: 10
        IPv4 Neighbor Address: 30.155.179.179
        IPv4 Interface Address: 30.155.179.155
        Adj-sid: 24045 flags: [L V] weight: 0x0
        Maximum link BW: 1.00 Gbps
        Min/Max unidirectional link delay: 100000/100000 us
        Average unidirectional link delay: 100000 us
        Application Specific Link Attributes:
          Standard applications: Flex-Algo
          User-defined applications: APP3
            Maximum link BW: 1.00 Gbps
            Min/Max unidirectional link delay: 100000/100000 us
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
      Reachability         : 20.57.155.0/24 Metric: 10 Type: 1 Up
      Reachability         : 20.149.155.0/24 Metric: 10 Type: 1 Up
      Reachability         : 20.155.179.0/24 Metric: 10 Type: 1 Up
      Reachability         : 30.155.179.0/24 Metric: 10 Type: 1 Up
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
    juniper_379_MX304.00-00        91  57196  1113    568 L2  0000.0001.7900.00-00  <>
      Remaining lifetime received: 1198 s Modified to: 1200 s
      NLPID: 0xCC(IPv4) 0x8E(IPv6)
      Hostname: juniper_379_MX304
      TE IPv4 router ID: 10.0.0.179
      Area addresses: 49.0001.00
      Interface address: 10.0.0.179
      IS Neighbor          : h55-8201-24H8FH.00  Metric: 10
        IPv4 Neighbor Address: 30.155.179.155
        IPv4 Interface Address: 30.155.179.179
        Adj-sid: 25 flags: [L V B] weight: 0x0
        Administrative group (Color): 12
        Maximum link BW: 1.00 Gbps
        Min/Max unidirectional link delay: 100000/100000 us
        Average unidirectional link delay: 100000 us
        Application Specific Link Attributes:
          Standard applications: Flex-Algo
            Administrative group (Color): 1,12
            TE default metric: 12
            Min/Max unidirectional link delay: 100000/100000 us
      IS Neighbor          : h55-8201-24H8FH.00  Metric: 10
        IPv4 Neighbor Address: 20.155.179.155
        IPv4 Interface Address: 20.155.179.179
        Adj-sid: 24 flags: [L V B] weight: 0x0
        Maximum link BW: 100.00 Gbps
        Min/Max unidirectional link delay: 600/1430 us
        Average unidirectional link delay: 895 us
        Unidirectional link delay variation: 17200 us
        Application Specific Link Attributes:
          Standard applications: Flex-Algo
            Administrative group (Color): 1
            TE default metric: 12
            Min/Max unidirectional link delay: 600/1430 us
      IS Neighbor          : NOKIA-SR2-57.00     Metric: 10
        IPv4 Neighbor Address: 20.57.179.57
        IPv4 Interface Address: 20.57.179.179
        Adj-sid: 23 flags: [L V B] weight: 0x0
        Maximum link BW: 100.00 Gbps
        Min/Max unidirectional link delay: 48/86 us
        Average unidirectional link delay: 65 us
        Unidirectional link delay variation: 20 us
        Application Specific Link Attributes:
          Standard applications: Flex-Algo
            TE default metric: 12
            Min/Max unidirectional link delay: 48/86 us
      Reachability         : 10.0.0.179/32 Metric: 0 Type: 1 Up
        SR Prefix-SID: 379 Flags: [N] Algorithm: 0
        SR Prefix-SID: 679 Flags: [N] Algorithm: 142
        SR Prefix-SID: 579 Flags: [N] Algorithm: 141
        SR Prefix-SID: 479 Flags: [N] Algorithm: 140
        SR Prefix-SID: 1379 Flags: [N] Algorithm: 130
        SR Prefix-SID: 1279 Flags: [N] Algorithm: 129
        SR Prefix-SID: 1179 Flags: [N] Algorithm: 128
      Reachability         : 20.155.179.0/24 Metric: 10 Type: 1 Up
      Reachability         : 20.57.179.0/24 Metric: 10 Type: 1 Up
      Reachability         : 30.155.179.0/24 Metric: 10 Type: 1 Up
      Router Capabilities: Router Id: 10.0.0.179 Flags: []
        Maximum SID depth:
          Base MPLS imposition (MSD type 1):  4
        SR Capability: Flags: [I V]
          SRGB Base: 20000 Range: 2000
        Algorithms:  0, 1, 128, 129, 130, 140, 141, 142
        Flex Algo: Algorithm: 142 Metric: IGP Metric (0) Calc: SPF (0) Prio: 0
        Flex Algo: Algorithm: 141 Metric: Min Unidirectional Delay Metric (1) Calc: SPF (0) Prio: 0
        Flex Algo: Algorithm: 140 Metric: IGP Metric (0) Calc: SPF (0) Prio: 255
        Flex Algo: Algorithm: 130 Metric: IGP Metric (0) Calc: SPF (0) Prio: 0
          Exclude admin groups: 1
        Flex Algo: Algorithm: 129 Metric: TE Metric (2) Calc: SPF (0) Prio: 0
        Flex Algo: Algorithm: 128 Metric: Min Unidirectional Delay Metric (1) Calc: SPF (0) Prio: 0
      Unsupported TLV: Type: 14 Length: 2
    0010.0010.0005.00-00        207  57832   569    303 L2  0010.0010.0005.00-00  <>
      NLPID: 0xCC(IPv4)
      TE IPv4 router ID: 10.0.0.5
      Area addresses: 49.0005
      Interface address: 10.0.0.5
      IS Neighbor          : h49-N540-24Q8L2DD.00 Metric: 10
        IPv4 Neighbor Address: 20.5.149.149
        IPv4 Interface Address: 20.5.149.5
        Adj-sid: 16000 flags: [L V] weight: 0x0
        TE default metric: 12
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
            TE default metric: 12
            Min/Max unidirectional link delay: 11/11 us
            Average unidirectional link delay: 11 us
      Reachability         : 10.0.0.5/32 Metric: 10 Type: 1 Up
        SR Prefix-SID: 5 Flags: [N] Algorithm: 0
        SR Prefix-SID: 1005 Flags: [N] Algorithm: 128
        SR Prefix-SID: 1105 Flags: [N] Algorithm: 129
        SR Prefix-SID: 1205 Flags: [N] Algorithm: 130
        SR Prefix-SID: 1305 Flags: [N] Algorithm: 131
      Reachability         : 20.5.149.0/24 Metric: 10 Type: 1 Up
      Router Capabilities: Router Id: 10.0.0.5 Flags: []
        SR Capability: Flags: [I]
          SRGB Base: 20000 Range: 2000
        Algorithms:  0, 128, 129, 130
        Flex Algo: Algorithm: 128 Metric: Min Unidirectional Delay Metric (1) Calc: SSPF (1) Prio: 128
        Flex Algo: Algorithm: 129 Metric: TE Metric (2) Calc: SSPF (1) Prio: 129
        Flex Algo: Algorithm: 130 Metric: IGP Metric (0) Calc: SSPF (1) Prio: 130
          Exclude admin groups: 1
    NOKIA-SR2-57.00-00        16474  53288  1198   1074 L2  0100.0000.0057.00-00  <>
      NLPID: 0xCC(IPv4) 0x8E(IPv6)
      Hostname: NOKIA-SR2-57
      TE IPv4 router ID: 10.0.0.57
      TE IPv6 router ID: 2002::57
      Area addresses: 49.0000.0000.0057.00
      Interface address: 10.0.0.57
      Interface address: 20.32.57.57
      Interface address: 20.57.149.57
      Interface address: 20.57.155.57
      Interface address: 20.57.171.57
      Interface address: 20.57.172.57
      Interface address: 20.57.179.57
      Interface address: 20.57.211.57
      Interface address: 20.57.254.57
      Interface address: 2002::57
      IS Neighbor (Narrow metrics, unsupported): h49-N540-24Q8L2DD.00 Metric: 10
      IS Neighbor (Narrow metrics, unsupported): h55-8201-24H8FH.00  Metric: 10
      IS Neighbor (Narrow metrics, unsupported): huawei_254_NetEngine_8000_F8.00 Metric: 10
      IS Neighbor (Narrow metrics, unsupported): juniper_379_MX304.00 Metric: 10
      IS Neighbor (Narrow metrics, unsupported): PE32-J2-172.00      Metric: 10
      IS Neighbor (Narrow metrics, unsupported): PE31-J2-171.00      Metric: 10
      IS Neighbor (Narrow metrics, unsupported): Ribbon-32.00        Metric: 10
      IS Neighbor          : h49-N540-24Q8L2DD.00 Metric: 10
        IPv4 Neighbor Address: 20.57.149.149
        IPv4 Interface Address: 20.57.149.57
        Adj-sid: 30149 flags: [L V B] weight: 0x0
        Application Specific Link Attributes:
          Standard applications: SR-TE
            TE default metric: 12
            Maximum link BW: 10.00 Gbps
        Application Specific Link Attributes:
          Standard applications: Flex-Algo
            Administrative group (Color): 127
            TE default metric: 12
            Min/Max unidirectional link delay: 10/10 us
      IS Neighbor          : h55-8201-24H8FH.00  Metric: 10
        IPv4 Neighbor Address: 20.57.155.155
        IPv4 Interface Address: 20.57.155.57
        Adj-sid: 30155 flags: [L V B] weight: 0x0
        Application Specific Link Attributes:
          Standard applications: SR-TE
            TE default metric: 12
            Maximum link BW: 10.00 Gbps
        Application Specific Link Attributes:
          Standard applications: Flex-Algo
            Administrative group (Color): 255
            TE default metric: 12
            Min/Max unidirectional link delay: 9/9 us
      IS Neighbor          : huawei_254_NetEngine_8000_F8.00 Metric: 10
        IPv4 Neighbor Address: 20.57.254.254
        IPv4 Interface Address: 20.57.254.57
        Adj-sid: 30254 flags: [L V B] weight: 0x0
        Application Specific Link Attributes:
          Standard applications: Flex-Algo
            Min/Max unidirectional link delay: 11/11 us
      IS Neighbor          : juniper_379_MX304.00 Metric: 10
        IPv4 Neighbor Address: 20.57.179.179
        IPv4 Interface Address: 20.57.179.57
        Adj-sid: 30179 flags: [L V B] weight: 0x0
        Application Specific Link Attributes:
          Standard applications: SR-TE
            TE default metric: 12
            Maximum link BW: 100.00 Gbps
        Application Specific Link Attributes:
          Standard applications: Flex-Algo
            TE default metric: 12
            Min/Max unidirectional link delay: 11/11 us
      IS Neighbor          : PE32-J2-172.00      Metric: 10
        IPv4 Neighbor Address: 20.57.172.172
        IPv4 Interface Address: 20.57.172.57
        Adj-sid: 30172 flags: [L V B] weight: 0x0
        Application Specific Link Attributes:
          Standard applications: Flex-Algo
            Min/Max unidirectional link delay: 11/11 us
      IS Neighbor          : PE31-J2-171.00      Metric: 10
        IPv4 Neighbor Address: 20.57.171.171
        IPv4 Interface Address: 20.57.171.57
        Adj-sid: 30171 flags: [L V B] weight: 0x0
        Application Specific Link Attributes:
          Standard applications: Flex-Algo
            Min/Max unidirectional link delay: 11/11 us
      IS Neighbor          : Ribbon-32.00        Metric: 10
        IPv4 Neighbor Address: 20.32.57.32
        IPv4 Interface Address: 20.32.57.57
        Adj-sid: 30032 flags: [L V B] weight: 0x0
        Application Specific Link Attributes:
          Standard applications: Flex-Algo
            Min/Max unidirectional link delay: 11/11 us
      Reachability (Narrow metrics, unsupported): 10.0.0.57/32 Metric: 0 Type: 1
      Reachability (Narrow metrics, unsupported): 20.32.57.0/24 Metric: 10 Type: 1
      Reachability (Narrow metrics, unsupported): 20.57.149.0/24 Metric: 10 Type: 1
      Reachability (Narrow metrics, unsupported): 20.57.155.0/24 Metric: 10 Type: 1
      Reachability (Narrow metrics, unsupported): 20.57.171.0/24 Metric: 10 Type: 1
      Reachability (Narrow metrics, unsupported): 20.57.172.0/24 Metric: 10 Type: 1
      Reachability (Narrow metrics, unsupported): 20.57.179.0/24 Metric: 10 Type: 1
      Reachability (Narrow metrics, unsupported): 20.57.211.0/24 Metric: 10 Type: 1
      Reachability (Narrow metrics, unsupported): 20.57.254.0/24 Metric: 10 Type: 1
      Reachability         : 10.0.0.57/32 Metric: 0 Type: 1 Up
        SR Prefix-SID: 57 Flags: [N P] Algorithm: 0
        SR Prefix-SID: 1057 Flags: [N P] Algorithm: 128
        SR Prefix-SID: 1157 Flags: [N P] Algorithm: 129
        SR Prefix-SID: 1257 Flags: [N P] Algorithm: 130
        SR Prefix-SID: 1357 Flags: [N P] Algorithm: 131
        SR Prefix-SID: 1457 Flags: [N P] Algorithm: 132
      Reachability         : 20.32.57.0/24 Metric: 10 Type: 1 Up
      Reachability         : 20.57.149.0/24 Metric: 10 Type: 1 Up
      Reachability         : 20.57.155.0/24 Metric: 10 Type: 1 Up
      Reachability         : 20.57.171.0/24 Metric: 10 Type: 1 Up
      Reachability         : 20.57.172.0/24 Metric: 10 Type: 1 Up
      Reachability         : 20.57.179.0/24 Metric: 10 Type: 1 Up
      Reachability         : 20.57.211.0/24 Metric: 10 Type: 1 Up
      Reachability         : 20.57.254.0/24 Metric: 10 Type: 1 Up
      Reachability          : 2002::57/128 Metric: 0 Type: 1 Up
      Router Capabilities: Router Id: 10.0.0.57 Flags: []
        Maximum SID depth:
          Base MPLS imposition (MSD type 1):  12
        SR Capability: Flags: [I V]
          SRGB Base: 20000 Range: 2000
        Algorithms:  0, 128, 129, 130, 131, 132
        Flex Algo: Algorithm: 128 Metric: Min Unidirectional Delay Metric (1) Calc: SPF (0) Prio: 255
          Flags: [M] 0x80
        Flex Algo: Algorithm: 129 Metric: TE Metric (2) Calc: SPF (0) Prio: 100
          Flags: [M] 0x80
        Flex Algo: Algorithm: 130 Metric: IGP Metric (0) Calc: SPF (0) Prio: 100
          Exclude admin groups: 1
          Flags: [M] 0x80
        Flex Algo: Algorithm: 131 Metric: IGP Metric (0) Calc: SPF (0) Prio: 100
          Exclude admin groups: 127
          Flags: [M] 0x80
        Flex Algo: Algorithm: 132 Metric: IGP Metric (0) Calc: SPF (0) Prio: 100
          Exclude admin groups: 255
          Flags: [M] 0x80
    PE31-J2-171.00-00           489  51511  1078    413 L2  0100.0000.0171.00-00  <>
      LSP generation remaining wait time: 0 ms
      Time remaining until refresh: 778 s
      NLPID: 0xCC(IPv4)
      Hostname: PE31-J2-171
      Area addresses: 49.0000
      Interface address: 20.32.171.171
      Interface address: 20.57.171.171
      Interface address: 20.171.172.171
      Interface address: 10.0.0.171
      IS Neighbor          : Ribbon-32.00        Metric: 10
        IPv4 Neighbor Address: 20.32.171.32
        IPv4 Interface Address: 20.32.171.171
        Adj-sid: 362148 flags: [L V] weight: 0x0
        Application Specific Link Attributes:
          Standard applications: Flex-Algo
            TE default metric: 12
            Min/Max unidirectional link delay: 11/11 us
      IS Neighbor          : NOKIA-SR2-57.00     Metric: 10
        IPv4 Neighbor Address: 20.57.171.57
        IPv4 Interface Address: 20.57.171.171
        Adj-sid: 362147 flags: [L V] weight: 0x0
        Application Specific Link Attributes:
          Standard applications: Flex-Algo
            Administrative group (Color): 127
            TE default metric: 12
            Min/Max unidirectional link delay: 1000/1000 us
      IS Neighbor          : PE32-J2-172.00      Metric: 10
        IPv4 Neighbor Address: 20.171.172.172
        IPv4 Interface Address: 20.171.172.171
        Adj-sid: 362146 flags: [L V] weight: 0x0
        Application Specific Link Attributes:
          Standard applications: Flex-Algo
            TE default metric: 12
            Min/Max unidirectional link delay: 11/11 us
      Reachability         : 20.32.171.0/24 Metric: 10 Type: 1 Up
      Reachability         : 20.57.171.0/24 Metric: 10 Type: 1 Up
      Reachability         : 20.171.172.0/24 Metric: 10 Type: 1 Up
      Reachability         : 10.0.0.171/32 Metric: 0 Type: 1 Up
        SR Prefix-SID: 171 Flags: [N] Algorithm: 0
        SR Prefix-SID: 1171 Flags: [N] Algorithm: 128
        SR Prefix-SID: 1271 Flags: [N] Algorithm: 129
        SR Prefix-SID: 1371 Flags: [N] Algorithm: 130
        SR Prefix-SID: 1471 Flags: [N] Algorithm: 131
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
          Exclude admin groups: 1
        Flex Algo: Algorithm: 129 Metric: TE Metric (2) Calc: SPF (0) Prio: 237
        Flex Algo: Algorithm: 128 Metric: Min Unidirectional Delay Metric (1) Calc: SPF (0) Prio: 237
    PE32-J2-172.00-00            14   4215   968    310 L2  0100.0000.0172.00-00  <>
      Remaining lifetime received: 1199 s Modified to: 1200 s
      NLPID: 0xCC(IPv4)
      Hostname: PE32-J2-172
      Area addresses: 49.0000
      Interface address: 20.57.172.172
      Interface address: 20.171.172.172
      Interface address: 10.0.0.172
      IS Neighbor          : NOKIA-SR2-57.00     Metric: 10
        IPv4 Neighbor Address: 20.57.172.57
        IPv4 Interface Address: 20.57.172.172
        Adj-sid: 411297 flags: [L V] weight: 0x0
        Application Specific Link Attributes:
          Standard applications: Flex-Algo
            TE default metric: 12
            Min/Max unidirectional link delay: 11/11 us
      IS Neighbor          : PE31-J2-171.00      Metric: 10
        IPv4 Neighbor Address: 20.171.172.171
        IPv4 Interface Address: 20.171.172.172
        Adj-sid: 411296 flags: [L V] weight: 0x0
        Application Specific Link Attributes:
          Standard applications: Flex-Algo
            TE default metric: 12
            Min/Max unidirectional link delay: 11/11 us
      Reachability         : 10.0.0.172/32 Metric: 0 Type: 1 Up
        SR Prefix-SID: 172 Flags: [N] Algorithm: 0
        SR Prefix-SID: 1272 Flags: [N] Algorithm: 129
        SR Prefix-SID: 1372 Flags: [N] Algorithm: 130
        SR Prefix-SID: 1472 Flags: [N] Algorithm: 131
      Reachability         : 20.57.172.0/24 Metric: 10 Type: 1 Up
      Reachability         : 20.171.172.0/24 Metric: 10 Type: 1 Up
      Router Capabilities: Router Id: 10.0.0.172 Flags: []
        SR Local Block:
          SRLB Base: 965536 Range: 65536
        Area leader priority: 250 algorithm: 0
        Maximum SID depth:
          Base MPLS imposition (MSD type 1):  12
        SR Capability: Flags: [I]
          SRGB Base: 20000 Range: 2000
        Algorithms:  0, 129, 130, 131
        Flex Algo: Algorithm: 131 Metric: IGP Metric (0) Calc: SPF (0) Prio: 237
          Exclude admin groups: 127
        Flex Algo: Algorithm: 130 Metric: IGP Metric (0) Calc: SPF (0) Prio: 237
          Exclude admin groups: 1
        Flex Algo: Algorithm: 129 Metric: TE Metric (2) Calc: SPF (0) Prio: 237
```

## show isis flex-algo

```text

IS-IS Instance: IGP VRF: default

Algorithm     Advertised Level Metric    Selected         
------------- ---------- ----- --------- -----------------
MIN-LATENCY   yes        L2    min-delay NOKIA-SR2-57     
MIN-TE        yes        L2    TE        h49-N540-24Q8L2DD
MIN-IGP       yes        L2    default   h49-N540-24Q8L2DD
MIN-IGP-ADMIN yes        L2    default   h49-N540-24Q8L2DD

```

## show isis flex-algo path detail

```text
Flex algo paths for IPv4 address family
Topology ID: Level-2
Destination: 0010.0010.0005
Path ID: 640
Path constraints: algo MIN-LATENCY
                  metric type MIN-DELAY
Request sequence number: 6209
Response sequence number: 6209
Number of times path updated: 6202
Last updated: 0:00:02 ago
Next Hop Interface
-------- ---------

Destination: 0010.0010.0005
Path ID: 641
Path constraints: algo MIN-TE
                  metric type TE
Request sequence number: 238
Response sequence number: 238
Number of times path updated: 240
Last updated: 0:02:02 ago
Metric: 36
Next Hop     Interface   
------------ ------------
20.57.171.57 Ethernet49/1

Destination: 0010.0010.0005
Path ID: 642
Path constraints: algo MIN-IGP
                  metric type IGP
                  administrative-group exclude 1
Request sequence number: 238
Response sequence number: 238
Number of times path updated: 240
Last updated: 0:02:02 ago
Metric: 30
Next Hop     Interface   
------------ ------------
20.57.171.57 Ethernet49/1

Destination: 0010.0010.0005
Path ID: 643
Path constraints: algo MIN-IGP-ADMIN
                  metric type IGP
                  administrative-group exclude 127
Request sequence number: 222
Response sequence number: 222
Number of times path updated: 222
Last updated: 0:02:02 ago
Next Hop Interface
-------- ---------

Destination: 12502-1
Path ID: 640
Path constraints: algo MIN-LATENCY
                  metric type MIN-DELAY
Request sequence number: 6210
Response sequence number: 6210
Number of times path updated: 6203
Last updated: 0:00:02 ago
Next Hop Interface
-------- ---------

Destination: 12502-1
Path ID: 641
Path constraints: algo MIN-TE
                  metric type TE
Request sequence number: 238
Response sequence number: 238
Number of times path updated: 240
Last updated: 0:02:02 ago
Metric: 36
Next Hop     Interface   
------------ ------------
20.57.171.57 Ethernet49/1

Destination: 12502-1
Path ID: 642
Path constraints: algo MIN-IGP
                  metric type IGP
                  administrative-group exclude 1
Request sequence number: 238
Response sequence number: 238
Number of times path updated: 240
Last updated: 0:02:02 ago
Metric: 30
Next Hop     Interface   
------------ ------------
20.57.171.57 Ethernet49/1

Destination: 12502-1
Path ID: 643
Path constraints: algo MIN-IGP-ADMIN
                  metric type IGP
                  administrative-group exclude 127
Request sequence number: 222
Response sequence number: 222
Number of times path updated: 224
Last updated: 0:02:02 ago
Metric: 50
Next Hop       Interface 
-------------- ----------
20.171.172.172 Ethernet47

Destination: NOKIA-SR2-57
Path ID: 640
Path constraints: algo MIN-LATENCY
                  metric type MIN-DELAY
Request sequence number: 6209
Response sequence number: 6209
Number of times path updated: 6205
Last updated: 0:00:02 ago
Metric: 22
Next Hop     Interface
------------ ---------
20.32.171.32 Ethernet7

Destination: NOKIA-SR2-57
Path ID: 641
Path constraints: algo MIN-TE
                  metric type TE
Request sequence number: 238
Response sequence number: 238
Number of times path updated: 238
Last updated: 0:02:02 ago
Metric: 12
Next Hop     Interface   
------------ ------------
20.57.171.57 Ethernet49/1

Destination: NOKIA-SR2-57
Path ID: 642
Path constraints: algo MIN-IGP
                  metric type IGP
                  administrative-group exclude 1
Request sequence number: 238
Response sequence number: 238
Number of times path updated: 238
Last updated: 0:02:02 ago
Metric: 10
Next Hop     Interface   
------------ ------------
20.57.171.57 Ethernet49/1

Destination: NOKIA-SR2-57
Path ID: 643
Path constraints: algo MIN-IGP-ADMIN
                  metric type IGP
                  administrative-group exclude 127
Request sequence number: 222
Response sequence number: 222
Number of times path updated: 225
Last updated: 0:02:02 ago
Metric: 20
Next Hop       Interface 
-------------- ----------
20.171.172.172 Ethernet47

Destination: PE31-J2-171
Path ID: 640
Path constraints: algo MIN-LATENCY
                  metric type MIN-DELAY
Request sequence number: 6214
Response sequence number: 6214
Number of times path updated: 6207
Last updated: 0:00:02 ago
Next Hop Interface
-------- ---------

Destination: PE31-J2-171
Path ID: 641
Path constraints: algo MIN-TE
                  metric type TE
Request sequence number: 243
Response sequence number: 243
Number of times path updated: 237
Last updated: 0:02:02 ago
Next Hop Interface
-------- ---------

Destination: PE31-J2-171
Path ID: 642
Path constraints: algo MIN-IGP
                  metric type IGP
                  administrative-group exclude 1
Request sequence number: 243
Response sequence number: 243
Number of times path updated: 237
Last updated: 0:02:02 ago
Next Hop Interface
-------- ---------

Destination: PE31-J2-171
Path ID: 643
Path constraints: algo MIN-IGP-ADMIN
                  metric type IGP
                  administrative-group exclude 127
Request sequence number: 227
Response sequence number: 227
Number of times path updated: 226
Last updated: 0:02:02 ago
Next Hop Interface
-------- ---------

Destination: PE32-J2-172
Path ID: 641
Path constraints: algo MIN-TE
                  metric type TE
Request sequence number: 41
Response sequence number: 41
Number of times path updated: 38
Last updated: 0:02:02 ago
Metric: 12
Next Hop       Interface 
-------------- ----------
20.171.172.172 Ethernet47

Destination: PE32-J2-172
Path ID: 642
Path constraints: algo MIN-IGP
                  metric type IGP
                  administrative-group exclude 1
Request sequence number: 41
Response sequence number: 41
Number of times path updated: 38
Last updated: 0:02:02 ago
Metric: 10
Next Hop       Interface 
-------------- ----------
20.171.172.172 Ethernet47

Destination: PE32-J2-172
Path ID: 643
Path constraints: algo MIN-IGP-ADMIN
                  metric type IGP
                  administrative-group exclude 127
Request sequence number: 34
Response sequence number: 34
Number of times path updated: 34
Last updated: 0:02:02 ago
Metric: 10
Next Hop       Interface 
-------------- ----------
20.171.172.172 Ethernet47

Destination: Ribbon-32
Path ID: 640
Path constraints: algo MIN-LATENCY
                  metric type MIN-DELAY
Request sequence number: 38
Response sequence number: 38
Number of times path updated: 37
Last updated: 0:00:02 ago
Metric: 11
Next Hop     Interface
------------ ---------
20.32.171.32 Ethernet7

Destination: h3c_19_CR16010E-F
Path ID: 640
Path constraints: algo MIN-LATENCY
                  metric type MIN-DELAY
Request sequence number: 6210
Response sequence number: 6210
Number of times path updated: 6203
Last updated: 0:00:02 ago
Next Hop Interface
-------- ---------

Destination: h3c_19_CR16010E-F
Path ID: 641
Path constraints: algo MIN-TE
                  metric type TE
Request sequence number: 238
Response sequence number: 238
Number of times path updated: 240
Last updated: 0:02:02 ago
Metric: 36
Next Hop     Interface   
------------ ------------
20.57.171.57 Ethernet49/1

Destination: h3c_19_CR16010E-F
Path ID: 642
Path constraints: algo MIN-IGP
                  metric type IGP
                  administrative-group exclude 1
Request sequence number: 238
Response sequence number: 238
Number of times path updated: 240
Last updated: 0:02:02 ago
Metric: 30
Next Hop     Interface   
------------ ------------
20.57.171.57 Ethernet49/1

Destination: h3c_19_CR16010E-F
Path ID: 643
Path constraints: algo MIN-IGP-ADMIN
                  metric type IGP
                  administrative-group exclude 127
Request sequence number: 222
Response sequence number: 222
Number of times path updated: 224
Last updated: 0:02:02 ago
Metric: 50
Next Hop       Interface 
-------------- ----------
20.171.172.172 Ethernet47

Destination: h49-N540-24Q8L2DD
Path ID: 641
Path constraints: algo MIN-TE
                  metric type TE
Request sequence number: 238
Response sequence number: 238
Number of times path updated: 240
Last updated: 0:02:02 ago
Metric: 24
Next Hop     Interface   
------------ ------------
20.57.171.57 Ethernet49/1

Destination: h49-N540-24Q8L2DD
Path ID: 642
Path constraints: algo MIN-IGP
                  metric type IGP
                  administrative-group exclude 1
Request sequence number: 238
Response sequence number: 238
Number of times path updated: 240
Last updated: 0:02:02 ago
Metric: 20
Next Hop     Interface   
------------ ------------
20.57.171.57 Ethernet49/1

Destination: h55-8201-24H8FH
Path ID: 640
Path constraints: algo MIN-LATENCY
                  metric type MIN-DELAY
Request sequence number: 6210
Response sequence number: 6210
Number of times path updated: 6206
Last updated: 0:00:02 ago
Metric: 31
Next Hop     Interface
------------ ---------
20.32.171.32 Ethernet7

Destination: h55-8201-24H8FH
Path ID: 641
Path constraints: algo MIN-TE
                  metric type TE
Request sequence number: 238
Response sequence number: 238
Number of times path updated: 236
Last updated: 0:02:02 ago
Metric: 24
Next Hop     Interface   
------------ ------------
20.57.171.57 Ethernet49/1

Destination: h55-8201-24H8FH
Path ID: 642
Path constraints: algo MIN-IGP
                  metric type IGP
                  administrative-group exclude 1
Request sequence number: 238
Response sequence number: 238
Number of times path updated: 236
Last updated: 0:02:02 ago
Metric: 20
Next Hop     Interface   
------------ ------------
20.57.171.57 Ethernet49/1

Destination: h55-8201-24H8FH
Path ID: 643
Path constraints: algo MIN-IGP-ADMIN
                  metric type IGP
                  administrative-group exclude 127
Request sequence number: 222
Response sequence number: 222
Number of times path updated: 224
Last updated: 0:02:02 ago
Metric: 30
Next Hop       Interface 
-------------- ----------
20.171.172.172 Ethernet47

Destination: juniper_379_MX304
Path ID: 640
Path constraints: algo MIN-LATENCY
                  metric type MIN-DELAY
Request sequence number: 660
Response sequence number: 660
Number of times path updated: 659
Last updated: 0:00:02 ago
Metric: 33
Next Hop     Interface
------------ ---------
20.32.171.32 Ethernet7

Destination: juniper_379_MX304
Path ID: 641
Path constraints: algo MIN-TE
                  metric type TE
Request sequence number: 76
Response sequence number: 76
Number of times path updated: 75
Last updated: 0:02:02 ago
Metric: 24
Next Hop     Interface   
------------ ------------
20.57.171.57 Ethernet49/1

Destination: juniper_379_MX304
Path ID: 642
Path constraints: algo MIN-IGP
                  metric type IGP
                  administrative-group exclude 1
Request sequence number: 76
Response sequence number: 76
Number of times path updated: 75
Last updated: 0:02:02 ago
Metric: 20
Next Hop     Interface   
------------ ------------
20.57.171.57 Ethernet49/1

```

## show isis segment-routing tunnel

```text
  Index     Endpoint          Next Hop/Tunnel Index      Interface    Labels   
--------- ----------------- -------------------------- -------------- ---------
  1         10.0.0.83/32      TI-LFA (20)                -            [ 20083 ]
  2         10.0.1.49/32      TI-LFA (20)                -            [ 20349 ]
  3         10.0.0.19/32      TI-LFA (20)                -            [ 20019 ]
  4         10.0.1.55/32      TI-LFA (20)                -            [ 20355 ]
  5         10.0.0.24/32      TI-LFA (20)                -            [ 20024 ]
  6         10.0.0.57/32      TI-LFA (20)                -            [ 20057 ]
  7         10.0.0.179/32     TI-LFA (20)                -            [ 20379 ]
  8         10.0.0.5/32       TI-LFA (20)                -            [ 20005 ]
  9         10.0.0.32/32      TI-LFA (1)                 -            [ 3 ]    
  10        10.0.0.172/32     TI-LFA (0)                 -            [ 3 ]    

```

## show isis segment-routing prefix-segments

```text

System ID: PE31-J2-171			Instance: 'IGP'
SR supported Data-plane: MPLS			SR Router ID: 10.0.0.171

Node: 56     Proxy-Node: 0      Prefix: 0       Total Segments: 56

Flag Descriptions: R: Re-advertised, N: Node Segment, P: no-PHP
                   E: Explicit-NULL, V: Value, L: Local
Segment status codes: * - Self originated Prefix, L1 - level 1, L2 - level 2, ! - SR-unreachable,
                      # - Some IS-IS next-hops are SR-unreachable
   Prefix                      SID   Label Type       Flags                        System ID       Level Protection  Algorithm   
   ------------------------- ----- ------- ---------- ---------------------------- --------------- ----- ----------- -------------
   10.0.0.5/32                   5   20005 Node       R:0 N:1 P:0 E:0 V:0 L:0      0010.0010.0005  L2    node        SPF         
   10.0.0.5/32                1005   21005 Node       R:0 N:1 P:0 E:0 V:0 L:0      0010.0010.0005  L2    unprotected MIN-LATENCY 
   10.0.0.5/32                1105   21105 Node       R:0 N:1 P:0 E:0 V:0 L:0      0010.0010.0005  L2    node        MIN-TE      
   10.0.0.5/32                1205   21205 Node       R:0 N:1 P:0 E:0 V:0 L:0      0010.0010.0005  L2    node        MIN-IGP     
   10.0.0.5/32                1305   21305 Node       R:0 N:1 P:0 E:0 V:0 L:0      0010.0010.0005  L2    unprotected MIN-IGP-ADMIN
   10.0.0.19/32                 19   20019 Node       R:0 N:1 P:0 E:0 V:0 L:0      h3c_19_CR16010E-F L2    node        SPF         
   10.0.0.19/32               1019   21019 Node       R:0 N:1 P:0 E:0 V:0 L:0      h3c_19_CR16010E-F L2    unprotected MIN-LATENCY 
   10.0.0.19/32               1119   21119 Node       R:0 N:1 P:0 E:0 V:0 L:0      h3c_19_CR16010E-F L2    node        MIN-TE      
   10.0.0.19/32               1219   21219 Node       R:0 N:1 P:0 E:0 V:0 L:0      h3c_19_CR16010E-F L2    node        MIN-IGP     
   10.0.0.19/32               1319   21319 Node       R:0 N:1 P:0 E:0 V:0 L:0      h3c_19_CR16010E-F L2    node        MIN-IGP-ADMIN
   10.0.0.24/32                 24   20024 Node       R:0 N:1 P:1 E:0 V:0 L:0      12502-1         L2    node        SPF         
   10.0.0.24/32               1024   21024 Node       R:0 N:1 P:1 E:0 V:0 L:0      12502-1         L2    unprotected MIN-LATENCY 
   10.0.0.24/32               1124   21124 Node       R:0 N:1 P:1 E:0 V:0 L:0      12502-1         L2    node        MIN-TE      
   10.0.0.24/32               1224   21224 Node       R:0 N:1 P:1 E:0 V:0 L:0      12502-1         L2    node        MIN-IGP     
   10.0.0.24/32               1324   21324 Node       R:0 N:1 P:1 E:0 V:0 L:0      12502-1         L2    node        MIN-IGP-ADMIN
   10.0.0.32/32                 32   20032 Node       R:0 N:1 P:0 E:0 V:0 L:0      Ribbon-32       L2    node        SPF         
   10.0.0.32/32               1032   21032 Node       R:0 N:1 P:0 E:0 V:0 L:0      Ribbon-32       L2    node        MIN-LATENCY 
   10.0.0.57/32                 57   20057 Node       R:0 N:1 P:1 E:0 V:0 L:0      NOKIA-SR2-57    L2    node        SPF         
   10.0.0.57/32               1057   21057 Node       R:0 N:1 P:1 E:0 V:0 L:0      NOKIA-SR2-57    L2    node        MIN-LATENCY 
   10.0.0.57/32               1157   21157 Node       R:0 N:1 P:1 E:0 V:0 L:0      NOKIA-SR2-57    L2    node        MIN-TE      
   10.0.0.57/32               1257   21257 Node       R:0 N:1 P:1 E:0 V:0 L:0      NOKIA-SR2-57    L2    node        MIN-IGP     
   10.0.0.57/32               1357   21357 Node       R:0 N:1 P:1 E:0 V:0 L:0      NOKIA-SR2-57    L2    node        MIN-IGP-ADMIN
   10.0.0.57/32               1457   21457 Node       R:0 N:1 P:1 E:0 V:0 L:0      NOKIA-SR2-57    L2    unprotected 132         
   10.0.0.83/32                 83   20083 Node       R:0 N:1 P:0 E:0 V:0 L:0      eantc-jcnr2     L2    node        SPF         
*  10.0.0.171/32               171   20171 Node       R:0 N:1 P:0 E:0 V:0 L:0      PE31-J2-171     L2    unprotected SPF         
*  10.0.0.171/32              1171   21171 Node       R:0 N:1 P:0 E:0 V:0 L:0      PE31-J2-171     L2    unprotected MIN-LATENCY 
*  10.0.0.171/32              1271   21271 Node       R:0 N:1 P:0 E:0 V:0 L:0      PE31-J2-171     L2    unprotected MIN-TE      
*  10.0.0.171/32              1371   21371 Node       R:0 N:1 P:0 E:0 V:0 L:0      PE31-J2-171     L2    unprotected MIN-IGP     
*  10.0.0.171/32              1471   21471 Node       R:0 N:1 P:0 E:0 V:0 L:0      PE31-J2-171     L2    unprotected MIN-IGP-ADMIN
   10.0.0.172/32               172   20172 Node       R:0 N:1 P:0 E:0 V:0 L:0      PE32-J2-172     L2    node        SPF         
   10.0.0.172/32              1272   21272 Node       R:0 N:1 P:0 E:0 V:0 L:0      PE32-J2-172     L2    node        MIN-TE      
   10.0.0.172/32              1372   21372 Node       R:0 N:1 P:0 E:0 V:0 L:0      PE32-J2-172     L2    node        MIN-IGP     
   10.0.0.172/32              1472   21472 Node       R:0 N:1 P:0 E:0 V:0 L:0      PE32-J2-172     L2    node        MIN-IGP-ADMIN
   10.0.0.179/32               379   20379 Node       R:0 N:1 P:0 E:0 V:0 L:0      juniper_379_MX304 L2    node        SPF         
   10.0.0.179/32              1179   21179 Node       R:0 N:1 P:0 E:0 V:0 L:0      juniper_379_MX304 L2    node        MIN-LATENCY 
   10.0.0.179/32              1279   21279 Node       R:0 N:1 P:0 E:0 V:0 L:0      juniper_379_MX304 L2    node        MIN-TE      
   10.0.0.179/32              1379   21379 Node       R:0 N:1 P:0 E:0 V:0 L:0      juniper_379_MX304 L2    node        MIN-IGP     
   10.0.0.179/32               479   20479 Node       R:0 N:1 P:0 E:0 V:0 L:0      juniper_379_MX304 L2    unprotected 140         
   10.0.0.179/32               579   20579 Node       R:0 N:1 P:0 E:0 V:0 L:0      juniper_379_MX304 L2    unprotected 141         
   10.0.0.179/32               679   20679 Node       R:0 N:1 P:0 E:0 V:0 L:0      juniper_379_MX304 L2    unprotected 142         
   10.0.1.49/32                349   20349 Node       R:0 N:1 P:0 E:0 V:0 L:0      h49-N540-24Q8L2DD L2    node        SPF         
   10.0.1.49/32               1449   21449 Node       R:0 N:1 P:0 E:0 V:0 L:0      h49-N540-24Q8L2DD L2    node        MIN-TE      
   10.0.1.49/32               1649   21649 Node       R:0 N:1 P:0 E:0 V:0 L:0      h49-N540-24Q8L2DD L2    node        MIN-IGP     
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

 I L2     10.0.0.5/32 [115/40]
           via 20.57.171.57, Ethernet49/1
 I L2     10.0.0.19/32 [115/30]
           via 20.57.171.57, Ethernet49/1
 I L2     10.0.0.24/32 [115/30]
           via 20.57.171.57, Ethernet49/1
 I L2     10.0.0.32/32 [115/10]
           via 20.32.171.32, Ethernet7
 I L2     10.0.0.57/32 [115/10]
           via 20.57.171.57, Ethernet49/1
 I L2     10.0.0.83/32 [115/30]
           via 20.57.171.57, Ethernet49/1
 C        10.0.0.171/32
           directly connected, Loopback0
 I L2     10.0.0.172/32 [115/10]
           via 20.171.172.172, Ethernet47
 I L2     10.0.0.179/32 [115/20]
           via 20.57.171.57, Ethernet49/1
 I L2     10.0.0.254/32 [115/20]
           via 20.57.171.57, Ethernet49/1
 I L2     10.0.1.49/32 [115/20]
           via 20.57.171.57, Ethernet49/1
 I L2     10.0.1.55/32 [115/20]
           via 20.57.171.57, Ethernet49/1
 I L2     20.5.149.0/24 [115/30]
           via 20.57.171.57, Ethernet49/1
 I L2     20.19.149.0/24 [115/30]
           via 20.57.171.57, Ethernet49/1
 I L2     20.24.149.0/24 [115/30]
           via 20.57.171.57, Ethernet49/1
 I L2     20.32.57.0/24 [115/20]
           via 20.32.171.32, Ethernet7
           via 20.57.171.57, Ethernet49/1
 I L2     20.32.149.0/24 [115/20]
           via 20.32.171.32, Ethernet7
 C        20.32.171.0/24
           directly connected, Ethernet7
 I L2     20.32.211.0/24 [115/20]
           via 20.32.171.32, Ethernet7
 I L2     20.47.149.0/24 [115/30]
           via 20.57.171.57, Ethernet49/1
 I L2     20.57.149.0/24 [115/20]
           via 20.57.171.57, Ethernet49/1
 I L2     20.57.155.0/24 [115/20]
           via 20.57.171.57, Ethernet49/1
 C        20.57.171.0/24
           directly connected, Ethernet49/1
 I L2     20.57.172.0/24 [115/20]
           via 20.171.172.172, Ethernet47
           via 20.57.171.57, Ethernet49/1
 I L2     20.57.179.0/24 [115/20]
           via 20.57.171.57, Ethernet49/1
 I L2     20.57.211.0/24 [115/20]
           via 20.57.171.57, Ethernet49/1
 I L2     20.57.254.0/24 [115/20]
           via 20.57.171.57, Ethernet49/1
 I L2     20.83.149.0/24 [115/30]
           via 20.57.171.57, Ethernet49/1
 I L2     20.111.149.0/24 [115/30]
           via 20.57.171.57, Ethernet49/1
 I L2     20.149.155.0/24 [115/30]
           via 20.57.171.57, Ethernet49/1
 I L2     20.149.254.0/24 [115/30]
           via 20.57.171.57, Ethernet49/1
 I L2     20.155.179.0/24 [115/30]
           via 20.57.171.57, Ethernet49/1
 C        20.171.172.0/24
           directly connected, Ethernet47
 I L2     30.155.179.0/24 [115/30]
           via 20.57.171.57, Ethernet49/1
 I L2     192.168.20.0/23 [115/30]
           via 20.57.171.57, Ethernet49/1
 I L2     192.168.0.0/19 [115/30]
           via 20.57.171.57, Ethernet49/1

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

 I L2     10.0.0.5/32 [115/40]
           via 20.57.171.57, Ethernet49/1
 I L2     10.0.0.19/32 [115/30]
           via 20.57.171.57, Ethernet49/1
 I L2     10.0.0.24/32 [115/30]
           via 20.57.171.57, Ethernet49/1
 I L2     10.0.0.32/32 [115/10]
           via 20.32.171.32, Ethernet7
 I L2     10.0.0.57/32 [115/10]
           via 20.57.171.57, Ethernet49/1
 I L2     10.0.0.83/32 [115/30]
           via 20.57.171.57, Ethernet49/1
 C        10.0.0.171/32
           directly connected, Loopback0
 I L2     10.0.0.172/32 [115/10]
           via 20.171.172.172, Ethernet47
 I L2     10.0.0.179/32 [115/20]
           via 20.57.171.57, Ethernet49/1
 I L2     10.0.0.254/32 [115/20]
           via 20.57.171.57, Ethernet49/1
 I L2     10.0.1.49/32 [115/20]
           via 20.57.171.57, Ethernet49/1
 I L2     10.0.1.55/32 [115/20]
           via 20.57.171.57, Ethernet49/1
 I L2     20.5.149.0/24 [115/30]
           via 20.57.171.57, Ethernet49/1
 I L2     20.19.149.0/24 [115/30]
           via 20.57.171.57, Ethernet49/1
 I L2     20.24.149.0/24 [115/30]
           via 20.57.171.57, Ethernet49/1
 I L2     20.32.57.0/24 [115/20]
           via 20.32.171.32, Ethernet7
           via 20.57.171.57, Ethernet49/1
 I L2     20.32.149.0/24 [115/20]
           via 20.32.171.32, Ethernet7
 C        20.32.171.0/24
           directly connected, Ethernet7
 I L2     20.32.211.0/24 [115/20]
           via 20.32.171.32, Ethernet7
 I L2     20.47.149.0/24 [115/30]
           via 20.57.171.57, Ethernet49/1
 I L2     20.57.149.0/24 [115/20]
           via 20.57.171.57, Ethernet49/1
 I L2     20.57.155.0/24 [115/20]
           via 20.57.171.57, Ethernet49/1
 C        20.57.171.0/24
           directly connected, Ethernet49/1
 I L2     20.57.172.0/24 [115/20]
           via 20.171.172.172, Ethernet47
           via 20.57.171.57, Ethernet49/1
 I L2     20.57.179.0/24 [115/20]
           via 20.57.171.57, Ethernet49/1
 I L2     20.57.211.0/24 [115/20]
           via 20.57.171.57, Ethernet49/1
 I L2     20.57.254.0/24 [115/20]
           via 20.57.171.57, Ethernet49/1
 I L2     20.83.149.0/24 [115/30]
           via 20.57.171.57, Ethernet49/1
 I L2     20.111.149.0/24 [115/30]
           via 20.57.171.57, Ethernet49/1
 I L2     20.149.155.0/24 [115/30]
           via 20.57.171.57, Ethernet49/1
 I L2     20.149.254.0/24 [115/30]
           via 20.57.171.57, Ethernet49/1
 I L2     20.155.179.0/24 [115/30]
           via 20.57.171.57, Ethernet49/1
 C        20.171.172.0/24
           directly connected, Ethernet47
 I L2     30.155.179.0/24 [115/30]
           via 20.57.171.57, Ethernet49/1
 I L2     192.168.20.0/23 [115/30]
           via 20.57.171.57, Ethernet49/1
 I L2     192.168.0.0/19 [115/30]
           via 20.57.171.57, Ethernet49/1


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

 B I      20.5.111.0/24 [200/0]
           via 10.0.0.5/32, IS-IS SR tunnel index 8, label 62011
              via TI-LFA tunnel index 20, label 20005
                 via 20.57.171.57, Ethernet49/1, label imp-null(3)
                 backup via 20.171.172.172, Ethernet47, label imp-null(3)
 B I      20.19.111.0/24 [200/0]
           via 10.0.0.19/32, IS-IS SR tunnel index 3, label 1271
              via TI-LFA tunnel index 20, label 20019
                 via 20.57.171.57, Ethernet49/1, label imp-null(3)
                 backup via 20.171.172.172, Ethernet47, label imp-null(3)
 B I      20.24.111.0/24 [200/0]
           via 10.0.0.24/32, IS-IS SR tunnel index 5, label 56502
              via TI-LFA tunnel index 20, label 20024
                 via 20.57.171.57, Ethernet49/1, label imp-null(3)
                 backup via 20.171.172.172, Ethernet47, label imp-null(3)
 B I      20.32.111.0/24 [200/0]
           via 10.0.0.32/32, algorithm MIN-LATENCY, IS-IS FlexAlgo tunnel index 24, label 756643
              via TI-LFA tunnel index 6, label imp-null(3)
                 via 20.32.171.32, Ethernet7, label imp-null(3)
                 backup via 20.57.171.57, Ethernet49/1, label 21032
 B I      20.57.111.0/24 [200/0]
           via 10.0.0.57/32, algorithm MIN-LATENCY, IS-IS FlexAlgo tunnel index 22, label 524286
              via TI-LFA tunnel index 5, label 21057
                 via 20.32.171.32, Ethernet7, label imp-null(3)
                 backup via 20.57.171.57, Ethernet49/1, label imp-null(3)
 B I      20.111.155.0/24 [200/0]
           via 10.0.1.55/32, algorithm MIN-LATENCY, IS-IS FlexAlgo tunnel index 21, label 24009
              via TI-LFA tunnel index 5, label 21355
                 via 20.32.171.32, Ethernet7, label imp-null(3)
                 backup via 20.57.171.57, Ethernet49/1, label imp-null(3)
 C        20.111.171.0/24
           directly connected, Ethernet5.128
 B I      20.111.179.0/24 [200/0]
           via 10.0.0.179/32, algorithm MIN-LATENCY, IS-IS FlexAlgo tunnel index 23, label 16
              via TI-LFA tunnel index 5, label 21179
                 via 20.32.171.32, Ethernet7, label imp-null(3)
                 backup via 20.57.171.57, Ethernet49/1, label imp-null(3)


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

 B I      20.5.111.0/24 [200/0]
           via 10.0.0.5/32, algorithm MIN-IGP, IS-IS FlexAlgo tunnel index 9, label 62014
              via TI-LFA tunnel index 20, label 21205
                 via 20.57.171.57, Ethernet49/1, label imp-null(3)
                 backup via 20.171.172.172, Ethernet47, label imp-null(3)
 B I      20.19.111.0/24 [200/0]
           via 10.0.0.19/32, algorithm MIN-IGP, IS-IS FlexAlgo tunnel index 14, label 1269
              via TI-LFA tunnel index 20, label 21219
                 via 20.57.171.57, Ethernet49/1, label imp-null(3)
                 backup via 20.171.172.172, Ethernet47, label imp-null(3)
 B I      20.24.111.0/24 [200/0]
           via 10.0.0.24/32, algorithm MIN-IGP, IS-IS FlexAlgo tunnel index 13, label 56500
              via TI-LFA tunnel index 20, label 21224
                 via 20.57.171.57, Ethernet49/1, label imp-null(3)
                 backup via 20.171.172.172, Ethernet47, label imp-null(3)
 B I      20.32.111.0/24 [200/0]
           via 10.0.0.32/32, IS-IS SR tunnel index 9, label 756645
              via TI-LFA tunnel index 1, label imp-null(3)
                 via 20.32.171.32, Ethernet7, label imp-null(3)
                 backup via 20.57.171.57, Ethernet49/1, label 20032
 B I      20.57.111.0/24 [200/0]
           via 10.0.0.57/32, algorithm MIN-IGP, IS-IS FlexAlgo tunnel index 4, label 524283
              via TI-LFA tunnel index 20, label 21257
                 via 20.57.171.57, Ethernet49/1, label imp-null(3)
                 backup via 20.171.172.172, Ethernet47, label imp-null(3)
 B I      20.111.155.0/24 [200/0]
           via 10.0.1.55/32, algorithm MIN-IGP, IS-IS FlexAlgo tunnel index 2, label 24012
              via TI-LFA tunnel index 20, label 21555
                 via 20.57.171.57, Ethernet49/1, label imp-null(3)
                 backup via 20.171.172.172, Ethernet47, label imp-null(3)
 C        20.111.171.0/24
           directly connected, Ethernet5.130
 B I      20.111.179.0/24 [200/0]
           via 10.0.0.179/32, algorithm MIN-IGP, IS-IS FlexAlgo tunnel index 12, label 18
              via TI-LFA tunnel index 20, label 21379
                 via 20.57.171.57, Ethernet49/1, label imp-null(3)
                 backup via 20.171.172.172, Ethernet47, label imp-null(3)
 B I      55.55.55.130/32 [200/0]
           via 10.0.1.55/32, algorithm MIN-IGP, IS-IS FlexAlgo tunnel index 2, label 24012
              via TI-LFA tunnel index 20, label 21555
                 via 20.57.171.57, Ethernet49/1, label imp-null(3)
                 backup via 20.171.172.172, Ethernet47, label imp-null(3)


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

 B I      20.19.111.0/24 [200/0]
           via 10.0.0.19/32, algorithm MIN-IGP-ADMIN, IS-IS FlexAlgo tunnel index 17, label 1268
              via 20.171.172.172, Ethernet47, label 21319
 B I      20.24.111.0/24 [200/0]
           via 10.0.0.24/32, IS-IS SR tunnel index 5, label 56499
              via TI-LFA tunnel index 20, label 20024
                 via 20.57.171.57, Ethernet49/1, label imp-null(3)
                 backup via 20.171.172.172, Ethernet47, label imp-null(3)
 B I      20.57.111.0/24 [200/0]
           via 10.0.0.57/32, algorithm MIN-IGP-ADMIN, IS-IS FlexAlgo tunnel index 18, label 524282
              via 20.171.172.172, Ethernet47, label 21357
 B I      20.111.155.0/24 [200/0]
           via 10.0.1.55/32, algorithm MIN-IGP-ADMIN, IS-IS FlexAlgo tunnel index 16, label 24011
              via 20.171.172.172, Ethernet47, label 21655
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

 B I      20.5.111.0/24 [200/0]
           via 10.0.0.5/32, algorithm MIN-TE, IS-IS FlexAlgo tunnel index 7, label 62012
              via TI-LFA tunnel index 20, label 21105
                 via 20.57.171.57, Ethernet49/1, label imp-null(3)
                 backup via 20.171.172.172, Ethernet47, label imp-null(3)
 B I      20.19.111.0/24 [200/0]
           via 10.0.0.19/32, algorithm MIN-TE, IS-IS FlexAlgo tunnel index 8, label 1270
              via TI-LFA tunnel index 20, label 21119
                 via 20.57.171.57, Ethernet49/1, label imp-null(3)
                 backup via 20.171.172.172, Ethernet47, label imp-null(3)
 B I      20.24.111.0/24 [200/0]
           via 10.0.0.24/32, algorithm MIN-TE, IS-IS FlexAlgo tunnel index 6, label 56501
              via TI-LFA tunnel index 20, label 21124
                 via 20.57.171.57, Ethernet49/1, label imp-null(3)
                 backup via 20.171.172.172, Ethernet47, label imp-null(3)
 B I      20.32.111.0/24 [200/0]
           via 10.0.0.32/32, IS-IS SR tunnel index 9, label 756644
              via TI-LFA tunnel index 1, label imp-null(3)
                 via 20.32.171.32, Ethernet7, label imp-null(3)
                 backup via 20.57.171.57, Ethernet49/1, label 20032
 B I      20.57.111.0/24 [200/0]
           via 10.0.0.57/32, algorithm MIN-TE, IS-IS FlexAlgo tunnel index 5, label 524284
              via TI-LFA tunnel index 20, label 21157
                 via 20.57.171.57, Ethernet49/1, label imp-null(3)
                 backup via 20.171.172.172, Ethernet47, label imp-null(3)
 B I      20.111.155.0/24 [200/0]
           via 10.0.1.55/32, algorithm MIN-TE, IS-IS FlexAlgo tunnel index 11, label 24010
              via TI-LFA tunnel index 20, label 21455
                 via 20.57.171.57, Ethernet49/1, label imp-null(3)
                 backup via 20.171.172.172, Ethernet47, label imp-null(3)
 C        20.111.171.0/24
           directly connected, Ethernet5.129
 B I      20.111.179.0/24 [200/0]
           via 10.0.0.179/32, algorithm MIN-TE, IS-IS FlexAlgo tunnel index 3, label 17
              via TI-LFA tunnel index 20, label 21279
                 via 20.57.171.57, Ethernet49/1, label imp-null(3)
                 backup via 20.171.172.172, Ethernet47, label imp-null(3)


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


! IPv6 routing not enabled
```

## show mpls route

```text
MPLS forwarding table (Label [metric] Vias) - 42 routes 
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
                  via TI-LFA tunnel index 20
                    via 20.57.171.57, Ethernet49/1, label imp-null(3)
                    backup via 20.171.172.172, Ethernet47, label imp-null(3)
 20019   A[1]
                via M, ::, forward
                    EgressACL: apply
                  via TI-LFA tunnel index 20
                    via 20.57.171.57, Ethernet49/1, label imp-null(3)
                    backup via 20.171.172.172, Ethernet47, label imp-null(3)
 20024   A[1]
                via M, ::, forward
                    EgressACL: apply
                  via TI-LFA tunnel index 20
                    via 20.57.171.57, Ethernet49/1, label imp-null(3)
                    backup via 20.171.172.172, Ethernet47, label imp-null(3)
 20032   A[1]
                via M, ::, pop
                    EgressACL: apply
                  via TI-LFA tunnel index 1
                    via 20.32.171.32, Ethernet7, label imp-null(3)
                    backup via 20.57.171.57, Ethernet49/1, label 20032
 20057   A[1]
                via M, ::, forward
                    EgressACL: apply
                  via TI-LFA tunnel index 20
                    via 20.57.171.57, Ethernet49/1, label imp-null(3)
                    backup via 20.171.172.172, Ethernet47, label imp-null(3)
 20083   A[1]
                via M, ::, forward
                    EgressACL: apply
                  via TI-LFA tunnel index 20
                    via 20.57.171.57, Ethernet49/1, label imp-null(3)
                    backup via 20.171.172.172, Ethernet47, label imp-null(3)
 20172   A[1]
                via M, ::, pop
                    EgressACL: apply
                  via TI-LFA tunnel index 0
                    via 20.171.172.172, Ethernet47, label imp-null(3)
                    backup via 20.57.171.57, Ethernet49/1, label 20172
 20349   A[1]
                via M, ::, forward
                    EgressACL: apply
                  via TI-LFA tunnel index 20
                    via 20.57.171.57, Ethernet49/1, label imp-null(3)
                    backup via 20.171.172.172, Ethernet47, label imp-null(3)
 20355   A[1]
                via M, ::, forward
                    EgressACL: apply
                  via TI-LFA tunnel index 20
                    via 20.57.171.57, Ethernet49/1, label imp-null(3)
                    backup via 20.171.172.172, Ethernet47, label imp-null(3)
 20379   A[1]
                via M, ::, forward
                    EgressACL: apply
                  via TI-LFA tunnel index 20
                    via 20.57.171.57, Ethernet49/1, label imp-null(3)
                    backup via 20.171.172.172, Ethernet47, label imp-null(3)
 21032   A[1]
                via M, ::, pop
                    EgressACL: apply
                  via TI-LFA tunnel index 6
                    via 20.32.171.32, Ethernet7, label imp-null(3)
                    backup via 20.57.171.57, Ethernet49/1, label 21032
 21057   A[1]
                via M, ::, forward
                    EgressACL: apply
                  via TI-LFA tunnel index 5
                    via 20.32.171.32, Ethernet7, label imp-null(3)
                    backup via 20.57.171.57, Ethernet49/1, label imp-null(3)
 21105   A[1]
                via M, ::, forward
                    EgressACL: apply
                  via TI-LFA tunnel index 20
                    via 20.57.171.57, Ethernet49/1, label imp-null(3)
                    backup via 20.171.172.172, Ethernet47, label imp-null(3)
 21119   A[1]
                via M, ::, forward
                    EgressACL: apply
                  via TI-LFA tunnel index 20
                    via 20.57.171.57, Ethernet49/1, label imp-null(3)
                    backup via 20.171.172.172, Ethernet47, label imp-null(3)
 21124   A[1]
                via M, ::, forward
                    EgressACL: apply
                  via TI-LFA tunnel index 20
                    via 20.57.171.57, Ethernet49/1, label imp-null(3)
                    backup via 20.171.172.172, Ethernet47, label imp-null(3)
 21157   A[1]
                via M, ::, forward
                    EgressACL: apply
                  via TI-LFA tunnel index 20
                    via 20.57.171.57, Ethernet49/1, label imp-null(3)
                    backup via 20.171.172.172, Ethernet47, label imp-null(3)
 21179   A[1]
                via M, ::, forward
                    EgressACL: apply
                  via TI-LFA tunnel index 5
                    via 20.32.171.32, Ethernet7, label imp-null(3)
                    backup via 20.57.171.57, Ethernet49/1, label imp-null(3)
 21205   A[1]
                via M, ::, forward
                    EgressACL: apply
                  via TI-LFA tunnel index 20
                    via 20.57.171.57, Ethernet49/1, label imp-null(3)
                    backup via 20.171.172.172, Ethernet47, label imp-null(3)
 21219   A[1]
                via M, ::, forward
                    EgressACL: apply
                  via TI-LFA tunnel index 20
                    via 20.57.171.57, Ethernet49/1, label imp-null(3)
                    backup via 20.171.172.172, Ethernet47, label imp-null(3)
 21224   A[1]
                via M, ::, forward
                    EgressACL: apply
                  via TI-LFA tunnel index 20
                    via 20.57.171.57, Ethernet49/1, label imp-null(3)
                    backup via 20.171.172.172, Ethernet47, label imp-null(3)
 21257   A[1]
                via M, ::, forward
                    EgressACL: apply
                  via TI-LFA tunnel index 20
                    via 20.57.171.57, Ethernet49/1, label imp-null(3)
                    backup via 20.171.172.172, Ethernet47, label imp-null(3)
 21272   A[1]
                via M, pop
                    EgressACL: apply
                    20.171.172.172 Ethernet47
 21279   A[1]
                via M, ::, forward
                    EgressACL: apply
                  via TI-LFA tunnel index 20
                    via 20.57.171.57, Ethernet49/1, label imp-null(3)
                    backup via 20.171.172.172, Ethernet47, label imp-null(3)
 21319   A[1]
                via M, forward
                    EgressACL: apply
                    20.171.172.172 Ethernet47
 21324   A[1]
                via M, forward
                    EgressACL: apply
                    20.171.172.172 Ethernet47
 21355   A[1]
                via M, ::, forward
                    EgressACL: apply
                  via TI-LFA tunnel index 5
                    via 20.32.171.32, Ethernet7, label imp-null(3)
                    backup via 20.57.171.57, Ethernet49/1, label imp-null(3)
 21357   A[1]
                via M, forward
                    EgressACL: apply
                    20.171.172.172 Ethernet47
 21372   A[1]
                via M, ::, pop
                    EgressACL: apply
                  via TI-LFA tunnel index 18
                    via 20.171.172.172, Ethernet47, label imp-null(3)
                    backup via 20.57.171.57, Ethernet49/1, label 21372
 21379   A[1]
                via M, ::, forward
                    EgressACL: apply
                  via TI-LFA tunnel index 20
                    via 20.57.171.57, Ethernet49/1, label imp-null(3)
                    backup via 20.171.172.172, Ethernet47, label imp-null(3)
 21449   A[1]
                via M, ::, forward
                    EgressACL: apply
                  via TI-LFA tunnel index 20
                    via 20.57.171.57, Ethernet49/1, label imp-null(3)
                    backup via 20.171.172.172, Ethernet47, label imp-null(3)
 21455   A[1]
                via M, ::, forward
                    EgressACL: apply
                  via TI-LFA tunnel index 20
                    via 20.57.171.57, Ethernet49/1, label imp-null(3)
                    backup via 20.171.172.172, Ethernet47, label imp-null(3)
 21472   A[1]
                via M, pop
                    EgressACL: apply
                    20.171.172.172 Ethernet47
 21555   A[1]
                via M, ::, forward
                    EgressACL: apply
                  via TI-LFA tunnel index 20
                    via 20.57.171.57, Ethernet49/1, label imp-null(3)
                    backup via 20.171.172.172, Ethernet47, label imp-null(3)
 21649   A[1]
                via M, ::, forward
                    EgressACL: apply
                  via TI-LFA tunnel index 20
                    via 20.57.171.57, Ethernet49/1, label imp-null(3)
                    backup via 20.171.172.172, Ethernet47, label imp-null(3)
 21655   A[1]
                via M, forward
                    EgressACL: apply
                    20.171.172.172 Ethernet47
 362146  A[1]
                via M, 20.171.172.172, pop
                    EgressACL: apply
                    directly connected, Ethernet47
                    2c:dd:e9:96:3a:bb, vlan 1016
 362147  A[1]
                via M, 20.57.171.57, pop
                    EgressACL: apply
                    directly connected, Ethernet49/1
                    c0:14:b8:21:ca:6e, vlan 1020
 362148  A[1]
                via M, 20.32.171.32, pop
                    EgressACL: apply
                    directly connected, Ethernet7
                    30:c5:07:1f:33:0f, vlan 1021
 378528   [0]
                via I, ipv4, vrf ISIS-SR-FLEXALGO-MIN-TE
 378529   [0]
                via I, ipv4, vrf ISIS-SR-FLEXALGO-MIN-IGP-ADMIN
 378530   [0]
                via I, ipv4, vrf ISIS-SR-FLEXALGO-MIN-IGP
 378531   [0]
                via I, ipv4, vrf ISIS-SR-FLEXALGO-MIN-DELAY
```

## show mpls lfib route

```text
MPLS forwarding table (Label [metric] Vias) - 42 routes 
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
                via TI-LFA tunnel index 20, forward
                 payload autoDecide, ttlMode uniform, dscpMode uniform, apply egress-acl
                    via 20.57.171.57, Ethernet49/1, label imp-null(3)
                    backup via 20.171.172.172, Ethernet47, label imp-null(3)
 IP    20019    [1], 10.0.0.19/32
                via TI-LFA tunnel index 20, forward
                 payload autoDecide, ttlMode uniform, dscpMode uniform, apply egress-acl
                    via 20.57.171.57, Ethernet49/1, label imp-null(3)
                    backup via 20.171.172.172, Ethernet47, label imp-null(3)
 IP    20024    [1], 10.0.0.24/32
                via TI-LFA tunnel index 20, forward
                 payload autoDecide, ttlMode uniform, dscpMode uniform, apply egress-acl
                    via 20.57.171.57, Ethernet49/1, label imp-null(3)
                    backup via 20.171.172.172, Ethernet47, label imp-null(3)
 IP    20032    [1], 10.0.0.32/32
                via TI-LFA tunnel index 1, pop
                 payload autoDecide, ttlMode uniform, dscpMode uniform, apply egress-acl
                    via 20.32.171.32, Ethernet7, label imp-null(3)
                    backup via 20.57.171.57, Ethernet49/1, label 20032
 IP    20057    [1], 10.0.0.57/32
                via TI-LFA tunnel index 20, forward
                 payload autoDecide, ttlMode uniform, dscpMode uniform, apply egress-acl
                    via 20.57.171.57, Ethernet49/1, label imp-null(3)
                    backup via 20.171.172.172, Ethernet47, label imp-null(3)
 IP    20083    [1], 10.0.0.83/32
                via TI-LFA tunnel index 20, forward
                 payload autoDecide, ttlMode uniform, dscpMode uniform, apply egress-acl
                    via 20.57.171.57, Ethernet49/1, label imp-null(3)
                    backup via 20.171.172.172, Ethernet47, label imp-null(3)
 IP    20172    [1], 10.0.0.172/32
                via TI-LFA tunnel index 0, pop
                 payload autoDecide, ttlMode uniform, dscpMode uniform, apply egress-acl
                    via 20.171.172.172, Ethernet47, label imp-null(3)
                    backup via 20.57.171.57, Ethernet49/1, label 20172
 IP    20349    [1], 10.0.1.49/32
                via TI-LFA tunnel index 20, forward
                 payload autoDecide, ttlMode uniform, dscpMode uniform, apply egress-acl
                    via 20.57.171.57, Ethernet49/1, label imp-null(3)
                    backup via 20.171.172.172, Ethernet47, label imp-null(3)
 IP    20355    [1], 10.0.1.55/32
                via TI-LFA tunnel index 20, forward
                 payload autoDecide, ttlMode uniform, dscpMode uniform, apply egress-acl
                    via 20.57.171.57, Ethernet49/1, label imp-null(3)
                    backup via 20.171.172.172, Ethernet47, label imp-null(3)
 IP    20379    [1], 10.0.0.179/32
                via TI-LFA tunnel index 20, forward
                 payload autoDecide, ttlMode uniform, dscpMode uniform, apply egress-acl
                    via 20.57.171.57, Ethernet49/1, label imp-null(3)
                    backup via 20.171.172.172, Ethernet47, label imp-null(3)
 IP    21032    [1], 10.0.0.32/32, algorithm MIN-LATENCY
                via TI-LFA tunnel index 6, pop
                 payload autoDecide, ttlMode uniform, dscpMode uniform, apply egress-acl
                    via 20.32.171.32, Ethernet7, label imp-null(3)
                    backup via 20.57.171.57, Ethernet49/1, label 21032
 IP    21057    [1], 10.0.0.57/32, algorithm MIN-LATENCY
                via TI-LFA tunnel index 5, forward
                 payload autoDecide, ttlMode uniform, dscpMode uniform, apply egress-acl
                    via 20.32.171.32, Ethernet7, label imp-null(3)
                    backup via 20.57.171.57, Ethernet49/1, label imp-null(3)
 IP    21105    [1], 10.0.0.5/32, algorithm MIN-TE
                via TI-LFA tunnel index 20, forward
                 payload autoDecide, ttlMode uniform, dscpMode uniform, apply egress-acl
                    via 20.57.171.57, Ethernet49/1, label imp-null(3)
                    backup via 20.171.172.172, Ethernet47, label imp-null(3)
 IP    21119    [1], 10.0.0.19/32, algorithm MIN-TE
                via TI-LFA tunnel index 20, forward
                 payload autoDecide, ttlMode uniform, dscpMode uniform, apply egress-acl
                    via 20.57.171.57, Ethernet49/1, label imp-null(3)
                    backup via 20.171.172.172, Ethernet47, label imp-null(3)
 IP    21124    [1], 10.0.0.24/32, algorithm MIN-TE
                via TI-LFA tunnel index 20, forward
                 payload autoDecide, ttlMode uniform, dscpMode uniform, apply egress-acl
                    via 20.57.171.57, Ethernet49/1, label imp-null(3)
                    backup via 20.171.172.172, Ethernet47, label imp-null(3)
 IP    21157    [1], 10.0.0.57/32, algorithm MIN-TE
                via TI-LFA tunnel index 20, forward
                 payload autoDecide, ttlMode uniform, dscpMode uniform, apply egress-acl
                    via 20.57.171.57, Ethernet49/1, label imp-null(3)
                    backup via 20.171.172.172, Ethernet47, label imp-null(3)
 IP    21179    [1], 10.0.0.179/32, algorithm MIN-LATENCY
                via TI-LFA tunnel index 5, forward
                 payload autoDecide, ttlMode uniform, dscpMode uniform, apply egress-acl
                    via 20.32.171.32, Ethernet7, label imp-null(3)
                    backup via 20.57.171.57, Ethernet49/1, label imp-null(3)
 IP    21205    [1], 10.0.0.5/32, algorithm MIN-IGP
                via TI-LFA tunnel index 20, forward
                 payload autoDecide, ttlMode uniform, dscpMode uniform, apply egress-acl
                    via 20.57.171.57, Ethernet49/1, label imp-null(3)
                    backup via 20.171.172.172, Ethernet47, label imp-null(3)
 IP    21219    [1], 10.0.0.19/32, algorithm MIN-IGP
                via TI-LFA tunnel index 20, forward
                 payload autoDecide, ttlMode uniform, dscpMode uniform, apply egress-acl
                    via 20.57.171.57, Ethernet49/1, label imp-null(3)
                    backup via 20.171.172.172, Ethernet47, label imp-null(3)
 IP    21224    [1], 10.0.0.24/32, algorithm MIN-IGP
                via TI-LFA tunnel index 20, forward
                 payload autoDecide, ttlMode uniform, dscpMode uniform, apply egress-acl
                    via 20.57.171.57, Ethernet49/1, label imp-null(3)
                    backup via 20.171.172.172, Ethernet47, label imp-null(3)
 IP    21257    [1], 10.0.0.57/32, algorithm MIN-IGP
                via TI-LFA tunnel index 20, forward
                 payload autoDecide, ttlMode uniform, dscpMode uniform, apply egress-acl
                    via 20.57.171.57, Ethernet49/1, label imp-null(3)
                    backup via 20.171.172.172, Ethernet47, label imp-null(3)
 IP    21272    [1], 10.0.0.172/32, algorithm MIN-TE
                via M, 20.171.172.172, pop
                 payload autoDecide, ttlMode uniform, dscpMode uniform, apply egress-acl
                 interface Ethernet47
 IP    21279    [1], 10.0.0.179/32, algorithm MIN-TE
                via TI-LFA tunnel index 20, forward
                 payload autoDecide, ttlMode uniform, dscpMode uniform, apply egress-acl
                    via 20.57.171.57, Ethernet49/1, label imp-null(3)
                    backup via 20.171.172.172, Ethernet47, label imp-null(3)
 IP    21319    [1], 10.0.0.19/32, algorithm MIN-IGP-ADMIN
                via M, 20.171.172.172, forward
                 payload autoDecide, ttlMode uniform, dscpMode uniform, apply egress-acl
                 interface Ethernet47
 IP    21324    [1], 10.0.0.24/32, algorithm MIN-IGP-ADMIN
                via M, 20.171.172.172, forward
                 payload autoDecide, ttlMode uniform, dscpMode uniform, apply egress-acl
                 interface Ethernet47
 IP    21355    [1], 10.0.1.55/32, algorithm MIN-LATENCY
                via TI-LFA tunnel index 5, forward
                 payload autoDecide, ttlMode uniform, dscpMode uniform, apply egress-acl
                    via 20.32.171.32, Ethernet7, label imp-null(3)
                    backup via 20.57.171.57, Ethernet49/1, label imp-null(3)
 IP    21357    [1], 10.0.0.57/32, algorithm MIN-IGP-ADMIN
                via M, 20.171.172.172, forward
                 payload autoDecide, ttlMode uniform, dscpMode uniform, apply egress-acl
                 interface Ethernet47
 IP    21372    [1], 10.0.0.172/32, algorithm MIN-IGP
                via TI-LFA tunnel index 18, pop
                 payload autoDecide, ttlMode uniform, dscpMode uniform, apply egress-acl
                    via 20.171.172.172, Ethernet47, label imp-null(3)
                    backup via 20.57.171.57, Ethernet49/1, label 21372
 IP    21379    [1], 10.0.0.179/32, algorithm MIN-IGP
                via TI-LFA tunnel index 20, forward
                 payload autoDecide, ttlMode uniform, dscpMode uniform, apply egress-acl
                    via 20.57.171.57, Ethernet49/1, label imp-null(3)
                    backup via 20.171.172.172, Ethernet47, label imp-null(3)
 IP    21449    [1], 10.0.1.49/32, algorithm MIN-TE
                via TI-LFA tunnel index 20, forward
                 payload autoDecide, ttlMode uniform, dscpMode uniform, apply egress-acl
                    via 20.57.171.57, Ethernet49/1, label imp-null(3)
                    backup via 20.171.172.172, Ethernet47, label imp-null(3)
 IP    21455    [1], 10.0.1.55/32, algorithm MIN-TE
                via TI-LFA tunnel index 20, forward
                 payload autoDecide, ttlMode uniform, dscpMode uniform, apply egress-acl
                    via 20.57.171.57, Ethernet49/1, label imp-null(3)
                    backup via 20.171.172.172, Ethernet47, label imp-null(3)
 IP    21472    [1], 10.0.0.172/32, algorithm MIN-IGP-ADMIN
                via M, 20.171.172.172, pop
                 payload autoDecide, ttlMode uniform, dscpMode uniform, apply egress-acl
                 interface Ethernet47
 IP    21555    [1], 10.0.1.55/32, algorithm MIN-IGP
                via TI-LFA tunnel index 20, forward
                 payload autoDecide, ttlMode uniform, dscpMode uniform, apply egress-acl
                    via 20.57.171.57, Ethernet49/1, label imp-null(3)
                    backup via 20.171.172.172, Ethernet47, label imp-null(3)
 IP    21649    [1], 10.0.1.49/32, algorithm MIN-IGP
                via TI-LFA tunnel index 20, forward
                 payload autoDecide, ttlMode uniform, dscpMode uniform, apply egress-acl
                    via 20.57.171.57, Ethernet49/1, label imp-null(3)
                    backup via 20.171.172.172, Ethernet47, label imp-null(3)
 IP    21655    [1], 10.0.1.55/32, algorithm MIN-IGP-ADMIN
                via M, 20.171.172.172, forward
                 payload autoDecide, ttlMode uniform, dscpMode uniform, apply egress-acl
                 interface Ethernet47
 IA    362146   [1]
                via M, 20.171.172.172, pop
                 payload autoDecide, ttlMode uniform, apply egress-acl
                 interface Ethernet47
 IA    362147   [1]
                via M, 20.57.171.57, pop
                 payload autoDecide, ttlMode uniform, apply egress-acl
                 interface Ethernet49/1
 IA    362148   [1]
                via M, 20.32.171.32, pop
                 payload autoDecide, ttlMode uniform, apply egress-acl
                 interface Ethernet7
 B3    378528   [0]
                via I, ipv4, vrf ISIS-SR-FLEXALGO-MIN-TE
 B3    378529   [0]
                via I, ipv4, vrf ISIS-SR-FLEXALGO-MIN-IGP-ADMIN
 B3    378530   [0]
                via I, ipv4, vrf ISIS-SR-FLEXALGO-MIN-IGP
 B3    378531   [0]
                via I, ipv4, vrf ISIS-SR-FLEXALGO-MIN-DELAY
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
 * >      RD: 65000:5 IPv4 prefix 20.5.111.0/24
                                 10.0.0.5              -       100     0       ? Or-ID: 10.0.0.5 C-LST: 10.0.1.49 
 * >      RD: 65000:128 IPv4 prefix 20.5.111.0/24
                                 10.0.0.5              -       100     0       ? Or-ID: 10.0.0.5 C-LST: 10.0.1.49 
 * >      RD: 65000:129 IPv4 prefix 20.5.111.0/24
                                 10.0.0.5              -       100     0       ? Or-ID: 10.0.0.5 C-LST: 10.0.1.49 
 * >      RD: 65000:130 IPv4 prefix 20.5.111.0/24
                                 10.0.0.5              -       100     0       ? Or-ID: 10.0.0.5 C-LST: 10.0.1.49 
 * >      RD: 65000:19 IPv4 prefix 20.19.111.0/24
                                 10.0.0.19             0       100     0       ? Or-ID: 10.0.0.19 C-LST: 10.0.1.49 
 * >      RD: 65000:128 IPv4 prefix 20.19.111.0/24
                                 10.0.0.19             0       100     0       ? Or-ID: 10.0.0.19 C-LST: 10.0.1.49 
 * >      RD: 65000:129 IPv4 prefix 20.19.111.0/24
                                 10.0.0.19             0       100     0       ? Or-ID: 10.0.0.19 C-LST: 10.0.1.49 
 * >      RD: 65000:130 IPv4 prefix 20.19.111.0/24
                                 10.0.0.19             0       100     0       ? Or-ID: 10.0.0.19 C-LST: 10.0.1.49 
 * >      RD: 65000:131 IPv4 prefix 20.19.111.0/24
                                 10.0.0.19             0       100     0       ? Or-ID: 10.0.0.19 C-LST: 10.0.1.49 
 * >      RD: 65001:19 IPv4 prefix 20.19.111.0/24
                                 10.0.0.19             0       100     0       ? Or-ID: 10.0.0.19 C-LST: 10.0.1.49 
 * >      RD: 65000:224 IPv4 prefix 20.24.111.0/24
                                 10.0.0.24             0       100     0       ? Or-ID: 10.0.0.24 C-LST: 10.0.1.49 
 * >      RD: 10.0.0.24:128 IPv4 prefix 20.24.111.0/24
                                 10.0.0.24             0       100     0       ? Or-ID: 10.0.0.24 C-LST: 10.0.1.49 
 * >      RD: 10.0.0.24:129 IPv4 prefix 20.24.111.0/24
                                 10.0.0.24             0       100     0       ? Or-ID: 10.0.0.24 C-LST: 10.0.1.49 
 * >      RD: 10.0.0.24:130 IPv4 prefix 20.24.111.0/24
                                 10.0.0.24             0       100     0       ? Or-ID: 10.0.0.24 C-LST: 10.0.1.49 
 * >      RD: 10.0.0.24:131 IPv4 prefix 20.24.111.0/24
                                 10.0.0.24             0       100     0       ? Or-ID: 10.0.0.24 C-LST: 10.0.1.49 
 * >      RD: 65000:128 IPv4 prefix 20.32.111.0/24
                                 10.0.0.32             -       100     0       i Or-ID: 10.0.0.32 C-LST: 10.0.1.49 
 * >      RD: 65000:129 IPv4 prefix 20.32.111.0/24
                                 10.0.0.32             -       100     0       i Or-ID: 10.0.0.32 C-LST: 10.0.1.49 
 * >      RD: 65000:130 IPv4 prefix 20.32.111.0/24
                                 10.0.0.32             -       100     0       i Or-ID: 10.0.0.32 C-LST: 10.0.1.49 
 * >      RD: 10.0.1.55:1 IPv4 prefix 20.55.111.0/24
                                 10.0.1.55             0       100     0       ? Or-ID: 10.0.1.55 C-LST: 10.0.1.49 
 * >      RD: 10.0.0.57:1 IPv4 prefix 20.57.111.0/24
                                 10.0.0.57             -       100     0       i Or-ID: 10.0.0.57 C-LST: 10.0.1.49 
 * >      RD: 10.0.0.57:128 IPv4 prefix 20.57.111.0/24
                                 10.0.0.57             -       100     0       i Or-ID: 10.0.0.57 C-LST: 10.0.1.49 
 * >      RD: 10.0.0.57:129 IPv4 prefix 20.57.111.0/24
                                 10.0.0.57             -       100     0       i Or-ID: 10.0.0.57 C-LST: 10.0.1.49 
 * >      RD: 10.0.0.57:130 IPv4 prefix 20.57.111.0/24
                                 10.0.0.57             -       100     0       i Or-ID: 10.0.0.57 C-LST: 10.0.1.49 
 * >      RD: 10.0.0.57:131 IPv4 prefix 20.57.111.0/24
                                 10.0.0.57             -       100     0       i Or-ID: 10.0.0.57 C-LST: 10.0.1.49 
 * >      RD: 10.0.0.57:132 IPv4 prefix 20.57.111.0/24
                                 10.0.0.57             -       100     0       i Or-ID: 10.0.0.57 C-LST: 10.0.1.49 
 * >      RD: 10.0.0.83:2 IPv4 prefix 20.83.111.0/24
                                 10.0.0.83             -       100     0       i Or-ID: 10.0.0.83 C-LST: 10.0.1.49 
 * >      RD: 65000:140 IPv4 prefix 20.111.155.0/24
                                 10.0.1.55             0       100     0       ? Or-ID: 10.0.1.55 C-LST: 10.0.1.49 
 * >      RD: 65000:141 IPv4 prefix 20.111.155.0/24
                                 10.0.1.55             0       100     0       ? Or-ID: 10.0.1.55 C-LST: 10.0.1.49 
 * >      RD: 65000:142 IPv4 prefix 20.111.155.0/24
                                 10.0.1.55             0       100     0       ? Or-ID: 10.0.1.55 C-LST: 10.0.1.49 
 * >      RD: 10.0.1.55:128 IPv4 prefix 20.111.155.0/24
                                 10.0.1.55             0       100     0       ? Or-ID: 10.0.1.55 C-LST: 10.0.1.49 
 * >      RD: 10.0.1.55:129 IPv4 prefix 20.111.155.0/24
                                 10.0.1.55             0       100     0       ? Or-ID: 10.0.1.55 C-LST: 10.0.1.49 
 * >      RD: 10.0.1.55:130 IPv4 prefix 20.111.155.0/24
                                 10.0.1.55             0       100     0       ? Or-ID: 10.0.1.55 C-LST: 10.0.1.49 
 * >      RD: 10.0.1.55:131 IPv4 prefix 20.111.155.0/24
                                 10.0.1.55             0       100     0       ? Or-ID: 10.0.1.55 C-LST: 10.0.1.49 
 * >      RD: 10.0.1.55:132 IPv4 prefix 20.111.155.0/24
                                 10.0.1.55             0       100     0       ? Or-ID: 10.0.1.55 C-LST: 10.0.1.49 
 * >      RD: 10.0.0.171:128 IPv4 prefix 20.111.171.0/24
                                 -                     -       -       0       i
 * >      RD: 10.0.0.171:129 IPv4 prefix 20.111.171.0/24
                                 -                     -       -       0       i
 * >      RD: 10.0.0.171:130 IPv4 prefix 20.111.171.0/24
                                 -                     -       -       0       i
 * >      RD: 10.0.0.171:131 IPv4 prefix 20.111.171.0/24
                                 -                     -       -       0       i
 * >      RD: 10.0.0.179:1809 IPv4 prefix 20.111.179.0/24
                                 10.0.0.179            -       100     0       i Or-ID: 10.0.0.179 C-LST: 10.0.1.49 
 * >      RD: 10.0.0.179:1810 IPv4 prefix 20.111.179.0/24
                                 10.0.0.179            -       100     0       i Or-ID: 10.0.0.179 C-LST: 10.0.1.49 
 * >      RD: 10.0.0.179:1811 IPv4 prefix 20.111.179.0/24
                                 10.0.0.179            -       100     0       i Or-ID: 10.0.0.179 C-LST: 10.0.1.49 
 * >      RD: 10.0.0.179:1812 IPv4 prefix 20.111.179.0/24
                                 10.0.0.179            -       100     0       i Or-ID: 10.0.0.179 C-LST: 10.0.1.49 
 * >      RD: 10.0.0.179:1813 IPv4 prefix 20.111.179.0/24
                                 10.0.0.179            -       100     0       i Or-ID: 10.0.0.179 C-LST: 10.0.1.49 
 * >      RD: 10.0.0.179:1814 IPv4 prefix 20.111.179.0/24
                                 10.0.0.179            -       100     0       i Or-ID: 10.0.0.179 C-LST: 10.0.1.49 
          RD: 65000:1254 IPv4 prefix 20.111.254.0/24
                                 10.0.0.254            0       100     0       ? Or-ID: 10.0.0.254 C-LST: 10.0.1.49 
          RD: 65000:1354 IPv4 prefix 20.111.254.0/24
                                 10.0.0.254            0       100     0       ? Or-ID: 10.0.0.254 C-LST: 10.0.1.49 
          RD: 65000:1454 IPv4 prefix 20.111.254.0/24
                                 10.0.0.254            0       100     0       ? Or-ID: 10.0.0.254 C-LST: 10.0.1.49 
          RD: 65000:1554 IPv4 prefix 20.111.254.0/24
                                 10.0.0.254            0       100     0       ? Or-ID: 10.0.0.254 C-LST: 10.0.1.49 
 * >      RD: 10.0.1.55:130 IPv4 prefix 55.55.55.130/32
                                 10.0.1.55             0       100     0       ? Or-ID: 10.0.1.55 C-LST: 10.0.1.49 
 * >      RD: 65000:140 IPv4 prefix 155.155.155.140/32
                                 10.0.1.55             0       100     0       ? Or-ID: 10.0.1.55 C-LST: 10.0.1.49 
 * >      RD: 65000:141 IPv4 prefix 155.155.155.141/32
                                 10.0.1.55             0       100     0       ? Or-ID: 10.0.1.55 C-LST: 10.0.1.49 
 * >      RD: 65000:142 IPv4 prefix 155.155.155.142/32
                                 10.0.1.55             0       100     0       ? Or-ID: 10.0.1.55 C-LST: 10.0.1.49 
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
```

## show bgp neighbors

```text
BGP neighbor is 10.0.1.49, remote AS 65000, internal link
  BGP version 4, remote router ID 10.0.1.49, VRF default
  Inherits configuration from and member of peer-group IBGP-PEER
  Last read 00:00:20, last write 00:00:45
  Hold time is 180, keepalive interval is 60 seconds
  Configured hold time is 180, keepalive interval is 60 seconds
  Effective minimum hold time is 3 seconds
  Send failure hold time is 0 seconds
  Hold timer is active, time left: 00:02:40
  Keepalive timer is active, time left: 00:00:03
  Connect timer is inactive
  Idle-restart timer is inactive
  BGP state is Established, up for 16:03:46
  Number of transitions to established: 1
  Last state was OpenConfirm
  Last event was RecvKeepAlive
  Last sent socket-error:Connect (Network is unreachable), Last time 16:04:53, First time 16:05:18, Repeats 5
  Types of communities advertised: standard extended large
  Neighbor Capabilities:
    Multiprotocol IPv4 Unicast: advertised
    Multiprotocol VPN-IPv4: advertised and received and negotiated
    Multiprotocol L2VPN EVPN: advertised
    Four Octet ASN: advertised and received and negotiated
    Route Refresh: advertised and received and negotiated
    Enhanced route refresh: advertised
    Send End-of-RIB messages: advertised
    Additional-paths recv capability:
      IPv4 Unicast: advertised
      VPN-IPv4: advertised
      L2VPN EVPN: advertised
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
  BGP session driven failover for IPv6 Unicast is disabled
  BGP session driven failover for IPv4 Unicast is disabled
  Message Statistics:
                         Sent      Rcvd
    Opens:                  1         1
    Notifications:          0         0
    Updates:                4        82
    Keepalives:          1124       959
    Route Refresh:          0         0
    Total messages:      1129      1042
  Prefix Statistics:
                                   Sent      Rcvd     Best Paths     Best ECMP Paths
    IPv4 Unicast:                     0         0              0                   0
    VPN-IPv4:                         4        48             44                   0
    IPv6 Unicast:                     0         0              0                   0
  Configured maximum total number of routes is 0
  Inbound updates dropped by reason:
    AS path loop detection: 0
    Cluster ID loop detection: 0
    Enforced First AS: 0
    Malformed MPBGP routes: 0
    Originator ID matches local router ID: 0
    Nexthop matches local IP address: 4
    Unexpected IPv6 nexthop for IPv4 routes: 0
  Inbound updates with attribute errors:
    Resulting in removal of all paths in update (treat as withdraw): 4
    Resulting in AFI/SAFI disable: 0
    Resulting in attribute ignore: 0
    Disabled AFI/SAFIs: None
    Last treat-as-withdraw attribute error: Nexthop is local address
    Last update with error received at: 16:03:41
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
  Outbound route map is RM-FLEXALGO
Local AS is 65000, local router ID 10.0.0.171
TTL is 255
Local TCP address is 10.0.0.171, local port is 37779
Remote TCP address is 10.0.1.49, remote port is 179
Local next hop for next hop self:
  VPN-IPv4: 10.0.0.171
TCP Socket Information:
  TCP state is ESTABLISHED
  Recv-Q: 0/32768
  Send-Q: 0/46080
  Outgoing Maximum Segment Size (MSS): 1240
  Total Number of TCP retransmissions: 3
  Options:
    Timestamps enabled: no
    Selective Acknowledgments enabled: no
    Window Scale enabled: yes
    Explicit Congestion Notification (ECN) enabled: no
  Socket Statistics:
    Window Scale (wscale): 0,7
    Retransmission Timeout (rto): 400.0ms
    Round-trip Time (rtt/rtvar): 199.5ms/2.5ms
    Delayed Ack Timeout (ato): 40.0ms
    Congestion Window (cwnd): 2
    Slow-start Threshold (ssthresh): 2
    TCP Throughput: 0.10 Mbps
    Advertised Recv Window (rcv_space): 14600

```

## show tunnel rib system-tunnel-rib brief

```text
Tunnel RIB: system-tunnel-rib
Endpoint        Tunnel Type     Index(es)   Tunnel Preference   IGP Preference 
-------------- --------------- ----------- ------------------- ----------------
10.0.0.5/32     IS-IS SR IPv4   8           200                 115            
10.0.0.19/32    IS-IS SR IPv4   3           200                 115            
10.0.0.24/32    IS-IS SR IPv4   5           200                 115            
10.0.0.32/32    IS-IS SR IPv4   9           200                 115            
10.0.0.57/32    IS-IS SR IPv4   6           200                 115            
10.0.0.83/32    IS-IS SR IPv4   1           200                 115            
10.0.0.172/32   IS-IS SR IPv4   10          200                 115            
10.0.0.179/32   IS-IS SR IPv4   7           200                 115            
10.0.1.49/32    IS-IS SR IPv4   2           200                 115            
10.0.1.55/32    IS-IS SR IPv4   4           200                 115            

   IGP Metric    Metric Type
---------------- -----------
   40            metric     
   30            metric     
   30            metric     
   10            metric     
   10            metric     
   30            metric     
   10            metric     
   20            metric     
   20            metric     
   20            metric     

```

## show tunnel rib colored brief

```text
Tunnel RIB: system-colored-tunnel-rib
 Endpoint        Color   Tunnel Type       Index(es)    Tunnel Preference    IGP Preference    IGP Metric   Metric Type
--------------- ------- ----------------- ------------ -------------------- ----------------- ------------- -----------
 10.0.0.5/32     129     IS-IS FlexAlgo    7            65                   115               36           metric     
 10.0.0.5/32     130     IS-IS FlexAlgo    9            65                   115               30           metric     
 10.0.0.19/32    129     IS-IS FlexAlgo    8            65                   115               36           metric     
 10.0.0.19/32    130     IS-IS FlexAlgo    14           65                   115               30           metric     
 10.0.0.19/32    131     IS-IS FlexAlgo    17           65                   115               50           metric     
 10.0.0.24/32    129     IS-IS FlexAlgo    6            65                   115               36           metric     
 10.0.0.24/32    130     IS-IS FlexAlgo    13           65                   115               30           metric     
 10.0.0.24/32    131     IS-IS FlexAlgo    15           65                   115               50           metric     
 10.0.0.32/32    128     IS-IS FlexAlgo    24           65                   115               11           metric     
 10.0.0.57/32    128     IS-IS FlexAlgo    22           65                   115               22           metric     
 10.0.0.57/32    129     IS-IS FlexAlgo    5            65                   115               12           metric     
 10.0.0.57/32    130     IS-IS FlexAlgo    4            65                   115               10           metric     
 10.0.0.57/32    131     IS-IS FlexAlgo    18           65                   115               20           metric     
 10.0.0.172/32   129     IS-IS FlexAlgo    26           65                   115               12           metric     
 10.0.0.172/32   130     IS-IS FlexAlgo    28           65                   115               10           metric     
 10.0.0.172/32   131     IS-IS FlexAlgo    27           65                   115               10           metric     
 10.0.0.179/32   128     IS-IS FlexAlgo    23           65                   115               33           metric     
 10.0.0.179/32   129     IS-IS FlexAlgo    3            65                   115               24           metric     
 10.0.0.179/32   130     IS-IS FlexAlgo    12           65                   115               20           metric     
 10.0.1.49/32    129     IS-IS FlexAlgo    1            65                   115               24           metric     
 10.0.1.49/32    130     IS-IS FlexAlgo    10           65                   115               20           metric     
 10.0.1.55/32    128     IS-IS FlexAlgo    21           65                   115               31           metric     
 10.0.1.55/32    129     IS-IS FlexAlgo    11           65                   115               24           metric     
 10.0.1.55/32    130     IS-IS FlexAlgo    2            65                   115               20           metric     
 10.0.1.55/32    131     IS-IS FlexAlgo    16           65                   115               30           metric     

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
>C    10.0.0.171/32 [0 pref/0 metric] updated 16:05:41 ago
         via Loopback0, directly connected
>C    20.32.171.0/24 [0 pref/0 metric] updated 00:04:46 ago
         via Ethernet7, directly connected
>C    20.57.171.0/24 [0 pref/0 metric] updated 00:26:27 ago
         via Ethernet49/1, directly connected
>C    20.171.172.0/24 [0 pref/0 metric] updated 00:36:26 ago
         via Ethernet47, directly connected
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
>P    0.0.0.0/8 [1 pref/0 metric] updated 16:05:38 ago
         via Null0, directly connected [NF]
>P    127.0.0.0/8 [1 pref/0 metric] updated 16:05:38 ago
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
>I    10.0.0.5/32 [115 pref/40 metric] updated 00:12:47 ago
         via 20.57.171.57, Ethernet49/1
>I    10.0.0.19/32 [115 pref/30 metric] updated 00:12:47 ago
         via 20.57.171.57, Ethernet49/1
>I    10.0.0.24/32 [115 pref/30 metric] updated 00:12:47 ago
         via 20.57.171.57, Ethernet49/1
>I    10.0.0.32/32 [115 pref/10 metric] updated 00:04:29 ago
         via 20.32.171.32, Ethernet7
>I    10.0.0.57/32 [115 pref/10 metric] updated 00:25:59 ago
         via 20.57.171.57, Ethernet49/1
>I    10.0.0.83/32 [115 pref/30 metric] updated 00:12:47 ago
         via 20.57.171.57, Ethernet49/1
>I    10.0.0.172/32 [115 pref/10 metric] updated 00:35:26 ago
         via 20.171.172.172, Ethernet47
>I    10.0.0.179/32 [115 pref/20 metric] updated 00:20:10 ago
         via 20.57.171.57, Ethernet49/1
>I    10.0.0.254/32 [115 pref/20 metric] updated 00:24:41 ago
         via 20.57.171.57, Ethernet49/1
>I    10.0.1.49/32 [115 pref/20 metric] updated 00:12:47 ago
         via 20.57.171.57, Ethernet49/1
>I    10.0.1.55/32 [115 pref/20 metric] updated 00:20:10 ago
         via 20.57.171.57, Ethernet49/1
>I    20.5.149.0/24 [115 pref/30 metric] updated 00:12:47 ago
         via 20.57.171.57, Ethernet49/1
>I    20.19.149.0/24 [115 pref/30 metric] updated 00:12:47 ago
         via 20.57.171.57, Ethernet49/1
>I    20.24.149.0/24 [115 pref/30 metric] updated 00:12:47 ago
         via 20.57.171.57, Ethernet49/1
>I    20.32.57.0/24 [115 pref/20 metric] updated 00:04:29 ago
         via 20.32.171.32, Ethernet7
         via 20.57.171.57, Ethernet49/1
>I    20.32.149.0/24 [115 pref/20 metric] updated 00:04:29 ago
         via 20.32.171.32, Ethernet7
>I    20.32.211.0/24 [115 pref/20 metric] updated 00:04:29 ago
         via 20.32.171.32, Ethernet7
>I    20.47.149.0/24 [115 pref/30 metric] updated 00:12:47 ago
         via 20.57.171.57, Ethernet49/1
>I    20.57.149.0/24 [115 pref/20 metric] updated 00:25:28 ago
         via 20.57.171.57, Ethernet49/1
>I    20.57.155.0/24 [115 pref/20 metric] updated 00:20:10 ago
         via 20.57.171.57, Ethernet49/1
>I    20.57.172.0/24 [115 pref/20 metric] updated 00:25:59 ago
         via 20.57.171.57, Ethernet49/1
         via 20.171.172.172, Ethernet47
>I    20.57.179.0/24 [115 pref/20 metric] updated 00:25:59 ago
         via 20.57.171.57, Ethernet49/1
>I    20.57.211.0/24 [115 pref/20 metric] updated 00:25:59 ago
         via 20.57.171.57, Ethernet49/1
>I    20.57.254.0/24 [115 pref/20 metric] updated 00:24:41 ago
         via 20.57.171.57, Ethernet49/1
>I    20.83.149.0/24 [115 pref/30 metric] updated 00:12:47 ago
         via 20.57.171.57, Ethernet49/1
>I    20.111.149.0/24 [115 pref/30 metric] updated 00:12:47 ago
         via 20.57.171.57, Ethernet49/1
>I    20.149.155.0/24 [115 pref/30 metric] updated 00:12:47 ago
         via 20.57.171.57, Ethernet49/1
>I    20.149.254.0/24 [115 pref/30 metric] updated 00:12:47 ago
         via 20.57.171.57, Ethernet49/1
>I    20.155.179.0/24 [115 pref/30 metric] updated 00:20:10 ago
         via 20.57.171.57, Ethernet49/1
>I    30.155.179.0/24 [115 pref/30 metric] updated 00:20:10 ago
         via 20.57.171.57, Ethernet49/1
>I    192.168.0.0/19 [115 pref/30 metric] updated 00:12:47 ago
         via 20.57.171.57, Ethernet49/1
>I    192.168.20.0/23 [115 pref/30 metric] updated 00:12:47 ago
         via 20.57.171.57, Ethernet49/1
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
>P    ::/96 [1 pref/0 metric] updated 16:05:38 ago
         via Null0, directly connected [NF]
>P    ::ffff:127.0.0.0/104 [1 pref/0 metric] updated 16:05:38 ago
         via :: [1 pref/1 metric] type ipv6
            via , directly connected
>P    fe80::/10 [1 pref/0 metric] updated 16:05:38 ago
```

## show platform sand l3 summary

```text
Number of vrfs: 7

Ipv4:
  Routes:       117  backlog:  0  unprogrammed:  0
  Adjacencies:  109  backlog:  0  unprogrammed:  0
Ipv6:
  Routes:       0    backlog:  0  unprogrammed:  0
  Adjacencies:  109  backlog:  0  unprogrammed:  0
Mpls:
  Routes:       38  backlog:  0  unprogrammed:  0
  Adjacencies:  3   backlog:  0  unprogrammed:  0

Jericho2 Ip Fecs:
  Non-ecmp fecs:  4165  ecmp fecs:  2  fec entries:  4169
Jericho2 Mpls Fecs:
  Non-ecmp fecs:  3  ecmp fecs:  0  fec entries:  3
Jericho2 Vxlan Tunnel Fecs:
  Non-ecmp fecs:  0  ecmp fecs:  0  fec entries:  0
  Number of vxlan tunnels configured: 0

Jericho2 Lpm Routes:
  Routes:   117  unprogrammed:   0   
  Routes6:  1    unprogrammed6:  0   
  Backlog:  0  

Jericho2 Lpm:
  TCAM entries used:   3   Percent free:  99  ADS2 entries used:   8  Percent free:  99
  Pivot buckets used:  4   Rows used:     1   Entries Per Bucket:  2  Percent free:  99
  Route buckets used:  18  Rows used:     3   Entries Per Bucket:  6  Percent free:  99

Lem:
  IPv4  Host in Lem:            disabled
  IPv4  Prefix-lengths in Lem:  None    
  IPv6  Host in Lem:            disabled
  IPv6  Prefix-lengths in Lem:  None    
  Number of downloads:        0
  Number of overflow events:  0

Egress Arp rewrite entries in use (in each fap):
  FixedSystem: 5
Egress Arp remote rewrite entries in use (in each fap):
  FixedSystem: 0
Egress Ip tunnel rewrite entries in use (in each fap):
  FixedSystem: 0
Egress Mpls (for outer 2 labels) rewrite entries in use (in each fap):
  FixedSystem: 0
Egress Mpls (for inner 2 labels) rewrite entries in use (in each fap):
  FixedSystem: 37
Egress Sflow rewrite entries in use (in each fap):
  FixedSystem: 0

Egress rewrite chains in backlog: resource-full 0, no-interface 0

Glem entries used per fap :
  FixedSystem: 4178

Jericho2 Fec:
  Maximum FEC hierarchy levels:  2
  ReusedEcmp:  14  allocs:  306  frees:  234  shuffles:  0  cmds:  0
  Zombies:     0    purges:    0
  Quarantine:  0/0  shuffles:  0  deletes:  0   
  Fec insertion failures:  0
  Level1  Fecs:
    Non-ecmp fecs:            0    ecmp fecs:            1 
    Non-ecmp (Percent free):  100  ecmp (Percent free):  99
  Level2  Fecs:
    Non-ecmp fecs:            50  ecmp fecs:            0  
    Non-ecmp (Percent free):  99  ecmp (Percent free):  100
  Level3  Fecs:
    Non-ecmp fecs:            98  ecmp fecs:            2 
    Non-ecmp (Percent free):  99  ecmp (Percent free):  99

Lpm Detail:
  Requests:  554  cleanses:  115  batches:  115  avg batch size:  4

Jericho Arp:
  ArpTable writes:      21196  queued      0   
  IngressTable writes:  78577  queued      0   
  Coprocessors:         1      in CmdRing

Tunnel Counter Status
  Number of MPLS tunnels:                  77   
  Number of uncountable MPLS tunnels:      22   
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
|0  |0.0.0.0/8         |DROP | DROP               |0    |  -     |                   |  -  |528482|   -   
|0  |10.0.0.5/32       |ROUTE| Et49/1             |1020 |103428  | c0:14:b8:21:ca:6e |  -  |528558|   -   
|0  |10.0.0.19/32      |ROUTE| Et49/1             |1020 |103428  | c0:14:b8:21:ca:6e |  -  |528558|   -   
|0  |10.0.0.24/32      |ROUTE| Et49/1             |1020 |103428  | c0:14:b8:21:ca:6e |  -  |528558|   -   
|0  |10.0.0.32/32      |ROUTE| Et7                |1021 |103421  | 30:c5:07:1f:33:0f |  -  |528574|   -   
|0  |10.0.0.57/32      |ROUTE| Et49/1             |1020 |103428  | c0:14:b8:21:ca:6e |  -  |528558|   -   
|0  |10.0.0.83/32      |ROUTE| Et49/1             |1020 |103428  | c0:14:b8:21:ca:6e |  -  |528558|   -   
|0  |10.0.0.171/32     |TRAP | CoppSystemIpUcast  |0    |  -     | Receive           |  -  |524291|   -   
|0  |10.0.0.172/32     |ROUTE| Et47               |1016 |103427  | 2c:dd:e9:96:3a:bb |  -  |528582|   -   
|0  |10.0.0.179/32     |ROUTE| Et49/1             |1020 |103428  | c0:14:b8:21:ca:6e |  -  |528558|   -   
|0  |10.0.0.254/32     |ROUTE| Et49/1             |1020 |103428  | c0:14:b8:21:ca:6e |  -  |528558|   -   
|0  |10.0.1.49/32      |ROUTE| Et49/1             |1020 |103428  | c0:14:b8:21:ca:6e |  -  |528558|   -   
|0  |10.0.1.55/32      |ROUTE| Et49/1             |1020 |103428  | c0:14:b8:21:ca:6e |  -  |528558|   -   
|0  |20.5.149.0/24     |ROUTE| Et49/1             |1020 |103428  | c0:14:b8:21:ca:6e |  -  |528558|   -   
|0  |20.19.149.0/24    |ROUTE| Et49/1             |1020 |103428  | c0:14:b8:21:ca:6e |  -  |528558|   -   
|0  |20.24.149.0/24    |ROUTE| Et49/1             |1020 |103428  | c0:14:b8:21:ca:6e |  -  |528558|   -   
|0  |20.32.57.0/24     |ROUTE| Et49/1             |1020 |103428  | c0:14:b8:21:ca:6e |24576|528566|   -   
|0  |20.32.57.0/24     |ROUTE| Et7                |1021 |103421  | 30:c5:07:1f:33:0f |24576|528567|   -   
|0  |20.32.57.0/24     |ROUTE| Et7                |1021 |103421  | 30:c5:07:1f:33:0f |24576|528568|   -   
|0  |20.32.57.0/24     |ROUTE| Et49/1             |1020 |103428  | c0:14:b8:21:ca:6e |24576|528569|   -   
|0  |20.32.149.0/24    |ROUTE| Et7                |1021 |103421  | 30:c5:07:1f:33:0f |  -  |528574|   -   
|0  |20.32.171.0/32    |TRAP | CoppSystemIpBcast  |0    |  -     | BcastReceive      |  -  |524288|   -   
|0  |20.32.171.32/32   |ROUTE| Et7                |1021 |103421  | 30:c5:07:1f:33:0f |  -  |528598|   -   
|0  |20.32.171.171/32  |TRAP | CoppSystemIpUcast  |0    |  -     | Receive           |  -  |524291|   -   
|0  |20.32.171.255/32  |TRAP | CoppSystemIpBcast  |0    |  -     | BcastReceive      |  -  |524288|   -   
|0  |20.32.171.0/24    |TRAP | CoppSystemL3DstMiss|1021 |1021    | ArpTrap           |  -  |525315|   -   
|0  |20.32.211.0/24    |ROUTE| Et7                |1021 |103421  | 30:c5:07:1f:33:0f |  -  |528574|   -   
|0  |20.47.149.0/24    |ROUTE| Et49/1             |1020 |103428  | c0:14:b8:21:ca:6e |  -  |528558|   -   
|0  |20.57.149.0/24    |ROUTE| Et49/1             |1020 |103428  | c0:14:b8:21:ca:6e |  -  |528558|   -   
|0  |20.57.155.0/24    |ROUTE| Et49/1             |1020 |103428  | c0:14:b8:21:ca:6e |  -  |528558|   -   
|0  |20.57.171.0/32    |TRAP | CoppSystemIpBcast  |0    |  -     | BcastReceive      |  -  |524288|   -   
|0  |20.57.171.57/32   |ROUTE| Et49/1             |1020 |103428  | c0:14:b8:21:ca:6e |  -  |528556|   -   
|0  |20.57.171.171/32  |TRAP | CoppSystemIpUcast  |0    |  -     | Receive           |  -  |524291|   -   
|0  |20.57.171.255/32  |TRAP | CoppSystemIpBcast  |0    |  -     | BcastReceive      |  -  |524288|   -   
|0  |20.57.171.0/24    |TRAP | CoppSystemL3DstMiss|1020 |1020    | ArpTrap           |  -  |525314|   -   
|0  |20.57.172.0/24    |ROUTE| Et47               |1016 |103427  | 2c:dd:e9:96:3a:bb |24587|528642|   -   
|0  |20.57.172.0/24    |ROUTE| Et49/1             |1020 |103428  | c0:14:b8:21:ca:6e |24587|528643|   -   
|0  |20.57.172.0/24    |ROUTE| Et49/1             |1020 |103428  | c0:14:b8:21:ca:6e |24587|528644|   -   
|0  |20.57.172.0/24    |ROUTE| Et47               |1016 |103427  | 2c:dd:e9:96:3a:bb |24587|528645|   -   
|0  |20.57.179.0/24    |ROUTE| Et49/1             |1020 |103428  | c0:14:b8:21:ca:6e |  -  |528558|   -   
|0  |20.57.211.0/24    |ROUTE| Et49/1             |1020 |103428  | c0:14:b8:21:ca:6e |  -  |528558|   -   
|0  |20.57.254.0/24    |ROUTE| Et49/1             |1020 |103428  | c0:14:b8:21:ca:6e |  -  |528558|   -   
|0  |20.83.149.0/24    |ROUTE| Et49/1             |1020 |103428  | c0:14:b8:21:ca:6e |  -  |528558|   -   
|0  |20.111.149.0/24   |ROUTE| Et49/1             |1020 |103428  | c0:14:b8:21:ca:6e |  -  |528558|   -   
|0  |20.149.155.0/24   |ROUTE| Et49/1             |1020 |103428  | c0:14:b8:21:ca:6e |  -  |528558|   -   
|0  |20.149.254.0/24   |ROUTE| Et49/1             |1020 |103428  | c0:14:b8:21:ca:6e |  -  |528558|   -   
|0  |20.155.179.0/24   |ROUTE| Et49/1             |1020 |103428  | c0:14:b8:21:ca:6e |  -  |528558|   -   
|0  |20.171.172.0/32   |TRAP | CoppSystemIpBcast  |0    |  -     | BcastReceive      |  -  |524288|   -   
|0  |20.171.172.171/32 |TRAP | CoppSystemIpUcast  |0    |  -     | Receive           |  -  |524291|   -   
|0  |20.171.172.172/32 |ROUTE| Et47               |1016 |103427  | 2c:dd:e9:96:3a:bb |  -  |528580|   -   
|0  |20.171.172.255/32 |TRAP | CoppSystemIpBcast  |0    |  -     | BcastReceive      |  -  |524288|   -   
|0  |20.171.172.0/24   |TRAP | CoppSystemL3DstMiss|1016 |1016    | ArpTrap           |  -  |525310|   -   
|0  |30.155.179.0/24   |ROUTE| Et49/1             |1020 |103428  | c0:14:b8:21:ca:6e |  -  |528558|   -   
|0  |127.0.0.0/8       |TRAP | CoppSystemL3DstMiss|0    |  -     | ArpTrap           |  -  |524294|   -   
|0  |192.168.20.0/23   |ROUTE| Et49/1             |1020 |103428  | c0:14:b8:21:ca:6e |  -  |528558|   -   
|0  |192.168.0.0/19    |ROUTE| Et49/1             |1020 |103428  | c0:14:b8:21:ca:6e |  -  |528558|   -   
|0  |0.0.0.0/0         |TRAP | CoppSystemL3LpmOver|0    |  -     | SlowReceive       |  -  |524292|   -   
|1  |0.0.0.0/8         |DROP | DROP               |0    |  -     |                   |  -  |528498|   -   
|1  |20.19.111.0/24    |ROUTE| FEC 528520         |0    |2097149 | 00:00:00:00:00:00 |  -  |288376|M 21319 1268
|1  |20.24.111.0/24    |ROUTE| FEC 528516         |0    |2097135 | 00:00:00:00:00:00 |  -  |288366|M 56499
|1  |20.57.111.0/24    |ROUTE| FEC 528520         |0    |2097119 | 00:00:00:00:00:00 |  -  |288378|M 21357 524282
|1  |20.111.155.0/24   |ROUTE| FEC 528520         |0    |2097146 | 00:00:00:00:00:00 |  -  |288386|M 21655 24011
|1  |20.111.171.0/32   |TRAP | CoppSystemIpBcast  |0    |  -     | BcastReceive      |  -  |524288|   -   
|1  |20.111.171.171/32 |TRAP | CoppSystemIpUcast  |0    |  -     | Receive           |  -  |524291|   -   
|1  |20.111.171.255/32 |TRAP | CoppSystemIpBcast  |0    |  -     | BcastReceive      |  -  |524288|   -   
|1  |20.111.171.0/24   |TRAP | CoppSystemL3DstMiss|1011 |1011    | ArpTrap           |  -  |525305|   -   
|1  |127.0.0.0/8       |TRAP | CoppSystemL3DstMiss|0    |  -     | ArpTrap           |  -  |524294|   -   
|1  |0.0.0.0/0         |TRAP | CoppSystemL3LpmOver|0    |  -     | SlowReceive       |  -  |524292|   -   
|2  |0.0.0.0/8         |DROP | DROP               |0    |  -     |                   |  -  |528502|   -   
|2  |20.5.111.0/24     |ROUTE| FEC 528518         |0    |2097133 | 00:00:00:00:00:00 |  -  |288372|M 62011
|2  |20.19.111.0/24    |ROUTE| FEC 528562         |0    |2097136 | 00:00:00:00:00:00 |  -  |288370|M 1271
|2  |20.24.111.0/24    |ROUTE| FEC 528516         |0    |2097134 | 00:00:00:00:00:00 |  -  |288368|M 56502
|2  |20.32.111.0/24    |ROUTE| FEC 528588         |0    |2097127 | 00:00:00:00:00:00 |  -  |288408|M 756643
|2  |20.57.111.0/24    |ROUTE| FEC 528608         |0    |2097137 | 00:00:00:00:00:00 |  -  |288362|M 524286
|2  |20.111.155.0/24   |ROUTE| FEC 528586         |0    |2097129 | 00:00:00:00:00:00 |  -  |288394|M 24009
|2  |20.111.171.0/32   |TRAP | CoppSystemIpBcast  |0    |  -     | BcastReceive      |  -  |524288|   -   
|2  |20.111.171.128/32 |ROUTE| Et5                |1006 |103422  | 00:14:01:00:00:01 |  -  |528512|   -   
|2  |20.111.171.171/32 |TRAP | CoppSystemIpUcast  |0    |  -     | Receive           |  -  |524291|   -   
|2  |20.111.171.255/32 |TRAP | CoppSystemIpBcast  |0    |  -     | BcastReceive      |  -  |524288|   -   
|2  |20.111.171.0/24   |TRAP | CoppSystemL3DstMiss|1006 |1006    | ArpTrap           |  -  |525300|   -   
|2  |20.111.179.0/24   |ROUTE| FEC 528612         |0    |2097131 | 00:00:00:00:00:00 |  -  |288388|M 16
|2  |127.0.0.0/8       |TRAP | CoppSystemL3DstMiss|0    |  -     | ArpTrap           |  -  |524294|   -   
|2  |0.0.0.0/0         |TRAP | CoppSystemL3LpmOver|0    |  -     | SlowReceive       |  -  |524292|   -   
|3  |0.0.0.0/8         |DROP | DROP               |0    |  -     |                   |  -  |528500|   -   
|3  |20.5.111.0/24     |ROUTE| FEC 528510         |0    |2097104 | 00:00:00:00:00:00 |  -  |288396|M 62014
|3  |20.19.111.0/24    |ROUTE| FEC 528488         |0    |2097109 | 00:00:00:00:00:00 |  -  |288402|M 1269
|3  |20.24.111.0/24    |ROUTE| FEC 528504         |0    |2097107 | 00:00:00:00:00:00 |  -  |288400|M 56500
|3  |20.32.111.0/24    |ROUTE| FEC 528590         |0    |2097147 | 00:00:00:00:00:00 |  -  |288406|M 756645
|3  |20.57.111.0/24    |ROUTE| FEC 528604         |0    |2097120 | 00:00:00:00:00:00 |  -  |288382|M 524283
|3  |20.111.155.0/24   |ROUTE| FEC 528572         |0    |2097130 | 00:00:00:00:00:00 |  -  |288364|M 24012
|3  |20.111.171.0/32   |TRAP | CoppSystemIpBcast  |0    |  -     | BcastReceive      |  -  |524288|   -   
|3  |20.111.171.171/32 |TRAP | CoppSystemIpUcast  |0    |  -     | Receive           |  -  |524291|   -   
|3  |20.111.171.255/32 |TRAP | CoppSystemIpBcast  |0    |  -     | BcastReceive      |  -  |524288|   -   
|3  |20.111.171.0/24   |TRAP | CoppSystemL3DstMiss|1008 |1008    | ArpTrap           |  -  |525302|   -   
|3  |20.111.179.0/24   |ROUTE| FEC 528514         |0    |2097112 | 00:00:00:00:00:00 |  -  |288398|M 18
|3  |55.55.55.130/32   |ROUTE| FEC 528572         |0    |2097130 | 00:00:00:00:00:00 |  -  |288364|M 24012
|3  |127.0.0.0/8       |TRAP | CoppSystemL3DstMiss|0    |  -     | ArpTrap           |  -  |524294|   -   
|3  |0.0.0.0/0         |TRAP | CoppSystemL3LpmOver|0    |  -     | SlowReceive       |  -  |524292|   -   
|4  |0.0.0.0/8         |DROP | DROP               |0    |  -     |                   |  -  |528490|   -   
|4  |127.0.0.0/8       |TRAP | CoppSystemL3DstMiss|0    |  -     | ArpTrap           |  -  |524294|   -   
|4  |0.0.0.0/0         |TRAP | CoppSystemL3LpmOver|0    |  -     | SlowReceive       |  -  |524292|   -   
|5  |0.0.0.0/8         |DROP | DROP               |0    |  -     |                   |  -  |528496|   -   
|5  |20.5.111.0/24     |ROUTE| FEC 528554         |0    |2097106 | 00:00:00:00:00:00 |  -  |288392|M 62012
|5  |20.19.111.0/24    |ROUTE| FEC 528508         |0    |2097105 | 00:00:00:00:00:00 |  -  |288360|M 1270
|5  |20.24.111.0/24    |ROUTE| FEC 528600         |0    |2097108 | 00:00:00:00:00:00 |  -  |288390|M 56501
|5  |20.32.111.0/24    |ROUTE| FEC 528590         |0    |2097148 | 00:00:00:00:00:00 |  -  |288404|M 756644
|5  |20.57.111.0/24    |ROUTE| FEC 528492         |0    |2097121 | 00:00:00:00:00:00 |  -  |288384|M 524284
|5  |20.111.155.0/24   |ROUTE| FEC 528560         |0    |2097128 | 00:00:00:00:00:00 |  -  |288374|M 24010
|5  |20.111.171.0/32   |TRAP | CoppSystemIpBcast  |0    |  -     | BcastReceive      |  -  |524288|   -   
|5  |20.111.171.129/32 |ROUTE| Et5                |1019 |103426  | 00:14:01:00:00:02 |  -  |528578|   -   
|5  |20.111.171.171/32 |TRAP | CoppSystemIpUcast  |0    |  -     | Receive           |  -  |524291|   -   
|5  |20.111.171.255/32 |TRAP | CoppSystemIpBcast  |0    |  -     | BcastReceive      |  -  |524288|   -   
|5  |20.111.171.0/24   |TRAP | CoppSystemL3DstMiss|1019 |1019    | ArpTrap           |  -  |525313|   -   
|5  |20.111.179.0/24   |ROUTE| FEC 528564         |0    |2097113 | 00:00:00:00:00:00 |  -  |288380|M 17
|5  |127.0.0.0/8       |TRAP | CoppSystemL3DstMiss|0    |  -     | ArpTrap           |  -  |524294|   -   
|5  |0.0.0.0/0         |TRAP | CoppSystemL3LpmOver|0    |  -     | SlowReceive       |  -  |524292|   -   
|6  |0.0.0.0/8         |DROP | DROP               |0    |  -     |                   |  -  |528494|   -   
|6  |127.0.0.0/8       |TRAP | CoppSystemL3DstMiss|0    |  -     | ArpTrap           |  -  |524294|   -   
|6  |192.168.20.0/32   |TRAP | CoppSystemIpBcast  |0    |  -     | BcastReceive      |  -  |524288|   -   
|6  |192.168.20.171/32 |TRAP | CoppSystemIpUcast  |0    |  -     | Receive           |  -  |524291|   -   
|6  |192.168.21.255/32 |TRAP | CoppSystemIpBcast  |0    |  -     | BcastReceive      |  -  |524288|   -   
|6  |192.168.20.0/23   |TRAP | CoppSystemL3DstMiss|0    |  -     | ArpTrap           |  -  |524294|   -   
|6  |0.0.0.0/0         |TRAP | CoppSystemL3DstMiss|0    |  -     | ArpTrap           |  -  |524294|   -   

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
|24576|528566|ROUTE| Et49/1             |1020 |103428  | c0:14:b8:21:ca:6e |   -   
|24576|528567|ROUTE| Et7                |1021 |103421  | 30:c5:07:1f:33:0f |   -   
|24576|528568|ROUTE| Et7                |1021 |103421  | 30:c5:07:1f:33:0f |   -   
|24576|528569|ROUTE| Et49/1             |1020 |103428  | c0:14:b8:21:ca:6e |   -   
|24587|528642|ROUTE| Et47               |1016 |103427  | 2c:dd:e9:96:3a:bb |   -   
|24587|528643|ROUTE| Et49/1             |1020 |103428  | c0:14:b8:21:ca:6e |   -   
|24587|528644|ROUTE| Et49/1             |1020 |103428  | c0:14:b8:21:ca:6e |   -   
|24587|528645|ROUTE| Et47               |1016 |103427  | 2c:dd:e9:96:3a:bb |   -   
|  -  |288360|ROUTE| FEC 528508         |   - |2097105 |                 - |Mpush 1270
|  -  |288362|ROUTE| FEC 528608         |   - |2097137 |                 - |Mpush 524286
|  -  |288364|ROUTE| FEC 528572         |   - |2097130 |                 - |Mpush 24012
|  -  |288366|ROUTE| FEC 528516         |   - |2097135 |                 - |Mpush 56499
|  -  |288368|ROUTE| FEC 528516         |   - |2097134 |                 - |Mpush 56502
|  -  |288370|ROUTE| FEC 528562         |   - |2097136 |                 - |Mpush 1271
|  -  |288372|ROUTE| FEC 528518         |   - |2097133 |                 - |Mpush 62011
|  -  |288374|ROUTE| FEC 528560         |   - |2097128 |                 - |Mpush 24010
|  -  |288376|ROUTE| FEC 528520         |   - |2097149 |                 - |Mpush 21319 1268
|  -  |288378|ROUTE| FEC 528520         |   - |2097119 |                 - |Mpush 21357 524282
|  -  |288380|ROUTE| FEC 528564         |   - |2097113 |                 - |Mpush 17
|  -  |288382|ROUTE| FEC 528604         |   - |2097120 |                 - |Mpush 524283
|  -  |288384|ROUTE| FEC 528492         |   - |2097121 |                 - |Mpush 524284
|  -  |288386|ROUTE| FEC 528520         |   - |2097146 |                 - |Mpush 21655 24011
|  -  |288388|ROUTE| FEC 528612         |   - |2097131 |                 - |Mpush 16
|  -  |288390|ROUTE| FEC 528600         |   - |2097108 |                 - |Mpush 56501
|  -  |288392|ROUTE| FEC 528554         |   - |2097106 |                 - |Mpush 62012
|  -  |288394|ROUTE| FEC 528586         |   - |2097129 |                 - |Mpush 24009
|  -  |288396|ROUTE| FEC 528510         |   - |2097104 |                 - |Mpush 62014
|  -  |288398|ROUTE| FEC 528514         |   - |2097112 |                 - |Mpush 18
|  -  |288400|ROUTE| FEC 528504         |   - |2097107 |                 - |Mpush 56500
|  -  |288402|ROUTE| FEC 528488         |   - |2097109 |                 - |Mpush 1269
|  -  |288404|ROUTE| FEC 528590         |   - |2097148 |                 - |Mpush 756644
|  -  |288406|ROUTE| FEC 528590         |   - |2097147 |                 - |Mpush 756645
|  -  |288408|ROUTE| FEC 528588         |   - |2097127 |                 - |Mpush 756643
|  -  |524288|TRAP | CoppSystemIpBcast  |0    |  -     | BcastReceive      |   -   
|  -  |524291|TRAP | CoppSystemIpUcast  |0    |  -     | Receive           |   -   
|  -  |524292|TRAP | CoppSystemL3LpmOver|0    |  -     | SlowReceive       |   -   
|  -  |524293|TRAP | CoppSystemL3LpmOver|0    |  -     | SlowReceive       |   -   
|  -  |524294|TRAP | CoppSystemL3DstMiss|0    |  -     | ArpTrap           |   -   
|  -  |525300|TRAP | CoppSystemL3DstMiss|1006 |1006    | ArpTrap           |   -   
|  -  |525302|TRAP | CoppSystemL3DstMiss|1008 |1008    | ArpTrap           |   -   
|  -  |525305|TRAP | CoppSystemL3DstMiss|1011 |1011    | ArpTrap           |   -   
|  -  |525310|TRAP | CoppSystemL3DstMiss|1016 |1016    | ArpTrap           |   -   
|  -  |525313|TRAP | CoppSystemL3DstMiss|1019 |1019    | ArpTrap           |   -   
|  -  |525314|TRAP | CoppSystemL3DstMiss|1020 |1020    | ArpTrap           |   -   
|  -  |525315|TRAP | CoppSystemL3DstMiss|1021 |1021    | ArpTrap           |   -   
|  -  |528482|DROP | DROP               |0    |  -     |                   |   -   
|  -  |528486|ROUTE| Et7                |1021 |103471  | 30:c5:07:1f:33:0f |   -   
|  -  |528487|ROUTE| Et49/1             |1020 |103472  | c0:14:b8:21:ca:6e |   -   
|  -  |528488|ROUTE| Et49/1             |1020 |103467  | c0:14:b8:21:ca:6e |Mpush 21219
|  -  |528489|ROUTE| Et47               |1016 |103440  | 2c:dd:e9:96:3a:bb |Mpush 21219
|  -  |528490|DROP | DROP               |0    |  -     |                   |   -   
|  -  |528492|ROUTE| Et49/1             |1020 |103507  | c0:14:b8:21:ca:6e |Mpush 21157
|  -  |528493|ROUTE| Et47               |1016 |103423  | 2c:dd:e9:96:3a:bb |Mpush 21157
|  -  |528494|DROP | DROP               |0    |  -     |                   |   -   
|  -  |528496|DROP | DROP               |0    |  -     |                   |   -   
|  -  |528498|DROP | DROP               |0    |  -     |                   |   -   
|  -  |528500|DROP | DROP               |0    |  -     |                   |   -   
|  -  |528502|DROP | DROP               |0    |  -     |                   |   -   
|  -  |528504|ROUTE| Et49/1             |1020 |103491  | c0:14:b8:21:ca:6e |Mpush 21224
|  -  |528505|ROUTE| Et47               |1016 |103437  | 2c:dd:e9:96:3a:bb |Mpush 21224
|  -  |528508|ROUTE| Et49/1             |1020 |103496  | c0:14:b8:21:ca:6e |Mpush 21119
|  -  |528509|ROUTE| Et47               |1016 |103497  | 2c:dd:e9:96:3a:bb |Mpush 21119
|  -  |528510|ROUTE| Et49/1             |1020 |103498  | c0:14:b8:21:ca:6e |Mpush 21205
|  -  |528511|ROUTE| Et47               |1016 |103442  | 2c:dd:e9:96:3a:bb |Mpush 21205
|  -  |528512|ROUTE| Et5                |1006 |103422  | 00:14:01:00:00:01 |   -   
|  -  |528514|ROUTE| Et49/1             |1020 |103465  | c0:14:b8:21:ca:6e |Mpush 21379
|  -  |528515|ROUTE| Et47               |1016 |103441  | 2c:dd:e9:96:3a:bb |Mpush 21379
|  -  |528516|ROUTE| Et49/1             |1020 |103453  | c0:14:b8:21:ca:6e |Mpush 20024
|  -  |528517|ROUTE| Et47               |1016 |103429  | 2c:dd:e9:96:3a:bb |Mpush 20024
|  -  |528518|ROUTE| Et49/1             |1020 |103456  | c0:14:b8:21:ca:6e |Mpush 20005
|  -  |528519|ROUTE| Et47               |1016 |103439  | 2c:dd:e9:96:3a:bb |Mpush 20005
|  -  |528520|ROUTE| Et47               |1016 |103427  | 2c:dd:e9:96:3a:bb |   -   
|  -  |528554|ROUTE| Et49/1             |1020 |103493  | c0:14:b8:21:ca:6e |Mpush 21105
|  -  |528555|ROUTE| Et47               |1016 |103433  | 2c:dd:e9:96:3a:bb |Mpush 21105
|  -  |528556|ROUTE| Et49/1             |1020 |103428  | c0:14:b8:21:ca:6e |   -   
|  -  |528558|ROUTE| Et49/1             |1020 |103428  | c0:14:b8:21:ca:6e |   -   
|  -  |528560|ROUTE| Et49/1             |1020 |103455  | c0:14:b8:21:ca:6e |Mpush 21455
|  -  |528561|ROUTE| Et47               |1016 |103443  | 2c:dd:e9:96:3a:bb |Mpush 21455
|  -  |528562|ROUTE| Et49/1             |1020 |103449  | c0:14:b8:21:ca:6e |Mpush 20019
|  -  |528563|ROUTE| Et47               |1016 |103438  | 2c:dd:e9:96:3a:bb |Mpush 20019
|  -  |528564|ROUTE| Et49/1             |1020 |103444  | c0:14:b8:21:ca:6e |Mpush 21279
|  -  |528565|ROUTE| Et47               |1016 |103425  | 2c:dd:e9:96:3a:bb |Mpush 21279
|  -  |528570|ROUTE| Et7                |1021 |103421  | 30:c5:07:1f:33:0f |   -   
|  -  |528572|ROUTE| Et49/1             |1020 |103434  | c0:14:b8:21:ca:6e |Mpush 21555
|  -  |528573|ROUTE| Et47               |1016 |103436  | 2c:dd:e9:96:3a:bb |Mpush 21555
|  -  |528574|ROUTE| Et7                |1021 |103421  | 30:c5:07:1f:33:0f |   -   
|  -  |528576|ROUTE| Et49/1             |1020 |103509  | c0:14:b8:21:ca:6e |   -   
|  -  |528577|ROUTE| Et47               |1016 |103510  | 2c:dd:e9:96:3a:bb |   -   
|  -  |528578|ROUTE| Et5                |1019 |103426  | 00:14:01:00:00:02 |   -   
|  -  |528580|ROUTE| Et47               |1016 |103427  | 2c:dd:e9:96:3a:bb |   -   
|  -  |528582|ROUTE| Et47               |1016 |103427  | 2c:dd:e9:96:3a:bb |   -   
|  -  |528584|ROUTE| Et47               |1016 |103427  | 2c:dd:e9:96:3a:bb |   -   
|  -  |528586|ROUTE| Et7                |1021 |103487  | 30:c5:07:1f:33:0f |Mpush 21355
|  -  |528587|ROUTE| Et49/1             |1020 |103489  | c0:14:b8:21:ca:6e |Mpush 21355
|  -  |528588|ROUTE| Et7                |1021 |103490  | 30:c5:07:1f:33:0f |   -   
|  -  |528589|ROUTE| Et49/1             |1020 |103492  | c0:14:b8:21:ca:6e |Mpush 21032
|  -  |528590|ROUTE| Et7                |1021 |103452  | 30:c5:07:1f:33:0f |   -   
|  -  |528591|ROUTE| Et49/1             |1020 |103454  | c0:14:b8:21:ca:6e |Mpush 20032
|  -  |528596|ROUTE| Et47               |1016 |103430  | 2c:dd:e9:96:3a:bb |   -   
|  -  |528597|ROUTE| Et49/1             |1020 |103431  | c0:14:b8:21:ca:6e |Mpush 20172
|  -  |528598|ROUTE| Et7                |1021 |103421  | 30:c5:07:1f:33:0f |   -   
|  -  |528600|ROUTE| Et49/1             |1020 |103488  | c0:14:b8:21:ca:6e |Mpush 21124
|  -  |528601|ROUTE| Et47               |1016 |103432  | 2c:dd:e9:96:3a:bb |Mpush 21124
|  -  |528602|ROUTE| Et7                |1021 |103424  | 30:c5:07:1f:33:0f |   -   
|  -  |528603|ROUTE| Et49/1             |1020 |103435  | c0:14:b8:21:ca:6e |Mpush 20032
|  -  |528604|ROUTE| Et49/1             |1020 |103513  | c0:14:b8:21:ca:6e |Mpush 21257
|  -  |528605|ROUTE| Et47               |1016 |103514  | 2c:dd:e9:96:3a:bb |Mpush 21257
|  -  |528608|ROUTE| Et7                |1021 |103475  | 30:c5:07:1f:33:0f |Mpush 21057
|  -  |528609|ROUTE| Et49/1             |1020 |103476  | c0:14:b8:21:ca:6e |Mpush 21057
|  -  |528610|ROUTE| Et7                |1021 |103477  | 30:c5:07:1f:33:0f |   -   
|  -  |528611|ROUTE| Et49/1             |1020 |103478  | c0:14:b8:21:ca:6e |Mpush 21032
|  -  |528612|ROUTE| Et7                |1021 |103485  | 30:c5:07:1f:33:0f |Mpush 21179
|  -  |528613|ROUTE| Et49/1             |1020 |103486  | c0:14:b8:21:ca:6e |Mpush 21179
|  -  |528614|ROUTE| Et47               |1016 |103501  | 2c:dd:e9:96:3a:bb |   -   
|  -  |528615|ROUTE| Et49/1             |1020 |103502  | c0:14:b8:21:ca:6e |Mpush 21372
|  -  |528646|ROUTE| Et49/1             |1020 |103428  | c0:14:b8:21:ca:6e |   -   

```

