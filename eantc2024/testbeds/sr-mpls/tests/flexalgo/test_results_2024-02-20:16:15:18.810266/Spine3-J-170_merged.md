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

Uptime: 1 day, 5 hours and 36 minutes
Total memory: 8051592 kB
Free memory: 5877276 kB

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
Interface       IP Address            Status     Protocol         MTU   Owner  
--------------- --------------------- ---------- ------------ --------- -------
Ethernet1       20.170.171.170/24     up         up              1500          
Ethernet3       20.47.170.170/24      up         up              1500          
Ethernet43      20.32.170.170/24      up         up              1500          
Ethernet45      20.57.170.170/24      up         up              1500          
Ethernet48      20.170.254.170/24     up         up              1500          
Loopback0       10.0.0.170/32         up         up             65535          
Management1     192.168.20.170/23     up         up              1500          

```

## show interfaces counters rates | nz

```text
Port      Name            Intvl  In Mbps      %  In Kpps Out Mbps      %

Port      Out Kpps
```

## show isis neighbors

```text
 
Instance  VRF      System Id        Type Interface          SNPA              State Hold time   Circuit Id          
IGP       default  0000.0000.0032   L2   Ethernet43         P2P               UP    89          00                  
IGP       default  SR1-SRMPLS       L2   Ethernet45         P2P               UP    23          00                  
IGP       default  PE31-J2-171      L2   Ethernet1          P2P               UP    23          50                  
```

## show isis database detail

```text
Legend:
H - hostname conflict
U - node unreachable

IS-IS Instance: IGP VRF: default
  IS-IS Level 2 Link State Database
    LSPID                   Seq Num  Cksum  Life Length IS  Received LSPID        Flags
    0000.0000.0019.00-00        317   4917  1165    160 L2  0000.0000.0019.00-00  <>
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
    eantc-jcnr2.00-00           453   1608   452    229 L2  0000.0000.0020.00-00  <>
      Remaining lifetime received: 1199 s Modified to: 1200 s
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
    12502-1.00-00               668  24241  1177    515 L2  0000.0000.0024.00-00  <>
      Remaining lifetime received: 1199 s Modified to: 1200 s
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
    huawei_34_NetEngine_8000_F8.00-00       148  54651   939    293 L2  0000.0000.0254.00-00  <>
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
    h55-8201-24H8FH.00-00       160  64064   540    720 L2  0000.0000.0355.00-00  <>
      Remaining lifetime received: 1199 s Modified to: 1200 s
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
    0010.0010.0005.00-00         23  30543   718    280 L2  0010.0010.0005.00-00  <>
      Remaining lifetime received: 1199 s Modified to: 1200 s
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
    SR1-SRMPLS.00-00            726  53685  1176    832 L2  0100.0000.0057.00-00  <>
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
      LSP generation remaining wait time: 0 ms
      Time remaining until refresh: 788 s
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
    PE31-J2-171.00-00           173  51996   742    442 L2  0100.0000.0171.00-00  <>
      Remaining lifetime received: 1199 s Modified to: 1200 s
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
    3800.0000.4111.00-00         14  19126   938    142 L2  3800.0000.4111.00-00  <DefaultAtt>
      Remaining lifetime received: 1199 s Modified to: 1200 s
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

```

## show isis flex-algo path detail

```text
```

## show isis segment-routing tunnel

```text
  Index     Endpoint          Next Hop/Tunnel Index     Interface     Labels   
--------- ----------------- ------------------------- --------------- ---------
  2         10.0.0.254/32     20.57.170.57              Ethernet45    [ 20254 ]
                              20.170.171.171            Ethernet1     [ 20254 ]
  6         10.0.0.171/32     TI-LFA (0)                -             [ 3 ]    
  7         10.0.1.49/32      20.57.170.57              Ethernet45    [ 20349 ]
                              20.170.171.171            Ethernet1     [ 20349 ]
  8         10.0.1.55/32      20.57.170.57              Ethernet45    [ 20355 ]
                              20.170.171.171            Ethernet1     [ 20355 ]
  9         10.0.0.179/32     20.57.170.57              Ethernet45    [ 20379 ]
                              20.170.171.171            Ethernet1     [ 20379 ]
  11        10.0.0.57/32      TI-LFA (7)                -             [ 20057 ]
  12        10.0.0.19/32      20.57.170.57              Ethernet45    [ 20019 ]
                              20.170.171.171            Ethernet1     [ 20019 ]
  17        10.0.0.83/32      20.57.170.57              Ethernet45    [ 20083 ]
                              20.170.171.171            Ethernet1     [ 20083 ]

```

## show isis segment-routing prefix-segments

```text

System ID: Spine3-J-170			Instance: 'IGP'
SR supported Data-plane: MPLS			SR Router ID: 100.0.0.170

