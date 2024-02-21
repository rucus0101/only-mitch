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

Uptime: 1 day, 4 hours and 33 minutes
Total memory: 8051592 kB
Free memory: 5916384 kB

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
IGP       default  Ribbon-32        L2   Ethernet43         P2P               UP    69          00                  
IGP       default  SR1-SRMPLS       L2   Ethernet45         P2P               UP    25          00                  
IGP       default  PE31-J2-171      L2   Ethernet1          P2P               UP    24          50                  
```

## show isis database detail

```text
Legend:
H - hostname conflict
U - node unreachable

IS-IS Instance: IGP VRF: default
  IS-IS Level 2 Link State Database
    LSPID                   Seq Num  Cksum  Life Length IS  Received LSPID        Flags
    0000.0000.0019.00-00        280  57388   727    134 L2  0000.0000.0019.00-00  <>
      NLPID: 0xCC(IPv4)
      Area addresses: 49
      Interface address: 10.0.0.19
      Interface address: 20.19.149.19
      IS Neighbor          : h49-N540-24Q8L2DD.00 Metric: 10
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
    eantc-jcnr2.00-00           449   3652   850    229 L2  0000.0000.0020.00-00  <>
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
    Ribbon-32.00-00              13  25915   543    109 L2  0000.0000.0032.00-00  <>
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
    Ribbon-32.00-01              10  35760   438     38 L2  0000.0000.0032.00-01  <>
      Hostname: Ribbon-32
    Ribbon-32.00-02             300  19799  1183    397 L2  0000.0000.0032.00-02  <>
      Interface address: 20.32.149.32
      Interface address: 20.32.170.32
      Interface address: 20.32.211.32
      Interface address: 10.0.0.32
      IS Neighbor          : h49-N540-24Q8L2DD.00 Metric: 10
        IPv4 Neighbor Address: 20.32.149.149
        IPv4 Interface Address: 20.32.149.32
        Adj-sid: 756640 flags: [L V] weight: 0x0
        Adj-sid: 756643 flags: [L V B] weight: 0x0
      IS Neighbor          : Spine3-J-170.00     Metric: 10
        IPv4 Neighbor Address: 20.32.170.170
        IPv4 Interface Address: 20.32.170.32
        Adj-sid: 756644 flags: [L V] weight: 0x0
        Adj-sid: 756646 flags: [L V B] weight: 0x0
      Reachability         : 20.32.149.0/24 Metric: 10 Type: 1 Up
      Reachability         : 20.32.170.0/24 Metric: 10 Type: 1 Up
      Reachability         : 20.32.211.0/24 Metric: 10 Type: 1 Up
      Reachability         : 10.0.0.32/32 Metric: 0 Type: 1 Up
        SR Prefix-SID: 32 Flags: [N] Algorithm: 0
        SR Prefix-SID: 1032 Flags: [N] Algorithm: 128
        SR Prefix-SID: 1132 Flags: [N] Algorithm: 129
        SR Prefix-SID: 1232 Flags: [N] Algorithm: 130
    huawei_34_NetEngine_8000_F8.00-00       116  10313   911    293 L2  0000.0000.0254.00-00  <>
      Remaining lifetime received: 1199 s Modified to: 1200 s
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
        Maximum SID depth:
          Base MPLS imposition (MSD type 1):  10
        SR Capability: Flags: [I]
          SRGB Base: 20000 Range: 2000
        Algorithms:  0, 128, 129, 130, 131
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
    h49-N540-24Q8L2DD.00-00       226  44755   495   1055 L2  0000.0000.0349.00-00  <>
      NLPID: 0xCC(IPv4)
      Hostname: h49-N540-24Q8L2DD
      Area addresses: 49
      Interface address: 10.0.1.49
      IS Neighbor          : 0000.0000.0019.00   Metric: 10
        IPv4 Neighbor Address: 20.19.149.19
        IPv4 Interface Address: 20.19.149.149
        Adj-sid: 24005 flags: [L V] weight: 0x0
      IS Neighbor          : PE31-J2-171.00      Metric: 10
        IPv4 Neighbor Address: 20.149.171.171
        IPv4 Interface Address: 20.149.171.149
        Adj-sid: 24011 flags: [L V] weight: 0x0
      IS Neighbor          : Ribbon-32.00        Metric: 10
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
      IS Neighbor          : SR1-SRMPLS.00       Metric: 10
        IPv4 Neighbor Address: 20.57.149.57
        IPv4 Interface Address: 20.57.149.149
        Adj-sid: 24009 flags: [L V] weight: 0x0
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
      Reachability         : 20.5.149.0/24 Metric: 10 Type: 1 Up
      Reachability         : 20.19.149.0/24 Metric: 10 Type: 1 Up
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
        Algorithms:  0, 1, 128, 129, 130, 131
        Flex Algo: Algorithm: 128 Metric: Min Unidirectional Delay Metric (1) Calc: SPF (0) Prio: 255
        Flex Algo: Algorithm: 129 Metric: TE Metric (2) Calc: SPF (0) Prio: 255
        Flex Algo: Algorithm: 130 Metric: IGP Metric (0) Calc: SPF (0) Prio: 255
          Exclude admin groups: 1
        Flex Algo: Algorithm: 131 Metric: IGP Metric (0) Calc: SPF (0) Prio: 255
          Exclude admin groups: 129
      Unsupported TLV: Type: 14 Length: 2
    h55-8201-24H8FH.00-00       154  30463   816    625 L2  0000.0000.0355.00-00  <>
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
        Algorithms:  0, 1, 128, 129, 130, 131
        Flex Algo: Algorithm: 128 Metric: Min Unidirectional Delay Metric (1) Calc: SPF (0) Prio: 10
        Flex Algo: Algorithm: 129 Metric: TE Metric (2) Calc: SPF (0) Prio: 10
        Flex Algo: Algorithm: 130 Metric: IGP Metric (0) Calc: SPF (0) Prio: 10
          Exclude admin groups: 1
        Flex Algo: Algorithm: 131 Metric: IGP Metric (0) Calc: SPF (0) Prio: 10
          Exclude admin groups: 127
      Unsupported TLV: Type: 14 Length: 2
    juniper_379_MX304.00-00        45  60006  1174    344 L2  0000.0001.7900.00-00  <>
      Remaining lifetime received: 1198 s Modified to: 1200 s
      NLPID: 0xCC(IPv4) 0x8E(IPv6)
      Hostname: juniper_379_MX304
      Area addresses: 49.0001.00
      Interface address: 10.0.0.179
      IS Neighbor          : h55-8201-24H8FH.00  Metric: 10
        IPv4 Neighbor Address: 20.155.179.155
        IPv4 Interface Address: 20.155.179.179
        Adj-sid: 18 flags: [L V] weight: 0x0
      IS Neighbor          : SR1-SRMPLS.00       Metric: 10
        IPv4 Neighbor Address: 20.57.179.57
        IPv4 Interface Address: 20.57.179.179
        Adj-sid: 17 flags: [L V] weight: 0x0
      Reachability         : 20.155.179.0/24 Metric: 10 Type: 1 Up
      Reachability         : 20.57.179.0/24 Metric: 10 Type: 1 Up
      Reachability         : 10.0.0.179/32 Metric: 0 Type: 1 Up
        SR Prefix-SID: 379 Flags: [N] Algorithm: 0
        SR Prefix-SID: 1379 Flags: [N] Algorithm: 130
        SR Prefix-SID: 1279 Flags: [N] Algorithm: 129
        SR Prefix-SID: 1179 Flags: [N] Algorithm: 128
      Router Capabilities: Router Id: 10.0.0.179 Flags: []
        Maximum SID depth:
          Base MPLS imposition (MSD type 1):  4
        SR Capability: Flags: [I V]
          SRGB Base: 20000 Range: 2000
        Algorithms:  0, 1, 128, 129, 130
      Unsupported TLV: Type: 14 Length: 2
    0010.0010.0005.00-00         19  32587   945    280 L2  0010.0010.0005.00-00  <>
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
    SR1-SRMPLS.00-00            399  34137  1183    798 L2  0100.0000.0057.00-00  <>
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
    Spine3-J-170.00-00          158  14636   848    265 L2  0100.0000.0170.00-00  <>
      LSP generation remaining wait time: 0 ms
      Time remaining until refresh: 548 s
      NLPID: 0xCC(IPv4)
      Hostname: Spine3-J-170
      Area addresses: 49.0000
      Interface address: 20.170.171.170
      Interface address: 20.47.170.170
      Interface address: 20.57.170.170
      Interface address: 20.32.170.170
      Interface address: 20.170.254.170
      Interface address: 10.0.0.170
      IS Neighbor          : SR1-SRMPLS.00       Metric: 10
        IPv4 Neighbor Address: 20.57.170.57
        IPv4 Interface Address: 20.57.170.170
        Adj-sid: 362145 flags: [L V] weight: 0x0
      IS Neighbor          : Ribbon-32.00        Metric: 10
        IPv4 Neighbor Address: 20.32.170.32
        IPv4 Interface Address: 20.32.170.170
        Adj-sid: 362147 flags: [L V] weight: 0x0
      IS Neighbor          : PE31-J2-171.00      Metric: 10
        IPv4 Neighbor Address: 20.170.171.171
        IPv4 Interface Address: 20.170.171.170
        Adj-sid: 362144 flags: [L V] weight: 0x0
      Reachability         : 20.170.171.0/24 Metric: 10 Type: 1 Up
      Reachability         : 20.47.170.0/24 Metric: 10 Type: 1 Up
      Reachability         : 20.57.170.0/24 Metric: 10 Type: 1 Up
      Reachability         : 20.32.170.0/24 Metric: 10 Type: 1 Up
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
    PE31-J2-171.00-00           164   9901   589    385 L2  0100.0000.0171.00-00  <>
      Remaining lifetime received: 1199 s Modified to: 1200 s
      NLPID: 0xCC(IPv4)
      Hostname: PE31-J2-171
      Area addresses: 49.0000
      Interface address: 20.155.171.171
      Interface address: 20.170.171.171
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
      IS Neighbor          : Spine3-J-170.00     Metric: 10
        IPv4 Neighbor Address: 20.170.171.170
        IPv4 Interface Address: 20.170.171.171
        Adj-sid: 362145 flags: [L V] weight: 0x0
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
  2         10.0.0.254/32     20.32.170.32              Ethernet43    [ 20254 ]
                              20.57.170.57              Ethernet45    [ 20254 ]
                              20.170.171.171            Ethernet1     [ 20254 ]
  6         10.0.0.171/32     TI-LFA (6)                -             [ 3 ]    
  7         10.0.1.49/32      20.32.170.32              Ethernet43    [ 20349 ]
                              20.57.170.57              Ethernet45    [ 20349 ]
                              20.170.171.171            Ethernet1     [ 20349 ]
  8         10.0.1.55/32      20.57.170.57              Ethernet45    [ 20355 ]
                              20.170.171.171            Ethernet1     [ 20355 ]
  9         10.0.0.179/32     TI-LFA (1)                -             [ 20379 ]
  11        10.0.0.57/32      TI-LFA (7)                -             [ 20057 ]
  12        10.0.0.19/32      20.32.170.32              Ethernet43    [ 20019 ]
                              20.57.170.57              Ethernet45    [ 20019 ]
                              20.170.171.171            Ethernet1     [ 20019 ]
  15        10.0.0.32/32      TI-LFA (2)                -             [ 3 ]    
  17        10.0.0.83/32      20.32.170.32              Ethernet43    [ 20083 ]
                              20.57.170.57              Ethernet45    [ 20083 ]
                              20.170.171.171            Ethernet1     [ 20083 ]

