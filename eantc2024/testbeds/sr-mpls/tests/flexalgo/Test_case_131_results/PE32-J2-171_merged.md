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

Uptime: 1 day, 1 hour and 21 minutes
Total memory: 65734516 kB
Free memory: 61686088 kB

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
Interface        IP Address           Status    Protocol          MTU   Owner  
---------------- -------------------- --------- ------------- --------- -------
Ethernet1        20.170.171.171/24    down      down             1500          
Ethernet5.128    20.111.171.171/24    up        up               1500          
Ethernet5.129    20.111.171.171/24    up        up               1500          
Ethernet5.130    20.111.171.171/24    up        up               1500          
Ethernet5.131    20.111.171.171/24    up        up               1500          
Ethernet24       20.149.171.171/24    up        up               1500          
Ethernet25       20.171.179.171/24    down      down             1500          
Ethernet46       20.155.171.171/24    up        up               1500          
Loopback0        10.0.0.171/32        up        up              65535          
Management1      192.168.20.171/23    up        up               1500          

```

## show interfaces counters rates | nz

```text
Port      Name             Intvl  In Mbps      %  In Kpps Out Mbps      %
Et5                         0:01     11.1   0.1%        1     11.1   0.1%
Et24      Cisco_Spine_349   0:01      4.4   0.0%        0      4.4   0.0%
Et46                        0:01      6.6   0.1%        0      6.7   0.1%

Port      Out Kpps
Et5              1
```

## show isis neighbors

```text
 
Instance  VRF      System Id        Type Interface          SNPA              State Hold time   Circuit Id          
IGP       default  h49-N540-24Q8L2DD L2   Ethernet24         P2P               UP    23          00                  
IGP       default  h55-8201-24H8FH  L2   Ethernet46         P2P               UP    21          00                  
```

## show isis database detail

```text
Legend:
H - hostname conflict
U - node unreachable

IS-IS Instance: IGP VRF: default
  IS-IS Level 2 Link State Database
    LSPID                   Seq Num  Cksum  Life Length IS  Received LSPID        Flags
    h3c_19_CR16010E-F.00-00      1106  55936  1168    367 L2  0000.0000.0019.00-00  <>
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
    eantc-jcnr2.00-00           549  17577   539    229 L2  0000.0000.0020.00-00  <>
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
    12502-1.00-00              7434  54877   705    482 L2  0000.0000.0024.00-00  <>
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
    Ribbon-32.00-00             205  58363   661    109 L2  0000.0000.0032.00-00  <>
      NLPID: 0xCC(IPv4)
      Area addresses: 49.0001
      Router Capabilities: Router Id: 10.0.0.32 Flags: []
        SR Local Block:
          SRLB Base: 16 Range: 15344
        Maximum SID depth:
          Base MPLS imposition (MSD type 1):  10
        SR Capability: Flags: [I]
          SRGB Base: 20000 Range: 2000
        Algorithms:  0, 128, 129, 130
        Flex Algo: Algorithm: 128 Metric: Min Unidirectional Delay Metric (1) Calc: SPF (0) Prio: 10
        Flex Algo: Algorithm: 129 Metric: TE Metric (2) Calc: SPF (0) Prio: 10
        Flex Algo: Algorithm: 130 Metric: IGP Metric (0) Calc: SPF (0) Prio: 10
          Exclude admin groups: 1
      Unsupported TLV: Type: 14 Length: 2
    Ribbon-32.00-01             167  20558   656     38 L2  0000.0000.0032.00-01  <>
      Hostname: Ribbon-32
    Ribbon-32.00-02             825  52368  1199    245 L2  0000.0000.0032.00-02  <>
      Interface address: 10.0.0.32
      Interface address: 20.32.149.32
      Interface address: 20.32.211.32
      IS Neighbor          : h49-N540-24Q8L2DD.00 Metric: 10
        IPv4 Neighbor Address: 20.32.149.149
        IPv4 Interface Address: 20.32.149.32
        Adj-sid: 756646 flags: [L V] weight: 0x0
        Adj-sid: 756647 flags: [L V B] weight: 0x0
      Reachability         : 10.0.0.32/32 Metric: 0 Type: 1 Up
        SR Prefix-SID: 32 Flags: [N] Algorithm: 0
        SR Prefix-SID: 1032 Flags: [N] Algorithm: 128
        SR Prefix-SID: 1132 Flags: [N] Algorithm: 129
        SR Prefix-SID: 1232 Flags: [N] Algorithm: 130
      Reachability         : 20.32.149.0/24 Metric: 10 Type: 1 Up
      Reachability         : 20.32.211.0/24 Metric: 10 Type: 1 Up
    huawei_34_NetEngine_8000_F8.00-00       394  26013  1094    281 L2  0000.0000.0254.00-00  <>
      NLPID: 0xCC(IPv4)
      Hostname: huawei_34_NetEngine_8000_F8
      Area addresses: 49
      Interface address: 10.0.0.254
      Interface address: 20.149.254.254
      IS Neighbor          : h49-N540-24Q8L2DD.00 Metric: 10
        IPv4 Neighbor Address: 20.149.254.149
        IPv4 Interface Address: 20.149.254.254
        Adj-sid: 48032 flags: [L V] weight: 0x0
      Reachability         : 10.0.0.254/32 Metric: 0 Type: 1 Up
        SR Prefix-SID: 254 Flags: [N] Algorithm: 0
        SR Prefix-SID: 1254 Flags: [N] Algorithm: 128
        SR Prefix-SID: 1354 Flags: [N] Algorithm: 129
        SR Prefix-SID: 1454 Flags: [N] Algorithm: 130
        SR Prefix-SID: 1554 Flags: [N] Algorithm: 131
      Reachability         : 20.149.254.0/24 Metric: 10 Type: 1 Up
      Router Capabilities: Router Id: 10.0.0.254 Flags: []
        Flex Algo: Algorithm: 128 Metric: Min Unidirectional Delay Metric (1) Calc: SPF (0) Prio: 128
          Flags: [M] 0x80
        Flex Algo: Algorithm: 129 Metric: TE Metric (2) Calc: SPF (0) Prio: 128
          Flags: [M] 0x80
        Flex Algo: Algorithm: 130 Metric: IGP Metric (0) Calc: SPF (0) Prio: 128
          Exclude admin groups: 1
          Flags: [M] 0x80
        Flex Algo: Algorithm: 131 Metric: IGP Metric (0) Calc: SPF (0) Prio: 128
          Exclude admin groups: 127
          Flags: [M] 0x80
      Router Capabilities: Router Id: 10.0.0.254 Flags: []
        Maximum SID depth:
          Base MPLS imposition (MSD type 1):  10
        SR Capability: Flags: [I]
          SRGB Base: 20000 Range: 2000
        Algorithms:  0, 128, 129, 130, 131
    h49-N540-24Q8L2DD.00-00       422  35968   658   1328 L2  0000.0000.0349.00-00  <>
      NLPID: 0xCC(IPv4)
      Hostname: h49-N540-24Q8L2DD
      Area addresses: 49
      Interface address: 10.0.1.49
      IS Neighbor          : h3c_19_CR16010E-F.00 Metric: 10
        IPv4 Neighbor Address: 20.19.149.19
        IPv4 Interface Address: 20.19.149.149
        Adj-sid: 24005 flags: [L V] weight: 0x0
      IS Neighbor          : NOKIA-SR2-57.00     Metric: 10
        IPv4 Neighbor Address: 20.57.149.57
        IPv4 Interface Address: 20.57.149.149
        Adj-sid: 24009 flags: [L V] weight: 0x0
      IS Neighbor          : 12502-1.00          Metric: 10
        IPv4 Neighbor Address: 20.24.149.24
        IPv4 Interface Address: 20.24.149.149
        Adj-sid: 24019 flags: [L V] weight: 0x0
      IS Neighbor          : PE31-J2-171.00      Metric: 10
        IPv4 Neighbor Address: 20.149.171.171
        IPv4 Interface Address: 20.149.171.149
        Adj-sid: 24011 flags: [L V] weight: 0x0
      IS Neighbor          : huawei_34_NetEngine_8000_F8.00 Metric: 10
        IPv4 Neighbor Address: 20.149.254.254
        IPv4 Interface Address: 20.149.254.149
        Adj-sid: 24001 flags: [L V] weight: 0x0
      IS Neighbor          : 3800.0000.4111.00   Metric: 10
        IPv4 Neighbor Address: 20.111.149.1
        IPv4 Interface Address: 20.111.149.149
        Adj-sid: 24015 flags: [L V] weight: 0x0
      IS Neighbor          : eantc-jcnr2.00      Metric: 10
        IPv4 Neighbor Address: 20.83.149.83
        IPv4 Interface Address: 20.83.149.149
        Adj-sid: 24021 flags: [L V] weight: 0x0
      IS Neighbor          : Ribbon-32.00        Metric: 10
        IPv4 Neighbor Address: 20.32.149.32
        IPv4 Interface Address: 20.32.149.149
        Adj-sid: 24003 flags: [L V] weight: 0x0
      IS Neighbor          : h55-8201-24H8FH.00  Metric: 10
        IPv4 Neighbor Address: 20.149.155.155
        IPv4 Interface Address: 20.149.155.149
        Adj-sid: 24013 flags: [L V] weight: 0x0
      IS Neighbor          : 0010.0010.0005.00   Metric: 10
        IPv4 Neighbor Address: 20.5.149.5
        IPv4 Interface Address: 20.5.149.149
        Adj-sid: 24007 flags: [L V] weight: 0x0
      Reachability         : 10.0.1.49/32 Metric: 0 Type: 1 Up
        SR Prefix-SID: 349 Flags: [N] Algorithm: 0
        SR Prefix-SID: 1349 Flags: [N] Algorithm: 128
        SR Prefix-SID: 1449 Flags: [N] Algorithm: 129
        SR Prefix-SID: 1649 Flags: [N] Algorithm: 130
        SR Prefix-SID: 1749 Flags: [N] Algorithm: 132
      Reachability         : 20.5.149.0/24 Metric: 10 Type: 1 Up
      Reachability         : 20.19.149.0/24 Metric: 10 Type: 1 Up
      Reachability         : 20.24.149.0/24 Metric: 10 Type: 1 Up
      Reachability         : 20.32.149.0/24 Metric: 10 Type: 1 Up
      Reachability         : 20.47.149.0/24 Metric: 10 Type: 1 Up
      Reachability         : 20.57.149.0/24 Metric: 10 Type: 1 Up
      Reachability         : 20.83.149.0/24 Metric: 10 Type: 1 Up
      Reachability         : 20.111.149.0/24 Metric: 10 Type: 1 Up
      Reachability         : 20.149.155.0/24 Metric: 10 Type: 1 Up
      Reachability         : 20.149.171.0/24 Metric: 10 Type: 1 Up
      Reachability         : 20.149.254.0/24 Metric: 10 Type: 1 Up
      Router Capabilities: Router Id: 10.0.1.49 Flags: []
        SR Local Block:
          SRLB Base: 15000 Range: 1000
        Maximum SID depth:
          Base MPLS imposition (MSD type 1):  12
        SR Capability: Flags: [I]
          SRGB Base: 20000 Range: 2000
        Algorithms:  0, 1, 128, 129, 130, 131, 132
        Flex Algo: Algorithm: 128 Metric: Min Unidirectional Delay Metric (1) Calc: SPF (0) Prio: 255
        Flex Algo: Algorithm: 129 Metric: TE Metric (2) Calc: SPF (0) Prio: 255
        Flex Algo: Algorithm: 130 Metric: IGP Metric (0) Calc: SPF (0) Prio: 255
          Exclude admin groups: 1
        Flex Algo: Algorithm: 131 Metric: IGP Metric (0) Calc: SPF (0) Prio: 255
          Exclude admin groups: 127
        Flex Algo: Algorithm: 132 Metric: IGP Metric (0) Calc: SPF (0) Prio: 255
          Exclude admin groups: 255
      Unsupported TLV: Type: 14 Length: 2
    h55-8201-24H8FH.00-00       269  59716   797    720 L2  0000.0000.0355.00-00  <>
      NLPID: 0xCC(IPv4)
      Hostname: h55-8201-24H8FH
      Area addresses: 49
      Interface address: 10.0.1.55
      IS Neighbor          : juniper_379_MX304.00 Metric: 10
        IPv4 Neighbor Address: 20.155.179.179
        IPv4 Interface Address: 20.155.179.155
        Adj-sid: 24003 flags: [L V] weight: 0x0
      IS Neighbor          : NOKIA-SR2-57.00     Metric: 10
        IPv4 Neighbor Address: 20.57.155.57
        IPv4 Interface Address: 20.57.155.155
        Adj-sid: 24008 flags: [L V] weight: 0x0
      IS Neighbor          : h49-N540-24Q8L2DD.00 Metric: 10
        IPv4 Neighbor Address: 20.149.155.149
        IPv4 Interface Address: 20.149.155.155
        Adj-sid: 24001 flags: [L V] weight: 0x0
      IS Neighbor          : PE31-J2-171.00      Metric: 10
        IPv4 Neighbor Address: 20.155.171.171
        IPv4 Interface Address: 20.155.171.155
        Adj-sid: 24006 flags: [L V] weight: 0x0
      Reachability         : 10.0.1.55/32 Metric: 0 Type: 1 Up
        SR Prefix-SID: 355 Flags: [N] Algorithm: 0
        SR Prefix-SID: 1355 Flags: [N] Algorithm: 128
        SR Prefix-SID: 1455 Flags: [N] Algorithm: 129
        SR Prefix-SID: 1555 Flags: [N] Algorithm: 130
        SR Prefix-SID: 1655 Flags: [N] Algorithm: 131
        SR Prefix-SID: 1755 Flags: [N] Algorithm: 132
      Reachability         : 20.57.155.0/24 Metric: 10 Type: 1 Up
      Reachability         : 20.149.155.0/24 Metric: 10 Type: 1 Up
      Reachability         : 20.155.171.0/24 Metric: 10 Type: 1 Up
      Reachability         : 20.155.179.0/24 Metric: 10 Type: 1 Up
      Router Capabilities: Router Id: 10.0.1.55 Flags: []
        SR Local Block:
          SRLB Base: 15000 Range: 1000
        Maximum SID depth:
          Base MPLS imposition (MSD type 1):  8
        SR Capability: Flags: [I]
          SRGB Base: 20000 Range: 2000
        Algorithms:  0, 1, 128, 129, 130, 131, 132
        Flex Algo: Algorithm: 128 Metric: Min Unidirectional Delay Metric (1) Calc: SPF (0) Prio: 10
        Flex Algo: Algorithm: 129 Metric: TE Metric (2) Calc: SPF (0) Prio: 10
        Flex Algo: Algorithm: 130 Metric: IGP Metric (0) Calc: SPF (0) Prio: 10
          Exclude admin groups: 1
        Flex Algo: Algorithm: 131 Metric: IGP Metric (0) Calc: SPF (0) Prio: 10
          Exclude admin groups: 127
        Flex Algo: Algorithm: 132 Metric: IGP Metric (0) Calc: SPF (0) Prio: 10
          Exclude admin groups: 255
      Unsupported TLV: Type: 14 Length: 2
    juniper_379_MX304.00-00      1020  51716  1167    368 L2  0000.0001.7900.00-00  <>
      NLPID: 0xCC(IPv4) 0x8E(IPv6)
      Hostname: juniper_379_MX304
      Area addresses: 49.0001.00
      Interface address: 10.0.0.179
      IS Neighbor          : h55-8201-24H8FH.00  Metric: 10
        IPv4 Neighbor Address: 20.155.179.155
        IPv4 Interface Address: 20.155.179.179
        Adj-sid: 21 flags: [L V B] weight: 0x0
      IS Neighbor          : NOKIA-SR2-57.00     Metric: 10
        IPv4 Neighbor Address: 20.57.179.57
        IPv4 Interface Address: 20.57.179.179
        Adj-sid: 20 flags: [L V B] weight: 0x0
      Reachability         : 10.0.0.179/32 Metric: 0 Type: 1 Up
        SR Prefix-SID: 379 Flags: [N] Algorithm: 0
        SR Prefix-SID: 1379 Flags: [N] Algorithm: 130
        SR Prefix-SID: 1279 Flags: [N] Algorithm: 129
        SR Prefix-SID: 1179 Flags: [N] Algorithm: 128
      Reachability         : 20.155.179.0/24 Metric: 10 Type: 1 Up
      Reachability         : 20.57.179.0/24 Metric: 10 Type: 1 Up
      Router Capabilities: Router Id: 10.0.0.179 Flags: []
        Maximum SID depth:
          Base MPLS imposition (MSD type 1):  4
        SR Capability: Flags: [I V]
          SRGB Base: 20000 Range: 2000
        Algorithms:  0, 1, 128, 129, 130
        Flex Algo: Algorithm: 130 Metric: IGP Metric (0) Calc: SPF (0) Prio: 0
          Exclude admin groups: 1
        Flex Algo: Algorithm: 129 Metric: TE Metric (2) Calc: SPF (0) Prio: 0
        Flex Algo: Algorithm: 128 Metric: Min Unidirectional Delay Metric (1) Calc: SPF (0) Prio: 0
      Unsupported TLV: Type: 14 Length: 2
    0010.0010.0005.00-00        124  34965   324    303 L2  0010.0010.0005.00-00  <>
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
    NOKIA-SR2-57.00-00         8603  65307  1199    758 L2  0100.0000.0057.00-00  <>
      NLPID: 0xCC(IPv4) 0x8E(IPv6)
      Hostname: NOKIA-SR2-57
      Area addresses: 49.0000.0000.0057.00
      Interface address: 10.0.0.57
      Interface address: 20.57.59.57
      Interface address: 20.57.149.57
      Interface address: 20.57.155.57
      Interface address: 20.57.179.57
      Interface address: 20.57.211.57
      Interface address: 2002::57
      IS Neighbor (Narrow metrics, unsupported): h49-N540-24Q8L2DD.00 Metric: 10
      IS Neighbor (Narrow metrics, unsupported): h55-8201-24H8FH.00  Metric: 10
      IS Neighbor (Narrow metrics, unsupported): juniper_379_MX304.00 Metric: 10
      IS Neighbor          : h49-N540-24Q8L2DD.00 Metric: 10
        IPv4 Neighbor Address: 20.57.149.149
        IPv4 Interface Address: 20.57.149.57
        Adj-sid: 30149 flags: [L V B] weight: 0x0
      IS Neighbor          : h55-8201-24H8FH.00  Metric: 10
        IPv4 Neighbor Address: 20.57.155.155
        IPv4 Interface Address: 20.57.155.57
        Adj-sid: 30155 flags: [L V B] weight: 0x0
      IS Neighbor          : juniper_379_MX304.00 Metric: 10
        IPv4 Neighbor Address: 20.57.179.179
        IPv4 Interface Address: 20.57.179.57
        Adj-sid: 30179 flags: [L V B] weight: 0x0
      Reachability (Narrow metrics, unsupported): 10.0.0.57/32 Metric: 0 Type: 1
      Reachability (Narrow metrics, unsupported): 20.57.59.0/24 Metric: 10 Type: 1
      Reachability (Narrow metrics, unsupported): 20.57.149.0/24 Metric: 10 Type: 1
      Reachability (Narrow metrics, unsupported): 20.57.155.0/24 Metric: 10 Type: 1
      Reachability (Narrow metrics, unsupported): 20.57.179.0/24 Metric: 10 Type: 1
      Reachability (Narrow metrics, unsupported): 20.57.211.0/24 Metric: 10 Type: 1
      Reachability         : 10.0.0.57/32 Metric: 0 Type: 1 Up
        SR Prefix-SID: 57 Flags: [N P] Algorithm: 0
        SR Prefix-SID: 1057 Flags: [N P] Algorithm: 128
        SR Prefix-SID: 1157 Flags: [N P] Algorithm: 129
        SR Prefix-SID: 1257 Flags: [N P] Algorithm: 130
        SR Prefix-SID: 1357 Flags: [N P] Algorithm: 131
        SR Prefix-SID: 1457 Flags: [N P] Algorithm: 132
      Reachability         : 20.57.59.0/24 Metric: 10 Type: 1 Up
      Reachability         : 20.57.149.0/24 Metric: 10 Type: 1 Up
      Reachability         : 20.57.155.0/24 Metric: 10 Type: 1 Up
      Reachability         : 20.57.179.0/24 Metric: 10 Type: 1 Up
      Reachability         : 20.57.211.0/24 Metric: 10 Type: 1 Up
      Reachability          : 2002::57/128 Metric: 0 Type: 1 Up
      Router Capabilities: Router Id: 10.0.0.57 Flags: []
        Maximum SID depth:
          Base MPLS imposition (MSD type 1):  12
        SR Capability: Flags: [I V]
          SRGB Base: 20000 Range: 2000
        Algorithms:  0, 128, 129, 130, 131, 132
        Flex Algo: Algorithm: 128 Metric: Min Unidirectional Delay Metric (1) Calc: SPF (0) Prio: 100
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
    PE31-J2-171.00-00           276  43971  1050    349 L2  0100.0000.0171.00-00  <>
      LSP generation remaining wait time: 0 ms
      Time remaining until refresh: 750 s
      NLPID: 0xCC(IPv4)
      Hostname: PE31-J2-171
      Area addresses: 49.0000
      Interface address: 20.155.171.171
      Interface address: 20.149.171.171
      Interface address: 10.0.0.171
      IS Neighbor          : h49-N540-24Q8L2DD.00 Metric: 10
        IPv4 Neighbor Address: 20.149.171.149
        IPv4 Interface Address: 20.149.171.171
        Adj-sid: 362144 flags: [L V] weight: 0x0
      IS Neighbor          : h55-8201-24H8FH.00  Metric: 10
        IPv4 Neighbor Address: 20.155.171.155
        IPv4 Interface Address: 20.155.171.171
        Adj-sid: 362146 flags: [L V] weight: 0x0
      Reachability         : 20.155.171.0/24 Metric: 10 Type: 1 Up
      Reachability         : 10.0.0.171/32 Metric: 0 Type: 1 Up
        SR Prefix-SID: 171 Flags: [N] Algorithm: 0
        SR Prefix-SID: 1171 Flags: [N] Algorithm: 128
        SR Prefix-SID: 1271 Flags: [N] Algorithm: 129
        SR Prefix-SID: 1371 Flags: [N] Algorithm: 130
        SR Prefix-SID: 1471 Flags: [N] Algorithm: 131
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
          Exclude admin groups: 1
        Flex Algo: Algorithm: 129 Metric: TE Metric (2) Calc: SPF (0) Prio: 237
        Flex Algo: Algorithm: 128 Metric: Min Unidirectional Delay Metric (1) Calc: SPF (0) Prio: 237
    3800.0000.4111.00-00         34  33556  1168    260 L2  3800.0000.4111.00-00  <DefaultAtt>
      NLPID: 0xCC(IPv4) 0x8E(IPv6) 0x81(CLNP)
      Area addresses: 49
      Interface address: 20.111.149.1
      IS Neighbor          : h49-N540-24Q8L2DD.00 Metric: 10
        IPv4 Neighbor Address: 20.111.149.149
        IPv4 Interface Address: 20.111.149.1
      Reachability         : 20.111.149.0/24 Metric: 10 Type: 1 Up
      Reachability         : 100.0.1.111/32 Metric: 0 Type: 1 Up
        SR Prefix-SID: 111 Flags: [N] Algorithm: 0
        SR Prefix-SID: 1111 Flags: [N] Algorithm: 128
        SR Prefix-SID: 1211 Flags: [N] Algorithm: 129
        SR Prefix-SID: 1311 Flags: [N] Algorithm: 130
        SR Prefix-SID: 1411 Flags: [N] Algorithm: 131
      Router Capabilities: Router Id: 100.0.1.111 Flags: []
        SR Capability: Flags: [I V]
          SRGB Base: 20000 Range: 2000
        Algorithms:  0, 128, 129, 130, 131
