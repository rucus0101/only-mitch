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

Uptime: 4 hours and 42 minutes
Total memory: 65734516 kB
Free memory: 61679920 kB

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
Ethernet1        20.170.171.171/24    up        up               1500          
Ethernet5.128    20.111.171.171/24    up        up               1500          
Ethernet5.129    20.111.171.171/24    up        up               1500          
Ethernet5.130    20.111.171.171/24    up        up               1500          
Ethernet5.131    20.111.171.171/24    up        up               1500          
Ethernet24       20.149.171.171/24    up        up               1500          
Ethernet25       20.171.179.171/24    up        up               1500          
Ethernet46       20.155.171.171/24    up        up               1500          
Loopback0        10.0.0.171/32        up        up              65535          
Management1      192.168.20.171/23    up        up               1500          

```

## show interfaces counters rates | nz

```text
Port      Name             Intvl  In Mbps      %  In Kpps Out Mbps      %

Port      Out Kpps
```

## show isis neighbors

```text
 
Instance  VRF      System Id        Type Interface          SNPA              State Hold time   Circuit Id          
IGP       default  h49-N540-24Q8L2DD L2   Ethernet24         P2P               UP    24          00                  
IGP       default  h55-8201-24H8FH  L2   Ethernet46         P2P               UP    23          00                  
IGP       default  juniper_379_MX304 L2   Ethernet25         P2P               UP    20          01                  
IGP       default  Spine3-J-170     L2   Ethernet1          P2P               UP    28          3E                  
```

## show isis database detail

```text
Legend:
H - hostname conflict
U - node unreachable

IS-IS Instance: IGP VRF: default
  IS-IS Level 2 Link State Database
    LSPID                   Seq Num  Cksum  Life Length IS  Received LSPID        Flags
    0000.0000.0019.00-00        317   4917  1166    160 L2  0000.0000.0019.00-00  <>
      NLPID: 0xCC(IPv4)
      Area addresses: 49
      Interface address: 10.0.0.19
      Interface address: 20.19.149.19
      IS Neighbor          : h49-N540-24Q8L2DD.00 Metric: 10
        IPv4 Neighbor Address: 20.19.149.149
        IPv4 Interface Address: 20.19.149.19
        Adj-sid: 1151 flags: [L V] weight: 0x0
      Reachability         : 10.0.0.19/32 Metric: 0 Type: 1 Up
        SR Prefix-SID: 19 Flags: [N] Algorithm: 0
      Reachability         : 20.19.149.0/24 Metric: 10 Type: 1 Up
      Reachability         : 20.19.211.0/24 Metric: 0 Type: 1 Up
      Reachability         : 192.168.0.0/19 Metric: 0 Type: 1 Up
      Router Capabilities: Router Id: 10.0.0.19 Flags: []
        Maximum SID depth:
          Base MPLS imposition (MSD type 1):  13
        SR Capability: Flags: [I]
          SRGB Base: 20000 Range: 2000
        Algorithms:  0, 128, 129
        Flex Algo: Algorithm: 128 Metric: Min Unidirectional Delay Metric (1) Calc: SPF (0) Prio: 128
          Flags: [] 0x1
    eantc-jcnr2.00-00           453   1608   453    229 L2  0000.0000.0020.00-00  <>
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
    12502-1.00-00               668  24241  1178    515 L2  0000.0000.0024.00-00  <>
      NLPID: 0xCC(IPv4)
      Hostname: 12502-1
      Area addresses: 49
      Interface address: 10.0.0.24
      Interface address: 20.24.149.24
      Interface address: 20.24.211.24
      IS Neighbor          : h49-N540-24Q8L2DD.00 Metric: 10
        IPv4 Neighbor Address: 20.24.149.149
        IPv4 Interface Address: 20.24.149.24
        Adj-sid: 56381 flags: [L V] weight: 0x0
      IS Neighbor          : h49-N540-24Q8L2DD.00 Metric: 10
        IPv4 Neighbor Address: 20.24.149.149
        IPv4 Interface Address: 20.24.149.24
      Reachability         : 10.0.0.24/32 Metric: 0 Type: 1 Up
        SR Prefix-SID: 1024 Flags: [N P] Algorithm: 128
        SR Prefix-SID: 1124 Flags: [N P] Algorithm: 129
        SR Prefix-SID: 1224 Flags: [N P] Algorithm: 130
        SR Prefix-SID: 1324 Flags: [N P] Algorithm: 131
      Reachability         : 20.24.149.0/24 Metric: 10 Type: 1 Up
      Reachability         : 20.24.211.0/24 Metric: 10 Type: 1 Up
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
    huawei_34_NetEngine_8000_F8.00-00       148  54651   940    293 L2  0000.0000.0254.00-00  <>
      NLPID: 0xCC(IPv4)
      Hostname: huawei_34_NetEngine_8000_F8
      Area addresses: 49
      Interface address: 10.0.0.254
      Interface address: 20.171.254.254
      Interface address: 20.149.254.254
      IS Neighbor          : h49-N540-24Q8L2DD.00 Metric: 10
        IPv4 Neighbor Address: 20.149.254.149
        IPv4 Interface Address: 20.149.254.254
        Adj-sid: 48030 flags: [L V] weight: 0x0
      Reachability         : 10.0.0.254/32 Metric: 0 Type: 1 Up
        SR Prefix-SID: 254 Flags: [N] Algorithm: 0
        SR Prefix-SID: 1254 Flags: [N] Algorithm: 128
        SR Prefix-SID: 1354 Flags: [N] Algorithm: 129
        SR Prefix-SID: 1454 Flags: [N] Algorithm: 130
        SR Prefix-SID: 1554 Flags: [N] Algorithm: 131
      Reachability         : 20.171.254.0/24 Metric: 10 Type: 1 Up
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
    h49-N540-24Q8L2DD.00-00       262  64642   939   1328 L2  0000.0000.0349.00-00  <>
      NLPID: 0xCC(IPv4)
      Hostname: h49-N540-24Q8L2DD
      Area addresses: 49
      Interface address: 10.0.1.49
      IS Neighbor          : 0000.0000.0019.00   Metric: 10
        IPv4 Neighbor Address: 20.19.149.19
        IPv4 Interface Address: 20.19.149.149
        Adj-sid: 24005 flags: [L V] weight: 0x0
      IS Neighbor          : SR1-SRMPLS.00       Metric: 10
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
      IS Neighbor          : 0000.0000.0032.00   Metric: 10
        IPv4 Neighbor Address: 20.32.149.32
        IPv4 Interface Address: 20.32.149.149
        Adj-sid: 24003 flags: [L V] weight: 0x0
      IS Neighbor          : huawei_34_NetEngine_8000_F8.00 Metric: 10
        IPv4 Neighbor Address: 20.149.254.254
        IPv4 Interface Address: 20.149.254.149
        Adj-sid: 24001 flags: [L V] weight: 0x0
      IS Neighbor          : eantc-jcnr2.00      Metric: 10
        IPv4 Neighbor Address: 20.83.149.83
        IPv4 Interface Address: 20.83.149.149
        Adj-sid: 24021 flags: [L V] weight: 0x0
      IS Neighbor          : 3800.0000.4111.00   Metric: 10
        IPv4 Neighbor Address: 20.111.149.1
        IPv4 Interface Address: 20.111.149.149
        Adj-sid: 24015 flags: [L V] weight: 0x0
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
    h55-8201-24H8FH.00-00       160  64064   541    720 L2  0000.0000.0355.00-00  <>
      NLPID: 0xCC(IPv4)
      Hostname: h55-8201-24H8FH
      Area addresses: 49
      Interface address: 10.0.1.55
      IS Neighbor          : juniper_379_MX304.00 Metric: 10
        IPv4 Neighbor Address: 20.155.179.179
        IPv4 Interface Address: 20.155.179.155
        Adj-sid: 24003 flags: [L V] weight: 0x0
      IS Neighbor          : SR1-SRMPLS.00       Metric: 10
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
    juniper_379_MX304.00-00       100  31883  1143    440 L2  0000.0001.7900.00-00  <>
      Remaining lifetime received: 1198 s Modified to: 1200 s
      NLPID: 0xCC(IPv4) 0x8E(IPv6)
      Hostname: juniper_379_MX304
      Area addresses: 49.0001.00
      Interface address: 10.0.0.179
      IS Neighbor          : SR1-SRMPLS.00       Metric: 10
        IPv4 Neighbor Address: 20.57.179.57
        IPv4 Interface Address: 20.57.179.179
        Adj-sid: 17 flags: [L V] weight: 0x0
      IS Neighbor          : PE31-J2-171.00      Metric: 10
        IPv4 Neighbor Address: 20.171.179.171
        IPv4 Interface Address: 20.171.179.179
        Adj-sid: 23 flags: [L V] weight: 0x0
      IS Neighbor          : h55-8201-24H8FH.00  Metric: 10
        IPv4 Neighbor Address: 20.155.179.155
        IPv4 Interface Address: 20.155.179.179
        Adj-sid: 18 flags: [L V] weight: 0x0
      Reachability         : 20.155.179.0/24 Metric: 10 Type: 1 Up
      Reachability         : 20.57.179.0/24 Metric: 10 Type: 1 Up
      Reachability         : 10.0.0.179/32 Metric: 0 Type: 1 Up
        SR Prefix-SID: 379 Flags: [N] Algorithm: 0
        SR Prefix-SID: 1379 Flags: [N] Algorithm: 130
        SR Prefix-SID: 1279 Flags: [N] Algorithm: 129
        SR Prefix-SID: 1179 Flags: [N] Algorithm: 128
      Reachability         : 20.171.179.0/24 Metric: 10 Type: 1 Up
      Router Capabilities: Router Id: 10.0.0.179 Flags: []
        Maximum SID depth:
          Base MPLS imposition (MSD type 1):  4
        SR Capability: Flags: [I V]
          SRGB Base: 20000 Range: 2000
        Algorithms:  0, 1, 128, 129, 130
      Unsupported TLV: Type: 14 Length: 2
    0010.0010.0005.00-00         23  30543   719    280 L2  0010.0010.0005.00-00  <>
      NLPID: 0xCC(IPv4)
      Area addresses: 49.0005
      Interface address: 10.0.0.5
      IS Neighbor          : h49-N540-24Q8L2DD.00 Metric: 10
        IPv4 Neighbor Address: 20.5.149.149
        IPv4 Interface Address: 20.5.149.5
        Adj-sid: 16000 flags: [L V] weight: 0x0
      Reachability         : 20.5.149.0/24 Metric: 10 Type: 1 Up
      Reachability         : 10.0.0.5/32 Metric: 10 Type: 1 Up
        SR Prefix-SID: 5 Flags: [N] Algorithm: 0
        SR Prefix-SID: 1005 Flags: [N] Algorithm: 128
        SR Prefix-SID: 1105 Flags: [N] Algorithm: 129
        SR Prefix-SID: 1205 Flags: [N] Algorithm: 130
        SR Prefix-SID: 1305 Flags: [N] Algorithm: 131
      Router Capabilities: Router Id: 10.0.0.5 Flags: []
        Algorithms:  0, 130, 128, 129
    SR1-SRMPLS.00-00            726  53685  1177    832 L2  0100.0000.0057.00-00  <>
      Remaining lifetime received: 1199 s Modified to: 1200 s
      NLPID: 0xCC(IPv4) 0x8E(IPv6)
      Hostname: SR1-SRMPLS
      Area addresses: 49.0000.0000.0057.00
      Interface address: 10.0.0.57
      Interface address: 20.57.59.57
      Interface address: 20.57.149.57
      Interface address: 20.57.155.57
      Interface address: 20.57.170.57
      Interface address: 20.57.179.57
      Interface address: 20.57.211.57
      Interface address: 2002::57
      IS Neighbor (Narrow metrics, unsupported): Spine3-J-170.00     Metric: 10
      IS Neighbor (Narrow metrics, unsupported): h49-N540-24Q8L2DD.00 Metric: 10
      IS Neighbor (Narrow metrics, unsupported): h55-8201-24H8FH.00  Metric: 10
      IS Neighbor (Narrow metrics, unsupported): juniper_379_MX304.00 Metric: 10
      IS Neighbor          : Spine3-J-170.00     Metric: 10
        IPv4 Neighbor Address: 20.57.170.170
        IPv4 Interface Address: 20.57.170.57
        Adj-sid: 30170 flags: [L V B] weight: 0x0
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
      Reachability (Narrow metrics, unsupported): 20.57.170.0/24 Metric: 10 Type: 1
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
      Reachability         : 20.57.170.0/24 Metric: 10 Type: 1 Up
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
    Spine3-J-170.00-00          167  22094  1088    246 L2  0100.0000.0170.00-00  <>
      Remaining lifetime received: 1199 s Modified to: 1200 s
      NLPID: 0xCC(IPv4)
      Hostname: Spine3-J-170
      Area addresses: 49.0000
      Interface address: 20.32.170.170
      Interface address: 20.170.171.170
      Interface address: 20.47.170.170
      Interface address: 20.57.170.170
      Interface address: 20.170.254.170
      Interface address: 10.0.0.170
      IS Neighbor          : 0000.0000.0032.00   Metric: 10
      IS Neighbor          : SR1-SRMPLS.00       Metric: 10
        IPv4 Neighbor Address: 20.57.170.57
        IPv4 Interface Address: 20.57.170.170
        Adj-sid: 362145 flags: [L V] weight: 0x0
      IS Neighbor          : PE31-J2-171.00      Metric: 10
        IPv4 Neighbor Address: 20.170.171.171
        IPv4 Interface Address: 20.170.171.170
        Adj-sid: 362144 flags: [L V] weight: 0x0
      Reachability         : 20.32.170.0/24 Metric: 10 Type: 1 Up
      Reachability         : 20.170.171.0/24 Metric: 10 Type: 1 Up
      Reachability         : 20.47.170.0/24 Metric: 10 Type: 1 Up
      Reachability         : 20.57.170.0/24 Metric: 10 Type: 1 Up
      Reachability         : 20.170.254.0/24 Metric: 10 Type: 1 Up
      Reachability         : 10.0.0.170/32 Metric: 10 Type: 1 Up
        SR Prefix-SID: 170 Flags: [N] Algorithm: 0
      Router Capabilities: Router Id: 100.0.0.170 Flags: []
        SR Local Block:
          SRLB Base: 965536 Range: 65536
        Area leader priority: 250 algorithm: 0
        Maximum SID depth:
          Base MPLS imposition (MSD type 1):  6
        SR Capability: Flags: [I]
          SRGB Base: 20000 Range: 2000
    PE31-J2-171.00-00           173  51996   743    442 L2  0100.0000.0171.00-00  <>
      LSP generation remaining wait time: 0 ms
      Time remaining until refresh: 443 s
      NLPID: 0xCC(IPv4)
      Hostname: PE31-J2-171
      Area addresses: 49.0000
      Interface address: 20.171.179.171
      Interface address: 20.155.171.171
      Interface address: 20.170.171.171
      Interface address: 20.149.171.171
      Interface address: 10.0.0.171
      IS Neighbor          : juniper_379_MX304.00 Metric: 10
        IPv4 Neighbor Address: 20.171.179.179
        IPv4 Interface Address: 20.171.179.171
        Adj-sid: 362147 flags: [L V] weight: 0x0
      IS Neighbor          : h49-N540-24Q8L2DD.00 Metric: 10
        IPv4 Neighbor Address: 20.149.171.149
        IPv4 Interface Address: 20.149.171.171
        Adj-sid: 362144 flags: [L V] weight: 0x0
      IS Neighbor          : h55-8201-24H8FH.00  Metric: 10
        IPv4 Neighbor Address: 20.155.171.155
        IPv4 Interface Address: 20.155.171.171
        Adj-sid: 362146 flags: [L V] weight: 0x0
      IS Neighbor          : Spine3-J-170.00     Metric: 10
        IPv4 Neighbor Address: 20.170.171.170
        IPv4 Interface Address: 20.170.171.171
        Adj-sid: 362145 flags: [L V] weight: 0x0
      Reachability         : 20.171.179.0/24 Metric: 10 Type: 1 Up
      Reachability         : 20.155.171.0/24 Metric: 10 Type: 1 Up
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
    3800.0000.4111.00-00         14  19126   939    142 L2  3800.0000.4111.00-00  <DefaultAtt>
      NLPID: 0xCC(IPv4) 0x8E(IPv6) 0x81(CLNP)
      Area addresses: 49
      Interface address: 20.111.149.1
      IS Neighbor          : h49-N540-24Q8L2DD.00 Metric: 10
      Reachability         : 20.111.149.0/24 Metric: 10 Type: 1 Up
      Reachability         : 200.111.0.0/24 Metric: 0 Type: 1 Up
        SR Prefix-SID: 1111 Flags: [] Algorithm: 128
        SR Prefix-SID: 1211 Flags: [] Algorithm: 129
        SR Prefix-SID: 1311 Flags: [] Algorithm: 130
        SR Prefix-SID: 1411 Flags: [] Algorithm: 131
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
Destination: 3800.0000.4111
Path ID: 640
Path constraints: algo MIN-LATENCY
                  metric type MIN-DELAY