```

## show isis segment-routing prefix-segments

```text

System ID: Spine3-J-170			Instance: 'IGP'
SR supported Data-plane: MPLS			SR Router ID: 100.0.0.170

Node: 36     Proxy-Node: 0      Prefix: 0       Total Segments: 36

Flag Descriptions: R: Re-advertised, N: Node Segment, P: no-PHP
                   E: Explicit-NULL, V: Value, L: Local
Segment status codes: * - Self originated Prefix, L1 - level 1, L2 - level 2, ! - SR-unreachable,
                      # - Some IS-IS next-hops are SR-unreachable
   Prefix                      SID Type       Flags                        System ID       Level Protection  Algorithm   
   ------------------------- ----- ---------- ---------------------------- --------------- ----- ----------- -------------
   10.0.0.19/32                 19 Node       R:0 N:1 P:0 E:0 V:0 L:0      0000.0000.0019  L2    unprotected SPF         
   10.0.0.32/32                 32 Node       R:0 N:1 P:0 E:0 V:0 L:0      Ribbon-32       L2    node        SPF         
   10.0.0.32/32               1032 Node       R:0 N:1 P:0 E:0 V:0 L:0      Ribbon-32       L2    unprotected 128         
   10.0.0.32/32               1132 Node       R:0 N:1 P:0 E:0 V:0 L:0      Ribbon-32       L2    unprotected 129         
   10.0.0.32/32               1232 Node       R:0 N:1 P:0 E:0 V:0 L:0      Ribbon-32       L2    unprotected 130         
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
   10.0.0.179/32               379 Node       R:0 N:1 P:0 E:0 V:0 L:0      juniper_379_MX304 L2    node        SPF         
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
   10.0.1.55/32                355 Node       R:0 N:1 P:0 E:0 V:0 L:0      h55-8201-24H8FH L2    unprotected SPF         
   10.0.1.55/32               1355 Node       R:0 N:1 P:0 E:0 V:0 L:0      h55-8201-24H8FH L2    unprotected 128         
   10.0.1.55/32               1455 Node       R:0 N:1 P:0 E:0 V:0 L:0      h55-8201-24H8FH L2    unprotected 129         
   10.0.1.55/32               1555 Node       R:0 N:1 P:0 E:0 V:0 L:0      h55-8201-24H8FH L2    unprotected 130         
   10.0.1.55/32               1655 Node       R:0 N:1 P:0 E:0 V:0 L:0      h55-8201-24H8FH L2    unprotected 131         
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
           via 20.32.170.32, Ethernet43
           via 20.57.170.57, Ethernet45
 I L2     10.0.0.19/32 [115/30]
           via 20.170.171.171, Ethernet1
           via 20.32.170.32, Ethernet43
           via 20.57.170.57, Ethernet45
 I L2     10.0.0.32/32 [115/10]
           via 20.32.170.32, Ethernet43
 I L2     10.0.0.57/32 [115/10]
           via 20.57.170.57, Ethernet45
 I L2     10.0.0.83/32 [115/30]
           via 20.170.171.171, Ethernet1
           via 20.32.170.32, Ethernet43
           via 20.57.170.57, Ethernet45
 C        10.0.0.170/32
           directly connected, Loopback0
 I L2     10.0.0.171/32 [115/10]
           via 20.170.171.171, Ethernet1
 I L2     10.0.0.179/32 [115/20]
           via 20.57.170.57, Ethernet45
 I L2     10.0.0.254/32 [115/30]
           via 20.170.171.171, Ethernet1
           via 20.32.170.32, Ethernet43
           via 20.57.170.57, Ethernet45
 I L2     10.0.1.49/32 [115/20]
           via 20.170.171.171, Ethernet1
           via 20.32.170.32, Ethernet43
           via 20.57.170.57, Ethernet45
 I L2     10.0.1.55/32 [115/20]
           via 20.170.171.171, Ethernet1
           via 20.57.170.57, Ethernet45
 I L2     20.5.149.0/24 [115/30]
           via 20.170.171.171, Ethernet1
           via 20.32.170.32, Ethernet43
           via 20.57.170.57, Ethernet45
 I L2     20.19.149.0/24 [115/30]
           via 20.170.171.171, Ethernet1
           via 20.32.170.32, Ethernet43
           via 20.57.170.57, Ethernet45
 I L2     20.19.211.0/24 [115/30]
           via 20.170.171.171, Ethernet1
           via 20.32.170.32, Ethernet43
           via 20.57.170.57, Ethernet45
 I L2     20.32.149.0/24 [115/20]
           via 20.32.170.32, Ethernet43
 C        20.32.170.0/24
           directly connected, Ethernet43
 I L2     20.32.211.0/24 [115/20]
           via 20.32.170.32, Ethernet43
 I L2     20.47.149.0/24 [115/30]
           via 20.170.171.171, Ethernet1
           via 20.32.170.32, Ethernet43
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
           via 20.32.170.32, Ethernet43
           via 20.57.170.57, Ethernet45
 I L2     20.111.149.0/24 [115/30]
           via 20.170.171.171, Ethernet1
           via 20.32.170.32, Ethernet43
           via 20.57.170.57, Ethernet45
 I L2     20.149.155.0/24 [115/30]
           via 20.170.171.171, Ethernet1
           via 20.32.170.32, Ethernet43
           via 20.57.170.57, Ethernet45
 I L2     20.149.171.0/24 [115/20]
           via 20.170.171.171, Ethernet1
 I L2     20.149.254.0/24 [115/30]
           via 20.170.171.171, Ethernet1
           via 20.32.170.32, Ethernet43
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
 I L2     20.171.254.0/24 [115/40]
           via 20.170.171.171, Ethernet1
           via 20.32.170.32, Ethernet43
           via 20.57.170.57, Ethernet45
 I L2     192.168.0.0/19 [115/30]
           via 20.170.171.171, Ethernet1
           via 20.32.170.32, Ethernet43
           via 20.57.170.57, Ethernet45

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
MPLS forwarding table (Label [metric] Vias) - 12 routes 
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
                    20.32.170.32 Ethernet43
                    20.57.170.57 Ethernet45
                    20.170.171.171 Ethernet1
 20032   A[1]
                via M, ::, pop
                    EgressACL: apply
                  via TI-LFA tunnel index 2
                    via 20.32.170.32, Ethernet43, label imp-null(3)
                    backup via 20.170.171.171, Ethernet1, label 20349 20032
 20057   A[1]
                via M, ::, forward
                    EgressACL: apply
                  via TI-LFA tunnel index 7
                    via 20.57.170.57, Ethernet45, label imp-null(3)
                    backup via 20.170.171.171, Ethernet1, label 20349
 20083   A[1]
                via M, forward
                    EgressACL: apply
                    20.32.170.32 Ethernet43
                    20.57.170.57 Ethernet45
                    20.170.171.171 Ethernet1
 20171   A[1]
                via M, ::, pop
                    EgressACL: apply
                  via TI-LFA tunnel index 6
                    via 20.170.171.171, Ethernet1, label imp-null(3)
                    backup via 20.32.170.32, Ethernet43, label 20349 20171
 20254   A[1]
                via M, forward
                    EgressACL: apply
                    20.32.170.32 Ethernet43
                    20.57.170.57 Ethernet45
                    20.170.171.171 Ethernet1
 20349   A[1]
                via M, forward
                    EgressACL: apply
                    20.32.170.32 Ethernet43
                    20.57.170.57 Ethernet45
                    20.170.171.171 Ethernet1
 20355   A[1]
                via M, forward
                    EgressACL: apply
                    20.57.170.57 Ethernet45
                    20.170.171.171 Ethernet1
 20379   A[1]
                via M, ::, forward
                    EgressACL: apply
                  via TI-LFA tunnel index 1
                    via 20.57.170.57, Ethernet45, label imp-null(3)
                    backup via 20.170.171.171, Ethernet1, label imp-null(3)
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
 362147  A[1]
                via M, 20.32.170.32, pop
                    EgressACL: apply
                    directly connected, Ethernet43
                    30:c5:07:1f:33:0c, vlan 1010