Node: 38     Proxy-Node: 0      Prefix: 4       Total Segments: 42

Flag Descriptions: R: Re-advertised, N: Node Segment, P: no-PHP
                   E: Explicit-NULL, V: Value, L: Local
Segment status codes: * - Self originated Prefix, L1 - level 1, L2 - level 2, ! - SR-unreachable,
                      # - Some IS-IS next-hops are SR-unreachable
   Prefix                      SID Type       Flags                        System ID       Level Protection  Algorithm   
   ------------------------- ----- ---------- ---------------------------- --------------- ----- ----------- -------------
   10.0.0.19/32                 19 Node       R:0 N:1 P:0 E:0 V:0 L:0      0000.0000.0019  L2    unprotected SPF         
   10.0.0.24/32               1024 Node       R:0 N:1 P:1 E:0 V:0 L:0      12502-1         L2    unprotected 128         
   10.0.0.24/32               1124 Node       R:0 N:1 P:1 E:0 V:0 L:0      12502-1         L2    unprotected 129         
   10.0.0.24/32               1224 Node       R:0 N:1 P:1 E:0 V:0 L:0      12502-1         L2    unprotected 130         
   10.0.0.24/32               1324 Node       R:0 N:1 P:1 E:0 V:0 L:0      12502-1         L2    unprotected 131         
   10.0.0.57/32                 57 Node       R:0 N:1 P:1 E:0 V:0 L:0      SR1-SRMPLS      L2    node        SPF         
   10.0.0.57/32               1057 Node       R:0 N:1 P:1 E:0 V:0 L:0      SR1-SRMPLS      L2    unprotected 128         
   10.0.0.57/32               1157 Node       R:0 N:1 P:1 E:0 V:0 L:0      SR1-SRMPLS      L2    unprotected 129         
   10.0.0.57/32               1257 Node       R:0 N:1 P:1 E:0 V:0 L:0      SR1-SRMPLS      L2    unprotected 130         
   10.0.0.57/32               1357 Node       R:0 N:1 P:1 E:0 V:0 L:0      SR1-SRMPLS      L2    unprotected 131         
   10.0.0.57/32               1457 Node       R:0 N:1 P:1 E:0 V:0 L:0      SR1-SRMPLS      L2    unprotected 132         
   10.0.0.83/32                 83 Node       R:0 N:1 P:0 E:0 V:0 L:0      eantc-jcnr2     L2    unprotected SPF         
