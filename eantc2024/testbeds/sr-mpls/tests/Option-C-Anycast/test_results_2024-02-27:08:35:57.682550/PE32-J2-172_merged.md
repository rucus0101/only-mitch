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

Uptime: 17 hours and 38 minutes
Total memory: 8099732 kB
Free memory: 5557232 kB

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
Interface      IP Address          Status      Protocol            MTU  Owner  
-------------- ------------------- ----------- ---------------- ------- -------
Ethernet5.2    20.111.172.172/24   down        lowerlayerdown     1500         
Ethernet5.171  20.111.172.172/24   down        lowerlayerdown     1500         
Ethernet25     20.149.172.172/24   up          up                 1500         
Ethernet45     20.172.211.172/24   down        notpresent         1500         
Ethernet47     20.171.172.172/24   admin down  down               1500         
Ethernet49/1   20.57.172.172/24    admin down  down               1500         
Ethernet50/1   20.32.172.172/24    admin down  down               1500         
Ethernet51/1   20.47.172.172/24    admin down  down               1500         
Ethernet52/1   20.170.172.172/24   up          up                 1500         
Ethernet55/1   20.19.172.172/24    admin down  down               1500         
Loopback0      10.0.0.172/32       up          up                65535         
Loopback209    209.209.209.209/32  up          up                65535         
Management1    192.168.20.172/23   up          up                 1500         

```

## show interfaces counters rates | nz

```text
Port      Name        Intvl  In Mbps      %  In Kpps Out Mbps      % Out Kpps
Et25      Cisco_349    0:05      0.0   0.0%        0     80.5   0.8%       10
Et52/1    Arista_170   0:05     81.0   0.1%       10      0.0   0.0%        0
Ma1                    0:05      0.0   0.0%        0      0.1   0.0%        0
```

## show isis neighbors

```text
 
Instance  VRF      System Id        Type Interface          SNPA              State Hold time   Circuit Id          
OPTION-C- default  h49-N540-24Q8L2DD L2   Ethernet25         P2P               UP    28          00                  
 
Instance  VRF      System Id        Type Interface          SNPA              State Hold time   Circuit Id          
OPTION-C- default  Spine3-J-170     L2   Ethernet52/1       P2P               UP    29          21                  
```

## show isis database detail

```text
Legend:
H - hostname conflict
U - node unreachable

IS-IS Instance: OPTION-C-DOMAIN-1 VRF: default
  IS-IS Level 2 Link State Database
    LSPID                   Seq Num  Cksum  Life Length IS  Received LSPID        Flags
    h3c_19_CR16010E-F.00-00       203    364  1179    267 L2  0000.0000.0019.00-00  <>
      NLPID: 0xCC(IPv4)
      Hostname: h3c_19_CR16010E-F
      Area addresses: 49
      Interface address: 10.0.0.19
      Interface address: 20.19.149.19
      IS Neighbor          : h49-N540-24Q8L2DD.00 Metric: 10
        IPv4 Neighbor Address: 20.19.149.149
        IPv4 Interface Address: 20.19.149.19
        Adj-sid: 1145 flags: [L V] weight: 0x0
      Reachability         : 10.0.0.19/32 Metric: 0 Type: 1 Up
        SR Prefix-SID: 19 Flags: [N P] Algorithm: 0
      Reachability         : 20.19.149.0/24 Metric: 10 Type: 1 Up
      Reachability         : 31.9.1.0/24 Metric: 0 Type: 1 Up
      Reachability         : 192.168.0.0/19 Metric: 0 Type: 1 Up
      Router Capabilities: Router Id: 10.0.0.19 Flags: []
        Maximum SID depth:
          Base MPLS imposition (MSD type 1):  13
        SR Capability: Flags: [I]
          SRGB Base: 20000 Range: 2000
    h3c_24_S12500R-48C6D.00-00       202   4373  1179    288 L2  0000.0000.0024.00-00  <>
      NLPID: 0xCC(IPv4)
      Hostname: h3c_24_S12500R-48C6D
      Area addresses: 49
      Interface address: 10.0.0.24
      Interface address: 20.24.149.24
      IS Neighbor          : h49-N540-24Q8L2DD.00 Metric: 10
        IPv4 Neighbor Address: 20.24.149.149
        IPv4 Interface Address: 20.24.149.24
        Adj-sid: 56127 flags: [L V] weight: 0x0
      Reachability         : 10.0.0.24/32 Metric: 0 Type: 1 Up
        SR Prefix-SID: 24 Flags: [N P] Algorithm: 0
      Reachability         : 10.0.1.24/32 Metric: 0 Type: 1 Up
      Reachability         : 20.24.149.0/24 Metric: 10 Type: 1 Up
      Reachability         : 192.168.20.0/23 Metric: 0 Type: 1 Up
      Router Capabilities: Router Id: 10.0.0.24 Flags: []
        SR Local Block:
          SRLB Base: 15000 Range: 1000
        Maximum SID depth:
          Base MPLS imposition (MSD type 1):  10
        SR Capability: Flags: [I]
          SRGB Base: 20000 Range: 2000
    Ribbon-32.00-00              80  49506   372     79 L2  0000.0000.0032.00-00  <>
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
    Ribbon-32.00-01              80  65270  1009     38 L2  0000.0000.0032.00-01  <>
      Hostname: Ribbon-32
    Ribbon-32.00-02              83  22315  1000    205 L2  0000.0000.0032.00-02  <>
      Interface address: 10.0.0.32
      Interface address: 20.32.149.32
      Interface address: 209.209.209.209
      IS Neighbor          : h49-N540-24Q8L2DD.00 Metric: 10
        IPv4 Neighbor Address: 20.32.149.149
        IPv4 Interface Address: 20.32.149.32
        Adj-sid: 756640 flags: [L V] weight: 0x0
        Adj-sid: 756641 flags: [L V B] weight: 0x0
      Reachability         : 10.0.0.32/32 Metric: 0 Type: 1 Up
        SR Prefix-SID: 32 Flags: [N] Algorithm: 0
      Reachability         : 20.32.149.0/24 Metric: 10 Type: 1 Up
      Reachability         : 209.209.209.209/32 Metric: 0 Type: 1 Up
        SR Prefix-SID: 209 Flags: [] Algorithm: 0
    R6676-50.00-00              122  33795   588    145 L2  0000.0000.0050.00-00  <>
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
    h43-9901.00-00              123  58457   684    186 L2  0000.0000.0343.00-00  <>
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
    h49-N540-24Q8L2DD.00-00       174  11066   426   1383 L2  0000.0000.0349.00-00  <>
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
      IS Neighbor          : R6676-50.00         Metric: 10
        IPv4 Neighbor Address: 20.50.149.50
        IPv4 Interface Address: 20.50.149.149
        Adj-sid: 24017 flags: [L V] weight: 0x0
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
      IS Neighbor          : PE32-J2-172.00      Metric: 10
        IPv4 Neighbor Address: 20.149.172.172
        IPv4 Interface Address: 20.149.172.149
        Adj-sid: 24006 flags: [L V B] weight: 0x0
        Adj-sid: 24007 flags: [L V] weight: 0x0
      IS Neighbor          : NOKIA-SR2-57.00     Metric: 10
        IPv4 Neighbor Address: 20.57.149.57
        IPv4 Interface Address: 20.57.149.149
        Adj-sid: 24018 flags: [L V B] weight: 0x0
        Adj-sid: 24019 flags: [L V] weight: 0x0
      IS Neighbor          : PE31-J2-171.00      Metric: 10
        IPv4 Neighbor Address: 20.149.171.171
        IPv4 Interface Address: 20.149.171.149
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
      Reachability         : 20.32.149.0/24 Metric: 10 Type: 1 Up
      Reachability         : 20.50.149.0/24 Metric: 10 Type: 1 Up
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
    h49-N540-24Q8L2DD.00-01       135  40666   667    124 L2  0000.0000.0349.00-01  <>
      IS Neighbor          : Ribbon-32.00        Metric: 10
        IPv4 Neighbor Address: 20.32.149.32
        IPv4 Interface Address: 20.32.149.149
        Adj-sid: 24025 flags: [L V] weight: 0x0
    h55-8201-24H8FH.00-00       128  59637  1117    482 L2  0000.0000.0355.00-00  <>
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
      Reachability         : 20.32.155.0/24 Metric: 10 Type: 1 Up
      Reachability         : 20.57.155.0/24 Metric: 10 Type: 1 Up
      Reachability         : 20.149.155.0/24 Metric: 10 Type: 1 Up
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
    juniper_379_MX304.00-00       142  49898   713    246 L2  0000.0001.7900.00-00  <>
      NLPID: 0xCC(IPv4) 0x8E(IPv6)
      Hostname: juniper_379_MX304
      Area addresses: 49.0001.00
      Interface address: 10.0.0.179
      Interface address: 209.209.209.209
      IS Neighbor          : h49-N540-24Q8L2DD.00 Metric: 10
        IPv4 Neighbor Address: 20.149.179.149
        IPv4 Interface Address: 20.149.179.179
        Adj-sid: 23 flags: [L V B] weight: 0x0
      Reachability         : 20.57.179.0/24 Metric: 10 Type: 1 Up
      Reachability         : 10.0.0.179/32 Metric: 0 Type: 1 Up
        SR Prefix-SID: 379 Flags: [N] Algorithm: 0
        SR Prefix-SID: 1379 Flags: [N] Algorithm: 130
        SR Prefix-SID: 1279 Flags: [N] Algorithm: 129
        SR Prefix-SID: 1179 Flags: [N] Algorithm: 128
      Reachability         : 209.209.209.209/32 Metric: 0 Type: 1 Up
        SR Prefix-SID: 209 Flags: [] Algorithm: 0
      Reachability         : 20.149.179.0/24 Metric: 10 Type: 1 Up
      Router Capabilities: Router Id: 10.0.0.179 Flags: []
        Maximum SID depth:
          Base MPLS imposition (MSD type 1):  4
        SR Capability: Flags: [I V]
          SRGB Base: 20000 Range: 2000
        Algorithms:  0, 1, 128, 129, 130
      Unsupported TLV: Type: 14 Length: 2
    0000.0010.0005.00-00         76  63421  1112    268 L2  0000.0010.0005.00-00  <>
      NLPID: 0xCC(IPv4)
      Area addresses: 49.0000
      Interface address: 20.5.149.5
      IS Neighbor          : h49-N540-24Q8L2DD.00 Metric: 10
        IPv4 Neighbor Address: 20.5.149.149
        IPv4 Interface Address: 20.5.149.5
        Adj-sid: 16002 flags: [L V] weight: 0x0
      Reachability         : 20.5.149.0/24 Metric: 10 Type: 1 Up
      Reachability         : 10.0.0.5/32 Metric: 0 Type: 1 Up
        SR Prefix-SID: 5 Flags: [N] Algorithm: 0
      Reachability          : 2002::5/128 Metric: 0 Type: 1 Up
      Router Capabilities: Router Id: 10.0.0.5 Flags: []
        SR Capability: Flags: [I]
          SRGB Base: 20000 Range: 2000
        Algorithms:  0
    NOKIA-SR2-57.00-00         3868   4775  1163    350 L2  0100.0000.0057.00-00  <>
      NLPID: 0xCC(IPv4) 0x8E(IPv6)
      Hostname: NOKIA-SR2-57
      Area addresses: 49.0000.0000.0057.00
      Interface address: 10.0.0.57
      Interface address: 20.57.149.57
      Interface address: 209.209.209.209
      Interface address: 2002::57
      IS Neighbor (Narrow metrics, unsupported): h49-N540-24Q8L2DD.00 Metric: 10
      IS Neighbor          : h49-N540-24Q8L2DD.00 Metric: 10
        IPv4 Neighbor Address: 20.57.149.149
        IPv4 Interface Address: 20.57.149.57
        Adj-sid: 30149 flags: [L V B] weight: 0x0
      Reachability (Narrow metrics, unsupported): 10.0.0.57/32 Metric: 0 Type: 1
      Reachability (Narrow metrics, unsupported): 20.57.149.0/24 Metric: 10 Type: 1
      Reachability (Narrow metrics, unsupported): 209.209.209.209/32 Metric: 0 Type: 1
      Reachability         : 10.0.0.57/32 Metric: 0 Type: 1 Up
        SR Prefix-SID: 57 Flags: [N P] Algorithm: 0
      Reachability         : 20.57.149.0/24 Metric: 10 Type: 1 Up
      Reachability         : 209.209.209.209/32 Metric: 0 Type: 1 Up
      Reachability          : 2002::57/128 Metric: 0 Type: 1 Up
        SR Prefix-SID: 157 Flags: [N P] Algorithm: 0
      Router Capabilities: Router Id: 10.0.0.57 Flags: []
        Maximum SID depth:
          Base MPLS imposition (MSD type 1):  12
        SR Capability: Flags: [I V]
          SRGB Base: 20000 Range: 2000
        Algorithms:  0
    PE31-J2-171.00-00           126  39377   760    287 L2  0100.0000.0171.00-00  <>
      NLPID: 0xCC(IPv4)
      Hostname: PE31-J2-171
      Area addresses: 49.0000
      Interface address: 20.149.171.171
      Interface address: 10.0.0.171
      IS Neighbor          : h49-N540-24Q8L2DD.00 Metric: 10
        IPv4 Neighbor Address: 20.149.171.149
        IPv4 Interface Address: 20.149.171.171
        Adj-sid: 362144 flags: [L V] weight: 0x0
      Reachability         : 20.149.171.0/24 Metric: 10 Type: 1 Up
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
    PE32-J2-172.00-00           128  15710  1009    178 L2  0100.0000.0172.00-00  <>
      LSP generation remaining wait time: 0 ms
      Time remaining until refresh: 709 s
      NLPID: 0xCC(IPv4)
      Hostname: PE32-J2-172
      Area addresses: 49.0000
      Interface address: 20.149.172.172
      Interface address: 209.209.209.209
      Interface address: 10.0.0.172
      IS Neighbor          : h49-N540-24Q8L2DD.00 Metric: 10
        IPv4 Neighbor Address: 20.149.172.149
        IPv4 Interface Address: 20.149.172.172
        Adj-sid: 362144 flags: [L V B] weight: 0x0
      Reachability         : 209.209.209.209/32 Metric: 0 Type: 1 Up
        SR Prefix-SID: 209 Flags: [] Algorithm: 0
      Reachability         : 20.149.172.0/24 Metric: 10 Type: 1 Up
      Reachability         : 10.0.0.172/32 Metric: 10 Type: 1 Up
        SR Prefix-SID: 172 Flags: [N] Algorithm: 0
      Router Capabilities: Router Id: 209.209.209.209 Flags: []
        SR Local Block:
          SRLB Base: 965536 Range: 65536
        Area leader priority: 250 algorithm: 0
        Maximum SID depth:
          Base MPLS imposition (MSD type 1):  12
        SR Capability: Flags: [I]
          SRGB Base: 20000 Range: 2000
 U  3800.0000.4111.00-00        111  38360     0     61 L2  3800.0000.4111.00-00  <DefaultAtt>
      Hostname: h49-N540-24Q8L2DD
      Purge originator: h49-N540-24Q8L2DD
      Purge originator upstream neighbor: juniper_379_MX304
Legend:
H - hostname conflict
U - node unreachable

