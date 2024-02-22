# Test results for PE32-J2-172

## show version

```text
Arista DCS-7280SR3-48YC8-F
Hardware version: 12.01
Serial number: JPE21210788
Hardware MAC address: 2cdd.e996.3abb
System MAC address: 2cdd.e996.3abb

Software image version: 4.31.2F
Architecture: i686
Internal build version: 4.31.2F-35442146.4312F
Internal build ID: 635a071a-386e-447f-942c-bcc34d9ffd3c
Image format version: 3.0
Image optimization: Default

Uptime: 20 hours and 59 minutes
Total memory: 8099732 kB
Free memory: 5564528 kB

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
Interface       IP Address           Status    Protocol           MTU   Owner  
--------------- -------------------- --------- -------------- --------- -------
Ethernet5.2     20.111.172.172/24    up        up                1500          
Ethernet45      20.172.211.172/24    down      notpresent        1500          
Ethernet47      20.171.172.172/24    up        up                1500          
Ethernet49/1    20.57.172.172/24     up        up                1500          
Loopback0       10.0.0.172/32        up        up               65535          
Management1     192.168.20.172/23    up        up                1500          

```

## show interfaces counters rates | nz

```text
Port      Name        Intvl  In Mbps      %  In Kpps Out Mbps      % Out Kpps
```

## show isis neighbors

```text
 
Instance  VRF      System Id        Type Interface          SNPA              State Hold time   Circuit Id          
IGP       default  NOKIA-SR2-57     L2   Ethernet49/1       P2P               UP    21          00                  
IGP       default  PE31-J2-171      L2   Ethernet47         P2P               UP    27          54                  
```

## show isis database detail