*  10.0.0.170/32               170 Node       R:0 N:1 P:0 E:0 V:0 L:0      Spine3-J-170    L2    unprotected SPF         
   10.0.0.171/32               171 Node       R:0 N:1 P:0 E:0 V:0 L:0      PE31-J2-171     L2    node        SPF         
   10.0.0.171/32              1171 Node       R:0 N:1 P:0 E:0 V:0 L:0      PE31-J2-171     L2    unprotected 128         
   10.0.0.171/32              1271 Node       R:0 N:1 P:0 E:0 V:0 L:0      PE31-J2-171     L2    unprotected 129         
   10.0.0.171/32              1371 Node       R:0 N:1 P:0 E:0 V:0 L:0      PE31-J2-171     L2    unprotected 130         
   10.0.0.171/32              1471 Node       R:0 N:1 P:0 E:0 V:0 L:0      PE31-J2-171     L2    unprotected 131         
   10.0.0.179/32               379 Node       R:0 N:1 P:0 E:0 V:0 L:0      juniper_379_MX304 L2    unprotected SPF         
   10.0.0.179/32              1179 Node       R:0 N:1 P:0 E:0 V:0 L:0      juniper_379_MX304 L2    unprotected 128         
   10.0.0.179/32              1279 Node       R:0 N:1 P:0 E:0 V:0 L:0      juniper_379_MX304 L2    unprotected 129         
   10.0.0.179/32              1379 Node       R:0 N:1 P:0 E:0 V:0 L:0      juniper_379_MX304 L2    unprotected 130         
   10.0.0.254/32               254 Node       R:0 N:1 P:0 E:0 V:0 L:0      huawei_34_NetEngine_8000_F8 L2    unprotected SPF         
   10.0.0.254/32              1254 Node       R:0 N:1 P:0 E:0 V:0 L:0      huawei_34_NetEngine_8000_F8 L2    unprotected 128         
   10.0.0.254/32              1354 Node       R:0 N:1 P:0 E:0 V:0 L:0      huawei_34_NetEngine_8000_F8 L2    unprotected 129         
   10.0.0.254/32              1454 Node       R:0 N:1 P:0 E:0 V:0 L:0      huawei_34_NetEngine_8000_F8 L2    unprotected 130         
   10.0.0.254/32              1554 Node       R:0 N:1 P:0 E:0 V:0 L:0      huawei_34_NetEngine_8000_F8 L2    unprotected 131         
   10.0.1.49/32                349 Node       R:0 N:1 P:0 E:0 V:0 L:0      h49-N540-24Q8L2DD L2    unprotected SPF         
   10.0.1.49/32               1349 Node       R:0 N:1 P:0 E:0 V:0 L:0      h49-N540-24Q8L2DD L2    unprotected 128         
   10.0.1.49/32               1449 Node       R:0 N:1 P:0 E:0 V:0 L:0      h49-N540-24Q8L2DD L2    unprotected 129         
   10.0.1.49/32               1649 Node       R:0 N:1 P:0 E:0 V:0 L:0      h49-N540-24Q8L2DD L2    unprotected 130         
   10.0.1.49/32               1749 Node       R:0 N:1 P:0 E:0 V:0 L:0      h49-N540-24Q8L2DD L2    unprotected 132         
   10.0.1.55/32                355 Node       R:0 N:1 P:0 E:0 V:0 L:0      h55-8201-24H8FH L2    unprotected SPF         
   10.0.1.55/32               1355 Node       R:0 N:1 P:0 E:0 V:0 L:0      h55-8201-24H8FH L2    unprotected 128         
   10.0.1.55/32               1455 Node       R:0 N:1 P:0 E:0 V:0 L:0      h55-8201-24H8FH L2    unprotected 129         
   10.0.1.55/32               1555 Node       R:0 N:1 P:0 E:0 V:0 L:0      h55-8201-24H8FH L2    unprotected 130         
   10.0.1.55/32               1655 Node       R:0 N:1 P:0 E:0 V:0 L:0      h55-8201-24H8FH L2    unprotected 131         
   10.0.1.55/32               1755 Node       R:0 N:1 P:0 E:0 V:0 L:0      h55-8201-24H8FH L2    unprotected 132         
   200.111.0.0/24             1111 Prefix     R:0 N:0 P:0 E:0 V:0 L:0      3800.0000.4111  L2    unprotected 128         
   200.111.0.0/24             1211 Prefix     R:0 N:0 P:0 E:0 V:0 L:0      3800.0000.4111  L2    unprotected 129         
   200.111.0.0/24             1311 Prefix     R:0 N:0 P:0 E:0 V:0 L:0      3800.0000.4111  L2    unprotected 130         
   200.111.0.0/24             1411 Prefix     R:0 N:0 P:0 E:0 V:0 L:0      3800.0000.4111  L2    unprotected 131         
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
           via 20.170.171.171, Ethernet1
           via 20.57.170.57, Ethernet45
 I L2     10.0.0.19/32 [115/30]
           via 20.170.171.171, Ethernet1
           via 20.57.170.57, Ethernet45
 I L2     10.0.0.24/32 [115/30]
           via 20.170.171.171, Ethernet1
           via 20.57.170.57, Ethernet45
 I L2     10.0.0.57/32 [115/10]
           via 20.57.170.57, Ethernet45
 I L2     10.0.0.83/32 [115/30]
           via 20.170.171.171, Ethernet1
           via 20.57.170.57, Ethernet45
 C        10.0.0.170/32
           directly connected, Loopback0
 I L2     10.0.0.171/32 [115/10]
           via 20.170.171.171, Ethernet1
 I L2     10.0.0.179/32 [115/20]
           via 20.170.171.171, Ethernet1
           via 20.57.170.57, Ethernet45
 I L2     10.0.0.254/32 [115/30]
           via 20.170.171.171, Ethernet1
           via 20.57.170.57, Ethernet45
 I L2     10.0.1.49/32 [115/20]
           via 20.170.171.171, Ethernet1
           via 20.57.170.57, Ethernet45
 I L2     10.0.1.55/32 [115/20]
           via 20.170.171.171, Ethernet1
           via 20.57.170.57, Ethernet45
 I L2     20.5.149.0/24 [115/30]
           via 20.170.171.171, Ethernet1
           via 20.57.170.57, Ethernet45
 I L2     20.19.149.0/24 [115/30]
           via 20.170.171.171, Ethernet1
           via 20.57.170.57, Ethernet45
 I L2     20.19.211.0/24 [115/30]
           via 20.170.171.171, Ethernet1
           via 20.57.170.57, Ethernet45
 I L2     20.24.149.0/24 [115/30]
           via 20.170.171.171, Ethernet1
           via 20.57.170.57, Ethernet45
 I L2     20.24.211.0/24 [115/40]
           via 20.170.171.171, Ethernet1
           via 20.57.170.57, Ethernet45
 I L2     20.32.149.0/24 [115/30]
           via 20.170.171.171, Ethernet1
           via 20.57.170.57, Ethernet45
 C        20.32.170.0/24
           directly connected, Ethernet43
 I L2     20.47.149.0/24 [115/30]
           via 20.170.171.171, Ethernet1
           via 20.57.170.57, Ethernet45
 C        20.47.170.0/24
           directly connected, Ethernet3
 I L2     20.57.59.0/24 [115/20]
           via 20.57.170.57, Ethernet45
 I L2     20.57.149.0/24 [115/20]
           via 20.57.170.57, Ethernet45
 I L2     20.57.155.0/24 [115/20]
           via 20.57.170.57, Ethernet45
 C        20.57.170.0/24
           directly connected, Ethernet45
 I L2     20.57.179.0/24 [115/20]
           via 20.57.170.57, Ethernet45
 I L2     20.57.211.0/24 [115/20]
           via 20.57.170.57, Ethernet45
 I L2     20.83.149.0/24 [115/30]
           via 20.170.171.171, Ethernet1
           via 20.57.170.57, Ethernet45
 I L2     20.111.149.0/24 [115/30]
           via 20.170.171.171, Ethernet1
           via 20.57.170.57, Ethernet45
 I L2     20.149.155.0/24 [115/30]
           via 20.170.171.171, Ethernet1
           via 20.57.170.57, Ethernet45
 I L2     20.149.171.0/24 [115/20]
           via 20.170.171.171, Ethernet1
 I L2     20.149.254.0/24 [115/30]
           via 20.170.171.171, Ethernet1
           via 20.57.170.57, Ethernet45
 I L2     20.155.171.0/24 [115/20]
           via 20.170.171.171, Ethernet1
 I L2     20.155.179.0/24 [115/30]
           via 20.170.171.171, Ethernet1
           via 20.57.170.57, Ethernet45
 C        20.170.171.0/24
           directly connected, Ethernet1
 C        20.170.254.0/24
           directly connected, Ethernet48
 I L2     20.171.179.0/24 [115/20]
           via 20.170.171.171, Ethernet1
 I L2     20.171.254.0/24 [115/40]
           via 20.170.171.171, Ethernet1
           via 20.57.170.57, Ethernet45
 I L2     192.168.20.0/23 [115/30]
           via 20.170.171.171, Ethernet1
           via 20.57.170.57, Ethernet45
 I L2     192.168.0.0/19 [115/30]
           via 20.170.171.171, Ethernet1
           via 20.57.170.57, Ethernet45
 I L2     200.111.0.0/24 [115/30]
           via 20.170.171.171, Ethernet1
           via 20.57.170.57, Ethernet45

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
           via 20.170.171.171, Ethernet1
           via 20.57.170.57, Ethernet45
 I L2     10.0.0.19/32 [115/30]
           via 20.170.171.171, Ethernet1
           via 20.57.170.57, Ethernet45
 I L2     10.0.0.24/32 [115/30]
           via 20.170.171.171, Ethernet1
           via 20.57.170.57, Ethernet45
 I L2     10.0.0.57/32 [115/10]
           via 20.57.170.57, Ethernet45
 I L2     10.0.0.83/32 [115/30]
           via 20.170.171.171, Ethernet1
           via 20.57.170.57, Ethernet45
 C        10.0.0.170/32
           directly connected, Loopback0
 I L2     10.0.0.171/32 [115/10]
           via 20.170.171.171, Ethernet1
 I L2     10.0.0.179/32 [115/20]
           via 20.170.171.171, Ethernet1
           via 20.57.170.57, Ethernet45
 I L2     10.0.0.254/32 [115/30]
           via 20.170.171.171, Ethernet1
           via 20.57.170.57, Ethernet45
 I L2     10.0.1.49/32 [115/20]
           via 20.170.171.171, Ethernet1
           via 20.57.170.57, Ethernet45
 I L2     10.0.1.55/32 [115/20]
           via 20.170.171.171, Ethernet1
           via 20.57.170.57, Ethernet45
 I L2     20.5.149.0/24 [115/30]
           via 20.170.171.171, Ethernet1
           via 20.57.170.57, Ethernet45
 I L2     20.19.149.0/24 [115/30]
           via 20.170.171.171, Ethernet1
           via 20.57.170.57, Ethernet45
 I L2     20.19.211.0/24 [115/30]
           via 20.170.171.171, Ethernet1
           via 20.57.170.57, Ethernet45
 I L2     20.24.149.0/24 [115/30]
           via 20.170.171.171, Ethernet1
           via 20.57.170.57, Ethernet45
 I L2     20.24.211.0/24 [115/40]
           via 20.170.171.171, Ethernet1
           via 20.57.170.57, Ethernet45
 I L2     20.32.149.0/24 [115/30]
           via 20.170.171.171, Ethernet1
           via 20.57.170.57, Ethernet45
 C        20.32.170.0/24
           directly connected, Ethernet43
 I L2     20.47.149.0/24 [115/30]
           via 20.170.171.171, Ethernet1
           via 20.57.170.57, Ethernet45
 C        20.47.170.0/24
           directly connected, Ethernet3
 I L2     20.57.59.0/24 [115/20]
           via 20.57.170.57, Ethernet45
 I L2     20.57.149.0/24 [115/20]
           via 20.57.170.57, Ethernet45
 I L2     20.57.155.0/24 [115/20]
           via 20.57.170.57, Ethernet45
 C        20.57.170.0/24
           directly connected, Ethernet45
 I L2     20.57.179.0/24 [115/20]
           via 20.57.170.57, Ethernet45
 I L2     20.57.211.0/24 [115/20]
           via 20.57.170.57, Ethernet45
 I L2     20.83.149.0/24 [115/30]
           via 20.170.171.171, Ethernet1
           via 20.57.170.57, Ethernet45
 I L2     20.111.149.0/24 [115/30]
           via 20.170.171.171, Ethernet1
           via 20.57.170.57, Ethernet45
 I L2     20.149.155.0/24 [115/30]
           via 20.170.171.171, Ethernet1
           via 20.57.170.57, Ethernet45
 I L2     20.149.171.0/24 [115/20]
           via 20.170.171.171, Ethernet1
 I L2     20.149.254.0/24 [115/30]
           via 20.170.171.171, Ethernet1
           via 20.57.170.57, Ethernet45
 I L2     20.155.171.0/24 [115/20]
           via 20.170.171.171, Ethernet1
 I L2     20.155.179.0/24 [115/30]
           via 20.170.171.171, Ethernet1
           via 20.57.170.57, Ethernet45
 C        20.170.171.0/24
           directly connected, Ethernet1
 C        20.170.254.0/24
           directly connected, Ethernet48
 I L2     20.171.179.0/24 [115/20]
           via 20.170.171.171, Ethernet1
 I L2     20.171.254.0/24 [115/40]
           via 20.170.171.171, Ethernet1
           via 20.57.170.57, Ethernet45
 I L2     192.168.20.0/23 [115/30]
           via 20.170.171.171, Ethernet1
           via 20.57.170.57, Ethernet45
 I L2     192.168.0.0/19 [115/30]
           via 20.170.171.171, Ethernet1
           via 20.57.170.57, Ethernet45
 I L2     200.111.0.0/24 [115/30]
           via 20.170.171.171, Ethernet1
           via 20.57.170.57, Ethernet45


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
MPLS forwarding table (Label [metric] Vias) - 10 routes 
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
                via M, forward
                    EgressACL: apply
                    20.57.170.57 Ethernet45
                    20.170.171.171 Ethernet1
 20057   A[1]
                via M, ::, forward
                    EgressACL: apply
                  via TI-LFA tunnel index 7
                    via 20.57.170.57, Ethernet45, label imp-null(3)
                    backup via 20.170.171.171, Ethernet1, label 20349
 20083   A[1]
                via M, forward
                    EgressACL: apply
                    20.57.170.57 Ethernet45
                    20.170.171.171 Ethernet1
 20171   A[1]
                via M, ::, pop
                    EgressACL: apply
                  via TI-LFA tunnel index 0
                    via 20.170.171.171, Ethernet1, label imp-null(3)
                    backup via 20.57.170.57, Ethernet45, label 20355 20171
 20254   A[1]
                via M, forward
                    EgressACL: apply
                    20.57.170.57 Ethernet45
                    20.170.171.171 Ethernet1
 20349   A[1]
                via M, forward
                    EgressACL: apply
                    20.57.170.57 Ethernet45
                    20.170.171.171 Ethernet1
 20355   A[1]
                via M, forward
                    EgressACL: apply
                    20.57.170.57 Ethernet45
                    20.170.171.171 Ethernet1
 20379   A[1]
                via M, forward
                    EgressACL: apply
                    20.57.170.57 Ethernet45
                    20.170.171.171 Ethernet1
 362144  A[1]
                via M, 20.170.171.171, pop
                    EgressACL: apply
                    directly connected, Ethernet1
                    2c:dd:e9:96:1a:b3, vlan 1006
 362145  A[1]
                via M, 20.57.170.57, pop
                    EgressACL: apply
                    directly connected, Ethernet45
                    c0:14:b8:21:ca:74, vlan 1008