```

## show isis database traffic-engineering

```text
Legend:
H - hostname conflict
U - node unreachable

IS-IS Instance: IGP VRF: default
  IS-IS Level 2 Link State Database
    LSPID                   Seq Num  Cksum  Life Length IS  Received LSPID        Flags
    h3c_19_CR16010E-F.00-00      1106  55936  1168    367 L2  0000.0000.0019.00-00  <>
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
    eantc-jcnr2.00-00           549  17577   539    229 L2  0000.0000.0020.00-00  <>
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
    12502-1.00-00              7434  54877   705    482 L2  0000.0000.0024.00-00  <>
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
    Ribbon-32.00-00             205  58363   661    109 L2  0000.0000.0032.00-00  <>
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
        Algorithms:  0, 128, 129, 130
        Flex Algo: Algorithm: 128 Metric: Min Unidirectional Delay Metric (1) Calc: SPF (0) Prio: 10
        Flex Algo: Algorithm: 129 Metric: TE Metric (2) Calc: SPF (0) Prio: 10
        Flex Algo: Algorithm: 130 Metric: IGP Metric (0) Calc: SPF (0) Prio: 10
          Exclude admin groups: 1
      Unsupported TLV: Type: 14 Length: 2
    Ribbon-32.00-01             167  20558   656     38 L2  0000.0000.0032.00-01  <>
      Hostname: Ribbon-32
    Ribbon-32.00-02             825  52368  1199    245 L2  0000.0000.0032.00-02  <>
      Interface address: 10.0.0.32
      Interface address: 20.32.149.32
      Interface address: 20.32.211.32
      IS Neighbor          : h49-N540-24Q8L2DD.00 Metric: 10
        IPv4 Neighbor Address: 20.32.149.149
        IPv4 Interface Address: 20.32.149.32
        Adj-sid: 756646 flags: [L V] weight: 0x0
        Adj-sid: 756647 flags: [L V B] weight: 0x0
        TE default metric: 12
        Maximum link BW: 1.00 Gbps
        Maximum reservable link BW: 1.00 Gbps
        Unreserved BW:
            TE class 0: 1.00 Gbps	TE class 1: 1.00 Gbps	TE class 2: 1.00 Gbps
            TE class 3: 1.00 Gbps	TE class 4: 1.00 Gbps	TE class 5: 1.00 Gbps
            TE class 6: 1.00 Gbps	TE class 7: 1.00 Gbps
        Min/Max unidirectional link delay: 11/11 us
        Application Specific Link Attributes:
          Standard applications: Flex-Algo
            TE default metric: 12
            Min/Max unidirectional link delay: 11/11 us
      Reachability         : 10.0.0.32/32 Metric: 0 Type: 1 Up
        SR Prefix-SID: 32 Flags: [N] Algorithm: 0
        SR Prefix-SID: 1032 Flags: [N] Algorithm: 128
        SR Prefix-SID: 1132 Flags: [N] Algorithm: 129
        SR Prefix-SID: 1232 Flags: [N] Algorithm: 130
      Reachability         : 20.32.149.0/24 Metric: 10 Type: 1 Up
      Reachability         : 20.32.211.0/24 Metric: 10 Type: 1 Up
    huawei_34_NetEngine_8000_F8.00-00       394  26013  1094    281 L2  0000.0000.0254.00-00  <>
      NLPID: 0xCC(IPv4)
      Hostname: huawei_34_NetEngine_8000_F8
      Area addresses: 49
      Interface address: 10.0.0.254
      Interface address: 20.149.254.254
      IS Neighbor          : h49-N540-24Q8L2DD.00 Metric: 10
        IPv4 Neighbor Address: 20.149.254.149
        IPv4 Interface Address: 20.149.254.254
        Adj-sid: 48032 flags: [L V] weight: 0x0
        Application Specific Link Attributes:
          Standard applications: Flex-Algo
            TE default metric: 12
            Min/Max unidirectional link delay: 11/11 us
      Reachability         : 10.0.0.254/32 Metric: 0 Type: 1 Up
        SR Prefix-SID: 254 Flags: [N] Algorithm: 0
        SR Prefix-SID: 1254 Flags: [N] Algorithm: 128
        SR Prefix-SID: 1354 Flags: [N] Algorithm: 129
        SR Prefix-SID: 1454 Flags: [N] Algorithm: 130
        SR Prefix-SID: 1554 Flags: [N] Algorithm: 131
      Reachability         : 20.149.254.0/24 Metric: 10 Type: 1 Up
      Router Capabilities: Router Id: 10.0.0.254 Flags: []
        Flex Algo: Algorithm: 128 Metric: Min Unidirectional Delay Metric (1) Calc: SPF (0) Prio: 128
          Flags: [M] 0x80
        Flex Algo: Algorithm: 129 Metric: TE Metric (2) Calc: SPF (0) Prio: 128
          Flags: [M] 0x80
        Flex Algo: Algorithm: 130 Metric: IGP Metric (0) Calc: SPF (0) Prio: 128
          Exclude admin groups: 1
          Flags: [M] 0x80
        Flex Algo: Algorithm: 131 Metric: IGP Metric (0) Calc: SPF (0) Prio: 128
          Exclude admin groups: 127
          Flags: [M] 0x80
      Router Capabilities: Router Id: 10.0.0.254 Flags: []
        Maximum SID depth:
          Base MPLS imposition (MSD type 1):  10
        SR Capability: Flags: [I]
          SRGB Base: 20000 Range: 2000
        Algorithms:  0, 128, 129, 130, 131
    h49-N540-24Q8L2DD.00-00       422  35968   657   1328 L2  0000.0000.0349.00-00  <>
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
            Min/Max unidirectional link delay: 11/11 us
      IS Neighbor          : PE31-J2-171.00      Metric: 10
        IPv4 Neighbor Address: 20.149.171.171
        IPv4 Interface Address: 20.149.171.149
        Adj-sid: 24011 flags: [L V] weight: 0x0
        Maximum link BW: 10.00 Gbps
        Min/Max unidirectional link delay: 1/1 us
        Average unidirectional link delay: 1 us
        Application Specific Link Attributes:
          Standard applications: Flex-Algo
          User-defined applications: APP3
            Administrative group (Color): 127
            TE default metric: 12
            Min/Max unidirectional link delay: 1/1 us
      IS Neighbor          : huawei_34_NetEngine_8000_F8.00 Metric: 10
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
            Min/Max unidirectional link delay: 11/11 us
      IS Neighbor          : 3800.0000.4111.00   Metric: 10
        IPv4 Neighbor Address: 20.111.149.1
        IPv4 Interface Address: 20.111.149.149
        Adj-sid: 24015 flags: [L V] weight: 0x0
        Maximum link BW: 10.00 Gbps
        Min/Max unidirectional link delay: 11/11 us
        Average unidirectional link delay: 11 us
        Application Specific Link Attributes:
          Standard applications: Flex-Algo
          User-defined applications: APP3
            TE default metric: 12
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
            Min/Max unidirectional link delay: 11/11 us
      IS Neighbor          : Ribbon-32.00        Metric: 10
        IPv4 Neighbor Address: 20.32.149.32
        IPv4 Interface Address: 20.32.149.149
        Adj-sid: 24003 flags: [L V] weight: 0x0
        Maximum link BW: 1.00 Gbps
        Min/Max unidirectional link delay: 11/11 us
        Average unidirectional link delay: 11 us
        Application Specific Link Attributes:
          Standard applications: Flex-Algo
          User-defined applications: APP3
            TE default metric: 12
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
            Min/Max unidirectional link delay: 11/11 us
      Reachability         : 10.0.1.49/32 Metric: 0 Type: 1 Up
        SR Prefix-SID: 349 Flags: [N] Algorithm: 0
        SR Prefix-SID: 1349 Flags: [N] Algorithm: 128
        SR Prefix-SID: 1449 Flags: [N] Algorithm: 129
        SR Prefix-SID: 1649 Flags: [N] Algorithm: 130
        SR Prefix-SID: 1749 Flags: [N] Algorithm: 132
      Reachability         : 20.5.149.0/24 Metric: 10 Type: 1 Up
      Reachability         : 20.19.149.0/24 Metric: 10 Type: 1 Up
      Reachability         : 20.24.149.0/24 Metric: 10 Type: 1 Up
      Reachability         : 20.32.149.0/24 Metric: 10 Type: 1 Up
      Reachability         : 20.47.149.0/24 Metric: 10 Type: 1 Up
      Reachability         : 20.57.149.0/24 Metric: 10 Type: 1 Up
      Reachability         : 20.83.149.0/24 Metric: 10 Type: 1 Up
      Reachability         : 20.111.149.0/24 Metric: 10 Type: 1 Up
      Reachability         : 20.149.155.0/24 Metric: 10 Type: 1 Up
      Reachability         : 20.149.171.0/24 Metric: 10 Type: 1 Up
      Reachability         : 20.149.254.0/24 Metric: 10 Type: 1 Up
      Router Capabilities: Router Id: 10.0.1.49 Flags: []
        SR Local Block:
          SRLB Base: 15000 Range: 1000
        Maximum SID depth:
          Base MPLS imposition (MSD type 1):  12
        SR Capability: Flags: [I]
          SRGB Base: 20000 Range: 2000
        Algorithms:  0, 1, 128, 129, 130, 131, 132
        Flex Algo: Algorithm: 128 Metric: Min Unidirectional Delay Metric (1) Calc: SPF (0) Prio: 255
        Flex Algo: Algorithm: 129 Metric: TE Metric (2) Calc: SPF (0) Prio: 255
        Flex Algo: Algorithm: 130 Metric: IGP Metric (0) Calc: SPF (0) Prio: 255
          Exclude admin groups: 1
        Flex Algo: Algorithm: 131 Metric: IGP Metric (0) Calc: SPF (0) Prio: 255
          Exclude admin groups: 127
        Flex Algo: Algorithm: 132 Metric: IGP Metric (0) Calc: SPF (0) Prio: 255
          Exclude admin groups: 255
      Unsupported TLV: Type: 14 Length: 2
    h55-8201-24H8FH.00-00       269  59716   797    720 L2  0000.0000.0355.00-00  <>
      NLPID: 0xCC(IPv4)
      Hostname: h55-8201-24H8FH
      TE IPv4 router ID: 10.0.1.55
      Area addresses: 49
      Interface address: 10.0.1.55
      IS Neighbor          : juniper_379_MX304.00 Metric: 10
        IPv4 Neighbor Address: 20.155.179.179
        IPv4 Interface Address: 20.155.179.155
        Adj-sid: 24003 flags: [L V] weight: 0x0
        Maximum link BW: 100.00 Gbps
        Min/Max unidirectional link delay: 11/11 us
        Average unidirectional link delay: 11 us
        Application Specific Link Attributes:
          Standard applications: Flex-Algo
          User-defined applications: APP3
            Administrative group (Color): 1
            TE default metric: 12
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
            Min/Max unidirectional link delay: 6/10 us
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
            Min/Max unidirectional link delay: 2/2 us
      IS Neighbor          : PE31-J2-171.00      Metric: 10
        IPv4 Neighbor Address: 20.155.171.171
        IPv4 Interface Address: 20.155.171.155
        Adj-sid: 24006 flags: [L V] weight: 0x0
        Maximum link BW: 10.00 Gbps
        Min/Max unidirectional link delay: 1/1 us
        Average unidirectional link delay: 1 us
        Application Specific Link Attributes:
          Standard applications: Flex-Algo
          User-defined applications: APP3
            TE default metric: 12
            Min/Max unidirectional link delay: 1/1 us
      Reachability         : 10.0.1.55/32 Metric: 0 Type: 1 Up
        SR Prefix-SID: 355 Flags: [N] Algorithm: 0
        SR Prefix-SID: 1355 Flags: [N] Algorithm: 128
        SR Prefix-SID: 1455 Flags: [N] Algorithm: 129
        SR Prefix-SID: 1555 Flags: [N] Algorithm: 130
        SR Prefix-SID: 1655 Flags: [N] Algorithm: 131
        SR Prefix-SID: 1755 Flags: [N] Algorithm: 132
      Reachability         : 20.57.155.0/24 Metric: 10 Type: 1 Up
      Reachability         : 20.149.155.0/24 Metric: 10 Type: 1 Up
      Reachability         : 20.155.171.0/24 Metric: 10 Type: 1 Up
      Reachability         : 20.155.179.0/24 Metric: 10 Type: 1 Up
      Router Capabilities: Router Id: 10.0.1.55 Flags: []
        SR Local Block:
          SRLB Base: 15000 Range: 1000
        Maximum SID depth:
          Base MPLS imposition (MSD type 1):  8
        SR Capability: Flags: [I]
          SRGB Base: 20000 Range: 2000
        Algorithms:  0, 1, 128, 129, 130, 131, 132
        Flex Algo: Algorithm: 128 Metric: Min Unidirectional Delay Metric (1) Calc: SPF (0) Prio: 10
        Flex Algo: Algorithm: 129 Metric: TE Metric (2) Calc: SPF (0) Prio: 10
        Flex Algo: Algorithm: 130 Metric: IGP Metric (0) Calc: SPF (0) Prio: 10
          Exclude admin groups: 1
        Flex Algo: Algorithm: 131 Metric: IGP Metric (0) Calc: SPF (0) Prio: 10
          Exclude admin groups: 127
        Flex Algo: Algorithm: 132 Metric: IGP Metric (0) Calc: SPF (0) Prio: 10
          Exclude admin groups: 255
      Unsupported TLV: Type: 14 Length: 2
    juniper_379_MX304.00-00      1020  51716  1167    368 L2  0000.0001.7900.00-00  <>
      NLPID: 0xCC(IPv4) 0x8E(IPv6)
      Hostname: juniper_379_MX304
      TE IPv4 router ID: 10.0.0.179
      Area addresses: 49.0001.00
      Interface address: 10.0.0.179
      IS Neighbor          : h55-8201-24H8FH.00  Metric: 10
        IPv4 Neighbor Address: 20.155.179.155
        IPv4 Interface Address: 20.155.179.179
        Adj-sid: 21 flags: [L V B] weight: 0x0
        Min/Max unidirectional link delay: 827/1490 us
        Average unidirectional link delay: 1084 us
        Unidirectional link delay variation: 30774 us
        Application Specific Link Attributes:
          Standard applications: Flex-Algo
            Administrative group (Color): 1
            TE default metric: 12
            Min/Max unidirectional link delay: 827/1490 us
      IS Neighbor          : NOKIA-SR2-57.00     Metric: 10
        IPv4 Neighbor Address: 20.57.179.57
        IPv4 Interface Address: 20.57.179.179
        Adj-sid: 20 flags: [L V B] weight: 0x0
        Min/Max unidirectional link delay: 65/121 us
        Average unidirectional link delay: 81 us
        Unidirectional link delay variation: 61 us
        Application Specific Link Attributes:
          Standard applications: Flex-Algo
            TE default metric: 12
            Min/Max unidirectional link delay: 65/121 us
      Reachability         : 10.0.0.179/32 Metric: 0 Type: 1 Up
        SR Prefix-SID: 379 Flags: [N] Algorithm: 0
        SR Prefix-SID: 1379 Flags: [N] Algorithm: 130
        SR Prefix-SID: 1279 Flags: [N] Algorithm: 129
        SR Prefix-SID: 1179 Flags: [N] Algorithm: 128
      Reachability         : 20.155.179.0/24 Metric: 10 Type: 1 Up
      Reachability         : 20.57.179.0/24 Metric: 10 Type: 1 Up
      Router Capabilities: Router Id: 10.0.0.179 Flags: []
        Maximum SID depth:
          Base MPLS imposition (MSD type 1):  4
        SR Capability: Flags: [I V]
          SRGB Base: 20000 Range: 2000
        Algorithms:  0, 1, 128, 129, 130
        Flex Algo: Algorithm: 130 Metric: IGP Metric (0) Calc: SPF (0) Prio: 0
          Exclude admin groups: 1
        Flex Algo: Algorithm: 129 Metric: TE Metric (2) Calc: SPF (0) Prio: 0
        Flex Algo: Algorithm: 128 Metric: Min Unidirectional Delay Metric (1) Calc: SPF (0) Prio: 0
      Unsupported TLV: Type: 14 Length: 2
    0010.0010.0005.00-00        124  34965   324    303 L2  0010.0010.0005.00-00  <>
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
    NOKIA-SR2-57.00-00         8603  65307  1198    758 L2  0100.0000.0057.00-00  <>
      NLPID: 0xCC(IPv4) 0x8E(IPv6)
      Hostname: NOKIA-SR2-57
      TE IPv4 router ID: 10.0.0.57
      TE IPv6 router ID: 2002::57
      Area addresses: 49.0000.0000.0057.00
      Interface address: 10.0.0.57
      Interface address: 20.57.59.57
      Interface address: 20.57.149.57
      Interface address: 20.57.155.57
      Interface address: 20.57.179.57
      Interface address: 20.57.211.57
      Interface address: 2002::57
      IS Neighbor (Narrow metrics, unsupported): h49-N540-24Q8L2DD.00 Metric: 10
      IS Neighbor (Narrow metrics, unsupported): h55-8201-24H8FH.00  Metric: 10
      IS Neighbor (Narrow metrics, unsupported): juniper_379_MX304.00 Metric: 10
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
            Min/Max unidirectional link delay: 9/9 us
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
      Reachability (Narrow metrics, unsupported): 10.0.0.57/32 Metric: 0 Type: 1
      Reachability (Narrow metrics, unsupported): 20.57.59.0/24 Metric: 10 Type: 1
      Reachability (Narrow metrics, unsupported): 20.57.149.0/24 Metric: 10 Type: 1
      Reachability (Narrow metrics, unsupported): 20.57.155.0/24 Metric: 10 Type: 1
      Reachability (Narrow metrics, unsupported): 20.57.179.0/24 Metric: 10 Type: 1
      Reachability (Narrow metrics, unsupported): 20.57.211.0/24 Metric: 10 Type: 1
      Reachability         : 10.0.0.57/32 Metric: 0 Type: 1 Up
        SR Prefix-SID: 57 Flags: [N P] Algorithm: 0
        SR Prefix-SID: 1057 Flags: [N P] Algorithm: 128
        SR Prefix-SID: 1157 Flags: [N P] Algorithm: 129
        SR Prefix-SID: 1257 Flags: [N P] Algorithm: 130
        SR Prefix-SID: 1357 Flags: [N P] Algorithm: 131
        SR Prefix-SID: 1457 Flags: [N P] Algorithm: 132
      Reachability         : 20.57.59.0/24 Metric: 10 Type: 1 Up
      Reachability         : 20.57.149.0/24 Metric: 10 Type: 1 Up
      Reachability         : 20.57.155.0/24 Metric: 10 Type: 1 Up
      Reachability         : 20.57.179.0/24 Metric: 10 Type: 1 Up
      Reachability         : 20.57.211.0/24 Metric: 10 Type: 1 Up
      Reachability          : 2002::57/128 Metric: 0 Type: 1 Up
      Router Capabilities: Router Id: 10.0.0.57 Flags: []
        Maximum SID depth:
          Base MPLS imposition (MSD type 1):  12
        SR Capability: Flags: [I V]
          SRGB Base: 20000 Range: 2000
        Algorithms:  0, 128, 129, 130, 131, 132
        Flex Algo: Algorithm: 128 Metric: Min Unidirectional Delay Metric (1) Calc: SPF (0) Prio: 100
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
    PE31-J2-171.00-00           276  43971  1049    349 L2  0100.0000.0171.00-00  <>
      LSP generation remaining wait time: 0 ms
      Time remaining until refresh: 749 s
      NLPID: 0xCC(IPv4)
      Hostname: PE31-J2-171
      Area addresses: 49.0000
      Interface address: 20.155.171.171
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
      IS Neighbor          : h55-8201-24H8FH.00  Metric: 10
        IPv4 Neighbor Address: 20.155.171.155
        IPv4 Interface Address: 20.155.171.171
        Adj-sid: 362146 flags: [L V] weight: 0x0
        Application Specific Link Attributes:
          Standard applications: Flex-Algo
            TE default metric: 12
            Min/Max unidirectional link delay: 2/2 us
      Reachability         : 20.155.171.0/24 Metric: 10 Type: 1 Up
      Reachability         : 10.0.0.171/32 Metric: 0 Type: 1 Up
        SR Prefix-SID: 171 Flags: [N] Algorithm: 0
        SR Prefix-SID: 1171 Flags: [N] Algorithm: 128
        SR Prefix-SID: 1271 Flags: [N] Algorithm: 129
        SR Prefix-SID: 1371 Flags: [N] Algorithm: 130
        SR Prefix-SID: 1471 Flags: [N] Algorithm: 131
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
          Exclude admin groups: 1
        Flex Algo: Algorithm: 129 Metric: TE Metric (2) Calc: SPF (0) Prio: 237
        Flex Algo: Algorithm: 128 Metric: Min Unidirectional Delay Metric (1) Calc: SPF (0) Prio: 237
    3800.0000.4111.00-00         34  33556  1168    260 L2  3800.0000.4111.00-00  <DefaultAtt>
      NLPID: 0xCC(IPv4) 0x8E(IPv6) 0x81(CLNP)
      TE IPv4 router ID: 100.0.1.111
      Area addresses: 49
      Interface address: 20.111.149.1
      IS Neighbor          : h49-N540-24Q8L2DD.00 Metric: 10
        IPv4 Neighbor Address: 20.111.149.149
        IPv4 Interface Address: 20.111.149.1
        Application Specific Link Attributes:
          Standard applications: Flex-Algo
            TE default metric: 12
            Maximum link BW: 1.00 Gbps
            Maximum reservable link BW: 1.00 Gbps
            Unreserved BW:
                TE class 0: 1.00 Gbps	TE class 1: 1.00 Gbps	TE class 2: 1.00 Gbps
                TE class 3: 1.00 Gbps	TE class 4: 1.00 Gbps	TE class 5: 1.00 Gbps
                TE class 6: 1.00 Gbps	TE class 7: 1.00 Gbps
            Average unidirectional link delay: 11 us
            Unidirectional link delay variation: 11 us
      Reachability         : 20.111.149.0/24 Metric: 10 Type: 1 Up
      Reachability         : 100.0.1.111/32 Metric: 0 Type: 1 Up
        SR Prefix-SID: 111 Flags: [N] Algorithm: 0
        SR Prefix-SID: 1111 Flags: [N] Algorithm: 128
        SR Prefix-SID: 1211 Flags: [N] Algorithm: 129
        SR Prefix-SID: 1311 Flags: [N] Algorithm: 130
        SR Prefix-SID: 1411 Flags: [N] Algorithm: 131
      Router Capabilities: Router Id: 100.0.1.111 Flags: []
        SR Capability: Flags: [I V]
          SRGB Base: 20000 Range: 2000
        Algorithms:  0, 128, 129, 130, 131