```

## show mpls lfib route

```text
MPLS forwarding table (Label [metric] Vias) - 12 routes 
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
                via M, 20.32.170.32, forward
                 payload autoDecide, ttlMode uniform, dscpMode uniform, apply egress-acl
                 interface Ethernet43
                via M, 20.57.170.57, forward
                 payload autoDecide, ttlMode uniform, dscpMode uniform, apply egress-acl
                 interface Ethernet45
                via M, 20.170.171.171, forward
                 payload autoDecide, ttlMode uniform, dscpMode uniform, apply egress-acl
                 interface Ethernet1
 IP    20032    [1], 10.0.0.32/32
                via TI-LFA tunnel index 2, pop
                 payload autoDecide, ttlMode uniform, dscpMode uniform, apply egress-acl
                    via 20.32.170.32, Ethernet43, label imp-null(3)
                    backup via 20.170.171.171, Ethernet1, label 20349 20032
 IP    20057    [1], 10.0.0.57/32
                via TI-LFA tunnel index 7, forward
                 payload autoDecide, ttlMode uniform, dscpMode uniform, apply egress-acl
                    via 20.57.170.57, Ethernet45, label imp-null(3)
                    backup via 20.170.171.171, Ethernet1, label 20349
 IP    20083    [1], 10.0.0.83/32
                via M, 20.32.170.32, forward
                 payload autoDecide, ttlMode uniform, dscpMode uniform, apply egress-acl
                 interface Ethernet43
                via M, 20.57.170.57, forward
                 payload autoDecide, ttlMode uniform, dscpMode uniform, apply egress-acl
                 interface Ethernet45
                via M, 20.170.171.171, forward
                 payload autoDecide, ttlMode uniform, dscpMode uniform, apply egress-acl
                 interface Ethernet1
 IP    20171    [1], 10.0.0.171/32
                via TI-LFA tunnel index 6, pop
                 payload autoDecide, ttlMode uniform, dscpMode uniform, apply egress-acl
                    via 20.170.171.171, Ethernet1, label imp-null(3)
                    backup via 20.32.170.32, Ethernet43, label 20349 20171
 IP    20254    [1], 10.0.0.254/32
                via M, 20.32.170.32, forward
                 payload autoDecide, ttlMode uniform, dscpMode uniform, apply egress-acl
                 interface Ethernet43
                via M, 20.57.170.57, forward
                 payload autoDecide, ttlMode uniform, dscpMode uniform, apply egress-acl
                 interface Ethernet45
                via M, 20.170.171.171, forward
                 payload autoDecide, ttlMode uniform, dscpMode uniform, apply egress-acl
                 interface Ethernet1
 IP    20349    [1], 10.0.1.49/32
                via M, 20.32.170.32, forward
                 payload autoDecide, ttlMode uniform, dscpMode uniform, apply egress-acl
                 interface Ethernet43
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
                via TI-LFA tunnel index 1, forward
                 payload autoDecide, ttlMode uniform, dscpMode uniform, apply egress-acl
                    via 20.57.170.57, Ethernet45, label imp-null(3)
                    backup via 20.170.171.171, Ethernet1, label imp-null(3)
 IA    362144   [1]
                via M, 20.170.171.171, pop
                 payload autoDecide, ttlMode uniform, apply egress-acl
                 interface Ethernet1
 IA    362145   [1]
                via M, 20.57.170.57, pop
                 payload autoDecide, ttlMode uniform, apply egress-acl
                 interface Ethernet45
 IA    362147   [1]
                via M, 20.32.170.32, pop
                 payload autoDecide, ttlMode uniform, apply egress-acl
                 interface Ethernet43
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
10.0.0.32/32    IS-IS SR IPv4   15          65                  115            
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
>C    10.0.0.170/32 [0 pref/0 metric] updated 1d00h ago
         via Loopback0, directly connected