```text
Legend:
H - hostname conflict
U - node unreachable

IS-IS Instance: IGP VRF: default
  IS-IS Level 2 Link State Database
    LSPID                   Seq Num  Cksum  Life Length IS  Received LSPID        Flags
    h3c_19_CR16010E-F.00-00      2025  41502  1182    367 L2  0000.0000.0019.00-00  <>
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
    eantc-jcnr2.00-00           660  25881   980    229 L2  0000.0000.0020.00-00  <>
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
    12502-1.00-00              7739  29072  1183    482 L2  0000.0000.0024.00-00  <>
      Remaining lifetime received: 1199 s Modified to: 1200 s
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
    Ribbon-32.00-00              15  43298   782     83 L2  0000.0000.0032.00-00  <>
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
        Algorithms:  0, 128
      Unsupported TLV: Type: 14 Length: 2
    Ribbon-32.00-03               5  35253   910     38 L2  0000.0000.0032.00-03  <>
      Remaining lifetime received: 1199 s Modified to: 1200 s
      Hostname: Ribbon-32
    Ribbon-32.00-04             181  11128  1188    245 L2  0000.0000.0032.00-04  <>
      Remaining lifetime received: 1199 s Modified to: 1200 s
      Interface address: 10.0.0.32
      Interface address: 20.32.149.32
      Interface address: 20.32.211.32
      Interface address: 20.32.171.32
      IS Neighbor          : PE31-J2-171.00      Metric: 10
        IPv4 Neighbor Address: 20.32.171.171
        IPv4 Interface Address: 20.32.171.32
        Adj-sid: 756652 flags: [L V] weight: 0x0
        Adj-sid: 756653 flags: [L V B] weight: 0x0
      Reachability         : 10.0.0.32/32 Metric: 0 Type: 1 Up
        SR Prefix-SID: 32 Flags: [N] Algorithm: 0
        SR Prefix-SID: 1032 Flags: [N] Algorithm: 128
      Reachability         : 20.32.149.0/24 Metric: 10 Type: 1 Up
      Reachability         : 20.32.211.0/24 Metric: 10 Type: 1 Up
      Reachability         : 20.32.171.0/24 Metric: 10 Type: 1 Up
    huawei_254_NetEngine_8000_F8.00-00      8532  12484  1182    278 L2  0000.0000.0254.00-00  <>
      NLPID: 0xCC(IPv4)
      Hostname: huawei_254_NetEngine_8000_F8
      Area addresses: 49
      Interface address: 10.0.0.254
      Interface address: 20.57.254.254
      Interface address: 20.179.254.254
      Interface address: 20.149.254.254
      IS Neighbor          : juniper_379_MX304.00 Metric: 10
        IPv4 Neighbor Address: 20.179.254.179
        IPv4 Interface Address: 20.179.254.254
        Adj-sid: 48041 flags: [L V] weight: 0x0
      IS Neighbor          : h49-N540-24Q8L2DD.00 Metric: 10
        IPv4 Neighbor Address: 20.149.254.149
        IPv4 Interface Address: 20.149.254.254
        Adj-sid: 48043 flags: [L V] weight: 0x0
      Reachability         : 10.0.0.254/32 Metric: 0 Type: 1 Up
        SR Prefix-SID: 254 Flags: [N] Algorithm: 0
        SR Prefix-SID: 1254 Flags: [N] Algorithm: 128
      Reachability         : 20.57.254.0/24 Metric: 10 Type: 1 Up
      Reachability         : 20.179.254.0/24 Metric: 10 Type: 1 Up
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
    h49-N540-24Q8L2DD.00-00       607  38908   867    953 L2  0000.0000.0349.00-00  <>
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
      IS Neighbor          : 0010.0010.0005.00   Metric: 10
        IPv4 Neighbor Address: 20.5.149.5
        IPv4 Interface Address: 20.5.149.149
        Adj-sid: 24007 flags: [L V] weight: 0x0
      IS Neighbor          : huawei_254_NetEngine_8000_F8.00 Metric: 10
        IPv4 Neighbor Address: 20.149.254.254
        IPv4 Interface Address: 20.149.254.149
        Adj-sid: 24001 flags: [L V] weight: 0x0
      IS Neighbor          : h55-8201-24H8FH.00  Metric: 10
        IPv4 Neighbor Address: 20.149.155.155
        IPv4 Interface Address: 20.149.155.149
        Adj-sid: 24013 flags: [L V] weight: 0x0
      IS Neighbor          : NOKIA-SR2-57.00     Metric: 10
        IPv4 Neighbor Address: 20.57.149.57
        IPv4 Interface Address: 20.57.149.149
        Adj-sid: 24009 flags: [L V] weight: 0x0
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
      Reachability         : 20.47.149.0/24 Metric: 10 Type: 1 Up
      Reachability         : 20.57.149.0/24 Metric: 10 Type: 1 Up
      Reachability         : 20.83.149.0/24 Metric: 10 Type: 1 Up
      Reachability         : 20.111.149.0/24 Metric: 10 Type: 1 Up
      Reachability         : 20.149.155.0/24 Metric: 10 Type: 1 Up
      Reachability         : 20.149.254.0/24 Metric: 10 Type: 1 Up
      Unsupported TLV: Type: 14 Length: 2
    h49-N540-24Q8L2DD.00-01       107  20323  1081    188 L2  0000.0000.0349.00-01  <>
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
    h55-8201-24H8FH.00-00       427    682   820    449 L2  0000.0000.0355.00-00  <>
      NLPID: 0xCC(IPv4)
      Hostname: h55-8201-24H8FH
      Area addresses: 49
      Interface address: 10.0.1.55
      IS Neighbor          : h49-N540-24Q8L2DD.00 Metric: 10
        IPv4 Neighbor Address: 20.149.155.149
        IPv4 Interface Address: 20.149.155.155
        Adj-sid: 24001 flags: [L V] weight: 0x0
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
    juniper_379_MX304.00-00       149   4896   870    350 L2  0000.0001.7900.00-00  <>
      Remaining lifetime received: 1195 s Modified to: 1200 s
      NLPID: 0xCC(IPv4) 0x8E(IPv6)
      Hostname: juniper_379_MX304
      Area addresses: 49.0001.00
      Interface address: 10.0.0.179
      IS Neighbor          : huawei_254_NetEngine_8000_F8.00 Metric: 100
        IPv4 Neighbor Address: 20.179.254.254
        IPv4 Interface Address: 20.179.254.179
        Adj-sid: 26 flags: [L V B] weight: 0x0
      Reachability         : 10.0.0.179/32 Metric: 0 Type: 1 Up
        SR Prefix-SID: 379 Flags: [N] Algorithm: 0
        SR Prefix-SID: 1179 Flags: [N] Algorithm: 128
        SR Prefix-SID: 679 Flags: [N] Algorithm: 142
        SR Prefix-SID: 579 Flags: [N] Algorithm: 141
        SR Prefix-SID: 479 Flags: [N] Algorithm: 140
        SR Prefix-SID: 1379 Flags: [N] Algorithm: 130
        SR Prefix-SID: 1279 Flags: [N] Algorithm: 129
      Reachability         : 20.57.179.0/24 Metric: 10 Type: 1 Up
      Reachability         : 20.179.254.0/24 Metric: 100 Type: 1 Up
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
    0010.0010.0005.00-00        222  45322  1140    303 L2  0010.0010.0005.00-00  <>
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
        Algorithms:  0, 130, 128, 129
        Flex Algo: Algorithm: 130 Metric: IGP Metric (0) Calc: SSPF (1) Prio: 130
          Exclude admin groups: 1
        Flex Algo: Algorithm: 128 Metric: Min Unidirectional Delay Metric (1) Calc: SSPF (1) Prio: 128
        Flex Algo: Algorithm: 129 Metric: TE Metric (2) Calc: SSPF (1) Prio: 129
    NOKIA-SR2-57.00-00        17559  40309  1182    643 L2  0100.0000.0057.00-00  <>
      NLPID: 0xCC(IPv4) 0x8E(IPv6)
      Hostname: NOKIA-SR2-57
      Area addresses: 49.0000.0000.0057.00
      Interface address: 10.0.0.57
      Interface address: 20.57.149.57
      Interface address: 20.57.171.57
      Interface address: 20.57.172.57
      Interface address: 2002::57
      IS Neighbor (Narrow metrics, unsupported): PE32-J2-172.00      Metric: 10
      IS Neighbor (Narrow metrics, unsupported): PE31-J2-171.00      Metric: 63
      IS Neighbor (Narrow metrics, unsupported): h49-N540-24Q8L2DD.00 Metric: 10
      IS Neighbor          : PE32-J2-172.00      Metric: 10
        IPv4 Neighbor Address: 20.57.172.172
        IPv4 Interface Address: 20.57.172.57
        Adj-sid: 30172 flags: [L V B] weight: 0x0
      IS Neighbor          : PE31-J2-171.00      Metric: 63
        IPv4 Neighbor Address: 20.57.171.171
        IPv4 Interface Address: 20.57.171.57
        Adj-sid: 30171 flags: [L V B] weight: 0x0
      IS Neighbor          : h49-N540-24Q8L2DD.00 Metric: 10
        IPv4 Neighbor Address: 20.57.149.149
        IPv4 Interface Address: 20.57.149.57
        Adj-sid: 30149 flags: [L V B] weight: 0x0
      Reachability (Narrow metrics, unsupported): 10.0.0.57/32 Metric: 0 Type: 1
      Reachability (Narrow metrics, unsupported): 20.57.149.0/24 Metric: 10 Type: 1
      Reachability (Narrow metrics, unsupported): 20.57.171.0/24 Metric: 63 Type: 1
      Reachability (Narrow metrics, unsupported): 20.57.172.0/24 Metric: 10 Type: 1
      Reachability         : 10.0.0.57/32 Metric: 0 Type: 1 Up
        SR Prefix-SID: 57 Flags: [N P] Algorithm: 0
        SR Prefix-SID: 1057 Flags: [N P] Algorithm: 128
        SR Prefix-SID: 1157 Flags: [N P] Algorithm: 129
        SR Prefix-SID: 1257 Flags: [N P] Algorithm: 130
        SR Prefix-SID: 1357 Flags: [N P] Algorithm: 131
        SR Prefix-SID: 1457 Flags: [N P] Algorithm: 132
      Reachability         : 20.57.149.0/24 Metric: 10 Type: 1 Up
      Reachability         : 20.57.171.0/24 Metric: 63 Type: 1 Up
      Reachability         : 20.57.172.0/24 Metric: 10 Type: 1 Up
      Reachability          : 2002::57/128 Metric: 0 Type: 1 Up
        SR Prefix-SID: 157 Flags: [N P] Algorithm: 0
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
    PE31-J2-171.00-00           525  45605   668    413 L2  0100.0000.0171.00-00  <>
      Remaining lifetime received: 1199 s Modified to: 1200 s
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
        Adj-sid: 362153 flags: [L V] weight: 0x0
      IS Neighbor          : NOKIA-SR2-57.00     Metric: 10
        IPv4 Neighbor Address: 20.57.171.57
        IPv4 Interface Address: 20.57.171.171
        Adj-sid: 362147 flags: [L V] weight: 0x0
      IS Neighbor          : PE32-J2-172.00      Metric: 10
        IPv4 Neighbor Address: 20.171.172.172
        IPv4 Interface Address: 20.171.172.171
        Adj-sid: 362146 flags: [L V] weight: 0x0
      Reachability         : 10.0.0.171/32 Metric: 0 Type: 1 Up
        SR Prefix-SID: 171 Flags: [N] Algorithm: 0
        SR Prefix-SID: 1171 Flags: [N] Algorithm: 128
        SR Prefix-SID: 1271 Flags: [N] Algorithm: 129
        SR Prefix-SID: 1371 Flags: [N] Algorithm: 130
        SR Prefix-SID: 1471 Flags: [N] Algorithm: 131
      Reachability         : 20.32.171.0/24 Metric: 10 Type: 1 Up
      Reachability         : 20.57.171.0/24 Metric: 10 Type: 1 Up
      Reachability         : 20.171.172.0/24 Metric: 10 Type: 1 Up
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
    PE32-J2-172.00-00            27  62852   666    310 L2  0100.0000.0172.00-00  <>
      LSP generation remaining wait time: 0 ms
      Time remaining until refresh: 366 s
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
    h3c_19_CR16010E-F.00-00      2025  41502  1181    367 L2  0000.0000.0019.00-00  <>
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
    eantc-jcnr2.00-00           660  25881   980    229 L2  0000.0000.0020.00-00  <>
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
    12502-1.00-00              7739  29072  1182    482 L2  0000.0000.0024.00-00  <>
      Remaining lifetime received: 1199 s Modified to: 1200 s
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
    Ribbon-32.00-00              15  43298   781     83 L2  0000.0000.0032.00-00  <>
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
        Algorithms:  0, 128
      Unsupported TLV: Type: 14 Length: 2
    Ribbon-32.00-03               5  35253   909     38 L2  0000.0000.0032.00-03  <>
      Remaining lifetime received: 1199 s Modified to: 1200 s
      Hostname: Ribbon-32
    Ribbon-32.00-04             181  11128  1187    245 L2  0000.0000.0032.00-04  <>
      Remaining lifetime received: 1199 s Modified to: 1200 s
      Interface address: 10.0.0.32
      Interface address: 20.32.149.32
      Interface address: 20.32.211.32
      Interface address: 20.32.171.32
      IS Neighbor          : PE31-J2-171.00      Metric: 10
        IPv4 Neighbor Address: 20.32.171.171
        IPv4 Interface Address: 20.32.171.32
        Adj-sid: 756652 flags: [L V] weight: 0x0
        Adj-sid: 756653 flags: [L V B] weight: 0x0
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
      Reachability         : 20.32.171.0/24 Metric: 10 Type: 1 Up
    huawei_254_NetEngine_8000_F8.00-00      8532  12484  1181    278 L2  0000.0000.0254.00-00  <>
      NLPID: 0xCC(IPv4)
      Hostname: huawei_254_NetEngine_8000_F8
      Area addresses: 49
      Interface address: 10.0.0.254
      Interface address: 20.57.254.254
      Interface address: 20.179.254.254
      Interface address: 20.149.254.254
      IS Neighbor          : juniper_379_MX304.00 Metric: 10
        IPv4 Neighbor Address: 20.179.254.179
        IPv4 Interface Address: 20.179.254.254
        Adj-sid: 48041 flags: [L V] weight: 0x0
        Application Specific Link Attributes:
          Standard applications: Flex-Algo
            TE default metric: 12
            Min/Max unidirectional link delay: 11/11 us
      IS Neighbor          : h49-N540-24Q8L2DD.00 Metric: 10
        IPv4 Neighbor Address: 20.149.254.149
        IPv4 Interface Address: 20.149.254.254
        Adj-sid: 48043 flags: [L V] weight: 0x0
        Application Specific Link Attributes:
          Standard applications: Flex-Algo
            TE default metric: 12
            Min/Max unidirectional link delay: 11/11 us
      Reachability         : 10.0.0.254/32 Metric: 0 Type: 1 Up
        SR Prefix-SID: 254 Flags: [N] Algorithm: 0
        SR Prefix-SID: 1254 Flags: [N] Algorithm: 128
      Reachability         : 20.57.254.0/24 Metric: 10 Type: 1 Up
      Reachability         : 20.179.254.0/24 Metric: 10 Type: 1 Up
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
    h49-N540-24Q8L2DD.00-00       607  38908   867    953 L2  0000.0000.0349.00-00  <>
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
        Application Specific Link Attributes:
          Standard applications: Flex-Algo
          User-defined applications: APP3
            TE default metric: 12
            Maximum link BW: 100.00 Gbps
            Min/Max unidirectional link delay: 11/11 us
      IS Neighbor          : 0010.0010.0005.00   Metric: 10
        IPv4 Neighbor Address: 20.5.149.5
        IPv4 Interface Address: 20.5.149.149
        Adj-sid: 24007 flags: [L V] weight: 0x0
        Maximum link BW: 10.00 Gbps
        Min/Max unidirectional link delay: 11/11 us
        Application Specific Link Attributes:
          Standard applications: Flex-Algo
          User-defined applications: APP3
            TE default metric: 12
            Maximum link BW: 10.00 Gbps
            Min/Max unidirectional link delay: 11/11 us
      IS Neighbor          : huawei_254_NetEngine_8000_F8.00 Metric: 10
        IPv4 Neighbor Address: 20.149.254.254
        IPv4 Interface Address: 20.149.254.149
        Adj-sid: 24001 flags: [L V] weight: 0x0
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
        Adj-sid: 24013 flags: [L V] weight: 0x0
        Maximum link BW: 100.00 Gbps
        Min/Max unidirectional link delay: 2/2 us
        Application Specific Link Attributes:
          Standard applications: Flex-Algo
          User-defined applications: APP3
            TE default metric: 12
            Maximum link BW: 100.00 Gbps
            Min/Max unidirectional link delay: 2/2 us
      IS Neighbor          : NOKIA-SR2-57.00     Metric: 10
        IPv4 Neighbor Address: 20.57.149.57
        IPv4 Interface Address: 20.57.149.149
        Adj-sid: 24009 flags: [L V] weight: 0x0
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
      Reachability         : 20.47.149.0/24 Metric: 10 Type: 1 Up
      Reachability         : 20.57.149.0/24 Metric: 10 Type: 1 Up
      Reachability         : 20.83.149.0/24 Metric: 10 Type: 1 Up
      Reachability         : 20.111.149.0/24 Metric: 10 Type: 1 Up
      Reachability         : 20.149.155.0/24 Metric: 10 Type: 1 Up
      Reachability         : 20.149.254.0/24 Metric: 10 Type: 1 Up
      Unsupported TLV: Type: 14 Length: 2
    h49-N540-24Q8L2DD.00-01       107  20323  1080    188 L2  0000.0000.0349.00-01  <>
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
    h55-8201-24H8FH.00-00       427    682   819    449 L2  0000.0000.0355.00-00  <>
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
    juniper_379_MX304.00-00       149   4896   869    350 L2  0000.0001.7900.00-00  <>
      Remaining lifetime received: 1195 s Modified to: 1200 s
      NLPID: 0xCC(IPv4) 0x8E(IPv6)
      Hostname: juniper_379_MX304
      TE IPv4 router ID: 10.0.0.179
      Area addresses: 49.0001.00
      Interface address: 10.0.0.179
      IS Neighbor          : huawei_254_NetEngine_8000_F8.00 Metric: 100
        IPv4 Neighbor Address: 20.179.254.254
        IPv4 Interface Address: 20.179.254.179
        Adj-sid: 26 flags: [L V B] weight: 0x0
        Maximum link BW: 10.00 Gbps
        Min/Max unidirectional link delay: 10/10 us
        Application Specific Link Attributes:
          Standard applications: Flex-Algo
            TE default metric: 12
            Min/Max unidirectional link delay: 10/10 us
      Reachability         : 10.0.0.179/32 Metric: 0 Type: 1 Up
        SR Prefix-SID: 379 Flags: [N] Algorithm: 0
        SR Prefix-SID: 1179 Flags: [N] Algorithm: 128
        SR Prefix-SID: 679 Flags: [N] Algorithm: 142
        SR Prefix-SID: 579 Flags: [N] Algorithm: 141
        SR Prefix-SID: 479 Flags: [N] Algorithm: 140
        SR Prefix-SID: 1379 Flags: [N] Algorithm: 130
        SR Prefix-SID: 1279 Flags: [N] Algorithm: 129
      Reachability         : 20.57.179.0/24 Metric: 10 Type: 1 Up
      Reachability         : 20.179.254.0/24 Metric: 100 Type: 1 Up
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
    0010.0010.0005.00-00        222  45322  1139    303 L2  0010.0010.0005.00-00  <>
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
        Application Specific Link Attributes:
          Standard applications: RSVP-TE SR-TE LFA Flex-Algo
            TE default metric: 12
            Min/Max unidirectional link delay: 11/11 us
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
        Algorithms:  0, 130, 128, 129
        Flex Algo: Algorithm: 130 Metric: IGP Metric (0) Calc: SSPF (1) Prio: 130
          Exclude admin groups: 1
        Flex Algo: Algorithm: 128 Metric: Min Unidirectional Delay Metric (1) Calc: SSPF (1) Prio: 128
        Flex Algo: Algorithm: 129 Metric: TE Metric (2) Calc: SSPF (1) Prio: 129
    NOKIA-SR2-57.00-00        17559  40309  1181    643 L2  0100.0000.0057.00-00  <>
      NLPID: 0xCC(IPv4) 0x8E(IPv6)
      Hostname: NOKIA-SR2-57
      TE IPv4 router ID: 10.0.0.57
      TE IPv6 router ID: 2002::57
      Area addresses: 49.0000.0000.0057.00
      Interface address: 10.0.0.57
      Interface address: 20.57.149.57
      Interface address: 20.57.171.57
      Interface address: 20.57.172.57
      Interface address: 2002::57
      IS Neighbor (Narrow metrics, unsupported): PE32-J2-172.00      Metric: 10
      IS Neighbor (Narrow metrics, unsupported): PE31-J2-171.00      Metric: 63
      IS Neighbor (Narrow metrics, unsupported): h49-N540-24Q8L2DD.00 Metric: 10
      IS Neighbor          : PE32-J2-172.00      Metric: 10
        IPv4 Neighbor Address: 20.57.172.172
        IPv4 Interface Address: 20.57.172.57
        Adj-sid: 30172 flags: [L V B] weight: 0x0
        Application Specific Link Attributes:
          Standard applications: Flex-Algo
            Min/Max unidirectional link delay: 11/11 us
      IS Neighbor          : PE31-J2-171.00      Metric: 63
        IPv4 Neighbor Address: 20.57.171.171
        IPv4 Interface Address: 20.57.171.57
        Adj-sid: 30171 flags: [L V B] weight: 0x0
        Application Specific Link Attributes:
          Standard applications: Flex-Algo
            Min/Max unidirectional link delay: 11/11 us
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
            Min/Max unidirectional link delay: 11/11 us
      Reachability (Narrow metrics, unsupported): 10.0.0.57/32 Metric: 0 Type: 1
      Reachability (Narrow metrics, unsupported): 20.57.149.0/24 Metric: 10 Type: 1
      Reachability (Narrow metrics, unsupported): 20.57.171.0/24 Metric: 63 Type: 1
      Reachability (Narrow metrics, unsupported): 20.57.172.0/24 Metric: 10 Type: 1
      Reachability         : 10.0.0.57/32 Metric: 0 Type: 1 Up
        SR Prefix-SID: 57 Flags: [N P] Algorithm: 0
        SR Prefix-SID: 1057 Flags: [N P] Algorithm: 128
        SR Prefix-SID: 1157 Flags: [N P] Algorithm: 129
        SR Prefix-SID: 1257 Flags: [N P] Algorithm: 130
        SR Prefix-SID: 1357 Flags: [N P] Algorithm: 131
        SR Prefix-SID: 1457 Flags: [N P] Algorithm: 132
      Reachability         : 20.57.149.0/24 Metric: 10 Type: 1 Up
      Reachability         : 20.57.171.0/24 Metric: 63 Type: 1 Up
      Reachability         : 20.57.172.0/24 Metric: 10 Type: 1 Up
      Reachability          : 2002::57/128 Metric: 0 Type: 1 Up
        SR Prefix-SID: 157 Flags: [N P] Algorithm: 0
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
    PE31-J2-171.00-00           525  45605   667    413 L2  0100.0000.0171.00-00  <>
      Remaining lifetime received: 1199 s Modified to: 1200 s
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
        Adj-sid: 362153 flags: [L V] weight: 0x0
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
      Reachability         : 10.0.0.171/32 Metric: 0 Type: 1 Up
        SR Prefix-SID: 171 Flags: [N] Algorithm: 0
        SR Prefix-SID: 1171 Flags: [N] Algorithm: 128
        SR Prefix-SID: 1271 Flags: [N] Algorithm: 129
        SR Prefix-SID: 1371 Flags: [N] Algorithm: 130
        SR Prefix-SID: 1471 Flags: [N] Algorithm: 131
      Reachability         : 20.32.171.0/24 Metric: 10 Type: 1 Up
      Reachability         : 20.57.171.0/24 Metric: 10 Type: 1 Up
      Reachability         : 20.171.172.0/24 Metric: 10 Type: 1 Up
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
    PE32-J2-172.00-00            27  62852   665    310 L2  0100.0000.0172.00-00  <>
      LSP generation remaining wait time: 0 ms
      Time remaining until refresh: 365 s
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

Algorithm     Advertised Level Metric  Selected         
------------- ---------- ----- ------- -----------------
MIN-TE        yes        L2    TE      h49-N540-24Q8L2DD
MIN-IGP       yes        L2    default h49-N540-24Q8L2DD
MIN-IGP-ADMIN yes        L2    default h49-N540-24Q8L2DD

```