```

## show isis flex-algo

```text

IS-IS Instance: IGP VRF: default

Algorithm     Advertised Level Metric    Selected         
------------- ---------- ----- --------- -----------------
MIN-LATENCY   yes        L2    min-delay h49-N540-24Q8L2DD
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
Request sequence number: 101
Response sequence number: 101
Number of times path updated: 101
Last updated: 0:08:14 ago
Metric: 13
Next Hop       Interface 
-------------- ----------
20.149.171.149 Ethernet24

Destination: 0010.0010.0005
Path ID: 641
Path constraints: algo MIN-TE
                  metric type TE
Request sequence number: 101
Response sequence number: 101
Number of times path updated: 101
Last updated: 0:08:14 ago
Metric: 24
Next Hop       Interface 
-------------- ----------
20.149.171.149 Ethernet24

Destination: 0010.0010.0005
Path ID: 642
Path constraints: algo MIN-IGP
                  metric type IGP
                  administrative-group exclude 1
Request sequence number: 104
Response sequence number: 104
Number of times path updated: 104
Last updated: 0:08:14 ago
Metric: 20
Next Hop       Interface 
-------------- ----------
20.149.171.149 Ethernet24

Destination: 0010.0010.0005
Path ID: 643
Path constraints: algo MIN-IGP-ADMIN
                  metric type IGP
                  administrative-group exclude 127
Request sequence number: 101
Response sequence number: 101
Number of times path updated: 101
Last updated: 0:08:14 ago
Next Hop Interface
-------- ---------

Destination: 3800.0000.4111
Path ID: 640
Path constraints: algo MIN-LATENCY
                  metric type MIN-DELAY
Request sequence number: 23
Response sequence number: 23
Number of times path updated: 23
Last updated: 0:08:14 ago
Metric: 13
Next Hop       Interface 
-------------- ----------
20.149.171.149 Ethernet24

Destination: 3800.0000.4111
Path ID: 641
Path constraints: algo MIN-TE
                  metric type TE
Request sequence number: 23
Response sequence number: 23
Number of times path updated: 23
Last updated: 0:08:14 ago
Metric: 24
Next Hop       Interface 
-------------- ----------
20.149.171.149 Ethernet24

Destination: 3800.0000.4111
Path ID: 642
Path constraints: algo MIN-IGP
                  metric type IGP
                  administrative-group exclude 1
Request sequence number: 23
Response sequence number: 23
Number of times path updated: 23
Last updated: 0:08:14 ago
Metric: 20
Next Hop       Interface 
-------------- ----------
20.149.171.149 Ethernet24

Destination: 3800.0000.4111
Path ID: 643
Path constraints: algo MIN-IGP-ADMIN
                  metric type IGP
                  administrative-group exclude 127
Request sequence number: 23
Response sequence number: 23
Number of times path updated: 23
Last updated: 0:08:14 ago
Metric: 30
Next Hop       Interface 
-------------- ----------
20.155.171.155 Ethernet46

Destination: 12502-1
Path ID: 640
Path constraints: algo MIN-LATENCY
                  metric type MIN-DELAY
Request sequence number: 14
Response sequence number: 14
Number of times path updated: 14
Last updated: 0:08:14 ago
Metric: 13
Next Hop       Interface 
-------------- ----------
20.149.171.149 Ethernet24

Destination: 12502-1
Path ID: 641
Path constraints: algo MIN-TE
                  metric type TE
Request sequence number: 14
Response sequence number: 14
Number of times path updated: 14
Last updated: 0:08:14 ago
Metric: 24
Next Hop       Interface 
-------------- ----------
20.149.171.149 Ethernet24

Destination: 12502-1
Path ID: 642
Path constraints: algo MIN-IGP
                  metric type IGP
                  administrative-group exclude 1
Request sequence number: 14
Response sequence number: 14
Number of times path updated: 14
Last updated: 0:08:14 ago
Metric: 20
Next Hop       Interface 
-------------- ----------
20.149.171.149 Ethernet24

Destination: 12502-1
Path ID: 643
Path constraints: algo MIN-IGP-ADMIN
                  metric type IGP
                  administrative-group exclude 127
Request sequence number: 14
Response sequence number: 14
Number of times path updated: 14
Last updated: 0:08:14 ago
Metric: 30
Next Hop       Interface 
-------------- ----------
20.155.171.155 Ethernet46

Destination: NOKIA-SR2-57
Path ID: 640
Path constraints: algo MIN-LATENCY
                  metric type MIN-DELAY
Request sequence number: 7367
Response sequence number: 7367
Number of times path updated: 7375
Last updated: 0:08:14 ago
Metric: 8
Next Hop       Interface 
-------------- ----------
20.155.171.155 Ethernet46

Destination: NOKIA-SR2-57
Path ID: 641
Path constraints: algo MIN-TE
                  metric type TE
Request sequence number: 7366
Response sequence number: 7366
Number of times path updated: 7369
Last updated: 0:08:14 ago
Metric: 24
Next Hop       Interface 
-------------- ----------
20.155.171.155 Ethernet46
20.149.171.149 Ethernet24

Destination: NOKIA-SR2-57
Path ID: 642
Path constraints: algo MIN-IGP
                  metric type IGP
                  administrative-group exclude 1
Request sequence number: 7276
Response sequence number: 7276
Number of times path updated: 7285
Last updated: 0:08:14 ago
Metric: 20
Next Hop       Interface 
-------------- ----------
20.155.171.155 Ethernet46
20.149.171.149 Ethernet24

Destination: NOKIA-SR2-57
Path ID: 643
Path constraints: algo MIN-IGP-ADMIN
                  metric type IGP
                  administrative-group exclude 127
Request sequence number: 7246
Response sequence number: 7246
Number of times path updated: 7246
Last updated: 0:08:14 ago
Metric: 20
Next Hop       Interface 
-------------- ----------
20.155.171.155 Ethernet46

Destination: PE31-J2-171
Path ID: 640
Path constraints: algo MIN-LATENCY
                  metric type MIN-DELAY
Request sequence number: 7407
Response sequence number: 7407
Number of times path updated: 7401
Last updated: 0:08:14 ago
Next Hop Interface
-------- ---------

Destination: PE31-J2-171
Path ID: 641
Path constraints: algo MIN-TE
                  metric type TE
Request sequence number: 7407
Response sequence number: 7407
Number of times path updated: 7401
Last updated: 0:08:14 ago
Next Hop Interface
-------- ---------

Destination: PE31-J2-171
Path ID: 642
Path constraints: algo MIN-IGP
                  metric type IGP
                  administrative-group exclude 1
Request sequence number: 7317
Response sequence number: 7317
Number of times path updated: 7312
Last updated: 0:08:14 ago
Next Hop Interface
-------- ---------

Destination: PE31-J2-171
Path ID: 643
Path constraints: algo MIN-IGP-ADMIN
                  metric type IGP
                  administrative-group exclude 127
Request sequence number: 7273
Response sequence number: 7273
Number of times path updated: 7269
Last updated: 0:08:14 ago
Next Hop Interface
-------- ---------

Destination: Ribbon-32
Path ID: 640
Path constraints: algo MIN-LATENCY
                  metric type MIN-DELAY
Request sequence number: 4
Response sequence number: 4
Number of times path updated: 4
Last updated: 0:08:14 ago
Metric: 13
Next Hop       Interface 
-------------- ----------
20.149.171.149 Ethernet24

Destination: Ribbon-32
Path ID: 641
Path constraints: algo MIN-TE
                  metric type TE
Request sequence number: 4
Response sequence number: 4
Number of times path updated: 4
Last updated: 0:08:14 ago
Metric: 24
Next Hop       Interface 
-------------- ----------
20.149.171.149 Ethernet24

Destination: Ribbon-32
Path ID: 642
Path constraints: algo MIN-IGP
                  metric type IGP
                  administrative-group exclude 1
Request sequence number: 4
Response sequence number: 4
Number of times path updated: 4
Last updated: 0:08:14 ago
Metric: 20
Next Hop       Interface 
-------------- ----------
20.149.171.149 Ethernet24

Destination: h3c_19_CR16010E-F
Path ID: 640
Path constraints: algo MIN-LATENCY
                  metric type MIN-DELAY
Request sequence number: 44
Response sequence number: 44
Number of times path updated: 44
Last updated: 0:08:14 ago
Next Hop Interface
-------- ---------

Destination: h3c_19_CR16010E-F
Path ID: 641
Path constraints: algo MIN-TE
                  metric type TE
Request sequence number: 44
Response sequence number: 44
Number of times path updated: 44
Last updated: 0:08:14 ago
Next Hop Interface
-------- ---------

Destination: h3c_19_CR16010E-F
Path ID: 642
Path constraints: algo MIN-IGP
                  metric type IGP
                  administrative-group exclude 1
Request sequence number: 44
Response sequence number: 44
Number of times path updated: 44
Last updated: 0:08:14 ago
Next Hop Interface
-------- ---------

Destination: h3c_19_CR16010E-F
Path ID: 643
Path constraints: algo MIN-IGP-ADMIN
                  metric type IGP
                  administrative-group exclude 127
Request sequence number: 44
Response sequence number: 44
Number of times path updated: 44
Last updated: 0:08:14 ago
Next Hop Interface
-------- ---------

Destination: h49-N540-24Q8L2DD
Path ID: 640
Path constraints: algo MIN-LATENCY
                  metric type MIN-DELAY
Request sequence number: 7410
Response sequence number: 7410
Number of times path updated: 7407
Last updated: 0:08:14 ago
Metric: 2
Next Hop       Interface 
-------------- ----------
20.149.171.149 Ethernet24

Destination: h49-N540-24Q8L2DD
Path ID: 641
Path constraints: algo MIN-TE
                  metric type TE
Request sequence number: 7409
Response sequence number: 7409
Number of times path updated: 7404
Last updated: 0:08:14 ago
Metric: 12
Next Hop       Interface 
-------------- ----------
20.149.171.149 Ethernet24

Destination: h49-N540-24Q8L2DD
Path ID: 642
Path constraints: algo MIN-IGP
                  metric type IGP
                  administrative-group exclude 1
Request sequence number: 7311
Response sequence number: 7311
Number of times path updated: 7315
Last updated: 0:08:14 ago
Metric: 10
Next Hop       Interface 
-------------- ----------
20.149.171.149 Ethernet24

Destination: h55-8201-24H8FH
Path ID: 640
Path constraints: algo MIN-LATENCY
                  metric type MIN-DELAY
Request sequence number: 7410
Response sequence number: 7410
Number of times path updated: 7408
Last updated: 0:08:14 ago
Metric: 2
Next Hop       Interface 
-------------- ----------
20.155.171.155 Ethernet46

Destination: h55-8201-24H8FH
Path ID: 641
Path constraints: algo MIN-TE
                  metric type TE
Request sequence number: 7409
Response sequence number: 7409
Number of times path updated: 7404
Last updated: 0:08:14 ago
Metric: 12
Next Hop       Interface 
-------------- ----------
20.155.171.155 Ethernet46

Destination: h55-8201-24H8FH
Path ID: 642
Path constraints: algo MIN-IGP
                  metric type IGP
                  administrative-group exclude 1
Request sequence number: 7318
Response sequence number: 7318
Number of times path updated: 7315
Last updated: 0:08:14 ago
Metric: 10
Next Hop       Interface 
-------------- ----------
20.155.171.155 Ethernet46

Destination: h55-8201-24H8FH
Path ID: 643
Path constraints: algo MIN-IGP-ADMIN
                  metric type IGP
                  administrative-group exclude 127
Request sequence number: 7270
Response sequence number: 7270
Number of times path updated: 7267
Last updated: 0:08:14 ago
Metric: 10
Next Hop       Interface 
-------------- ----------
20.155.171.155 Ethernet46

Destination: huawei_34_NetEngine_8000_F8
Path ID: 640
Path constraints: algo MIN-LATENCY
                  metric type MIN-DELAY
Request sequence number: 116
Response sequence number: 116
Number of times path updated: 116
Last updated: 0:08:14 ago
Metric: 13
Next Hop       Interface 
-------------- ----------
20.149.171.149 Ethernet24

Destination: huawei_34_NetEngine_8000_F8
Path ID: 641
Path constraints: algo MIN-TE
                  metric type TE
Request sequence number: 116
Response sequence number: 116
Number of times path updated: 116
Last updated: 0:08:14 ago
Metric: 24
Next Hop       Interface 
-------------- ----------
20.149.171.149 Ethernet24

Destination: huawei_34_NetEngine_8000_F8
Path ID: 642
Path constraints: algo MIN-IGP
                  metric type IGP
                  administrative-group exclude 1
Request sequence number: 1
Response sequence number: 1
Number of times path updated: 1
Last updated: 0:05:34 ago
Metric: 20
Next Hop       Interface 
-------------- ----------
20.149.171.149 Ethernet24

Destination: huawei_34_NetEngine_8000_F8
Path ID: 643
Path constraints: algo MIN-IGP-ADMIN
                  metric type IGP
                  administrative-group exclude 127
Request sequence number: 1
Response sequence number: 1
Number of times path updated: 1
Last updated: 0:05:34 ago
Metric: 30
Next Hop       Interface 
-------------- ----------
20.155.171.155 Ethernet46

Destination: juniper_379_MX304
Path ID: 640
Path constraints: algo MIN-LATENCY
                  metric type MIN-DELAY
Request sequence number: 21
Response sequence number: 21
Number of times path updated: 22
Last updated: 0:08:14 ago
Metric: 13
Next Hop       Interface 
-------------- ----------
20.155.171.155 Ethernet46

Destination: juniper_379_MX304
Path ID: 641
Path constraints: algo MIN-TE
                  metric type TE
Request sequence number: 21
Response sequence number: 21
Number of times path updated: 22
Last updated: 0:08:14 ago
Metric: 24
Next Hop       Interface 
-------------- ----------
20.155.171.155 Ethernet46

Destination: juniper_379_MX304
Path ID: 642
Path constraints: algo MIN-IGP
                  metric type IGP
                  administrative-group exclude 1
Request sequence number: 21
Response sequence number: 21
Number of times path updated: 22
Last updated: 0:08:14 ago
Metric: 30
Next Hop       Interface 
-------------- ----------
20.155.171.155 Ethernet46
20.149.171.149 Ethernet24

```

## show isis segment-routing tunnel

```text
  Index     Endpoint           Next Hop/Tunnel Index     Interface    Labels   
--------- ------------------ ------------------------- -------------- ---------
  1         10.0.0.83/32       TI-LFA (4)                -            [ 20083 ]
  3         10.0.1.49/32       TI-LFA (7)                -            [ 3 ]    
  4         10.0.0.19/32       20.149.171.149            Ethernet24   [ 20019 ]
  5         10.0.1.55/32       TI-LFA (3)                -            [ 3 ]    
  6         10.0.0.254/32      TI-LFA (4)                -            [ 20254 ]
  7         10.0.0.57/32       20.149.171.149            Ethernet24   [ 20057 ]
                               20.155.171.155            Ethernet46   [ 20057 ]
  8         10.0.0.179/32      TI-LFA (2)                -            [ 20379 ]
  9         10.0.0.32/32       TI-LFA (4)                -            [ 20032 ]
  10        100.0.1.111/32     TI-LFA (4)                -            [ 20111 ]
  11        10.0.0.24/32       TI-LFA (4)                -            [ 20024 ]
  12        10.0.0.5/32        TI-LFA (4)                -            [ 20005 ]

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
   10.0.0.5/32                1005   21005 Node       R:0 N:1 P:0 E:0 V:0 L:0      0010.0010.0005  L2    node        MIN-LATENCY 
   10.0.0.5/32                1105   21105 Node       R:0 N:1 P:0 E:0 V:0 L:0      0010.0010.0005  L2    node        MIN-TE      
   10.0.0.5/32                1205   21205 Node       R:0 N:1 P:0 E:0 V:0 L:0      0010.0010.0005  L2    node        MIN-IGP     
   10.0.0.5/32                1305   21305 Node       R:0 N:1 P:0 E:0 V:0 L:0      0010.0010.0005  L2    unprotected MIN-IGP-ADMIN
   10.0.0.19/32                 19   20019 Node       R:0 N:1 P:0 E:0 V:0 L:0      h3c_19_CR16010E-F L2    node        SPF         
   10.0.0.19/32               1019   21019 Node       R:0 N:1 P:0 E:0 V:0 L:0      h3c_19_CR16010E-F L2    unprotected MIN-LATENCY 
   10.0.0.19/32               1119   21119 Node       R:0 N:1 P:0 E:0 V:0 L:0      h3c_19_CR16010E-F L2    unprotected MIN-TE      
   10.0.0.19/32               1219   21219 Node       R:0 N:1 P:0 E:0 V:0 L:0      h3c_19_CR16010E-F L2    unprotected MIN-IGP     
   10.0.0.19/32               1319   21319 Node       R:0 N:1 P:0 E:0 V:0 L:0      h3c_19_CR16010E-F L2    unprotected MIN-IGP-ADMIN
   10.0.0.24/32                 24   20024 Node       R:0 N:1 P:1 E:0 V:0 L:0      12502-1         L2    node        SPF         
   10.0.0.24/32               1024   21024 Node       R:0 N:1 P:1 E:0 V:0 L:0      12502-1         L2    node        MIN-LATENCY 
   10.0.0.24/32               1124   21124 Node       R:0 N:1 P:1 E:0 V:0 L:0      12502-1         L2    node        MIN-TE      
   10.0.0.24/32               1224   21224 Node       R:0 N:1 P:1 E:0 V:0 L:0      12502-1         L2    node        MIN-IGP     
   10.0.0.24/32               1324   21324 Node       R:0 N:1 P:1 E:0 V:0 L:0      12502-1         L2    node        MIN-IGP-ADMIN
   10.0.0.32/32                 32   20032 Node       R:0 N:1 P:0 E:0 V:0 L:0      Ribbon-32       L2    node        SPF         
   10.0.0.32/32               1032   21032 Node       R:0 N:1 P:0 E:0 V:0 L:0      Ribbon-32       L2    node        MIN-LATENCY 
   10.0.0.32/32               1132   21132 Node       R:0 N:1 P:0 E:0 V:0 L:0      Ribbon-32       L2    node        MIN-TE      
   10.0.0.32/32               1232   21232 Node       R:0 N:1 P:0 E:0 V:0 L:0      Ribbon-32       L2    node        MIN-IGP     
   10.0.0.57/32                 57   20057 Node       R:0 N:1 P:1 E:0 V:0 L:0      NOKIA-SR2-57    L2    unprotected SPF         
   10.0.0.57/32               1057   21057 Node       R:0 N:1 P:1 E:0 V:0 L:0      NOKIA-SR2-57    L2    node        MIN-LATENCY 
   10.0.0.57/32               1157   21157 Node       R:0 N:1 P:1 E:0 V:0 L:0      NOKIA-SR2-57    L2    unprotected MIN-TE      
   10.0.0.57/32               1257   21257 Node       R:0 N:1 P:1 E:0 V:0 L:0      NOKIA-SR2-57    L2    unprotected MIN-IGP     
   10.0.0.57/32               1357   21357 Node       R:0 N:1 P:1 E:0 V:0 L:0      NOKIA-SR2-57    L2    node        MIN-IGP-ADMIN
   10.0.0.57/32               1457   21457 Node       R:0 N:1 P:1 E:0 V:0 L:0      NOKIA-SR2-57    L2    unprotected 132         
   10.0.0.83/32                 83   20083 Node       R:0 N:1 P:0 E:0 V:0 L:0      eantc-jcnr2     L2    node        SPF         