>C    20.32.170.0/24 [0 pref/0 metric] updated 06:17:37 ago
         via Ethernet43, directly connected
>C    20.47.170.0/24 [0 pref/0 metric] updated 05:55:15 ago
         via Ethernet3, directly connected
>C    20.57.170.0/24 [0 pref/0 metric] updated 06:16:17 ago
         via Ethernet45, directly connected
>C    20.170.171.0/24 [0 pref/0 metric] updated 03:34:12 ago
         via Ethernet1, directly connected
>C    20.170.254.0/24 [0 pref/0 metric] updated 1d00h ago
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
>P    0.0.0.0/8 [1 pref/0 metric] updated 1d04h ago
         via Null0, directly connected [NF]
>P    127.0.0.0/8 [1 pref/0 metric] updated 1d04h ago
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
>I    10.0.0.5/32 [115 pref/40 metric] updated 01:05:46 ago
         via 20.32.170.32, Ethernet43
         via 20.57.170.57, Ethernet45
         via 20.170.171.171, Ethernet1
>I    10.0.0.19/32 [115 pref/30 metric] updated 01:05:46 ago
         via 20.32.170.32, Ethernet43
         via 20.57.170.57, Ethernet45
         via 20.170.171.171, Ethernet1
>I    10.0.0.32/32 [115 pref/10 metric] updated 02:09:02 ago
         via 20.32.170.32, Ethernet43