## show isis flex-algo path detail

```text
Flex algo paths for IPv4 address family
Topology ID: Level-2
Destination: 0010.0010.0005
Path ID: 641
Path constraints: algo MIN-TE
                  metric type TE
Request sequence number: 11
Response sequence number: 11
Number of times path updated: 11
Last updated: 0:00:18 ago
Metric: 36
Next Hop     Interface   
------------ ------------
20.57.172.57 Ethernet49/1

Destination: 0010.0010.0005
Path ID: 642
Path constraints: algo MIN-IGP
                  metric type IGP
                  administrative-group exclude 1
Request sequence number: 11
Response sequence number: 11
Number of times path updated: 12
Last updated: 0:00:18 ago
Metric: 30
Next Hop     Interface   
------------ ------------
20.57.172.57 Ethernet49/1

Destination: 0010.0010.0005
Path ID: 643
Path constraints: algo MIN-IGP-ADMIN
                  metric type IGP
                  administrative-group exclude 127
Request sequence number: 11
Response sequence number: 11
Number of times path updated: 11
Last updated: 0:00:18 ago
Next Hop Interface
-------- ---------

Destination: 12502-1
Path ID: 641
Path constraints: algo MIN-TE
                  metric type TE
Request sequence number: 11
Response sequence number: 11
Number of times path updated: 11
Last updated: 0:00:18 ago
Metric: 36
Next Hop     Interface   
------------ ------------
20.57.172.57 Ethernet49/1

Destination: 12502-1
Path ID: 642
Path constraints: algo MIN-IGP
                  metric type IGP
                  administrative-group exclude 1
Request sequence number: 11
Response sequence number: 11
Number of times path updated: 12
Last updated: 0:00:18 ago
Metric: 30
Next Hop     Interface   
------------ ------------
20.57.172.57 Ethernet49/1

Destination: 12502-1
Path ID: 643
Path constraints: algo MIN-IGP-ADMIN
                  metric type IGP
                  administrative-group exclude 127
Request sequence number: 11
Response sequence number: 11
Number of times path updated: 11
Last updated: 0:00:18 ago
Next Hop Interface
-------- ---------

Destination: NOKIA-SR2-57
Path ID: 641
Path constraints: algo MIN-TE
                  metric type TE
Request sequence number: 97
Response sequence number: 97
Number of times path updated: 96
Last updated: 0:00:18 ago
Metric: 12
Next Hop     Interface   
------------ ------------
20.57.172.57 Ethernet49/1

Destination: NOKIA-SR2-57
Path ID: 642
Path constraints: algo MIN-IGP
                  metric type IGP
                  administrative-group exclude 1
Request sequence number: 97
Response sequence number: 97
Number of times path updated: 96
Last updated: 0:00:18 ago
Metric: 10
Next Hop     Interface   
------------ ------------
20.57.172.57 Ethernet49/1

Destination: NOKIA-SR2-57
Path ID: 643
Path constraints: algo MIN-IGP-ADMIN
                  metric type IGP
                  administrative-group exclude 127
Request sequence number: 94
Response sequence number: 94
Number of times path updated: 94
Last updated: 0:00:18 ago
Metric: 10
Next Hop     Interface   
------------ ------------
20.57.172.57 Ethernet49/1

Destination: PE31-J2-171
Path ID: 641
Path constraints: algo MIN-TE
                  metric type TE
Request sequence number: 97
Response sequence number: 97
Number of times path updated: 96
Last updated: 0:00:18 ago
Metric: 12
Next Hop       Interface 
-------------- ----------
20.171.172.171 Ethernet47

Destination: PE31-J2-171
Path ID: 642
Path constraints: algo MIN-IGP
                  metric type IGP
                  administrative-group exclude 1
Request sequence number: 97
Response sequence number: 97
Number of times path updated: 96
Last updated: 0:00:18 ago
Metric: 10
Next Hop       Interface 
-------------- ----------
20.171.172.171 Ethernet47

Destination: PE31-J2-171
Path ID: 643
Path constraints: algo MIN-IGP-ADMIN
                  metric type IGP
                  administrative-group exclude 127
Request sequence number: 94
Response sequence number: 94
Number of times path updated: 93
Last updated: 0:00:18 ago
Metric: 10
Next Hop       Interface 
-------------- ----------
20.171.172.171 Ethernet47

Destination: PE32-J2-172
Path ID: 641
Path constraints: algo MIN-TE
                  metric type TE
Request sequence number: 78
Response sequence number: 78
Number of times path updated: 78
Last updated: 0:00:18 ago
Next Hop Interface
-------- ---------

Destination: PE32-J2-172
Path ID: 642
Path constraints: algo MIN-IGP
                  metric type IGP
                  administrative-group exclude 1
Request sequence number: 78
Response sequence number: 78
Number of times path updated: 78
Last updated: 0:00:18 ago
Next Hop Interface
-------- ---------

Destination: PE32-J2-172
Path ID: 643
Path constraints: algo MIN-IGP-ADMIN
                  metric type IGP
                  administrative-group exclude 127
Request sequence number: 77
Response sequence number: 77
Number of times path updated: 77
Last updated: 0:00:18 ago
Next Hop Interface
-------- ---------

Destination: h3c_19_CR16010E-F
Path ID: 641
Path constraints: algo MIN-TE
                  metric type TE
Request sequence number: 11
Response sequence number: 11
Number of times path updated: 11
Last updated: 0:00:18 ago
Metric: 36
Next Hop     Interface   
------------ ------------
20.57.172.57 Ethernet49/1

Destination: h3c_19_CR16010E-F
Path ID: 642
Path constraints: algo MIN-IGP
                  metric type IGP
                  administrative-group exclude 1
Request sequence number: 11
Response sequence number: 11
Number of times path updated: 12
Last updated: 0:00:18 ago
Metric: 30
Next Hop     Interface   
------------ ------------
20.57.172.57 Ethernet49/1

Destination: h3c_19_CR16010E-F
Path ID: 643
Path constraints: algo MIN-IGP-ADMIN
                  metric type IGP
                  administrative-group exclude 127
Request sequence number: 11
Response sequence number: 11
Number of times path updated: 11
Last updated: 0:00:18 ago
Next Hop Interface
-------- ---------

Destination: h49-N540-24Q8L2DD
Path ID: 641
Path constraints: algo MIN-TE
                  metric type TE
Request sequence number: 11
Response sequence number: 11
Number of times path updated: 11
Last updated: 0:00:18 ago
Metric: 24
Next Hop     Interface   
------------ ------------
20.57.172.57 Ethernet49/1

Destination: h49-N540-24Q8L2DD
Path ID: 642
Path constraints: algo MIN-IGP
                  metric type IGP
                  administrative-group exclude 1
Request sequence number: 11
Response sequence number: 11
Number of times path updated: 12
Last updated: 0:00:18 ago
Metric: 20
Next Hop     Interface   
------------ ------------
20.57.172.57 Ethernet49/1

Destination: h49-N540-24Q8L2DD
Path ID: 643
Path constraints: algo MIN-IGP-ADMIN
                  metric type IGP
                  administrative-group exclude 127
Request sequence number: 11
Response sequence number: 11
Number of times path updated: 11
Last updated: 0:00:18 ago
Next Hop Interface
-------- ---------

Destination: h55-8201-24H8FH
Path ID: 641
Path constraints: algo MIN-TE
                  metric type TE
Request sequence number: 11
Response sequence number: 11
Number of times path updated: 11
Last updated: 0:00:18 ago
Metric: 36
Next Hop     Interface   
------------ ------------
20.57.172.57 Ethernet49/1

Destination: h55-8201-24H8FH
Path ID: 642
Path constraints: algo MIN-IGP
                  metric type IGP
                  administrative-group exclude 1
Request sequence number: 11
Response sequence number: 11
Number of times path updated: 12
Last updated: 0:00:18 ago
Metric: 30
Next Hop     Interface   
------------ ------------
20.57.172.57 Ethernet49/1

Destination: h55-8201-24H8FH
Path ID: 643
Path constraints: algo MIN-IGP-ADMIN
                  metric type IGP
                  administrative-group exclude 127
Request sequence number: 11
Response sequence number: 11
Number of times path updated: 11
Last updated: 0:00:18 ago
Next Hop Interface
-------- ---------

Destination: juniper_379_MX304
Path ID: 641
Path constraints: algo MIN-TE
                  metric type TE
Request sequence number: 6
Response sequence number: 6
Number of times path updated: 6
Last updated: 0:00:18 ago
Next Hop Interface
-------- ---------

Destination: juniper_379_MX304
Path ID: 642
Path constraints: algo MIN-IGP
                  metric type IGP
                  administrative-group exclude 1
Request sequence number: 6
Response sequence number: 6
Number of times path updated: 6
Last updated: 0:00:18 ago
Next Hop Interface
-------- ---------

```

## show isis segment-routing tunnel

```text
  Index     Endpoint          Next Hop/Tunnel Index      Interface    Labels   
--------- ----------------- -------------------------- -------------- ---------
  1         10.0.0.83/32      TI-LFA (5)                 -            [ 20083 ]
  2         10.0.1.49/32      TI-LFA (5)                 -            [ 20349 ]
  3         10.0.0.19/32      TI-LFA (5)                 -            [ 20019 ]
  4         10.0.1.55/32      TI-LFA (5)                 -            [ 20355 ]
  5         10.0.0.57/32      TI-LFA (5)                 -            [ 20057 ]
  6         10.0.0.179/32     TI-LFA (5)                 -            [ 20379 ]
  7         10.0.0.24/32      TI-LFA (5)                 -            [ 20024 ]
  8         10.0.0.5/32       TI-LFA (5)                 -            [ 20005 ]
  9         10.0.0.171/32     TI-LFA (3)                 -            [ 3 ]    
  10        10.0.0.32/32      TI-LFA (3)                 -            [ 20032 ]

```