IS-IS Instance: OPTION-C-DOMAIN-2 VRF: default
  IS-IS Level 2 Link State Database
    LSPID                   Seq Num  Cksum  Life Length IS  Received LSPID        Flags
    0000.0000.0001.00-00         75  49081  1117    214 L2  0000.0000.0001.00-00  <>
      Remaining lifetime received: 1199 s Modified to: 1200 s
      NLPID: 0xCC(IPv4)
      Area addresses: 49.0001
      Interface address: 20.5.170.5
      IS Neighbor          : Spine3-J-170.00     Metric: 10
        IPv4 Neighbor Address: 20.5.170.170
        IPv4 Interface Address: 20.5.170.5
        Adj-sid: 16003 flags: [L V] weight: 0x0
      Reachability         : 20.5.170.0/24 Metric: 10 Type: 1 Up
      Reachability         : 10.0.0.5/32 Metric: 0 Type: 1 Up
        SR Prefix-SID: 5 Flags: [N] Algorithm: 0
      Reachability          : 2002::5/128 Metric: 0 Type: 1 Up
      Router Capabilities: Router Id: 10.0.0.5 Flags: []
        SR Capability: Flags: [I]
          SRGB Base: 20000 Range: 2000
        Algorithms:  0
    Ericsson_47.00-00           130  37636  1090    166 L2  0000.0000.0047.00-00  <>
      Remaining lifetime received: 978 s Modified to: 1200 s
      NLPID: 0xCC(IPv4)
      Hostname: Ericsson_47
      Area addresses: 49.0001
      Interface address: 10.0.0.47
      Interface address: 2002::47
      IS Neighbor          : Spine3-J-170.00     Metric: 10
        IPv4 Interface Address: 20.47.170.47
      Reachability         : 10.0.0.47/32 Metric: 10 Type: 1 Up
        SR Prefix-SID: 47 Flags: [N P] Algorithm: 0
      Reachability         : 20.47.170.0/24 Metric: 10 Type: 1 Up
      Router Capabilities: Router Id: 10.0.0.47 Flags: []
        Maximum SID depth:
          Base MPLS imposition (MSD type 1):  8
        SR Capability: Flags: [I]
          SRGB Base: 20000 Range: 2000
        Algorithms:  0
    Ribbon-32.00-00              81  46444   665     79 L2  0000.0001.0032.00-00  <>
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
    Ribbon-32.00-01              81  61953  1090     38 L2  0000.0001.0032.00-01  <>
      Remaining lifetime received: 1065 s Modified to: 1200 s
      Hostname: Ribbon-32
    Ribbon-32.00-02              86  10009  1090    205 L2  0000.0001.0032.00-02  <>
      Remaining lifetime received: 929 s Modified to: 1200 s
      Interface address: 10.0.0.32
      Interface address: 20.32.170.32
      Interface address: 209.209.209.209
      IS Neighbor          : Spine3-J-170.00     Metric: 10
        IPv4 Neighbor Address: 20.32.170.170
        IPv4 Interface Address: 20.32.170.32
        Adj-sid: 756642 flags: [L V] weight: 0x0
        Adj-sid: 756643 flags: [L V B] weight: 0x0
      Reachability         : 10.0.0.32/32 Metric: 0 Type: 1 Up
        SR Prefix-SID: 32 Flags: [N] Algorithm: 0
      Reachability         : 20.32.170.0/24 Metric: 10 Type: 1 Up
      Reachability         : 209.209.209.209/32 Metric: 0 Type: 1 Up
        SR Prefix-SID: 209 Flags: [] Algorithm: 0
    juniper_379_MX304.00-00       152    440  1136    211 L2  0000.0001.7900.00-00  <>
      Remaining lifetime received: 1199 s Modified to: 1200 s
      NLPID: 0xCC(IPv4) 0x8E(IPv6)
      Hostname: juniper_379_MX304
      Area addresses: 49.0001.00
      Interface address: 10.0.0.179
      Interface address: 209.209.209.209
      IS Neighbor          : Spine3-J-170.00     Metric: 10
        IPv4 Neighbor Address: 20.170.179.170
        IPv4 Interface Address: 20.170.179.179
        Adj-sid: 26 flags: [L V] weight: 0x0
      Reachability         : 10.0.0.179/32 Metric: 0 Type: 1 Up
        SR Prefix-SID: 379 Flags: [N] Algorithm: 0
      Reachability         : 209.209.209.209/32 Metric: 0 Type: 1 Up
        SR Prefix-SID: 209 Flags: [] Algorithm: 0
      Reachability         : 20.170.179.0/24 Metric: 10 Type: 1 Up
      Router Capabilities: Router Id: 10.0.0.179 Flags: []
        Maximum SID depth:
          Base MPLS imposition (MSD type 1):  4
        SR Capability: Flags: [I V]
          SRGB Base: 20000 Range: 2000
        Algorithms:  0, 1
      Unsupported TLV: Type: 14 Length: 2
    JNPR-312-ACX7100-48L.00-00       140   1443   656    178 L2  0000.0003.1200.00-00  <>
      Remaining lifetime received: 1199 s Modified to: 1200 s
      NLPID: 0xCC(IPv4) 0x8E(IPv6)
      Hostname: JNPR-312-ACX7100-48L
      Area addresses: 49.0001.00
      Interface address: 10.0.0.212
      IS Neighbor          : Spine3-J-170.00     Metric: 10
        IPv4 Neighbor Address: 20.170.212.170
        IPv4 Interface Address: 20.170.212.212
        Adj-sid: 213 flags: [L V B] weight: 0x0
      Reachability         : 10.0.0.212/32 Metric: 0 Type: 1 Up
        SR Prefix-SID: 212 Flags: [N] Algorithm: 0
      Reachability         : 20.170.212.0/24 Metric: 10 Type: 1 Up
      Router Capabilities: Router Id: 10.0.0.212 Flags: []
        Maximum SID depth:
          Base MPLS imposition (MSD type 1):  4
        SR Capability: Flags: [I V]
          SRGB Base: 20000 Range: 2000
        Algorithms:  0, 1
      Unsupported TLV: Type: 14 Length: 2
    h55-8201-24H8FH.00-00       130  18187  1096    214 L2  0001.0000.0355.00-00  <>
      Remaining lifetime received: 1199 s Modified to: 1200 s
      NLPID: 0xCC(IPv4)
      Hostname: h55-8201-24H8FH
      Area addresses: 49
      Interface address: 10.0.1.55
      IS Neighbor          : Spine3-J-170.00     Metric: 10
        IPv4 Neighbor Address: 20.155.170.170
        IPv4 Interface Address: 20.155.170.155
        Adj-sid: 24007 flags: [L V] weight: 0x0
      Reachability         : 10.0.1.55/32 Metric: 0 Type: 1 Up
        SR Prefix-SID: 355 Flags: [N] Algorithm: 0
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
        Algorithms:  0, 1
      Unsupported TLV: Type: 14 Length: 2
    NOKIA-SR2-57.00-00          160    270  1149    271 L2  0100.0000.0057.00-00  <>
      Remaining lifetime received: 1199 s Modified to: 1200 s
      NLPID: 0xCC(IPv4) 0x8E(IPv6)
      Hostname: NOKIA-SR2-57
      Area addresses: 49.0001.0000.0057.00
      Interface address: 10.0.0.57
      Interface address: 20.57.170.57
      Interface address: 2002::57
      IS Neighbor (Narrow metrics, unsupported): Spine3-J-170.00     Metric: 10
      IS Neighbor          : Spine3-J-170.00     Metric: 10
        IPv4 Neighbor Address: 20.57.170.170
        IPv4 Interface Address: 20.57.170.57
        Adj-sid: 30170 flags: [L V B] weight: 0x0
      Reachability (Narrow metrics, unsupported): 10.0.0.57/32 Metric: 0 Type: 1
      Reachability (Narrow metrics, unsupported): 20.57.170.0/24 Metric: 10 Type: 1
      Reachability         : 10.0.0.57/32 Metric: 0 Type: 1 Up
        SR Prefix-SID: 57 Flags: [N P] Algorithm: 0
      Reachability         : 20.57.170.0/24 Metric: 10 Type: 1 Up
      Reachability          : 2002::57/128 Metric: 0 Type: 1 Up
        SR Prefix-SID: 157 Flags: [N P] Algorithm: 0
      Router Capabilities: Router Id: 10.0.0.57 Flags: []
        Maximum SID depth:
          Base MPLS imposition (MSD type 1):  12
        SR Capability: Flags: [I V]
          SRGB Base: 20000 Range: 2000
        Algorithms:  0
    Nokia-59-IXRe2.00-00        160  35655   599    271 L2  0100.0000.0059.00-00  <>
      Remaining lifetime received: 1199 s Modified to: 1200 s
      NLPID: 0xCC(IPv4) 0x8E(IPv6)
      Hostname: Nokia-59-IXRe2
      Area addresses: 49.0001.0000.0057.00
      Interface address: 10.0.0.59
      Interface address: 20.59.170.59
      Interface address: 2002::59
      IS Neighbor (Narrow metrics, unsupported): Spine3-J-170.00     Metric: 10
      IS Neighbor          : Spine3-J-170.00     Metric: 10
        IPv4 Neighbor Address: 20.59.170.170
        IPv4 Interface Address: 20.59.170.59
        Adj-sid: 30170 flags: [L V B] weight: 0x0
      Reachability (Narrow metrics, unsupported): 20.59.170.0/24 Metric: 10 Type: 1
      Reachability (Narrow metrics, unsupported): 10.0.0.59/32 Metric: 0 Type: 1
      Reachability         : 20.59.170.0/24 Metric: 10 Type: 1 Up
      Reachability         : 10.0.0.59/32 Metric: 0 Type: 1 Up
        SR Prefix-SID: 59 Flags: [N P] Algorithm: 0
      Reachability          : 2002::59/128 Metric: 0 Type: 1 Up
        SR Prefix-SID: 159 Flags: [N P] Algorithm: 0
      Router Capabilities: Router Id: 10.0.0.59 Flags: []
        Maximum SID depth:
          Base MPLS imposition (MSD type 1):  9
        SR Capability: Flags: [I V]
          SRGB Base: 20000 Range: 2000
        Algorithms:  0
    Spine3-J-170.00-00          249  56232  1090    507 L2  0100.0000.0170.00-00  <>
      Remaining lifetime received: 1199 s Modified to: 1200 s
      NLPID: 0xCC(IPv4)
      Hostname: Spine3-J-170
      Area addresses: 49.0000
      Interface address: 20.170.172.170
      Interface address: 20.170.254.170
      Interface address: 20.32.170.170
      Interface address: 20.170.212.170
      Interface address: 20.57.170.170
      Interface address: 20.59.170.170
      Interface address: 20.47.170.170
      Interface address: 20.170.179.170
      Interface address: 20.5.170.170
      Interface address: 20.155.170.170
      Interface address: 10.0.0.170
      IS Neighbor          : PE32-J2-172.00      Metric: 1
        IPv4 Neighbor Address: 20.170.172.172
        IPv4 Interface Address: 20.170.172.170
        Adj-sid: 362151 flags: [L V] weight: 0x0
      IS Neighbor          : Ribbon-32.00        Metric: 5
        IPv4 Neighbor Address: 20.32.170.32
        IPv4 Interface Address: 20.32.170.170
        Adj-sid: 362152 flags: [L V] weight: 0x0
      IS Neighbor          : NOKIA-SR2-57.00     Metric: 10
        IPv4 Neighbor Address: 20.57.170.57
        IPv4 Interface Address: 20.57.170.170
        Adj-sid: 362155 flags: [L V] weight: 0x0
      IS Neighbor          : 0000.0000.0001.00   Metric: 10
        IPv4 Neighbor Address: 20.5.170.5
        IPv4 Interface Address: 20.5.170.170
        Adj-sid: 362153 flags: [L V] weight: 0x0
      IS Neighbor          : juniper_379_MX304.00 Metric: 10
        IPv4 Neighbor Address: 20.170.179.179
        IPv4 Interface Address: 20.170.179.170
        Adj-sid: 362150 flags: [L V] weight: 0x0
      IS Neighbor          : JNPR-312-ACX7100-48L.00 Metric: 10
        IPv4 Neighbor Address: 20.170.212.212
        IPv4 Interface Address: 20.170.212.170
        Adj-sid: 362149 flags: [L V] weight: 0x0
      IS Neighbor          : Ericsson_47.00      Metric: 10
        IPv4 Neighbor Address: 20.47.170.47
        IPv4 Interface Address: 20.47.170.170
        Adj-sid: 362148 flags: [L V] weight: 0x0
      IS Neighbor          : Nokia-59-IXRe2.00   Metric: 10
        IPv4 Neighbor Address: 20.59.170.59
        IPv4 Interface Address: 20.59.170.170
        Adj-sid: 362146 flags: [L V] weight: 0x0
      IS Neighbor          : h55-8201-24H8FH.00  Metric: 20
        IPv4 Neighbor Address: 20.155.170.155
        IPv4 Interface Address: 20.155.170.170
        Adj-sid: 362144 flags: [L V] weight: 0x0
      Reachability         : 20.170.172.0/24 Metric: 1 Type: 1 Up
      Reachability         : 20.170.254.0/24 Metric: 10 Type: 1 Up
      Reachability         : 20.32.170.0/24 Metric: 5 Type: 1 Up
      Reachability         : 20.170.212.0/24 Metric: 10 Type: 1 Up
      Reachability         : 20.57.170.0/24 Metric: 10 Type: 1 Up
      Reachability         : 20.59.170.0/24 Metric: 10 Type: 1 Up
      Reachability         : 20.47.170.0/24 Metric: 10 Type: 1 Up
      Reachability         : 20.170.179.0/24 Metric: 10 Type: 1 Up
      Reachability         : 20.5.170.0/24 Metric: 10 Type: 1 Up
      Reachability         : 20.155.170.0/24 Metric: 20 Type: 1 Up
      Reachability         : 10.0.0.170/32 Metric: 10 Type: 1 Up
        SR Prefix-SID: 170 Flags: [N] Algorithm: 0
      Router Capabilities: Router Id: 10.0.0.170 Flags: []
        SR Local Block:
          SRLB Base: 965536 Range: 65536
        Area leader priority: 250 algorithm: 0
        Maximum SID depth:
          Base MPLS imposition (MSD type 1):  6
        SR Capability: Flags: [I]
          SRGB Base: 20000 Range: 2000
    PE32-J2-172.00-00           129  56671  1090    184 L2  0100.0000.0172.00-00  <>
      LSP generation remaining wait time: 0 ms
      Time remaining until refresh: 790 s
      NLPID: 0xCC(IPv4)
      Hostname: PE32-J2-172
      Area addresses: 49.0000
      Interface address: 20.170.172.172
      Interface address: 209.209.209.209
      Interface address: 10.0.0.172
      IS Neighbor          : Spine3-J-170.00     Metric: 10
        IPv4 Neighbor Address: 20.170.172.170
        IPv4 Interface Address: 20.170.172.172
        Adj-sid: 362145 flags: [L V] weight: 0x0
      Reachability         : 20.170.172.0/24 Metric: 10 Type: 1 Up
      Reachability         : 209.209.209.209/32 Metric: 0 Type: 1 Up
        SR Prefix-SID: 209 Flags: [] Algorithm: 0
      Reachability         : 10.0.0.172/32 Metric: 10 Type: 1 Up
        SR Prefix-SID: 172 Flags: [N] Algorithm: 0
      Router Capabilities: Router Id: 209.209.209.209 Flags: []
        SR Local Block:
          SRLB Base: 965536 Range: 65536
        Area leader priority: 250 algorithm: 0
        Maximum SID depth:
          Base MPLS imposition (MSD type 1):  12
        SR Capability: Flags: [I]
          SRGB Base: 20000 Range: 2000
      Instance ID: 2 supported_instance_ids: 0
```

## show isis database traffic-engineering

```text
Legend:
H - hostname conflict
U - node unreachable