*  10.0.0.171/32               171   20171 Node       R:0 N:1 P:0 E:0 V:0 L:0      PE31-J2-171     L2    unprotected SPF         
*  10.0.0.171/32              1171   21171 Node       R:0 N:1 P:0 E:0 V:0 L:0      PE31-J2-171     L2    unprotected MIN-LATENCY 
*  10.0.0.171/32              1271   21271 Node       R:0 N:1 P:0 E:0 V:0 L:0      PE31-J2-171     L2    unprotected MIN-TE      
*  10.0.0.171/32              1371   21371 Node       R:0 N:1 P:0 E:0 V:0 L:0      PE31-J2-171     L2    unprotected MIN-IGP     
*  10.0.0.171/32              1471   21471 Node       R:0 N:1 P:0 E:0 V:0 L:0      PE31-J2-171     L2    unprotected MIN-IGP-ADMIN
   10.0.0.179/32               379   20379 Node       R:0 N:1 P:0 E:0 V:0 L:0      juniper_379_MX304 L2    node        SPF         
   10.0.0.179/32              1179   21179 Node       R:0 N:1 P:0 E:0 V:0 L:0      juniper_379_MX304 L2    node        MIN-LATENCY 
   10.0.0.179/32              1279   21279 Node       R:0 N:1 P:0 E:0 V:0 L:0      juniper_379_MX304 L2    node        MIN-TE      
   10.0.0.179/32              1379   21379 Node       R:0 N:1 P:0 E:0 V:0 L:0      juniper_379_MX304 L2    unprotected MIN-IGP     
   10.0.0.254/32               254   20254 Node       R:0 N:1 P:0 E:0 V:0 L:0      huawei_34_NetEngine_8000_F8 L2    node        SPF         
   10.0.0.254/32              1254   21254 Node       R:0 N:1 P:0 E:0 V:0 L:0      huawei_34_NetEngine_8000_F8 L2    node        MIN-LATENCY 
   10.0.0.254/32              1354   21354 Node       R:0 N:1 P:0 E:0 V:0 L:0      huawei_34_NetEngine_8000_F8 L2    node        MIN-TE      
   10.0.0.254/32              1454   21454 Node       R:0 N:1 P:0 E:0 V:0 L:0      huawei_34_NetEngine_8000_F8 L2    node        MIN-IGP     
   10.0.0.254/32              1554   21554 Node       R:0 N:1 P:0 E:0 V:0 L:0      huawei_34_NetEngine_8000_F8 L2    node        MIN-IGP-ADMIN
   10.0.1.49/32                349   20349 Node       R:0 N:1 P:0 E:0 V:0 L:0      h49-N540-24Q8L2DD L2    node        SPF         
   10.0.1.49/32               1349   21349 Node       R:0 N:1 P:0 E:0 V:0 L:0      h49-N540-24Q8L2DD L2    node        MIN-LATENCY 
   10.0.1.49/32               1449   21449 Node       R:0 N:1 P:0 E:0 V:0 L:0      h49-N540-24Q8L2DD L2    node        MIN-TE      
   10.0.1.49/32               1649   21649 Node       R:0 N:1 P:0 E:0 V:0 L:0      h49-N540-24Q8L2DD L2    node        MIN-IGP     
   10.0.1.49/32               1749   21749 Node       R:0 N:1 P:0 E:0 V:0 L:0      h49-N540-24Q8L2DD L2    unprotected 132         
   10.0.1.55/32                355   20355 Node       R:0 N:1 P:0 E:0 V:0 L:0      h55-8201-24H8FH L2    node        SPF         
   10.0.1.55/32               1355   21355 Node       R:0 N:1 P:0 E:0 V:0 L:0      h55-8201-24H8FH L2    node        MIN-LATENCY 
   10.0.1.55/32               1455   21455 Node       R:0 N:1 P:0 E:0 V:0 L:0      h55-8201-24H8FH L2    node        MIN-TE      
   10.0.1.55/32               1555   21555 Node       R:0 N:1 P:0 E:0 V:0 L:0      h55-8201-24H8FH L2    node        MIN-IGP     
   10.0.1.55/32               1655   21655 Node       R:0 N:1 P:0 E:0 V:0 L:0      h55-8201-24H8FH L2    node        MIN-IGP-ADMIN
   10.0.1.55/32               1755   21755 Node       R:0 N:1 P:0 E:0 V:0 L:0      h55-8201-24H8FH L2    unprotected 132         
   100.0.1.111/32              111   20111 Node       R:0 N:1 P:0 E:0 V:0 L:0      3800.0000.4111  L2    node        SPF         
   100.0.1.111/32             1111   21111 Node       R:0 N:1 P:0 E:0 V:0 L:0      3800.0000.4111  L2    node        MIN-LATENCY 
   100.0.1.111/32             1211   21211 Node       R:0 N:1 P:0 E:0 V:0 L:0      3800.0000.4111  L2    node        MIN-TE      
   100.0.1.111/32             1311   21311 Node       R:0 N:1 P:0 E:0 V:0 L:0      3800.0000.4111  L2    node        MIN-IGP     
   100.0.1.111/32             1411   21411 Node       R:0 N:1 P:0 E:0 V:0 L:0      3800.0000.4111  L2    node        MIN-IGP-ADMIN
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

 I L2     10.0.0.5/32 [115/30]
           via 20.149.171.149, Ethernet24
 I L2     10.0.0.19/32 [115/20]
           via 20.149.171.149, Ethernet24
 I L2     10.0.0.24/32 [115/20]
           via 20.149.171.149, Ethernet24
 I L2     10.0.0.32/32 [115/20]
           via 20.149.171.149, Ethernet24
 I L2     10.0.0.57/32 [115/20]
           via 20.149.171.149, Ethernet24
           via 20.155.171.155, Ethernet46
 I L2     10.0.0.83/32 [115/20]
           via 20.149.171.149, Ethernet24
 C        10.0.0.171/32
           directly connected, Loopback0
 I L2     10.0.0.179/32 [115/20]
           via 20.155.171.155, Ethernet46
 I L2     10.0.0.254/32 [115/20]
           via 20.149.171.149, Ethernet24
 I L2     10.0.1.49/32 [115/10]
           via 20.149.171.149, Ethernet24
 I L2     10.0.1.55/32 [115/10]
           via 20.155.171.155, Ethernet46
 I L2     20.5.149.0/24 [115/20]
           via 20.149.171.149, Ethernet24
 I L2     20.19.149.0/24 [115/20]
           via 20.149.171.149, Ethernet24
 I L2     20.24.149.0/24 [115/20]
           via 20.149.171.149, Ethernet24
 I L2     20.32.149.0/24 [115/20]
           via 20.149.171.149, Ethernet24
 I L2     20.32.211.0/24 [115/30]
           via 20.149.171.149, Ethernet24
 I L2     20.47.149.0/24 [115/20]
           via 20.149.171.149, Ethernet24
 I L2     20.57.59.0/24 [115/30]
           via 20.149.171.149, Ethernet24
           via 20.155.171.155, Ethernet46
 I L2     20.57.149.0/24 [115/20]
           via 20.149.171.149, Ethernet24
 I L2     20.57.155.0/24 [115/20]
           via 20.155.171.155, Ethernet46
 I L2     20.57.179.0/24 [115/30]
           via 20.149.171.149, Ethernet24
           via 20.155.171.155, Ethernet46
 I L2     20.57.211.0/24 [115/30]
           via 20.149.171.149, Ethernet24
           via 20.155.171.155, Ethernet46
 I L2     20.83.149.0/24 [115/20]
           via 20.149.171.149, Ethernet24
 I L2     20.111.149.0/24 [115/20]
           via 20.149.171.149, Ethernet24
 I L2     20.149.155.0/24 [115/20]
           via 20.149.171.149, Ethernet24
           via 20.155.171.155, Ethernet46
 C        20.149.171.0/24
           directly connected, Ethernet24
 I L2     20.149.254.0/24 [115/20]
           via 20.149.171.149, Ethernet24
 C        20.155.171.0/24
           directly connected, Ethernet46
 I L2     20.155.179.0/24 [115/20]
           via 20.155.171.155, Ethernet46
 I L2     100.0.1.111/32 [115/20]
           via 20.149.171.149, Ethernet24
 I L2     192.168.20.0/23 [115/20]
           via 20.149.171.149, Ethernet24
 I L2     192.168.0.0/19 [115/20]
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