Request sequence number: 31
Response sequence number: 31
Number of times path updated: 31
Last updated: 0:00:21 ago
Metric: 13
Next Hop       Interface 
-------------- ----------
20.149.171.149 Ethernet24

Destination: 3800.0000.4111
Path ID: 641
Path constraints: algo MIN-TE
                  metric type TE
Request sequence number: 31
Response sequence number: 31
Number of times path updated: 31
Last updated: 0:00:21 ago
Metric: 24
Next Hop       Interface 
-------------- ----------
20.149.171.149 Ethernet24

Destination: 3800.0000.4111
Path ID: 642
Path constraints: algo MIN-IGP
                  metric type IGP
                  administrative-group exclude 1
Request sequence number: 31
Response sequence number: 31
Number of times path updated: 31
Last updated: 0:00:21 ago
Metric: 20
Next Hop       Interface 
-------------- ----------
20.149.171.149 Ethernet24

Destination: 3800.0000.4111
Path ID: 643
Path constraints: algo MIN-IGP-ADMIN
                  metric type IGP
                  administrative-group exclude 127
Request sequence number: 31
Response sequence number: 31
Number of times path updated: 31
Last updated: 0:00:21 ago
Metric: 30
Next Hop       Interface 
-------------- ----------
20.155.171.155 Ethernet46

Destination: 12502-1
Path ID: 640
Path constraints: algo MIN-LATENCY
                  metric type MIN-DELAY
Request sequence number: 370
Response sequence number: 370
Number of times path updated: 393
Last updated: 0:00:21 ago
Next Hop Interface
-------- ---------

Destination: 12502-1
Path ID: 641
Path constraints: algo MIN-TE
                  metric type TE
Request sequence number: 369
Response sequence number: 369
Number of times path updated: 393
Last updated: 0:00:21 ago
Next Hop Interface
-------- ---------

Destination: 12502-1
Path ID: 642
Path constraints: algo MIN-IGP
                  metric type IGP
                  administrative-group exclude 1
Request sequence number: 300
Response sequence number: 300
Number of times path updated: 299
Last updated: 0:00:21 ago
Next Hop Interface
-------- ---------

Destination: 12502-1
Path ID: 643
Path constraints: algo MIN-IGP-ADMIN
                  metric type IGP
                  administrative-group exclude 127
Request sequence number: 276
Response sequence number: 276
Number of times path updated: 275
Last updated: 0:00:21 ago
Next Hop Interface
-------- ---------

Destination: PE31-J2-171
Path ID: 640
Path constraints: algo MIN-LATENCY
                  metric type MIN-DELAY
Request sequence number: 463
Response sequence number: 463
Number of times path updated: 461
Last updated: 0:00:21 ago
Next Hop Interface
-------- ---------

Destination: PE31-J2-171
Path ID: 641
Path constraints: algo MIN-TE
                  metric type TE
Request sequence number: 463
Response sequence number: 463
Number of times path updated: 461
Last updated: 0:00:21 ago
Next Hop Interface
-------- ---------

Destination: PE31-J2-171
Path ID: 642
Path constraints: algo MIN-IGP
                  metric type IGP
                  administrative-group exclude 1
Request sequence number: 370
Response sequence number: 370
Number of times path updated: 369
Last updated: 0:00:21 ago
Next Hop Interface
-------- ---------

Destination: PE31-J2-171
Path ID: 643
Path constraints: algo MIN-IGP-ADMIN
                  metric type IGP
                  administrative-group exclude 127
Request sequence number: 330
Response sequence number: 330
Number of times path updated: 329
Last updated: 0:00:21 ago
Next Hop Interface
-------- ---------

Destination: SR1-SRMPLS
Path ID: 640
Path constraints: algo MIN-LATENCY
                  metric type MIN-DELAY
Request sequence number: 423
Response sequence number: 423
Number of times path updated: 434
Last updated: 0:00:21 ago
Metric: 13
Next Hop       Interface 
-------------- ----------
20.155.171.155 Ethernet46
20.149.171.149 Ethernet24

Destination: SR1-SRMPLS
Path ID: 641
Path constraints: algo MIN-TE
                  metric type TE
Request sequence number: 422
Response sequence number: 422
Number of times path updated: 429
Last updated: 0:00:21 ago
Metric: 24
Next Hop       Interface 
-------------- ----------
20.155.171.155 Ethernet46
20.149.171.149 Ethernet24

Destination: SR1-SRMPLS
Path ID: 642
Path constraints: algo MIN-IGP
                  metric type IGP
                  administrative-group exclude 1
Request sequence number: 329
Response sequence number: 329
Number of times path updated: 339
Last updated: 0:00:21 ago
Metric: 20
Next Hop       Interface 
-------------- ----------
20.155.171.155 Ethernet46
20.171.179.179 Ethernet25
20.149.171.149 Ethernet24

Destination: SR1-SRMPLS
Path ID: 643
Path constraints: algo MIN-IGP-ADMIN
                  metric type IGP
                  administrative-group exclude 127
Request sequence number: 303
Response sequence number: 303
Number of times path updated: 306
Last updated: 0:00:21 ago
Metric: 20
Next Hop       Interface 
-------------- ----------
20.155.171.155 Ethernet46

Destination: h49-N540-24Q8L2DD
Path ID: 640
Path constraints: algo MIN-LATENCY
                  metric type MIN-DELAY
Request sequence number: 466
Response sequence number: 466
Number of times path updated: 467
Last updated: 0:00:21 ago
Metric: 2
Next Hop       Interface 
-------------- ----------
20.149.171.149 Ethernet24

Destination: h49-N540-24Q8L2DD
Path ID: 641
Path constraints: algo MIN-TE
                  metric type TE
Request sequence number: 465
Response sequence number: 465
Number of times path updated: 464
Last updated: 0:00:21 ago
Metric: 12
Next Hop       Interface 
-------------- ----------
20.149.171.149 Ethernet24

Destination: h49-N540-24Q8L2DD
Path ID: 642
Path constraints: algo MIN-IGP
                  metric type IGP
                  administrative-group exclude 1
Request sequence number: 364
Response sequence number: 364
Number of times path updated: 372
Last updated: 0:00:21 ago
Metric: 10
Next Hop       Interface 
-------------- ----------
20.149.171.149 Ethernet24

Destination: h55-8201-24H8FH
Path ID: 640
Path constraints: algo MIN-LATENCY
                  metric type MIN-DELAY
Request sequence number: 466
Response sequence number: 466
Number of times path updated: 468
Last updated: 0:00:21 ago
Metric: 2
Next Hop       Interface 
-------------- ----------
20.155.171.155 Ethernet46

Destination: h55-8201-24H8FH
Path ID: 641
Path constraints: algo MIN-TE
                  metric type TE
Request sequence number: 465
Response sequence number: 465
Number of times path updated: 464
Last updated: 0:00:21 ago
Metric: 12
Next Hop       Interface 
-------------- ----------
20.155.171.155 Ethernet46

Destination: h55-8201-24H8FH
Path ID: 642
Path constraints: algo MIN-IGP
                  metric type IGP
                  administrative-group exclude 1
Request sequence number: 371
Response sequence number: 371
Number of times path updated: 372
Last updated: 0:00:21 ago
Metric: 10
Next Hop       Interface 
-------------- ----------
20.155.171.155 Ethernet46

Destination: h55-8201-24H8FH
Path ID: 643
Path constraints: algo MIN-IGP-ADMIN
                  metric type IGP
                  administrative-group exclude 127
Request sequence number: 327
Response sequence number: 327
Number of times path updated: 327
Last updated: 0:00:21 ago
Metric: 10
Next Hop       Interface 
-------------- ----------
20.155.171.155 Ethernet46

Destination: huawei_34_NetEngine_8000_F8
Path ID: 640
Path constraints: algo MIN-LATENCY
                  metric type MIN-DELAY
Request sequence number: 441
Response sequence number: 441
Number of times path updated: 441
Last updated: 0:00:21 ago
Metric: 13
Next Hop       Interface 
-------------- ----------
20.149.171.149 Ethernet24