```

## show mpls lfib route

```text
MPLS forwarding table (Label [metric] Vias) - 10 routes 
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
                via M, 20.57.170.57, forward
                 payload autoDecide, ttlMode uniform, dscpMode uniform, apply egress-acl
                 interface Ethernet45
                via M, 20.170.171.171, forward
                 payload autoDecide, ttlMode uniform, dscpMode uniform, apply egress-acl
                 interface Ethernet1
 IP    20057    [1], 10.0.0.57/32
                via TI-LFA tunnel index 7, forward
                 payload autoDecide, ttlMode uniform, dscpMode uniform, apply egress-acl
                    via 20.57.170.57, Ethernet45, label imp-null(3)
                    backup via 20.170.171.171, Ethernet1, label 20349
 IP    20083    [1], 10.0.0.83/32
                via M, 20.57.170.57, forward
                 payload autoDecide, ttlMode uniform, dscpMode uniform, apply egress-acl
                 interface Ethernet45
                via M, 20.170.171.171, forward
                 payload autoDecide, ttlMode uniform, dscpMode uniform, apply egress-acl
                 interface Ethernet1
 IP    20171    [1], 10.0.0.171/32
                via TI-LFA tunnel index 0, pop
                 payload autoDecide, ttlMode uniform, dscpMode uniform, apply egress-acl
                    via 20.170.171.171, Ethernet1, label imp-null(3)
                    backup via 20.57.170.57, Ethernet45, label 20355 20171
 IP    20254    [1], 10.0.0.254/32
                via M, 20.57.170.57, forward
                 payload autoDecide, ttlMode uniform, dscpMode uniform, apply egress-acl
                 interface Ethernet45
                via M, 20.170.171.171, forward
                 payload autoDecide, ttlMode uniform, dscpMode uniform, apply egress-acl
                 interface Ethernet1
 IP    20349    [1], 10.0.1.49/32
                via M, 20.57.170.57, forward
                 payload autoDecide, ttlMode uniform, dscpMode uniform, apply egress-acl
                 interface Ethernet45
                via M, 20.170.171.171, forward
                 payload autoDecide, ttlMode uniform, dscpMode uniform, apply egress-acl
                 interface Ethernet1
 IP    20355    [1], 10.0.1.55/32
                via M, 20.57.170.57, forward
                 payload autoDecide, ttlMode uniform, dscpMode uniform, apply egress-acl
                 interface Ethernet45
                via M, 20.170.171.171, forward
                 payload autoDecide, ttlMode uniform, dscpMode uniform, apply egress-acl
                 interface Ethernet1
 IP    20379    [1], 10.0.0.179/32
                via M, 20.57.170.57, forward
                 payload autoDecide, ttlMode uniform, dscpMode uniform, apply egress-acl
                 interface Ethernet45
                via M, 20.170.171.171, forward
                 payload autoDecide, ttlMode uniform, dscpMode uniform, apply egress-acl
                 interface Ethernet1
 IA    362144   [1]
                via M, 20.170.171.171, pop
                 payload autoDecide, ttlMode uniform, apply egress-acl
                 interface Ethernet1
 IA    362145   [1]
                via M, 20.57.170.57, pop
                 payload autoDecide, ttlMode uniform, apply egress-acl
                 interface Ethernet45
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
Endpoint        Tunnel Type     Index(es)   Tunnel Preference   IGP Preference 
-------------- --------------- ----------- ------------------- ----------------
10.0.0.19/32    IS-IS SR IPv4   12          65                  115            
10.0.0.57/32    IS-IS SR IPv4   11          65                  115            
10.0.0.83/32    IS-IS SR IPv4   17          65                  115            
10.0.0.171/32   IS-IS SR IPv4   6           65                  115            
10.0.0.179/32   IS-IS SR IPv4   9           65                  115            
10.0.0.254/32   IS-IS SR IPv4   2           65                  115            
10.0.1.49/32    IS-IS SR IPv4   7           65                  115            
10.0.1.55/32    IS-IS SR IPv4   8           65                  115            

   IGP Metric    Metric Type