Gateway of last resort is not set

 I L2     10.0.0.5/32 [115/30]
           via 20.149.171.149, Ethernet24
 I L2     10.0.0.19/32 [115/20]
           via 20.149.171.149, Ethernet24
 I L2     10.0.0.24/32 [115/20]
           via 20.149.171.149, Ethernet24
 I L2     10.0.0.32/32 [115/20]
           via 20.149.171.149, Ethernet24
 I L2     10.0.0.57/32 [115/20]
           via 20.149.171.149, Ethernet24
           via 20.155.171.155, Ethernet46
 I L2     10.0.0.83/32 [115/20]
           via 20.149.171.149, Ethernet24
 C        10.0.0.171/32
           directly connected, Loopback0
 I L2     10.0.0.179/32 [115/20]
           via 20.155.171.155, Ethernet46
 I L2     10.0.0.254/32 [115/20]
           via 20.149.171.149, Ethernet24
 I L2     10.0.1.49/32 [115/10]
           via 20.149.171.149, Ethernet24
 I L2     10.0.1.55/32 [115/10]
           via 20.155.171.155, Ethernet46
 I L2     20.5.149.0/24 [115/20]
           via 20.149.171.149, Ethernet24
 I L2     20.19.149.0/24 [115/20]
           via 20.149.171.149, Ethernet24
 I L2     20.24.149.0/24 [115/20]
           via 20.149.171.149, Ethernet24
 I L2     20.32.149.0/24 [115/20]
           via 20.149.171.149, Ethernet24
 I L2     20.32.211.0/24 [115/30]
           via 20.149.171.149, Ethernet24
 I L2     20.47.149.0/24 [115/20]
           via 20.149.171.149, Ethernet24
 I L2     20.57.59.0/24 [115/30]
           via 20.149.171.149, Ethernet24
           via 20.155.171.155, Ethernet46
 I L2     20.57.149.0/24 [115/20]
           via 20.149.171.149, Ethernet24
 I L2     20.57.155.0/24 [115/20]
           via 20.155.171.155, Ethernet46
 I L2     20.57.179.0/24 [115/30]
           via 20.149.171.149, Ethernet24
           via 20.155.171.155, Ethernet46
 I L2     20.57.211.0/24 [115/30]
           via 20.149.171.149, Ethernet24
           via 20.155.171.155, Ethernet46
 I L2     20.83.149.0/24 [115/20]
           via 20.149.171.149, Ethernet24
 I L2     20.111.149.0/24 [115/20]
           via 20.149.171.149, Ethernet24
 I L2     20.149.155.0/24 [115/20]
           via 20.149.171.149, Ethernet24
           via 20.155.171.155, Ethernet46
 C        20.149.171.0/24
           directly connected, Ethernet24
 I L2     20.149.254.0/24 [115/20]
           via 20.149.171.149, Ethernet24
 C        20.155.171.0/24
           directly connected, Ethernet46
 I L2     20.155.179.0/24 [115/20]
           via 20.155.171.155, Ethernet46
 I L2     100.0.1.111/32 [115/20]
           via 20.149.171.149, Ethernet24
 I L2     192.168.20.0/23 [115/20]
           via 20.149.171.149, Ethernet24
 I L2     192.168.0.0/19 [115/20]
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

 B I      20.5.111.0/24 [200/0]
           via 10.0.0.5/32, algorithm MIN-LATENCY, IS-IS FlexAlgo tunnel index 36, label 62004
              via TI-LFA tunnel index 4, label 21005
                 via 20.149.171.149, Ethernet24, label imp-null(3)
                 backup via 20.155.171.155, Ethernet46, label imp-null(3)
 B I      20.19.111.0/24 [200/0]
           via 10.0.0.19/32, IS-IS SR tunnel index 4, label 1277
              via 20.149.171.149, Ethernet24, label 20019
 B I      20.24.111.0/24 [200/0]
           via 10.0.0.24/32, algorithm MIN-LATENCY, IS-IS FlexAlgo tunnel index 39, label 56507
              via TI-LFA tunnel index 4, label 21024
                 via 20.149.171.149, Ethernet24, label imp-null(3)
                 backup via 20.155.171.155, Ethernet46, label imp-null(3)
 B I      20.32.111.0/24 [200/0]
           via 10.0.0.32/32, algorithm MIN-LATENCY, IS-IS FlexAlgo tunnel index 13, label 756643
              via TI-LFA tunnel index 4, label 21032
                 via 20.149.171.149, Ethernet24, label imp-null(3)
                 backup via 20.155.171.155, Ethernet46, label imp-null(3)
 B I      20.57.111.0/24 [200/0]
           via 10.0.0.57/32, algorithm MIN-LATENCY, IS-IS FlexAlgo tunnel index 15, label 524286
              via TI-LFA tunnel index 6, label 21057
                 via 20.155.171.155, Ethernet46, label imp-null(3)
                 backup via 20.149.171.149, Ethernet24, label 24009
 B I      20.111.111.0/24 [200/0]
           via 100.0.1.111/32, algorithm MIN-LATENCY, IS-IS FlexAlgo tunnel index 28, label 17
              via TI-LFA tunnel index 4, label 21111
                 via 20.149.171.149, Ethernet24, label imp-null(3)
                 backup via 20.155.171.155, Ethernet46, label imp-null(3)
 B I      20.111.155.0/24 [200/0]
           via 10.0.1.55/32, algorithm MIN-LATENCY, IS-IS FlexAlgo tunnel index 8, label 24009
              via TI-LFA tunnel index 8, label imp-null(3)
                 via 20.155.171.155, Ethernet46, label imp-null(3)
                 backup via 20.149.171.149, Ethernet24, label 21355
 C        20.111.171.0/24
           directly connected, Ethernet5.128
 B I      20.111.179.0/24 [200/0]
           via 10.0.0.179/32, algorithm MIN-LATENCY, IS-IS FlexAlgo tunnel index 19, label 16
              via TI-LFA tunnel index 6, label 21179
                 via 20.155.171.155, Ethernet46, label imp-null(3)
                 backup via 20.149.171.149, Ethernet24, label 24009
 B I      20.111.254.0/24 [200/0]
           via 10.0.0.254/32, algorithm MIN-LATENCY, IS-IS FlexAlgo tunnel index 14, label 48091
              via TI-LFA tunnel index 4, label 21254
                 via 20.149.171.149, Ethernet24, label imp-null(3)
                 backup via 20.155.171.155, Ethernet46, label imp-null(3)


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
           via 10.0.0.5/32, algorithm MIN-IGP, IS-IS FlexAlgo tunnel index 35, label 62006
              via TI-LFA tunnel index 4, label 21205
                 via 20.149.171.149, Ethernet24, label imp-null(3)
                 backup via 20.155.171.155, Ethernet46, label imp-null(3)
 B I      20.19.111.0/24 [200/0]
           via 10.0.0.19/32, IS-IS SR tunnel index 4, label 1275
              via 20.149.171.149, Ethernet24, label 20019
 B I      20.24.111.0/24 [200/0]
           via 10.0.0.24/32, algorithm MIN-IGP, IS-IS FlexAlgo tunnel index 40, label 56505
              via TI-LFA tunnel index 4, label 21224
                 via 20.149.171.149, Ethernet24, label imp-null(3)
                 backup via 20.155.171.155, Ethernet46, label imp-null(3)
 B I      20.32.111.0/24 [200/0]
           via 10.0.0.32/32, algorithm MIN-IGP, IS-IS FlexAlgo tunnel index 3, label 756645
              via TI-LFA tunnel index 4, label 21232
                 via 20.149.171.149, Ethernet24, label imp-null(3)
                 backup via 20.155.171.155, Ethernet46, label imp-null(3)
 B I      20.57.111.0/24 [200/0]
           via 10.0.0.57/32, algorithm MIN-IGP, IS-IS FlexAlgo tunnel index 17, label 524283
              via 20.149.171.149, Ethernet24, label 21257
              via 20.155.171.155, Ethernet46, label 21257
 B I      20.111.111.0/24 [200/0]
           via 100.0.1.111/32, algorithm MIN-IGP, IS-IS FlexAlgo tunnel index 26, label 19
              via TI-LFA tunnel index 4, label 21311
                 via 20.149.171.149, Ethernet24, label imp-null(3)
                 backup via 20.155.171.155, Ethernet46, label imp-null(3)
 B I      20.111.155.0/24 [200/0]
           via 10.0.1.55/32, algorithm MIN-IGP, IS-IS FlexAlgo tunnel index 1, label 24012
              via TI-LFA tunnel index 9, label imp-null(3)
                 via 20.155.171.155, Ethernet46, label imp-null(3)
                 backup via 20.149.171.149, Ethernet24, label 21555
 C        20.111.171.0/24
           directly connected, Ethernet5.130
 B I      20.111.179.0/24 [200/0]
           via 10.0.0.179/32, algorithm MIN-IGP, IS-IS FlexAlgo tunnel index 25, label 18
              via 20.149.171.149, Ethernet24, label 21379
              via 20.155.171.155, Ethernet46, label 21379
 B I      20.111.254.0/24 [200/0]
           via 10.0.0.254/32, algorithm MIN-IGP, IS-IS FlexAlgo tunnel index 10, label 48093
              via TI-LFA tunnel index 4, label 21454
                 via 20.149.171.149, Ethernet24, label imp-null(3)
                 backup via 20.155.171.155, Ethernet46, label imp-null(3)
 B I      55.55.55.130/32 [200/0]
           via 10.0.1.55/32, algorithm MIN-IGP, IS-IS FlexAlgo tunnel index 1, label 24012
              via TI-LFA tunnel index 9, label imp-null(3)
                 via 20.155.171.155, Ethernet46, label imp-null(3)
                 backup via 20.149.171.149, Ethernet24, label 21555


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
           via 10.0.0.19/32, IS-IS SR tunnel index 4, label 1274
              via 20.149.171.149, Ethernet24, label 20019
 B I      20.24.111.0/24 [200/0]
           via 10.0.0.24/32, algorithm MIN-LATENCY, IS-IS FlexAlgo tunnel index 39, label 56504
              via TI-LFA tunnel index 4, label 21024
                 via 20.149.171.149, Ethernet24, label imp-null(3)
                 backup via 20.155.171.155, Ethernet46, label imp-null(3)
 B I      20.57.111.0/24 [200/0]
           via 10.0.0.57/32, algorithm MIN-IGP-ADMIN, IS-IS FlexAlgo tunnel index 20, label 524282
              via 20.155.171.155, Ethernet46, label 21357
 B I      20.111.111.0/24 [200/0]
           via 100.0.1.111/32, algorithm MIN-IGP-ADMIN, IS-IS FlexAlgo tunnel index 27, label 20
              via 20.155.171.155, Ethernet46, label 21411
 B I      20.111.155.0/24 [200/0]
           via 10.0.1.55/32, algorithm MIN-IGP-ADMIN, IS-IS FlexAlgo tunnel index 5, label 24011
              via 20.155.171.155, Ethernet46, label imp-null(3)
 C        20.111.171.0/24
           directly connected, Ethernet5.131
 B I      20.111.254.0/24 [200/0]
           via 10.0.0.254/32, algorithm MIN-IGP-ADMIN, IS-IS FlexAlgo tunnel index 11, label 48094
              via 20.155.171.155, Ethernet46, label 21554


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
           via 10.0.0.5/32, algorithm MIN-TE, IS-IS FlexAlgo tunnel index 34, label 62005
              via TI-LFA tunnel index 4, label 21105
                 via 20.149.171.149, Ethernet24, label imp-null(3)
                 backup via 20.155.171.155, Ethernet46, label imp-null(3)
 B I      20.19.111.0/24 [200/0]
           via 10.0.0.19/32, IS-IS SR tunnel index 4, label 1276
              via 20.149.171.149, Ethernet24, label 20019
 B I      20.24.111.0/24 [200/0]
           via 10.0.0.24/32, algorithm MIN-TE, IS-IS FlexAlgo tunnel index 38, label 56506
              via TI-LFA tunnel index 4, label 21124
                 via 20.149.171.149, Ethernet24, label imp-null(3)
                 backup via 20.155.171.155, Ethernet46, label imp-null(3)
 B I      20.32.111.0/24 [200/0]
           via 10.0.0.32/32, algorithm MIN-TE, IS-IS FlexAlgo tunnel index 9, label 756644
              via TI-LFA tunnel index 4, label 21132
                 via 20.149.171.149, Ethernet24, label imp-null(3)
                 backup via 20.155.171.155, Ethernet46, label imp-null(3)
 B I      20.57.111.0/24 [200/0]
           via 10.0.0.57/32, algorithm MIN-TE, IS-IS FlexAlgo tunnel index 16, label 524284
              via 20.149.171.149, Ethernet24, label 21157
              via 20.155.171.155, Ethernet46, label 21157
 B I      20.111.111.0/24 [200/0]
           via 100.0.1.111/32, algorithm MIN-TE, IS-IS FlexAlgo tunnel index 29, label 18
              via TI-LFA tunnel index 4, label 21211
                 via 20.149.171.149, Ethernet24, label imp-null(3)
                 backup via 20.155.171.155, Ethernet46, label imp-null(3)
 B I      20.111.155.0/24 [200/0]
           via 10.0.1.55/32, algorithm MIN-TE, IS-IS FlexAlgo tunnel index 7, label 24010
              via TI-LFA tunnel index 1, label imp-null(3)
                 via 20.155.171.155, Ethernet46, label imp-null(3)
                 backup via 20.149.171.149, Ethernet24, label 21455
 C        20.111.171.0/24
           directly connected, Ethernet5.129
 B I      20.111.179.0/24 [200/0]
           via 10.0.0.179/32, algorithm MIN-TE, IS-IS FlexAlgo tunnel index 18, label 17
              via TI-LFA tunnel index 11, label 21279
                 via 20.155.171.155, Ethernet46, label imp-null(3)
                 backup via 20.149.171.149, Ethernet24, label 21157
 B I      20.111.254.0/24 [200/0]
           via 10.0.0.254/32, algorithm MIN-TE, IS-IS FlexAlgo tunnel index 12, label 48092
              via TI-LFA tunnel index 4, label 21354
                 via 20.149.171.149, Ethernet24, label imp-null(3)
                 backup via 20.155.171.155, Ethernet46, label imp-null(3)


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

 B I      20.5.111.0/24 [200/0]
           via 10.0.0.5/32, IS-IS SR tunnel index 12, label 62000
              via TI-LFA tunnel index 4, label 20005
                 via 20.149.171.149, Ethernet24, label imp-null(3)
                 backup via 20.155.171.155, Ethernet46, label imp-null(3)
 B I      20.19.111.0/24 [200/0]
           via 10.0.0.19/32, IS-IS SR tunnel index 4, label 1279
              via 20.149.171.149, Ethernet24, label 20019
 B I      20.55.111.0/24 [200/0]
           via 10.0.1.55/32, IS-IS SR tunnel index 5, label 24004
              via TI-LFA tunnel index 3, label imp-null(3)
                 via 20.155.171.155, Ethernet46, label imp-null(3)
                 backup via 20.149.171.149, Ethernet24, label 20355
 B I      20.57.111.0/24 [200/0]
           via 10.0.0.57/32, IS-IS SR tunnel index 7, label 524287
              via 20.149.171.149, Ethernet24, label 20057
              via 20.155.171.155, Ethernet46, label 20057
 B I      20.83.111.0/24 [200/0]
           via 10.0.0.83/32, IS-IS SR tunnel index 1, label 18
              via TI-LFA tunnel index 4, label 20083
                 via 20.149.171.149, Ethernet24, label imp-null(3)
                 backup via 20.155.171.155, Ethernet46, label imp-null(3)


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
MPLS forwarding table (Label [metric] Vias) - 50 routes 
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
                  via TI-LFA tunnel index 4
                    via 20.149.171.149, Ethernet24, label imp-null(3)
                    backup via 20.155.171.155, Ethernet46, label imp-null(3)
 20019   A[1]
                via M, forward
                    EgressACL: apply
                    20.149.171.149 Ethernet24
 20024   A[1]
                via M, ::, forward
                    EgressACL: apply
                  via TI-LFA tunnel index 4
                    via 20.149.171.149, Ethernet24, label imp-null(3)
                    backup via 20.155.171.155, Ethernet46, label imp-null(3)
 20032   A[1]
                via M, ::, forward
                    EgressACL: apply
                  via TI-LFA tunnel index 4
                    via 20.149.171.149, Ethernet24, label imp-null(3)
                    backup via 20.155.171.155, Ethernet46, label imp-null(3)
 20057   A[1]
                via M, forward
                    EgressACL: apply
                    20.149.171.149 Ethernet24
                    20.155.171.155 Ethernet46
 20083   A[1]
                via M, ::, forward
                    EgressACL: apply
                  via TI-LFA tunnel index 4
                    via 20.149.171.149, Ethernet24, label imp-null(3)
                    backup via 20.155.171.155, Ethernet46, label imp-null(3)
 20111   A[1]
                via M, ::, forward
                    EgressACL: apply
                  via TI-LFA tunnel index 4
                    via 20.149.171.149, Ethernet24, label imp-null(3)
                    backup via 20.155.171.155, Ethernet46, label imp-null(3)
 20254   A[1]
                via M, ::, forward
                    EgressACL: apply
                  via TI-LFA tunnel index 4
                    via 20.149.171.149, Ethernet24, label imp-null(3)
                    backup via 20.155.171.155, Ethernet46, label imp-null(3)
 20349   A[1]
                via M, ::, pop
                    EgressACL: apply
                  via TI-LFA tunnel index 7
                    via 20.149.171.149, Ethernet24, label imp-null(3)
                    backup via 20.155.171.155, Ethernet46, label 20349
 20355   A[1]
                via M, ::, pop
                    EgressACL: apply
                  via TI-LFA tunnel index 3
                    via 20.155.171.155, Ethernet46, label imp-null(3)
                    backup via 20.149.171.149, Ethernet24, label 20355
 20379   A[1]
                via M, ::, forward
                    EgressACL: apply
                  via TI-LFA tunnel index 2
                    via 20.155.171.155, Ethernet46, label imp-null(3)
                    backup via 20.149.171.149, Ethernet24, label 20057
 21005   A[1]
                via M, ::, forward
                    EgressACL: apply
                  via TI-LFA tunnel index 4
                    via 20.149.171.149, Ethernet24, label imp-null(3)
                    backup via 20.155.171.155, Ethernet46, label imp-null(3)
 21024   A[1]
                via M, ::, forward
                    EgressACL: apply
                  via TI-LFA tunnel index 4
                    via 20.149.171.149, Ethernet24, label imp-null(3)
                    backup via 20.155.171.155, Ethernet46, label imp-null(3)
 21032   A[1]
                via M, ::, forward
                    EgressACL: apply
                  via TI-LFA tunnel index 4
                    via 20.149.171.149, Ethernet24, label imp-null(3)
                    backup via 20.155.171.155, Ethernet46, label imp-null(3)
 21057   A[1]
                via M, ::, forward
                    EgressACL: apply
                  via TI-LFA tunnel index 6
                    via 20.155.171.155, Ethernet46, label imp-null(3)
                    backup via 20.149.171.149, Ethernet24, label 24009
 21105   A[1]
                via M, ::, forward
                    EgressACL: apply
                  via TI-LFA tunnel index 4
                    via 20.149.171.149, Ethernet24, label imp-null(3)
                    backup via 20.155.171.155, Ethernet46, label imp-null(3)
 21111   A[1]
                via M, ::, forward
                    EgressACL: apply
                  via TI-LFA tunnel index 4
                    via 20.149.171.149, Ethernet24, label imp-null(3)
                    backup via 20.155.171.155, Ethernet46, label imp-null(3)
 21124   A[1]
                via M, ::, forward
                    EgressACL: apply
                  via TI-LFA tunnel index 4
                    via 20.149.171.149, Ethernet24, label imp-null(3)
                    backup via 20.155.171.155, Ethernet46, label imp-null(3)
 21132   A[1]
                via M, ::, forward
                    EgressACL: apply
                  via TI-LFA tunnel index 4
                    via 20.149.171.149, Ethernet24, label imp-null(3)
                    backup via 20.155.171.155, Ethernet46, label imp-null(3)
 21157   A[1]
                via M, forward
                    EgressACL: apply
                    20.149.171.149 Ethernet24
                    20.155.171.155 Ethernet46
 21179   A[1]
                via M, ::, forward
                    EgressACL: apply
                  via TI-LFA tunnel index 6
                    via 20.155.171.155, Ethernet46, label imp-null(3)
                    backup via 20.149.171.149, Ethernet24, label 24009
 21205   A[1]
                via M, ::, forward
                    EgressACL: apply
                  via TI-LFA tunnel index 4
                    via 20.149.171.149, Ethernet24, label imp-null(3)
                    backup via 20.155.171.155, Ethernet46, label imp-null(3)
 21211   A[1]
                via M, ::, forward
                    EgressACL: apply
                  via TI-LFA tunnel index 4
                    via 20.149.171.149, Ethernet24, label imp-null(3)
                    backup via 20.155.171.155, Ethernet46, label imp-null(3)
 21224   A[1]
                via M, ::, forward
                    EgressACL: apply
                  via TI-LFA tunnel index 4
                    via 20.149.171.149, Ethernet24, label imp-null(3)
                    backup via 20.155.171.155, Ethernet46, label imp-null(3)
 21232   A[1]
                via M, ::, forward
                    EgressACL: apply
                  via TI-LFA tunnel index 4
                    via 20.149.171.149, Ethernet24, label imp-null(3)
                    backup via 20.155.171.155, Ethernet46, label imp-null(3)
 21254   A[1]
                via M, ::, forward
                    EgressACL: apply
                  via TI-LFA tunnel index 4
                    via 20.149.171.149, Ethernet24, label imp-null(3)
                    backup via 20.155.171.155, Ethernet46, label imp-null(3)
 21257   A[1]
                via M, forward
                    EgressACL: apply
                    20.149.171.149 Ethernet24
                    20.155.171.155 Ethernet46
 21279   A[1]
                via M, ::, forward
                    EgressACL: apply
                  via TI-LFA tunnel index 11
                    via 20.155.171.155, Ethernet46, label imp-null(3)
                    backup via 20.149.171.149, Ethernet24, label 21157
 21311   A[1]
                via M, ::, forward
                    EgressACL: apply
                  via TI-LFA tunnel index 4
                    via 20.149.171.149, Ethernet24, label imp-null(3)
                    backup via 20.155.171.155, Ethernet46, label imp-null(3)
 21324   A[1]
                via M, forward
                    EgressACL: apply
                    20.155.171.155 Ethernet46
 21349   A[1]
                via M, ::, pop
                    EgressACL: apply
                  via TI-LFA tunnel index 5
                    via 20.149.171.149, Ethernet24, label imp-null(3)
                    backup via 20.155.171.155, Ethernet46, label 21349
 21354   A[1]
                via M, ::, forward
                    EgressACL: apply
                  via TI-LFA tunnel index 4
                    via 20.149.171.149, Ethernet24, label imp-null(3)
                    backup via 20.155.171.155, Ethernet46, label imp-null(3)
 21355   A[1]
                via M, ::, pop
                    EgressACL: apply
                  via TI-LFA tunnel index 8
                    via 20.155.171.155, Ethernet46, label imp-null(3)
                    backup via 20.149.171.149, Ethernet24, label 21355
 21357   A[1]
                via M, forward
                    EgressACL: apply
                    20.155.171.155 Ethernet46
 21379   A[1]
                via M, forward
                    EgressACL: apply
                    20.149.171.149 Ethernet24
                    20.155.171.155 Ethernet46
 21411   A[1]
                via M, forward
                    EgressACL: apply
                    20.155.171.155 Ethernet46
 21449   A[1]
                via M, ::, pop
                    EgressACL: apply
                  via TI-LFA tunnel index 0
                    via 20.149.171.149, Ethernet24, label imp-null(3)
                    backup via 20.155.171.155, Ethernet46, label 21449
 21454   A[1]
                via M, ::, forward
                    EgressACL: apply
                  via TI-LFA tunnel index 4
                    via 20.149.171.149, Ethernet24, label imp-null(3)
                    backup via 20.155.171.155, Ethernet46, label imp-null(3)
 21455   A[1]
                via M, ::, pop
                    EgressACL: apply
                  via TI-LFA tunnel index 1
                    via 20.155.171.155, Ethernet46, label imp-null(3)
                    backup via 20.149.171.149, Ethernet24, label 21455
 21554   A[1]
                via M, forward
                    EgressACL: apply
                    20.155.171.155 Ethernet46
 21555   A[1]
                via M, ::, pop
                    EgressACL: apply
                  via TI-LFA tunnel index 9
                    via 20.155.171.155, Ethernet46, label imp-null(3)
                    backup via 20.149.171.149, Ethernet24, label 21555
 21649   A[1]
                via M, ::, pop
                    EgressACL: apply
                  via TI-LFA tunnel index 10
                    via 20.149.171.149, Ethernet24, label imp-null(3)
                    backup via 20.155.171.155, Ethernet46, label 21649
 21655   A[1]
                via M, pop
                    EgressACL: apply
                    20.155.171.155 Ethernet46
 362144  A[1]
                via M, 20.149.171.149, pop
                    EgressACL: apply
                    directly connected, Ethernet24
                    c0:f8:7f:6a:4e:1c, vlan 1008
 362146  A[1]
                via M, 20.155.171.155, pop
                    EgressACL: apply
                    directly connected, Ethernet46
                    34:88:18:bf:4a:30, vlan 1050
 378528   [0]
                via I, ipv4, vrf ISIS-SR-L3VPN
 378529   [0]
                via I, ipv4, vrf ISIS-SR-FLEXALGO-MIN-DELAY
 378530   [0]
                via I, ipv4, vrf ISIS-SR-FLEXALGO-MIN-TE
 378531   [0]
                via I, ipv4, vrf ISIS-SR-FLEXALGO-MIN-IGP
 378532   [0]
                via I, ipv4, vrf ISIS-SR-FLEXALGO-MIN-IGP-ADMIN