Destination: huawei_34_NetEngine_8000_F8
Path ID: 641
Path constraints: algo MIN-TE
                  metric type TE
Request sequence number: 441
Response sequence number: 441
Number of times path updated: 439
Last updated: 0:00:21 ago
Metric: 24
Next Hop       Interface 
-------------- ----------
20.149.171.149 Ethernet24

Destination: huawei_34_NetEngine_8000_F8
Path ID: 642
Path constraints: algo MIN-IGP
                  metric type IGP
                  administrative-group exclude 1
Request sequence number: 348
Response sequence number: 348
Number of times path updated: 347
Last updated: 0:00:21 ago
Metric: 20
Next Hop       Interface 
-------------- ----------
20.149.171.149 Ethernet24

Destination: huawei_34_NetEngine_8000_F8
Path ID: 643
Path constraints: algo MIN-IGP-ADMIN
                  metric type IGP
                  administrative-group exclude 127
Request sequence number: 316
Response sequence number: 316
Number of times path updated: 315
Last updated: 0:00:21 ago
Metric: 30
Next Hop       Interface 
-------------- ----------
20.155.171.155 Ethernet46

Destination: juniper_379_MX304
Path ID: 640
Path constraints: algo MIN-LATENCY
                  metric type MIN-DELAY
Request sequence number: 409
Response sequence number: 409
Number of times path updated: 410
Last updated: 0:00:21 ago
Metric: 11
Next Hop       Interface 
-------------- ----------
20.171.179.179 Ethernet25

Destination: juniper_379_MX304
Path ID: 641
Path constraints: algo MIN-TE
                  metric type TE
Request sequence number: 408
Response sequence number: 408
Number of times path updated: 409
Last updated: 0:00:21 ago
Metric: 24
Next Hop       Interface 
-------------- ----------
20.155.171.155 Ethernet46

Destination: juniper_379_MX304
Path ID: 642
Path constraints: algo MIN-IGP
                  metric type IGP
                  administrative-group exclude 1
Request sequence number: 315
Response sequence number: 315
Number of times path updated: 315
Last updated: 0:00:21 ago
Metric: 10
Next Hop       Interface 
-------------- ----------
20.171.179.179 Ethernet25

```

## show isis segment-routing tunnel

```text
  Index     Endpoint          Next Hop/Tunnel Index     Interface     Labels   
--------- ----------------- ------------------------- --------------- ---------
  1         10.0.0.83/32      TI-LFA (4)                -             [ 20083 ]
  2         10.0.0.170/32     TI-LFA (6)                -             [ 3 ]    
  3         10.0.1.49/32      TI-LFA (7)                -             [ 3 ]    
  4         10.0.0.19/32      TI-LFA (4)                -             [ 20019 ]
  5         10.0.1.55/32      TI-LFA (3)                -             [ 3 ]    
  6         10.0.0.254/32     TI-LFA (4)                -             [ 20254 ]
  7         10.0.0.57/32      20.149.171.149            Ethernet24    [ 20057 ]
                              20.155.171.155            Ethernet46    [ 20057 ]
                              20.170.171.170            Ethernet1     [ 20057 ]
                              20.171.179.179            Ethernet25    [ 20057 ]
  8         10.0.0.179/32     TI-LFA (17)               -             [ 3 ]    

```

## show isis segment-routing prefix-segments

```text

System ID: PE31-J2-171			Instance: 'IGP'
SR supported Data-plane: MPLS			SR Router ID: 10.0.0.171

Node: 38     Proxy-Node: 0      Prefix: 4       Total Segments: 42

Flag Descriptions: R: Re-advertised, N: Node Segment, P: no-PHP
                   E: Explicit-NULL, V: Value, L: Local
Segment status codes: * - Self originated Prefix, L1 - level 1, L2 - level 2, ! - SR-unreachable,
                      # - Some IS-IS next-hops are SR-unreachable
   Prefix                      SID   Label Type       Flags                        System ID       Level Protection  Algorithm   
   ------------------------- ----- ------- ---------- ---------------------------- --------------- ----- ----------- -------------
   10.0.0.19/32                 19   20019 Node       R:0 N:1 P:0 E:0 V:0 L:0      0000.0000.0019  L2    node        SPF         
   10.0.0.24/32               1024   21024 Node       R:0 N:1 P:1 E:0 V:0 L:0      12502-1         L2    unprotected MIN-LATENCY 
   10.0.0.24/32               1124   21124 Node       R:0 N:1 P:1 E:0 V:0 L:0      12502-1         L2    unprotected MIN-TE      
   10.0.0.24/32               1224   21224 Node       R:0 N:1 P:1 E:0 V:0 L:0      12502-1         L2    unprotected MIN-IGP     
   10.0.0.24/32               1324   21324 Node       R:0 N:1 P:1 E:0 V:0 L:0      12502-1         L2    unprotected MIN-IGP-ADMIN
   10.0.0.57/32                 57   20057 Node       R:0 N:1 P:1 E:0 V:0 L:0      SR1-SRMPLS      L2    unprotected SPF         
   10.0.0.57/32               1057   21057 Node       R:0 N:1 P:1 E:0 V:0 L:0      SR1-SRMPLS      L2    unprotected MIN-LATENCY 
   10.0.0.57/32               1157   21157 Node       R:0 N:1 P:1 E:0 V:0 L:0      SR1-SRMPLS      L2    unprotected MIN-TE      
   10.0.0.57/32               1257   21257 Node       R:0 N:1 P:1 E:0 V:0 L:0      SR1-SRMPLS      L2    unprotected MIN-IGP     
   10.0.0.57/32               1357   21357 Node       R:0 N:1 P:1 E:0 V:0 L:0      SR1-SRMPLS      L2    node        MIN-IGP-ADMIN
   10.0.0.57/32               1457   21457 Node       R:0 N:1 P:1 E:0 V:0 L:0      SR1-SRMPLS      L2    unprotected 132         
   10.0.0.83/32                 83   20083 Node       R:0 N:1 P:0 E:0 V:0 L:0      eantc-jcnr2     L2    node        SPF         
   10.0.0.170/32               170   20170 Node       R:0 N:1 P:0 E:0 V:0 L:0      Spine3-J-170    L2    node        SPF         