## show isis segment-routing prefix-segments

```text

System ID: PE32-J2-172			Instance: 'IGP'
SR supported Data-plane: MPLS			SR Router ID: 10.0.0.172

Node: 58     Proxy-Node: 0      Prefix: 0       Total Segments: 58

Flag Descriptions: R: Re-advertised, N: Node Segment, P: no-PHP
                   E: Explicit-NULL, V: Value, L: Local
Segment status codes: * - Self originated Prefix, L1 - level 1, L2 - level 2, ! - SR-unreachable,
                      # - Some IS-IS next-hops are SR-unreachable
   Prefix                      SID Type       Flags                        System ID       Level Protection  Algorithm   
   ------------------------- ----- ---------- ---------------------------- --------------- ----- ----------- -------------
   10.0.0.5/32                   5 Node       R:0 N:1 P:0 E:0 V:0 L:0      0010.0010.0005  L2    node        SPF         
   10.0.0.5/32                1005 Node       R:0 N:1 P:0 E:0 V:0 L:0      0010.0010.0005  L2    unprotected 128         
   10.0.0.5/32                1105 Node       R:0 N:1 P:0 E:0 V:0 L:0      0010.0010.0005  L2    node        MIN-TE      
   10.0.0.5/32                1205 Node       R:0 N:1 P:0 E:0 V:0 L:0      0010.0010.0005  L2    node        MIN-IGP     
   10.0.0.5/32                1305 Node       R:0 N:1 P:0 E:0 V:0 L:0      0010.0010.0005  L2    unprotected MIN-IGP-ADMIN
   10.0.0.19/32                 19 Node       R:0 N:1 P:0 E:0 V:0 L:0      h3c_19_CR16010E-F L2    node        SPF         
   10.0.0.19/32               1019 Node       R:0 N:1 P:0 E:0 V:0 L:0      h3c_19_CR16010E-F L2    unprotected 128         
   10.0.0.19/32               1119 Node       R:0 N:1 P:0 E:0 V:0 L:0      h3c_19_CR16010E-F L2    node        MIN-TE      
   10.0.0.19/32               1219 Node       R:0 N:1 P:0 E:0 V:0 L:0      h3c_19_CR16010E-F L2    node        MIN-IGP     
   10.0.0.19/32               1319 Node       R:0 N:1 P:0 E:0 V:0 L:0      h3c_19_CR16010E-F L2    unprotected MIN-IGP-ADMIN
   10.0.0.24/32                 24 Node       R:0 N:1 P:1 E:0 V:0 L:0      12502-1         L2    node        SPF         
   10.0.0.24/32               1024 Node       R:0 N:1 P:1 E:0 V:0 L:0      12502-1         L2    unprotected 128         
   10.0.0.24/32               1124 Node       R:0 N:1 P:1 E:0 V:0 L:0      12502-1         L2    node        MIN-TE      
   10.0.0.24/32               1224 Node       R:0 N:1 P:1 E:0 V:0 L:0      12502-1         L2    node        MIN-IGP     
   10.0.0.24/32               1324 Node       R:0 N:1 P:1 E:0 V:0 L:0      12502-1         L2    unprotected MIN-IGP-ADMIN
   10.0.0.32/32                 32 Node       R:0 N:1 P:0 E:0 V:0 L:0      Ribbon-32       L2    node        SPF         
   10.0.0.32/32               1032 Node       R:0 N:1 P:0 E:0 V:0 L:0      Ribbon-32       L2    unprotected 128         
   10.0.0.57/32                 57 Node       R:0 N:1 P:1 E:0 V:0 L:0      NOKIA-SR2-57    L2    node        SPF         
   10.0.0.57/32               1057 Node       R:0 N:1 P:1 E:0 V:0 L:0      NOKIA-SR2-57    L2    unprotected 128         
   10.0.0.57/32               1157 Node       R:0 N:1 P:1 E:0 V:0 L:0      NOKIA-SR2-57    L2    node        MIN-TE      
   10.0.0.57/32               1257 Node       R:0 N:1 P:1 E:0 V:0 L:0      NOKIA-SR2-57    L2    node        MIN-IGP     
   10.0.0.57/32               1357 Node       R:0 N:1 P:1 E:0 V:0 L:0      NOKIA-SR2-57    L2    node        MIN-IGP-ADMIN
   10.0.0.57/32               1457 Node       R:0 N:1 P:1 E:0 V:0 L:0      NOKIA-SR2-57    L2    unprotected 132         
   10.0.0.83/32                 83 Node       R:0 N:1 P:0 E:0 V:0 L:0      eantc-jcnr2     L2    node        SPF         
   10.0.0.171/32               171 Node       R:0 N:1 P:0 E:0 V:0 L:0      PE31-J2-171     L2    node        SPF         
   10.0.0.171/32              1171 Node       R:0 N:1 P:0 E:0 V:0 L:0      PE31-J2-171     L2    unprotected 128         
   10.0.0.171/32              1271 Node       R:0 N:1 P:0 E:0 V:0 L:0      PE31-J2-171     L2    node        MIN-TE      
   10.0.0.171/32              1371 Node       R:0 N:1 P:0 E:0 V:0 L:0      PE31-J2-171     L2    node        MIN-IGP     
   10.0.0.171/32              1471 Node       R:0 N:1 P:0 E:0 V:0 L:0      PE31-J2-171     L2    node        MIN-IGP-ADMIN
*  10.0.0.172/32               172 Node       R:0 N:1 P:0 E:0 V:0 L:0      PE32-J2-172     L2    unprotected SPF         
*  10.0.0.172/32              1272 Node       R:0 N:1 P:0 E:0 V:0 L:0      PE32-J2-172     L2    unprotected MIN-TE      
*  10.0.0.172/32              1372 Node       R:0 N:1 P:0 E:0 V:0 L:0      PE32-J2-172     L2    unprotected MIN-IGP     
*  10.0.0.172/32              1472 Node       R:0 N:1 P:0 E:0 V:0 L:0      PE32-J2-172     L2    unprotected MIN-IGP-ADMIN
   10.0.0.179/32               379 Node       R:0 N:1 P:0 E:0 V:0 L:0      juniper_379_MX304 L2    node        SPF         
   10.0.0.179/32              1179 Node       R:0 N:1 P:0 E:0 V:0 L:0      juniper_379_MX304 L2    unprotected 128         
   10.0.0.179/32              1279 Node       R:0 N:1 P:0 E:0 V:0 L:0      juniper_379_MX304 L2    unprotected MIN-TE      
   10.0.0.179/32              1379 Node       R:0 N:1 P:0 E:0 V:0 L:0      juniper_379_MX304 L2    unprotected MIN-IGP     
   10.0.0.179/32               479 Node       R:0 N:1 P:0 E:0 V:0 L:0      juniper_379_MX304 L2    unprotected 140         
   10.0.0.179/32               579 Node       R:0 N:1 P:0 E:0 V:0 L:0      juniper_379_MX304 L2    unprotected 141         
   10.0.0.179/32               679 Node       R:0 N:1 P:0 E:0 V:0 L:0      juniper_379_MX304 L2    unprotected 142         
   10.0.1.49/32                349 Node       R:0 N:1 P:0 E:0 V:0 L:0      h49-N540-24Q8L2DD L2    node        SPF         
   10.0.1.49/32               1449 Node       R:0 N:1 P:0 E:0 V:0 L:0      h49-N540-24Q8L2DD L2    node        MIN-TE      
   10.0.1.49/32               1549 Node       R:0 N:1 P:0 E:0 V:0 L:0      h49-N540-24Q8L2DD L2    node        MIN-IGP     
   10.0.1.49/32               1649 Node       R:0 N:1 P:0 E:0 V:0 L:0      h49-N540-24Q8L2DD L2    unprotected MIN-IGP-ADMIN
   10.0.1.49/32               1749 Node       R:0 N:1 P:0 E:0 V:0 L:0      h49-N540-24Q8L2DD L2    unprotected 132         
   10.0.1.49/32                449 Node       R:0 N:1 P:0 E:0 V:0 L:0      h49-N540-24Q8L2DD L2    unprotected 140         
   10.0.1.49/32                549 Node       R:0 N:1 P:0 E:0 V:0 L:0      h49-N540-24Q8L2DD L2    unprotected 141         
   10.0.1.49/32                649 Node       R:0 N:1 P:0 E:0 V:0 L:0      h49-N540-24Q8L2DD L2    unprotected 142         
   10.0.1.55/32                355 Node       R:0 N:1 P:0 E:0 V:0 L:0      h55-8201-24H8FH L2    node        SPF         
   10.0.1.55/32               1355 Node       R:0 N:1 P:0 E:0 V:0 L:0      h55-8201-24H8FH L2    unprotected 128         
   10.0.1.55/32               1455 Node       R:0 N:1 P:0 E:0 V:0 L:0      h55-8201-24H8FH L2    node        MIN-TE      
   10.0.1.55/32               1555 Node       R:0 N:1 P:0 E:0 V:0 L:0      h55-8201-24H8FH L2    node        MIN-IGP     
   10.0.1.55/32               1655 Node       R:0 N:1 P:0 E:0 V:0 L:0      h55-8201-24H8FH L2    unprotected MIN-IGP-ADMIN
   10.0.1.55/32               1755 Node       R:0 N:1 P:0 E:0 V:0 L:0      h55-8201-24H8FH L2    unprotected 132         
   10.0.1.55/32                455 Node       R:0 N:1 P:0 E:0 V:0 L:0      h55-8201-24H8FH L2    unprotected 140         
   10.0.1.55/32                555 Node       R:0 N:1 P:0 E:0 V:0 L:0      h55-8201-24H8FH L2    unprotected 141         
   10.0.1.55/32                655 Node       R:0 N:1 P:0 E:0 V:0 L:0      h55-8201-24H8FH L2    unprotected 142         
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

 I L2     10.0.0.5/32 [115/40]
           via 20.57.172.57, Ethernet49/1
 I L2     10.0.0.19/32 [115/30]
           via 20.57.172.57, Ethernet49/1
 I L2     10.0.0.24/32 [115/30]
           via 20.57.172.57, Ethernet49/1
 I L2     10.0.0.32/32 [115/20]
           via 20.171.172.171, Ethernet47
 I L2     10.0.0.57/32 [115/10]
           via 20.57.172.57, Ethernet49/1
 I L2     10.0.0.83/32 [115/30]
           via 20.57.172.57, Ethernet49/1
 I L2     10.0.0.171/32 [115/10]
           via 20.171.172.171, Ethernet47
 C        10.0.0.172/32
           directly connected, Loopback0
 I L2     10.0.0.179/32 [115/40]
           via 20.57.172.57, Ethernet49/1
 I L2     10.0.0.254/32 [115/30]
           via 20.57.172.57, Ethernet49/1
 I L2     10.0.1.49/32 [115/20]
           via 20.57.172.57, Ethernet49/1
 I L2     10.0.1.55/32 [115/30]
           via 20.57.172.57, Ethernet49/1
 I L2     20.5.149.0/24 [115/30]
           via 20.57.172.57, Ethernet49/1
 I L2     20.19.149.0/24 [115/30]
           via 20.57.172.57, Ethernet49/1
 I L2     20.24.149.0/24 [115/30]
           via 20.57.172.57, Ethernet49/1
 I L2     20.32.149.0/24 [115/30]
           via 20.171.172.171, Ethernet47
 I L2     20.32.171.0/24 [115/20]
           via 20.171.172.171, Ethernet47
 I L2     20.32.211.0/24 [115/30]
           via 20.171.172.171, Ethernet47
 I L2     20.47.149.0/24 [115/30]
           via 20.57.172.57, Ethernet49/1
 I L2     20.57.149.0/24 [115/20]
           via 20.57.172.57, Ethernet49/1
 I L2     20.57.155.0/24 [115/40]
           via 20.57.172.57, Ethernet49/1
 I L2     20.57.171.0/24 [115/20]
           via 20.171.172.171, Ethernet47
 C        20.57.172.0/24
           directly connected, Ethernet49/1
 I L2     20.57.179.0/24 [115/50]
           via 20.57.172.57, Ethernet49/1
 I L2     20.57.254.0/24 [115/40]
           via 20.57.172.57, Ethernet49/1
 I L2     20.83.149.0/24 [115/30]
           via 20.57.172.57, Ethernet49/1
 I L2     20.111.149.0/24 [115/30]
           via 20.57.172.57, Ethernet49/1
 I L2     20.149.155.0/24 [115/30]
           via 20.57.172.57, Ethernet49/1
 I L2     20.149.254.0/24 [115/30]
           via 20.57.172.57, Ethernet49/1
 C        20.171.172.0/24
           directly connected, Ethernet47
 I L2     20.179.254.0/24 [115/40]
           via 20.57.172.57, Ethernet49/1
 I L2     192.168.20.0/23 [115/30]
           via 20.57.172.57, Ethernet49/1
 I L2     192.168.0.0/19 [115/30]
           via 20.57.172.57, Ethernet49/1

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
           via 20.57.172.57, Ethernet49/1
 I L2     10.0.0.19/32 [115/30]
           via 20.57.172.57, Ethernet49/1
 I L2     10.0.0.24/32 [115/30]
           via 20.57.172.57, Ethernet49/1
 I L2     10.0.0.32/32 [115/20]
           via 20.171.172.171, Ethernet47
 I L2     10.0.0.57/32 [115/10]
           via 20.57.172.57, Ethernet49/1
 I L2     10.0.0.83/32 [115/30]
           via 20.57.172.57, Ethernet49/1
 I L2     10.0.0.171/32 [115/10]
           via 20.171.172.171, Ethernet47
 C        10.0.0.172/32
           directly connected, Loopback0
 I L2     10.0.0.179/32 [115/40]
           via 20.57.172.57, Ethernet49/1
 I L2     10.0.0.254/32 [115/30]
           via 20.57.172.57, Ethernet49/1
 I L2     10.0.1.49/32 [115/20]
           via 20.57.172.57, Ethernet49/1
 I L2     10.0.1.55/32 [115/30]
           via 20.57.172.57, Ethernet49/1
 I L2     20.5.149.0/24 [115/30]
           via 20.57.172.57, Ethernet49/1
 I L2     20.19.149.0/24 [115/30]
           via 20.57.172.57, Ethernet49/1
 I L2     20.24.149.0/24 [115/30]
           via 20.57.172.57, Ethernet49/1
 I L2     20.32.149.0/24 [115/30]
           via 20.171.172.171, Ethernet47
 I L2     20.32.171.0/24 [115/20]
           via 20.171.172.171, Ethernet47
 I L2     20.32.211.0/24 [115/30]
           via 20.171.172.171, Ethernet47
 I L2     20.47.149.0/24 [115/30]
           via 20.57.172.57, Ethernet49/1
 I L2     20.57.149.0/24 [115/20]
           via 20.57.172.57, Ethernet49/1
 I L2     20.57.155.0/24 [115/40]
           via 20.57.172.57, Ethernet49/1
 I L2     20.57.171.0/24 [115/20]
           via 20.171.172.171, Ethernet47
 C        20.57.172.0/24
           directly connected, Ethernet49/1
 I L2     20.57.179.0/24 [115/50]
           via 20.57.172.57, Ethernet49/1
 I L2     20.57.254.0/24 [115/40]
           via 20.57.172.57, Ethernet49/1
 I L2     20.83.149.0/24 [115/30]
           via 20.57.172.57, Ethernet49/1
 I L2     20.111.149.0/24 [115/30]
           via 20.57.172.57, Ethernet49/1
 I L2     20.149.155.0/24 [115/30]
           via 20.57.172.57, Ethernet49/1
 I L2     20.149.254.0/24 [115/30]
           via 20.57.172.57, Ethernet49/1
 C        20.171.172.0/24
           directly connected, Ethernet47
 I L2     20.179.254.0/24 [115/40]
           via 20.57.172.57, Ethernet49/1
 I L2     192.168.20.0/23 [115/30]
           via 20.57.172.57, Ethernet49/1
 I L2     192.168.0.0/19 [115/30]
           via 20.57.172.57, Ethernet49/1


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


! IP routing not enabled

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


! IP routing not enabled

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


! IP routing not enabled

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


! IP routing not enabled

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


! IP routing not enabled

VRF: OSPF-SR-L3VPN
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

 C        20.111.172.0/24
           directly connected, Ethernet5.2


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
MPLS forwarding table (Label [metric] Vias) - 29 routes 
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
                  via TI-LFA tunnel index 5
                    via 20.57.172.57, Ethernet49/1, label imp-null(3)
                    backup via 20.171.172.171, Ethernet47, label imp-null(3)
 20019   A[1]
                via M, ::, forward
                    EgressACL: apply
                  via TI-LFA tunnel index 5
                    via 20.57.172.57, Ethernet49/1, label imp-null(3)
                    backup via 20.171.172.171, Ethernet47, label imp-null(3)
 20024   A[1]
                via M, ::, forward
                    EgressACL: apply
                  via TI-LFA tunnel index 5
                    via 20.57.172.57, Ethernet49/1, label imp-null(3)
                    backup via 20.171.172.171, Ethernet47, label imp-null(3)
 20032   A[1]
                via M, ::, forward
                    EgressACL: apply
                  via TI-LFA tunnel index 3
                    via 20.171.172.171, Ethernet47, label imp-null(3)
                    backup via 20.57.172.57, Ethernet49/1, label 30171
 20057   A[1]
                via M, ::, forward
                    EgressACL: apply
                  via TI-LFA tunnel index 5
                    via 20.57.172.57, Ethernet49/1, label imp-null(3)
                    backup via 20.171.172.171, Ethernet47, label imp-null(3)
 20083   A[1]
                via M, ::, forward
                    EgressACL: apply
                  via TI-LFA tunnel index 5
                    via 20.57.172.57, Ethernet49/1, label imp-null(3)
                    backup via 20.171.172.171, Ethernet47, label imp-null(3)
 20171   A[1]
                via M, ::, pop
                    EgressACL: apply
                  via TI-LFA tunnel index 3
                    via 20.171.172.171, Ethernet47, label imp-null(3)
                    backup via 20.57.172.57, Ethernet49/1, label 30171
 20349   A[1]
                via M, ::, forward
                    EgressACL: apply
                  via TI-LFA tunnel index 5
                    via 20.57.172.57, Ethernet49/1, label imp-null(3)
                    backup via 20.171.172.171, Ethernet47, label imp-null(3)
 20355   A[1]
                via M, ::, forward
                    EgressACL: apply
                  via TI-LFA tunnel index 5
                    via 20.57.172.57, Ethernet49/1, label imp-null(3)
                    backup via 20.171.172.171, Ethernet47, label imp-null(3)
 20379   A[1]
                via M, ::, forward
                    EgressACL: apply
                  via TI-LFA tunnel index 5
                    via 20.57.172.57, Ethernet49/1, label imp-null(3)
                    backup via 20.171.172.171, Ethernet47, label imp-null(3)
 21105   A[1]
                via M, ::, forward
                    EgressACL: apply
                  via TI-LFA tunnel index 5
                    via 20.57.172.57, Ethernet49/1, label imp-null(3)
                    backup via 20.171.172.171, Ethernet47, label imp-null(3)
 21119   A[1]
                via M, ::, forward
                    EgressACL: apply
                  via TI-LFA tunnel index 5
                    via 20.57.172.57, Ethernet49/1, label imp-null(3)
                    backup via 20.171.172.171, Ethernet47, label imp-null(3)
 21124   A[1]
                via M, ::, forward
                    EgressACL: apply
                  via TI-LFA tunnel index 5
                    via 20.57.172.57, Ethernet49/1, label imp-null(3)
                    backup via 20.171.172.171, Ethernet47, label imp-null(3)
 21157   A[1]
                via M, ::, forward
                    EgressACL: apply
                  via TI-LFA tunnel index 5
                    via 20.57.172.57, Ethernet49/1, label imp-null(3)
                    backup via 20.171.172.171, Ethernet47, label imp-null(3)
 21205   A[1]
                via M, ::, forward
                    EgressACL: apply
                  via TI-LFA tunnel index 5
                    via 20.57.172.57, Ethernet49/1, label imp-null(3)
                    backup via 20.171.172.171, Ethernet47, label imp-null(3)
 21219   A[1]
                via M, ::, forward
                    EgressACL: apply
                  via TI-LFA tunnel index 5
                    via 20.57.172.57, Ethernet49/1, label imp-null(3)
                    backup via 20.171.172.171, Ethernet47, label imp-null(3)
 21224   A[1]
                via M, ::, forward
                    EgressACL: apply
                  via TI-LFA tunnel index 5
                    via 20.57.172.57, Ethernet49/1, label imp-null(3)
                    backup via 20.171.172.171, Ethernet47, label imp-null(3)
 21257   A[1]
                via M, ::, forward
                    EgressACL: apply
                  via TI-LFA tunnel index 5
                    via 20.57.172.57, Ethernet49/1, label imp-null(3)
                    backup via 20.171.172.171, Ethernet47, label imp-null(3)
 21271   A[1]
                via M, pop
                    EgressACL: apply
                    20.171.172.171 Ethernet47
 21357   A[1]
                via M, forward
                    EgressACL: apply
                    20.57.172.57 Ethernet49/1
 21371   A[1]
                via M, ::, pop
                    EgressACL: apply
                  via TI-LFA tunnel index 3
                    via 20.171.172.171, Ethernet47, label imp-null(3)
                    backup via 20.57.172.57, Ethernet49/1, label 30171
 21449   A[1]
                via M, ::, forward
                    EgressACL: apply
                  via TI-LFA tunnel index 5
                    via 20.57.172.57, Ethernet49/1, label imp-null(3)
                    backup via 20.171.172.171, Ethernet47, label imp-null(3)
 21455   A[1]
                via M, ::, forward
                    EgressACL: apply
                  via TI-LFA tunnel index 5
                    via 20.57.172.57, Ethernet49/1, label imp-null(3)
                    backup via 20.171.172.171, Ethernet47, label imp-null(3)
 21471   A[1]
                via M, ::, pop
                    EgressACL: apply
                  via TI-LFA tunnel index 3
                    via 20.171.172.171, Ethernet47, label imp-null(3)
                    backup via 20.57.172.57, Ethernet49/1, label 30171
 21549   A[1]
                via M, ::, forward
                    EgressACL: apply
                  via TI-LFA tunnel index 5
                    via 20.57.172.57, Ethernet49/1, label imp-null(3)
                    backup via 20.171.172.171, Ethernet47, label imp-null(3)
 21555   A[1]
                via M, ::, forward
                    EgressACL: apply
                  via TI-LFA tunnel index 5
                    via 20.57.172.57, Ethernet49/1, label imp-null(3)
                    backup via 20.171.172.171, Ethernet47, label imp-null(3)
 378528   [0]
                via I, ipv4, vrf OSPF-SR-L3VPN
 411296  A[1]
                via M, 20.171.172.171, pop
                    EgressACL: apply
                    directly connected, Ethernet47
                    2c:dd:e9:96:1a:b3, vlan 1010
 411297  A[1]
                via M, 20.57.172.57, pop
                    EgressACL: apply
                    directly connected, Ethernet49/1
                    c0:14:b8:21:ca:6d, vlan 1009
```