---------------- -----------
   30            metric     
   10            metric     
   30            metric     
   10            metric     
   20            metric     
   30            metric     
   20            metric     
   20            metric     

```

## show tunnel rib colored brief

```text
Tunnel RIB: system-colored-tunnel-rib
 Endpoint     Color     Tunnel Type     Index(es)     Tunnel Preference     IGP Preference     IGP Metric   Metric Type
----------- --------- --------------- ------------- --------------------- ------------------ -------------- -----------

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
>C    10.0.0.170/32 [0 pref/0 metric] updated 1d01h ago
         via Loopback0, directly connected
>C    20.32.170.0/24 [0 pref/0 metric] updated 00:42:15 ago
         via Ethernet43, directly connected
>C    20.47.170.0/24 [0 pref/0 metric] updated 06:59:01 ago
         via Ethernet3, directly connected
>C    20.57.170.0/24 [0 pref/0 metric] updated 07:20:03 ago
         via Ethernet45, directly connected
>C    20.170.171.0/24 [0 pref/0 metric] updated 04:37:58 ago
         via Ethernet1, directly connected
>C    20.170.254.0/24 [0 pref/0 metric] updated 1d01h ago
         via Ethernet48, directly connected
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
>P    0.0.0.0/8 [1 pref/0 metric] updated 1d05h ago
         via Null0, directly connected [NF]