*  10.0.0.171/32               171   20171 Node       R:0 N:1 P:0 E:0 V:0 L:0      PE31-J2-171     L2    unprotected SPF         
*  10.0.0.171/32              1171   21171 Node       R:0 N:1 P:0 E:0 V:0 L:0      PE31-J2-171     L2    unprotected MIN-LATENCY 
*  10.0.0.171/32              1271   21271 Node       R:0 N:1 P:0 E:0 V:0 L:0      PE31-J2-171     L2    unprotected MIN-TE      
*  10.0.0.171/32              1371   21371 Node       R:0 N:1 P:0 E:0 V:0 L:0      PE31-J2-171     L2    unprotected MIN-IGP     
*  10.0.0.171/32              1471   21471 Node       R:0 N:1 P:0 E:0 V:0 L:0      PE31-J2-171     L2    unprotected MIN-IGP-ADMIN
   10.0.0.179/32               379   20379 Node       R:0 N:1 P:0 E:0 V:0 L:0      juniper_379_MX304 L2    node        SPF         
   10.0.0.179/32              1179   21179 Node       R:0 N:1 P:0 E:0 V:0 L:0      juniper_379_MX304 L2    node        MIN-LATENCY 
   10.0.0.179/32              1279   21279 Node       R:0 N:1 P:0 E:0 V:0 L:0      juniper_379_MX304 L2    node        MIN-TE      
   10.0.0.179/32              1379   21379 Node       R:0 N:1 P:0 E:0 V:0 L:0      juniper_379_MX304 L2    node        MIN-IGP     
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
   200.111.0.0/24             1111   21111 Prefix     R:0 N:0 P:0 E:0 V:0 L:0      3800.0000.4111  L2    node        MIN-LATENCY 
   200.111.0.0/24             1211   21211 Prefix     R:0 N:0 P:0 E:0 V:0 L:0      3800.0000.4111  L2    node        MIN-TE      
   200.111.0.0/24             1311   21311 Prefix     R:0 N:0 P:0 E:0 V:0 L:0      3800.0000.4111  L2    node        MIN-IGP     
   200.111.0.0/24             1411   21411 Prefix     R:0 N:0 P:0 E:0 V:0 L:0      3800.0000.4111  L2    node        MIN-IGP-ADMIN
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
 I L2     10.0.0.57/32 [115/20]
           via 20.170.171.170, Ethernet1
           via 20.149.171.149, Ethernet24
           via 20.171.179.179, Ethernet25
           via 20.155.171.155, Ethernet46
 I L2     10.0.0.83/32 [115/20]
           via 20.149.171.149, Ethernet24
 I L2     10.0.0.170/32 [115/20]
           via 20.170.171.170, Ethernet1
 C        10.0.0.171/32
           directly connected, Loopback0
 I L2     10.0.0.179/32 [115/10]
           via 20.171.179.179, Ethernet25
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
 I L2     20.19.211.0/24 [115/20]
           via 20.149.171.149, Ethernet24
 I L2     20.24.149.0/24 [115/20]
           via 20.149.171.149, Ethernet24
 I L2     20.24.211.0/24 [115/30]
           via 20.149.171.149, Ethernet24
 I L2     20.32.149.0/24 [115/20]
           via 20.149.171.149, Ethernet24
 I L2     20.32.170.0/24 [115/20]
           via 20.170.171.170, Ethernet1
 I L2     20.47.149.0/24 [115/20]
           via 20.149.171.149, Ethernet24
 I L2     20.47.170.0/24 [115/20]
           via 20.170.171.170, Ethernet1
 I L2     20.57.59.0/24 [115/30]
           via 20.170.171.170, Ethernet1
           via 20.149.171.149, Ethernet24
           via 20.171.179.179, Ethernet25
           via 20.155.171.155, Ethernet46
 I L2     20.57.149.0/24 [115/20]
           via 20.149.171.149, Ethernet24
 I L2     20.57.155.0/24 [115/20]
           via 20.155.171.155, Ethernet46
 I L2     20.57.170.0/24 [115/20]
           via 20.170.171.170, Ethernet1
 I L2     20.57.179.0/24 [115/20]
           via 20.171.179.179, Ethernet25
 I L2     20.57.211.0/24 [115/30]
           via 20.170.171.170, Ethernet1
           via 20.149.171.149, Ethernet24
           via 20.171.179.179, Ethernet25
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
           via 20.171.179.179, Ethernet25
           via 20.155.171.155, Ethernet46
 C        20.170.171.0/24
           directly connected, Ethernet1
 I L2     20.170.254.0/24 [115/20]
           via 20.170.171.170, Ethernet1
 C        20.171.179.0/24
           directly connected, Ethernet25
 I L2     20.171.254.0/24 [115/30]
           via 20.149.171.149, Ethernet24
 I L2     192.168.20.0/23 [115/20]
           via 20.149.171.149, Ethernet24
 I L2     192.168.0.0/19 [115/20]
           via 20.149.171.149, Ethernet24
 I L2     200.111.0.0/24 [115/20]
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
 I L2     10.0.0.57/32 [115/20]
           via 20.170.171.170, Ethernet1
           via 20.149.171.149, Ethernet24
           via 20.171.179.179, Ethernet25
           via 20.155.171.155, Ethernet46
 I L2     10.0.0.83/32 [115/20]
           via 20.149.171.149, Ethernet24
 I L2     10.0.0.170/32 [115/20]
           via 20.170.171.170, Ethernet1
 C        10.0.0.171/32
           directly connected, Loopback0
 I L2     10.0.0.179/32 [115/10]
           via 20.171.179.179, Ethernet25
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
 I L2     20.19.211.0/24 [115/20]
           via 20.149.171.149, Ethernet24
 I L2     20.24.149.0/24 [115/20]
           via 20.149.171.149, Ethernet24
 I L2     20.24.211.0/24 [115/30]
           via 20.149.171.149, Ethernet24
 I L2     20.32.149.0/24 [115/20]
           via 20.149.171.149, Ethernet24
 I L2     20.32.170.0/24 [115/20]
           via 20.170.171.170, Ethernet1
 I L2     20.47.149.0/24 [115/20]
           via 20.149.171.149, Ethernet24
 I L2     20.47.170.0/24 [115/20]
           via 20.170.171.170, Ethernet1
 I L2     20.57.59.0/24 [115/30]
           via 20.170.171.170, Ethernet1
           via 20.149.171.149, Ethernet24
           via 20.171.179.179, Ethernet25
           via 20.155.171.155, Ethernet46
 I L2     20.57.149.0/24 [115/20]
           via 20.149.171.149, Ethernet24
 I L2     20.57.155.0/24 [115/20]
           via 20.155.171.155, Ethernet46
 I L2     20.57.170.0/24 [115/20]
           via 20.170.171.170, Ethernet1
 I L2     20.57.179.0/24 [115/20]
           via 20.171.179.179, Ethernet25
 I L2     20.57.211.0/24 [115/30]
           via 20.170.171.170, Ethernet1
           via 20.149.171.149, Ethernet24
           via 20.171.179.179, Ethernet25
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
           via 20.171.179.179, Ethernet25
           via 20.155.171.155, Ethernet46
 C        20.170.171.0/24
           directly connected, Ethernet1
 I L2     20.170.254.0/24 [115/20]
           via 20.170.171.170, Ethernet1
 C        20.171.179.0/24
           directly connected, Ethernet25
 I L2     20.171.254.0/24 [115/30]
           via 20.149.171.149, Ethernet24
 I L2     192.168.20.0/23 [115/20]
           via 20.149.171.149, Ethernet24
 I L2     192.168.0.0/19 [115/20]
           via 20.149.171.149, Ethernet24
 I L2     200.111.0.0/24 [115/20]
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
           via 10.0.0.57/32, algorithm MIN-LATENCY, IS-IS FlexAlgo tunnel index 15, label 524286
              via 20.149.171.149, Ethernet24, label 21057
              via 20.155.171.155, Ethernet46, label 21057
 B I      20.111.155.0/24 [200/0]
           via 10.0.1.55/32, IS-IS SR tunnel index 5, label 24009
              via TI-LFA tunnel index 3, label imp-null(3)
                 via 20.155.171.155, Ethernet46, label imp-null(3)
                 backup via 20.149.171.149, Ethernet24, label 20355
 C        20.111.171.0/24
           directly connected, Ethernet5.128
 B I      20.111.179.0/24 [200/0]
           via 10.0.0.179/32, algorithm MIN-LATENCY, IS-IS FlexAlgo tunnel index 19, label 19
              via TI-LFA tunnel index 2, label imp-null(3)
                 via 20.171.179.179, Ethernet25, label imp-null(3)
                 backup via 20.155.171.155, Ethernet46, label 21179
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

 B I      20.57.111.0/24 [200/0]
           via 10.0.0.57/32, algorithm MIN-IGP, IS-IS FlexAlgo tunnel index 17, label 524283
              via 20.149.171.149, Ethernet24, label 21257
              via 20.155.171.155, Ethernet46, label 21257
              via 20.171.179.179, Ethernet25, label 21257
 B I      20.111.155.0/24 [200/0]
           via 10.0.1.55/32, IS-IS SR tunnel index 5, label 24012
              via TI-LFA tunnel index 3, label imp-null(3)
                 via 20.155.171.155, Ethernet46, label imp-null(3)
                 backup via 20.149.171.149, Ethernet24, label 20355
 C        20.111.171.0/24
           directly connected, Ethernet5.130
 B I      20.111.179.0/24 [200/0]
           via 10.0.0.179/32, algorithm MIN-IGP, IS-IS FlexAlgo tunnel index 25, label 21
              via 20.171.179.179, Ethernet25, label imp-null(3)
 B I      20.111.254.0/24 [200/0]
           via 10.0.0.254/32, algorithm MIN-IGP, IS-IS FlexAlgo tunnel index 10, label 48093
              via TI-LFA tunnel index 4, label 21454
                 via 20.149.171.149, Ethernet24, label imp-null(3)
                 backup via 20.155.171.155, Ethernet46, label imp-null(3)


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
           via 10.0.0.57/32, algorithm MIN-IGP-ADMIN, IS-IS FlexAlgo tunnel index 20, label 524282
              via 20.155.171.155, Ethernet46, label 21357
 B I      20.111.155.0/24 [200/0]
           via 10.0.1.55/32, IS-IS SR tunnel index 5, label 24011
              via TI-LFA tunnel index 3, label imp-null(3)
                 via 20.155.171.155, Ethernet46, label imp-null(3)
                 backup via 20.149.171.149, Ethernet24, label 20355
 C        20.111.171.0/24
           directly connected, Ethernet5.131
 B I      20.111.179.0/24 [200/0]
           via 10.0.0.179/32, IS-IS SR tunnel index 8, label 22
              via TI-LFA tunnel index 17, label imp-null(3)
                 via 20.171.179.179, Ethernet25, label imp-null(3)
                 backup via 20.155.171.155, Ethernet46, label 20379
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

 B I      20.57.111.0/24 [200/0]
           via 10.0.0.57/32, algorithm MIN-TE, IS-IS FlexAlgo tunnel index 16, label 524284
              via 20.149.171.149, Ethernet24, label 21157
              via 20.155.171.155, Ethernet46, label 21157
 B I      20.111.155.0/24 [200/0]
           via 10.0.1.55/32, IS-IS SR tunnel index 5, label 24010
              via TI-LFA tunnel index 3, label imp-null(3)
                 via 20.155.171.155, Ethernet46, label imp-null(3)
                 backup via 20.149.171.149, Ethernet24, label 20355
 C        20.111.171.0/24
           directly connected, Ethernet5.129
 B I      20.111.179.0/24 [200/0]
           via 10.0.0.179/32, algorithm MIN-TE, IS-IS FlexAlgo tunnel index 18, label 20
              via TI-LFA tunnel index 12, label 21279
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

 B I      20.19.111.0/24 [200/0]
           via 10.0.0.19/32, IS-IS SR tunnel index 4, label 1279
              via TI-LFA tunnel index 4, label 20019
                 via 20.149.171.149, Ethernet24, label imp-null(3)
                 backup via 20.155.171.155, Ethernet46, label imp-null(3)
 B I      20.55.111.0/24 [200/0]
           via 10.0.1.55/32, IS-IS SR tunnel index 5, label 24004
              via TI-LFA tunnel index 3, label imp-null(3)
                 via 20.155.171.155, Ethernet46, label imp-null(3)
                 backup via 20.149.171.149, Ethernet24, label 20355
 B I      20.57.111.0/24 [200/0]
           via 10.0.0.57/32, IS-IS SR tunnel index 7, label 524287
              via 20.149.171.149, Ethernet24, label 20057
              via 20.155.171.155, Ethernet46, label 20057
              via 20.170.171.170, Ethernet1, label 20057
              via 20.171.179.179, Ethernet25, label 20057
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
MPLS forwarding table (Label [metric] Vias) - 39 routes 
MPLS next-hop resolution allow default route: False
Metric Codes:
          A - Active metric