```

## show mpls lfib route

```text
MPLS forwarding table (Label [metric] Vias) - 50 routes 
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
                via TI-LFA tunnel index 4, forward
                 payload autoDecide, ttlMode uniform, dscpMode uniform, apply egress-acl
                    via 20.149.171.149, Ethernet24, label imp-null(3)
                    backup via 20.155.171.155, Ethernet46, label imp-null(3)
 IP    20019    [1], 10.0.0.19/32
                via M, 20.149.171.149, forward
                 payload autoDecide, ttlMode uniform, dscpMode uniform, apply egress-acl
                 interface Ethernet24
 IP    20024    [1], 10.0.0.24/32
                via TI-LFA tunnel index 4, forward
                 payload autoDecide, ttlMode uniform, dscpMode uniform, apply egress-acl
                    via 20.149.171.149, Ethernet24, label imp-null(3)
                    backup via 20.155.171.155, Ethernet46, label imp-null(3)
 IP    20032    [1], 10.0.0.32/32
                via TI-LFA tunnel index 4, forward
                 payload autoDecide, ttlMode uniform, dscpMode uniform, apply egress-acl
                    via 20.149.171.149, Ethernet24, label imp-null(3)
                    backup via 20.155.171.155, Ethernet46, label imp-null(3)
 IP    20057    [1], 10.0.0.57/32
                via M, 20.149.171.149, forward
                 payload autoDecide, ttlMode uniform, dscpMode uniform, apply egress-acl
                 interface Ethernet24
                via M, 20.155.171.155, forward
                 payload autoDecide, ttlMode uniform, dscpMode uniform, apply egress-acl
                 interface Ethernet46
 IP    20083    [1], 10.0.0.83/32
                via TI-LFA tunnel index 4, forward
                 payload autoDecide, ttlMode uniform, dscpMode uniform, apply egress-acl
                    via 20.149.171.149, Ethernet24, label imp-null(3)
                    backup via 20.155.171.155, Ethernet46, label imp-null(3)
 IP    20111    [1], 100.0.1.111/32
                via TI-LFA tunnel index 4, forward
                 payload autoDecide, ttlMode uniform, dscpMode uniform, apply egress-acl
                    via 20.149.171.149, Ethernet24, label imp-null(3)
                    backup via 20.155.171.155, Ethernet46, label imp-null(3)
 IP    20254    [1], 10.0.0.254/32
                via TI-LFA tunnel index 4, forward
                 payload autoDecide, ttlMode uniform, dscpMode uniform, apply egress-acl
                    via 20.149.171.149, Ethernet24, label imp-null(3)
                    backup via 20.155.171.155, Ethernet46, label imp-null(3)
 IP    20349    [1], 10.0.1.49/32
                via TI-LFA tunnel index 7, pop
                 payload autoDecide, ttlMode uniform, dscpMode uniform, apply egress-acl
                    via 20.149.171.149, Ethernet24, label imp-null(3)
                    backup via 20.155.171.155, Ethernet46, label 20349
 IP    20355    [1], 10.0.1.55/32
                via TI-LFA tunnel index 3, pop
                 payload autoDecide, ttlMode uniform, dscpMode uniform, apply egress-acl
                    via 20.155.171.155, Ethernet46, label imp-null(3)
                    backup via 20.149.171.149, Ethernet24, label 20355
 IP    20379    [1], 10.0.0.179/32
                via TI-LFA tunnel index 2, forward
                 payload autoDecide, ttlMode uniform, dscpMode uniform, apply egress-acl
                    via 20.155.171.155, Ethernet46, label imp-null(3)
                    backup via 20.149.171.149, Ethernet24, label 20057
 IP    21005    [1], 10.0.0.5/32, algorithm MIN-LATENCY
                via TI-LFA tunnel index 4, forward
                 payload autoDecide, ttlMode uniform, dscpMode uniform, apply egress-acl
                    via 20.149.171.149, Ethernet24, label imp-null(3)
                    backup via 20.155.171.155, Ethernet46, label imp-null(3)
 IP    21024    [1], 10.0.0.24/32, algorithm MIN-LATENCY
                via TI-LFA tunnel index 4, forward
                 payload autoDecide, ttlMode uniform, dscpMode uniform, apply egress-acl
                    via 20.149.171.149, Ethernet24, label imp-null(3)
                    backup via 20.155.171.155, Ethernet46, label imp-null(3)
 IP    21032    [1], 10.0.0.32/32, algorithm MIN-LATENCY
                via TI-LFA tunnel index 4, forward
                 payload autoDecide, ttlMode uniform, dscpMode uniform, apply egress-acl
                    via 20.149.171.149, Ethernet24, label imp-null(3)
                    backup via 20.155.171.155, Ethernet46, label imp-null(3)
 IP    21057    [1], 10.0.0.57/32, algorithm MIN-LATENCY
                via TI-LFA tunnel index 6, forward
                 payload autoDecide, ttlMode uniform, dscpMode uniform, apply egress-acl
                    via 20.155.171.155, Ethernet46, label imp-null(3)
                    backup via 20.149.171.149, Ethernet24, label 24009
 IP    21105    [1], 10.0.0.5/32, algorithm MIN-TE
                via TI-LFA tunnel index 4, forward
                 payload autoDecide, ttlMode uniform, dscpMode uniform, apply egress-acl
                    via 20.149.171.149, Ethernet24, label imp-null(3)
                    backup via 20.155.171.155, Ethernet46, label imp-null(3)
 IP    21111    [1], 100.0.1.111/32, algorithm MIN-LATENCY
                via TI-LFA tunnel index 4, forward
                 payload autoDecide, ttlMode uniform, dscpMode uniform, apply egress-acl
                    via 20.149.171.149, Ethernet24, label imp-null(3)
                    backup via 20.155.171.155, Ethernet46, label imp-null(3)
 IP    21124    [1], 10.0.0.24/32, algorithm MIN-TE
                via TI-LFA tunnel index 4, forward
                 payload autoDecide, ttlMode uniform, dscpMode uniform, apply egress-acl
                    via 20.149.171.149, Ethernet24, label imp-null(3)
                    backup via 20.155.171.155, Ethernet46, label imp-null(3)
 IP    21132    [1], 10.0.0.32/32, algorithm MIN-TE
                via TI-LFA tunnel index 4, forward
                 payload autoDecide, ttlMode uniform, dscpMode uniform, apply egress-acl
                    via 20.149.171.149, Ethernet24, label imp-null(3)
                    backup via 20.155.171.155, Ethernet46, label imp-null(3)
 IP    21157    [1], 10.0.0.57/32, algorithm MIN-TE
                via M, 20.149.171.149, forward
                 payload autoDecide, ttlMode uniform, dscpMode uniform, apply egress-acl
                 interface Ethernet24
                via M, 20.155.171.155, forward
                 payload autoDecide, ttlMode uniform, dscpMode uniform, apply egress-acl
                 interface Ethernet46
 IP    21179    [1], 10.0.0.179/32, algorithm MIN-LATENCY
                via TI-LFA tunnel index 6, forward
                 payload autoDecide, ttlMode uniform, dscpMode uniform, apply egress-acl
                    via 20.155.171.155, Ethernet46, label imp-null(3)
                    backup via 20.149.171.149, Ethernet24, label 24009
 IP    21205    [1], 10.0.0.5/32, algorithm MIN-IGP
                via TI-LFA tunnel index 4, forward
                 payload autoDecide, ttlMode uniform, dscpMode uniform, apply egress-acl
                    via 20.149.171.149, Ethernet24, label imp-null(3)
                    backup via 20.155.171.155, Ethernet46, label imp-null(3)
 IP    21211    [1], 100.0.1.111/32, algorithm MIN-TE
                via TI-LFA tunnel index 4, forward
                 payload autoDecide, ttlMode uniform, dscpMode uniform, apply egress-acl
                    via 20.149.171.149, Ethernet24, label imp-null(3)
                    backup via 20.155.171.155, Ethernet46, label imp-null(3)
 IP    21224    [1], 10.0.0.24/32, algorithm MIN-IGP
                via TI-LFA tunnel index 4, forward
                 payload autoDecide, ttlMode uniform, dscpMode uniform, apply egress-acl
                    via 20.149.171.149, Ethernet24, label imp-null(3)
                    backup via 20.155.171.155, Ethernet46, label imp-null(3)
 IP    21232    [1], 10.0.0.32/32, algorithm MIN-IGP
                via TI-LFA tunnel index 4, forward
                 payload autoDecide, ttlMode uniform, dscpMode uniform, apply egress-acl
                    via 20.149.171.149, Ethernet24, label imp-null(3)
                    backup via 20.155.171.155, Ethernet46, label imp-null(3)
 IP    21254    [1], 10.0.0.254/32, algorithm MIN-LATENCY
                via TI-LFA tunnel index 4, forward
                 payload autoDecide, ttlMode uniform, dscpMode uniform, apply egress-acl
                    via 20.149.171.149, Ethernet24, label imp-null(3)
                    backup via 20.155.171.155, Ethernet46, label imp-null(3)
 IP    21257    [1], 10.0.0.57/32, algorithm MIN-IGP
                via M, 20.149.171.149, forward
                 payload autoDecide, ttlMode uniform, dscpMode uniform, apply egress-acl
                 interface Ethernet24
                via M, 20.155.171.155, forward
                 payload autoDecide, ttlMode uniform, dscpMode uniform, apply egress-acl
                 interface Ethernet46
 IP    21279    [1], 10.0.0.179/32, algorithm MIN-TE
                via TI-LFA tunnel index 11, forward
                 payload autoDecide, ttlMode uniform, dscpMode uniform, apply egress-acl
                    via 20.155.171.155, Ethernet46, label imp-null(3)
                    backup via 20.149.171.149, Ethernet24, label 21157
 IP    21311    [1], 100.0.1.111/32, algorithm MIN-IGP
                via TI-LFA tunnel index 4, forward
                 payload autoDecide, ttlMode uniform, dscpMode uniform, apply egress-acl
                    via 20.149.171.149, Ethernet24, label imp-null(3)
                    backup via 20.155.171.155, Ethernet46, label imp-null(3)
 IP    21324    [1], 10.0.0.24/32, algorithm MIN-IGP-ADMIN
                via M, 20.155.171.155, forward
                 payload autoDecide, ttlMode uniform, dscpMode uniform, apply egress-acl
                 interface Ethernet46
 IP    21349    [1], 10.0.1.49/32, algorithm MIN-LATENCY
                via TI-LFA tunnel index 5, pop
                 payload autoDecide, ttlMode uniform, dscpMode uniform, apply egress-acl
                    via 20.149.171.149, Ethernet24, label imp-null(3)
                    backup via 20.155.171.155, Ethernet46, label 21349
 IP    21354    [1], 10.0.0.254/32, algorithm MIN-TE
                via TI-LFA tunnel index 4, forward
                 payload autoDecide, ttlMode uniform, dscpMode uniform, apply egress-acl
                    via 20.149.171.149, Ethernet24, label imp-null(3)
                    backup via 20.155.171.155, Ethernet46, label imp-null(3)
 IP    21355    [1], 10.0.1.55/32, algorithm MIN-LATENCY
                via TI-LFA tunnel index 8, pop
                 payload autoDecide, ttlMode uniform, dscpMode uniform, apply egress-acl
                    via 20.155.171.155, Ethernet46, label imp-null(3)
                    backup via 20.149.171.149, Ethernet24, label 21355
 IP    21357    [1], 10.0.0.57/32, algorithm MIN-IGP-ADMIN
                via M, 20.155.171.155, forward
                 payload autoDecide, ttlMode uniform, dscpMode uniform, apply egress-acl
                 interface Ethernet46
 IP    21379    [1], 10.0.0.179/32, algorithm MIN-IGP
                via M, 20.149.171.149, forward
                 payload autoDecide, ttlMode uniform, dscpMode uniform, apply egress-acl
                 interface Ethernet24
                via M, 20.155.171.155, forward
                 payload autoDecide, ttlMode uniform, dscpMode uniform, apply egress-acl
                 interface Ethernet46
 IP    21411    [1], 100.0.1.111/32, algorithm MIN-IGP-ADMIN
                via M, 20.155.171.155, forward
                 payload autoDecide, ttlMode uniform, dscpMode uniform, apply egress-acl
                 interface Ethernet46
 IP    21449    [1], 10.0.1.49/32, algorithm MIN-TE
                via TI-LFA tunnel index 0, pop
                 payload autoDecide, ttlMode uniform, dscpMode uniform, apply egress-acl
                    via 20.149.171.149, Ethernet24, label imp-null(3)
                    backup via 20.155.171.155, Ethernet46, label 21449
 IP    21454    [1], 10.0.0.254/32, algorithm MIN-IGP
                via TI-LFA tunnel index 4, forward
                 payload autoDecide, ttlMode uniform, dscpMode uniform, apply egress-acl
                    via 20.149.171.149, Ethernet24, label imp-null(3)
                    backup via 20.155.171.155, Ethernet46, label imp-null(3)
 IP    21455    [1], 10.0.1.55/32, algorithm MIN-TE
                via TI-LFA tunnel index 1, pop
                 payload autoDecide, ttlMode uniform, dscpMode uniform, apply egress-acl
                    via 20.155.171.155, Ethernet46, label imp-null(3)
                    backup via 20.149.171.149, Ethernet24, label 21455
 IP    21554    [1], 10.0.0.254/32, algorithm MIN-IGP-ADMIN
                via M, 20.155.171.155, forward
                 payload autoDecide, ttlMode uniform, dscpMode uniform, apply egress-acl
                 interface Ethernet46
 IP    21555    [1], 10.0.1.55/32, algorithm MIN-IGP
                via TI-LFA tunnel index 9, pop
                 payload autoDecide, ttlMode uniform, dscpMode uniform, apply egress-acl
                    via 20.155.171.155, Ethernet46, label imp-null(3)
                    backup via 20.149.171.149, Ethernet24, label 21555
 IP    21649    [1], 10.0.1.49/32, algorithm MIN-IGP
                via TI-LFA tunnel index 10, pop
                 payload autoDecide, ttlMode uniform, dscpMode uniform, apply egress-acl
                    via 20.149.171.149, Ethernet24, label imp-null(3)
                    backup via 20.155.171.155, Ethernet46, label 21649
 IP    21655    [1], 10.0.1.55/32, algorithm MIN-IGP-ADMIN
                via M, 20.155.171.155, pop
                 payload autoDecide, ttlMode uniform, dscpMode uniform, apply egress-acl
                 interface Ethernet46
 IA    362144   [1]
                via M, 20.149.171.149, pop
                 payload autoDecide, ttlMode uniform, apply egress-acl
                 interface Ethernet24
 IA    362146   [1]
                via M, 20.155.171.155, pop
                 payload autoDecide, ttlMode uniform, apply egress-acl
                 interface Ethernet46
 B3    378528   [0]
                via I, ipv4, vrf ISIS-SR-L3VPN
 B3    378529   [0]
                via I, ipv4, vrf ISIS-SR-FLEXALGO-MIN-DELAY
 B3    378530   [0]
                via I, ipv4, vrf ISIS-SR-FLEXALGO-MIN-TE
 B3    378531   [0]
                via I, ipv4, vrf ISIS-SR-FLEXALGO-MIN-IGP
 B3    378532   [0]
                via I, ipv4, vrf ISIS-SR-FLEXALGO-MIN-IGP-ADMIN
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
 * >      RD: 10.0.0.57:2 IPv4 prefix 20.57.112.0/24
                                 10.0.0.57             -       100     0       i Or-ID: 10.0.0.57 C-LST: 10.0.1.49 
 * >      RD: 10.0.0.83:2 IPv4 prefix 20.83.111.0/24
                                 10.0.0.83             -       100     0       i Or-ID: 10.0.0.83 C-LST: 10.0.1.49 
 * >      RD: 65000:1 IPv4 prefix 20.111.111.0/24
                                 100.0.1.111           -       0       0       i Or-ID: 194.0.0.1 C-LST: 10.0.1.49 
 * >      RD: 65000:2 IPv4 prefix 20.111.111.0/24
                                 100.0.1.111           -       0       0       i Or-ID: 194.0.0.1 C-LST: 10.0.1.49 
 * >      RD: 65000:3 IPv4 prefix 20.111.111.0/24
                                 100.0.1.111           -       0       0       i Or-ID: 194.0.0.1 C-LST: 10.0.1.49 
 * >      RD: 65000:4 IPv4 prefix 20.111.111.0/24
                                 100.0.1.111           -       0       0       i Or-ID: 194.0.0.1 C-LST: 10.0.1.49 
 * >      RD: 65000:5 IPv4 prefix 20.111.111.0/24
                                 100.0.1.111           -       0       0       i Or-ID: 194.0.0.1 C-LST: 10.0.1.49 
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
 * >      RD: 10.0.0.179:1806 IPv4 prefix 20.111.179.0/24
                                 10.0.0.179            -       100     0       i Or-ID: 10.0.0.179 C-LST: 10.0.1.49 
 * >      RD: 10.0.0.179:1807 IPv4 prefix 20.111.179.0/24
                                 10.0.0.179            -       100     0       i Or-ID: 10.0.0.179 C-LST: 10.0.1.49 
 * >      RD: 10.0.0.179:1808 IPv4 prefix 20.111.179.0/24
                                 10.0.0.179            -       100     0       i Or-ID: 10.0.0.179 C-LST: 10.0.1.49 
 * >      RD: 65000:1254 IPv4 prefix 20.111.254.0/24
                                 10.0.0.254            0       100     0       ? Or-ID: 10.0.0.254 C-LST: 10.0.1.49 
 * >      RD: 65000:1354 IPv4 prefix 20.111.254.0/24
                                 10.0.0.254            0       100     0       ? Or-ID: 10.0.0.254 C-LST: 10.0.1.49 
 * >      RD: 65000:1454 IPv4 prefix 20.111.254.0/24
                                 10.0.0.254            0       100     0       ? Or-ID: 10.0.0.254 C-LST: 10.0.1.49 
 * >      RD: 65000:1554 IPv4 prefix 20.111.254.0/24
                                 10.0.0.254            0       100     0       ? Or-ID: 10.0.0.254 C-LST: 10.0.1.49 
 * >      RD: 10.0.1.55:130 IPv4 prefix 55.55.55.130/32
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
  Last read 00:00:56, last write 00:00:17
  Hold time is 180, keepalive interval is 60 seconds
  Configured hold time is 180, keepalive interval is 60 seconds
  Effective minimum hold time is 3 seconds
  Send failure hold time is 0 seconds
  Hold timer is active, time left: 00:02:04
  Keepalive timer is active, time left: 00:00:37
  Connect timer is inactive
  Idle-restart timer is inactive
  BGP state is Established, up for 1d01h
  Number of transitions to established: 1
  Last state was OpenConfirm
  Last event was ReapplyInboundPolicy
  Last sent socket-error:Connect (Network is unreachable), Last time 1d01h, First time 1d01h, Repeats 6
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
  BGP session driven failover for IPv4 Unicast is disabled
  BGP session driven failover for IPv6 Unicast is disabled
  Message Statistics:
                         Sent      Rcvd
    Opens:                  1         1
    Notifications:          0         0
    Updates:                7       400
    Keepalives:          1778      1469
    Route Refresh:          0         0
    Total messages:      1786      1870
  Prefix Statistics:
                                   Sent      Rcvd     Best Paths     Best ECMP Paths
    IPv4 Unicast:                     0         0              0                   0
    VPN-IPv4:                         4        45             45                   0
    IPv6 Unicast:                     0         0              0                   0
  Configured maximum total number of routes is 0
  Inbound updates dropped by reason:
    AS path loop detection: 0
    Cluster ID loop detection: 0
    Enforced First AS: 0
    Malformed MPBGP routes: 0
    Originator ID matches local router ID: 0
    Nexthop matches local IP address: 6
    Unexpected IPv6 nexthop for IPv4 routes: 0
  Inbound updates with attribute errors:
    Resulting in removal of all paths in update (treat as withdraw): 6
    Resulting in AFI/SAFI disable: 0
    Resulting in attribute ignore: 0
    Disabled AFI/SAFIs: None
    Last treat-as-withdraw attribute error: Nexthop is local address
    Last update with error received at: 22:48:27
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
Local TCP address is 10.0.0.171, local port is 179
Remote TCP address is 10.0.1.49, remote port is 23088
Local next hop for next hop self:
  VPN-IPv4: 10.0.0.171
TCP Socket Information:
  TCP state is ESTABLISHED
  Recv-Q: 0/32768
  Send-Q: 0/46080
  Outgoing Maximum Segment Size (MSS): 1240
  Total Number of TCP retransmissions: 0
  Options:
    Timestamps enabled: no
    Selective Acknowledgments enabled: no
    Window Scale enabled: yes
    Explicit Congestion Notification (ECN) enabled: no
  Socket Statistics:
    Window Scale (wscale): 0,7
    Retransmission Timeout (rto): 404.0ms
    Round-trip Time (rtt/rtvar): 200.3ms/0.9ms
    Delayed Ack Timeout (ato): 40.0ms
    Congestion Window (cwnd): 10
    TCP Throughput: 0.50 Mbps
    Recv Round-trip Time (rcv_rtt): 519974.6ms
    Advertised Recv Window (rcv_space): 64326

```

## show tunnel rib system-tunnel-rib brief

```text
Tunnel RIB: system-tunnel-rib
Endpoint        Tunnel Type     Index(es)   Tunnel Preference   IGP Preference 
--------------- -------------- ----------- ------------------- ----------------
10.0.0.5/32     IS-IS SR IPv4   12          200                 115            
10.0.0.19/32    IS-IS SR IPv4   4           200                 115            
10.0.0.24/32    IS-IS SR IPv4   11          200                 115            
10.0.0.32/32    IS-IS SR IPv4   9           200                 115            
10.0.0.57/32    IS-IS SR IPv4   7           200                 115            
10.0.0.83/32    IS-IS SR IPv4   1           200                 115            
10.0.0.179/32   IS-IS SR IPv4   8           200                 115            
10.0.0.254/32   IS-IS SR IPv4   6           200                 115            
10.0.1.49/32    IS-IS SR IPv4   3           200                 115            
10.0.1.55/32    IS-IS SR IPv4   5           200                 115            
100.0.1.111/32  IS-IS SR IPv4   10          200                 115            

   IGP Metric    Metric Type
---------------- -----------
   30            metric     
   20            metric     
   20            metric     
   20            metric     
   20            metric     
   20            metric     
   20            metric     
   20            metric     
   10            metric     
   10            metric     
   20            metric     

```

## show tunnel rib colored brief

```text
Tunnel RIB: system-colored-tunnel-rib
 Endpoint         Color   Tunnel Type      Index(es)    Tunnel Preference    IGP Preference    IGP Metric   Metric Type
---------------- ------- ---------------- ------------ -------------------- ----------------- ------------- -----------
 10.0.0.5/32      128     IS-IS FlexAlgo   36           65                   115               13           metric     
 10.0.0.5/32      129     IS-IS FlexAlgo   34           65                   115               24           metric     
 10.0.0.5/32      130     IS-IS FlexAlgo   35           65                   115               20           metric     
 10.0.0.24/32     128     IS-IS FlexAlgo   39           65                   115               13           metric     
 10.0.0.24/32     129     IS-IS FlexAlgo   38           65                   115               24           metric     
 10.0.0.24/32     130     IS-IS FlexAlgo   40           65                   115               20           metric     
 10.0.0.24/32     131     IS-IS FlexAlgo   37           65                   115               30           metric     
 10.0.0.32/32     128     IS-IS FlexAlgo   13           65                   115               13           metric     
 10.0.0.32/32     129     IS-IS FlexAlgo   9            65                   115               24           metric     
 10.0.0.32/32     130     IS-IS FlexAlgo   3            65                   115               20           metric     
 10.0.0.57/32     128     IS-IS FlexAlgo   15           65                   115               8            metric     
 10.0.0.57/32     129     IS-IS FlexAlgo   16           65                   115               24           metric     
 10.0.0.57/32     130     IS-IS FlexAlgo   17           65                   115               20           metric     
 10.0.0.57/32     131     IS-IS FlexAlgo   20           65                   115               20           metric     
 10.0.0.179/32    128     IS-IS FlexAlgo   19           65                   115               13           metric     
 10.0.0.179/32    129     IS-IS FlexAlgo   18           65                   115               24           metric     
 10.0.0.179/32    130     IS-IS FlexAlgo   25           65                   115               30           metric     
 10.0.0.254/32    128     IS-IS FlexAlgo   14           65                   115               13           metric     
 10.0.0.254/32    129     IS-IS FlexAlgo   12           65                   115               24           metric     
 10.0.0.254/32    130     IS-IS FlexAlgo   10           65                   115               20           metric     
 10.0.0.254/32    131     IS-IS FlexAlgo   11           65                   115               30           metric     
 10.0.1.49/32     128     IS-IS FlexAlgo   4            65                   115               2            metric     
 10.0.1.49/32     129     IS-IS FlexAlgo   6            65                   115               12           metric     
 10.0.1.49/32     130     IS-IS FlexAlgo   2            65                   115               10           metric     
 10.0.1.55/32     128     IS-IS FlexAlgo   8            65                   115               2            metric     
 10.0.1.55/32     129     IS-IS FlexAlgo   7            65                   115               12           metric     
 10.0.1.55/32     130     IS-IS FlexAlgo   1            65                   115               10           metric     
 10.0.1.55/32     131     IS-IS FlexAlgo   5            65                   115               10           metric     
 100.0.1.111/32   128     IS-IS FlexAlgo   28           65                   115               13           metric     
 100.0.1.111/32   129     IS-IS FlexAlgo   29           65                   115               24           metric     
 100.0.1.111/32   130     IS-IS FlexAlgo   26           65                   115               20           metric     
 100.0.1.111/32   131     IS-IS FlexAlgo   27           65                   115               30           metric     

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
>C    10.0.0.171/32 [0 pref/0 metric] updated 1d01h ago
         via Loopback0, directly connected
>C    20.149.171.0/24 [0 pref/0 metric] updated 1d01h ago
         via Ethernet24, directly connected
>C    20.155.171.0/24 [0 pref/0 metric] updated 23:15:07 ago
         via Ethernet46, directly connected
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
>P    0.0.0.0/8 [1 pref/0 metric] updated 1d01h ago
         via Null0, directly connected [NF]
>P    127.0.0.0/8 [1 pref/0 metric] updated 1d01h ago
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
>I    10.0.0.5/32 [115 pref/30 metric] updated 03:11:13 ago
         via 20.149.171.149, Ethernet24
>I    10.0.0.19/32 [115 pref/20 metric] updated 01:33:10 ago
         via 20.149.171.149, Ethernet24
>I    10.0.0.24/32 [115 pref/20 metric] updated 00:18:07 ago
         via 20.149.171.149, Ethernet24
>I    10.0.0.32/32 [115 pref/20 metric] updated 00:09:04 ago
         via 20.149.171.149, Ethernet24
>I    10.0.0.57/32 [115 pref/20 metric] updated 04:27:14 ago
         via 20.149.171.149, Ethernet24
         via 20.155.171.155, Ethernet46
>I    10.0.0.83/32 [115 pref/20 metric] updated 1d01h ago
         via 20.149.171.149, Ethernet24
>I    10.0.0.179/32 [115 pref/20 metric] updated 00:31:06 ago
         via 20.155.171.155, Ethernet46
>I    10.0.0.254/32 [115 pref/20 metric] updated 03:31:15 ago
         via 20.149.171.149, Ethernet24
>I    10.0.1.49/32 [115 pref/10 metric] updated 1d01h ago
         via 20.149.171.149, Ethernet24
>I    10.0.1.55/32 [115 pref/10 metric] updated 23:15:05 ago
         via 20.155.171.155, Ethernet46
>I    20.5.149.0/24 [115 pref/20 metric] updated 03:11:17 ago
         via 20.149.171.149, Ethernet24
>I    20.19.149.0/24 [115 pref/20 metric] updated 1d01h ago
         via 20.149.171.149, Ethernet24
>I    20.24.149.0/24 [115 pref/20 metric] updated 21:29:54 ago
         via 20.149.171.149, Ethernet24
>I    20.32.149.0/24 [115 pref/20 metric] updated 00:09:22 ago
         via 20.149.171.149, Ethernet24
>I    20.32.211.0/24 [115 pref/30 metric] updated 00:09:04 ago
         via 20.149.171.149, Ethernet24