## show mpls lfib route

```text
MPLS forwarding table (Label [metric] Vias) - 29 routes 
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
                via TI-LFA tunnel index 5, forward
                 payload autoDecide, ttlMode uniform, dscpMode uniform, apply egress-acl
                    via 20.57.172.57, Ethernet49/1, label imp-null(3)
                    backup via 20.171.172.171, Ethernet47, label imp-null(3)
 IP    20019    [1], 10.0.0.19/32
                via TI-LFA tunnel index 5, forward
                 payload autoDecide, ttlMode uniform, dscpMode uniform, apply egress-acl
                    via 20.57.172.57, Ethernet49/1, label imp-null(3)
                    backup via 20.171.172.171, Ethernet47, label imp-null(3)
 IP    20024    [1], 10.0.0.24/32
                via TI-LFA tunnel index 5, forward
                 payload autoDecide, ttlMode uniform, dscpMode uniform, apply egress-acl
                    via 20.57.172.57, Ethernet49/1, label imp-null(3)
                    backup via 20.171.172.171, Ethernet47, label imp-null(3)
 IP    20032    [1], 10.0.0.32/32
                via TI-LFA tunnel index 3, forward
                 payload autoDecide, ttlMode uniform, dscpMode uniform, apply egress-acl
                    via 20.171.172.171, Ethernet47, label imp-null(3)
                    backup via 20.57.172.57, Ethernet49/1, label 30171
 IP    20057    [1], 10.0.0.57/32
                via TI-LFA tunnel index 5, forward
                 payload autoDecide, ttlMode uniform, dscpMode uniform, apply egress-acl
                    via 20.57.172.57, Ethernet49/1, label imp-null(3)
                    backup via 20.171.172.171, Ethernet47, label imp-null(3)
 IP    20083    [1], 10.0.0.83/32
                via TI-LFA tunnel index 5, forward
                 payload autoDecide, ttlMode uniform, dscpMode uniform, apply egress-acl
                    via 20.57.172.57, Ethernet49/1, label imp-null(3)
                    backup via 20.171.172.171, Ethernet47, label imp-null(3)
 IP    20171    [1], 10.0.0.171/32
                via TI-LFA tunnel index 3, pop
                 payload autoDecide, ttlMode uniform, dscpMode uniform, apply egress-acl
                    via 20.171.172.171, Ethernet47, label imp-null(3)
                    backup via 20.57.172.57, Ethernet49/1, label 30171
 IP    20349    [1], 10.0.1.49/32
                via TI-LFA tunnel index 5, forward
                 payload autoDecide, ttlMode uniform, dscpMode uniform, apply egress-acl
                    via 20.57.172.57, Ethernet49/1, label imp-null(3)
                    backup via 20.171.172.171, Ethernet47, label imp-null(3)
 IP    20355    [1], 10.0.1.55/32
                via TI-LFA tunnel index 5, forward
                 payload autoDecide, ttlMode uniform, dscpMode uniform, apply egress-acl
                    via 20.57.172.57, Ethernet49/1, label imp-null(3)
                    backup via 20.171.172.171, Ethernet47, label imp-null(3)
 IP    20379    [1], 10.0.0.179/32
                via TI-LFA tunnel index 5, forward
                 payload autoDecide, ttlMode uniform, dscpMode uniform, apply egress-acl
                    via 20.57.172.57, Ethernet49/1, label imp-null(3)
                    backup via 20.171.172.171, Ethernet47, label imp-null(3)
 IP    21105    [1], 10.0.0.5/32, algorithm MIN-TE
                via TI-LFA tunnel index 5, forward
                 payload autoDecide, ttlMode uniform, dscpMode uniform, apply egress-acl
                    via 20.57.172.57, Ethernet49/1, label imp-null(3)
                    backup via 20.171.172.171, Ethernet47, label imp-null(3)
 IP    21119    [1], 10.0.0.19/32, algorithm MIN-TE
                via TI-LFA tunnel index 5, forward
                 payload autoDecide, ttlMode uniform, dscpMode uniform, apply egress-acl
                    via 20.57.172.57, Ethernet49/1, label imp-null(3)
                    backup via 20.171.172.171, Ethernet47, label imp-null(3)
 IP    21124    [1], 10.0.0.24/32, algorithm MIN-TE
                via TI-LFA tunnel index 5, forward
                 payload autoDecide, ttlMode uniform, dscpMode uniform, apply egress-acl
                    via 20.57.172.57, Ethernet49/1, label imp-null(3)
                    backup via 20.171.172.171, Ethernet47, label imp-null(3)
 IP    21157    [1], 10.0.0.57/32, algorithm MIN-TE
                via TI-LFA tunnel index 5, forward
                 payload autoDecide, ttlMode uniform, dscpMode uniform, apply egress-acl
                    via 20.57.172.57, Ethernet49/1, label imp-null(3)
                    backup via 20.171.172.171, Ethernet47, label imp-null(3)
 IP    21205    [1], 10.0.0.5/32, algorithm MIN-IGP
                via TI-LFA tunnel index 5, forward
                 payload autoDecide, ttlMode uniform, dscpMode uniform, apply egress-acl
                    via 20.57.172.57, Ethernet49/1, label imp-null(3)
                    backup via 20.171.172.171, Ethernet47, label imp-null(3)
 IP    21219    [1], 10.0.0.19/32, algorithm MIN-IGP
                via TI-LFA tunnel index 5, forward
                 payload autoDecide, ttlMode uniform, dscpMode uniform, apply egress-acl
                    via 20.57.172.57, Ethernet49/1, label imp-null(3)
                    backup via 20.171.172.171, Ethernet47, label imp-null(3)
 IP    21224    [1], 10.0.0.24/32, algorithm MIN-IGP
                via TI-LFA tunnel index 5, forward
                 payload autoDecide, ttlMode uniform, dscpMode uniform, apply egress-acl
                    via 20.57.172.57, Ethernet49/1, label imp-null(3)
                    backup via 20.171.172.171, Ethernet47, label imp-null(3)
 IP    21257    [1], 10.0.0.57/32, algorithm MIN-IGP
                via TI-LFA tunnel index 5, forward
                 payload autoDecide, ttlMode uniform, dscpMode uniform, apply egress-acl
                    via 20.57.172.57, Ethernet49/1, label imp-null(3)
                    backup via 20.171.172.171, Ethernet47, label imp-null(3)
 IP    21271    [1], 10.0.0.171/32, algorithm MIN-TE
                via M, 20.171.172.171, pop
                 payload autoDecide, ttlMode uniform, dscpMode uniform, apply egress-acl
                 interface Ethernet47
 IP    21357    [1], 10.0.0.57/32, algorithm MIN-IGP-ADMIN
                via M, 20.57.172.57, forward
                 payload autoDecide, ttlMode uniform, dscpMode uniform, apply egress-acl
                 interface Ethernet49/1
 IP    21371    [1], 10.0.0.171/32, algorithm MIN-IGP
                via TI-LFA tunnel index 3, pop
                 payload autoDecide, ttlMode uniform, dscpMode uniform, apply egress-acl
                    via 20.171.172.171, Ethernet47, label imp-null(3)
                    backup via 20.57.172.57, Ethernet49/1, label 30171
 IP    21449    [1], 10.0.1.49/32, algorithm MIN-TE
                via TI-LFA tunnel index 5, forward
                 payload autoDecide, ttlMode uniform, dscpMode uniform, apply egress-acl
                    via 20.57.172.57, Ethernet49/1, label imp-null(3)
                    backup via 20.171.172.171, Ethernet47, label imp-null(3)
 IP    21455    [1], 10.0.1.55/32, algorithm MIN-TE
                via TI-LFA tunnel index 5, forward
                 payload autoDecide, ttlMode uniform, dscpMode uniform, apply egress-acl
                    via 20.57.172.57, Ethernet49/1, label imp-null(3)
                    backup via 20.171.172.171, Ethernet47, label imp-null(3)
 IP    21471    [1], 10.0.0.171/32, algorithm MIN-IGP-ADMIN
                via TI-LFA tunnel index 3, pop
                 payload autoDecide, ttlMode uniform, dscpMode uniform, apply egress-acl
                    via 20.171.172.171, Ethernet47, label imp-null(3)
                    backup via 20.57.172.57, Ethernet49/1, label 30171
 IP    21549    [1], 10.0.1.49/32, algorithm MIN-IGP
                via TI-LFA tunnel index 5, forward
                 payload autoDecide, ttlMode uniform, dscpMode uniform, apply egress-acl
                    via 20.57.172.57, Ethernet49/1, label imp-null(3)
                    backup via 20.171.172.171, Ethernet47, label imp-null(3)
 IP    21555    [1], 10.0.1.55/32, algorithm MIN-IGP
                via TI-LFA tunnel index 5, forward
                 payload autoDecide, ttlMode uniform, dscpMode uniform, apply egress-acl
                    via 20.57.172.57, Ethernet49/1, label imp-null(3)
                    backup via 20.171.172.171, Ethernet47, label imp-null(3)
 B3    378528   [0]
                via I, ipv4, vrf OSPF-SR-L3VPN
 IA    411296   [1]
                via M, 20.171.172.171, pop
                 payload autoDecide, ttlMode uniform, apply egress-acl
                 interface Ethernet47
 IA    411297   [1]
                via M, 20.57.172.57, pop
                 payload autoDecide, ttlMode uniform, apply egress-acl
                 interface Ethernet49/1
```