Via Type Codes:
          M - MPLS via, P - Pseudowire via,
          I - IP lookup via, V - VLAN via,
          VA - EVPN VLAN aware via, ES - EVPN ethernet segment via,
          VF - EVPN VLAN flood via, AF - EVPN VLAN aware flood via,
          NG - Nexthop group via

 20019   A[1]
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
                    20.170.171.170 Ethernet1
                    20.171.179.179 Ethernet25
 20083   A[1]
                via M, ::, forward
                    EgressACL: apply
                  via TI-LFA tunnel index 4
                    via 20.149.171.149, Ethernet24, label imp-null(3)
                    backup via 20.155.171.155, Ethernet46, label imp-null(3)
 20170   A[1]
                via M, ::, pop
                    EgressACL: apply
                  via TI-LFA tunnel index 6
                    via 20.170.171.170, Ethernet1, label imp-null(3)
                    backup via 20.149.171.149, Ethernet24, label 20057 20170
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
                via M, ::, pop
                    EgressACL: apply
                  via TI-LFA tunnel index 17
                    via 20.171.179.179, Ethernet25, label imp-null(3)
                    backup via 20.155.171.155, Ethernet46, label 20379
 21057   A[1]
                via M, forward
                    EgressACL: apply
                    20.149.171.149 Ethernet24
                    20.155.171.155 Ethernet46
 21111   A[1]
                via M, forward
                    EgressACL: apply
                    20.149.171.149 Ethernet24
 21157   A[1]
                via M, forward
                    EgressACL: apply
                    20.149.171.149 Ethernet24
                    20.155.171.155 Ethernet46
 21179   A[1]
                via M, ::, pop
                    EgressACL: apply
                  via TI-LFA tunnel index 2
                    via 20.171.179.179, Ethernet25, label imp-null(3)
                    backup via 20.155.171.155, Ethernet46, label 21179
 21211   A[1]
                via M, forward
                    EgressACL: apply
                    20.149.171.149 Ethernet24
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
                    20.171.179.179 Ethernet25
 21279   A[1]
                via M, ::, forward
                    EgressACL: apply
                  via TI-LFA tunnel index 12
                    via 20.155.171.155, Ethernet46, label imp-null(3)
                    backup via 20.149.171.149, Ethernet24, label 21157
 21311   A[1]
                via M, forward
                    EgressACL: apply
                    20.149.171.149 Ethernet24
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
                  via TI-LFA tunnel index 13
                    via 20.155.171.155, Ethernet46, label imp-null(3)
                    backup via 20.149.171.149, Ethernet24, label 24013
 21357   A[1]
                via M, forward
                    EgressACL: apply
                    20.155.171.155 Ethernet46
 21379   A[1]
                via M, pop
                    EgressACL: apply
                    20.171.179.179 Ethernet25
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
                  via TI-LFA tunnel index 10
                    via 20.155.171.155, Ethernet46, label imp-null(3)
                    backup via 20.149.171.149, Ethernet24, label 21555
 21649   A[1]
                via M, ::, pop
                    EgressACL: apply
                  via TI-LFA tunnel index 9
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
 362145  A[1]
                via M, 20.170.171.170, pop
                    EgressACL: apply
                    directly connected, Ethernet1
                    28:99:3a:06:b4:e1, vlan 1045
 362146  A[1]
                via M, 20.155.171.155, pop
                    EgressACL: apply
                    directly connected, Ethernet46
                    34:88:18:bf:4a:30, vlan 1050
 362147  A[1]
                via M, 20.171.179.179, pop
                    EgressACL: apply
                    directly connected, Ethernet25
                    60:c7:8d:2d:3c:bf, vlan 1013
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
MPLS forwarding table (Label [metric] Vias) - 39 routes 
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

 IP    20019    [1], 10.0.0.19/32
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
                via M, 20.170.171.170, forward
                 payload autoDecide, ttlMode uniform, dscpMode uniform, apply egress-acl
                 interface Ethernet1
                via M, 20.171.179.179, forward
                 payload autoDecide, ttlMode uniform, dscpMode uniform, apply egress-acl
                 interface Ethernet25
 IP    20083    [1], 10.0.0.83/32
                via TI-LFA tunnel index 4, forward
                 payload autoDecide, ttlMode uniform, dscpMode uniform, apply egress-acl
                    via 20.149.171.149, Ethernet24, label imp-null(3)
                    backup via 20.155.171.155, Ethernet46, label imp-null(3)
 IP    20170    [1], 10.0.0.170/32
                via TI-LFA tunnel index 6, pop
                 payload autoDecide, ttlMode uniform, dscpMode uniform, apply egress-acl
                    via 20.170.171.170, Ethernet1, label imp-null(3)
                    backup via 20.149.171.149, Ethernet24, label 20057 20170
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
                via TI-LFA tunnel index 17, pop
                 payload autoDecide, ttlMode uniform, dscpMode uniform, apply egress-acl
                    via 20.171.179.179, Ethernet25, label imp-null(3)
                    backup via 20.155.171.155, Ethernet46, label 20379
 IP    21057    [1], 10.0.0.57/32, algorithm MIN-LATENCY
                via M, 20.149.171.149, forward
                 payload autoDecide, ttlMode uniform, dscpMode uniform, apply egress-acl
                 interface Ethernet24
                via M, 20.155.171.155, forward
                 payload autoDecide, ttlMode uniform, dscpMode uniform, apply egress-acl
                 interface Ethernet46
 IP    21111    [1], 200.111.0.0/24, algorithm MIN-LATENCY
                via M, 20.149.171.149, forward
                 payload autoDecide, ttlMode uniform, dscpMode uniform, apply egress-acl
                 interface Ethernet24
 IP    21157    [1], 10.0.0.57/32, algorithm MIN-TE
                via M, 20.149.171.149, forward
                 payload autoDecide, ttlMode uniform, dscpMode uniform, apply egress-acl
                 interface Ethernet24
                via M, 20.155.171.155, forward
                 payload autoDecide, ttlMode uniform, dscpMode uniform, apply egress-acl
                 interface Ethernet46
 IP    21179    [1], 10.0.0.179/32, algorithm MIN-LATENCY
                via TI-LFA tunnel index 2, pop
                 payload autoDecide, ttlMode uniform, dscpMode uniform, apply egress-acl
                    via 20.171.179.179, Ethernet25, label imp-null(3)
                    backup via 20.155.171.155, Ethernet46, label 21179
 IP    21211    [1], 200.111.0.0/24, algorithm MIN-TE
                via M, 20.149.171.149, forward
                 payload autoDecide, ttlMode uniform, dscpMode uniform, apply egress-acl
                 interface Ethernet24
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
                via M, 20.171.179.179, forward
                 payload autoDecide, ttlMode uniform, dscpMode uniform, apply egress-acl
                 interface Ethernet25
 IP    21279    [1], 10.0.0.179/32, algorithm MIN-TE
                via TI-LFA tunnel index 12, forward
                 payload autoDecide, ttlMode uniform, dscpMode uniform, apply egress-acl
                    via 20.155.171.155, Ethernet46, label imp-null(3)
                    backup via 20.149.171.149, Ethernet24, label 21157
 IP    21311    [1], 200.111.0.0/24, algorithm MIN-IGP
                via M, 20.149.171.149, forward
                 payload autoDecide, ttlMode uniform, dscpMode uniform, apply egress-acl
                 interface Ethernet24
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
                via TI-LFA tunnel index 13, pop
                 payload autoDecide, ttlMode uniform, dscpMode uniform, apply egress-acl
                    via 20.155.171.155, Ethernet46, label imp-null(3)
                    backup via 20.149.171.149, Ethernet24, label 24013
 IP    21357    [1], 10.0.0.57/32, algorithm MIN-IGP-ADMIN
                via M, 20.155.171.155, forward
                 payload autoDecide, ttlMode uniform, dscpMode uniform, apply egress-acl
                 interface Ethernet46
 IP    21379    [1], 10.0.0.179/32, algorithm MIN-IGP
                via M, 20.171.179.179, pop
                 payload autoDecide, ttlMode uniform, dscpMode uniform, apply egress-acl
                 interface Ethernet25
 IP    21411    [1], 200.111.0.0/24, algorithm MIN-IGP-ADMIN
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
                via TI-LFA tunnel index 10, pop
                 payload autoDecide, ttlMode uniform, dscpMode uniform, apply egress-acl
                    via 20.155.171.155, Ethernet46, label imp-null(3)
                    backup via 20.149.171.149, Ethernet24, label 21555
 IP    21649    [1], 10.0.1.49/32, algorithm MIN-IGP
                via TI-LFA tunnel index 9, pop
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
 IA    362145   [1]
                via M, 20.170.171.170, pop
                 payload autoDecide, ttlMode uniform, apply egress-acl
                 interface Ethernet1
 IA    362146   [1]
                via M, 20.155.171.155, pop
                 payload autoDecide, ttlMode uniform, apply egress-acl
                 interface Ethernet46
 IA    362147   [1]
                via M, 20.171.179.179, pop
                 payload autoDecide, ttlMode uniform, apply egress-acl
                 interface Ethernet25
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
          RD: 65000:5 IPv4 prefix 20.5.111.0/24
                                 10.0.0.5              -       100     0       ? Or-ID: 10.0.0.5 C-LST: 10.0.1.49 
          RD: 65000:128 IPv4 prefix 20.5.111.0/24
                                 10.0.0.5              -       100     0       ? Or-ID: 10.0.0.5 C-LST: 10.0.1.49 
          RD: 65000:129 IPv4 prefix 20.5.111.0/24
                                 10.0.0.5              -       100     0       ? Or-ID: 10.0.0.5 C-LST: 10.0.1.49 
          RD: 65000:130 IPv4 prefix 20.5.111.0/24
                                 10.0.0.5              -       100     0       ? Or-ID: 10.0.0.5 C-LST: 10.0.1.49 
          RD: 65000:131 IPv4 prefix 20.5.111.0/24
                                 10.0.0.5              -       100     0       ? Or-ID: 10.0.0.5 C-LST: 10.0.1.49 
 * >      RD: 65000:19 IPv4 prefix 20.19.111.0/24
                                 10.0.0.19             0       100     0       ? Or-ID: 10.0.0.19 C-LST: 10.0.1.49 
 * >      RD: 65001:19 IPv4 prefix 20.19.111.0/24
                                 10.0.0.19             0       100     0       ? Or-ID: 10.0.0.19 C-LST: 10.0.1.49 
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
 * >      RD: 10.0.1.55:128 IPv4 prefix 20.111.155.0/24
                                 10.0.1.55             0       100     0       ? Or-ID: 10.0.1.55 C-LST: 10.0.1.49 
 * >      RD: 10.0.1.55:129 IPv4 prefix 20.111.155.0/24
                                 10.0.1.55             0       100     0       ? Or-ID: 10.0.1.55 C-LST: 10.0.1.49 
 * >      RD: 10.0.1.55:130 IPv4 prefix 20.111.155.0/24
                                 10.0.1.55             0       100     0       ? Or-ID: 10.0.1.55 C-LST: 10.0.1.49 
 * >      RD: 10.0.1.55:131 IPv4 prefix 20.111.155.0/24
                                 10.0.1.55             0       100     0       ? Or-ID: 10.0.1.55 C-LST: 10.0.1.49 
 * >      RD: 10.0.0.171:128 IPv4 prefix 20.111.171.0/24
                                 -                     -       -       0       i
 * >      RD: 10.0.0.171:129 IPv4 prefix 20.111.171.0/24
                                 -                     -       -       0       i
 * >      RD: 10.0.0.171:130 IPv4 prefix 20.111.171.0/24
                                 -                     -       -       0       i
 * >      RD: 10.0.0.171:131 IPv4 prefix 20.111.171.0/24
                                 -                     -       -       0       i
 * >      RD: 10.0.0.179:1808 IPv4 prefix 20.111.179.0/24
                                 10.0.0.179            -       100     0       i Or-ID: 10.0.0.179 C-LST: 10.0.1.49 
 * >      RD: 10.0.0.179:1809 IPv4 prefix 20.111.179.0/24
                                 10.0.0.179            -       100     0       i Or-ID: 10.0.0.179 C-LST: 10.0.1.49 
 * >      RD: 10.0.0.179:1810 IPv4 prefix 20.111.179.0/24
                                 10.0.0.179            -       100     0       i Or-ID: 10.0.0.179 C-LST: 10.0.1.49 
 * >      RD: 10.0.0.179:1811 IPv4 prefix 20.111.179.0/24
                                 10.0.0.179            -       100     0       i Or-ID: 10.0.0.179 C-LST: 10.0.1.49 
 * >      RD: 65000:1254 IPv4 prefix 20.111.254.0/24
                                 10.0.0.254            0       100     0       ? Or-ID: 10.0.0.254 C-LST: 10.0.1.49 
 * >      RD: 65000:1354 IPv4 prefix 20.111.254.0/24
                                 10.0.0.254            0       100     0       ? Or-ID: 10.0.0.254 C-LST: 10.0.1.49 
 * >      RD: 65000:1454 IPv4 prefix 20.111.254.0/24
                                 10.0.0.254            0       100     0       ? Or-ID: 10.0.0.254 C-LST: 10.0.1.49 
 * >      RD: 65000:1554 IPv4 prefix 20.111.254.0/24
                                 10.0.0.254            0       100     0       ? Or-ID: 10.0.0.254 C-LST: 10.0.1.49 
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
  Last read 00:00:19, last write 00:00:34
  Hold time is 180, keepalive interval is 60 seconds
  Configured hold time is 180, keepalive interval is 60 seconds
  Effective minimum hold time is 3 seconds
  Send failure hold time is 0 seconds
  Hold timer is active, time left: 00:02:41
  Keepalive timer is active, time left: 00:00:19
  Connect timer is inactive
  Idle-restart timer is inactive
  BGP state is Established, up for 04:37:54
  Number of transitions to established: 1
  Last state was OpenConfirm
  Last event was ReapplyInboundPolicy
  Last sent socket-error:Connect (Network is unreachable), Last time 04:37:58, First time 04:39:26, Repeats 6
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
    Updates:                7        93
    Keepalives:           326       265
    Route Refresh:          0         0
    Total messages:       334       359
  Prefix Statistics:
                                   Sent      Rcvd     Best Paths     Best ECMP Paths
    IPv4 Unicast:                     0         0              0                   0
    VPN-IPv4:                         4        28             23                   0
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
    Last update with error received at: 02:09:24
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
    Retransmission Timeout (rto): 400.0ms
    Round-trip Time (rtt/rtvar): 199.6ms/2.3ms
    Delayed Ack Timeout (ato): 40.0ms
    Congestion Window (cwnd): 10
    TCP Throughput: 0.50 Mbps
    Advertised Recv Window (rcv_space): 14600

```

## show tunnel rib system-tunnel-rib brief

```text
Tunnel RIB: system-tunnel-rib
Endpoint        Tunnel Type     Index(es)   Tunnel Preference   IGP Preference 
-------------- --------------- ----------- ------------------- ----------------
10.0.0.19/32    IS-IS SR IPv4   4           200                 115            
10.0.0.57/32    IS-IS SR IPv4   7           200                 115            
10.0.0.83/32    IS-IS SR IPv4   1           200                 115            
10.0.0.170/32   IS-IS SR IPv4   2           200                 115            
10.0.0.179/32   IS-IS SR IPv4   8           200                 115            
10.0.0.254/32   IS-IS SR IPv4   6           200                 115            
10.0.1.49/32    IS-IS SR IPv4   3           200                 115            
10.0.1.55/32    IS-IS SR IPv4   5           200                 115            

   IGP Metric    Metric Type
---------------- -----------
   20            metric     
   20            metric     
   20            metric     
   20            metric     
   10            metric     
   20            metric     
   10            metric     
   10            metric     

```

## show tunnel rib colored brief

```text
Tunnel RIB: system-colored-tunnel-rib
 Endpoint         Color   Tunnel Type      Index(es)    Tunnel Preference    IGP Preference    IGP Metric   Metric Type
---------------- ------- ---------------- ------------ -------------------- ----------------- ------------- -----------
 10.0.0.57/32     128     IS-IS FlexAlgo   15           65                   115               13           metric     
 10.0.0.57/32     129     IS-IS FlexAlgo   16           65                   115               24           metric     
 10.0.0.57/32     130     IS-IS FlexAlgo   17           65                   115               20           metric     
 10.0.0.57/32     131     IS-IS FlexAlgo   20           65                   115               20           metric     
 10.0.0.179/32    128     IS-IS FlexAlgo   19           65                   115               11           metric     
 10.0.0.179/32    129     IS-IS FlexAlgo   18           65                   115               24           metric     
 10.0.0.179/32    130     IS-IS FlexAlgo   25           65                   115               10           metric     
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
 200.111.0.0/24   128     IS-IS FlexAlgo   23           65                   115               13           metric     
 200.111.0.0/24   129     IS-IS FlexAlgo   22           65                   115               24           metric     
 200.111.0.0/24   130     IS-IS FlexAlgo   21           65                   115               20           metric     
 200.111.0.0/24   131     IS-IS FlexAlgo   24           65                   115               30           metric     

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
>C    10.0.0.171/32 [0 pref/0 metric] updated 04:39:42 ago
         via Loopback0, directly connected
>C    20.149.171.0/24 [0 pref/0 metric] updated 04:37:59 ago
         via Ethernet24, directly connected
>C    20.155.171.0/24 [0 pref/0 metric] updated 02:36:04 ago
         via Ethernet46, directly connected
>C    20.170.171.0/24 [0 pref/0 metric] updated 04:37:56 ago
         via Ethernet1, directly connected
>C    20.171.179.0/24 [0 pref/0 metric] updated 00:35:38 ago
         via Ethernet25, directly connected
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
>P    0.0.0.0/8 [1 pref/0 metric] updated 04:39:41 ago
         via Null0, directly connected [NF]
>P    127.0.0.0/8 [1 pref/0 metric] updated 04:39:41 ago
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
>I    10.0.0.5/32 [115 pref/30 metric] updated 02:14:11 ago
         via 20.149.171.149, Ethernet24
>I    10.0.0.19/32 [115 pref/20 metric] updated 04:37:59 ago
         via 20.149.171.149, Ethernet24
>I    10.0.0.24/32 [115 pref/20 metric] updated 00:50:49 ago
         via 20.149.171.149, Ethernet24