>P    127.0.0.0/8 [1 pref/0 metric] updated 1d05h ago
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
>I    10.0.0.5/32 [115 pref/40 metric] updated 00:10:26 ago
         via 20.57.170.57, Ethernet45
         via 20.170.171.171, Ethernet1
>I    10.0.0.19/32 [115 pref/30 metric] updated 00:10:26 ago
         via 20.57.170.57, Ethernet45
         via 20.170.171.171, Ethernet1
>I    10.0.0.24/32 [115 pref/30 metric] updated 00:10:26 ago
         via 20.57.170.57, Ethernet45
         via 20.170.171.171, Ethernet1
>I    10.0.0.57/32 [115 pref/10 metric] updated 02:09:42 ago
         via 20.57.170.57, Ethernet45
>I    10.0.0.83/32 [115 pref/30 metric] updated 00:10:26 ago
         via 20.57.170.57, Ethernet45
         via 20.170.171.171, Ethernet1
>I    10.0.0.171/32 [115 pref/10 metric] updated 01:57:36 ago
         via 20.170.171.171, Ethernet1
>I    10.0.0.179/32 [115 pref/20 metric] updated 00:30:00 ago
         via 20.57.170.57, Ethernet45
         via 20.170.171.171, Ethernet1
>I    10.0.0.254/32 [115 pref/30 metric] updated 00:10:26 ago
         via 20.57.170.57, Ethernet45
         via 20.170.171.171, Ethernet1