## show ip ospf segment-routing

```text
OSPF Instance ID: 1
SR supported Data-plane: MPLS			SR Router ID: 10.0.0.172
SR Global Block( SRGB ): Base: 20000           	Size: 2000            

OSPF Reachability Algorithm : SPF (0)

Number of OSPF segment routing capable nodes excluding self: 0

Self-Originated Segment Statistics:
Node-Segments       : 1
Prefix-Segments     : 0
Proxy-Node-Segments : 0
Adjacency Segments  : 0

```

## show ip ospf segment-routing global-blocks

```text
OSPF Instance ID: 1
SR supported Data-plane: MPLS			SR Router ID: 10.0.0.172
Number of OSPF segment routing capable nodes excluding self: 0

    Router ID        Base    Size
---------------- ----------- ----
   10.0.0.172       20000    2000

```

## show ip ospf segment-routing bindings

```text
10.0.0.172/32
   Local binding:  Label: imp-null
```

## show bgp evpn

```text
BGP routing table information for VRF default
Router identifier 10.0.0.172, local AS number 65000
Route status codes: * - valid, > - active, S - Stale, E - ECMP head, e - ECMP
                    c - Contributing to ECMP, % - Pending best path selection
Origin codes: i - IGP, e - EGP, ? - incomplete
AS Path Attributes: Or-ID - Originator ID, C-LST - Cluster List, LL Nexthop - Link Local Nexthop

          Network                Next Hop              Metric  LocPref Weight  Path
```

## show bgp vpn-ipv4

```text
BGP routing table information for VRF default
Router identifier 10.0.0.172, local AS number 65000
Route status codes: s - suppressed contributor, * - valid, > - active, E - ECMP head, e - ECMP
                    S - Stale, c - Contributing to ECMP, b - backup, L - labeled-unicast
                    % - Pending best path selection
Origin codes: i - IGP, e - EGP, ? - incomplete
AS Path Attributes: Or-ID - Originator ID, C-LST - Cluster List, LL Nexthop - Link Local Nexthop

          Network                Next Hop              Metric  LocPref Weight  Path
 * >      RD: 10.0.0.172:2 IPv4 prefix 20.111.172.0/24
                                 -                     -       -       0       i
```

## show bgp vpn-ipv6

```text
BGP routing table information for VRF default
Router identifier 10.0.0.172, local AS number 65000
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
Router identifier 10.0.0.172, local AS number 65000
Route status codes: s - suppressed contributor, * - valid, > - active, E - ECMP head, e - ECMP
                    S - Stale, c - Contributing to ECMP, b - backup, L - labeled-unicast
                    % - Pending best path selection
Origin codes: i - IGP, e - EGP, ? - incomplete
AS Path Attributes: Or-ID - Originator ID, C-LST - Cluster List, LL Nexthop - Link Local Nexthop

          Network                Next Hop              Metric  AIGP       LocPref Weight  Path
```

## show bgp neighbors