IS-IS Instance: OPTION-C-DOMAIN-1 VRF: default
  IS-IS Level 2 Link State Database
    LSPID                   Seq Num  Cksum  Life Length IS  Received LSPID        Flags
    h3c_19_CR16010E-F.00-00       203    364  1179    267 L2  0000.0000.0019.00-00  <>
      NLPID: 0xCC(IPv4)
      Hostname: h3c_19_CR16010E-F
      TE IPv4 router ID: 10.0.0.19
      Area addresses: 49
      Interface address: 10.0.0.19
      Interface address: 20.19.149.19
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
      Reachability         : 10.0.0.19/32 Metric: 0 Type: 1 Up
        SR Prefix-SID: 19 Flags: [N P] Algorithm: 0
      Reachability         : 20.19.149.0/24 Metric: 10 Type: 1 Up
      Reachability         : 31.9.1.0/24 Metric: 0 Type: 1 Up
      Reachability         : 192.168.0.0/19 Metric: 0 Type: 1 Up
      Router Capabilities: Router Id: 10.0.0.19 Flags: []
        Maximum SID depth:
          Base MPLS imposition (MSD type 1):  13
        SR Capability: Flags: [I]
          SRGB Base: 20000 Range: 2000
    h3c_24_S12500R-48C6D.00-00       202   4373  1179    288 L2  0000.0000.0024.00-00  <>
      NLPID: 0xCC(IPv4)
      Hostname: h3c_24_S12500R-48C6D
      TE IPv4 router ID: 10.0.0.24
      Area addresses: 49
      Interface address: 10.0.0.24
      Interface address: 20.24.149.24
      IS Neighbor          : h49-N540-24Q8L2DD.00 Metric: 10
        IPv4 Neighbor Address: 20.24.149.149
        IPv4 Interface Address: 20.24.149.24
        Adj-sid: 56127 flags: [L V] weight: 0x0
        TE default metric: 10
        Maximum link BW: 0.00 bps
        Maximum reservable link BW: 0.00 bps
        Unreserved BW:
            TE class 0: 0.00 bps	TE class 1: 0.00 bps	TE class 2: 0.00 bps
            TE class 3: 0.00 bps	TE class 4: 0.00 bps	TE class 5: 0.00 bps
            TE class 6: 0.00 bps	TE class 7: 0.00 bps
      Reachability         : 10.0.0.24/32 Metric: 0 Type: 1 Up
        SR Prefix-SID: 24 Flags: [N P] Algorithm: 0
      Reachability         : 10.0.1.24/32 Metric: 0 Type: 1 Up
      Reachability         : 20.24.149.0/24 Metric: 10 Type: 1 Up
      Reachability         : 192.168.20.0/23 Metric: 0 Type: 1 Up
      Router Capabilities: Router Id: 10.0.0.24 Flags: []
        SR Local Block:
          SRLB Base: 15000 Range: 1000
        Maximum SID depth:
          Base MPLS imposition (MSD type 1):  10
        SR Capability: Flags: [I]
          SRGB Base: 20000 Range: 2000
    Ribbon-32.00-00              80  49506   372     79 L2  0000.0000.0032.00-00  <>
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
    Ribbon-32.00-01              80  65270  1008     38 L2  0000.0000.0032.00-01  <>
      Hostname: Ribbon-32
    Ribbon-32.00-02              83  22315  1000    205 L2  0000.0000.0032.00-02  <>
      Interface address: 10.0.0.32
      Interface address: 20.32.149.32
      Interface address: 209.209.209.209
      IS Neighbor          : h49-N540-24Q8L2DD.00 Metric: 10
        IPv4 Neighbor Address: 20.32.149.149
        IPv4 Interface Address: 20.32.149.32
        Adj-sid: 756640 flags: [L V] weight: 0x0
        Adj-sid: 756641 flags: [L V B] weight: 0x0
        TE default metric: 10
        Maximum link BW: 1.00 Gbps
        Maximum reservable link BW: 1.00 Gbps
        Unreserved BW:
            TE class 0: 1.00 Gbps	TE class 1: 1.00 Gbps	TE class 2: 1.00 Gbps
            TE class 3: 1.00 Gbps	TE class 4: 1.00 Gbps	TE class 5: 1.00 Gbps
            TE class 6: 1.00 Gbps	TE class 7: 1.00 Gbps
        Min/Max unidirectional link delay: 11/11 us
      Reachability         : 10.0.0.32/32 Metric: 0 Type: 1 Up
        SR Prefix-SID: 32 Flags: [N] Algorithm: 0
      Reachability         : 20.32.149.0/24 Metric: 10 Type: 1 Up
      Reachability         : 209.209.209.209/32 Metric: 0 Type: 1 Up
        SR Prefix-SID: 209 Flags: [] Algorithm: 0
    R6676-50.00-00              122  33795   588    145 L2  0000.0000.0050.00-00  <>
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
    h43-9901.00-00              123  58457   684    186 L2  0000.0000.0343.00-00  <>
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
    h49-N540-24Q8L2DD.00-00       174  11066   426   1383 L2  0000.0000.0349.00-00  <>
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
      IS Neighbor          : R6676-50.00         Metric: 10
        IPv4 Neighbor Address: 20.50.149.50
        IPv4 Interface Address: 20.50.149.149
        Adj-sid: 24017 flags: [L V] weight: 0x0
        Maximum link BW: 10.00 Gbps
        Application Specific Link Attributes:
          Standard applications: Flex-Algo
          User-defined applications: APP3
            Maximum link BW: 10.00 Gbps
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
        Application Specific Link Attributes:
          Standard applications: Flex-Algo
          User-defined applications: APP3
            TE default metric: 12
            Maximum link BW: 10.00 Gbps
            Min/Max unidirectional link delay: 11/11 us
      IS Neighbor          : PE32-J2-172.00      Metric: 10
        IPv4 Neighbor Address: 20.149.172.172
        IPv4 Interface Address: 20.149.172.149
        Adj-sid: 24006 flags: [L V B] weight: 0x0
        Adj-sid: 24007 flags: [L V] weight: 0x0
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
      Reachability         : 20.50.149.0/24 Metric: 10 Type: 1 Up
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
    h49-N540-24Q8L2DD.00-01       135  40666   667    124 L2  0000.0000.0349.00-01  <>
      IS Neighbor          : Ribbon-32.00        Metric: 10
        IPv4 Neighbor Address: 20.32.149.32
        IPv4 Interface Address: 20.32.149.149
        Adj-sid: 24025 flags: [L V] weight: 0x0
        Maximum link BW: 1.00 Gbps
        Min/Max unidirectional link delay: 11/11 us
        Application Specific Link Attributes:
          Standard applications: Flex-Algo
          User-defined applications: APP3
            TE default metric: 12
            Maximum link BW: 1.00 Gbps
            Min/Max unidirectional link delay: 11/11 us
    h55-8201-24H8FH.00-00       128  59637  1116    482 L2  0000.0000.0355.00-00  <>
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
      Reachability         : 20.32.155.0/24 Metric: 10 Type: 1 Up
      Reachability         : 20.57.155.0/24 Metric: 10 Type: 1 Up
      Reachability         : 20.149.155.0/24 Metric: 10 Type: 1 Up
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
    juniper_379_MX304.00-00       142  49898   713    246 L2  0000.0001.7900.00-00  <>
      NLPID: 0xCC(IPv4) 0x8E(IPv6)
      Hostname: juniper_379_MX304
      TE IPv4 router ID: 10.0.0.179
      Area addresses: 49.0001.00
      Interface address: 10.0.0.179
      Interface address: 209.209.209.209
      IS Neighbor          : h49-N540-24Q8L2DD.00 Metric: 10
        IPv4 Neighbor Address: 20.149.179.149
        IPv4 Interface Address: 20.149.179.179
        Adj-sid: 23 flags: [L V B] weight: 0x0
        Maximum link BW: 10.00 Gbps
      Reachability         : 20.57.179.0/24 Metric: 10 Type: 1 Up
      Reachability         : 10.0.0.179/32 Metric: 0 Type: 1 Up
        SR Prefix-SID: 379 Flags: [N] Algorithm: 0
        SR Prefix-SID: 1379 Flags: [N] Algorithm: 130
        SR Prefix-SID: 1279 Flags: [N] Algorithm: 129
        SR Prefix-SID: 1179 Flags: [N] Algorithm: 128
      Reachability         : 209.209.209.209/32 Metric: 0 Type: 1 Up
        SR Prefix-SID: 209 Flags: [] Algorithm: 0
      Reachability         : 20.149.179.0/24 Metric: 10 Type: 1 Up
      Router Capabilities: Router Id: 10.0.0.179 Flags: []
        Maximum SID depth:
          Base MPLS imposition (MSD type 1):  4
        SR Capability: Flags: [I V]
          SRGB Base: 20000 Range: 2000
        Algorithms:  0, 1, 128, 129, 130
      Unsupported TLV: Type: 14 Length: 2
    0000.0010.0005.00-00         76  63421  1112    268 L2  0000.0010.0005.00-00  <>
      NLPID: 0xCC(IPv4)
      TE IPv4 router ID: 10.0.0.5
      Area addresses: 49.0000
      Interface address: 20.5.149.5
      IS Neighbor          : h49-N540-24Q8L2DD.00 Metric: 10
        IPv4 Neighbor Address: 20.5.149.149
        IPv4 Interface Address: 20.5.149.5
        Adj-sid: 16002 flags: [L V] weight: 0x0
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
      Reachability         : 20.5.149.0/24 Metric: 10 Type: 1 Up
      Reachability         : 10.0.0.5/32 Metric: 0 Type: 1 Up
        SR Prefix-SID: 5 Flags: [N] Algorithm: 0
      Reachability          : 2002::5/128 Metric: 0 Type: 1 Up
      Router Capabilities: Router Id: 10.0.0.5 Flags: []
        SR Capability: Flags: [I]
          SRGB Base: 20000 Range: 2000
        Algorithms:  0
    NOKIA-SR2-57.00-00         3868   4775  1162    350 L2  0100.0000.0057.00-00  <>
      NLPID: 0xCC(IPv4) 0x8E(IPv6)
      Hostname: NOKIA-SR2-57
      TE IPv4 router ID: 10.0.0.57
      TE IPv6 router ID: 2002::57
      Area addresses: 49.0000.0000.0057.00
      Interface address: 10.0.0.57
      Interface address: 20.57.149.57
      Interface address: 209.209.209.209
      Interface address: 2002::57
      IS Neighbor (Narrow metrics, unsupported): h49-N540-24Q8L2DD.00 Metric: 10
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
      Reachability (Narrow metrics, unsupported): 10.0.0.57/32 Metric: 0 Type: 1
      Reachability (Narrow metrics, unsupported): 20.57.149.0/24 Metric: 10 Type: 1
      Reachability (Narrow metrics, unsupported): 209.209.209.209/32 Metric: 0 Type: 1
      Reachability         : 10.0.0.57/32 Metric: 0 Type: 1 Up
        SR Prefix-SID: 57 Flags: [N P] Algorithm: 0
      Reachability         : 20.57.149.0/24 Metric: 10 Type: 1 Up
      Reachability         : 209.209.209.209/32 Metric: 0 Type: 1 Up
      Reachability          : 2002::57/128 Metric: 0 Type: 1 Up
        SR Prefix-SID: 157 Flags: [N P] Algorithm: 0
      Router Capabilities: Router Id: 10.0.0.57 Flags: []
        Maximum SID depth:
          Base MPLS imposition (MSD type 1):  12
        SR Capability: Flags: [I V]
          SRGB Base: 20000 Range: 2000
        Algorithms:  0
    PE31-J2-171.00-00           126  39377   759    287 L2  0100.0000.0171.00-00  <>
      NLPID: 0xCC(IPv4)
      Hostname: PE31-J2-171
      Area addresses: 49.0000
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
      Reachability         : 20.149.171.0/24 Metric: 10 Type: 1 Up
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
    PE32-J2-172.00-00           128  15710  1008    178 L2  0100.0000.0172.00-00  <>
      LSP generation remaining wait time: 0 ms
      Time remaining until refresh: 708 s
      NLPID: 0xCC(IPv4)
      Hostname: PE32-J2-172
      Area addresses: 49.0000
      Interface address: 20.149.172.172
      Interface address: 209.209.209.209
      Interface address: 10.0.0.172
      IS Neighbor          : h49-N540-24Q8L2DD.00 Metric: 10
        IPv4 Neighbor Address: 20.149.172.149
        IPv4 Interface Address: 20.149.172.172
        Adj-sid: 362144 flags: [L V B] weight: 0x0
      Reachability         : 209.209.209.209/32 Metric: 0 Type: 1 Up
        SR Prefix-SID: 209 Flags: [] Algorithm: 0
      Reachability         : 20.149.172.0/24 Metric: 10 Type: 1 Up
      Reachability         : 10.0.0.172/32 Metric: 10 Type: 1 Up
        SR Prefix-SID: 172 Flags: [N] Algorithm: 0
      Router Capabilities: Router Id: 209.209.209.209 Flags: []
        SR Local Block:
          SRLB Base: 965536 Range: 65536
        Area leader priority: 250 algorithm: 0
        Maximum SID depth:
          Base MPLS imposition (MSD type 1):  12
        SR Capability: Flags: [I]
          SRGB Base: 20000 Range: 2000
 U  3800.0000.4111.00-00        111  38360     0     61 L2  3800.0000.4111.00-00  <DefaultAtt>
      Hostname: h49-N540-24Q8L2DD
      Purge originator: h49-N540-24Q8L2DD
      Purge originator upstream neighbor: juniper_379_MX304
Legend:
H - hostname conflict
U - node unreachable