>I    20.47.149.0/24 [115 pref/20 metric] updated 1d01h ago
         via 20.149.171.149, Ethernet24
>I    20.57.59.0/24 [115 pref/30 metric] updated 03:14:49 ago
         via 20.149.171.149, Ethernet24
         via 20.155.171.155, Ethernet46
>I    20.57.149.0/24 [115 pref/20 metric] updated 1d01h ago
         via 20.149.171.149, Ethernet24
>I    20.57.155.0/24 [115 pref/20 metric] updated 23:11:24 ago
         via 20.155.171.155, Ethernet46
>I    20.57.179.0/24 [115 pref/30 metric] updated 00:31:14 ago
         via 20.149.171.149, Ethernet24
         via 20.155.171.155, Ethernet46
>I    20.57.211.0/24 [115 pref/30 metric] updated 04:27:14 ago
         via 20.149.171.149, Ethernet24
         via 20.155.171.155, Ethernet46
>I    20.83.149.0/24 [115 pref/20 metric] updated 1d01h ago
         via 20.149.171.149, Ethernet24
>I    20.111.149.0/24 [115 pref/20 metric] updated 03:48:48 ago
         via 20.149.171.149, Ethernet24
>I    20.149.155.0/24 [115 pref/20 metric] updated 23:15:05 ago
         via 20.149.171.149, Ethernet24
         via 20.155.171.155, Ethernet46
>I    20.149.254.0/24 [115 pref/20 metric] updated 1d01h ago
         via 20.149.171.149, Ethernet24
>I    20.155.179.0/24 [115 pref/20 metric] updated 00:31:17 ago
         via 20.155.171.155, Ethernet46
>I    100.0.1.111/32 [115 pref/20 metric] updated 00:34:04 ago
         via 20.149.171.149, Ethernet24
>I    192.168.0.0/19 [115 pref/20 metric] updated 01:33:10 ago
         via 20.149.171.149, Ethernet24
>I    192.168.20.0/23 [115 pref/20 metric] updated 00:18:07 ago
         via 20.149.171.149, Ethernet24
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
>P    ::/96 [1 pref/0 metric] updated 22:48:30 ago
         via Null0, directly connected [NF]
>P    ::ffff:127.0.0.0/104 [1 pref/0 metric] updated 22:48:30 ago
         via :: [1 pref/1 metric] type ipv6
            via , directly connected
>P    fe80::/10 [1 pref/0 metric] updated 22:48:30 ago
```

## show platform sand l3 summary

```text
Number of vrfs: 7

Ipv4:
  Routes:       124  backlog:  0  unprogrammed:  0
  Adjacencies:  135  backlog:  0  unprogrammed:  0
Ipv6:
  Routes:       0    backlog:  0  unprogrammed:  0
  Adjacencies:  135  backlog:  0  unprogrammed:  0
Mpls:
  Routes:       45  backlog:  0  unprogrammed:  0
  Adjacencies:  2   backlog:  0  unprogrammed:  0

Jericho2 Ip Fecs:
  Non-ecmp fecs:  4189  ecmp fecs:  2  fec entries:  4193
Jericho2 Mpls Fecs:
  Non-ecmp fecs:  2  ecmp fecs:  0  fec entries:  2
Jericho2 Vxlan Tunnel Fecs:
  Non-ecmp fecs:  0  ecmp fecs:  0  fec entries:  0
  Number of vxlan tunnels configured: 0

Jericho2 Lpm Routes:
  Routes:   124  unprogrammed:   0   
  Routes6:  1    unprogrammed6:  0   
  Backlog:  0  

Jericho2 Lpm:
  TCAM entries used:   3   Percent free:  99  ADS2 entries used:   8  Percent free:  99
  Pivot buckets used:  4   Rows used:     1   Entries Per Bucket:  2  Percent free:  99
  Route buckets used:  20  Rows used:     4   Entries Per Bucket:  6  Percent free:  99

Lem:
  IPv4  Host in Lem:            disabled
  IPv4  Prefix-lengths in Lem:  None    
  IPv6  Host in Lem:            disabled
  IPv6  Prefix-lengths in Lem:  None    
  Number of downloads:        0
  Number of overflow events:  0

Egress Arp rewrite entries in use (in each fap):
  FixedSystem: 6
Egress Arp remote rewrite entries in use (in each fap):
  FixedSystem: 0
Egress Ip tunnel rewrite entries in use (in each fap):
  FixedSystem: 0
Egress Mpls (for outer 2 labels) rewrite entries in use (in each fap):
  FixedSystem: 0
Egress Mpls (for inner 2 labels) rewrite entries in use (in each fap):
  FixedSystem: 52
Egress Sflow rewrite entries in use (in each fap):
  FixedSystem: 0

Egress rewrite chains in backlog: resource-full 0, no-interface 0

Glem entries used per fap :
  FixedSystem: 4212

Jericho2 Fec:
  Maximum FEC hierarchy levels:  2
  ReusedEcmp:  9  allocs:  465  frees:  370  shuffles:  0  cmds:  0
  Zombies:     0    purges:    0
  Quarantine:  0/0  shuffles:  0  deletes:  0   
  Fec insertion failures:  0
  Level1  Fecs:
    Non-ecmp fecs:            0    ecmp fecs:            1 
    Non-ecmp (Percent free):  100  ecmp (Percent free):  99
  Level2  Fecs:
    Non-ecmp fecs:            76  ecmp fecs:            0  
    Non-ecmp (Percent free):  99  ecmp (Percent free):  100
  Level3  Fecs:
    Non-ecmp fecs:            118  ecmp fecs:            2 
    Non-ecmp (Percent free):  99   ecmp (Percent free):  99

Lpm Detail:
  Requests:  963  cleanses:  362  batches:  362  avg batch size:  2

Jericho Arp:
  ArpTable writes:      21346  queued      0   
  IngressTable writes:  80611  queued      0   
  Coprocessors:         1      in CmdRing