>I    10.0.0.57/32 [115 pref/10 metric] updated 01:05:56 ago
         via 20.57.170.57, Ethernet45
>I    10.0.0.83/32 [115 pref/30 metric] updated 01:05:46 ago
         via 20.32.170.32, Ethernet43
         via 20.57.170.57, Ethernet45
         via 20.170.171.171, Ethernet1
>I    10.0.0.171/32 [115 pref/10 metric] updated 00:53:50 ago
         via 20.170.171.171, Ethernet1
>I    10.0.0.179/32 [115 pref/20 metric] updated 00:47:10 ago
         via 20.57.170.57, Ethernet45
>I    10.0.0.254/32 [115 pref/30 metric] updated 01:05:46 ago
         via 20.32.170.32, Ethernet43
         via 20.57.170.57, Ethernet45
         via 20.170.171.171, Ethernet1
>I    10.0.1.49/32 [115 pref/20 metric] updated 01:05:46 ago
         via 20.32.170.32, Ethernet43
         via 20.57.170.57, Ethernet45
         via 20.170.171.171, Ethernet1
>I    10.0.1.55/32 [115 pref/20 metric] updated 01:05:41 ago
         via 20.57.170.57, Ethernet45
         via 20.170.171.171, Ethernet1
>I    20.5.149.0/24 [115 pref/30 metric] updated 01:05:46 ago
         via 20.32.170.32, Ethernet43
         via 20.57.170.57, Ethernet45
         via 20.170.171.171, Ethernet1