IS-IS Instance: OPTION-C-DOMAIN-2 VRF: default
  IS-IS Level 2 Link State Database
    LSPID                   Seq Num  Cksum  Life Length IS  Received LSPID        Flags
    0000.0000.0001.00-00         75  49081  1117    214 L2  0000.0000.0001.00-00  <>
      Remaining lifetime received: 1199 s Modified to: 1200 s
      NLPID: 0xCC(IPv4)
      TE IPv4 router ID: 10.0.0.5
      Area addresses: 49.0001
      Interface address: 20.5.170.5
      IS Neighbor          : Spine3-J-170.00     Metric: 10
        IPv4 Neighbor Address: 20.5.170.170
        IPv4 Interface Address: 20.5.170.5
        Adj-sid: 16003 flags: [L V] weight: 0x0
        Maximum link BW: 100.00 Gbps
        Maximum reservable link BW: 100.00 Gbps
        Unreserved BW:
            TE class 0: 0.00 bps	TE class 1: 0.00 bps	TE class 2: 0.00 bps
            TE class 3: 0.00 bps	TE class 4: 0.00 bps	TE class 5: 0.00 bps
            TE class 6: 0.00 bps	TE class 7: 0.00 bps
        Application Specific Link Attributes:
          Standard applications: [L] RSVP-TE SR-TE LFA Flex-Algo
      Reachability         : 20.5.170.0/24 Metric: 10 Type: 1 Up
      Reachability         : 10.0.0.5/32 Metric: 0 Type: 1 Up
        SR Prefix-SID: 5 Flags: [N] Algorithm: 0
      Reachability          : 2002::5/128 Metric: 0 Type: 1 Up
      Router Capabilities: Router Id: 10.0.0.5 Flags: []
        SR Capability: Flags: [I]
          SRGB Base: 20000 Range: 2000
        Algorithms:  0
    Ericsson_47.00-00           130  37636  1090    166 L2  0000.0000.0047.00-00  <>
      Remaining lifetime received: 978 s Modified to: 1200 s
      NLPID: 0xCC(IPv4)
      Hostname: Ericsson_47
      TE IPv4 router ID: 10.0.0.47
      Area addresses: 49.0001
      Interface address: 10.0.0.47
      Interface address: 2002::47
      IS Neighbor          : Spine3-J-170.00     Metric: 10
        IPv4 Interface Address: 20.47.170.47
      Reachability         : 10.0.0.47/32 Metric: 10 Type: 1 Up
        SR Prefix-SID: 47 Flags: [N P] Algorithm: 0
      Reachability         : 20.47.170.0/24 Metric: 10 Type: 1 Up
      Router Capabilities: Router Id: 10.0.0.47 Flags: []
        Maximum SID depth:
          Base MPLS imposition (MSD type 1):  8
        SR Capability: Flags: [I]
          SRGB Base: 20000 Range: 2000
        Algorithms:  0
    Ribbon-32.00-00              81  46444   665     79 L2  0000.0001.0032.00-00  <>
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
    Ribbon-32.00-01              81  61953  1090     38 L2  0000.0001.0032.00-01  <>
      Remaining lifetime received: 1065 s Modified to: 1200 s
      Hostname: Ribbon-32
    Ribbon-32.00-02              86  10009  1090    205 L2  0000.0001.0032.00-02  <>
      Remaining lifetime received: 929 s Modified to: 1200 s
      Interface address: 10.0.0.32
      Interface address: 20.32.170.32
      Interface address: 209.209.209.209
      IS Neighbor          : Spine3-J-170.00     Metric: 10
        IPv4 Neighbor Address: 20.32.170.170
        IPv4 Interface Address: 20.32.170.32
        Adj-sid: 756642 flags: [L V] weight: 0x0
        Adj-sid: 756643 flags: [L V B] weight: 0x0
        TE default metric: 10
        Maximum link BW: 10.00 Gbps
        Maximum reservable link BW: 10.00 Gbps
        Unreserved BW:
            TE class 0: 10.00 Gbps	TE class 1: 10.00 Gbps	TE class 2: 10.00 Gbps
            TE class 3: 10.00 Gbps	TE class 4: 10.00 Gbps	TE class 5: 10.00 Gbps
            TE class 6: 10.00 Gbps	TE class 7: 10.00 Gbps
        Min/Max unidirectional link delay: 11/11 us
      Reachability         : 10.0.0.32/32 Metric: 0 Type: 1 Up
        SR Prefix-SID: 32 Flags: [N] Algorithm: 0
      Reachability         : 20.32.170.0/24 Metric: 10 Type: 1 Up
      Reachability         : 209.209.209.209/32 Metric: 0 Type: 1 Up
        SR Prefix-SID: 209 Flags: [] Algorithm: 0
    juniper_379_MX304.00-00       152    440  1136    211 L2  0000.0001.7900.00-00  <>
      Remaining lifetime received: 1199 s Modified to: 1200 s
      NLPID: 0xCC(IPv4) 0x8E(IPv6)
      Hostname: juniper_379_MX304
      TE IPv4 router ID: 10.0.0.179
      Area addresses: 49.0001.00
      Interface address: 10.0.0.179
      Interface address: 209.209.209.209
      IS Neighbor          : Spine3-J-170.00     Metric: 10
        IPv4 Neighbor Address: 20.170.179.170
        IPv4 Interface Address: 20.170.179.179
        Adj-sid: 26 flags: [L V] weight: 0x0
        Maximum link BW: 10.00 Gbps
      Reachability         : 10.0.0.179/32 Metric: 0 Type: 1 Up
        SR Prefix-SID: 379 Flags: [N] Algorithm: 0
      Reachability         : 209.209.209.209/32 Metric: 0 Type: 1 Up
        SR Prefix-SID: 209 Flags: [] Algorithm: 0
      Reachability         : 20.170.179.0/24 Metric: 10 Type: 1 Up
      Router Capabilities: Router Id: 10.0.0.179 Flags: []
        Maximum SID depth:
          Base MPLS imposition (MSD type 1):  4
        SR Capability: Flags: [I V]
          SRGB Base: 20000 Range: 2000
        Algorithms:  0, 1
      Unsupported TLV: Type: 14 Length: 2
    JNPR-312-ACX7100-48L.00-00       140   1443   656    178 L2  0000.0003.1200.00-00  <>
      Remaining lifetime received: 1199 s Modified to: 1200 s
      NLPID: 0xCC(IPv4) 0x8E(IPv6)
      Hostname: JNPR-312-ACX7100-48L
      TE IPv4 router ID: 10.0.0.212
      Area addresses: 49.0001.00
      Interface address: 10.0.0.212
      IS Neighbor          : Spine3-J-170.00     Metric: 10
        IPv4 Neighbor Address: 20.170.212.170
        IPv4 Interface Address: 20.170.212.212
        Adj-sid: 213 flags: [L V B] weight: 0x0
      Reachability         : 10.0.0.212/32 Metric: 0 Type: 1 Up
        SR Prefix-SID: 212 Flags: [N] Algorithm: 0
      Reachability         : 20.170.212.0/24 Metric: 10 Type: 1 Up
      Router Capabilities: Router Id: 10.0.0.212 Flags: []
        Maximum SID depth:
          Base MPLS imposition (MSD type 1):  4
        SR Capability: Flags: [I V]
          SRGB Base: 20000 Range: 2000
        Algorithms:  0, 1
      Unsupported TLV: Type: 14 Length: 2
    h55-8201-24H8FH.00-00       130  18187  1096    214 L2  0001.0000.0355.00-00  <>
      Remaining lifetime received: 1199 s Modified to: 1200 s
      NLPID: 0xCC(IPv4)
      Hostname: h55-8201-24H8FH
      TE IPv4 router ID: 10.0.1.55
      Area addresses: 49
      Interface address: 10.0.1.55
      IS Neighbor          : Spine3-J-170.00     Metric: 10
        IPv4 Neighbor Address: 20.155.170.170
        IPv4 Interface Address: 20.155.170.155
        Adj-sid: 24007 flags: [L V] weight: 0x0
        Maximum link BW: 100.00 Gbps
      Reachability         : 10.0.1.55/32 Metric: 0 Type: 1 Up
        SR Prefix-SID: 355 Flags: [N] Algorithm: 0
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
        Algorithms:  0, 1
      Unsupported TLV: Type: 14 Length: 2
    NOKIA-SR2-57.00-00          160    270  1149    271 L2  0100.0000.0057.00-00  <>
      Remaining lifetime received: 1199 s Modified to: 1200 s
      NLPID: 0xCC(IPv4) 0x8E(IPv6)
      Hostname: NOKIA-SR2-57
      TE IPv4 router ID: 10.0.0.57
      TE IPv6 router ID: 2002::57
      Area addresses: 49.0001.0000.0057.00
      Interface address: 10.0.0.57
      Interface address: 20.57.170.57
      Interface address: 2002::57
      IS Neighbor (Narrow metrics, unsupported): Spine3-J-170.00     Metric: 10
      IS Neighbor          : Spine3-J-170.00     Metric: 10
        IPv4 Neighbor Address: 20.57.170.170
        IPv4 Interface Address: 20.57.170.57
        Adj-sid: 30170 flags: [L V B] weight: 0x0
      Reachability (Narrow metrics, unsupported): 10.0.0.57/32 Metric: 0 Type: 1
      Reachability (Narrow metrics, unsupported): 20.57.170.0/24 Metric: 10 Type: 1
      Reachability         : 10.0.0.57/32 Metric: 0 Type: 1 Up
        SR Prefix-SID: 57 Flags: [N P] Algorithm: 0
      Reachability         : 20.57.170.0/24 Metric: 10 Type: 1 Up
      Reachability          : 2002::57/128 Metric: 0 Type: 1 Up
        SR Prefix-SID: 157 Flags: [N P] Algorithm: 0
      Router Capabilities: Router Id: 10.0.0.57 Flags: []
        Maximum SID depth:
          Base MPLS imposition (MSD type 1):  12
        SR Capability: Flags: [I V]
          SRGB Base: 20000 Range: 2000
        Algorithms:  0
    Nokia-59-IXRe2.00-00        160  35655   599    271 L2  0100.0000.0059.00-00  <>
      Remaining lifetime received: 1199 s Modified to: 1200 s
      NLPID: 0xCC(IPv4) 0x8E(IPv6)
      Hostname: Nokia-59-IXRe2
      TE IPv4 router ID: 10.0.0.59
      TE IPv6 router ID: 2002::59
      Area addresses: 49.0001.0000.0057.00
      Interface address: 10.0.0.59
      Interface address: 20.59.170.59
      Interface address: 2002::59
      IS Neighbor (Narrow metrics, unsupported): Spine3-J-170.00     Metric: 10
      IS Neighbor          : Spine3-J-170.00     Metric: 10
        IPv4 Neighbor Address: 20.59.170.170
        IPv4 Interface Address: 20.59.170.59
        Adj-sid: 30170 flags: [L V B] weight: 0x0
      Reachability (Narrow metrics, unsupported): 20.59.170.0/24 Metric: 10 Type: 1
      Reachability (Narrow metrics, unsupported): 10.0.0.59/32 Metric: 0 Type: 1
      Reachability         : 20.59.170.0/24 Metric: 10 Type: 1 Up
      Reachability         : 10.0.0.59/32 Metric: 0 Type: 1 Up
        SR Prefix-SID: 59 Flags: [N P] Algorithm: 0
      Reachability          : 2002::59/128 Metric: 0 Type: 1 Up
        SR Prefix-SID: 159 Flags: [N P] Algorithm: 0
      Router Capabilities: Router Id: 10.0.0.59 Flags: []
        Maximum SID depth:
          Base MPLS imposition (MSD type 1):  9
        SR Capability: Flags: [I V]
          SRGB Base: 20000 Range: 2000
        Algorithms:  0
    Spine3-J-170.00-00          249  56232  1090    507 L2  0100.0000.0170.00-00  <>
      Remaining lifetime received: 1199 s Modified to: 1200 s
      NLPID: 0xCC(IPv4)
      Hostname: Spine3-J-170
      Area addresses: 49.0000
      Interface address: 20.170.172.170
      Interface address: 20.170.254.170
      Interface address: 20.32.170.170
      Interface address: 20.170.212.170
      Interface address: 20.57.170.170
      Interface address: 20.59.170.170
      Interface address: 20.47.170.170
      Interface address: 20.170.179.170
      Interface address: 20.5.170.170
      Interface address: 20.155.170.170
      Interface address: 10.0.0.170
      IS Neighbor          : PE32-J2-172.00      Metric: 1
        IPv4 Neighbor Address: 20.170.172.172
        IPv4 Interface Address: 20.170.172.170
        Adj-sid: 362151 flags: [L V] weight: 0x0
      IS Neighbor          : Ribbon-32.00        Metric: 5
        IPv4 Neighbor Address: 20.32.170.32
        IPv4 Interface Address: 20.32.170.170
        Adj-sid: 362152 flags: [L V] weight: 0x0
      IS Neighbor          : NOKIA-SR2-57.00     Metric: 10
        IPv4 Neighbor Address: 20.57.170.57
        IPv4 Interface Address: 20.57.170.170
        Adj-sid: 362155 flags: [L V] weight: 0x0
      IS Neighbor          : 0000.0000.0001.00   Metric: 10
        IPv4 Neighbor Address: 20.5.170.5
        IPv4 Interface Address: 20.5.170.170
        Adj-sid: 362153 flags: [L V] weight: 0x0
      IS Neighbor          : juniper_379_MX304.00 Metric: 10
        IPv4 Neighbor Address: 20.170.179.179
        IPv4 Interface Address: 20.170.179.170
        Adj-sid: 362150 flags: [L V] weight: 0x0
      IS Neighbor          : JNPR-312-ACX7100-48L.00 Metric: 10
        IPv4 Neighbor Address: 20.170.212.212
        IPv4 Interface Address: 20.170.212.170
        Adj-sid: 362149 flags: [L V] weight: 0x0
      IS Neighbor          : Ericsson_47.00      Metric: 10
        IPv4 Neighbor Address: 20.47.170.47
        IPv4 Interface Address: 20.47.170.170
        Adj-sid: 362148 flags: [L V] weight: 0x0
      IS Neighbor          : Nokia-59-IXRe2.00   Metric: 10
        IPv4 Neighbor Address: 20.59.170.59
        IPv4 Interface Address: 20.59.170.170
        Adj-sid: 362146 flags: [L V] weight: 0x0
      IS Neighbor          : h55-8201-24H8FH.00  Metric: 20
        IPv4 Neighbor Address: 20.155.170.155
        IPv4 Interface Address: 20.155.170.170
        Adj-sid: 362144 flags: [L V] weight: 0x0
      Reachability         : 20.170.172.0/24 Metric: 1 Type: 1 Up
      Reachability         : 20.170.254.0/24 Metric: 10 Type: 1 Up
      Reachability         : 20.32.170.0/24 Metric: 5 Type: 1 Up
      Reachability         : 20.170.212.0/24 Metric: 10 Type: 1 Up
      Reachability         : 20.57.170.0/24 Metric: 10 Type: 1 Up
      Reachability         : 20.59.170.0/24 Metric: 10 Type: 1 Up
      Reachability         : 20.47.170.0/24 Metric: 10 Type: 1 Up
      Reachability         : 20.170.179.0/24 Metric: 10 Type: 1 Up
      Reachability         : 20.5.170.0/24 Metric: 10 Type: 1 Up
      Reachability         : 20.155.170.0/24 Metric: 20 Type: 1 Up
      Reachability         : 10.0.0.170/32 Metric: 10 Type: 1 Up
        SR Prefix-SID: 170 Flags: [N] Algorithm: 0
      Router Capabilities: Router Id: 10.0.0.170 Flags: []
        SR Local Block:
          SRLB Base: 965536 Range: 65536
        Area leader priority: 250 algorithm: 0
        Maximum SID depth:
          Base MPLS imposition (MSD type 1):  6
        SR Capability: Flags: [I]
          SRGB Base: 20000 Range: 2000
    PE32-J2-172.00-00           129  56671  1090    184 L2  0100.0000.0172.00-00  <>
      LSP generation remaining wait time: 0 ms
      Time remaining until refresh: 790 s
      NLPID: 0xCC(IPv4)
      Hostname: PE32-J2-172
      Area addresses: 49.0000
      Interface address: 20.170.172.172
      Interface address: 209.209.209.209
      Interface address: 10.0.0.172
      IS Neighbor          : Spine3-J-170.00     Metric: 10
        IPv4 Neighbor Address: 20.170.172.170
        IPv4 Interface Address: 20.170.172.172
        Adj-sid: 362145 flags: [L V] weight: 0x0
      Reachability         : 20.170.172.0/24 Metric: 10 Type: 1 Up
      Reachability         : 209.209.209.209/32 Metric: 0 Type: 1 Up
        SR Prefix-SID: 209 Flags: [] Algorithm: 0
      Reachability         : 10.0.0.172/32 Metric: 10 Type: 1 Up
        SR Prefix-SID: 172 Flags: [N] Algorithm: 0
      Router Capabilities: Router Id: 209.209.209.209 Flags: []
        SR Local Block:
          SRLB Base: 965536 Range: 65536
        Area leader priority: 250 algorithm: 0
        Maximum SID depth:
          Base MPLS imposition (MSD type 1):  12
        SR Capability: Flags: [I]
          SRGB Base: 20000 Range: 2000
      Instance ID: 2 supported_instance_ids: 0
```

## show isis flex-algo

```text

IS-IS Instance: OPTION-C-DOMAIN-1 VRF: default


IS-IS Instance: OPTION-C-DOMAIN-2 VRF: default

```

## show isis flex-algo path detail

```text
```

## show isis segment-routing tunnel

```text
 Index     Endpoint          Next Hop/Tunnel Index     Interface      Labels   
-------- ----------------- ------------------------- ---------------- ---------
 1         10.0.1.49/32      20.149.172.149            Ethernet25     [ 3 ]    
 2         10.0.1.43/32      20.149.172.149            Ethernet25     [ 20343 ]
 3         10.0.0.19/32      20.149.172.149            Ethernet25     [ 20019 ]
 4         10.0.1.55/32      20.149.172.149            Ethernet25     [ 20355 ]
 5         10.0.0.50/32      20.149.172.149            Ethernet25     [ 20050 ]
 7         10.0.0.179/32     20.149.172.149            Ethernet25     [ 20379 ]
 8         10.0.0.24/32      20.149.172.149            Ethernet25     [ 20024 ]
 9         10.0.0.5/32       20.149.172.149            Ethernet25     [ 20005 ]
 11        10.0.0.57/32      20.149.172.149            Ethernet25     [ 20057 ]
 12        10.0.0.171/32     20.149.172.149            Ethernet25     [ 20171 ]
 13        10.0.0.170/32     20.170.172.170            Ethernet52/1   [ 3 ]    
 14        10.0.0.59/32      20.170.172.170            Ethernet52/1   [ 20059 ]
 15        10.0.0.32/32      20.170.172.170            Ethernet52/1   [ 20032 ]
 16        10.0.0.47/32      20.170.172.170            Ethernet52/1   [ 20047 ]
 17        10.0.0.212/32     20.170.172.170            Ethernet52/1   [ 20212 ]

```

## show isis segment-routing prefix-segments

```text

System ID: PE32-J2-172			Instance: 'OPTION-C-DOMAIN-1'
SR supported Data-plane: MPLS			SR Router ID: 209.209.209.209

Node: 34     Proxy-Node: 0      Prefix: 1       Total Segments: 35

Flag Descriptions: R: Re-advertised, N: Node Segment, P: no-PHP
                   E: Explicit-NULL, V: Value, L: Local
Segment status codes: * - Self originated Prefix, L1 - level 1, L2 - level 2, ! - SR-unreachable,
                      # - Some IS-IS next-hops are SR-unreachable
   Prefix                      SID Type       Flags                        System ID       Level Protection  Algorithm   
   ------------------------- ----- ---------- ---------------------------- --------------- ----- ----------- -------------
   10.0.0.5/32                   5 Node       R:0 N:1 P:0 E:0 V:0 L:0      0000.0010.0005  L2    node        SPF         
   10.0.0.19/32                 19 Node       R:0 N:1 P:1 E:0 V:0 L:0      h3c_19_CR16010E-F L2    node        SPF         
   10.0.0.24/32                 24 Node       R:0 N:1 P:1 E:0 V:0 L:0      h3c_24_S12500R-48C6D L2    node        SPF         
   10.0.0.50/32                 50 Node       R:0 N:1 P:1 E:0 V:0 L:0      R6676-50        L2    node        SPF         
   10.0.0.57/32                 57 Node       R:0 N:1 P:1 E:0 V:0 L:0      NOKIA-SR2-57    L2    node        SPF         
   10.0.0.171/32               171 Node       R:0 N:1 P:0 E:0 V:0 L:0      PE31-J2-171     L2    node        SPF         
   10.0.0.171/32              1171 Node       R:0 N:1 P:0 E:0 V:0 L:0      PE31-J2-171     L2    unprotected 128         
   10.0.0.171/32              1271 Node       R:0 N:1 P:0 E:0 V:0 L:0      PE31-J2-171     L2    unprotected MIN-TE      
   10.0.0.171/32              1371 Node       R:0 N:1 P:0 E:0 V:0 L:0      PE31-J2-171     L2    unprotected MIN-IGP     
   10.0.0.171/32              1471 Node       R:0 N:1 P:0 E:0 V:0 L:0      PE31-J2-171     L2    unprotected MIN-IGP-ADMIN