>I    10.0.0.57/32 [115 pref/20 metric] updated 00:29:58 ago
         via 20.149.171.149, Ethernet24
         via 20.155.171.155, Ethernet46
         via 20.170.171.170, Ethernet1
         via 20.171.179.179, Ethernet25
>I    10.0.0.83/32 [115 pref/20 metric] updated 04:37:59 ago
         via 20.149.171.149, Ethernet24
>I    10.0.0.170/32 [115 pref/20 metric] updated 04:37:48 ago
         via 20.170.171.170, Ethernet1
>I    10.0.0.179/32 [115 pref/10 metric] updated 00:29:58 ago
         via 20.171.179.179, Ethernet25
>I    10.0.0.254/32 [115 pref/20 metric] updated 04:37:59 ago
         via 20.149.171.149, Ethernet24
>I    10.0.1.49/32 [115 pref/10 metric] updated 04:37:59 ago
         via 20.149.171.149, Ethernet24
>I    10.0.1.55/32 [115 pref/10 metric] updated 02:36:02 ago
         via 20.155.171.155, Ethernet46
>I    20.5.149.0/24 [115 pref/20 metric] updated 03:05:05 ago
         via 20.149.171.149, Ethernet24
>I    20.19.149.0/24 [115 pref/20 metric] updated 04:37:59 ago
         via 20.149.171.149, Ethernet24
>I    20.19.211.0/24 [115 pref/20 metric] updated 04:37:59 ago
         via 20.149.171.149, Ethernet24
>I    20.24.149.0/24 [115 pref/20 metric] updated 00:50:51 ago
         via 20.149.171.149, Ethernet24
>I    20.24.211.0/24 [115 pref/30 metric] updated 00:50:49 ago
         via 20.149.171.149, Ethernet24
>I    20.32.149.0/24 [115 pref/20 metric] updated 00:42:16 ago
         via 20.149.171.149, Ethernet24
>I    20.32.170.0/24 [115 pref/20 metric] updated 00:42:13 ago
         via 20.170.171.170, Ethernet1
>I    20.47.149.0/24 [115 pref/20 metric] updated 04:37:59 ago
         via 20.149.171.149, Ethernet24
>I    20.47.170.0/24 [115 pref/20 metric] updated 04:37:48 ago
         via 20.170.171.170, Ethernet1
>I    20.57.59.0/24 [115 pref/30 metric] updated 00:29:58 ago
         via 20.149.171.149, Ethernet24
         via 20.155.171.155, Ethernet46
         via 20.170.171.170, Ethernet1
         via 20.171.179.179, Ethernet25
>I    20.57.149.0/24 [115 pref/20 metric] updated 04:37:59 ago
         via 20.149.171.149, Ethernet24
>I    20.57.155.0/24 [115 pref/20 metric] updated 02:32:21 ago
         via 20.155.171.155, Ethernet46
>I    20.57.170.0/24 [115 pref/20 metric] updated 04:37:48 ago
         via 20.170.171.170, Ethernet1
>I    20.57.179.0/24 [115 pref/20 metric] updated 00:29:58 ago
         via 20.171.179.179, Ethernet25
>I    20.57.211.0/24 [115 pref/30 metric] updated 00:29:58 ago
         via 20.149.171.149, Ethernet24
         via 20.155.171.155, Ethernet46
         via 20.170.171.170, Ethernet1
         via 20.171.179.179, Ethernet25
>I    20.83.149.0/24 [115 pref/20 metric] updated 04:37:59 ago
         via 20.149.171.149, Ethernet24
>I    20.111.149.0/24 [115 pref/20 metric] updated 00:16:05 ago
         via 20.149.171.149, Ethernet24
>I    20.149.155.0/24 [115 pref/20 metric] updated 02:36:02 ago
         via 20.149.171.149, Ethernet24
         via 20.155.171.155, Ethernet46
>I    20.149.254.0/24 [115 pref/20 metric] updated 04:37:59 ago
         via 20.149.171.149, Ethernet24
>I    20.155.179.0/24 [115 pref/20 metric] updated 00:29:58 ago
         via 20.155.171.155, Ethernet46
         via 20.171.179.179, Ethernet25
>I    20.170.254.0/24 [115 pref/20 metric] updated 04:37:48 ago
         via 20.170.171.170, Ethernet1
>I    20.171.254.0/24 [115 pref/30 metric] updated 04:37:59 ago
         via 20.149.171.149, Ethernet24
>I    192.168.0.0/19 [115 pref/20 metric] updated 04:37:59 ago
         via 20.149.171.149, Ethernet24
>I    192.168.20.0/23 [115 pref/20 metric] updated 00:50:49 ago
         via 20.149.171.149, Ethernet24
>I    200.111.0.0/24 [115 pref/20 metric] updated 00:04:22 ago
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
>P    ::/96 [1 pref/0 metric] updated 02:09:27 ago
         via Null0, directly connected [NF]
>P    ::ffff:127.0.0.0/104 [1 pref/0 metric] updated 02:09:27 ago
         via :: [1 pref/1 metric] type ipv6
            via , directly connected
>P    fe80::/10 [1 pref/0 metric] updated 02:09:27 ago
```

## show platform sand l3 summary

```text
Number of vrfs: 7

Ipv4:
  Routes:       117  backlog:  0  unprogrammed:  0
  Adjacencies:  114  backlog:  0  unprogrammed:  0
Ipv6:
  Routes:       0    backlog:  0  unprogrammed:  0
  Adjacencies:  114  backlog:  0  unprogrammed:  0
Mpls:
  Routes:       34  backlog:  0  unprogrammed:  0
  Adjacencies:  4   backlog:  0  unprogrammed:  0

Jericho2 Ip Fecs:
  Non-ecmp fecs:  4148  ecmp fecs:  7  fec entries:  4168
Jericho2 Mpls Fecs:
  Non-ecmp fecs:  4  ecmp fecs:  0  fec entries:  4
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
  Route buckets used:  19  Rows used:     4   Entries Per Bucket:  6  Percent free:  99

Lem:
  IPv4  Host in Lem:            disabled
  IPv4  Prefix-lengths in Lem:  None    
  IPv6  Host in Lem:            disabled
  IPv6  Prefix-lengths in Lem:  None    
  Number of downloads:        0
  Number of overflow events:  0

Egress Arp rewrite entries in use (in each fap):
  FixedSystem: 4
Egress Arp remote rewrite entries in use (in each fap):
  FixedSystem: 0
Egress Ip tunnel rewrite entries in use (in each fap):
  FixedSystem: 0
Egress Mpls (for outer 2 labels) rewrite entries in use (in each fap):
  FixedSystem: 0
Egress Mpls (for inner 2 labels) rewrite entries in use (in each fap):
  FixedSystem: 25
Egress Sflow rewrite entries in use (in each fap):
  FixedSystem: 0

Egress rewrite chains in backlog: resource-full 0, no-interface 0

Glem entries used per fap :
  FixedSystem: 4132

Jericho2 Fec:
  Maximum FEC hierarchy levels:  2
  ReusedEcmp:  1  allocs:  161  frees:  100  shuffles:  0  cmds:  0
  Zombies:     0    purges:    0
  Quarantine:  0/0  shuffles:  0  deletes:  0   
  Fec insertion failures:  0
  Level1  Fecs:
    Non-ecmp fecs:            0    ecmp fecs:            1 
    Non-ecmp (Percent free):  100  ecmp (Percent free):  99
  Level2  Fecs:
    Non-ecmp fecs:            40  ecmp fecs:            0  
    Non-ecmp (Percent free):  99  ecmp (Percent free):  100
  Level3  Fecs:
    Non-ecmp fecs:            108  ecmp fecs:            7 
    Non-ecmp (Percent free):  99   ecmp (Percent free):  99

Lpm Detail:
  Requests:  355  cleanses:  134  batches:  134  avg batch size:  2

Jericho Arp:
  ArpTable writes:      17921  queued      0   
  IngressTable writes:  77429  queued      0   
  Coprocessors:         1      in CmdRing