>I    10.0.1.49/32 [115 pref/20 metric] updated 00:10:26 ago
         via 20.57.170.57, Ethernet45
         via 20.170.171.171, Ethernet1
>I    10.0.1.55/32 [115 pref/20 metric] updated 02:09:27 ago
         via 20.57.170.57, Ethernet45
         via 20.170.171.171, Ethernet1
>I    20.5.149.0/24 [115 pref/30 metric] updated 00:10:26 ago
         via 20.57.170.57, Ethernet45
         via 20.170.171.171, Ethernet1
>I    20.19.149.0/24 [115 pref/30 metric] updated 00:10:26 ago
         via 20.57.170.57, Ethernet45
         via 20.170.171.171, Ethernet1
>I    20.19.211.0/24 [115 pref/30 metric] updated 00:10:26 ago
         via 20.57.170.57, Ethernet45
         via 20.170.171.171, Ethernet1
>I    20.24.149.0/24 [115 pref/30 metric] updated 00:10:26 ago
         via 20.57.170.57, Ethernet45
         via 20.170.171.171, Ethernet1
>I    20.24.211.0/24 [115 pref/40 metric] updated 00:10:26 ago
         via 20.57.170.57, Ethernet45
         via 20.170.171.171, Ethernet1
>I    20.32.149.0/24 [115 pref/30 metric] updated 00:10:26 ago
         via 20.57.170.57, Ethernet45
         via 20.170.171.171, Ethernet1
>I    20.47.149.0/24 [115 pref/30 metric] updated 00:10:26 ago
         via 20.57.170.57, Ethernet45
         via 20.170.171.171, Ethernet1
>I    20.57.59.0/24 [115 pref/20 metric] updated 02:09:42 ago
         via 20.57.170.57, Ethernet45
>I    20.57.149.0/24 [115 pref/20 metric] updated 02:09:42 ago
         via 20.57.170.57, Ethernet45
>I    20.57.155.0/24 [115 pref/20 metric] updated 02:09:42 ago
         via 20.57.170.57, Ethernet45
>I    20.57.179.0/24 [115 pref/20 metric] updated 02:09:42 ago
         via 20.57.170.57, Ethernet45
>I    20.57.211.0/24 [115 pref/20 metric] updated 02:09:08 ago
         via 20.57.170.57, Ethernet45
>I    20.83.149.0/24 [115 pref/30 metric] updated 00:10:26 ago
         via 20.57.170.57, Ethernet45
         via 20.170.171.171, Ethernet1
>I    20.111.149.0/24 [115 pref/30 metric] updated 00:10:26 ago
         via 20.57.170.57, Ethernet45
         via 20.170.171.171, Ethernet1
>I    20.149.155.0/24 [115 pref/30 metric] updated 00:10:26 ago
         via 20.57.170.57, Ethernet45
         via 20.170.171.171, Ethernet1
>I    20.149.171.0/24 [115 pref/20 metric] updated 04:37:50 ago
         via 20.170.171.171, Ethernet1
>I    20.149.254.0/24 [115 pref/30 metric] updated 00:10:26 ago
         via 20.57.170.57, Ethernet45
         via 20.170.171.171, Ethernet1
>I    20.155.171.0/24 [115 pref/20 metric] updated 02:36:06 ago
         via 20.170.171.171, Ethernet1