Tunnel Counter Status
  Number of MPLS tunnels:                  110  
  Number of uncountable MPLS tunnels:      25   
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
|0  |10.0.0.5/32       |ROUTE| Et24               |1008 |103421  | c0:f8:7f:6a:4e:1c |  -  |528490|   -   
|0  |10.0.0.19/32      |ROUTE| Et24               |1008 |103421  | c0:f8:7f:6a:4e:1c |  -  |528490|   -   
|0  |10.0.0.24/32      |ROUTE| Et24               |1008 |103421  | c0:f8:7f:6a:4e:1c |  -  |528490|   -   
|0  |10.0.0.32/32      |ROUTE| Et24               |1008 |103421  | c0:f8:7f:6a:4e:1c |  -  |528490|   -   
|0  |10.0.0.57/32      |ROUTE| Et24               |1008 |103421  | c0:f8:7f:6a:4e:1c |24579|528526|   -   
|0  |10.0.0.57/32      |ROUTE| Et46               |1050 |103424  | 34:88:18:bf:4a:30 |24579|528527|   -   
|0  |10.0.0.57/32      |ROUTE| Et46               |1050 |103424  | 34:88:18:bf:4a:30 |24579|528528|   -   
|0  |10.0.0.57/32      |ROUTE| Et24               |1008 |103421  | c0:f8:7f:6a:4e:1c |24579|528529|   -   
|0  |10.0.0.83/32      |ROUTE| Et24               |1008 |103421  | c0:f8:7f:6a:4e:1c |  -  |528490|   -   
|0  |10.0.0.171/32     |TRAP | CoppSystemIpUcast  |0    |  -     | Receive           |  -  |524291|   -   
|0  |10.0.0.179/32     |ROUTE| Et46               |1050 |103424  | 34:88:18:bf:4a:30 |  -  |528524|   -   
|0  |10.0.0.254/32     |ROUTE| Et24               |1008 |103421  | c0:f8:7f:6a:4e:1c |  -  |528490|   -   
|0  |10.0.1.49/32      |ROUTE| Et24               |1008 |103421  | c0:f8:7f:6a:4e:1c |  -  |528490|   -   
|0  |10.0.1.55/32      |ROUTE| Et46               |1050 |103424  | 34:88:18:bf:4a:30 |  -  |528524|   -   
|0  |20.5.149.0/24     |ROUTE| Et24               |1008 |103421  | c0:f8:7f:6a:4e:1c |  -  |528490|   -   
|0  |20.19.149.0/24    |ROUTE| Et24               |1008 |103421  | c0:f8:7f:6a:4e:1c |  -  |528490|   -   
|0  |20.24.149.0/24    |ROUTE| Et24               |1008 |103421  | c0:f8:7f:6a:4e:1c |  -  |528490|   -   
|0  |20.32.149.0/24    |ROUTE| Et24               |1008 |103421  | c0:f8:7f:6a:4e:1c |  -  |528490|   -   
|0  |20.32.211.0/24    |ROUTE| Et24               |1008 |103421  | c0:f8:7f:6a:4e:1c |  -  |528490|   -   
|0  |20.47.149.0/24    |ROUTE| Et24               |1008 |103421  | c0:f8:7f:6a:4e:1c |  -  |528490|   -   
|0  |20.57.59.0/24     |ROUTE| Et24               |1008 |103421  | c0:f8:7f:6a:4e:1c |24579|528526|   -   
|0  |20.57.59.0/24     |ROUTE| Et46               |1050 |103424  | 34:88:18:bf:4a:30 |24579|528527|   -   
|0  |20.57.59.0/24     |ROUTE| Et46               |1050 |103424  | 34:88:18:bf:4a:30 |24579|528528|   -   
|0  |20.57.59.0/24     |ROUTE| Et24               |1008 |103421  | c0:f8:7f:6a:4e:1c |24579|528529|   -   
|0  |20.57.149.0/24    |ROUTE| Et24               |1008 |103421  | c0:f8:7f:6a:4e:1c |  -  |528490|   -   
|0  |20.57.155.0/24    |ROUTE| Et46               |1050 |103424  | 34:88:18:bf:4a:30 |  -  |528524|   -   
|0  |20.57.179.0/24    |ROUTE| Et24               |1008 |103421  | c0:f8:7f:6a:4e:1c |24579|528526|   -   
|0  |20.57.179.0/24    |ROUTE| Et46               |1050 |103424  | 34:88:18:bf:4a:30 |24579|528527|   -   
|0  |20.57.179.0/24    |ROUTE| Et46               |1050 |103424  | 34:88:18:bf:4a:30 |24579|528528|   -   
|0  |20.57.179.0/24    |ROUTE| Et24               |1008 |103421  | c0:f8:7f:6a:4e:1c |24579|528529|   -   
|0  |20.57.211.0/24    |ROUTE| Et24               |1008 |103421  | c0:f8:7f:6a:4e:1c |24579|528526|   -   
|0  |20.57.211.0/24    |ROUTE| Et46               |1050 |103424  | 34:88:18:bf:4a:30 |24579|528527|   -   
|0  |20.57.211.0/24    |ROUTE| Et46               |1050 |103424  | 34:88:18:bf:4a:30 |24579|528528|   -   
|0  |20.57.211.0/24    |ROUTE| Et24               |1008 |103421  | c0:f8:7f:6a:4e:1c |24579|528529|   -   
|0  |20.83.149.0/24    |ROUTE| Et24               |1008 |103421  | c0:f8:7f:6a:4e:1c |  -  |528490|   -   
|0  |20.111.149.0/24   |ROUTE| Et24               |1008 |103421  | c0:f8:7f:6a:4e:1c |  -  |528490|   -   
|0  |20.149.155.0/24   |ROUTE| Et24               |1008 |103421  | c0:f8:7f:6a:4e:1c |24579|528526|   -   
|0  |20.149.155.0/24   |ROUTE| Et46               |1050 |103424  | 34:88:18:bf:4a:30 |24579|528527|   -   
|0  |20.149.155.0/24   |ROUTE| Et46               |1050 |103424  | 34:88:18:bf:4a:30 |24579|528528|   -   
|0  |20.149.155.0/24   |ROUTE| Et24               |1008 |103421  | c0:f8:7f:6a:4e:1c |24579|528529|   -   
|0  |20.149.171.0/32   |TRAP | CoppSystemIpBcast  |0    |  -     | BcastReceive      |  -  |524288|   -   
|0  |20.149.171.149/32 |ROUTE| Et24               |1008 |103421  | c0:f8:7f:6a:4e:1c |  -  |528486|   -   
|0  |20.149.171.171/32 |TRAP | CoppSystemIpUcast  |0    |  -     | Receive           |  -  |524291|   -   
|0  |20.149.171.255/32 |TRAP | CoppSystemIpBcast  |0    |  -     | BcastReceive      |  -  |524288|   -   
|0  |20.149.171.0/24   |TRAP | CoppSystemL3DstMiss|1008 |1008    | ArpTrap           |  -  |525302|   -   
|0  |20.149.254.0/24   |ROUTE| Et24               |1008 |103421  | c0:f8:7f:6a:4e:1c |  -  |528490|   -   
|0  |20.155.171.0/32   |TRAP | CoppSystemIpBcast  |0    |  -     | BcastReceive      |  -  |524288|   -   
|0  |20.155.171.155/32 |ROUTE| Et46               |1050 |103424  | 34:88:18:bf:4a:30 |  -  |528514|   -   
|0  |20.155.171.171/32 |TRAP | CoppSystemIpUcast  |0    |  -     | Receive           |  -  |524291|   -   
|0  |20.155.171.255/32 |TRAP | CoppSystemIpBcast  |0    |  -     | BcastReceive      |  -  |524288|   -   
|0  |20.155.171.0/24   |TRAP | CoppSystemL3DstMiss|1050 |1050    | ArpTrap           |  -  |525344|   -   
|0  |20.155.179.0/24   |ROUTE| Et46               |1050 |103424  | 34:88:18:bf:4a:30 |  -  |528524|   -   
|0  |100.0.1.111/32    |ROUTE| Et24               |1008 |103421  | c0:f8:7f:6a:4e:1c |  -  |528490|   -   
|0  |127.0.0.0/8       |TRAP | CoppSystemL3DstMiss|0    |  -     | ArpTrap           |  -  |524294|   -   
|0  |192.168.20.0/23   |ROUTE| Et24               |1008 |103421  | c0:f8:7f:6a:4e:1c |  -  |528490|   -   
|0  |192.168.0.0/19    |ROUTE| Et24               |1008 |103421  | c0:f8:7f:6a:4e:1c |  -  |528490|   -   
|0  |0.0.0.0/0         |TRAP | CoppSystemL3LpmOver|0    |  -     | SlowReceive       |  -  |524292|   -   
|1  |0.0.0.0/8         |DROP | DROP               |0    |  -     |                   |  -  |528484|   -   
|1  |127.0.0.0/8       |TRAP | CoppSystemL3DstMiss|0    |  -     | ArpTrap           |  -  |524294|   -   
|1  |192.168.20.0/32   |TRAP | CoppSystemIpBcast  |0    |  -     | BcastReceive      |  -  |524288|   -   
|1  |192.168.20.171/32 |TRAP | CoppSystemIpUcast  |0    |  -     | Receive           |  -  |524291|   -   
|1  |192.168.21.255/32 |TRAP | CoppSystemIpBcast  |0    |  -     | BcastReceive      |  -  |524288|   -   
|1  |192.168.20.0/23   |TRAP | CoppSystemL3DstMiss|0    |  -     | ArpTrap           |  -  |524294|   -   
|1  |0.0.0.0/0         |TRAP | CoppSystemL3DstMiss|0    |  -     | ArpTrap           |  -  |524294|   -   
|2  |0.0.0.0/8         |DROP | DROP               |0    |  -     |                   |  -  |528566|   -   
|2  |20.5.111.0/24     |ROUTE| FEC 528594         |0    |2097147 | 00:00:00:00:00:00 |  -  |288418|M 62000
|2  |20.19.111.0/24    |ROUTE| FEC 528498         |0    |2097134 | 00:00:00:00:00:00 |  -  |288360|M 20019 1279
|2  |20.55.111.0/24    |ROUTE| FEC 528578         |0    |2097100 | 00:00:00:00:00:00 |  -  |288364|M 24004
|2  |20.57.111.0/24    |ROUTE| FEC 24577          |0    |2097097 | 00:00:00:00:00:00 |  -  |288368|M 20057 524287
|2  |20.83.111.0/24    |ROUTE| FEC 528546         |0    |2097124 | 00:00:00:00:00:00 |  -  |288362|M 18
|2  |127.0.0.0/8       |TRAP | CoppSystemL3DstMiss|0    |  -     | ArpTrap           |  -  |524294|   -   
|2  |0.0.0.0/0         |TRAP | CoppSystemL3LpmOver|0    |  -     | SlowReceive       |  -  |524292|   -   
|3  |0.0.0.0/8         |DROP | DROP               |0    |  -     |                   |  -  |528494|   -   
|3  |20.5.111.0/24     |ROUTE| FEC 528582         |0    |2097131 | 00:00:00:00:00:00 |  -  |288434|M 62004
|3  |20.19.111.0/24    |ROUTE| FEC 528498         |0    |2097135 | 00:00:00:00:00:00 |  -  |288392|M 20019 1277
|3  |20.24.111.0/24    |ROUTE| FEC 528552         |0    |2097148 | 00:00:00:00:00:00 |  -  |288416|M 56507
|3  |20.32.111.0/24    |ROUTE| FEC 528534         |0    |2097145 | 00:00:00:00:00:00 |  -  |288410|M 756643
|3  |20.57.111.0/24    |ROUTE| FEC 528564         |0    |2097103 | 00:00:00:00:00:00 |  -  |288372|M 524286
|3  |20.111.111.0/24   |ROUTE| FEC 528506         |0    |2097150 | 00:00:00:00:00:00 |  -  |288414|M 17
|3  |20.111.155.0/24   |ROUTE| FEC 528576         |0    |2097094 | 00:00:00:00:00:00 |  -  |288374|M 24009
|3  |20.111.171.0/32   |TRAP | CoppSystemIpBcast  |0    |  -     | BcastReceive      |  -  |524288|   -   
|3  |20.111.171.128/32 |ROUTE| Et5                |1007 |103422  | 00:14:01:00:00:01 |  -  |528500|   -   
|3  |20.111.171.171/32 |TRAP | CoppSystemIpUcast  |0    |  -     | Receive           |  -  |524291|   -   
|3  |20.111.171.255/32 |TRAP | CoppSystemIpBcast  |0    |  -     | BcastReceive      |  -  |524288|   -   
|3  |20.111.171.0/24   |TRAP | CoppSystemL3DstMiss|1007 |1007    | ArpTrap           |  -  |525301|   -   
|3  |20.111.179.0/24   |ROUTE| FEC 528590         |0    |2097138 | 00:00:00:00:00:00 |  -  |288426|M 16
|3  |20.111.254.0/24   |ROUTE| FEC 528560         |0    |2097121 | 00:00:00:00:00:00 |  -  |288390|M 48091
|3  |127.0.0.0/8       |TRAP | CoppSystemL3DstMiss|0    |  -     | ArpTrap           |  -  |524294|   -   
|3  |0.0.0.0/0         |TRAP | CoppSystemL3LpmOver|0    |  -     | SlowReceive       |  -  |524292|   -   
|4  |0.0.0.0/8         |DROP | DROP               |0    |  -     |                   |  -  |528488|   -   
|4  |20.5.111.0/24     |ROUTE| FEC 528584         |0    |2097146 | 00:00:00:00:00:00 |  -  |288420|M 62005
|4  |20.19.111.0/24    |ROUTE| FEC 528498         |0    |2097132 | 00:00:00:00:00:00 |  -  |288432|M 20019 1276
|4  |20.24.111.0/24    |ROUTE| FEC 528508         |0    |2097143 | 00:00:00:00:00:00 |  -  |288376|M 56506
|4  |20.32.111.0/24    |ROUTE| FEC 528596         |0    |2097129 | 00:00:00:00:00:00 |  -  |288412|M 756644
|4  |20.57.111.0/24    |ROUTE| FEC 24577          |0    |2097104 | 00:00:00:00:00:00 |  -  |288378|M 21157 524284
|4  |20.111.111.0/24   |ROUTE| FEC 528548         |0    |2097141 | 00:00:00:00:00:00 |  -  |288396|M 18
|4  |20.111.155.0/24   |ROUTE| FEC 528572         |0    |2097099 | 00:00:00:00:00:00 |  -  |288384|M 24010
|4  |20.111.171.0/32   |TRAP | CoppSystemIpBcast  |0    |  -     | BcastReceive      |  -  |524288|   -   
|4  |20.111.171.129/32 |ROUTE| Et5                |1010 |103425  | 00:14:01:00:00:02 |  -  |528592|   -   
|4  |20.111.171.171/32 |TRAP | CoppSystemIpUcast  |0    |  -     | Receive           |  -  |524291|   -   
|4  |20.111.171.255/32 |TRAP | CoppSystemIpBcast  |0    |  -     | BcastReceive      |  -  |524288|   -   
|4  |20.111.171.0/24   |TRAP | CoppSystemL3DstMiss|1010 |1010    | ArpTrap           |  -  |525304|   -   
|4  |20.111.179.0/24   |ROUTE| FEC 528580         |0    |2097133 | 00:00:00:00:00:00 |  -  |288430|M 17
|4  |20.111.254.0/24   |ROUTE| FEC 528536         |0    |2097114 | 00:00:00:00:00:00 |  -  |288452|M 48092
|4  |127.0.0.0/8       |TRAP | CoppSystemL3DstMiss|0    |  -     | ArpTrap           |  -  |524294|   -   
|4  |0.0.0.0/0         |TRAP | CoppSystemL3LpmOver|0    |  -     | SlowReceive       |  -  |524292|   -   
|5  |0.0.0.0/8         |DROP | DROP               |0    |  -     |                   |  -  |528512|   -   
|5  |20.5.111.0/24     |ROUTE| FEC 528532         |0    |2097130 | 00:00:00:00:00:00 |  -  |288422|M 62006
|5  |20.19.111.0/24    |ROUTE| FEC 528498         |0    |2097149 | 00:00:00:00:00:00 |  -  |288408|M 20019 1275
|5  |20.24.111.0/24    |ROUTE| FEC 528530         |0    |2097142 | 00:00:00:00:00:00 |  -  |288394|M 56505
|5  |20.32.111.0/24    |ROUTE| FEC 528598         |0    |2097128 | 00:00:00:00:00:00 |  -  |288404|M 756645
|5  |20.57.111.0/24    |ROUTE| FEC 24577          |0    |2097101 | 00:00:00:00:00:00 |  -  |288382|M 21257 524283
|5  |20.111.111.0/24   |ROUTE| FEC 528518         |0    |2097140 | 00:00:00:00:00:00 |  -  |288398|M 19
|5  |20.111.155.0/24   |ROUTE| FEC 528574         |0    |2097137 | 00:00:00:00:00:00 |  -  |288402|M 24012
|5  |20.111.171.0/32   |TRAP | CoppSystemIpBcast  |0    |  -     | BcastReceive      |  -  |524288|   -   
|5  |20.111.171.130/32 |ROUTE| Et5                |1011 |103427  | 00:14:01:00:00:03 |  -  |528558|   -   
|5  |20.111.171.171/32 |TRAP | CoppSystemIpUcast  |0    |  -     | Receive           |  -  |524291|   -   
|5  |20.111.171.255/32 |TRAP | CoppSystemIpBcast  |0    |  -     | BcastReceive      |  -  |524288|   -   
|5  |20.111.171.0/24   |TRAP | CoppSystemL3DstMiss|1011 |1011    | ArpTrap           |  -  |525305|   -   
|5  |20.111.179.0/24   |ROUTE| FEC 24577          |0    |2097136 | 00:00:00:00:00:00 |  -  |288428|M 21379 18
|5  |20.111.254.0/24   |ROUTE| FEC 528550         |0    |2097123 | 00:00:00:00:00:00 |  -  |288388|M 48093
|5  |55.55.55.130/32   |ROUTE| FEC 528574         |0    |2097137 | 00:00:00:00:00:00 |  -  |288402|M 24012
|5  |127.0.0.0/8       |TRAP | CoppSystemL3DstMiss|0    |  -     | ArpTrap           |  -  |524294|   -   
|5  |0.0.0.0/0         |TRAP | CoppSystemL3LpmOver|0    |  -     | SlowReceive       |  -  |524292|   -   
|6  |0.0.0.0/8         |DROP | DROP               |0    |  -     |                   |  -  |528510|   -   
|6  |20.19.111.0/24    |ROUTE| FEC 528498         |0    |2097151 | 00:00:00:00:00:00 |  -  |288424|M 20019 1274
|6  |20.24.111.0/24    |ROUTE| FEC 528552         |0    |2097144 | 00:00:00:00:00:00 |  -  |288386|M 56504
|6  |20.57.111.0/24    |ROUTE| FEC 528522         |0    |2097105 | 00:00:00:00:00:00 |  -  |288370|M 21357 524282
|6  |20.111.111.0/24   |ROUTE| FEC 528522         |0    |2097139 | 00:00:00:00:00:00 |  -  |288400|M 21411 20
|6  |20.111.155.0/24   |ROUTE| FEC 528522         |0    |2097108 | 00:00:00:00:00:00 |  -  |288380|M 24011
|6  |20.111.171.0/32   |TRAP | CoppSystemIpBcast  |0    |  -     | BcastReceive      |  -  |524288|   -   
|6  |20.111.171.131/32 |ROUTE| Et5                |1012 |103423  | 00:14:01:00:00:04 |  -  |528502|   -   
|6  |20.111.171.171/32 |TRAP | CoppSystemIpUcast  |0    |  -     | Receive           |  -  |524291|   -   
|6  |20.111.171.255/32 |TRAP | CoppSystemIpBcast  |0    |  -     | BcastReceive      |  -  |524288|   -   
|6  |20.111.171.0/24   |TRAP | CoppSystemL3DstMiss|1012 |1012    | ArpTrap           |  -  |525306|   -   
|6  |20.111.254.0/24   |ROUTE| FEC 528522         |0    |2097125 | 00:00:00:00:00:00 |  -  |288366|M 21554 48094
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
|24577|528568|ROUTE| Et24               |1008 |103421  | c0:f8:7f:6a:4e:1c |   -   
|24577|528569|ROUTE| Et46               |1050 |103424  | 34:88:18:bf:4a:30 |   -   
|24577|528570|ROUTE| Et46               |1050 |103424  | 34:88:18:bf:4a:30 |   -   
|24577|528571|ROUTE| Et24               |1008 |103421  | c0:f8:7f:6a:4e:1c |   -   
|24579|528526|ROUTE| Et24               |1008 |103421  | c0:f8:7f:6a:4e:1c |   -   
|24579|528527|ROUTE| Et46               |1050 |103424  | 34:88:18:bf:4a:30 |   -   
|24579|528528|ROUTE| Et46               |1050 |103424  | 34:88:18:bf:4a:30 |   -   
|24579|528529|ROUTE| Et24               |1008 |103421  | c0:f8:7f:6a:4e:1c |   -   
|  -  |288360|ROUTE| FEC 528498         |   - |2097134 |                 - |Mpush 20019 1279
|  -  |288362|ROUTE| FEC 528546         |   - |2097124 |                 - |Mpush 18
|  -  |288364|ROUTE| FEC 528578         |   - |2097100 |                 - |Mpush 24004
|  -  |288366|ROUTE| FEC 528522         |   - |2097125 |                 - |Mpush 21554 48094
|  -  |288368|ROUTE| FEC 24577          |   - |2097097 |                 - |Mpush 20057 524287
|  -  |288370|ROUTE| FEC 528522         |   - |2097105 |                 - |Mpush 21357 524282
|  -  |288372|ROUTE| FEC 528564         |   - |2097103 |                 - |Mpush 524286
|  -  |288374|ROUTE| FEC 528576         |   - |2097094 |                 - |Mpush 24009
|  -  |288376|ROUTE| FEC 528508         |   - |2097143 |                 - |Mpush 56506
|  -  |288378|ROUTE| FEC 24577          |   - |2097104 |                 - |Mpush 21157 524284
|  -  |288380|ROUTE| FEC 528522         |   - |2097108 |                 - |Mpush 24011
|  -  |288382|ROUTE| FEC 24577          |   - |2097101 |                 - |Mpush 21257 524283
|  -  |288384|ROUTE| FEC 528572         |   - |2097099 |                 - |Mpush 24010
|  -  |288386|ROUTE| FEC 528552         |   - |2097144 |                 - |Mpush 56504
|  -  |288388|ROUTE| FEC 528550         |   - |2097123 |                 - |Mpush 48093
|  -  |288390|ROUTE| FEC 528560         |   - |2097121 |                 - |Mpush 48091
|  -  |288392|ROUTE| FEC 528498         |   - |2097135 |                 - |Mpush 20019 1277
|  -  |288394|ROUTE| FEC 528530         |   - |2097142 |                 - |Mpush 56505
|  -  |288396|ROUTE| FEC 528548         |   - |2097141 |                 - |Mpush 18
|  -  |288398|ROUTE| FEC 528518         |   - |2097140 |                 - |Mpush 19
|  -  |288400|ROUTE| FEC 528522         |   - |2097139 |                 - |Mpush 21411 20
|  -  |288402|ROUTE| FEC 528574         |   - |2097137 |                 - |Mpush 24012
|  -  |288404|ROUTE| FEC 528598         |   - |2097128 |                 - |Mpush 756645
|  -  |288408|ROUTE| FEC 528498         |   - |2097149 |                 - |Mpush 20019 1275
|  -  |288410|ROUTE| FEC 528534         |   - |2097145 |                 - |Mpush 756643
|  -  |288412|ROUTE| FEC 528596         |   - |2097129 |                 - |Mpush 756644
|  -  |288414|ROUTE| FEC 528506         |   - |2097150 |                 - |Mpush 17
|  -  |288416|ROUTE| FEC 528552         |   - |2097148 |                 - |Mpush 56507
|  -  |288418|ROUTE| FEC 528594         |   - |2097147 |                 - |Mpush 62000
|  -  |288420|ROUTE| FEC 528584         |   - |2097146 |                 - |Mpush 62005
|  -  |288422|ROUTE| FEC 528532         |   - |2097130 |                 - |Mpush 62006
|  -  |288424|ROUTE| FEC 528498         |   - |2097151 |                 - |Mpush 20019 1274
|  -  |288426|ROUTE| FEC 528590         |   - |2097138 |                 - |Mpush 16
|  -  |288428|ROUTE| FEC 24577          |   - |2097136 |                 - |Mpush 21379 18
|  -  |288430|ROUTE| FEC 528580         |   - |2097133 |                 - |Mpush 17
|  -  |288432|ROUTE| FEC 528498         |   - |2097132 |                 - |Mpush 20019 1276
|  -  |288434|ROUTE| FEC 528582         |   - |2097131 |                 - |Mpush 62004
|  -  |288452|ROUTE| FEC 528536         |   - |2097114 |                 - |Mpush 48092
|  -  |524288|TRAP | CoppSystemIpBcast  |0    |  -     | BcastReceive      |   -   
|  -  |524291|TRAP | CoppSystemIpUcast  |0    |  -     | Receive           |   -   
|  -  |524292|TRAP | CoppSystemL3LpmOver|0    |  -     | SlowReceive       |   -   
|  -  |524293|TRAP | CoppSystemL3LpmOver|0    |  -     | SlowReceive       |   -   
|  -  |524294|TRAP | CoppSystemL3DstMiss|0    |  -     | ArpTrap           |   -   
|  -  |525301|TRAP | CoppSystemL3DstMiss|1007 |1007    | ArpTrap           |   -   
|  -  |525302|TRAP | CoppSystemL3DstMiss|1008 |1008    | ArpTrap           |   -   
|  -  |525304|TRAP | CoppSystemL3DstMiss|1010 |1010    | ArpTrap           |   -   
|  -  |525305|TRAP | CoppSystemL3DstMiss|1011 |1011    | ArpTrap           |   -   
|  -  |525306|TRAP | CoppSystemL3DstMiss|1012 |1012    | ArpTrap           |   -   
|  -  |525344|TRAP | CoppSystemL3DstMiss|1050 |1050    | ArpTrap           |   -   
|  -  |528482|DROP | DROP               |0    |  -     |                   |   -   
|  -  |528484|DROP | DROP               |0    |  -     |                   |   -   
|  -  |528486|ROUTE| Et24               |1008 |103421  | c0:f8:7f:6a:4e:1c |   -   
|  -  |528488|DROP | DROP               |0    |  -     |                   |   -   
|  -  |528490|ROUTE| Et24               |1008 |103421  | c0:f8:7f:6a:4e:1c |   -   
|  -  |528492|ROUTE| Et24               |1008 |103421  | c0:f8:7f:6a:4e:1c |   -   
|  -  |528494|DROP | DROP               |0    |  -     |                   |   -   
|  -  |528496|ROUTE| Et46               |1050 |103448  | 34:88:18:bf:4a:30 |   -   
|  -  |528497|ROUTE| Et24               |1008 |103449  | c0:f8:7f:6a:4e:1c |Mpush 21555
|  -  |528498|ROUTE| Et24               |1008 |103421  | c0:f8:7f:6a:4e:1c |   -   
|  -  |528500|ROUTE| Et5                |1007 |103422  | 00:14:01:00:00:01 |   -   
|  -  |528502|ROUTE| Et5                |1012 |103423  | 00:14:01:00:00:04 |   -   
|  -  |528504|ROUTE| Et46               |1050 |103436  | 34:88:18:bf:4a:30 |   -   
|  -  |528505|ROUTE| Et24               |1008 |103439  | c0:f8:7f:6a:4e:1c |Mpush 24009
|  -  |528506|ROUTE| Et24               |1008 |103438  | c0:f8:7f:6a:4e:1c |Mpush 21111
|  -  |528507|ROUTE| Et46               |1050 |103446  | 34:88:18:bf:4a:30 |Mpush 21111
|  -  |528508|ROUTE| Et24               |1008 |103469  | c0:f8:7f:6a:4e:1c |Mpush 21124
|  -  |528509|ROUTE| Et46               |1050 |103470  | 34:88:18:bf:4a:30 |Mpush 21124
|  -  |528510|DROP | DROP               |0    |  -     |                   |   -   
|  -  |528512|DROP | DROP               |0    |  -     |                   |   -   
|  -  |528514|ROUTE| Et46               |1050 |103424  | 34:88:18:bf:4a:30 |   -   
|  -  |528516|ROUTE| Et46               |1050 |103424  | 34:88:18:bf:4a:30 |   -   
|  -  |528518|ROUTE| Et24               |1008 |103451  | c0:f8:7f:6a:4e:1c |Mpush 21311
|  -  |528519|ROUTE| Et46               |1050 |103454  | 34:88:18:bf:4a:30 |Mpush 21311
|  -  |528520|ROUTE| Et24               |1008 |103480  | c0:f8:7f:6a:4e:1c |   -   
|  -  |528521|ROUTE| Et46               |1050 |103481  | 34:88:18:bf:4a:30 |Mpush 21449
|  -  |528522|ROUTE| Et46               |1050 |103424  | 34:88:18:bf:4a:30 |   -   
|  -  |528524|ROUTE| Et46               |1050 |103424  | 34:88:18:bf:4a:30 |   -   
|  -  |528530|ROUTE| Et24               |1008 |103471  | c0:f8:7f:6a:4e:1c |Mpush 21224
|  -  |528531|ROUTE| Et46               |1050 |103472  | 34:88:18:bf:4a:30 |Mpush 21224
|  -  |528532|ROUTE| Et24               |1008 |103459  | c0:f8:7f:6a:4e:1c |Mpush 21205
|  -  |528533|ROUTE| Et46               |1050 |103460  | 34:88:18:bf:4a:30 |Mpush 21205
|  -  |528534|ROUTE| Et24               |1008 |103465  | c0:f8:7f:6a:4e:1c |Mpush 21032
|  -  |528535|ROUTE| Et46               |1050 |103466  | 34:88:18:bf:4a:30 |Mpush 21032
|  -  |528536|ROUTE| Et24               |1008 |103518  | c0:f8:7f:6a:4e:1c |Mpush 21354
|  -  |528537|ROUTE| Et46               |1050 |103519  | 34:88:18:bf:4a:30 |Mpush 21354
|  -  |528538|ROUTE| Et46               |1050 |103442  | 34:88:18:bf:4a:30 |   -   
|  -  |528539|ROUTE| Et24               |1008 |103443  | c0:f8:7f:6a:4e:1c |Mpush 20355
|  -  |528540|ROUTE| Et24               |1008 |103482  | c0:f8:7f:6a:4e:1c |   -   
|  -  |528541|ROUTE| Et46               |1050 |103483  | 34:88:18:bf:4a:30 |Mpush 21649
|  -  |528542|ROUTE| Et24               |1008 |103426  | c0:f8:7f:6a:4e:1c |   -   
|  -  |528543|ROUTE| Et46               |1050 |103433  | 34:88:18:bf:4a:30 |   -   
|  -  |528544|ROUTE| Et24               |1008 |103452  | c0:f8:7f:6a:4e:1c |   -   
|  -  |528545|ROUTE| Et46               |1050 |103453  | 34:88:18:bf:4a:30 |Mpush 20349
|  -  |528546|ROUTE| Et24               |1008 |103504  | c0:f8:7f:6a:4e:1c |Mpush 20083
|  -  |528547|ROUTE| Et46               |1050 |103505  | 34:88:18:bf:4a:30 |Mpush 20083
|  -  |528548|ROUTE| Et24               |1008 |103447  | c0:f8:7f:6a:4e:1c |Mpush 21211
|  -  |528549|ROUTE| Et46               |1050 |103450  | 34:88:18:bf:4a:30 |Mpush 21211
|  -  |528550|ROUTE| Et24               |1008 |103475  | c0:f8:7f:6a:4e:1c |Mpush 21454
|  -  |528551|ROUTE| Et46               |1050 |103476  | 34:88:18:bf:4a:30 |Mpush 21454
|  -  |528552|ROUTE| Et24               |1008 |103467  | c0:f8:7f:6a:4e:1c |Mpush 21024
|  -  |528553|ROUTE| Et46               |1050 |103468  | 34:88:18:bf:4a:30 |Mpush 21024
|  -  |528554|ROUTE| Et46               |1050 |103444  | 34:88:18:bf:4a:30 |   -   
|  -  |528555|ROUTE| Et24               |1008 |103445  | c0:f8:7f:6a:4e:1c |Mpush 21455
|  -  |528556|ROUTE| Et24               |1008 |103484  | c0:f8:7f:6a:4e:1c |   -   
|  -  |528557|ROUTE| Et46               |1050 |103485  | 34:88:18:bf:4a:30 |Mpush 21349
|  -  |528558|ROUTE| Et5                |1011 |103427  | 00:14:01:00:00:03 |   -   
|  -  |528560|ROUTE| Et24               |1008 |103510  | c0:f8:7f:6a:4e:1c |Mpush 21254
|  -  |528561|ROUTE| Et46               |1050 |103511  | 34:88:18:bf:4a:30 |Mpush 21254
|  -  |528562|ROUTE| Et46               |1050 |103428  | 34:88:18:bf:4a:30 |   -   
|  -  |528563|ROUTE| Et24               |1008 |103431  | c0:f8:7f:6a:4e:1c |Mpush 20057
|  -  |528564|ROUTE| Et46               |1050 |103522  | 34:88:18:bf:4a:30 |Mpush 21057
|  -  |528565|ROUTE| Et24               |1008 |103523  | c0:f8:7f:6a:4e:1c |Mpush 24009 21057
|  -  |528566|DROP | DROP               |0    |  -     |                   |   -   
|  -  |528572|ROUTE| Et46               |1050 |103526  | 34:88:18:bf:4a:30 |   -   
|  -  |528573|ROUTE| Et24               |1008 |103527  | c0:f8:7f:6a:4e:1c |Mpush 21455
|  -  |528574|ROUTE| Et46               |1050 |103498  | 34:88:18:bf:4a:30 |   -   
|  -  |528575|ROUTE| Et24               |1008 |103499  | c0:f8:7f:6a:4e:1c |Mpush 21555
|  -  |528576|ROUTE| Et46               |1050 |103530  | 34:88:18:bf:4a:30 |   -   
|  -  |528577|ROUTE| Et24               |1008 |103531  | c0:f8:7f:6a:4e:1c |Mpush 21355
|  -  |528578|ROUTE| Et46               |1050 |103524  | 34:88:18:bf:4a:30 |   -   
|  -  |528579|ROUTE| Et24               |1008 |103525  | c0:f8:7f:6a:4e:1c |Mpush 20355
|  -  |528580|ROUTE| Et46               |1050 |103463  | 34:88:18:bf:4a:30 |Mpush 21279
|  -  |528581|ROUTE| Et24               |1008 |103464  | c0:f8:7f:6a:4e:1c |Mpush 21157 21279
|  -  |528582|ROUTE| Et24               |1008 |103461  | c0:f8:7f:6a:4e:1c |Mpush 21005
|  -  |528583|ROUTE| Et46               |1050 |103462  | 34:88:18:bf:4a:30 |Mpush 21005
|  -  |528584|ROUTE| Et24               |1008 |103457  | c0:f8:7f:6a:4e:1c |Mpush 21105
|  -  |528585|ROUTE| Et46               |1050 |103458  | 34:88:18:bf:4a:30 |Mpush 21105
|  -  |528586|ROUTE| Et46               |1050 |103440  | 34:88:18:bf:4a:30 |   -   
|  -  |528587|ROUTE| Et24               |1008 |103441  | c0:f8:7f:6a:4e:1c |Mpush 21355
|  -  |528588|ROUTE| Et46               |1050 |103432  | 34:88:18:bf:4a:30 |   -   
|  -  |528589|ROUTE| Et24               |1008 |103434  | c0:f8:7f:6a:4e:1c |Mpush 21157
|  -  |528590|ROUTE| Et46               |1050 |103455  | 34:88:18:bf:4a:30 |Mpush 21179
|  -  |528591|ROUTE| Et24               |1008 |103456  | c0:f8:7f:6a:4e:1c |Mpush 24009 21179
|  -  |528592|ROUTE| Et5                |1010 |103425  | 00:14:01:00:00:02 |   -   
|  -  |528594|ROUTE| Et24               |1008 |103429  | c0:f8:7f:6a:4e:1c |Mpush 20005
|  -  |528595|ROUTE| Et46               |1050 |103430  | 34:88:18:bf:4a:30 |Mpush 20005
|  -  |528596|ROUTE| Et24               |1008 |103477  | c0:f8:7f:6a:4e:1c |Mpush 21132
|  -  |528597|ROUTE| Et46               |1050 |103478  | 34:88:18:bf:4a:30 |Mpush 21132
|  -  |528598|ROUTE| Et24               |1008 |103479  | c0:f8:7f:6a:4e:1c |Mpush 21232
|  -  |528599|ROUTE| Et46               |1050 |103486  | 34:88:18:bf:4a:30 |Mpush 21232

```