Tunnel Counter Status
  Number of MPLS tunnels:                  32   
  Number of uncountable MPLS tunnels:      32   
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
|0  |10.0.0.57/32      |ROUTE| Et25               |1013 |103426  | 60:c7:8d:2d:3c:bf |24582|528576|   -   
|0  |10.0.0.57/32      |ROUTE| Et24               |1008 |103421  | c0:f8:7f:6a:4e:1c |24582|528577|   -   
|0  |10.0.0.57/32      |ROUTE| Et24               |1008 |103421  | c0:f8:7f:6a:4e:1c |24582|528578|   -   
|0  |10.0.0.57/32      |ROUTE| Et1                |1045 |103423  | 28:99:3a:06:b4:e1 |24582|528579|   -   
|0  |10.0.0.57/32      |ROUTE| Et1                |1045 |103423  | 28:99:3a:06:b4:e1 |24582|528580|   -   
|0  |10.0.0.57/32      |ROUTE| Et46               |1050 |103424  | 34:88:18:bf:4a:30 |24582|528581|   -   
|0  |10.0.0.57/32      |ROUTE| Et46               |1050 |103424  | 34:88:18:bf:4a:30 |24582|528582|   -   
|0  |10.0.0.57/32      |ROUTE| Et25               |1013 |103426  | 60:c7:8d:2d:3c:bf |24582|528583|   -   
|0  |10.0.0.83/32      |ROUTE| Et24               |1008 |103421  | c0:f8:7f:6a:4e:1c |  -  |528490|   -   
|0  |10.0.0.170/32     |ROUTE| Et1                |1045 |103423  | 28:99:3a:06:b4:e1 |  -  |528498|   -   
|0  |10.0.0.171/32     |TRAP | CoppSystemIpUcast  |0    |  -     | Receive           |  -  |524291|   -   
|0  |10.0.0.179/32     |ROUTE| Et25               |1013 |103426  | 60:c7:8d:2d:3c:bf |  -  |528560|   -   
|0  |10.0.0.254/32     |ROUTE| Et24               |1008 |103421  | c0:f8:7f:6a:4e:1c |  -  |528490|   -   
|0  |10.0.1.49/32      |ROUTE| Et24               |1008 |103421  | c0:f8:7f:6a:4e:1c |  -  |528490|   -   
|0  |10.0.1.55/32      |ROUTE| Et46               |1050 |103424  | 34:88:18:bf:4a:30 |  -  |528524|   -   
|0  |20.5.149.0/24     |ROUTE| Et24               |1008 |103421  | c0:f8:7f:6a:4e:1c |  -  |528490|   -   
|0  |20.19.149.0/24    |ROUTE| Et24               |1008 |103421  | c0:f8:7f:6a:4e:1c |  -  |528490|   -   
|0  |20.19.211.0/24    |ROUTE| Et24               |1008 |103421  | c0:f8:7f:6a:4e:1c |  -  |528490|   -   
|0  |20.24.149.0/24    |ROUTE| Et24               |1008 |103421  | c0:f8:7f:6a:4e:1c |  -  |528490|   -   
|0  |20.24.211.0/24    |ROUTE| Et24               |1008 |103421  | c0:f8:7f:6a:4e:1c |  -  |528490|   -   
|0  |20.32.149.0/24    |ROUTE| Et24               |1008 |103421  | c0:f8:7f:6a:4e:1c |  -  |528490|   -   
|0  |20.32.170.0/24    |ROUTE| Et1                |1045 |103423  | 28:99:3a:06:b4:e1 |  -  |528498|   -   
|0  |20.47.149.0/24    |ROUTE| Et24               |1008 |103421  | c0:f8:7f:6a:4e:1c |  -  |528490|   -   
|0  |20.47.170.0/24    |ROUTE| Et1                |1045 |103423  | 28:99:3a:06:b4:e1 |  -  |528498|   -   
|0  |20.57.59.0/24     |ROUTE| Et25               |1013 |103426  | 60:c7:8d:2d:3c:bf |24582|528576|   -   
|0  |20.57.59.0/24     |ROUTE| Et24               |1008 |103421  | c0:f8:7f:6a:4e:1c |24582|528577|   -   
|0  |20.57.59.0/24     |ROUTE| Et24               |1008 |103421  | c0:f8:7f:6a:4e:1c |24582|528578|   -   
|0  |20.57.59.0/24     |ROUTE| Et1                |1045 |103423  | 28:99:3a:06:b4:e1 |24582|528579|   -   
|0  |20.57.59.0/24     |ROUTE| Et1                |1045 |103423  | 28:99:3a:06:b4:e1 |24582|528580|   -   
|0  |20.57.59.0/24     |ROUTE| Et46               |1050 |103424  | 34:88:18:bf:4a:30 |24582|528581|   -   
|0  |20.57.59.0/24     |ROUTE| Et46               |1050 |103424  | 34:88:18:bf:4a:30 |24582|528582|   -   
|0  |20.57.59.0/24     |ROUTE| Et25               |1013 |103426  | 60:c7:8d:2d:3c:bf |24582|528583|   -   
|0  |20.57.149.0/24    |ROUTE| Et24               |1008 |103421  | c0:f8:7f:6a:4e:1c |  -  |528490|   -   
|0  |20.57.155.0/24    |ROUTE| Et46               |1050 |103424  | 34:88:18:bf:4a:30 |  -  |528524|   -   
|0  |20.57.170.0/24    |ROUTE| Et1                |1045 |103423  | 28:99:3a:06:b4:e1 |  -  |528498|   -   
|0  |20.57.179.0/24    |ROUTE| Et25               |1013 |103426  | 60:c7:8d:2d:3c:bf |  -  |528560|   -   
|0  |20.57.211.0/24    |ROUTE| Et25               |1013 |103426  | 60:c7:8d:2d:3c:bf |24582|528576|   -   
|0  |20.57.211.0/24    |ROUTE| Et24               |1008 |103421  | c0:f8:7f:6a:4e:1c |24582|528577|   -   
|0  |20.57.211.0/24    |ROUTE| Et24               |1008 |103421  | c0:f8:7f:6a:4e:1c |24582|528578|   -   
|0  |20.57.211.0/24    |ROUTE| Et1                |1045 |103423  | 28:99:3a:06:b4:e1 |24582|528579|   -   
|0  |20.57.211.0/24    |ROUTE| Et1                |1045 |103423  | 28:99:3a:06:b4:e1 |24582|528580|   -   
|0  |20.57.211.0/24    |ROUTE| Et46               |1050 |103424  | 34:88:18:bf:4a:30 |24582|528581|   -   
|0  |20.57.211.0/24    |ROUTE| Et46               |1050 |103424  | 34:88:18:bf:4a:30 |24582|528582|   -   
|0  |20.57.211.0/24    |ROUTE| Et25               |1013 |103426  | 60:c7:8d:2d:3c:bf |24582|528583|   -   
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
|0  |20.155.179.0/24   |ROUTE| Et25               |1013 |103426  | 60:c7:8d:2d:3c:bf |24581|528572|   -   
|0  |20.155.179.0/24   |ROUTE| Et46               |1050 |103424  | 34:88:18:bf:4a:30 |24581|528573|   -   
|0  |20.155.179.0/24   |ROUTE| Et46               |1050 |103424  | 34:88:18:bf:4a:30 |24581|528574|   -   
|0  |20.155.179.0/24   |ROUTE| Et25               |1013 |103426  | 60:c7:8d:2d:3c:bf |24581|528575|   -   
|0  |20.170.171.0/32   |TRAP | CoppSystemIpBcast  |0    |  -     | BcastReceive      |  -  |524288|   -   
|0  |20.170.171.170/32 |ROUTE| Et1                |1045 |103423  | 28:99:3a:06:b4:e1 |  -  |528502|   -   
|0  |20.170.171.171/32 |TRAP | CoppSystemIpUcast  |0    |  -     | Receive           |  -  |524291|   -   
|0  |20.170.171.255/32 |TRAP | CoppSystemIpBcast  |0    |  -     | BcastReceive      |  -  |524288|   -   
|0  |20.170.171.0/24   |TRAP | CoppSystemL3DstMiss|1045 |1045    | ArpTrap           |  -  |525339|   -   
|0  |20.170.254.0/24   |ROUTE| Et1                |1045 |103423  | 28:99:3a:06:b4:e1 |  -  |528498|   -   
|0  |20.171.179.0/32   |TRAP | CoppSystemIpBcast  |0    |  -     | BcastReceive      |  -  |524288|   -   
|0  |20.171.179.171/32 |TRAP | CoppSystemIpUcast  |0    |  -     | Receive           |  -  |524291|   -   
|0  |20.171.179.179/32 |ROUTE| Et25               |1013 |103426  | 60:c7:8d:2d:3c:bf |  -  |528518|   -   
|0  |20.171.179.255/32 |TRAP | CoppSystemIpBcast  |0    |  -     | BcastReceive      |  -  |524288|   -   
|0  |20.171.179.0/24   |TRAP | CoppSystemL3DstMiss|1013 |1013    | ArpTrap           |  -  |525307|   -   
|0  |20.171.254.0/24   |ROUTE| Et24               |1008 |103421  | c0:f8:7f:6a:4e:1c |  -  |528490|   -   
|0  |127.0.0.0/8       |TRAP | CoppSystemL3DstMiss|0    |  -     | ArpTrap           |  -  |524294|   -   
|0  |192.168.20.0/23   |ROUTE| Et24               |1008 |103421  | c0:f8:7f:6a:4e:1c |  -  |528490|   -   
|0  |192.168.0.0/19    |ROUTE| Et24               |1008 |103421  | c0:f8:7f:6a:4e:1c |  -  |528490|   -   
|0  |200.111.0.0/24    |ROUTE| Et24               |1008 |103421  | c0:f8:7f:6a:4e:1c |  -  |528490|   -   
|0  |0.0.0.0/0         |TRAP | CoppSystemL3LpmOver|0    |  -     | SlowReceive       |  -  |524292|   -   
|1  |0.0.0.0/8         |DROP | DROP               |0    |  -     |                   |  -  |528484|   -   
|1  |127.0.0.0/8       |TRAP | CoppSystemL3DstMiss|0    |  -     | ArpTrap           |  -  |524294|   -   
|1  |192.168.20.0/32   |TRAP | CoppSystemIpBcast  |0    |  -     | BcastReceive      |  -  |524288|   -   
|1  |192.168.20.171/32 |TRAP | CoppSystemIpUcast  |0    |  -     | Receive           |  -  |524291|   -   
|1  |192.168.21.255/32 |TRAP | CoppSystemIpBcast  |0    |  -     | BcastReceive      |  -  |524288|   -   
|1  |192.168.20.0/23   |TRAP | CoppSystemL3DstMiss|0    |  -     | ArpTrap           |  -  |524294|   -   
|1  |0.0.0.0/0         |TRAP | CoppSystemL3DstMiss|0    |  -     | ArpTrap           |  -  |524294|   -   
|2  |0.0.0.0/8         |DROP | DROP               |0    |  -     |                   |  -  |528566|   -   
|2  |20.19.111.0/24    |ROUTE| FEC 528542         |0    |2097141 | 00:00:00:00:00:00 |  -  |288360|M 20019 1279
|2  |20.55.111.0/24    |ROUTE| FEC 528538         |0    |2097146 | 00:00:00:00:00:00 |  -  |288364|M 24004
|2  |20.57.111.0/24    |ROUTE| FEC 24584          |0    |2097142 | 00:00:00:00:00:00 |  -  |288368|M 20057 524287
|2  |20.83.111.0/24    |ROUTE| FEC 528542         |0    |2097143 | 00:00:00:00:00:00 |  -  |288362|M 20083 18
|2  |127.0.0.0/8       |TRAP | CoppSystemL3DstMiss|0    |  -     | ArpTrap           |  -  |524294|   -   
|2  |0.0.0.0/0         |TRAP | CoppSystemL3LpmOver|0    |  -     | SlowReceive       |  -  |524292|   -   
|3  |0.0.0.0/8         |DROP | DROP               |0    |  -     |                   |  -  |528494|   -   
|3  |20.57.111.0/24    |ROUTE| FEC 24577          |0    |2097150 | 00:00:00:00:00:00 |  -  |288372|M 21057 524286
|3  |20.111.155.0/24   |ROUTE| FEC 528538         |0    |2097130 | 00:00:00:00:00:00 |  -  |288400|M 24009
|3  |20.111.171.0/32   |TRAP | CoppSystemIpBcast  |0    |  -     | BcastReceive      |  -  |524288|   -   
|3  |20.111.171.171/32 |TRAP | CoppSystemIpUcast  |0    |  -     | Receive           |  -  |524291|   -   
|3  |20.111.171.255/32 |TRAP | CoppSystemIpBcast  |0    |  -     | BcastReceive      |  -  |524288|   -   
|3  |20.111.171.0/24   |TRAP | CoppSystemL3DstMiss|1007 |1007    | ArpTrap           |  -  |525301|   -   
|3  |20.111.179.0/24   |ROUTE| FEC 528558         |0    |2097140 | 00:00:00:00:00:00 |  -  |288396|M 19
|3  |20.111.254.0/24   |ROUTE| FEC 528542         |0    |2097134 | 00:00:00:00:00:00 |  -  |288390|M 21254 48091
|3  |127.0.0.0/8       |TRAP | CoppSystemL3DstMiss|0    |  -     | ArpTrap           |  -  |524294|   -   
|3  |0.0.0.0/0         |TRAP | CoppSystemL3LpmOver|0    |  -     | SlowReceive       |  -  |524292|   -   
|4  |0.0.0.0/8         |DROP | DROP               |0    |  -     |                   |  -  |528488|   -   
|4  |20.57.111.0/24    |ROUTE| FEC 24577          |0    |2097129 | 00:00:00:00:00:00 |  -  |288378|M 21157 524284
|4  |20.111.155.0/24   |ROUTE| FEC 528538         |0    |2097126 | 00:00:00:00:00:00 |  -  |288404|M 24010
|4  |20.111.171.0/32   |TRAP | CoppSystemIpBcast  |0    |  -     | BcastReceive      |  -  |524288|   -   
|4  |20.111.171.171/32 |TRAP | CoppSystemIpUcast  |0    |  -     | Receive           |  -  |524291|   -   
|4  |20.111.171.255/32 |TRAP | CoppSystemIpBcast  |0    |  -     | BcastReceive      |  -  |524288|   -   
|4  |20.111.171.0/24   |TRAP | CoppSystemL3DstMiss|1010 |1010    | ArpTrap           |  -  |525304|   -   
|4  |20.111.179.0/24   |ROUTE| FEC 528536         |0    |2097132 | 00:00:00:00:00:00 |  -  |288398|M 21279 20
|4  |20.111.254.0/24   |ROUTE| FEC 528542         |0    |2097133 | 00:00:00:00:00:00 |  -  |288392|M 21354 48092
|4  |127.0.0.0/8       |TRAP | CoppSystemL3DstMiss|0    |  -     | ArpTrap           |  -  |524294|   -   
|4  |0.0.0.0/0         |TRAP | CoppSystemL3LpmOver|0    |  -     | SlowReceive       |  -  |524292|   -   
|5  |0.0.0.0/8         |DROP | DROP               |0    |  -     |                   |  -  |528512|   -   
|5  |20.57.111.0/24    |ROUTE| FEC 24583          |0    |2097144 | 00:00:00:00:00:00 |  -  |288382|M 21257 524283
|5  |20.111.155.0/24   |ROUTE| FEC 528538         |0    |2097135 | 00:00:00:00:00:00 |  -  |288384|M 24012
|5  |20.111.171.0/32   |TRAP | CoppSystemIpBcast  |0    |  -     | BcastReceive      |  -  |524288|   -   
|5  |20.111.171.171/32 |TRAP | CoppSystemIpUcast  |0    |  -     | Receive           |  -  |524291|   -   
|5  |20.111.171.255/32 |TRAP | CoppSystemIpBcast  |0    |  -     | BcastReceive      |  -  |524288|   -   
|5  |20.111.171.0/24   |TRAP | CoppSystemL3DstMiss|1011 |1011    | ArpTrap           |  -  |525305|   -   
|5  |20.111.179.0/24   |ROUTE| FEC 528530         |0    |2097151 | 00:00:00:00:00:00 |  -  |288394|M 21
|5  |20.111.254.0/24   |ROUTE| FEC 528542         |0    |2097145 | 00:00:00:00:00:00 |  -  |288366|M 21454 48093
|5  |127.0.0.0/8       |TRAP | CoppSystemL3DstMiss|0    |  -     | ArpTrap           |  -  |524294|   -   
|5  |0.0.0.0/0         |TRAP | CoppSystemL3LpmOver|0    |  -     | SlowReceive       |  -  |524292|   -   
|6  |0.0.0.0/8         |DROP | DROP               |0    |  -     |                   |  -  |528510|   -   
|6  |20.57.111.0/24    |ROUTE| FEC 528522         |0    |2097136 | 00:00:00:00:00:00 |  -  |288370|M 21357 524282
|6  |20.111.155.0/24   |ROUTE| FEC 528538         |0    |2097139 | 00:00:00:00:00:00 |  -  |288402|M 24011
|6  |20.111.171.0/32   |TRAP | CoppSystemIpBcast  |0    |  -     | BcastReceive      |  -  |524288|   -   
|6  |20.111.171.171/32 |TRAP | CoppSystemIpUcast  |0    |  -     | Receive           |  -  |524291|   -   
|6  |20.111.171.255/32 |TRAP | CoppSystemIpBcast  |0    |  -     | BcastReceive      |  -  |524288|   -   
|6  |20.111.171.0/24   |TRAP | CoppSystemL3DstMiss|1012 |1012    | ArpTrap           |  -  |525306|   -   
|6  |20.111.179.0/24   |ROUTE| FEC 528500         |0    |2097122 | 00:00:00:00:00:00 |  -  |288386|M 22
|6  |20.111.254.0/24   |ROUTE| FEC 528522         |0    |2097137 | 00:00:00:00:00:00 |  -  |288388|M 21554 48094
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
|24581|528572|ROUTE| Et25               |1013 |103426  | 60:c7:8d:2d:3c:bf |   -   
|24581|528573|ROUTE| Et46               |1050 |103424  | 34:88:18:bf:4a:30 |   -   
|24581|528574|ROUTE| Et46               |1050 |103424  | 34:88:18:bf:4a:30 |   -   
|24581|528575|ROUTE| Et25               |1013 |103426  | 60:c7:8d:2d:3c:bf |   -   
|24582|528576|ROUTE| Et25               |1013 |103426  | 60:c7:8d:2d:3c:bf |   -   
|24582|528577|ROUTE| Et24               |1008 |103421  | c0:f8:7f:6a:4e:1c |   -   
|24582|528578|ROUTE| Et24               |1008 |103421  | c0:f8:7f:6a:4e:1c |   -   
|24582|528579|ROUTE| Et1                |1045 |103423  | 28:99:3a:06:b4:e1 |   -   
|24582|528580|ROUTE| Et1                |1045 |103423  | 28:99:3a:06:b4:e1 |   -   
|24582|528581|ROUTE| Et46               |1050 |103424  | 34:88:18:bf:4a:30 |   -   
|24582|528582|ROUTE| Et46               |1050 |103424  | 34:88:18:bf:4a:30 |   -   
|24582|528583|ROUTE| Et25               |1013 |103426  | 60:c7:8d:2d:3c:bf |   -   
|24583|528588|ROUTE| Et25               |1013 |103426  | 60:c7:8d:2d:3c:bf |   -   
|24583|528589|ROUTE| Et24               |1008 |103421  | c0:f8:7f:6a:4e:1c |   -   
|24583|528590|ROUTE| Et24               |1008 |103421  | c0:f8:7f:6a:4e:1c |   -   
|24583|528591|ROUTE| Et46               |1050 |103424  | 34:88:18:bf:4a:30 |   -   
|24583|528592|ROUTE| Et46               |1050 |103424  | 34:88:18:bf:4a:30 |   -   
|24583|528593|ROUTE| Et25               |1013 |103426  | 60:c7:8d:2d:3c:bf |   -   
|24584|528594|ROUTE| Et25               |1013 |103426  | 60:c7:8d:2d:3c:bf |   -   
|24584|528595|ROUTE| Et24               |1008 |103421  | c0:f8:7f:6a:4e:1c |   -   
|24584|528596|ROUTE| Et24               |1008 |103421  | c0:f8:7f:6a:4e:1c |   -   
|24584|528597|ROUTE| Et1                |1045 |103423  | 28:99:3a:06:b4:e1 |   -   
|24584|528598|ROUTE| Et1                |1045 |103423  | 28:99:3a:06:b4:e1 |   -   
|24584|528599|ROUTE| Et46               |1050 |103424  | 34:88:18:bf:4a:30 |   -   
|24584|528600|ROUTE| Et46               |1050 |103424  | 34:88:18:bf:4a:30 |   -   
|24584|528601|ROUTE| Et25               |1013 |103426  | 60:c7:8d:2d:3c:bf |   -   
|24585|528602|ROUTE| Et25               |1013 |103426  | 60:c7:8d:2d:3c:bf |   -   
|24585|528603|ROUTE| Et24               |1008 |103421  | c0:f8:7f:6a:4e:1c |   -   
|24585|528604|ROUTE| Et24               |1008 |103421  | c0:f8:7f:6a:4e:1c |   -   
|24585|528605|ROUTE| Et46               |1050 |103424  | 34:88:18:bf:4a:30 |   -   
|24585|528606|ROUTE| Et46               |1050 |103424  | 34:88:18:bf:4a:30 |   -   
|24585|528607|ROUTE| Et25               |1013 |103426  | 60:c7:8d:2d:3c:bf |   -   
|  -  |288360|ROUTE| FEC 528542         |   - |2097141 |                 - |Mpush 20019 1279
|  -  |288362|ROUTE| FEC 528542         |   - |2097143 |                 - |Mpush 20083 18
|  -  |288364|ROUTE| FEC 528538         |   - |2097146 |                 - |Mpush 24004
|  -  |288366|ROUTE| FEC 528542         |   - |2097145 |                 - |Mpush 21454 48093
|  -  |288368|ROUTE| FEC 24584          |   - |2097142 |                 - |Mpush 20057 524287
|  -  |288370|ROUTE| FEC 528522         |   - |2097136 |                 - |Mpush 21357 524282
|  -  |288372|ROUTE| FEC 24577          |   - |2097150 |                 - |Mpush 21057 524286
|  -  |288378|ROUTE| FEC 24577          |   - |2097129 |                 - |Mpush 21157 524284
|  -  |288382|ROUTE| FEC 24583          |   - |2097144 |                 - |Mpush 21257 524283
|  -  |288384|ROUTE| FEC 528538         |   - |2097135 |                 - |Mpush 24012
|  -  |288386|ROUTE| FEC 528500         |   - |2097122 |                 - |Mpush 22
|  -  |288388|ROUTE| FEC 528522         |   - |2097137 |                 - |Mpush 21554 48094
|  -  |288390|ROUTE| FEC 528542         |   - |2097134 |                 - |Mpush 21254 48091
|  -  |288392|ROUTE| FEC 528542         |   - |2097133 |                 - |Mpush 21354 48092
|  -  |288394|ROUTE| FEC 528530         |   - |2097151 |                 - |Mpush 21
|  -  |288396|ROUTE| FEC 528558         |   - |2097140 |                 - |Mpush 19
|  -  |288398|ROUTE| FEC 528536         |   - |2097132 |                 - |Mpush 21279 20
|  -  |288400|ROUTE| FEC 528538         |   - |2097130 |                 - |Mpush 24009
|  -  |288402|ROUTE| FEC 528538         |   - |2097139 |                 - |Mpush 24011
|  -  |288404|ROUTE| FEC 528538         |   - |2097126 |                 - |Mpush 24010
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
|  -  |525307|TRAP | CoppSystemL3DstMiss|1013 |1013    | ArpTrap           |   -   
|  -  |525339|TRAP | CoppSystemL3DstMiss|1045 |1045    | ArpTrap           |   -   
|  -  |525344|TRAP | CoppSystemL3DstMiss|1050 |1050    | ArpTrap           |   -   
|  -  |528482|DROP | DROP               |0    |  -     |                   |   -   
|  -  |528484|DROP | DROP               |0    |  -     |                   |   -   
|  -  |528486|ROUTE| Et24               |1008 |103421  | c0:f8:7f:6a:4e:1c |   -   
|  -  |528488|DROP | DROP               |0    |  -     |                   |   -   
|  -  |528490|ROUTE| Et24               |1008 |103421  | c0:f8:7f:6a:4e:1c |   -   
|  -  |528492|ROUTE| Et24               |1008 |103421  | c0:f8:7f:6a:4e:1c |   -   
|  -  |528494|DROP | DROP               |0    |  -     |                   |   -   
|  -  |528496|ROUTE| Et46               |1050 |103424  | 34:88:18:bf:4a:30 |   -   
|  -  |528497|ROUTE| Et24               |1008 |103439  | c0:f8:7f:6a:4e:1c |Mpush 21555
|  -  |528498|ROUTE| Et1                |1045 |103423  | 28:99:3a:06:b4:e1 |   -   
|  -  |528500|ROUTE| Et25               |1013 |103426  | 60:c7:8d:2d:3c:bf |   -   
|  -  |528501|ROUTE| Et46               |1050 |103442  | 34:88:18:bf:4a:30 |Mpush 20379
|  -  |528502|ROUTE| Et1                |1045 |103423  | 28:99:3a:06:b4:e1 |   -   
|  -  |528508|ROUTE| Et1                |1045 |103423  | 28:99:3a:06:b4:e1 |   -   
|  -  |528510|DROP | DROP               |0    |  -     |                   |   -   
|  -  |528512|DROP | DROP               |0    |  -     |                   |   -   
|  -  |528514|ROUTE| Et46               |1050 |103424  | 34:88:18:bf:4a:30 |   -   
|  -  |528516|ROUTE| Et46               |1050 |103424  | 34:88:18:bf:4a:30 |   -   
|  -  |528518|ROUTE| Et25               |1013 |103426  | 60:c7:8d:2d:3c:bf |   -   
|  -  |528520|ROUTE| Et24               |1008 |103421  | c0:f8:7f:6a:4e:1c |   -   
|  -  |528521|ROUTE| Et46               |1050 |103425  | 34:88:18:bf:4a:30 |Mpush 21449
|  -  |528522|ROUTE| Et46               |1050 |103424  | 34:88:18:bf:4a:30 |   -   
|  -  |528524|ROUTE| Et46               |1050 |103424  | 34:88:18:bf:4a:30 |   -   
|  -  |528530|ROUTE| Et25               |1013 |103426  | 60:c7:8d:2d:3c:bf |   -   
|  -  |528536|ROUTE| Et46               |1050 |103424  | 34:88:18:bf:4a:30 |   -   
|  -  |528537|ROUTE| Et24               |1008 |103429  | c0:f8:7f:6a:4e:1c |Mpush 21157
|  -  |528538|ROUTE| Et46               |1050 |103424  | 34:88:18:bf:4a:30 |   -   
|  -  |528539|ROUTE| Et24               |1008 |103427  | c0:f8:7f:6a:4e:1c |Mpush 20355
|  -  |528540|ROUTE| Et24               |1008 |103421  | c0:f8:7f:6a:4e:1c |   -   
|  -  |528541|ROUTE| Et46               |1050 |103431  | 34:88:18:bf:4a:30 |Mpush 21649
|  -  |528542|ROUTE| Et24               |1008 |103421  | c0:f8:7f:6a:4e:1c |   -   
|  -  |528543|ROUTE| Et46               |1050 |103424  | 34:88:18:bf:4a:30 |   -   
|  -  |528544|ROUTE| Et24               |1008 |103421  | c0:f8:7f:6a:4e:1c |   -   
|  -  |528545|ROUTE| Et46               |1050 |103432  | 34:88:18:bf:4a:30 |Mpush 20349
|  -  |528554|ROUTE| Et46               |1050 |103424  | 34:88:18:bf:4a:30 |   -   
|  -  |528555|ROUTE| Et24               |1008 |103430  | c0:f8:7f:6a:4e:1c |Mpush 21455
|  -  |528556|ROUTE| Et24               |1008 |103421  | c0:f8:7f:6a:4e:1c |   -   
|  -  |528557|ROUTE| Et46               |1050 |103428  | 34:88:18:bf:4a:30 |Mpush 21349
|  -  |528558|ROUTE| Et25               |1013 |103426  | 60:c7:8d:2d:3c:bf |   -   
|  -  |528559|ROUTE| Et46               |1050 |103436  | 34:88:18:bf:4a:30 |Mpush 21179
|  -  |528560|ROUTE| Et25               |1013 |103426  | 60:c7:8d:2d:3c:bf |   -   
|  -  |528562|ROUTE| Et46               |1050 |103424  | 34:88:18:bf:4a:30 |   -   
|  -  |528563|ROUTE| Et24               |1008 |103433  | c0:f8:7f:6a:4e:1c |Mpush 24013
|  -  |528564|ROUTE| Et1                |1045 |103423  | 28:99:3a:06:b4:e1 |   -   
|  -  |528565|ROUTE| Et24               |1008 |103422  | c0:f8:7f:6a:4e:1c |Mpush 20057 20170
|  -  |528566|DROP | DROP               |0    |  -     |                   |   -   
|  -  |528584|ROUTE| Et25               |1013 |103426  | 60:c7:8d:2d:3c:bf |   -   

```