>I    20.155.179.0/24 [115 pref/30 metric] updated 02:09:42 ago
         via 20.57.170.57, Ethernet45
         via 20.170.171.171, Ethernet1
>I    20.171.179.0/24 [115 pref/20 metric] updated 00:35:32 ago
         via 20.170.171.171, Ethernet1
>I    20.171.254.0/24 [115 pref/40 metric] updated 00:10:26 ago
         via 20.57.170.57, Ethernet45
         via 20.170.171.171, Ethernet1
>I    192.168.0.0/19 [115 pref/30 metric] updated 00:10:26 ago
         via 20.57.170.57, Ethernet45
         via 20.170.171.171, Ethernet1
>I    192.168.20.0/23 [115 pref/30 metric] updated 00:10:26 ago
         via 20.57.170.57, Ethernet45
         via 20.170.171.171, Ethernet1
>I    200.111.0.0/24 [115 pref/30 metric] updated 00:04:24 ago
         via 20.57.170.57, Ethernet45
         via 20.170.171.171, Ethernet1
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
>P    ::/96 [1 pref/0 metric] updated 1d05h ago
         via Null0, directly connected [NF]
>P    ::ffff:127.0.0.0/104 [1 pref/0 metric] updated 1d05h ago
         via :: [1 pref/1 metric] type ipv6
            via , directly connected
>P    fe80::/10 [1 pref/0 metric] updated 1d05h ago
```

## show platform sand l3 summary

```text
Number of vrfs: 2

Ipv4:
  Routes:       69  backlog:  0  unprogrammed:  0
  Adjacencies:  39  backlog:  0  unprogrammed:  0
Ipv6:
  Routes:       4   backlog:  0  unprogrammed:  0
  Adjacencies:  39  backlog:  0  unprogrammed:  0
Mpls:
  Routes:       10  backlog:  0  unprogrammed:  0
  Adjacencies:  2   backlog:  0  unprogrammed:  0

Jericho Ip Fecs:
  Non-ecmp fecs:  4109  ecmp fecs:  1  fec entries:  4111
Jericho Mpls Fecs:
  Non-ecmp fecs:  2  ecmp fecs:  0  fec entries:  2
Jericho Vxlan Overlay Fecs:
  Non-ecmp fecs:  0  ecmp fecs:  0  fec entries:  0
Jericho Vxlan Tunnel Fecs:
  Non-ecmp fecs:  0  ecmp fecs:  0  fec entries:  0
  Number of vxlan tunnels configured: 0

Jericho Lpm Routes:
  Routes:   65  unprogrammed:   0   
  Routes6:  4   unprogrammed6:  0   
  Backlog:  0 

Jericho Lpm:
  TCAM pivots used:  3   Percent free:  99
  Buckets used:      12  Rows used:     2   Entries Per Bucket:  5     Percent free:  99  

Lem:
  IPv4  Host in Lem:            enabled
  IPv4  Hosts:                  4      
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
  MPLS (for inner 2 labels) Egress Banks in use:  None
  SVI egress counters Egress Banks in use:        None
  

Egress Arp rewrite entries in use (in each fap):
  FixedSystem: 12
Egress Arp remote rewrite entries in use (in each fap):
  FixedSystem: 0
Egress Ip tunnel rewrite entries in use (in each fap):
  FixedSystem: 0
Egress Mpls (for outer 2 labels) rewrite entries in use (in each fap):
  FixedSystem: 0
Egress Mpls (for inner 2 labels) rewrite entries in use (in each fap):
  FixedSystem: 0
Egress Sflow rewrite entries in use (in each fap):
  FixedSystem: 0

Egress rewrite chains in backlog: resource-full 0, no-interface 0

Glem is disabled

Route Update State:
  v4 route update suspended:  False
  v6 route update suspended:  False

Jericho Fec:
  Maximum FEC hierarchy levels:  2
  Used:                     15  ecmp:                 2   reusedEcmp:  13    allocs:  215   frees:  201   shuffles:  0     cmds:  0   
  Non-ecmp (Percent free):  99  ecmp (Percent free):  99
  Zombies:     0    purges:    0
  Quarantine:  0/2  shuffles:  0  deletes:  2   
  Fec insertion failures:  0
  Banks in use (level, used, Percent free):
     2 (2, 15, 99%)

Lpm Detail:
  Requests:  1068  cleanses:  332  batches:  332  avg batch size:  3

Lem Cmds:
  Adds:  134  dels:  120  mods:  268  fails:  0  cmds:  522

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
  ArpTable writes:      629    queued      0   
  IngressTable writes:  10380  queued      0   
  Coprocessors:         1      in CmdRing

TopBank To EedbBank Mapping:
None

Tunnel Counter Status
  Number of MPLS tunnels:                  0    
  Number of uncountable MPLS tunnels:      0    
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