*  10.0.0.172/32               172 Node       R:0 N:1 P:0 E:0 V:0 L:0      PE32-J2-172     L2    unprotected SPF         
   10.0.0.179/32               379 Node       R:0 N:1 P:0 E:0 V:0 L:0      juniper_379_MX304 L2    node        SPF         
   10.0.0.179/32              1179 Node       R:0 N:1 P:0 E:0 V:0 L:0      juniper_379_MX304 L2    unprotected 128         
   10.0.0.179/32              1279 Node       R:0 N:1 P:0 E:0 V:0 L:0      juniper_379_MX304 L2    unprotected MIN-TE      
   10.0.0.179/32              1379 Node       R:0 N:1 P:0 E:0 V:0 L:0      juniper_379_MX304 L2    unprotected MIN-IGP     
   10.0.1.43/32                343 Node       R:0 N:1 P:0 E:0 V:0 L:0      h43-9901        L2    node        SPF         
   10.0.1.49/32                349 Node       R:0 N:1 P:0 E:0 V:0 L:0      h49-N540-24Q8L2DD L2    node        SPF         
   10.0.1.49/32               1449 Node       R:0 N:1 P:0 E:0 V:0 L:0      h49-N540-24Q8L2DD L2    unprotected MIN-TE      
   10.0.1.49/32               1549 Node       R:0 N:1 P:0 E:0 V:0 L:0      h49-N540-24Q8L2DD L2    unprotected MIN-IGP     
   10.0.1.49/32               1649 Node       R:0 N:1 P:0 E:0 V:0 L:0      h49-N540-24Q8L2DD L2    unprotected MIN-IGP-ADMIN
   10.0.1.49/32               1749 Node       R:0 N:1 P:0 E:0 V:0 L:0      h49-N540-24Q8L2DD L2    unprotected 132         
   10.0.1.49/32                449 Node       R:0 N:1 P:0 E:0 V:0 L:0      h49-N540-24Q8L2DD L2    unprotected 140         
   10.0.1.49/32                549 Node       R:0 N:1 P:0 E:0 V:0 L:0      h49-N540-24Q8L2DD L2    unprotected 141         
   10.0.1.49/32                649 Node       R:0 N:1 P:0 E:0 V:0 L:0      h49-N540-24Q8L2DD L2    unprotected 142         
   10.0.1.55/32                355 Node       R:0 N:1 P:0 E:0 V:0 L:0      h55-8201-24H8FH L2    node        SPF         
   10.0.1.55/32               1355 Node       R:0 N:1 P:0 E:0 V:0 L:0      h55-8201-24H8FH L2    unprotected 128         
   10.0.1.55/32               1455 Node       R:0 N:1 P:0 E:0 V:0 L:0      h55-8201-24H8FH L2    unprotected MIN-TE      
   10.0.1.55/32               1555 Node       R:0 N:1 P:0 E:0 V:0 L:0      h55-8201-24H8FH L2    unprotected MIN-IGP     
   10.0.1.55/32               1655 Node       R:0 N:1 P:0 E:0 V:0 L:0      h55-8201-24H8FH L2    unprotected MIN-IGP-ADMIN
   10.0.1.55/32               1755 Node       R:0 N:1 P:0 E:0 V:0 L:0      h55-8201-24H8FH L2    unprotected 132         
   10.0.1.55/32                455 Node       R:0 N:1 P:0 E:0 V:0 L:0      h55-8201-24H8FH L2    unprotected 140         
   10.0.1.55/32                555 Node       R:0 N:1 P:0 E:0 V:0 L:0      h55-8201-24H8FH L2    unprotected 141         
   10.0.1.55/32                655 Node       R:0 N:1 P:0 E:0 V:0 L:0      h55-8201-24H8FH L2    unprotected 142         
*  209.209.209.209/32          209 Prefix     R:0 N:0 P:0 E:0 V:0 L:0      PE32-J2-172     L2    unprotected SPF         
   209.209.209.209/32          209 Prefix     R:0 N:0 P:0 E:0 V:0 L:0      Ribbon-32       L2    unprotected SPF         
   209.209.209.209/32          209 Prefix     R:0 N:0 P:0 E:0 V:0 L:0      juniper_379_MX304 L2    unprotected SPF         
   209.209.209.209/32          209 Prefix     R:0 N:0 P:0 E:0 V:0 L:0      h55-8201-24H8FH L2    unprotected SPF         
   2002::57/128                157 Node       R:0 N:1 P:1 E:0 V:0 L:0      NOKIA-SR2-57    L2    unprotected SPF         

System ID: PE32-J2-172			Instance: 'OPTION-C-DOMAIN-2'
SR supported Data-plane: MPLS			SR Router ID: 209.209.209.209

Node: 6      Proxy-Node: 0      Prefix: 0       Total Segments: 6

Flag Descriptions: R: Re-advertised, N: Node Segment, P: no-PHP
                   E: Explicit-NULL, V: Value, L: Local
Segment status codes: * - Self originated Prefix, L1 - level 1, L2 - level 2, ! - SR-unreachable,
                      # - Some IS-IS next-hops are SR-unreachable
   Prefix                      SID Type       Flags                        System ID       Level Protection  Algorithm   
   ------------------------- ----- ---------- ---------------------------- --------------- ----- ----------- -------------
   10.0.0.32/32                 32 Node       R:0 N:1 P:0 E:0 V:0 L:0      Ribbon-32       L2    node        SPF         
   10.0.0.47/32                 47 Node       R:0 N:1 P:1 E:0 V:0 L:0      Ericsson_47     L2    node        SPF         
   10.0.0.59/32                 59 Node       R:0 N:1 P:1 E:0 V:0 L:0      Nokia-59-IXRe2  L2    node        SPF         
   10.0.0.170/32               170 Node       R:0 N:1 P:0 E:0 V:0 L:0      Spine3-J-170    L2    node        SPF         
   10.0.0.212/32               212 Node       R:0 N:1 P:0 E:0 V:0 L:0      JNPR-312-ACX7100-48L L2    node        SPF         
   2002::59/128                159 Node       R:0 N:1 P:1 E:0 V:0 L:0      Nokia-59-IXRe2  L2    unprotected SPF         
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

 I L2     10.0.0.5/32 [115/20]
           via 20.149.172.149, Ethernet25
 I L2     10.0.0.19/32 [115/20]
           via 20.149.172.149, Ethernet25
 I L2     10.0.0.24/32 [115/20]
           via 20.149.172.149, Ethernet25
 I L2     10.0.0.32/32 [115/15]
           via 20.170.172.170, Ethernet52/1
 I L2     10.0.0.47/32 [115/30]
           via 20.170.172.170, Ethernet52/1
 I L2     10.0.0.50/32 [115/30]
           via 20.149.172.149, Ethernet25
 I L2     10.0.0.57/32 [115/20]
           via 20.149.172.149, Ethernet25
 I L2     10.0.0.59/32 [115/20]
           via 20.170.172.170, Ethernet52/1
 I L2     10.0.0.170/32 [115/20]
           via 20.170.172.170, Ethernet52/1
 I L2     10.0.0.171/32 [115/20]
           via 20.149.172.149, Ethernet25
 C        10.0.0.172/32
           directly connected, Loopback0
 I L2     10.0.0.179/32 [115/20]
           via 20.149.172.149, Ethernet25
 I L2     10.0.0.212/32 [115/20]
           via 20.170.172.170, Ethernet52/1
 I L2     10.0.1.24/32 [115/20]
           via 20.149.172.149, Ethernet25
 I L2     10.0.1.43/32 [115/20]
           via 20.149.172.149, Ethernet25
 I L2     10.0.1.49/32 [115/10]
           via 20.149.172.149, Ethernet25
 I L2     10.0.1.55/32 [115/20]
           via 20.149.172.149, Ethernet25
 I L2     20.5.149.0/24 [115/20]
           via 20.149.172.149, Ethernet25
 I L2     20.5.170.0/24 [115/20]
           via 20.170.172.170, Ethernet52/1
 I L2     20.19.149.0/24 [115/20]
           via 20.149.172.149, Ethernet25
 I L2     20.24.149.0/24 [115/20]
           via 20.149.172.149, Ethernet25
 I L2     20.32.149.0/24 [115/20]
           via 20.149.172.149, Ethernet25
 I L2     20.32.155.0/24 [115/30]
           via 20.149.172.149, Ethernet25
 I L2     20.32.170.0/24 [115/15]
           via 20.170.172.170, Ethernet52/1
 I L2     20.47.170.0/24 [115/20]
           via 20.170.172.170, Ethernet52/1
 I L2     20.50.149.0/24 [115/20]
           via 20.149.172.149, Ethernet25
 I L2     20.57.149.0/24 [115/20]
           via 20.149.172.149, Ethernet25
 I L2     20.57.155.0/24 [115/30]
           via 20.149.172.149, Ethernet25
 I L2     20.57.170.0/24 [115/20]
           via 20.170.172.170, Ethernet52/1
 I L2     20.57.179.0/24 [115/30]
           via 20.149.172.149, Ethernet25
 I L2     20.59.170.0/24 [115/20]
           via 20.170.172.170, Ethernet52/1
 I L2     20.111.149.0/24 [115/20]
           via 20.149.172.149, Ethernet25
 I L2     20.143.149.0/24 [115/20]
           via 20.149.172.149, Ethernet25
 I L2     20.149.155.0/24 [115/20]
           via 20.149.172.149, Ethernet25
 I L2     20.149.171.0/24 [115/20]
           via 20.149.172.149, Ethernet25
 C        20.149.172.0/24
           directly connected, Ethernet25
 I L2     20.149.179.0/24 [115/20]
           via 20.149.172.149, Ethernet25
 I L2     20.149.254.0/24 [115/20]
           via 20.149.172.149, Ethernet25
 I L2     20.155.170.0/24 [115/30]
           via 20.170.172.170, Ethernet52/1
 C        20.170.172.0/24
           directly connected, Ethernet52/1
 I L2     20.170.179.0/24 [115/20]
           via 20.170.172.170, Ethernet52/1
 I L2     20.170.212.0/24 [115/20]
           via 20.170.172.170, Ethernet52/1
 I L2     20.170.254.0/24 [115/20]
           via 20.170.172.170, Ethernet52/1
 I L2     31.9.1.0/24 [115/20]
           via 20.149.172.149, Ethernet25
 I L2     192.168.20.0/23 [115/20]
           via 20.149.172.149, Ethernet25
 I L2     192.168.0.0/19 [115/20]
           via 20.149.172.149, Ethernet25
 C        209.209.209.209/32
           directly connected, Loopback209

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

 I L2     10.0.0.5/32 [115/20]
           via 20.149.172.149, Ethernet25
 I L2     10.0.0.19/32 [115/20]
           via 20.149.172.149, Ethernet25
 I L2     10.0.0.24/32 [115/20]
           via 20.149.172.149, Ethernet25
 I L2     10.0.0.32/32 [115/15]
           via 20.170.172.170, Ethernet52/1
 I L2     10.0.0.47/32 [115/30]
           via 20.170.172.170, Ethernet52/1
 I L2     10.0.0.50/32 [115/30]
           via 20.149.172.149, Ethernet25
 I L2     10.0.0.57/32 [115/20]
           via 20.149.172.149, Ethernet25
 I L2     10.0.0.59/32 [115/20]
           via 20.170.172.170, Ethernet52/1
 I L2     10.0.0.170/32 [115/20]
           via 20.170.172.170, Ethernet52/1
 I L2     10.0.0.171/32 [115/20]
           via 20.149.172.149, Ethernet25
 C        10.0.0.172/32
           directly connected, Loopback0
 I L2     10.0.0.179/32 [115/20]
           via 20.149.172.149, Ethernet25
 I L2     10.0.0.212/32 [115/20]
           via 20.170.172.170, Ethernet52/1
 I L2     10.0.1.24/32 [115/20]
           via 20.149.172.149, Ethernet25
 I L2     10.0.1.43/32 [115/20]
           via 20.149.172.149, Ethernet25
 I L2     10.0.1.49/32 [115/10]
           via 20.149.172.149, Ethernet25
 I L2     10.0.1.55/32 [115/20]
           via 20.149.172.149, Ethernet25
 I L2     20.5.149.0/24 [115/20]
           via 20.149.172.149, Ethernet25
 I L2     20.5.170.0/24 [115/20]
           via 20.170.172.170, Ethernet52/1
 I L2     20.19.149.0/24 [115/20]
           via 20.149.172.149, Ethernet25
 I L2     20.24.149.0/24 [115/20]
           via 20.149.172.149, Ethernet25
 I L2     20.32.149.0/24 [115/20]
           via 20.149.172.149, Ethernet25
 I L2     20.32.155.0/24 [115/30]
           via 20.149.172.149, Ethernet25
 I L2     20.32.170.0/24 [115/15]
           via 20.170.172.170, Ethernet52/1
 I L2     20.47.170.0/24 [115/20]
           via 20.170.172.170, Ethernet52/1
 I L2     20.50.149.0/24 [115/20]
           via 20.149.172.149, Ethernet25
 I L2     20.57.149.0/24 [115/20]
           via 20.149.172.149, Ethernet25
 I L2     20.57.155.0/24 [115/30]
           via 20.149.172.149, Ethernet25
 I L2     20.57.170.0/24 [115/20]
           via 20.170.172.170, Ethernet52/1
 I L2     20.57.179.0/24 [115/30]
           via 20.149.172.149, Ethernet25
 I L2     20.59.170.0/24 [115/20]
           via 20.170.172.170, Ethernet52/1
 I L2     20.111.149.0/24 [115/20]
           via 20.149.172.149, Ethernet25
 I L2     20.143.149.0/24 [115/20]
           via 20.149.172.149, Ethernet25
 I L2     20.149.155.0/24 [115/20]
           via 20.149.172.149, Ethernet25
 I L2     20.149.171.0/24 [115/20]
           via 20.149.172.149, Ethernet25
 C        20.149.172.0/24
           directly connected, Ethernet25
 I L2     20.149.179.0/24 [115/20]
           via 20.149.172.149, Ethernet25
 I L2     20.149.254.0/24 [115/20]
           via 20.149.172.149, Ethernet25
 I L2     20.155.170.0/24 [115/30]
           via 20.170.172.170, Ethernet52/1
 C        20.170.172.0/24
           directly connected, Ethernet52/1
 I L2     20.170.179.0/24 [115/20]
           via 20.170.172.170, Ethernet52/1
 I L2     20.170.212.0/24 [115/20]
           via 20.170.172.170, Ethernet52/1
 I L2     20.170.254.0/24 [115/20]
           via 20.170.172.170, Ethernet52/1
 I L2     31.9.1.0/24 [115/20]
           via 20.149.172.149, Ethernet25
 I L2     192.168.20.0/23 [115/20]
           via 20.149.172.149, Ethernet25
 I L2     192.168.0.0/19 [115/20]
           via 20.149.172.149, Ethernet25
 C        209.209.209.209/32
           directly connected, Loopback209


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
MPLS forwarding table (Label [metric] Vias) - 17 routes 
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
                    20.149.172.149 Ethernet25
 20019   A[1]
                via M, forward
                    EgressACL: apply
                    20.149.172.149 Ethernet25
 20024   A[1]
                via M, forward
                    EgressACL: apply
                    20.149.172.149 Ethernet25
 20032   A[1]
                via M, forward
                    EgressACL: apply
                    20.170.172.170 Ethernet52/1
 20047   A[1]
                via M, forward
                    EgressACL: apply
                    20.170.172.170 Ethernet52/1
 20050   A[1]
                via M, forward
                    EgressACL: apply
                    20.149.172.149 Ethernet25
 20057   A[1]
                via M, forward
                    EgressACL: apply
                    20.149.172.149 Ethernet25
 20059   A[1]
                via M, forward
                    EgressACL: apply
                    20.170.172.170 Ethernet52/1
 20170   A[1]
                via M, pop
                    EgressACL: apply
                    20.170.172.170 Ethernet52/1
 20171   A[1]
                via M, ::, pop
                    EgressACL: apply
                  via IS-IS SR tunnel index 12
                    via 20.149.172.149, Ethernet25, label 20171
 20212   A[1]
                via M, ::, pop
                    EgressACL: apply
                  via IS-IS SR tunnel index 17
                    via 20.170.172.170, Ethernet52/1, label 20212
 20343   A[1]
                via M, ::, pop
                    EgressACL: apply
                  via IS-IS SR tunnel index 2
                    via 20.149.172.149, Ethernet25, label 20343
 20349   A[1]
                via M, pop
                    EgressACL: apply
                    20.149.172.149 Ethernet25
 20355   A[1]
                via M, forward
                    EgressACL: apply
                    20.149.172.149 Ethernet25
 20379   A[1]
                via M, forward
                    EgressACL: apply
                    20.149.172.149 Ethernet25
 362144  A[1]
                via M, 20.149.172.149, pop
                    EgressACL: apply
                    directly connected, Ethernet25
                    c0:f8:7f:6a:4e:2a, vlan 1011
 362145  A[1]
                via M, 20.170.172.170, pop
                    EgressACL: apply
                    directly connected, Ethernet52/1
                    28:99:3a:06:b4:e1, vlan 1013