>I    20.19.149.0/24 [115 pref/30 metric] updated 01:05:46 ago
         via 20.32.170.32, Ethernet43
         via 20.57.170.57, Ethernet45
         via 20.170.171.171, Ethernet1
>I    20.19.211.0/24 [115 pref/30 metric] updated 01:05:46 ago
         via 20.32.170.32, Ethernet43
         via 20.57.170.57, Ethernet45
         via 20.170.171.171, Ethernet1
>I    20.32.149.0/24 [115 pref/20 metric] updated 02:09:02 ago
         via 20.32.170.32, Ethernet43
>I    20.32.211.0/24 [115 pref/20 metric] updated 02:09:02 ago
         via 20.32.170.32, Ethernet43
>I    20.47.149.0/24 [115 pref/30 metric] updated 01:05:46 ago
         via 20.32.170.32, Ethernet43
         via 20.57.170.57, Ethernet45
         via 20.170.171.171, Ethernet1
>I    20.57.59.0/24 [115 pref/20 metric] updated 01:05:56 ago
         via 20.57.170.57, Ethernet45
>I    20.57.149.0/24 [115 pref/20 metric] updated 01:05:56 ago
         via 20.57.170.57, Ethernet45
>I    20.57.155.0/24 [115 pref/20 metric] updated 01:05:56 ago
         via 20.57.170.57, Ethernet45