```text
BGP neighbor is 10.0.0.211, remote AS 65000, internal link
  BGP version 4, remote router ID 0.0.0.0, VRF default
  Inherits configuration from and member of peer-group IBGP-PEER
  Last read never, last write never
  Hold time is 0, keepalive interval is 0 seconds
  Configured hold time is 180, keepalive interval is 60 seconds
  Effective minimum hold time is 3 seconds
  Send failure hold time is 0 seconds
  Hold timer is inactive
  Keepalive timer is inactive
  Connect timer is active, time left: 00:01:56
  Connection interval is 148 seconds
  Failed connection attempts is 451
  Idle-restart timer is inactive
  BGP state is Active
  Number of transitions to established: 0
  Last state was Connect
  Last event was TransportError
  Last sent socket-error:Connect (Network is unreachable), Last time 00:00:43, First time 20:57:48, Repeats 450
  Types of communities advertised: standard extended large
  Neighbor Capabilities:
  Restart timer is inactive
  End of rib timer is inactive
  AIGP attribute send and receive for IPv4 Unicast are enabled
  AIGP attribute send and receive for IPv4 with MPLS Labels are enabled
  AIGP attribute send and receive for IPv6 Unicast are enabled
  AIGP attribute send and receive for IPv6 with MPLS Labels are enabled
  BGP session driven failover for IPv6 Unicast is disabled
  BGP session driven failover for IPv4 Unicast is disabled
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
Local AS is 65000, local router ID 10.0.0.172
TTL is 255
Local TCP address is 10.0.0.172
Remote TCP address is 10.0.0.211, remote port is 179

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
  Connect timer is active, time left: 00:01:51
  Connection interval is 148 seconds
  Failed connection attempts is 13
  Idle-restart timer is inactive
  BGP state is Active
  Number of transitions to established: 0
  Last state was Connect
  Last event was TransportError
  Last sent socket-error:Connect (Connection refused), Last time 00:01:11, First time 00:16:15, Repeats 11
  Types of communities advertised: standard extended large
  Neighbor Capabilities:
  Restart timer is inactive
  End of rib timer is inactive
  AIGP attribute send and receive for IPv4 Unicast are enabled
  AIGP attribute send and receive for IPv4 with MPLS Labels are enabled
  AIGP attribute send and receive for IPv6 Unicast are enabled
  AIGP attribute send and receive for IPv6 with MPLS Labels are enabled
  BGP session driven failover for IPv6 Unicast is disabled
  BGP session driven failover for IPv4 Unicast is disabled
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
Local AS is 65000, local router ID 10.0.0.172
TTL is 255
Local TCP address is 10.0.0.172
Remote TCP address is 10.0.1.49, remote port is 179

```

## show tunnel rib system-tunnel-rib brief

```text
Tunnel RIB: system-tunnel-rib
Endpoint        Tunnel Type     Index(es)   Tunnel Preference   IGP Preference 
-------------- --------------- ----------- ------------------- ----------------
10.0.0.5/32     IS-IS SR IPv4   8           65                  115            
10.0.0.19/32    IS-IS SR IPv4   3           65                  115            
10.0.0.24/32    IS-IS SR IPv4   7           65                  115            
10.0.0.32/32    IS-IS SR IPv4   10          65                  115            
10.0.0.57/32    IS-IS SR IPv4   5           65                  115            
10.0.0.83/32    IS-IS SR IPv4   1           65                  115            
10.0.0.171/32   IS-IS SR IPv4   9           65                  115            
10.0.0.179/32   IS-IS SR IPv4   6           65                  115            
10.0.1.49/32    IS-IS SR IPv4   2           65                  115            
10.0.1.55/32    IS-IS SR IPv4   4           65                  115            

   IGP Metric    Metric Type
---------------- -----------
   40            metric     
   30            metric     
   30            metric     
   20            metric     
   10            metric     
   30            metric     
   10            metric     
   40            metric     
   20            metric     
   30            metric     

```

## show tunnel rib colored brief

```text
Tunnel RIB: system-colored-tunnel-rib
 Endpoint        Color   Tunnel Type       Index(es)    Tunnel Preference    IGP Preference    IGP Metric   Metric Type
--------------- ------- ----------------- ------------ -------------------- ----------------- ------------- -----------
 10.0.0.5/32     129     IS-IS FlexAlgo    15           65                   115               36           metric     
 10.0.0.5/32     130     IS-IS FlexAlgo    19           65                   115               30           metric     
 10.0.0.19/32    129     IS-IS FlexAlgo    17           65                   115               36           metric     
 10.0.0.19/32    130     IS-IS FlexAlgo    24           65                   115               30           metric     
 10.0.0.24/32    129     IS-IS FlexAlgo    14           65                   115               36           metric     
 10.0.0.24/32    130     IS-IS FlexAlgo    23           65                   115               30           metric     
 10.0.0.57/32    129     IS-IS FlexAlgo    12           65                   115               12           metric     
 10.0.0.57/32    130     IS-IS FlexAlgo    10           65                   115               10           metric     
 10.0.0.57/32    131     IS-IS FlexAlgo    13           65                   115               10           metric     
 10.0.0.171/32   129     IS-IS FlexAlgo    8            65                   115               12           metric     
 10.0.0.171/32   130     IS-IS FlexAlgo    6            65                   115               10           metric     
 10.0.0.171/32   131     IS-IS FlexAlgo    16           65                   115               10           metric     
 10.0.1.49/32    129     IS-IS FlexAlgo    2            65                   115               24           metric     
 10.0.1.49/32    130     IS-IS FlexAlgo    20           65                   115               20           metric     
 10.0.1.55/32    129     IS-IS FlexAlgo    21           65                   115               36           metric     
 10.0.1.55/32    130     IS-IS FlexAlgo    4            65                   115               30           metric     

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
>C    10.0.0.172/32 [0 pref/0 metric] updated 20:58:05 ago
         via Loopback0, directly connected
>C    20.57.172.0/24 [0 pref/0 metric] updated 03:47:18 ago
         via Ethernet49/1, directly connected
>C    20.171.172.0/24 [0 pref/0 metric] updated 03:36:04 ago
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
>P    0.0.0.0/8 [1 pref/0 metric] updated 20:58:03 ago
         via Null0, directly connected [NF]
>P    127.0.0.0/8 [1 pref/0 metric] updated 20:58:03 ago
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
>I    10.0.0.5/32 [115 pref/40 metric] updated 00:16:17 ago
         via 20.57.172.57, Ethernet49/1
>I    10.0.0.19/32 [115 pref/30 metric] updated 00:16:17 ago
         via 20.57.172.57, Ethernet49/1
>I    10.0.0.24/32 [115 pref/30 metric] updated 00:16:17 ago
         via 20.57.172.57, Ethernet49/1
>I    10.0.0.32/32 [115 pref/20 metric] updated 00:00:28 ago
         via 20.171.172.171, Ethernet47
>I    10.0.0.57/32 [115 pref/10 metric] updated 03:34:42 ago
         via 20.57.172.57, Ethernet49/1
>I    10.0.0.83/32 [115 pref/30 metric] updated 00:16:17 ago
         via 20.57.172.57, Ethernet49/1
>I    10.0.0.171/32 [115 pref/10 metric] updated 03:35:31 ago
         via 20.171.172.171, Ethernet47
>I    10.0.0.179/32 [115 pref/40 metric] updated 00:05:43 ago
         via 20.57.172.57, Ethernet49/1
>I    10.0.0.254/32 [115 pref/30 metric] updated 00:05:43 ago
         via 20.57.172.57, Ethernet49/1
>I    10.0.1.49/32 [115 pref/20 metric] updated 00:16:17 ago
         via 20.57.172.57, Ethernet49/1
>I    10.0.1.55/32 [115 pref/30 metric] updated 00:16:17 ago
         via 20.57.172.57, Ethernet49/1
>I    20.5.149.0/24 [115 pref/30 metric] updated 00:16:17 ago
         via 20.57.172.57, Ethernet49/1
>I    20.19.149.0/24 [115 pref/30 metric] updated 00:16:17 ago
         via 20.57.172.57, Ethernet49/1
>I    20.24.149.0/24 [115 pref/30 metric] updated 00:16:17 ago
         via 20.57.172.57, Ethernet49/1
>I    20.32.149.0/24 [115 pref/30 metric] updated 00:00:28 ago
         via 20.171.172.171, Ethernet47
>I    20.32.171.0/24 [115 pref/20 metric] updated 01:13:11 ago
         via 20.171.172.171, Ethernet47
>I    20.32.211.0/24 [115 pref/30 metric] updated 00:00:28 ago
         via 20.171.172.171, Ethernet47
>I    20.47.149.0/24 [115 pref/30 metric] updated 00:16:17 ago
         via 20.57.172.57, Ethernet49/1
>I    20.57.149.0/24 [115 pref/20 metric] updated 00:16:22 ago
         via 20.57.172.57, Ethernet49/1
>I    20.57.155.0/24 [115 pref/40 metric] updated 00:16:17 ago
         via 20.57.172.57, Ethernet49/1
>I    20.57.171.0/24 [115 pref/20 metric] updated 00:31:09 ago
         via 20.171.172.171, Ethernet47
>I    20.57.179.0/24 [115 pref/50 metric] updated 00:05:43 ago
         via 20.57.172.57, Ethernet49/1
>I    20.57.254.0/24 [115 pref/40 metric] updated 00:05:43 ago
         via 20.57.172.57, Ethernet49/1
>I    20.83.149.0/24 [115 pref/30 metric] updated 00:16:17 ago
         via 20.57.172.57, Ethernet49/1
>I    20.111.149.0/24 [115 pref/30 metric] updated 00:16:17 ago
         via 20.57.172.57, Ethernet49/1
>I    20.149.155.0/24 [115 pref/30 metric] updated 00:16:17 ago
         via 20.57.172.57, Ethernet49/1
>I    20.149.254.0/24 [115 pref/30 metric] updated 00:05:45 ago
         via 20.57.172.57, Ethernet49/1
>I    20.179.254.0/24 [115 pref/40 metric] updated 00:05:43 ago
         via 20.57.172.57, Ethernet49/1
>I    192.168.0.0/19 [115 pref/30 metric] updated 00:16:17 ago
         via 20.57.172.57, Ethernet49/1
>I    192.168.20.0/23 [115 pref/30 metric] updated 00:16:17 ago
         via 20.57.172.57, Ethernet49/1
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
>P    ::/96 [1 pref/0 metric] updated 20:58:03 ago
         via Null0, directly connected [NF]
>P    ::ffff:127.0.0.0/104 [1 pref/0 metric] updated 20:58:03 ago
         via :: [1 pref/1 metric] type ipv6
            via , directly connected
>P    fe80::/10 [1 pref/0 metric] updated 20:58:03 ago
```

## show platform sand l3 summary