```

## show mpls lfib route

```text
MPLS forwarding table (Label [metric] Vias) - 17 routes 
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
                via M, 20.149.172.149, forward
                 payload autoDecide, ttlMode uniform, dscpMode uniform, apply egress-acl
                 interface Ethernet25
 IP    20019    [1], 10.0.0.19/32
                via M, 20.149.172.149, forward
                 payload autoDecide, ttlMode uniform, dscpMode uniform, apply egress-acl
                 interface Ethernet25
 IP    20024    [1], 10.0.0.24/32
                via M, 20.149.172.149, forward
                 payload autoDecide, ttlMode uniform, dscpMode uniform, apply egress-acl
                 interface Ethernet25
 IP    20032    [1], 10.0.0.32/32
                via M, 20.170.172.170, forward
                 payload autoDecide, ttlMode uniform, dscpMode uniform, apply egress-acl
                 interface Ethernet52/1
 IP    20047    [1], 10.0.0.47/32
                via M, 20.170.172.170, forward
                 payload autoDecide, ttlMode uniform, dscpMode uniform, apply egress-acl
                 interface Ethernet52/1
 IP    20050    [1], 10.0.0.50/32
                via M, 20.149.172.149, forward
                 payload autoDecide, ttlMode uniform, dscpMode uniform, apply egress-acl
                 interface Ethernet25
 IP    20057    [1], 10.0.0.57/32
                via M, 20.149.172.149, forward
                 payload autoDecide, ttlMode uniform, dscpMode uniform, apply egress-acl
                 interface Ethernet25
 IP    20059    [1], 10.0.0.59/32
                via M, 20.170.172.170, forward
                 payload autoDecide, ttlMode uniform, dscpMode uniform, apply egress-acl
                 interface Ethernet52/1
 IP    20170    [1], 10.0.0.170/32
                via M, 20.170.172.170, pop
                 payload autoDecide, ttlMode uniform, dscpMode uniform, apply egress-acl
                 interface Ethernet52/1
 I>BL  20171    [1], 10.0.0.171/32
                via IS-IS SR tunnel index 12, pop
                 payload autoDecide, ttlMode uniform, apply egress-acl
                    via 20.149.172.149, Ethernet25, label 20171
 I>BL  20212    [1], 10.0.0.212/32
                via IS-IS SR tunnel index 17, pop
                 payload autoDecide, ttlMode uniform, apply egress-acl
                    via 20.170.172.170, Ethernet52/1, label 20212
 I>BL  20343    [1], 10.0.1.43/32
                via IS-IS SR tunnel index 2, pop
                 payload autoDecide, ttlMode uniform, apply egress-acl
                    via 20.149.172.149, Ethernet25, label 20343
 IP    20349    [1], 10.0.1.49/32
                via M, 20.149.172.149, pop
                 payload autoDecide, ttlMode uniform, dscpMode uniform, apply egress-acl
                 interface Ethernet25
 IP    20355    [1], 10.0.1.55/32
                via M, 20.149.172.149, forward
                 payload autoDecide, ttlMode uniform, dscpMode uniform, apply egress-acl
                 interface Ethernet25
 IP    20379    [1], 10.0.0.179/32
                via M, 20.149.172.149, forward
                 payload autoDecide, ttlMode uniform, dscpMode uniform, apply egress-acl
                 interface Ethernet25
 IA    362144   [1]
                via M, 20.149.172.149, pop
                 payload autoDecide, ttlMode uniform, apply egress-acl
                 interface Ethernet25
 IA    362145   [1]
                via M, 20.170.172.170, pop
                 payload autoDecide, ttlMode uniform, apply egress-acl
                 interface Ethernet52/1
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
 * >  L   10.0.0.171/32          10.0.0.171            0       -          100     0       i
 * >  L   10.0.0.212/32          10.0.0.212            0       -          100     0       i
 * >  L   10.0.1.43/32           10.0.1.43             0       -          100     0       i
```

## show bgp neighbors

```text
BGP neighbor is 10.0.0.5, remote AS 65000, internal link
  BGP version 4, remote router ID 10.0.0.5, VRF default
  Inherits configuration from and member of peer-group BGP-LU-DOMAIN1
  Last read 17:13:15, last write 00:01:25
  Hold time is 180, keepalive interval is 60 seconds
  Configured hold time is 180, keepalive interval is 60 seconds
  Effective minimum hold time is 3 seconds
  Send failure hold time is 0 seconds
  Hold timer is inactive
  Keepalive timer is inactive
  Connect timer is active, time left: 00:01:09
  Connection interval is 148 seconds
  Failed connection attempts is 371
  Idle-restart timer is inactive
  BGP state is Active
  Number of transitions to established: 8
  Last state was Idle
  Last event was Start
  Last sent notification:Cease/administrative reset, Last time 17:18:12, First time 17:34:01, Repeats 6
  Last rcvd notification:Cease/peer de-configured, Last time 17:13:15
  Last sent socket-error:Connect (Network is unreachable), Last time 17:35:25, First time 17:37:02, Repeats 6
  Last rcvd socket-error:Connection reset by peer, Last time 00:01:25, First time 17:34:00, Repeats 388
  Types of communities advertised: standard extended
  Neighbor is a route reflector client (meshed)
  Neighbor is using cluster ID 1.1.1.1
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
  BGP session driven failover for IPv6 Unicast is disabled
  BGP session driven failover for IPv4 Unicast is disabled
  Message Statistics:
                         Sent      Rcvd
    Opens:                397         8
    Notifications:          7         1
    Updates:               41        16
    Keepalives:            32        23
    Route Refresh:          0         0
    Total messages:       477        48
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
  Outbound route map for IPv4 with MPLS Labels is ADD_ASN_65001
Local AS is 65000, local router ID 10.0.0.172
TTL is 255
Local TCP address is 10.0.0.172
Remote TCP address is 10.0.0.5, remote port is 179

BGP neighbor is 10.0.0.24, remote AS 65000, internal link
  BGP version 4, remote router ID 0.0.0.0, VRF default
  Inherits configuration from and member of peer-group BGP-LU-DOMAIN1
  Last read never, last write never
  Hold time is 0, keepalive interval is 0 seconds
  Configured hold time is 180, keepalive interval is 60 seconds
  Effective minimum hold time is 3 seconds
  Send failure hold time is 0 seconds
  Hold timer is inactive
  Keepalive timer is inactive
  Connect timer is active, time left: 00:01:12
  Connection interval is 148 seconds
  Failed connection attempts is 367
  Idle-restart timer is inactive
  BGP state is Active
  Number of transitions to established: 0
  Last state was Connect
  Last event was TransportError
  Last sent socket-error:Connect (Connection refused), Last time 00:01:31, First time 17:35:19, Repeats 425
  Types of communities advertised: standard extended
  Neighbor is a route reflector client (meshed)
  Neighbor is using cluster ID 1.1.1.1
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
  Outbound route map for IPv4 with MPLS Labels is ADD_ASN_65001
Local AS is 65000, local router ID 10.0.0.172
TTL is 255
Local TCP address is 10.0.0.172
Remote TCP address is 10.0.0.24, remote port is 179

BGP neighbor is 10.0.0.32, remote AS 65001, internal link
  BGP version 4, remote router ID 0.0.0.0, VRF default
  Inherits configuration from and member of peer-group BGP-LU-DOMAIN2
  Last read 00:00:08, last write 00:00:08
  Hold time is 0, keepalive interval is 0 seconds
  Configured hold time is 180, keepalive interval is 60 seconds
  Effective minimum hold time is 3 seconds
  Send failure hold time is 0 seconds
  Hold timer is inactive
  Keepalive timer is inactive
  Connect timer is active, time left: 00:02:45
  Connection interval is 148 seconds
  Failed connection attempts is 338
  Idle-restart timer is inactive
  BGP state is Active
  Peering failure hint: Cease/connection rejected
  Number of transitions to established: 0
  Last state was Idle
  Last event was Start
  Last rcvd notification:Cease/connection rejected, Last time 00:00:08, First time 16:40:11, Repeats 355
  Last sent socket-error:Connect (Network is unreachable), Last time 15:46:59, First time 15:50:01, Repeats 1
  Types of communities advertised: standard extended
  Neighbor is a route reflector client (meshed)
  Neighbor is using cluster ID 2.2.2.2
  Neighbor Capabilities:
    Multiprotocol IPv4 Unicast: advertised
    Multiprotocol IPv4 with MPLS Labels: advertised
    Four Octet ASN: advertised
    Route Refresh: advertised
    Enhanced route refresh: advertised
    Send End-of-RIB messages: advertised
    Additional-paths recv capability:
      IPv4 Unicast: advertised
      IPv4 with MPLS Labels: advertised
    Additional-paths send capability:
    Multiple labels capability:
      IPv4 with MPLS Labels: advertised with count 13
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
    Opens:                356         0
    Notifications:          0       356
    Updates:                0         0
    Keepalives:             0         0
    Route Refresh:          0         0
    Total messages:       356       356
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
  Outbound route map for IPv4 with MPLS Labels is ADD_ASN_65000
Local AS is 65001, local router ID 10.0.0.172
TTL is 255
Local TCP address is 10.0.0.172
Remote TCP address is 10.0.0.32, remote port is 179

BGP neighbor is 10.0.0.47, remote AS 65001, internal link
  BGP version 4, remote router ID 10.0.0.47, VRF default
  Inherits configuration from and member of peer-group BGP-LU-DOMAIN2
  Last read 16:47:49, last write 00:00:18
  Hold time is 180, keepalive interval is 60 seconds
  Configured hold time is 180, keepalive interval is 60 seconds
  Effective minimum hold time is 3 seconds
  Send failure hold time is 0 seconds
  Hold timer is inactive
  Keepalive timer is inactive
  Connect timer is active, time left: 00:01:01
  Connection interval is 64 seconds
  Failed connection attempts is 7
  Idle-restart timer is inactive
  BGP state is Active
  Number of transitions to established: 9
  Last state was Idle
  Last event was Start
  Last sent notification:Cease/administrative reset, Last time 17:03:37, First time 17:31:23, Repeats 7
  Last rcvd notification:Cease/administrative shutdown, Last time 16:47:49
  Last sent socket-error:Connect (Network is unreachable), Last time 00:01:52, First time 17:37:02, Repeats 21
  Last rcvd socket-error:Connection reset by peer, Last time 00:00:18, First time 16:47:48, Repeats 363
  Types of communities advertised: standard extended
  Neighbor is a route reflector client (meshed)
  Neighbor is using cluster ID 2.2.2.2
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
    Graceful Restart received:
      Restart-time is 120
      Restart-State bit: no
      Graceful notification: no
      IPv4 Unicast is enabled, Forwarding State is preserved
      IPv4 with MPLS Labels is enabled, Forwarding State is preserved
    Multiple labels capability:
      IPv4 with MPLS Labels: advertised with count 13
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
    Opens:                373         9
    Notifications:          8         1
    Updates:               56        27
    Keepalives:            61        49
    Route Refresh:          0         0
    Total messages:       498        86
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
  Outbound route map for IPv4 with MPLS Labels is ADD_ASN_65000
Local AS is 65001, local router ID 10.0.0.172
TTL is 255
Local TCP address is 10.0.0.172
Remote TCP address is 10.0.0.47, remote port is 179

BGP neighbor is 10.0.0.59, remote AS 65001, internal link
  BGP version 4, remote router ID 10.0.0.59, VRF default
  Inherits configuration from and member of peer-group BGP-LU-DOMAIN2
  Last read 17:26:33, last write 00:00:19
  Hold time is 90, keepalive interval is 30 seconds
  Configured hold time is 180, keepalive interval is 60 seconds
  Effective minimum hold time is 3 seconds
  Send failure hold time is 0 seconds
  Hold timer is inactive
  Keepalive timer is inactive
  Connect timer is active, time left: 00:00:51
  Connection interval is 64 seconds
  Failed connection attempts is 7
  Idle-restart timer is inactive
  BGP state is Active
  Number of transitions to established: 6
  Last state was Idle
  Last event was Start
  Last sent notification:Cease/administrative reset, Last time 17:27:22, First time 17:31:21, Repeats 4
  Last rcvd notification:Cease/administrative shutdown, Last time 17:26:33
  Last sent socket-error:Broken pipe, Last time 00:00:19, First time 00:01:47, Repeats 3
  Last rcvd socket-error:Connection reset by peer, Last time 00:01:33, First time 17:29:06, Repeats 230
  Types of communities advertised: standard extended
  Neighbor is a route reflector client (meshed)
  Neighbor is using cluster ID 2.2.2.2
  Neighbor Capabilities:
    Multiprotocol IPv4 Unicast: advertised
    Multiprotocol IPv4 with MPLS Labels: advertised and received
    Four Octet ASN: advertised and received
    Route Refresh: advertised and received
    Enhanced route refresh: advertised
    Send End-of-RIB messages: advertised and received
    Additional-paths recv capability:
      IPv4 Unicast: advertised
      IPv4 with MPLS Labels: advertised
    Additional-paths send capability:
    Multiple labels capability:
      IPv4 with MPLS Labels: advertised with count 13
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
    Opens:                396         6
    Notifications:          5         1
    Updates:               20        12
    Keepalives:            20        20
    Route Refresh:          0         0
    Total messages:       441        39
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
  Outbound route map for IPv4 with MPLS Labels is ADD_ASN_65000
Local AS is 65001, local router ID 10.0.0.172
TTL is 255
Local TCP address is 10.0.0.172
Remote TCP address is 10.0.0.59, remote port is 179

BGP neighbor is 10.0.0.171, remote AS 65000, internal link
  BGP version 4, remote router ID 10.0.0.171, VRF default
  Inherits configuration from and member of peer-group BGP-LU-DOMAIN1
  Last read 00:00:02, last write 00:00:15
  Hold time is 180, keepalive interval is 60 seconds
  Configured hold time is 180, keepalive interval is 60 seconds
  Effective minimum hold time is 3 seconds
  Send failure hold time is 0 seconds
  Hold timer is active, time left: 00:02:58
  Keepalive timer is active, time left: 00:00:43
  Connect timer is inactive
  Idle-restart timer is inactive
  BGP state is Established, up for 00:54:24
  Number of transitions to established: 12
  Last state was OpenConfirm
  Last event was RecvUpdate
  Last sent notification:Cease/administrative reset, Last time 17:03:37, First time 17:34:01, Repeats 9
  Last rcvd notification:Cease/connection rejected, Last time 00:54:30, First time 16:47:47, Repeats 342
  Last sent socket-error:Connect (Network is unreachable), Last time 17:35:19, First time 17:37:02, Repeats 7
  Types of communities advertised: standard extended
  Enhanced route refresh stale path removal disabled
  Outbound enhanced route refresh enabled
  Neighbor is a route reflector client (meshed)
  Neighbor is using cluster ID 1.1.1.1
  Neighbor Capabilities:
    Multiprotocol IPv4 Unicast: advertised and received and negotiated
    Multiprotocol IPv4 with MPLS Labels: advertised and received and negotiated
    Four Octet ASN: advertised and received and negotiated
    Route Refresh: advertised and received and negotiated
    Enhanced route refresh: advertised and received and negotiated
    Send End-of-RIB messages: advertised and received and negotiated
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
    IPv4 Unicast End-of-RIB received: Yes
      Received 00:54:24
      Number of stale paths removed after graceful restart: 0
    IPv4 with MPLS Labels End-of-RIB received: Yes
      Received 00:54:24
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
    Opens:                         355        12
    Notifications:                  10       344
    Updates:                        77        32
    Keepalives:                    131       137
    Enhanced Route Refresh:          0         0
    Begin of Route Refresh:          0         0
    End of Route Refresh:            0         0
    Total messages:                573       525
  Prefix Statistics:
                                   Sent      Rcvd     Best Paths     Best ECMP Paths
    IPv4 Unicast:                     0         0              0                   0
    IPv4 with MPLS Labels:            1         1              1                   0
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
    IPv4 labeled-unicast NLRIs dropped due to maximum route limit violation: 0
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
  Outbound route map for IPv4 with MPLS Labels is ADD_ASN_65001
Local AS is 65000, local router ID 10.0.0.172
TTL is 255
Local TCP address is 10.0.0.172, local port is 179
Remote TCP address is 10.0.0.171, remote port is 46759
Local next hop for next hop self:
  IPv4 Unicast: 10.0.0.172
  IPv4 with MPLS Labels: 209.209.209.209
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
    Round-trip Time (rtt/rtvar): 0.2ms/0.0ms
    Delayed Ack Timeout (ato): 40.0ms
    Congestion Window (cwnd): 10
    TCP Throughput: 559.61 Mbps
    Advertised Recv Window (rcv_space): 14600

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