>I    20.57.179.0/24 [115 pref/20 metric] updated 01:05:56 ago
         via 20.57.170.57, Ethernet45
>I    20.57.211.0/24 [115 pref/20 metric] updated 01:05:22 ago
         via 20.57.170.57, Ethernet45
>I    20.83.149.0/24 [115 pref/30 metric] updated 01:05:46 ago
         via 20.32.170.32, Ethernet43
         via 20.57.170.57, Ethernet45
         via 20.170.171.171, Ethernet1
>I    20.111.149.0/24 [115 pref/30 metric] updated 01:05:46 ago
         via 20.32.170.32, Ethernet43
         via 20.57.170.57, Ethernet45
         via 20.170.171.171, Ethernet1
>I    20.149.155.0/24 [115 pref/30 metric] updated 01:05:56 ago
         via 20.32.170.32, Ethernet43
         via 20.57.170.57, Ethernet45
         via 20.170.171.171, Ethernet1
>I    20.149.171.0/24 [115 pref/20 metric] updated 03:34:04 ago
         via 20.170.171.171, Ethernet1
>I    20.149.254.0/24 [115 pref/30 metric] updated 01:05:46 ago
         via 20.32.170.32, Ethernet43
         via 20.57.170.57, Ethernet45
         via 20.170.171.171, Ethernet1