```text
Number of vrfs: 8

Ipv4:
  Routes:       58  backlog:  0  unprogrammed:  0
  Adjacencies:  32  backlog:  0  unprogrammed:  0
Ipv6:
  Routes:       4   backlog:  0  unprogrammed:  0
  Adjacencies:  32  backlog:  0  unprogrammed:  0
Mpls:
  Routes:       28  backlog:  0  unprogrammed:  0
  Adjacencies:  2   backlog:  0  unprogrammed:  0

Jericho2 Ip Fecs:
  Non-ecmp fecs:  4108  ecmp fecs:  0  fec entries:  4108
Jericho2 Mpls Fecs:
  Non-ecmp fecs:  2  ecmp fecs:  0  fec entries:  2
Jericho2 Vxlan Tunnel Fecs:
  Non-ecmp fecs:  0  ecmp fecs:  0  fec entries:  0
  Number of vxlan tunnels configured: 0

Jericho2 Lpm Routes:
  Routes:   58  unprogrammed:   0   
  Routes6:  4   unprogrammed6:  0   
  Backlog:  0 

Jericho2 Lpm:
  TCAM entries used:   3   Percent free:  99  ADS2 entries used:   4  Percent free:  99
  Pivot buckets used:  4   Rows used:     1   Entries Per Bucket:  1  Percent free:  99
  Route buckets used:  10  Rows used:     3   Entries Per Bucket:  6  Percent free:  99

Lem:
  IPv4  Host in Lem:            disabled
  IPv4  Prefix-lengths in Lem:  None    
  IPv6  Host in Lem:            disabled
  IPv6  Prefix-lengths in Lem:  None    
  Number of downloads:        0
  Number of overflow events:  0

Egress Arp rewrite entries in use (in each fap):
  FixedSystem: 2
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

Glem entries used per fap :
  FixedSystem: 4098

Jericho2 Fec:
  Maximum FEC hierarchy levels:  3
  ReusedEcmp:  0  allocs:  54  frees:  42  shuffles:  0  cmds:  0
  Zombies:     0    purges:    0
  Quarantine:  0/0  shuffles:  0  deletes:  0   
  Fec insertion failures:  0
  Level1  Fecs:
    Non-ecmp fecs:            0    ecmp fecs:            1 
    Non-ecmp (Percent free):  100  ecmp (Percent free):  99
  Level2  Fecs:
    Non-ecmp fecs:            12  ecmp fecs:            0  
    Non-ecmp (Percent free):  99  ecmp (Percent free):  100
  Level3  Fecs:
    Non-ecmp fecs:            0    ecmp fecs:            0  
    Non-ecmp (Percent free):  100  ecmp (Percent free):  100

Lpm Detail:
  Requests:  305  cleanses:  106  batches:  106  avg batch size:  2

Jericho Arp:
  ArpTable writes:      16839  queued      0   
  IngressTable writes:  75059  queued      0   
  Coprocessors:         1      in CmdRing

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
|0  |0.0.0.0/8         |DROP | DROP               |0    |  -     |                   |  -  |288360|   -   
|0  |10.0.0.5/32       |ROUTE| Et49/1             |1009 |103422  | c0:14:b8:21:ca:6d |  -  |288370|   -   
|0  |10.0.0.19/32      |ROUTE| Et49/1             |1009 |103422  | c0:14:b8:21:ca:6d |  -  |288370|   -   
|0  |10.0.0.24/32      |ROUTE| Et49/1             |1009 |103422  | c0:14:b8:21:ca:6d |  -  |288370|   -   
|0  |10.0.0.32/32      |ROUTE| Et47               |1010 |103421  | 2c:dd:e9:96:1a:b3 |  -  |288365|   -   
|0  |10.0.0.57/32      |ROUTE| Et49/1             |1009 |103422  | c0:14:b8:21:ca:6d |  -  |288370|   -   
|0  |10.0.0.83/32      |ROUTE| Et49/1             |1009 |103422  | c0:14:b8:21:ca:6d |  -  |288370|   -   
|0  |10.0.0.171/32     |ROUTE| Et47               |1010 |103421  | 2c:dd:e9:96:1a:b3 |  -  |288365|   -   
|0  |10.0.0.172/32     |TRAP | CoppSystemIpUcast  |0    |  -     | Receive           |  -  |524291|   -   
|0  |10.0.0.179/32     |ROUTE| Et49/1             |1009 |103422  | c0:14:b8:21:ca:6d |  -  |288370|   -   
|0  |10.0.0.254/32     |ROUTE| Et49/1             |1009 |103422  | c0:14:b8:21:ca:6d |  -  |288370|   -   
|0  |10.0.1.49/32      |ROUTE| Et49/1             |1009 |103422  | c0:14:b8:21:ca:6d |  -  |288370|   -   
|0  |10.0.1.55/32      |ROUTE| Et49/1             |1009 |103422  | c0:14:b8:21:ca:6d |  -  |288370|   -   
|0  |20.5.149.0/24     |ROUTE| Et49/1             |1009 |103422  | c0:14:b8:21:ca:6d |  -  |288370|   -   
|0  |20.19.149.0/24    |ROUTE| Et49/1             |1009 |103422  | c0:14:b8:21:ca:6d |  -  |288370|   -   
|0  |20.24.149.0/24    |ROUTE| Et49/1             |1009 |103422  | c0:14:b8:21:ca:6d |  -  |288370|   -   
|0  |20.32.149.0/24    |ROUTE| Et47               |1010 |103421  | 2c:dd:e9:96:1a:b3 |  -  |288365|   -   
|0  |20.32.171.0/24    |ROUTE| Et47               |1010 |103421  | 2c:dd:e9:96:1a:b3 |  -  |288365|   -   
|0  |20.32.211.0/24    |ROUTE| Et47               |1010 |103421  | 2c:dd:e9:96:1a:b3 |  -  |288365|   -   
|0  |20.47.149.0/24    |ROUTE| Et49/1             |1009 |103422  | c0:14:b8:21:ca:6d |  -  |288370|   -   
|0  |20.57.149.0/24    |ROUTE| Et49/1             |1009 |103422  | c0:14:b8:21:ca:6d |  -  |288370|   -   
|0  |20.57.155.0/24    |ROUTE| Et49/1             |1009 |103422  | c0:14:b8:21:ca:6d |  -  |288370|   -   
|0  |20.57.171.0/24    |ROUTE| Et47               |1010 |103421  | 2c:dd:e9:96:1a:b3 |  -  |288365|   -   
|0  |20.57.172.0/32    |TRAP | CoppSystemIpBcast  |0    |  -     | BcastReceive      |  -  |524288|   -   
|0  |20.57.172.57/32   |ROUTE| Et49/1             |1009 |103422  | c0:14:b8:21:ca:6d |  -  |288367|   -   
|0  |20.57.172.172/32  |TRAP | CoppSystemIpUcast  |0    |  -     | Receive           |  -  |524291|   -   
|0  |20.57.172.255/32  |TRAP | CoppSystemIpBcast  |0    |  -     | BcastReceive      |  -  |524288|   -   
|0  |20.57.172.0/24    |TRAP | CoppSystemL3DstMiss|1009 |1009    | ArpTrap           |  -  |525303|   -   
|0  |20.57.179.0/24    |ROUTE| Et49/1             |1009 |103422  | c0:14:b8:21:ca:6d |  -  |288370|   -   
|0  |20.57.254.0/24    |ROUTE| Et49/1             |1009 |103422  | c0:14:b8:21:ca:6d |  -  |288370|   -   
|0  |20.83.149.0/24    |ROUTE| Et49/1             |1009 |103422  | c0:14:b8:21:ca:6d |  -  |288370|   -   
|0  |20.111.149.0/24   |ROUTE| Et49/1             |1009 |103422  | c0:14:b8:21:ca:6d |  -  |288370|   -   
|0  |20.149.155.0/24   |ROUTE| Et49/1             |1009 |103422  | c0:14:b8:21:ca:6d |  -  |288370|   -   
|0  |20.149.254.0/24   |ROUTE| Et49/1             |1009 |103422  | c0:14:b8:21:ca:6d |  -  |288370|   -   
|0  |20.171.172.0/32   |TRAP | CoppSystemIpBcast  |0    |  -     | BcastReceive      |  -  |524288|   -   
|0  |20.171.172.171/32 |ROUTE| Et47               |1010 |103421  | 2c:dd:e9:96:1a:b3 |  -  |288364|   -   
|0  |20.171.172.172/32 |TRAP | CoppSystemIpUcast  |0    |  -     | Receive           |  -  |524291|   -   
|0  |20.171.172.255/32 |TRAP | CoppSystemIpBcast  |0    |  -     | BcastReceive      |  -  |524288|   -   
|0  |20.171.172.0/24   |TRAP | CoppSystemL3DstMiss|1010 |1010    | ArpTrap           |  -  |525304|   -   
|0  |20.179.254.0/24   |ROUTE| Et49/1             |1009 |103422  | c0:14:b8:21:ca:6d |  -  |288370|   -   
|0  |127.0.0.0/8       |TRAP | CoppSystemL3DstMiss|0    |  -     | ArpTrap           |  -  |524294|   -   
|0  |192.168.20.0/23   |ROUTE| Et49/1             |1009 |103422  | c0:14:b8:21:ca:6d |  -  |288370|   -   
|0  |192.168.0.0/19    |ROUTE| Et49/1             |1009 |103422  | c0:14:b8:21:ca:6d |  -  |288370|   -   
|0  |0.0.0.0/0         |TRAP | CoppSystemL3LpmOver|0    |  -     | SlowReceive       |  -  |524292|   -   
|1  |0.0.0.0/8         |DROP | DROP               |0    |  -     |                   |  -  |288362|   -   
|1  |127.0.0.0/8       |TRAP | CoppSystemL3DstMiss|0    |  -     | ArpTrap           |  -  |524294|   -   
|1  |192.168.20.0/32   |TRAP | CoppSystemIpBcast  |0    |  -     | BcastReceive      |  -  |524288|   -   
|1  |192.168.20.172/32 |TRAP | CoppSystemIpUcast  |0    |  -     | Receive           |  -  |524291|   -   
|1  |192.168.21.255/32 |TRAP | CoppSystemIpBcast  |0    |  -     | BcastReceive      |  -  |524288|   -   
|1  |192.168.20.0/23   |TRAP | CoppSystemL3DstMiss|0    |  -     | ArpTrap           |  -  |524294|   -   
|1  |0.0.0.0/0         |TRAP | CoppSystemL3DstMiss|0    |  -     | ArpTrap           |  -  |524294|   -   
|2  |0.0.0.0/8         |DROP | DROP               |0    |  -     |                   |  -  |288363|   -   
|2  |20.111.172.0/32   |TRAP | CoppSystemIpBcast  |0    |  -     | BcastReceive      |  -  |524288|   -   
|2  |20.111.172.172/32 |TRAP | CoppSystemIpUcast  |0    |  -     | Receive           |  -  |524291|   -   
|2  |20.111.172.255/32 |TRAP | CoppSystemIpBcast  |0    |  -     | BcastReceive      |  -  |524288|   -   
|2  |20.111.172.0/24   |TRAP | CoppSystemL3DstMiss|1006 |1006    | ArpTrap           |  -  |525300|   -   
|2  |127.0.0.0/8       |TRAP | CoppSystemL3DstMiss|0    |  -     | ArpTrap           |  -  |524294|   -   
|2  |0.0.0.0/0         |TRAP | CoppSystemL3LpmOver|0    |  -     | SlowReceive       |  -  |524292|   -   

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
|  -  |288360|DROP | DROP               |0    |  -     |                   |   -   
|  -  |288361|DROP | DROP               |0    |  -     |                   |   -   
|  -  |288362|DROP | DROP               |0    |  -     |                   |   -   
|  -  |288363|DROP | DROP               |0    |  -     |                   |   -   
|  -  |288364|ROUTE| Et47               |1010 |103421  | 2c:dd:e9:96:1a:b3 |   -   
|  -  |288365|ROUTE| Et47               |1010 |103421  | 2c:dd:e9:96:1a:b3 |   -   
|  -  |288366|ROUTE| Et47               |1010 |103421  | 2c:dd:e9:96:1a:b3 |   -   
|  -  |288367|ROUTE| Et49/1             |1009 |103422  | c0:14:b8:21:ca:6d |   -   
|  -  |288370|ROUTE| Et49/1             |1009 |103422  | c0:14:b8:21:ca:6d |   -   
|  -  |288371|ROUTE| Et49/1             |1009 |103422  | c0:14:b8:21:ca:6d |   -   
|  -  |288377|ROUTE| Et49/1             |1009 |103422  | c0:14:b8:21:ca:6d |   -   
|  -  |288378|ROUTE| Et47               |1010 |103421  | 2c:dd:e9:96:1a:b3 |   -   
|  -  |524288|TRAP | CoppSystemIpBcast  |0    |  -     | BcastReceive      |   -   
|  -  |524291|TRAP | CoppSystemIpUcast  |0    |  -     | Receive           |   -   
|  -  |524292|TRAP | CoppSystemL3LpmOver|0    |  -     | SlowReceive       |   -   
|  -  |524294|TRAP | CoppSystemL3DstMiss|0    |  -     | ArpTrap           |   -   
|  -  |525300|TRAP | CoppSystemL3DstMiss|1006 |1006    | ArpTrap           |   -   
|  -  |525303|TRAP | CoppSystemL3DstMiss|1009 |1009    | ArpTrap           |   -   
|  -  |525304|TRAP | CoppSystemL3DstMiss|1010 |1010    | ArpTrap           |   -   

```