BGP neighbor is 10.0.0.212, remote AS 65001, internal link
  BGP version 4, remote router ID 10.0.0.212, VRF default
  Inherits configuration from and member of peer-group BGP-LU-DOMAIN2
  Last read 00:00:24, last write 00:00:05
  Hold time is 90, keepalive interval is 30 seconds
  Configured hold time is 180, keepalive interval is 60 seconds
  Effective minimum hold time is 3 seconds
  Send failure hold time is 0 seconds
  Hold timer is active, time left: 00:01:06
  Keepalive timer is active, time left: 00:00:17
  Connect timer is inactive
  Idle-restart timer is inactive
  BGP state is Established, up for 00:01:47
  Number of transitions to established: 9
  Last state was OpenConfirm
  Last event was RecvUpdate
  Last sent notification:Hold Timer Expired Error/None, Last time 00:06:01
  Last sent socket-error:Connect (Network is unreachable), Last time 00:01:52, First time 17:37:02, Repeats 29
  Last rcvd socket-error:Connection reset by peer, Last time 17:29:06
  Types of communities advertised: standard extended
  Neighbor is a route reflector client (meshed)
  Neighbor is using cluster ID 2.2.2.2
  Neighbor Capabilities:
    Multiprotocol IPv4 Unicast: advertised
    Multiprotocol IPv4 with MPLS Labels: advertised and received and negotiated
    Four Octet ASN: advertised and received and negotiated
    Route Refresh: advertised and received and negotiated
    Enhanced route refresh: advertised
    Send End-of-RIB messages: advertised and received and negotiated
    Additional-paths recv capability:
      IPv4 Unicast: advertised
      IPv4 with MPLS Labels: advertised
    Additional-paths send capability:
    Long Lived Graceful Restart received:
      Helper only
    Multiple labels capability:
      IPv4 with MPLS Labels: advertised with count 13
  Restart timer is inactive
  End of rib timer is inactive
    IPv4 with MPLS Labels End-of-RIB received: Yes
      Received 00:01:46
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
    Opens:                  9         9
    Notifications:          8         0
    Updates:               52        19
    Keepalives:          2462      2291
    Route Refresh:          0         0
    Total messages:      2531      2319
  Prefix Statistics:
                                   Sent      Rcvd     Best Paths     Best ECMP Paths
    IPv4 Unicast:                     0         0              0                   0
    IPv4 with MPLS Labels:            2         1              1                   0
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
    IPv4 labeled-unicast NLRIs dropped due to maximum route limit violation: 0
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
  Outbound route map for IPv4 with MPLS Labels is ADD_ASN_65000
Local AS is 65001, local router ID 10.0.0.172
TTL is 255
Local TCP address is 10.0.0.172, local port is 43811
Remote TCP address is 10.0.0.212, remote port is 179
Local next hop for next hop self:
  IPv4 with MPLS Labels: 209.209.209.209
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
    Round-trip Time (rtt/rtvar): 2.4ms/4.0ms
    Delayed Ack Timeout (ato): 40.0ms
    Congestion Window (cwnd): 10
    TCP Throughput: 47.63 Mbps
    Advertised Recv Window (rcv_space): 14480

BGP neighbor is 10.0.0.254, remote AS 65000, internal link
  BGP version 4, remote router ID 0.0.0.0, VRF default
  Inherits configuration from and member of peer-group BGP-LU-DOMAIN1
  Last read never, last write never
  Hold time is 0, keepalive interval is 0 seconds
  Configured hold time is 180, keepalive interval is 60 seconds
  Effective minimum hold time is 3 seconds
  Send failure hold time is 0 seconds
  Hold timer is inactive
  Keepalive timer is inactive
  Connect timer is active, time left: 00:02:27
  Connection interval is 148 seconds
  Failed connection attempts is 369
  Idle-restart timer is inactive
  BGP state is Active
  Number of transitions to established: 0
  Last state was Connect
  Last event was TransportError
  Last sent socket-error:Connect (Network is unreachable), Last time 00:00:23, First time 00:28:34, Repeats 10
  Types of communities advertised: standard extended
  Neighbor is a route reflector client (meshed)
  Neighbor is using cluster ID 1.1.1.1
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
  Outbound route map for IPv4 with MPLS Labels is ADD_ASN_65001
Local AS is 65000, local router ID 10.0.0.172
TTL is 255
Local TCP address is 10.0.0.172
Remote TCP address is 10.0.0.254, remote port is 179

BGP neighbor is 10.0.1.43, remote AS 65000, internal link
  BGP version 4, remote router ID 10.0.1.43, VRF default
  Inherits configuration from and member of peer-group BGP-LU-DOMAIN1
  Last read 00:00:32, last write 00:00:48
  Hold time is 180, keepalive interval is 60 seconds
  Configured hold time is 180, keepalive interval is 60 seconds
  Effective minimum hold time is 3 seconds
  Send failure hold time is 0 seconds
  Hold timer is active, time left: 00:02:28
  Keepalive timer is active, time left: 00:00:05
  Connect timer is inactive
  Idle-restart timer is inactive
  BGP state is Established, up for 00:48:37
  Number of transitions to established: 2
  Last state was OpenConfirm
  Last event was RecvKeepAlive
  Last sent notification:Cease/connection rejected, Last time 16:57:57, First time 17:35:14, Repeats 99
  Last rcvd notification:Cease/administrative shutdown, Last time 16:45:45
  Last sent socket-error:Connect (Connection refused), Last time 00:49:55, First time 16:45:39, Repeats 343
  Last rcvd socket-error:Connection reset by peer, Last time 16:45:44
  Types of communities advertised: standard extended
  Neighbor is a route reflector client (meshed)
  Neighbor is using cluster ID 1.1.1.1
  Neighbor Capabilities:
    Multiprotocol IPv4 Unicast: advertised
    Multiprotocol IPv4 with MPLS Labels: advertised and received and negotiated
    Four Octet ASN: advertised and received and negotiated
    Route Refresh: advertised and received and negotiated
    Enhanced route refresh: advertised
    Send End-of-RIB messages: advertised
    Additional-paths recv capability:
      IPv4 Unicast: advertised
      IPv4 with MPLS Labels: advertised
    Additional-paths send capability:
    Multiple labels capability:
      IPv4 with MPLS Labels: advertised with count 13
    Extended Next-Hop Capability:
      IPv4 Unicast: received
      VPN-IPv4: received
  Restart timer is inactive
  End of rib timer is inactive
    IPv4 with MPLS Labels End-of-RIB received: No
      Number of stale paths removed after graceful restart: 0
  AIGP attribute send and receive for IPv4 Unicast are enabled
  AIGP attribute send and receive for IPv4 with MPLS Labels are enabled
  AIGP attribute send and receive for IPv6 Unicast are enabled
  AIGP attribute send and receive for IPv6 with MPLS Labels are enabled
  BGP session driven failover for IPv6 Unicast is disabled
  BGP session driven failover for IPv4 Unicast is disabled
  Message Statistics:
                         Sent      Rcvd
    Opens:                  3       102
    Notifications:        100         1
    Updates:                6         4
    Keepalives:            72        61
    Route Refresh:          0         0
    Total messages:       181       168
  Prefix Statistics:
                                   Sent      Rcvd     Best Paths     Best ECMP Paths
    IPv4 Unicast:                     0         0              0                   0
    IPv4 with MPLS Labels:            1         1              1                   0
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
    IPv4 labeled-unicast NLRIs dropped due to maximum route limit violation: 0
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
  Outbound route map for IPv4 with MPLS Labels is ADD_ASN_65001
Local AS is 65000, local router ID 10.0.0.172
TTL is 255
Local TCP address is 10.0.0.172, local port is 179
Remote TCP address is 10.0.1.43, remote port is 34368
Local next hop for next hop self:
  IPv4 with MPLS Labels: 209.209.209.209
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
    Retransmission Timeout (rto): 388.0ms
    Round-trip Time (rtt/rtvar): 186.5ms/15.9ms
    Delayed Ack Timeout (ato): 40.0ms
    Congestion Window (cwnd): 10
    TCP Throughput: 0.53 Mbps
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

BGP neighbor is 100.0.1.111, remote AS 65000, internal link
  BGP version 4, remote router ID 0.0.0.0, VRF default
  Inherits configuration from and member of peer-group BGP-LU-DOMAIN1
  Last read never, last write 00:10:58
  Hold time is 0, keepalive interval is 0 seconds
  Configured hold time is 180, keepalive interval is 60 seconds
  Effective minimum hold time is 3 seconds
  Send failure hold time is 0 seconds
  Hold timer is inactive
  Keepalive timer is inactive
  Connect timer is active, time left: 00:02:10
  Connection interval is 148 seconds
  Failed connection attempts is 314
  Idle-restart timer is inactive
  BGP state is Active
  Number of transitions to established: 0
  Last state was Connect
  Last event was TransportError
  Last sent socket-error:Connect (Network is unreachable), Last time 00:00:20, First time 17:37:02, Repeats 19
  Last rcvd socket-error:Connection reset by peer, Last time 00:10:58, First time 17:35:23, Repeats 445
  Types of communities advertised: standard extended
  Neighbor is a route reflector client (meshed)
  Neighbor is using cluster ID 1.1.1.1
  Neighbor Capabilities:
    Multiprotocol IPv4 Unicast: advertised
    Multiprotocol IPv4 with MPLS Labels: advertised
    Four Octet ASN: advertised
    Route Refresh: advertised
    Enhanced route refresh: advertised
    Send End-of-RIB messages: advertised
    Additional-paths recv capability:
      IPv4 Unicast: advertised
      IPv4 with MPLS Labels: advertised
    Additional-paths send capability:
    Multiple labels capability:
      IPv4 with MPLS Labels: advertised with count 13
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
    Opens:                446         0
    Notifications:          0         0
    Updates:                0         0
    Keepalives:             0         0
    Route Refresh:          0         0
    Total messages:       446         0
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
  Outbound route map for IPv4 with MPLS Labels is ADD_ASN_65001
Local AS is 65000, local router ID 10.0.0.172
TTL is 255
Local TCP address is 10.0.0.172
Remote TCP address is 100.0.1.111, remote port is 179

```

## show tunnel rib system-tunnel-rib brief

```text
Tunnel RIB: system-tunnel-rib
Endpoint        Tunnel Type     Index(es)   Tunnel Preference   IGP Preference 
-------------- --------------- ----------- ------------------- ----------------
10.0.0.5/32     IS-IS SR IPv4   9           30                  115            
10.0.0.19/32    IS-IS SR IPv4   3           30                  115            
10.0.0.24/32    IS-IS SR IPv4   8           30                  115            
10.0.0.32/32    IS-IS SR IPv4   15          30                  115            
10.0.0.47/32    IS-IS SR IPv4   16          30                  115            
10.0.0.50/32    IS-IS SR IPv4   5           30                  115            
10.0.0.57/32    IS-IS SR IPv4   11          30                  115            
10.0.0.59/32    IS-IS SR IPv4   14          30                  115            
10.0.0.170/32   IS-IS SR IPv4   13          30                  115            
10.0.0.171/32   IS-IS SR IPv4   12          30                  115            
10.0.0.179/32   IS-IS SR IPv4   7           30                  115            
10.0.0.212/32   IS-IS SR IPv4   17          30                  115            
10.0.1.43/32    IS-IS SR IPv4   2           30                  115            
10.0.1.49/32    IS-IS SR IPv4   1           30                  115            
10.0.1.55/32    IS-IS SR IPv4   4           30                  115            

   IGP Metric    Metric Type
---------------- -----------
   20            metric     
   20            metric     
   20            metric     
   15            metric     
   30            metric     
   30            metric     
   20            metric     
   20            metric     
   20            metric     
   20            metric     
   20            metric     
   20            metric     
   20            metric     
   10            metric     
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
>C    10.0.0.172/32 [0 pref/0 metric] updated 17:37:19 ago
         via Loopback0, directly connected
>C    20.149.172.0/24 [0 pref/0 metric] updated 17:35:25 ago
         via Ethernet25, directly connected
>C    20.170.172.0/24 [0 pref/0 metric] updated 00:02:02 ago
         via Ethernet52/1, directly connected
>C    209.209.209.209/32 [0 pref/0 metric] updated 17:37:19 ago
         via Loopback209, directly connected
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
 B    10.0.0.171/32 [200 pref/0 MED] updated 00:54:25 ago
         via BGP LU Forwarding IPv4 Tunnel index 90
            via IS-IS SR Tunnel index 12 label 3
               via ::, NextLevelFecId2493952.5 label 20171 [NF]
 B    10.0.0.212/32 [200 pref/0 MED] updated 00:01:48 ago
         via BGP LU Forwarding IPv4 Tunnel index 94
            via IS-IS SR Tunnel index 17 label 3
               via ::, NextLevelFecId2493952.7 label 20212 [NF]
 B    10.0.1.43/32 [200 pref/0 MED] updated 00:48:33 ago
         via BGP LU Forwarding IPv4 Tunnel index 92
            via IS-IS SR Tunnel index 2 label 3
               via ::, NextLevelFecId2493952.5 label 20343 [NF]
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
>P    0.0.0.0/8 [1 pref/0 metric] updated 17:37:17 ago
         via Null0, directly connected [NF]
>P    127.0.0.0/8 [1 pref/0 metric] updated 17:37:17 ago
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
>I    10.0.0.5/32 [115 pref/20 metric] updated 17:31:28 ago
         via 20.149.172.149, Ethernet25
>I    10.0.0.19/32 [115 pref/20 metric] updated 17:09:18 ago
         via 20.149.172.149, Ethernet25
>I    10.0.0.24/32 [115 pref/20 metric] updated 17:35:25 ago
         via 20.149.172.149, Ethernet25
>I    10.0.0.32/32 [115 pref/15 metric] updated 00:01:53 ago
         via 20.170.172.170, Ethernet52/1
>I    10.0.0.47/32 [115 pref/30 metric] updated 00:01:53 ago
         via 20.170.172.170, Ethernet52/1
>I    10.0.0.50/32 [115 pref/30 metric] updated 17:35:25 ago
         via 20.149.172.149, Ethernet25
>I    10.0.0.57/32 [115 pref/20 metric] updated 16:09:07 ago
         via 20.149.172.149, Ethernet25
>I    10.0.0.59/32 [115 pref/20 metric] updated 00:01:53 ago
         via 20.170.172.170, Ethernet52/1
>I    10.0.0.170/32 [115 pref/20 metric] updated 00:01:53 ago
         via 20.170.172.170, Ethernet52/1
>I    10.0.0.171/32 [115 pref/20 metric] updated 17:35:20 ago
         via 20.149.172.149, Ethernet25
>I    10.0.0.179/32 [115 pref/20 metric] updated 17:35:25 ago
         via 20.149.172.149, Ethernet25
>I    10.0.0.212/32 [115 pref/20 metric] updated 00:01:53 ago
         via 20.170.172.170, Ethernet52/1
>I    10.0.1.24/32 [115 pref/20 metric] updated 00:03:27 ago
         via 20.149.172.149, Ethernet25
>I    10.0.1.43/32 [115 pref/20 metric] updated 17:35:25 ago
         via 20.149.172.149, Ethernet25
>I    10.0.1.49/32 [115 pref/10 metric] updated 17:35:25 ago
         via 20.149.172.149, Ethernet25
>I    10.0.1.55/32 [115 pref/20 metric] updated 17:35:25 ago
         via 20.149.172.149, Ethernet25
>I    20.5.149.0/24 [115 pref/20 metric] updated 17:35:25 ago
         via 20.149.172.149, Ethernet25
>I    20.5.170.0/24 [115 pref/20 metric] updated 00:01:53 ago
         via 20.170.172.170, Ethernet52/1
>I    20.19.149.0/24 [115 pref/20 metric] updated 17:35:25 ago
         via 20.149.172.149, Ethernet25
>I    20.24.149.0/24 [115 pref/20 metric] updated 17:35:25 ago
         via 20.149.172.149, Ethernet25
>I    20.32.149.0/24 [115 pref/20 metric] updated 15:44:23 ago
         via 20.149.172.149, Ethernet25
>I    20.32.155.0/24 [115 pref/30 metric] updated 17:35:25 ago
         via 20.149.172.149, Ethernet25
>I    20.32.170.0/24 [115 pref/15 metric] updated 00:01:53 ago
         via 20.170.172.170, Ethernet52/1
>I    20.47.170.0/24 [115 pref/20 metric] updated 00:01:53 ago
         via 20.170.172.170, Ethernet52/1
>I    20.50.149.0/24 [115 pref/20 metric] updated 17:35:25 ago
         via 20.149.172.149, Ethernet25
>I    20.57.149.0/24 [115 pref/20 metric] updated 17:35:25 ago
         via 20.149.172.149, Ethernet25
>I    20.57.155.0/24 [115 pref/30 metric] updated 17:35:25 ago
         via 20.149.172.149, Ethernet25
>I    20.57.170.0/24 [115 pref/20 metric] updated 00:01:53 ago
         via 20.170.172.170, Ethernet52/1
>I    20.57.179.0/24 [115 pref/30 metric] updated 17:35:25 ago
         via 20.149.172.149, Ethernet25
>I    20.59.170.0/24 [115 pref/20 metric] updated 00:01:53 ago
         via 20.170.172.170, Ethernet52/1
>I    20.111.149.0/24 [115 pref/20 metric] updated 17:35:25 ago
         via 20.149.172.149, Ethernet25
>I    20.143.149.0/24 [115 pref/20 metric] updated 17:35:25 ago
         via 20.149.172.149, Ethernet25
>I    20.149.155.0/24 [115 pref/20 metric] updated 17:35:25 ago
         via 20.149.172.149, Ethernet25
>I    20.149.171.0/24 [115 pref/20 metric] updated 17:35:22 ago
         via 20.149.172.149, Ethernet25
>I    20.149.179.0/24 [115 pref/20 metric] updated 17:35:25 ago
         via 20.149.172.149, Ethernet25
>I    20.149.254.0/24 [115 pref/20 metric] updated 00:24:41 ago
         via 20.149.172.149, Ethernet25