>I    20.155.171.0/24 [115 pref/20 metric] updated 01:32:20 ago
         via 20.170.171.171, Ethernet1
>I    20.155.179.0/24 [115 pref/30 metric] updated 01:05:56 ago
         via 20.57.170.57, Ethernet45
         via 20.170.171.171, Ethernet1
>I    20.171.254.0/24 [115 pref/40 metric] updated 01:05:46 ago
         via 20.32.170.32, Ethernet43
         via 20.57.170.57, Ethernet45
         via 20.170.171.171, Ethernet1
>I    192.168.0.0/19 [115 pref/30 metric] updated 01:05:46 ago
         via 20.32.170.32, Ethernet43
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
>P    ::/96 [1 pref/0 metric] updated 1d04h ago
         via Null0, directly connected [NF]
>P    ::ffff:127.0.0.0/104 [1 pref/0 metric] updated 1d04h ago
         via :: [1 pref/1 metric] type ipv6
            via , directly connected
>P    fe80::/10 [1 pref/0 metric] updated 1d04h ago
```

## show platform sand l3 summary

```text
Number of vrfs: 2

Ipv4:
  Routes:       65  backlog:  0  unprogrammed:  0
  Adjacencies:  44  backlog:  0  unprogrammed:  0
Ipv6:
  Routes:       4   backlog:  0  unprogrammed:  0
  Adjacencies:  44  backlog:  0  unprogrammed:  0
Mpls:
  Routes:       12  backlog:  0  unprogrammed:  0
  Adjacencies:  3   backlog:  0  unprogrammed:  0

Jericho Ip Fecs:
  Non-ecmp fecs:  4112  ecmp fecs:  2  fec entries:  4117
Jericho Mpls Fecs:
  Non-ecmp fecs:  3  ecmp fecs:  0  fec entries:  3
Jericho Vxlan Overlay Fecs:
  Non-ecmp fecs:  0  ecmp fecs:  0  fec entries:  0
Jericho Vxlan Tunnel Fecs:
  Non-ecmp fecs:  0  ecmp fecs:  0  fec entries:  0
  Number of vxlan tunnels configured: 0

Jericho Lpm Routes:
  Routes:   61  unprogrammed:   0   
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
  Used:                     22  ecmp:                 3   reusedEcmp:  12    allocs:  199   frees:  180   shuffles:  0     cmds:  0   
  Non-ecmp (Percent free):  99  ecmp (Percent free):  99
  Zombies:     0    purges:    0
  Quarantine:  0/2  shuffles:  0  deletes:  2   
  Fec insertion failures:  0
  Banks in use (level, used, Percent free):
     2 (2, 22, 99%)

Lpm Detail:
  Requests:  949  cleanses:  293  batches:  293  avg batch size:  3

Lem Cmds:
  Adds:  128  dels:  112  mods:  243  fails:  0  cmds:  483

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
  ArpTable writes:      590    queued      0   
  IngressTable writes:  10179  queued      0   
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