>I    20.155.170.0/24 [115 pref/30 metric] updated 00:01:53 ago
         via 20.170.172.170, Ethernet52/1
>I    20.170.179.0/24 [115 pref/20 metric] updated 00:01:53 ago
         via 20.170.172.170, Ethernet52/1
>I    20.170.212.0/24 [115 pref/20 metric] updated 00:01:53 ago
         via 20.170.172.170, Ethernet52/1
>I    20.170.254.0/24 [115 pref/20 metric] updated 00:01:53 ago
         via 20.170.172.170, Ethernet52/1
>I    31.9.1.0/24 [115 pref/20 metric] updated 17:09:18 ago
         via 20.149.172.149, Ethernet25
>I    192.168.0.0/19 [115 pref/20 metric] updated 17:09:18 ago
         via 20.149.172.149, Ethernet25
>I    192.168.20.0/23 [115 pref/20 metric] updated 17:35:25 ago
         via 20.149.172.149, Ethernet25
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
>P    ::/96 [1 pref/0 metric] updated 17:37:17 ago
         via Null0, directly connected [NF]
>P    ::ffff:127.0.0.0/104 [1 pref/0 metric] updated 17:37:17 ago
         via :: [1 pref/1 metric] type ipv6
            via , directly connected
>P    fe80::/10 [1 pref/0 metric] updated 17:37:17 ago
```

## show platform sand l3 summary

```text
Number of vrfs: 8

Ipv4:
  Routes:       71  backlog:  0  unprogrammed:  0
  Adjacencies:  38  backlog:  0  unprogrammed:  0
Ipv6:
  Routes:       4   backlog:  0  unprogrammed:  0
  Adjacencies:  38  backlog:  0  unprogrammed:  0
Mpls:
  Routes:       17  backlog:  0  unprogrammed:  0
  Adjacencies:  2   backlog:  0  unprogrammed:  0

Jericho2 Ip Fecs:
  Non-ecmp fecs:  4115  ecmp fecs:  0  fec entries:  4115
Jericho2 Mpls Fecs:
  Non-ecmp fecs:  2  ecmp fecs:  0  fec entries:  2
Jericho2 Vxlan Tunnel Fecs:
  Non-ecmp fecs:  0  ecmp fecs:  0  fec entries:  0
  Number of vxlan tunnels configured: 0

Jericho2 Lpm Routes:
  Routes:   71  unprogrammed:   0   
  Routes6:  4   unprogrammed6:  0   
  Backlog:  0 

Jericho2 Lpm:
  TCAM entries used:   3   Percent free:  99  ADS2 entries used:   6  Percent free:  99
  Pivot buckets used:  4   Rows used:     1   Entries Per Bucket:  1  Percent free:  99
  Route buckets used:  12  Rows used:     3   Entries Per Bucket:  6  Percent free:  99

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
  FixedSystem: 3
Egress Sflow rewrite entries in use (in each fap):
  FixedSystem: 0

Egress rewrite chains in backlog: resource-full 0, no-interface 0

Glem entries used per fap :
  FixedSystem: 4101

Jericho2 Fec:
  Maximum FEC hierarchy levels:  3
  ReusedEcmp:  0  allocs:  136  frees:  117  shuffles:  0  cmds:  0
  Zombies:     0    purges:    0
  Quarantine:  0/0  shuffles:  0  deletes:  0   
  Fec insertion failures:  0
  Level1  Fecs:
    Non-ecmp fecs:            6   ecmp fecs:            1 
    Non-ecmp (Percent free):  99  ecmp (Percent free):  99
  Level2  Fecs:
    Non-ecmp fecs:            28  ecmp fecs:            0  
    Non-ecmp (Percent free):  99  ecmp (Percent free):  100
  Level3  Fecs:
    Non-ecmp fecs:            4   ecmp fecs:            0  
    Non-ecmp (Percent free):  99  ecmp (Percent free):  100

Lpm Detail:
  Requests:  192  cleanses:  59  batches:  59  avg batch size:  3

Jericho Arp:
  ArpTable writes:      17404  queued      0   
  IngressTable writes:  75118  queued      0   
  Coprocessors:         1      in CmdRing

Tunnel Counter Status
  Number of MPLS tunnels:                  3    
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
|0  |10.0.0.5/32       |ROUTE| Et25               |1011 |103421  | c0:f8:7f:6a:4e:2a |  -  |288364|   -   
|0  |10.0.0.19/32      |ROUTE| Et25               |1011 |103421  | c0:f8:7f:6a:4e:2a |  -  |288364|   -   
|0  |10.0.0.24/32      |ROUTE| Et25               |1011 |103421  | c0:f8:7f:6a:4e:2a |  -  |288364|   -   
|0  |10.0.0.32/32      |ROUTE| Et52/1             |1013 |103422  | 28:99:3a:06:b4:e1 |  -  |288380|   -   
|0  |10.0.0.47/32      |ROUTE| Et52/1             |1013 |103422  | 28:99:3a:06:b4:e1 |  -  |288380|   -   
|0  |10.0.0.50/32      |ROUTE| Et25               |1011 |103421  | c0:f8:7f:6a:4e:2a |  -  |288364|   -   
|0  |10.0.0.57/32      |ROUTE| Et25               |1011 |103421  | c0:f8:7f:6a:4e:2a |  -  |288364|   -   
|0  |10.0.0.59/32      |ROUTE| Et52/1             |1013 |103422  | 28:99:3a:06:b4:e1 |  -  |288380|   -   
|0  |10.0.0.170/32     |ROUTE| Et52/1             |1013 |103422  | 28:99:3a:06:b4:e1 |  -  |288380|   -   
|0  |10.0.0.171/32     |ROUTE| Et25               |1011 |103421  | c0:f8:7f:6a:4e:2a |  -  |288364|   -   
|0  |10.0.0.172/32     |TRAP | CoppSystemIpUcast  |0    |  -     | Receive           |  -  |524291|   -   
|0  |10.0.0.179/32     |ROUTE| Et25               |1011 |103421  | c0:f8:7f:6a:4e:2a |  -  |288364|   -   
|0  |10.0.0.212/32     |ROUTE| Et52/1             |1013 |103422  | 28:99:3a:06:b4:e1 |  -  |288380|   -   
|0  |10.0.1.24/32      |ROUTE| Et25               |1011 |103421  | c0:f8:7f:6a:4e:2a |  -  |288364|   -   
|0  |10.0.1.43/32      |ROUTE| Et25               |1011 |103421  | c0:f8:7f:6a:4e:2a |  -  |288364|   -   
|0  |10.0.1.49/32      |ROUTE| Et25               |1011 |103421  | c0:f8:7f:6a:4e:2a |  -  |288364|   -   
|0  |10.0.1.55/32      |ROUTE| Et25               |1011 |103421  | c0:f8:7f:6a:4e:2a |  -  |288364|   -   
|0  |20.5.149.0/24     |ROUTE| Et25               |1011 |103421  | c0:f8:7f:6a:4e:2a |  -  |288364|   -   
|0  |20.5.170.0/24     |ROUTE| Et52/1             |1013 |103422  | 28:99:3a:06:b4:e1 |  -  |288380|   -   
|0  |20.19.149.0/24    |ROUTE| Et25               |1011 |103421  | c0:f8:7f:6a:4e:2a |  -  |288364|   -   
|0  |20.24.149.0/24    |ROUTE| Et25               |1011 |103421  | c0:f8:7f:6a:4e:2a |  -  |288364|   -   
|0  |20.32.149.0/24    |ROUTE| Et25               |1011 |103421  | c0:f8:7f:6a:4e:2a |  -  |288364|   -   
|0  |20.32.155.0/24    |ROUTE| Et25               |1011 |103421  | c0:f8:7f:6a:4e:2a |  -  |288364|   -   
|0  |20.32.170.0/24    |ROUTE| Et52/1             |1013 |103422  | 28:99:3a:06:b4:e1 |  -  |288380|   -   
|0  |20.47.170.0/24    |ROUTE| Et52/1             |1013 |103422  | 28:99:3a:06:b4:e1 |  -  |288380|   -   
|0  |20.50.149.0/24    |ROUTE| Et25               |1011 |103421  | c0:f8:7f:6a:4e:2a |  -  |288364|   -   
|0  |20.57.149.0/24    |ROUTE| Et25               |1011 |103421  | c0:f8:7f:6a:4e:2a |  -  |288364|   -   
|0  |20.57.155.0/24    |ROUTE| Et25               |1011 |103421  | c0:f8:7f:6a:4e:2a |  -  |288364|   -   
|0  |20.57.170.0/24    |ROUTE| Et52/1             |1013 |103422  | 28:99:3a:06:b4:e1 |  -  |288380|   -   
|0  |20.57.179.0/24    |ROUTE| Et25               |1011 |103421  | c0:f8:7f:6a:4e:2a |  -  |288364|   -   
|0  |20.59.170.0/24    |ROUTE| Et52/1             |1013 |103422  | 28:99:3a:06:b4:e1 |  -  |288380|   -   
|0  |20.111.149.0/24   |ROUTE| Et25               |1011 |103421  | c0:f8:7f:6a:4e:2a |  -  |288364|   -   
|0  |20.143.149.0/24   |ROUTE| Et25               |1011 |103421  | c0:f8:7f:6a:4e:2a |  -  |288364|   -   
|0  |20.149.155.0/24   |ROUTE| Et25               |1011 |103421  | c0:f8:7f:6a:4e:2a |  -  |288364|   -   
|0  |20.149.171.0/24   |ROUTE| Et25               |1011 |103421  | c0:f8:7f:6a:4e:2a |  -  |288364|   -   
|0  |20.149.172.0/32   |TRAP | CoppSystemIpBcast  |0    |  -     | BcastReceive      |  -  |524288|   -   
|0  |20.149.172.149/32 |ROUTE| Et25               |1011 |103421  | c0:f8:7f:6a:4e:2a |  -  |288368|   -   
|0  |20.149.172.172/32 |TRAP | CoppSystemIpUcast  |0    |  -     | Receive           |  -  |524291|   -   
|0  |20.149.172.255/32 |TRAP | CoppSystemIpBcast  |0    |  -     | BcastReceive      |  -  |524288|   -   
|0  |20.149.172.0/24   |TRAP | CoppSystemL3DstMiss|1011 |1011    | ArpTrap           |  -  |525305|   -   
|0  |20.149.179.0/24   |ROUTE| Et25               |1011 |103421  | c0:f8:7f:6a:4e:2a |  -  |288364|   -   
|0  |20.149.254.0/24   |ROUTE| Et25               |1011 |103421  | c0:f8:7f:6a:4e:2a |  -  |288364|   -   
|0  |20.155.170.0/24   |ROUTE| Et52/1             |1013 |103422  | 28:99:3a:06:b4:e1 |  -  |288380|   -   
|0  |20.170.172.0/32   |TRAP | CoppSystemIpBcast  |0    |  -     | BcastReceive      |  -  |524288|   -   
|0  |20.170.172.170/32 |ROUTE| Et52/1             |1013 |103422  | 28:99:3a:06:b4:e1 |  -  |288378|   -   
|0  |20.170.172.172/32 |TRAP | CoppSystemIpUcast  |0    |  -     | Receive           |  -  |524291|   -   
|0  |20.170.172.255/32 |TRAP | CoppSystemIpBcast  |0    |  -     | BcastReceive      |  -  |524288|   -   
|0  |20.170.172.0/24   |TRAP | CoppSystemL3DstMiss|1013 |1013    | ArpTrap           |  -  |525307|   -   
|0  |20.170.179.0/24   |ROUTE| Et52/1             |1013 |103422  | 28:99:3a:06:b4:e1 |  -  |288380|   -   
|0  |20.170.212.0/24   |ROUTE| Et52/1             |1013 |103422  | 28:99:3a:06:b4:e1 |  -  |288380|   -   
|0  |20.170.254.0/24   |ROUTE| Et52/1             |1013 |103422  | 28:99:3a:06:b4:e1 |  -  |288380|   -   
|0  |31.9.1.0/24       |ROUTE| Et25               |1011 |103421  | c0:f8:7f:6a:4e:2a |  -  |288364|   -   
|0  |127.0.0.0/8       |TRAP | CoppSystemL3DstMiss|0    |  -     | ArpTrap           |  -  |524294|   -   
|0  |192.168.20.0/23   |ROUTE| Et25               |1011 |103421  | c0:f8:7f:6a:4e:2a |  -  |288364|   -   
|0  |192.168.0.0/19    |ROUTE| Et25               |1011 |103421  | c0:f8:7f:6a:4e:2a |  -  |288364|   -   
|0  |209.209.209.209/32|TRAP | CoppSystemIpUcast  |0    |  -     | Receive           |  -  |524291|   -   
|0  |0.0.0.0/0         |TRAP | CoppSystemL3LpmOver|0    |  -     | SlowReceive       |  -  |524292|   -   
|1  |0.0.0.0/8         |DROP | DROP               |0    |  -     |                   |  -  |288372|   -   
|1  |127.0.0.0/8       |TRAP | CoppSystemL3DstMiss|0    |  -     | ArpTrap           |  -  |524294|   -   
|1  |0.0.0.0/0         |TRAP | CoppSystemL3LpmOver|0    |  -     | SlowReceive       |  -  |524292|   -   
|2  |0.0.0.0/8         |DROP | DROP               |0    |  -     |                   |  -  |288366|   -   
|2  |127.0.0.0/8       |TRAP | CoppSystemL3DstMiss|0    |  -     | ArpTrap           |  -  |524294|   -   
|2  |192.168.20.0/32   |TRAP | CoppSystemIpBcast  |0    |  -     | BcastReceive      |  -  |524288|   -   
|2  |192.168.20.172/32 |TRAP | CoppSystemIpUcast  |0    |  -     | Receive           |  -  |524291|   -   
|2  |192.168.21.255/32 |TRAP | CoppSystemIpBcast  |0    |  -     | BcastReceive      |  -  |524288|   -   
|2  |192.168.20.0/23   |TRAP | CoppSystemL3DstMiss|0    |  -     | ArpTrap           |  -  |524294|   -   
|2  |0.0.0.0/0         |TRAP | CoppSystemL3DstMiss|0    |  -     | ArpTrap           |  -  |524294|   -   
|6  |0.0.0.0/8         |DROP | DROP               |0    |  -     |                   |  -  |288370|   -   
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
|  -  |91752 |ROUTE| FEC 288384         |   - |  -     |                   |   -   
|  -  |91754 |ROUTE| FEC 288376         |   - |  -     |                   |   -   
|  -  |91756 |ROUTE| FEC 288386         |   - |  -     |                   |   -   
|  -  |288360|DROP | DROP               |0    |  -     |                   |   -   
|  -  |288362|DROP | DROP               |0    |  -     |                   |   -   
|  -  |288364|ROUTE| Et25               |1011 |103421  | c0:f8:7f:6a:4e:2a |   -   
|  -  |288366|DROP | DROP               |0    |  -     |                   |   -   
|  -  |288368|ROUTE| Et25               |1011 |103421  | c0:f8:7f:6a:4e:2a |   -   
|  -  |288370|DROP | DROP               |0    |  -     |                   |   -   
|  -  |288372|DROP | DROP               |0    |  -     |                   |   -   
|  -  |288374|ROUTE| Et25               |1011 |103421  | c0:f8:7f:6a:4e:2a |   -   
|  -  |288376|ROUTE| FEC 528484         |   - |2097151 |                 - |Mpush 20171
|  -  |288378|ROUTE| Et52/1             |1013 |103422  | 28:99:3a:06:b4:e1 |   -   
|  -  |288380|ROUTE| Et52/1             |1013 |103422  | 28:99:3a:06:b4:e1 |   -   
|  -  |288382|ROUTE| Et52/1             |1013 |103422  | 28:99:3a:06:b4:e1 |   -   
|  -  |288384|ROUTE| FEC 528482         |   - |2097149 |                 - |Mpush 20212
|  -  |288386|ROUTE| FEC 528484         |   - |2097150 |                 - |Mpush 20343
|  -  |524288|TRAP | CoppSystemIpBcast  |0    |  -     | BcastReceive      |   -   
|  -  |524291|TRAP | CoppSystemIpUcast  |0    |  -     | Receive           |   -   
|  -  |524292|TRAP | CoppSystemL3LpmOver|0    |  -     | SlowReceive       |   -   
|  -  |524294|TRAP | CoppSystemL3DstMiss|0    |  -     | ArpTrap           |   -   
|  -  |525305|TRAP | CoppSystemL3DstMiss|1011 |1011    | ArpTrap           |   -   
|  -  |525307|TRAP | CoppSystemL3DstMiss|1013 |1013    | ArpTrap           |   -   
|  -  |528482|ROUTE| Et52/1             |1013 |103422  | 28:99:3a:06:b4:e1 |   -   
|  -  |528484|ROUTE| Et25               |1011 |103421  | c0:f8:7f:6a:4e:2a |   -   

```

