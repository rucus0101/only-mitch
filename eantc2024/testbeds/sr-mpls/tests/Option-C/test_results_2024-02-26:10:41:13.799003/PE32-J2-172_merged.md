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

Uptime: 3 hours and 43 minutes
Total memory: 8099732 kB
Free memory: 5603056 kB

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
Interface      IP Address         Status       Protocol            MTU  Owner  
-------------- ------------------ ------------ ---------------- ------- -------
Ethernet5.2    20.111.172.172/24  down         lowerlayerdown     1500         
Ethernet5.171  20.111.172.172/24  down         lowerlayerdown     1500         
Ethernet25     20.149.172.172/24  up           up                 1500         
Ethernet45     20.172.211.172/24  down         notpresent         1500         
Ethernet47     20.171.172.172/24  admin down   down               1500         
Ethernet49/1   20.57.172.172/24   admin down   down               1500         
Ethernet50/1   20.32.172.172/24   admin down   down               1500         
Ethernet51/1   20.47.172.172/24   up           up                 1500         
Ethernet52/1   20.170.172.172/24  up           up                 1500         
Ethernet55/1   20.19.172.172/24   admin down   down               1500         
Loopback0      10.0.0.172/32      up           up                65535         
Management1    192.168.20.172/23  up           up                 1500         

```

## show interfaces counters rates | nz

```text
Port      Name        Intvl  In Mbps      %  In Kpps Out Mbps      % Out Kpps
Ma1                    0:05      0.0   0.0%        0      0.1   0.0%        0
```

## show isis neighbors

```text
 
Instance  VRF      System Id        Type Interface          SNPA              State Hold time   Circuit Id          
OPTION-C- default  h49-N540-24Q8L2DD L2   Ethernet25         P2P               UP    22          00                  
 
Instance  VRF      System Id        Type Interface          SNPA              State Hold time   Circuit Id          
OPTION-C- default  Spine3-J-170     L2   Ethernet52/1       P2P               UP    29          1F                  
```

## show isis database detail

```text
Legend:
H - hostname conflict
U - node unreachable

IS-IS Instance: OPTION-C-DOMAIN-1 VRF: default
  IS-IS Level 2 Link State Database
    LSPID                   Seq Num  Cksum  Life Length IS  Received LSPID        Flags
    h3c_19_CR16010E-F.00-00        44  17396   769    275 L2  0000.0000.0019.00-00  <>
      NLPID: 0xCC(IPv4)
      Hostname: h3c_19_CR16010E-F
      Area addresses: 49
      Interface address: 10.0.0.19
      Interface address: 20.19.149.19
      IS Neighbor          : h49-N540-24Q8L2DD.00 Metric: 10
        IPv4 Neighbor Address: 20.19.149.149
        IPv4 Interface Address: 20.19.149.19
        Adj-sid: 1148 flags: [L V] weight: 0x0
      Reachability         : 10.0.0.19/32 Metric: 0 Type: 1 Up
        SR Prefix-SID: 19 Flags: [N] Algorithm: 0
      Reachability         : 20.19.149.0/24 Metric: 10 Type: 1 Up
      Reachability         : 20.19.170.0/24 Metric: 0 Type: 1 Up
      Reachability         : 31.9.1.0/24 Metric: 0 Type: 1 Up
      Reachability         : 192.168.0.0/19 Metric: 0 Type: 1 Up
      Router Capabilities: Router Id: 10.0.0.19 Flags: []
        Maximum SID depth:
          Base MPLS imposition (MSD type 1):  13
        SR Capability: Flags: [I]
          SRGB Base: 20000 Range: 2000
    h3c_24_S12500R-48C6D.00-00        46  20670   769    279 L2  0000.0000.0024.00-00  <>
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
      Reachability         : 20.24.149.0/24 Metric: 10 Type: 1 Up
      Reachability         : 192.168.20.0/23 Metric: 0 Type: 1 Up
      Router Capabilities: Router Id: 10.0.0.24 Flags: []
        SR Local Block:
          SRLB Base: 15000 Range: 1000
        Maximum SID depth:
          Base MPLS imposition (MSD type 1):  10
        SR Capability: Flags: [I]
          SRGB Base: 20000 Range: 2000
    R6676-50.00-00               32  14760   663    145 L2  0000.0000.0050.00-00  <>
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
    huawei_254_NetEngine_8000_F8.00-00        18  52103   410    156 L2  0000.0000.0254.00-00  <>
      NLPID: 0xCC(IPv4)
      Hostname: huawei_254_NetEngine_8000_F8
      Area addresses: 49
      Interface address: 10.0.0.254
      Interface address: 20.149.254.254
      IS Neighbor          : h49-N540-24Q8L2DD.00 Metric: 10
        IPv4 Neighbor Address: 20.149.254.149
        IPv4 Interface Address: 20.149.254.254
        Adj-sid: 48001 flags: [L V] weight: 0x0
      Reachability         : 10.0.0.254/32 Metric: 0 Type: 1 Up
        SR Prefix-SID: 254 Flags: [N] Algorithm: 0
      Reachability         : 20.149.254.0/24 Metric: 10 Type: 1 Up
      Router Capabilities: Router Id: 10.0.0.254 Flags: []
        Maximum SID depth:
          Base MPLS imposition (MSD type 1):  10
        SR Capability: Flags: [I]
          SRGB Base: 20000 Range: 2000
    h43-9901.00-00               23  44532  1088    186 L2  0000.0000.0343.00-00  <>
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
    h49-N540-24Q8L2DD.00-00        51  19947   454   1343 L2  0000.0000.0349.00-00  <>
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
        Adj-sid: 24001 flags: [L V] weight: 0x0
      IS Neighbor          : juniper_379_MX304.00 Metric: 10
        IPv4 Neighbor Address: 20.149.179.179
        IPv4 Interface Address: 20.149.179.149
        Adj-sid: 24013 flags: [L V] weight: 0x0
      IS Neighbor          : 0010.0010.0005.00   Metric: 10
        IPv4 Neighbor Address: 20.5.149.5
        IPv4 Interface Address: 20.5.149.149
        Adj-sid: 24003 flags: [L V] weight: 0x0
      IS Neighbor          : NOKIA-SR2-57.00     Metric: 10
        IPv4 Neighbor Address: 20.57.149.57
        IPv4 Interface Address: 20.57.149.149
        Adj-sid: 24019 flags: [L V] weight: 0x0
      IS Neighbor          : PE31-J2-171.00      Metric: 10
        IPv4 Neighbor Address: 20.149.171.171
        IPv4 Interface Address: 20.149.171.149
        Adj-sid: 24009 flags: [L V] weight: 0x0
      IS Neighbor          : PE32-J2-172.00      Metric: 10
        IPv4 Neighbor Address: 20.149.172.172
        IPv4 Interface Address: 20.149.172.149
        Adj-sid: 24007 flags: [L V] weight: 0x0
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
    h49-N540-24Q8L2DD.00-01        19  56407  1172    124 L2  0000.0000.0349.00-01  <>
      IS Neighbor          : huawei_254_NetEngine_8000_F8.00 Metric: 10
        IPv4 Neighbor Address: 20.149.254.254
        IPv4 Interface Address: 20.149.254.149
        Adj-sid: 24021 flags: [L V] weight: 0x0
    h55-8201-24H8FH.00-00        26  35179  1036    461 L2  0000.0000.0355.00-00  <>
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
    juniper_379_MX304.00-00        33  14900   831    246 L2  0000.0001.7900.00-00  <>
      NLPID: 0xCC(IPv4) 0x8E(IPv6)
      Hostname: juniper_379_MX304
      Area addresses: 49.0001.00
      Interface address: 10.0.0.179
      Interface address: 10.1.0.179
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
      Reachability         : 10.1.0.179/32 Metric: 0 Type: 1 Up
        SR Prefix-SID: 79 Flags: [N] Algorithm: 0
      Reachability         : 20.149.179.0/24 Metric: 10 Type: 1 Up
      Router Capabilities: Router Id: 10.0.0.179 Flags: []
        Maximum SID depth:
          Base MPLS imposition (MSD type 1):  4
        SR Capability: Flags: [I V]
          SRGB Base: 20000 Range: 2000
        Algorithms:  0, 1, 128, 129, 130
      Unsupported TLV: Type: 14 Length: 2
    0010.0010.0005.00-00         21  51982   505    268 L2  0010.0010.0005.00-00  <>
      NLPID: 0xCC(IPv4)
      Area addresses: 49.0005
      Interface address: 20.5.149.5
      IS Neighbor          : h49-N540-24Q8L2DD.00 Metric: 10
        IPv4 Neighbor Address: 20.5.149.149
        IPv4 Interface Address: 20.5.149.5
        Adj-sid: 16000 flags: [L V] weight: 0x0
      Reachability         : 10.0.0.5/32 Metric: 0 Type: 1 Up
        SR Prefix-SID: 5 Flags: [N] Algorithm: 0
      Reachability         : 20.5.149.0/24 Metric: 10 Type: 1 Up
      Reachability          : 2002::5/128 Metric: 0 Type: 1 Up
      Router Capabilities: Router Id: 10.0.0.5 Flags: []
        SR Capability: Flags: [I]
          SRGB Base: 20000 Range: 2000
        Algorithms:  0
    NOKIA-SR2-57.00-00          510  55960  1194    325 L2  0100.0000.0057.00-00  <>
      NLPID: 0xCC(IPv4) 0x8E(IPv6)
      Hostname: NOKIA-SR2-57
      Area addresses: 49.0000.0000.0057.00
      Interface address: 10.0.0.57
      Interface address: 20.57.149.57
      Interface address: 2002::57
      IS Neighbor (Narrow metrics, unsupported): h49-N540-24Q8L2DD.00 Metric: 10
      IS Neighbor          : h49-N540-24Q8L2DD.00 Metric: 10
        IPv4 Neighbor Address: 20.57.149.149
        IPv4 Interface Address: 20.57.149.57
        Adj-sid: 30149 flags: [L V B] weight: 0x0
      Reachability (Narrow metrics, unsupported): 10.0.0.57/32 Metric: 0 Type: 1
      Reachability (Narrow metrics, unsupported): 20.57.149.0/24 Metric: 10 Type: 1
      Reachability         : 10.0.0.57/32 Metric: 0 Type: 1 Up
        SR Prefix-SID: 57 Flags: [N P] Algorithm: 0
      Reachability         : 20.57.149.0/24 Metric: 10 Type: 1 Up
      Reachability          : 2002::57/128 Metric: 0 Type: 1 Up
        SR Prefix-SID: 157 Flags: [N P] Algorithm: 0
      Router Capabilities: Router Id: 10.0.0.57 Flags: []
        Maximum SID depth:
          Base MPLS imposition (MSD type 1):  12
        SR Capability: Flags: [I V]
          SRGB Base: 20000 Range: 2000
        Algorithms:  0
    PE31-J2-171.00-00            22  60636  1096    287 L2  0100.0000.0171.00-00  <>
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
    PE32-J2-172.00-00            20  36083   416    156 L2  0100.0000.0172.00-00  <>
      LSP generation remaining wait time: 0 ms
      Time remaining until refresh: 116 s
      NLPID: 0xCC(IPv4)
      Hostname: PE32-J2-172
      Area addresses: 49.0000
      Interface address: 20.149.172.172
      Interface address: 10.0.0.172
      IS Neighbor          : h49-N540-24Q8L2DD.00 Metric: 10
        IPv4 Neighbor Address: 20.149.172.149
        IPv4 Interface Address: 20.149.172.172
        Adj-sid: 362144 flags: [L V B] weight: 0x0
      Reachability         : 20.149.172.0/24 Metric: 10 Type: 1 Up
      Reachability         : 10.0.0.172/32 Metric: 10 Type: 1 Up
        SR Prefix-SID: 172 Flags: [N] Algorithm: 0
      Router Capabilities: Router Id: 10.0.0.172 Flags: []
        SR Local Block:
          SRLB Base: 965536 Range: 65536
        Area leader priority: 250 algorithm: 0
        Maximum SID depth:
          Base MPLS imposition (MSD type 1):  12
        SR Capability: Flags: [I]
          SRGB Base: 20000 Range: 2000
 U  3800.0000.4111.00-00          8  16708   770    115 L2  3800.0000.4111.00-00  <DefaultAtt>
      NLPID: 0xCC(IPv4) 0x8E(IPv6) 0x81(CLNP)
      Area addresses: 49
      Interface address: 20.111.149.1
      IS Neighbor          : h49-N540-24Q8L2DD.00 Metric: 10
      Reachability         : 100.0.1.111/32 Metric: 10 Type: 1 Up
        SR Prefix-SID: 411 Flags: [N] Algorithm: 0
      Reachability         : 20.111.149.0/24 Metric: 10 Type: 1 Up
      Router Capabilities: Router Id: 100.0.1.111 Flags: []
        SR Capability: Flags: [I V]
          SRGB Base: 20000 Range: 2000
        Algorithms:  0
Legend:
H - hostname conflict
U - node unreachable

IS-IS Instance: OPTION-C-DOMAIN-2 VRF: default
  IS-IS Level 2 Link State Database
    LSPID                   Seq Num  Cksum  Life Length IS  Received LSPID        Flags
    Ribbon-32.00-00              14  17952   598     79 L2  0000.0000.0032.00-00  <>
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
    Ribbon-32.00-01              14  33716   758     38 L2  0000.0000.0032.00-01  <>
      Remaining lifetime received: 1199 s Modified to: 1200 s
      Hostname: Ribbon-32
    Ribbon-32.00-02              18   4966   580    179 L2  0000.0000.0032.00-02  <>
      Remaining lifetime received: 1199 s Modified to: 1200 s
      Interface address: 10.0.0.32
      Interface address: 20.32.170.32
      IS Neighbor          : Spine3-J-170.00     Metric: 10
        IPv4 Neighbor Address: 20.32.170.170
        IPv4 Interface Address: 20.32.170.32
        Adj-sid: 756642 flags: [L V] weight: 0x0
        Adj-sid: 756643 flags: [L V B] weight: 0x0
      Reachability         : 10.0.0.32/32 Metric: 0 Type: 1 Up
        SR Prefix-SID: 32 Flags: [N] Algorithm: 0
      Reachability         : 20.32.170.0/24 Metric: 10 Type: 1 Up
    Ericsson_47.00-00            32  22689   676    166 L2  0000.0000.0047.00-00  <>
      Remaining lifetime received: 1199 s Modified to: 1200 s
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
    R6676-50.00-00               32  37629   693    145 L2  0000.0000.0050.00-00  <>
      Remaining lifetime received: 1199 s Modified to: 1200 s
      NLPID: 0xCC(IPv4)
      Hostname: R6676-50
      Area addresses: 49.0001
      Interface address: 10.0.0.50
      IS Neighbor          : Spine3-J-170.00     Metric: 10
        IPv4 Interface Address: 20.50.170.50
      Reachability         : 10.0.0.50/32 Metric: 10 Type: 1 Up
        SR Prefix-SID: 50 Flags: [N P] Algorithm: 0
      Reachability         : 20.50.170.0/24 Metric: 10 Type: 1 Up
      Router Capabilities: Router Id: 10.0.0.50 Flags: []
        Maximum SID depth:
          Base MPLS imposition (MSD type 1):  8
        SR Capability: Flags: [I]
          SRGB Base: 20000 Range: 2000
        Algorithms:  0
    h3c_27_S12500R-2L.00-00        43  44321   861    187 L2  0000.0001.0027.00-00  <>
      Remaining lifetime received: 1199 s Modified to: 1200 s
      NLPID: 0xCC(IPv4)
      Hostname: h3c_27_S12500R-2L
      Area addresses: 49.0001
      Interface address: 31.9.1.1
      Interface address: 100.0.1.27
      IS Neighbor          : h3c_19_CR16010E-F-2.00 Metric: 10
        IPv4 Neighbor Address: 31.9.1.2
        IPv4 Interface Address: 31.9.1.1
        Adj-sid: 56260 flags: [L V] weight: 0x0
      Reachability         : 20.27.180.0/24 Metric: 0 Type: 1 Up
      Reachability         : 31.9.1.0/24 Metric: 10 Type: 1 Up
      Reachability         : 100.0.0.27/32 Metric: 0 Type: 1 Up
      Reachability         : 100.0.1.27/32 Metric: 0 Type: 1 Up
        SR Prefix-SID: 270 Flags: [N P] Algorithm: 0
      Reachability         : 192.168.20.0/23 Metric: 0 Type: 1 Up
      Router Capabilities: Router Id: 100.0.1.27 Flags: []
        SR Local Block:
          SRLB Base: 15000 Range: 1000
        Maximum SID depth:
          Base MPLS imposition (MSD type 1):  10
        SR Capability: Flags: [I]
          SRGB Base: 20000 Range: 2000
    juniper_379_MX304.00-00        28  34054   982    211 L2  0000.0001.7900.00-00  <>
      Remaining lifetime received: 1199 s Modified to: 1200 s
      NLPID: 0xCC(IPv4) 0x8E(IPv6)
      Hostname: juniper_379_MX304
      Area addresses: 49.0001.00
      Interface address: 10.0.0.179
      Interface address: 10.1.0.179
      IS Neighbor          : Spine3-J-170.00     Metric: 10
        IPv4 Neighbor Address: 20.170.179.170
        IPv4 Interface Address: 20.170.179.179
        Adj-sid: 24 flags: [L V] weight: 0x0
      Reachability         : 10.0.0.179/32 Metric: 0 Type: 1 Up
        SR Prefix-SID: 379 Flags: [N] Algorithm: 0
      Reachability         : 10.1.0.179/32 Metric: 0 Type: 1 Up
        SR Prefix-SID: 79 Flags: [N] Algorithm: 0
      Reachability         : 20.170.179.0/24 Metric: 10 Type: 1 Up
      Router Capabilities: Router Id: 10.0.0.179 Flags: []
        Maximum SID depth:
          Base MPLS imposition (MSD type 1):  4
        SR Capability: Flags: [I V]
          SRGB Base: 20000 Range: 2000
        Algorithms:  0, 1
      Unsupported TLV: Type: 14 Length: 2
    JNPR-312-ACX7100-48L.00-00        24  44147   552    178 L2  0000.0003.1200.00-00  <>
      Remaining lifetime received: 1199 s Modified to: 1200 s
      NLPID: 0xCC(IPv4) 0x8E(IPv6)
      Hostname: JNPR-312-ACX7100-48L
      Area addresses: 49.0001.00
      Interface address: 10.0.0.212
      IS Neighbor          : Spine3-J-170.00     Metric: 10
        IPv4 Neighbor Address: 20.170.212.170
        IPv4 Interface Address: 20.170.212.212
        Adj-sid: 16 flags: [L V] weight: 0x0
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
    h3c_19_CR16010E-F-2.00-00        28  13235  1077    295 L2  0001.0000.0019.00-00  <>
      Remaining lifetime received: 1199 s Modified to: 1200 s
      NLPID: 0xCC(IPv4)
      Hostname: h3c_19_CR16010E-F-2
      Area addresses: 49
      Interface address: 20.19.170.19
      Interface address: 31.9.1.2
      IS Neighbor          : h3c_27_S12500R-2L.00 Metric: 10
        IPv4 Neighbor Address: 31.9.1.1
        IPv4 Interface Address: 31.9.1.2
        Adj-sid: 1147 flags: [L V] weight: 0x0
      IS Neighbor          : Spine3-J-170.00     Metric: 10
        IPv4 Neighbor Address: 20.19.170.170
        IPv4 Interface Address: 20.19.170.19
        Adj-sid: 1146 flags: [L V] weight: 0x0
      Reachability         : 10.0.0.19/32 Metric: 0 Type: 1 Up
        SR Prefix-SID: 19 Flags: [R P] Algorithm: 0
      Reachability         : 20.19.170.0/24 Metric: 10 Type: 1 Up
      Reachability         : 31.9.1.0/24 Metric: 10 Type: 1 Up
      Router Capabilities: Router Id: 10.0.0.19 Flags: []
        Maximum SID depth:
          Base MPLS imposition (MSD type 1):  13
        SR Capability: Flags: [I]
          SRGB Base: 20000 Range: 2000
    h55-8201-24H8FH.00-00        23  54171  1177    193 L2  0001.0000.0355.00-00  <>
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
      Router Capabilities: Router Id: 10.0.1.55 Flags: []
        SR Local Block:
          SRLB Base: 15000 Range: 1000
        Maximum SID depth:
          Base MPLS imposition (MSD type 1):  8
        SR Capability: Flags: [I]
          SRGB Base: 20000 Range: 2000
        Algorithms:  0, 1
      Unsupported TLV: Type: 14 Length: 2
    NOKIA-SR2-57.00-00           24   4741   913    271 L2  0100.0000.0057.00-00  <>
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
    Nokia-59-IXRe2.00-00         24  40126   677    271 L2  0100.0000.0059.00-00  <>
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
    Spine3-J-170.00-00           54  59831   625    537 L2  0100.0000.0170.00-00  <>
      Remaining lifetime received: 1199 s Modified to: 1200 s
      NLPID: 0xCC(IPv4)
      Hostname: Spine3-J-170
      Area addresses: 49.0000
      Interface address: 20.32.170.170
      Interface address: 20.57.170.170
      Interface address: 20.47.170.170
      Interface address: 20.50.170.170
      Interface address: 20.59.170.170
      Interface address: 20.19.170.170
      Interface address: 20.170.179.170
      Interface address: 20.170.172.170
      Interface address: 20.170.212.170
      Interface address: 20.155.170.170
      Interface address: 10.0.0.170
      IS Neighbor          : Ribbon-32.00        Metric: 10
        IPv4 Neighbor Address: 20.32.170.32
        IPv4 Interface Address: 20.32.170.170
        Adj-sid: 362153 flags: [L V] weight: 0x0
      IS Neighbor          : h3c_19_CR16010E-F-2.00 Metric: 10
        IPv4 Neighbor Address: 20.19.170.19
        IPv4 Interface Address: 20.19.170.170
        Adj-sid: 362148 flags: [L V] weight: 0x0
      IS Neighbor          : NOKIA-SR2-57.00     Metric: 10
        IPv4 Neighbor Address: 20.57.170.57
        IPv4 Interface Address: 20.57.170.170
        Adj-sid: 362152 flags: [L V] weight: 0x0
      IS Neighbor          : Ericsson_47.00      Metric: 10
        IPv4 Neighbor Address: 20.47.170.47
        IPv4 Interface Address: 20.47.170.170
        Adj-sid: 362151 flags: [L V] weight: 0x0
      IS Neighbor          : R6676-50.00         Metric: 10
        IPv4 Neighbor Address: 20.50.170.50
        IPv4 Interface Address: 20.50.170.170
        Adj-sid: 362150 flags: [L V] weight: 0x0
      IS Neighbor          : Nokia-59-IXRe2.00   Metric: 10
        IPv4 Neighbor Address: 20.59.170.59
        IPv4 Interface Address: 20.59.170.170
        Adj-sid: 362149 flags: [L V] weight: 0x0
      IS Neighbor          : juniper_379_MX304.00 Metric: 10
        IPv4 Neighbor Address: 20.170.179.179
        IPv4 Interface Address: 20.170.179.170
        Adj-sid: 362147 flags: [L V] weight: 0x0
      IS Neighbor          : PE32-J2-172.00      Metric: 10
        IPv4 Neighbor Address: 20.170.172.172
        IPv4 Interface Address: 20.170.172.170
        Adj-sid: 362146 flags: [L V] weight: 0x0
      IS Neighbor          : JNPR-312-ACX7100-48L.00 Metric: 10
        IPv4 Neighbor Address: 20.170.212.212
        IPv4 Interface Address: 20.170.212.170
        Adj-sid: 362145 flags: [L V] weight: 0x0
      IS Neighbor          : h55-8201-24H8FH.00  Metric: 10
        IPv4 Neighbor Address: 20.155.170.155
        IPv4 Interface Address: 20.155.170.170
        Adj-sid: 362144 flags: [L V] weight: 0x0
      Reachability         : 20.32.170.0/24 Metric: 10 Type: 1 Up
      Reachability         : 20.57.170.0/24 Metric: 10 Type: 1 Up
      Reachability         : 20.47.170.0/24 Metric: 10 Type: 1 Up
      Reachability         : 20.50.170.0/24 Metric: 10 Type: 1 Up
      Reachability         : 20.59.170.0/24 Metric: 10 Type: 1 Up
      Reachability         : 20.19.170.0/24 Metric: 10 Type: 1 Up
      Reachability         : 20.170.179.0/24 Metric: 10 Type: 1 Up
      Reachability         : 20.170.172.0/24 Metric: 10 Type: 1 Up
      Reachability         : 20.170.212.0/24 Metric: 10 Type: 1 Up
      Reachability         : 20.155.170.0/24 Metric: 10 Type: 1 Up
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
    PE32-J2-172.00-00            20  11510   825    162 L2  0100.0000.0172.00-00  <>
      LSP generation remaining wait time: 0 ms
      Time remaining until refresh: 525 s
      NLPID: 0xCC(IPv4)
      Hostname: PE32-J2-172
      Area addresses: 49.0000
      Interface address: 20.170.172.172
      Interface address: 10.0.0.172
      IS Neighbor          : Spine3-J-170.00     Metric: 10
        IPv4 Neighbor Address: 20.170.172.170
        IPv4 Interface Address: 20.170.172.172
        Adj-sid: 362145 flags: [L V] weight: 0x0
      Reachability         : 20.170.172.0/24 Metric: 10 Type: 1 Up
      Reachability         : 10.0.0.172/32 Metric: 10 Type: 1 Up
        SR Prefix-SID: 172 Flags: [N] Algorithm: 0
      Router Capabilities: Router Id: 10.0.0.172 Flags: []
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
    h3c_19_CR16010E-F.00-00        44  17396   768    275 L2  0000.0000.0019.00-00  <>
      NLPID: 0xCC(IPv4)
      Hostname: h3c_19_CR16010E-F
      TE IPv4 router ID: 10.0.0.19
      Area addresses: 49
      Interface address: 10.0.0.19
      Interface address: 20.19.149.19
      IS Neighbor          : h49-N540-24Q8L2DD.00 Metric: 10
        IPv4 Neighbor Address: 20.19.149.149
        IPv4 Interface Address: 20.19.149.19
        Adj-sid: 1148 flags: [L V] weight: 0x0
        TE default metric: 100
        Maximum link BW: 0.00 bps
        Maximum reservable link BW: 0.00 bps
        Unreserved BW:
            TE class 0: 0.00 bps	TE class 1: 0.00 bps	TE class 2: 0.00 bps
            TE class 3: 0.00 bps	TE class 4: 0.00 bps	TE class 5: 0.00 bps
            TE class 6: 0.00 bps	TE class 7: 0.00 bps
      Reachability         : 10.0.0.19/32 Metric: 0 Type: 1 Up
        SR Prefix-SID: 19 Flags: [N] Algorithm: 0
      Reachability         : 20.19.149.0/24 Metric: 10 Type: 1 Up
      Reachability         : 20.19.170.0/24 Metric: 0 Type: 1 Up
      Reachability         : 31.9.1.0/24 Metric: 0 Type: 1 Up
      Reachability         : 192.168.0.0/19 Metric: 0 Type: 1 Up
      Router Capabilities: Router Id: 10.0.0.19 Flags: []
        Maximum SID depth:
          Base MPLS imposition (MSD type 1):  13
        SR Capability: Flags: [I]
          SRGB Base: 20000 Range: 2000
    h3c_24_S12500R-48C6D.00-00        46  20670   768    279 L2  0000.0000.0024.00-00  <>
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
      Reachability         : 20.24.149.0/24 Metric: 10 Type: 1 Up
      Reachability         : 192.168.20.0/23 Metric: 0 Type: 1 Up
      Router Capabilities: Router Id: 10.0.0.24 Flags: []
        SR Local Block:
          SRLB Base: 15000 Range: 1000
        Maximum SID depth:
          Base MPLS imposition (MSD type 1):  10
        SR Capability: Flags: [I]
          SRGB Base: 20000 Range: 2000
    R6676-50.00-00               32  14760   662    145 L2  0000.0000.0050.00-00  <>
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
    huawei_254_NetEngine_8000_F8.00-00        18  52103   409    156 L2  0000.0000.0254.00-00  <>
      NLPID: 0xCC(IPv4)
      Hostname: huawei_254_NetEngine_8000_F8
      Area addresses: 49
      Interface address: 10.0.0.254
      Interface address: 20.149.254.254
      IS Neighbor          : h49-N540-24Q8L2DD.00 Metric: 10
        IPv4 Neighbor Address: 20.149.254.149
        IPv4 Interface Address: 20.149.254.254
        Adj-sid: 48001 flags: [L V] weight: 0x0
      Reachability         : 10.0.0.254/32 Metric: 0 Type: 1 Up
        SR Prefix-SID: 254 Flags: [N] Algorithm: 0
      Reachability         : 20.149.254.0/24 Metric: 10 Type: 1 Up
      Router Capabilities: Router Id: 10.0.0.254 Flags: []
        Maximum SID depth:
          Base MPLS imposition (MSD type 1):  10
        SR Capability: Flags: [I]
          SRGB Base: 20000 Range: 2000
    h43-9901.00-00               23  44532  1088    186 L2  0000.0000.0343.00-00  <>
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
    h49-N540-24Q8L2DD.00-00        51  19947   453   1343 L2  0000.0000.0349.00-00  <>
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
        Adj-sid: 24013 flags: [L V] weight: 0x0
        Maximum link BW: 10.00 Gbps
        Application Specific Link Attributes:
          Standard applications: Flex-Algo
          User-defined applications: APP3
            Maximum link BW: 10.00 Gbps
      IS Neighbor          : 0010.0010.0005.00   Metric: 10
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
      IS Neighbor          : NOKIA-SR2-57.00     Metric: 10
        IPv4 Neighbor Address: 20.57.149.57
        IPv4 Interface Address: 20.57.149.149
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
      IS Neighbor          : PE32-J2-172.00      Metric: 10
        IPv4 Neighbor Address: 20.149.172.172
        IPv4 Interface Address: 20.149.172.149
        Adj-sid: 24007 flags: [L V] weight: 0x0
        Maximum link BW: 10.00 Gbps
        Application Specific Link Attributes:
          Standard applications: Flex-Algo
          User-defined applications: APP3
            Maximum link BW: 10.00 Gbps
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
    h49-N540-24Q8L2DD.00-01        19  56407  1171    124 L2  0000.0000.0349.00-01  <>
      IS Neighbor          : huawei_254_NetEngine_8000_F8.00 Metric: 10
        IPv4 Neighbor Address: 20.149.254.254
        IPv4 Interface Address: 20.149.254.149
        Adj-sid: 24021 flags: [L V] weight: 0x0
        Maximum link BW: 10.00 Gbps
        Min/Max unidirectional link delay: 11/11 us
        Application Specific Link Attributes:
          Standard applications: Flex-Algo
          User-defined applications: APP3
            TE default metric: 12
            Maximum link BW: 10.00 Gbps
            Min/Max unidirectional link delay: 11/11 us
    h55-8201-24H8FH.00-00        26  35179  1035    461 L2  0000.0000.0355.00-00  <>
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
    juniper_379_MX304.00-00        33  14900   831    246 L2  0000.0001.7900.00-00  <>
      NLPID: 0xCC(IPv4) 0x8E(IPv6)
      Hostname: juniper_379_MX304
      TE IPv4 router ID: 10.0.0.179
      Area addresses: 49.0001.00
      Interface address: 10.0.0.179
      Interface address: 10.1.0.179
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
      Reachability         : 10.1.0.179/32 Metric: 0 Type: 1 Up
        SR Prefix-SID: 79 Flags: [N] Algorithm: 0
      Reachability         : 20.149.179.0/24 Metric: 10 Type: 1 Up
      Router Capabilities: Router Id: 10.0.0.179 Flags: []
        Maximum SID depth:
          Base MPLS imposition (MSD type 1):  4
        SR Capability: Flags: [I V]
          SRGB Base: 20000 Range: 2000
        Algorithms:  0, 1, 128, 129, 130
      Unsupported TLV: Type: 14 Length: 2
    0010.0010.0005.00-00         21  51982   504    268 L2  0010.0010.0005.00-00  <>
      NLPID: 0xCC(IPv4)
      TE IPv4 router ID: 10.0.0.5
      Area addresses: 49.0005
      Interface address: 20.5.149.5
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
      Reachability         : 10.0.0.5/32 Metric: 0 Type: 1 Up
        SR Prefix-SID: 5 Flags: [N] Algorithm: 0
      Reachability         : 20.5.149.0/24 Metric: 10 Type: 1 Up
      Reachability          : 2002::5/128 Metric: 0 Type: 1 Up
      Router Capabilities: Router Id: 10.0.0.5 Flags: []
        SR Capability: Flags: [I]
          SRGB Base: 20000 Range: 2000
        Algorithms:  0
    NOKIA-SR2-57.00-00          510  55960  1194    325 L2  0100.0000.0057.00-00  <>
      NLPID: 0xCC(IPv4) 0x8E(IPv6)
      Hostname: NOKIA-SR2-57
      TE IPv4 router ID: 10.0.0.57
      TE IPv6 router ID: 2002::57
      Area addresses: 49.0000.0000.0057.00
      Interface address: 10.0.0.57
      Interface address: 20.57.149.57
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
            Min/Max unidirectional link delay: 10/10 us
      Reachability (Narrow metrics, unsupported): 10.0.0.57/32 Metric: 0 Type: 1
      Reachability (Narrow metrics, unsupported): 20.57.149.0/24 Metric: 10 Type: 1
      Reachability         : 10.0.0.57/32 Metric: 0 Type: 1 Up
        SR Prefix-SID: 57 Flags: [N P] Algorithm: 0
      Reachability         : 20.57.149.0/24 Metric: 10 Type: 1 Up
      Reachability          : 2002::57/128 Metric: 0 Type: 1 Up
        SR Prefix-SID: 157 Flags: [N P] Algorithm: 0
      Router Capabilities: Router Id: 10.0.0.57 Flags: []
        Maximum SID depth:
          Base MPLS imposition (MSD type 1):  12
        SR Capability: Flags: [I V]
          SRGB Base: 20000 Range: 2000
        Algorithms:  0
    PE31-J2-171.00-00            22  60636  1096    287 L2  0100.0000.0171.00-00  <>
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
            Min/Max unidirectional link delay: 2/12 us
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
    PE32-J2-172.00-00            20  36083   415    156 L2  0100.0000.0172.00-00  <>
      LSP generation remaining wait time: 0 ms
      Time remaining until refresh: 115 s
      NLPID: 0xCC(IPv4)
      Hostname: PE32-J2-172
      Area addresses: 49.0000
      Interface address: 20.149.172.172
      Interface address: 10.0.0.172
      IS Neighbor          : h49-N540-24Q8L2DD.00 Metric: 10
        IPv4 Neighbor Address: 20.149.172.149
        IPv4 Interface Address: 20.149.172.172
        Adj-sid: 362144 flags: [L V B] weight: 0x0
      Reachability         : 20.149.172.0/24 Metric: 10 Type: 1 Up
      Reachability         : 10.0.0.172/32 Metric: 10 Type: 1 Up
        SR Prefix-SID: 172 Flags: [N] Algorithm: 0
      Router Capabilities: Router Id: 10.0.0.172 Flags: []
        SR Local Block:
          SRLB Base: 965536 Range: 65536
        Area leader priority: 250 algorithm: 0
        Maximum SID depth:
          Base MPLS imposition (MSD type 1):  12
        SR Capability: Flags: [I]
          SRGB Base: 20000 Range: 2000
 U  3800.0000.4111.00-00          8  16708   769    115 L2  3800.0000.4111.00-00  <DefaultAtt>
      NLPID: 0xCC(IPv4) 0x8E(IPv6) 0x81(CLNP)
      Area addresses: 49
      Interface address: 20.111.149.1
      IS Neighbor          : h49-N540-24Q8L2DD.00 Metric: 10
      Reachability         : 100.0.1.111/32 Metric: 10 Type: 1 Up
        SR Prefix-SID: 411 Flags: [N] Algorithm: 0
      Reachability         : 20.111.149.0/24 Metric: 10 Type: 1 Up
      Router Capabilities: Router Id: 100.0.1.111 Flags: []
        SR Capability: Flags: [I V]
          SRGB Base: 20000 Range: 2000
        Algorithms:  0
Legend:
H - hostname conflict
U - node unreachable

IS-IS Instance: OPTION-C-DOMAIN-2 VRF: default
  IS-IS Level 2 Link State Database
    LSPID                   Seq Num  Cksum  Life Length IS  Received LSPID        Flags
    Ribbon-32.00-00              14  17952   597     79 L2  0000.0000.0032.00-00  <>
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
    Ribbon-32.00-01              14  33716   757     38 L2  0000.0000.0032.00-01  <>
      Remaining lifetime received: 1199 s Modified to: 1200 s
      Hostname: Ribbon-32
    Ribbon-32.00-02              18   4966   579    179 L2  0000.0000.0032.00-02  <>
      Remaining lifetime received: 1199 s Modified to: 1200 s
      Interface address: 10.0.0.32
      Interface address: 20.32.170.32
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
    Ericsson_47.00-00            32  22689   675    166 L2  0000.0000.0047.00-00  <>
      Remaining lifetime received: 1199 s Modified to: 1200 s
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
    R6676-50.00-00               32  37629   692    145 L2  0000.0000.0050.00-00  <>
      Remaining lifetime received: 1199 s Modified to: 1200 s
      NLPID: 0xCC(IPv4)
      Hostname: R6676-50
      TE IPv4 router ID: 10.0.0.50
      Area addresses: 49.0001
      Interface address: 10.0.0.50
      IS Neighbor          : Spine3-J-170.00     Metric: 10
        IPv4 Interface Address: 20.50.170.50
      Reachability         : 10.0.0.50/32 Metric: 10 Type: 1 Up
        SR Prefix-SID: 50 Flags: [N P] Algorithm: 0
      Reachability         : 20.50.170.0/24 Metric: 10 Type: 1 Up
      Router Capabilities: Router Id: 10.0.0.50 Flags: []
        Maximum SID depth:
          Base MPLS imposition (MSD type 1):  8
        SR Capability: Flags: [I]
          SRGB Base: 20000 Range: 2000
        Algorithms:  0
    h3c_27_S12500R-2L.00-00        43  44321   861    187 L2  0000.0001.0027.00-00  <>
      Remaining lifetime received: 1199 s Modified to: 1200 s
      NLPID: 0xCC(IPv4)
      Hostname: h3c_27_S12500R-2L
      Area addresses: 49.0001
      Interface address: 31.9.1.1
      Interface address: 100.0.1.27
      IS Neighbor          : h3c_19_CR16010E-F-2.00 Metric: 10
        IPv4 Neighbor Address: 31.9.1.2
        IPv4 Interface Address: 31.9.1.1
        Adj-sid: 56260 flags: [L V] weight: 0x0
      Reachability         : 20.27.180.0/24 Metric: 0 Type: 1 Up
      Reachability         : 31.9.1.0/24 Metric: 10 Type: 1 Up
      Reachability         : 100.0.0.27/32 Metric: 0 Type: 1 Up
      Reachability         : 100.0.1.27/32 Metric: 0 Type: 1 Up
        SR Prefix-SID: 270 Flags: [N P] Algorithm: 0
      Reachability         : 192.168.20.0/23 Metric: 0 Type: 1 Up
      Router Capabilities: Router Id: 100.0.1.27 Flags: []
        SR Local Block:
          SRLB Base: 15000 Range: 1000
        Maximum SID depth:
          Base MPLS imposition (MSD type 1):  10
        SR Capability: Flags: [I]
          SRGB Base: 20000 Range: 2000
    juniper_379_MX304.00-00        28  34054   981    211 L2  0000.0001.7900.00-00  <>
      Remaining lifetime received: 1199 s Modified to: 1200 s
      NLPID: 0xCC(IPv4) 0x8E(IPv6)
      Hostname: juniper_379_MX304
      TE IPv4 router ID: 10.0.0.179
      Area addresses: 49.0001.00
      Interface address: 10.0.0.179
      Interface address: 10.1.0.179
      IS Neighbor          : Spine3-J-170.00     Metric: 10
        IPv4 Neighbor Address: 20.170.179.170
        IPv4 Interface Address: 20.170.179.179
        Adj-sid: 24 flags: [L V] weight: 0x0
        Maximum link BW: 10.00 Gbps
      Reachability         : 10.0.0.179/32 Metric: 0 Type: 1 Up
        SR Prefix-SID: 379 Flags: [N] Algorithm: 0
      Reachability         : 10.1.0.179/32 Metric: 0 Type: 1 Up
        SR Prefix-SID: 79 Flags: [N] Algorithm: 0
      Reachability         : 20.170.179.0/24 Metric: 10 Type: 1 Up
      Router Capabilities: Router Id: 10.0.0.179 Flags: []
        Maximum SID depth:
          Base MPLS imposition (MSD type 1):  4
        SR Capability: Flags: [I V]
          SRGB Base: 20000 Range: 2000
        Algorithms:  0, 1
      Unsupported TLV: Type: 14 Length: 2
    JNPR-312-ACX7100-48L.00-00        24  44147   552    178 L2  0000.0003.1200.00-00  <>
      Remaining lifetime received: 1199 s Modified to: 1200 s
      NLPID: 0xCC(IPv4) 0x8E(IPv6)
      Hostname: JNPR-312-ACX7100-48L
      TE IPv4 router ID: 10.0.0.212
      Area addresses: 49.0001.00
      Interface address: 10.0.0.212
      IS Neighbor          : Spine3-J-170.00     Metric: 10
        IPv4 Neighbor Address: 20.170.212.170
        IPv4 Interface Address: 20.170.212.212
        Adj-sid: 16 flags: [L V] weight: 0x0
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
    h3c_19_CR16010E-F-2.00-00        28  13235  1077    295 L2  0001.0000.0019.00-00  <>
      Remaining lifetime received: 1199 s Modified to: 1200 s
      NLPID: 0xCC(IPv4)
      Hostname: h3c_19_CR16010E-F-2
      TE IPv4 router ID: 10.0.0.19
      Area addresses: 49
      Interface address: 20.19.170.19
      Interface address: 31.9.1.2
      IS Neighbor          : h3c_27_S12500R-2L.00 Metric: 10
        IPv4 Neighbor Address: 31.9.1.1
        IPv4 Interface Address: 31.9.1.2
        Adj-sid: 1147 flags: [L V] weight: 0x0
      IS Neighbor          : Spine3-J-170.00     Metric: 10
        IPv4 Neighbor Address: 20.19.170.170
        IPv4 Interface Address: 20.19.170.19
        Adj-sid: 1146 flags: [L V] weight: 0x0
        TE default metric: 10
        Maximum link BW: 0.00 bps
        Maximum reservable link BW: 0.00 bps
        Unreserved BW:
            TE class 0: 0.00 bps	TE class 1: 0.00 bps	TE class 2: 0.00 bps
            TE class 3: 0.00 bps	TE class 4: 0.00 bps	TE class 5: 0.00 bps
            TE class 6: 0.00 bps	TE class 7: 0.00 bps
      Reachability         : 10.0.0.19/32 Metric: 0 Type: 1 Up
        SR Prefix-SID: 19 Flags: [R P] Algorithm: 0
      Reachability         : 20.19.170.0/24 Metric: 10 Type: 1 Up
      Reachability         : 31.9.1.0/24 Metric: 10 Type: 1 Up
      Router Capabilities: Router Id: 10.0.0.19 Flags: []
        Maximum SID depth:
          Base MPLS imposition (MSD type 1):  13
        SR Capability: Flags: [I]
          SRGB Base: 20000 Range: 2000
    h55-8201-24H8FH.00-00        23  54171  1177    193 L2  0001.0000.0355.00-00  <>
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
      Router Capabilities: Router Id: 10.0.1.55 Flags: []
        SR Local Block:
          SRLB Base: 15000 Range: 1000
        Maximum SID depth:
          Base MPLS imposition (MSD type 1):  8
        SR Capability: Flags: [I]
          SRGB Base: 20000 Range: 2000
        Algorithms:  0, 1
      Unsupported TLV: Type: 14 Length: 2
    NOKIA-SR2-57.00-00           24   4741   913    271 L2  0100.0000.0057.00-00  <>
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
    Nokia-59-IXRe2.00-00         24  40126   676    271 L2  0100.0000.0059.00-00  <>
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
    Spine3-J-170.00-00           54  59831   624    537 L2  0100.0000.0170.00-00  <>
      Remaining lifetime received: 1199 s Modified to: 1200 s
      NLPID: 0xCC(IPv4)
      Hostname: Spine3-J-170
      Area addresses: 49.0000
      Interface address: 20.32.170.170
      Interface address: 20.57.170.170
      Interface address: 20.47.170.170
      Interface address: 20.50.170.170
      Interface address: 20.59.170.170
      Interface address: 20.19.170.170
      Interface address: 20.170.179.170
      Interface address: 20.170.172.170
      Interface address: 20.170.212.170
      Interface address: 20.155.170.170
      Interface address: 10.0.0.170
      IS Neighbor          : Ribbon-32.00        Metric: 10
        IPv4 Neighbor Address: 20.32.170.32
        IPv4 Interface Address: 20.32.170.170
        Adj-sid: 362153 flags: [L V] weight: 0x0
      IS Neighbor          : h3c_19_CR16010E-F-2.00 Metric: 10
        IPv4 Neighbor Address: 20.19.170.19
        IPv4 Interface Address: 20.19.170.170
        Adj-sid: 362148 flags: [L V] weight: 0x0
      IS Neighbor          : NOKIA-SR2-57.00     Metric: 10
        IPv4 Neighbor Address: 20.57.170.57
        IPv4 Interface Address: 20.57.170.170
        Adj-sid: 362152 flags: [L V] weight: 0x0
      IS Neighbor          : Ericsson_47.00      Metric: 10
        IPv4 Neighbor Address: 20.47.170.47
        IPv4 Interface Address: 20.47.170.170
        Adj-sid: 362151 flags: [L V] weight: 0x0
      IS Neighbor          : R6676-50.00         Metric: 10
        IPv4 Neighbor Address: 20.50.170.50
        IPv4 Interface Address: 20.50.170.170
        Adj-sid: 362150 flags: [L V] weight: 0x0
      IS Neighbor          : Nokia-59-IXRe2.00   Metric: 10
        IPv4 Neighbor Address: 20.59.170.59
        IPv4 Interface Address: 20.59.170.170
        Adj-sid: 362149 flags: [L V] weight: 0x0
      IS Neighbor          : juniper_379_MX304.00 Metric: 10
        IPv4 Neighbor Address: 20.170.179.179
        IPv4 Interface Address: 20.170.179.170
        Adj-sid: 362147 flags: [L V] weight: 0x0
      IS Neighbor          : PE32-J2-172.00      Metric: 10
        IPv4 Neighbor Address: 20.170.172.172
        IPv4 Interface Address: 20.170.172.170
        Adj-sid: 362146 flags: [L V] weight: 0x0
      IS Neighbor          : JNPR-312-ACX7100-48L.00 Metric: 10
        IPv4 Neighbor Address: 20.170.212.212
        IPv4 Interface Address: 20.170.212.170
        Adj-sid: 362145 flags: [L V] weight: 0x0
      IS Neighbor          : h55-8201-24H8FH.00  Metric: 10
        IPv4 Neighbor Address: 20.155.170.155
        IPv4 Interface Address: 20.155.170.170
        Adj-sid: 362144 flags: [L V] weight: 0x0
      Reachability         : 20.32.170.0/24 Metric: 10 Type: 1 Up
      Reachability         : 20.57.170.0/24 Metric: 10 Type: 1 Up
      Reachability         : 20.47.170.0/24 Metric: 10 Type: 1 Up
      Reachability         : 20.50.170.0/24 Metric: 10 Type: 1 Up
      Reachability         : 20.59.170.0/24 Metric: 10 Type: 1 Up
      Reachability         : 20.19.170.0/24 Metric: 10 Type: 1 Up
      Reachability         : 20.170.179.0/24 Metric: 10 Type: 1 Up
      Reachability         : 20.170.172.0/24 Metric: 10 Type: 1 Up
      Reachability         : 20.170.212.0/24 Metric: 10 Type: 1 Up
      Reachability         : 20.155.170.0/24 Metric: 10 Type: 1 Up
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
    PE32-J2-172.00-00            20  11510   824    162 L2  0100.0000.0172.00-00  <>
      LSP generation remaining wait time: 0 ms
      Time remaining until refresh: 524 s
      NLPID: 0xCC(IPv4)
      Hostname: PE32-J2-172
      Area addresses: 49.0000
      Interface address: 20.170.172.172
      Interface address: 10.0.0.172
      IS Neighbor          : Spine3-J-170.00     Metric: 10
        IPv4 Neighbor Address: 20.170.172.170
        IPv4 Interface Address: 20.170.172.172
        Adj-sid: 362145 flags: [L V] weight: 0x0
      Reachability         : 20.170.172.0/24 Metric: 10 Type: 1 Up
      Reachability         : 10.0.0.172/32 Metric: 10 Type: 1 Up
        SR Prefix-SID: 172 Flags: [N] Algorithm: 0
      Router Capabilities: Router Id: 10.0.0.172 Flags: []
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
 2         10.0.1.55/32      20.149.172.149            Ethernet25     [ 20355 ]
 3         10.0.0.5/32       20.149.172.149            Ethernet25     [ 20005 ]
 4         10.0.0.24/32      20.149.172.149            Ethernet25     [ 20024 ]
 5         10.0.0.171/32     20.149.172.149            Ethernet25     [ 20171 ]
 6         10.0.0.170/32     20.170.172.170            Ethernet52/1   [ 3 ]    
 7         10.0.1.43/32      20.149.172.149            Ethernet25     [ 20343 ]
 8         10.0.0.212/32     20.170.172.170            Ethernet52/1   [ 20212 ]
 9         10.0.0.179/32     20.149.172.149            Ethernet25     [ 20379 ]
 10        10.0.0.19/32      20.149.172.149            Ethernet25     [ 20019 ]
 11        100.0.1.27/32     20.170.172.170            Ethernet52/1   [ 20270 ]
 12        10.0.0.59/32      20.170.172.170            Ethernet52/1   [ 20059 ]
 13        10.0.0.50/32      20.149.172.149            Ethernet25     [ 20050 ]
 14        10.0.0.47/32      20.170.172.170            Ethernet52/1   [ 20047 ]
 15        10.0.0.57/32      20.149.172.149            Ethernet25     [ 20057 ]
 16        10.0.0.254/32     20.149.172.149            Ethernet25     [ 20254 ]
 17        10.0.0.32/32      20.170.172.170            Ethernet52/1   [ 20032 ]
 18        10.1.0.179/32     20.149.172.149            Ethernet25     [ 20079 ]

```

## show isis segment-routing prefix-segments

```text

System ID: PE32-J2-172			Instance: 'OPTION-C-DOMAIN-1'
SR supported Data-plane: MPLS			SR Router ID: 10.0.0.172

Node: 36     Proxy-Node: 0      Prefix: 0       Total Segments: 36

Flag Descriptions: R: Re-advertised, N: Node Segment, P: no-PHP
                   E: Explicit-NULL, V: Value, L: Local
Segment status codes: * - Self originated Prefix, L1 - level 1, L2 - level 2, ! - SR-unreachable,
                      # - Some IS-IS next-hops are SR-unreachable
   Prefix                      SID Type       Flags                        System ID       Level Protection  Algorithm   
   ------------------------- ----- ---------- ---------------------------- --------------- ----- ----------- -------------
   10.0.0.5/32                   5 Node       R:0 N:1 P:0 E:0 V:0 L:0      0010.0010.0005  L2    node        SPF         
   10.0.0.19/32                 19 Node       R:0 N:1 P:0 E:0 V:0 L:0      h3c_19_CR16010E-F L2    node        SPF         
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
   10.0.0.254/32               254 Node       R:0 N:1 P:0 E:0 V:0 L:0      huawei_254_NetEngine_8000_F8 L2    node        SPF         
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
   10.1.0.179/32                79 Node       R:0 N:1 P:0 E:0 V:0 L:0      juniper_379_MX304 L2    node        SPF         
   2002::57/128                157 Node       R:0 N:1 P:1 E:0 V:0 L:0      NOKIA-SR2-57    L2    unprotected SPF         

System ID: PE32-J2-172			Instance: 'OPTION-C-DOMAIN-2'
SR supported Data-plane: MPLS			SR Router ID: 10.0.0.172

Node: 7      Proxy-Node: 0      Prefix: 0       Total Segments: 7

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
   100.0.1.27/32               270 Node       R:0 N:1 P:1 E:0 V:0 L:0      h3c_27_S12500R-2L L2    node        SPF         
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
 I L2     10.0.0.32/32 [115/20]
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
 I L2     10.0.0.254/32 [115/20]
           via 20.149.172.149, Ethernet25
 I L2     10.0.1.43/32 [115/20]
           via 20.149.172.149, Ethernet25
 I L2     10.0.1.49/32 [115/10]
           via 20.149.172.149, Ethernet25
 I L2     10.0.1.55/32 [115/20]
           via 20.149.172.149, Ethernet25
 I L2     10.1.0.179/32 [115/20]
           via 20.149.172.149, Ethernet25
 I L2     20.5.149.0/24 [115/20]
           via 20.149.172.149, Ethernet25
 I L2     20.19.149.0/24 [115/20]
           via 20.149.172.149, Ethernet25
 I L2     20.19.170.0/24 [115/20]
           via 20.149.172.149, Ethernet25
 I L2     20.24.149.0/24 [115/20]
           via 20.149.172.149, Ethernet25
 I L2     20.27.180.0/24 [115/30]
           via 20.170.172.170, Ethernet52/1
 I L2     20.32.155.0/24 [115/30]
           via 20.149.172.149, Ethernet25
 I L2     20.32.170.0/24 [115/20]
           via 20.170.172.170, Ethernet52/1
 I L2     20.47.170.0/24 [115/20]
           via 20.170.172.170, Ethernet52/1
 C        20.47.172.0/24
           directly connected, Ethernet51/1
 I L2     20.50.149.0/24 [115/20]
           via 20.149.172.149, Ethernet25
 I L2     20.50.170.0/24 [115/20]
           via 20.170.172.170, Ethernet52/1
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
 I L2     20.155.170.0/24 [115/20]
           via 20.170.172.170, Ethernet52/1
 C        20.170.172.0/24
           directly connected, Ethernet52/1
 I L2     20.170.179.0/24 [115/20]
           via 20.170.172.170, Ethernet52/1
 I L2     20.170.212.0/24 [115/20]
           via 20.170.172.170, Ethernet52/1
 I L2     31.9.1.0/24 [115/20]
           via 20.149.172.149, Ethernet25
 I L2     100.0.0.27/32 [115/30]
           via 20.170.172.170, Ethernet52/1
 I L2     100.0.1.27/32 [115/30]
           via 20.170.172.170, Ethernet52/1
 I L2     192.168.20.0/23 [115/20]
           via 20.149.172.149, Ethernet25
 I L2     192.168.0.0/19 [115/20]
           via 20.149.172.149, Ethernet25

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
 I L2     10.0.0.32/32 [115/20]
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
 I L2     10.0.0.254/32 [115/20]
           via 20.149.172.149, Ethernet25
 I L2     10.0.1.43/32 [115/20]
           via 20.149.172.149, Ethernet25
 I L2     10.0.1.49/32 [115/10]
           via 20.149.172.149, Ethernet25
 I L2     10.0.1.55/32 [115/20]
           via 20.149.172.149, Ethernet25
 I L2     10.1.0.179/32 [115/20]
           via 20.149.172.149, Ethernet25
 I L2     20.5.149.0/24 [115/20]
           via 20.149.172.149, Ethernet25
 I L2     20.19.149.0/24 [115/20]
           via 20.149.172.149, Ethernet25
 I L2     20.19.170.0/24 [115/20]
           via 20.149.172.149, Ethernet25
 I L2     20.24.149.0/24 [115/20]
           via 20.149.172.149, Ethernet25
 I L2     20.27.180.0/24 [115/30]
           via 20.170.172.170, Ethernet52/1
 I L2     20.32.155.0/24 [115/30]
           via 20.149.172.149, Ethernet25
 I L2     20.32.170.0/24 [115/20]
           via 20.170.172.170, Ethernet52/1
 I L2     20.47.170.0/24 [115/20]
           via 20.170.172.170, Ethernet52/1
 C        20.47.172.0/24
           directly connected, Ethernet51/1
 I L2     20.50.149.0/24 [115/20]
           via 20.149.172.149, Ethernet25
 I L2     20.50.170.0/24 [115/20]
           via 20.170.172.170, Ethernet52/1
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
 I L2     20.155.170.0/24 [115/20]
           via 20.170.172.170, Ethernet52/1
 C        20.170.172.0/24
           directly connected, Ethernet52/1
 I L2     20.170.179.0/24 [115/20]
           via 20.170.172.170, Ethernet52/1
 I L2     20.170.212.0/24 [115/20]
           via 20.170.172.170, Ethernet52/1
 I L2     31.9.1.0/24 [115/20]
           via 20.149.172.149, Ethernet25
 I L2     100.0.0.27/32 [115/30]
           via 20.170.172.170, Ethernet52/1
 I L2     100.0.1.27/32 [115/30]
           via 20.170.172.170, Ethernet52/1
 I L2     192.168.20.0/23 [115/20]
           via 20.149.172.149, Ethernet25
 I L2     192.168.0.0/19 [115/20]
           via 20.149.172.149, Ethernet25


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
MPLS forwarding table (Label [metric] Vias) - 20 routes 
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
 20079   A[1]
                via M, forward
                    EgressACL: apply
                    20.149.172.149 Ethernet25
 20170   A[1]
                via M, pop
                    EgressACL: apply
                    20.170.172.170 Ethernet52/1
 20171   A[1]
                via M, forward
                    EgressACL: apply
                    20.149.172.149 Ethernet25
 20212   A[1]
                via M, forward
                    EgressACL: apply
                    20.170.172.170 Ethernet52/1
 20254   A[1]
                via M, forward
                    EgressACL: apply
                    20.149.172.149 Ethernet25
 20270   A[1]
                via M, forward
                    EgressACL: apply
                    20.170.172.170 Ethernet52/1
 20343   A[1]
                via M, forward
                    EgressACL: apply
                    20.149.172.149 Ethernet25
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
                    28:99:3a:06:b4:e1, vlan 1012
```

## show mpls lfib route

```text
MPLS forwarding table (Label [metric] Vias) - 20 routes 
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
 IP    20079    [1], 10.1.0.179/32
                via M, 20.149.172.149, forward
                 payload autoDecide, ttlMode uniform, dscpMode uniform, apply egress-acl
                 interface Ethernet25
 IP    20170    [1], 10.0.0.170/32
                via M, 20.170.172.170, pop
                 payload autoDecide, ttlMode uniform, dscpMode uniform, apply egress-acl
                 interface Ethernet52/1
 IP    20171    [1], 10.0.0.171/32
                via M, 20.149.172.149, forward
                 payload autoDecide, ttlMode uniform, dscpMode uniform, apply egress-acl
                 interface Ethernet25
 IP    20212    [1], 10.0.0.212/32
                via M, 20.170.172.170, forward
                 payload autoDecide, ttlMode uniform, dscpMode uniform, apply egress-acl
                 interface Ethernet52/1
 IP    20254    [1], 10.0.0.254/32
                via M, 20.149.172.149, forward
                 payload autoDecide, ttlMode uniform, dscpMode uniform, apply egress-acl
                 interface Ethernet25
 IP    20270    [1], 100.0.1.27/32
                via M, 20.170.172.170, forward
                 payload autoDecide, ttlMode uniform, dscpMode uniform, apply egress-acl
                 interface Ethernet52/1
 IP    20343    [1], 10.0.1.43/32
                via M, 20.149.172.149, forward
                 payload autoDecide, ttlMode uniform, dscpMode uniform, apply egress-acl
                 interface Ethernet25
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
```

## show bgp neighbors

```text
BGP neighbor is 10.0.0.5, remote AS 65000, internal link
  BGP version 4, remote router ID 10.0.0.5, VRF default
  Inherits configuration from and member of peer-group BGP-LU-DOMAIN1
  Last read 00:49:34, last write 00:00:31
  Hold time is 180, keepalive interval is 60 seconds
  Configured hold time is 180, keepalive interval is 60 seconds
  Effective minimum hold time is 3 seconds
  Send failure hold time is 0 seconds
  Hold timer is inactive
  Keepalive timer is inactive
  Connect timer is active, time left: 00:02:02
  Connection interval is 148 seconds
  Failed connection attempts is 18
  Idle-restart timer is inactive
  BGP state is Active
  Number of transitions to established: 2
  Last state was Idle
  Last event was Start
  Last rcvd notification:Cease/administrative shutdown, Last time 00:49:34
  Last rcvd socket-error:Connection reset by peer, Last time 00:00:31, First time 02:05:07, Repeats 42
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
  BGP session driven failover for IPv4 Unicast is disabled
  BGP session driven failover for IPv6 Unicast is disabled
  Message Statistics:
                         Sent      Rcvd
    Opens:                 45         2
    Notifications:          0         2
    Updates:             5514         4
    Keepalives:             4        61
    Route Refresh:          0         0
    Total messages:      5563        69
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
  BGP version 4, remote router ID 10.0.0.24, VRF default
  Inherits configuration from and member of peer-group BGP-LU-DOMAIN1
  Last read 00:11:20, last write 00:12:19
  Hold time is 180, keepalive interval is 60 seconds
  Configured hold time is 180, keepalive interval is 60 seconds
  Effective minimum hold time is 3 seconds
  Send failure hold time is 0 seconds
  Hold timer is inactive
  Keepalive timer is inactive
  Connect timer is active, time left: 00:01:06
  Connection interval is 148 seconds
  Failed connection attempts is 11
  Idle-restart timer is inactive
  BGP state is Active
  Number of transitions to established: 4
  Last state was Connect
  Last event was TransportError
  Last sent notification:Cease/administrative reset, Last time 00:30:34
  Last rcvd notification:Cease/peer de-configured, Last time 00:11:20
  Last sent socket-error:Connect (Connection refused), Last time 00:01:33, First time 00:11:19, Repeats 10
  Last rcvd socket-error:Connection reset by peer, Last time 00:30:33, First time 01:44:30, Repeats 2
  Types of communities advertised: standard extended
  Neighbor is a route reflector client (meshed)
  Neighbor is using cluster ID 1.1.1.1
  Neighbor Capabilities:
    Multiprotocol IPv4 Unicast: advertised and received
    Multiprotocol IPv4 with MPLS Labels: advertised and received
    Four Octet ASN: advertised and received
    Route Refresh: advertised and received
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
  BGP session driven failover for IPv4 Unicast is disabled
  BGP session driven failover for IPv6 Unicast is disabled
  Message Statistics:
                         Sent      Rcvd
    Opens:                  7         4
    Notifications:          1         3
    Updates:             8378        18
    Keepalives:             8       112
    Route Refresh:          0         0
    Total messages:      8394       137
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
  BGP version 4, remote router ID 10.0.0.32, VRF default
  Inherits configuration from and member of peer-group BGP-LU-DOMAIN2
  Last read 00:00:00, last write 00:00:00
  Hold time is 180, keepalive interval is 60 seconds
  Configured hold time is 180, keepalive interval is 60 seconds
  Effective minimum hold time is 3 seconds
  Send failure hold time is 0 seconds
  Hold timer is inactive
  Keepalive timer is inactive
  Connect timer is active, time left: 00:02:33
  Connection interval is 148 seconds
  Failed connection attempts is 18
  Idle-restart timer is inactive
  BGP state is Active
  Peering failure hint: Cease/connection rejected
  Number of transitions to established: 5
  Last state was Idle
  Last event was Start
  Last sent notification:Cease/connection rejected, Last time 01:42:34, First time 01:44:34, Repeats 8
  Last rcvd notification:Cease/connection rejected, Last time 00:00:00, First time 00:43:24, Repeats 29
  Last sent socket-error:Connect (Network is unreachable), Last time 01:26:11, First time 03:42:01, Repeats 34
  Last rcvd socket-error:Connection reset by peer, Last time 01:32:34, First time 02:46:21, Repeats 13
  Types of communities advertised: standard extended
  Neighbor is a route reflector client (meshed)
  Neighbor is using cluster ID 2.2.2.2
  Neighbor Capabilities:
    Multiprotocol IPv4 Unicast: advertised
    Multiprotocol IPv4 with MPLS Labels: advertised and received
    Four Octet ASN: advertised and received
    Route Refresh: advertised and received
    Enhanced route refresh: advertised and received
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
  BGP session driven failover for IPv4 Unicast is disabled
  BGP session driven failover for IPv6 Unicast is disabled
  Message Statistics:
                         Sent      Rcvd
    Opens:                 70        36
    Notifications:         34        31
    Updates:             4206         5
    Keepalives:            30       309
    Route Refresh:          0         0
    Total messages:      4340       381
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
  Last read 00:12:19, last write 00:02:58
  Hold time is 180, keepalive interval is 60 seconds
  Configured hold time is 180, keepalive interval is 60 seconds
  Effective minimum hold time is 3 seconds
  Send failure hold time is 0 seconds
  Hold timer is inactive
  Keepalive timer is inactive
  Connect timer is active, time left: 00:00:10
  Connection interval is 148 seconds
  Failed connection attempts is 11
  Idle-restart timer is inactive
  BGP state is Active
  Number of transitions to established: 4
  Last state was Idle
  Last event was Start
  Last sent notification:Cease/administrative reset, Last time 00:30:34
  Last rcvd notification:Cease/administrative shutdown, Last time 00:12:19
  Last rcvd socket-error:Connection reset by peer, Last time 00:02:58, First time 02:22:55, Repeats 12
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
  BGP session driven failover for IPv4 Unicast is disabled
  BGP session driven failover for IPv6 Unicast is disabled
  Message Statistics:
                         Sent      Rcvd
    Opens:                 16         6
    Notifications:          4         1
    Updates:             6055        13
    Keepalives:            15       140
    Route Refresh:          0         0
    Total messages:      6090       160
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
  Last read 00:50:07, last write 00:00:50
  Hold time is 90, keepalive interval is 30 seconds
  Configured hold time is 180, keepalive interval is 60 seconds
  Effective minimum hold time is 3 seconds
  Send failure hold time is 0 seconds
  Hold timer is inactive
  Keepalive timer is inactive
  Connect timer is active, time left: 00:02:17
  Connection interval is 148 seconds
  Failed connection attempts is 18
  Idle-restart timer is inactive
  BGP state is Active
  Number of transitions to established: 1
  Last state was Idle
  Last event was Start
  Last rcvd notification:Cease/administrative shutdown, Last time 00:50:07
  Last sent socket-error:Broken pipe, Last time 00:00:50, First time 00:30:28, Repeats 12
  Last rcvd socket-error:Connection reset by peer, Last time 00:06:19, First time 01:33:23, Repeats 4
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
  BGP session driven failover for IPv4 Unicast is disabled
  BGP session driven failover for IPv6 Unicast is disabled
  Message Statistics:
                         Sent      Rcvd
    Opens:                 42         1
    Notifications:          0         1
    Updates:             2195         2
    Keepalives:             2        86
    Route Refresh:          0         0
    Total messages:      2239        90
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
  Last read 00:00:11, last write 00:00:11
  Hold time is 180, keepalive interval is 60 seconds
  Configured hold time is 180, keepalive interval is 60 seconds
  Effective minimum hold time is 3 seconds
  Send failure hold time is 0 seconds
  Hold timer is inactive
  Keepalive timer is inactive
  Connect timer is active, time left: 00:02:20
  Connection interval is 148 seconds
  Failed connection attempts is 13
  Idle-restart timer is inactive
  BGP state is Active
  Peering failure hint: Cease/connection rejected
  Number of transitions to established: 3
  Last state was Idle
  Last event was Start
  Last sent notification:Cease/administrative reset, Last time 00:30:34
  Last rcvd notification:Cease/connection rejected, Last time 00:00:11, First time 00:14:54, Repeats 12
  Types of communities advertised: standard extended
  Neighbor is a route reflector client (meshed)
  Neighbor is using cluster ID 1.1.1.1
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
    Opens:                 16         3
    Notifications:          2        14
    Updates:             9508        10
    Keepalives:            19       175
    Route Refresh:          0         0
    Total messages:      9545       202
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
Remote TCP address is 10.0.0.171, remote port is 179

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
Local AS is 65000, local router ID 10.0.0.172
TTL is 255

BGP neighbor is 10.0.0.212, remote AS 65001, internal link
  BGP version 4, remote router ID 10.0.0.212, VRF default
  Inherits configuration from and member of peer-group BGP-LU-DOMAIN2
  Last read 00:01:28, last write 00:01:28
  Hold time is 90, keepalive interval is 30 seconds
  Configured hold time is 180, keepalive interval is 60 seconds
  Effective minimum hold time is 3 seconds
  Send failure hold time is 0 seconds
  Hold timer is inactive
  Keepalive timer is inactive
  Connect timer is active, time left: 00:01:28
  Connection interval is 148 seconds
  Failed connection attempts is 18
  Idle-restart timer is inactive
  BGP state is Active
  Peering failure hint: Cease/connection rejected
  Number of transitions to established: 2
  Last state was Idle
  Last event was Start
  Last sent notification:Cease/connection rejected, Last time 01:42:44, First time 01:44:54, Repeats 12
  Last rcvd notification:Cease/connection rejected, Last time 00:01:28, First time 00:43:22, Repeats 29
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
  BGP session driven failover for IPv4 Unicast is disabled
  BGP session driven failover for IPv6 Unicast is disabled
  Message Statistics:
                         Sent      Rcvd
    Opens:                 32        45
    Notifications:         14        31
    Updates:             3297         7
    Keepalives:            35       138
    Route Refresh:          0         0
    Total messages:      3378       221
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
Remote TCP address is 10.0.0.212, remote port is 179

BGP neighbor is 10.0.0.254, remote AS 65000, internal link
  BGP version 4, remote router ID 10.0.0.254, VRF default
  Inherits configuration from and member of peer-group BGP-LU-DOMAIN1
  Last read 00:49:29, last write 00:49:33
  Hold time is 180, keepalive interval is 60 seconds
  Configured hold time is 180, keepalive interval is 60 seconds
  Effective minimum hold time is 3 seconds
  Send failure hold time is 0 seconds
  Hold timer is inactive
  Keepalive timer is inactive
  Connect timer is active, time left: 00:02:16
  Connection interval is 148 seconds
  Failed connection attempts is 18
  Idle-restart timer is inactive
  BGP state is Active
  Number of transitions to established: 1
  Last state was Connect
  Last event was TransportError
  Last rcvd notification:Cease/administrative shutdown, Last time 00:49:29
  Last sent socket-error:Connect (Connection refused), Last time 00:00:16, First time 00:49:28, Repeats 31
  Types of communities advertised: standard extended
  Neighbor is a route reflector client (meshed)
  Neighbor is using cluster ID 1.1.1.1
  Neighbor Capabilities:
    Multiprotocol IPv4 Unicast: advertised and received
    Multiprotocol IPv4 with MPLS Labels: advertised and received
    Four Octet ASN: advertised and received
    Route Refresh: advertised and received
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
  BGP session driven failover for IPv4 Unicast is disabled
  BGP session driven failover for IPv6 Unicast is disabled
  Message Statistics:
                         Sent      Rcvd
    Opens:                  1         1
    Notifications:          0         1
    Updates:             5086       106
    Keepalives:             2        68
    Route Refresh:          0         0
    Total messages:      5089       176
  Prefix Statistics:
                                   Sent      Rcvd     Best Paths     Best ECMP Paths
    IPv4 Unicast:                     0         0              0                   0
    IPv6 Unicast:                     0         0              0                   0
  Configured maximum total number of routes is 256000, warning limit is 204800
  Inbound updates dropped by reason:
    AS path loop detection: 0
    Cluster ID loop detection: 32
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
  Last read 00:27:40, last write 00:27:38
  Hold time is 180, keepalive interval is 60 seconds
  Configured hold time is 180, keepalive interval is 60 seconds
  Effective minimum hold time is 3 seconds
  Send failure hold time is 0 seconds
  Hold timer is inactive
  Keepalive timer is inactive
  Connect timer is active, time left: 00:01:14
  Connection interval is 148 seconds
  Failed connection attempts is 17
  Idle-restart timer is inactive
  BGP state is Active
  Number of transitions to established: 2
  Last state was Connect
  Last event was TransportError
  Last sent notification:Cease/administrative reset, Last time 00:30:34
  Last rcvd notification:Cease/administrative shutdown, Last time 00:27:40
  Last sent socket-error:Connect (Connection refused), Last time 00:01:16, First time 00:27:34, Repeats 15
  Last rcvd socket-error:Connection reset by peer, Last time 00:27:38, First time 00:30:33, Repeats 1
  Types of communities advertised: standard extended
  Neighbor is a route reflector client (meshed)
  Neighbor is using cluster ID 1.1.1.1
  Neighbor Capabilities:
    Multiprotocol IPv4 Unicast: advertised
    Multiprotocol IPv4 with MPLS Labels: advertised and received
    Four Octet ASN: advertised and received
    Route Refresh: advertised and received
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
  AIGP attribute send and receive for IPv4 Unicast are enabled
  AIGP attribute send and receive for IPv4 with MPLS Labels are enabled
  AIGP attribute send and receive for IPv6 Unicast are enabled
  AIGP attribute send and receive for IPv6 with MPLS Labels are enabled
  BGP session driven failover for IPv4 Unicast is disabled
  BGP session driven failover for IPv6 Unicast is disabled
  Message Statistics:
                         Sent      Rcvd
    Opens:                  4         2
    Notifications:          1         1
    Updates:             7431         4
    Keepalives:             4        82
    Route Refresh:          0         0
    Total messages:      7440        89
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
Remote TCP address is 10.0.1.43, remote port is 179

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
Local AS is 65000, local router ID 10.0.0.172
TTL is 255

BGP neighbor is 100.0.1.111, remote AS 65000, internal link
  BGP version 4, remote router ID 0.0.0.0, VRF default
  Inherits configuration from and member of peer-group BGP-LU-DOMAIN1
  Last read never, last write 00:03:02
  Hold time is 0, keepalive interval is 0 seconds
  Configured hold time is 180, keepalive interval is 60 seconds
  Effective minimum hold time is 3 seconds
  Send failure hold time is 0 seconds
  Hold timer is inactive
  Keepalive timer is inactive
  Connect timer is active, time left: 00:02:20
  Connection interval is 148 seconds
  Failed connection attempts is 10
  Idle-restart timer is inactive
  BGP state is Active
  Number of transitions to established: 0
  Last state was Connect
  Last event was TransportError
  Last sent socket-error:Connect (Network is unreachable), Last time 00:00:26, First time 00:28:38, Repeats 5
  Last rcvd socket-error:Connection reset by peer, Last time 00:03:02, First time 00:46:55, Repeats 36
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
  BGP session driven failover for IPv4 Unicast is disabled
  BGP session driven failover for IPv6 Unicast is disabled
  Message Statistics:
                         Sent      Rcvd
    Opens:                 37         0
    Notifications:          0         0
    Updates:                0         0
    Keepalives:             0         0
    Route Refresh:          0         0
    Total messages:        37         0
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
10.0.0.5/32     IS-IS SR IPv4   3           30                  115            
10.0.0.19/32    IS-IS SR IPv4   10          30                  115            
10.0.0.24/32    IS-IS SR IPv4   4           30                  115            
10.0.0.32/32    IS-IS SR IPv4   17          30                  115            
10.0.0.47/32    IS-IS SR IPv4   14          30                  115            
10.0.0.50/32    IS-IS SR IPv4   13          30                  115            
10.0.0.57/32    IS-IS SR IPv4   15          30                  115            
10.0.0.59/32    IS-IS SR IPv4   12          30                  115            
10.0.0.170/32   IS-IS SR IPv4   6           30                  115            
10.0.0.171/32   IS-IS SR IPv4   5           30                  115            
10.0.0.179/32   IS-IS SR IPv4   9           30                  115            
10.0.0.212/32   IS-IS SR IPv4   8           30                  115            
10.0.0.254/32   IS-IS SR IPv4   16          30                  115            
10.0.1.43/32    IS-IS SR IPv4   7           30                  115            
10.0.1.49/32    IS-IS SR IPv4   1           30                  115            
10.0.1.55/32    IS-IS SR IPv4   2           30                  115            
10.1.0.179/32   IS-IS SR IPv4   18          30                  115            
100.0.1.27/32   IS-IS SR IPv4   11          30                  115            

   IGP Metric    Metric Type
---------------- -----------
   20            metric     
   20            metric     
   20            metric     
   20            metric     
   30            metric     
   30            metric     
   20            metric     
   20            metric     
   20            metric     
   20            metric     
   20            metric     
   20            metric     
   20            metric     
   20            metric     
   10            metric     
   20            metric     
   20            metric     
   30            metric     

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
>C    10.0.0.172/32 [0 pref/0 metric] updated 03:42:21 ago
         via Loopback0, directly connected
>C    20.47.172.0/24 [0 pref/0 metric] updated 03:17:38 ago
         via Ethernet51/1, directly connected
>C    20.149.172.0/24 [0 pref/0 metric] updated 03:40:25 ago
         via Ethernet25, directly connected
>C    20.170.172.0/24 [0 pref/0 metric] updated 03:39:37 ago
         via Ethernet52/1, directly connected
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
>P    0.0.0.0/8 [1 pref/0 metric] updated 03:42:19 ago
         via Null0, directly connected [NF]
>P    127.0.0.0/8 [1 pref/0 metric] updated 03:42:19 ago
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
>I    10.0.0.5/32 [115 pref/20 metric] updated 03:40:25 ago
         via 20.149.172.149, Ethernet25
>I    10.0.0.19/32 [115 pref/20 metric] updated 02:42:35 ago
         via 20.149.172.149, Ethernet25
>I    10.0.0.24/32 [115 pref/20 metric] updated 03:40:24 ago
         via 20.149.172.149, Ethernet25
>I    10.0.0.32/32 [115 pref/20 metric] updated 01:26:13 ago
         via 20.170.172.170, Ethernet52/1
>I    10.0.0.47/32 [115 pref/30 metric] updated 03:17:37 ago
         via 20.170.172.170, Ethernet52/1
>I    10.0.0.50/32 [115 pref/30 metric] updated 03:18:43 ago
         via 20.149.172.149, Ethernet25
>I    10.0.0.57/32 [115 pref/20 metric] updated 03:17:19 ago
         via 20.149.172.149, Ethernet25
>I    10.0.0.59/32 [115 pref/20 metric] updated 03:20:39 ago
         via 20.170.172.170, Ethernet52/1
>I    10.0.0.170/32 [115 pref/20 metric] updated 03:39:26 ago
         via 20.170.172.170, Ethernet52/1
>I    10.0.0.171/32 [115 pref/20 metric] updated 03:40:23 ago
         via 20.149.172.149, Ethernet25
>I    10.0.0.179/32 [115 pref/20 metric] updated 03:33:18 ago
         via 20.149.172.149, Ethernet25
>I    10.0.0.212/32 [115 pref/20 metric] updated 03:36:34 ago
         via 20.170.172.170, Ethernet52/1
>I    10.0.0.254/32 [115 pref/20 metric] updated 02:55:04 ago
         via 20.149.172.149, Ethernet25
>I    10.0.1.43/32 [115 pref/20 metric] updated 03:37:02 ago
         via 20.149.172.149, Ethernet25
>I    10.0.1.49/32 [115 pref/10 metric] updated 03:40:25 ago
         via 20.149.172.149, Ethernet25
>I    10.0.1.55/32 [115 pref/20 metric] updated 03:40:25 ago
         via 20.149.172.149, Ethernet25
>I    10.1.0.179/32 [115 pref/20 metric] updated 01:53:14 ago
         via 20.149.172.149, Ethernet25
>I    20.5.149.0/24 [115 pref/20 metric] updated 03:40:25 ago
         via 20.149.172.149, Ethernet25
>I    20.19.149.0/24 [115 pref/20 metric] updated 03:32:59 ago
         via 20.149.172.149, Ethernet25
>I    20.19.170.0/24 [115 pref/20 metric] updated 02:42:35 ago
         via 20.149.172.149, Ethernet25
>I    20.24.149.0/24 [115 pref/20 metric] updated 03:40:25 ago
         via 20.149.172.149, Ethernet25
>I    20.27.180.0/24 [115 pref/30 metric] updated 02:42:29 ago
         via 20.170.172.170, Ethernet52/1
>I    20.32.155.0/24 [115 pref/30 metric] updated 03:40:25 ago
         via 20.149.172.149, Ethernet25
>I    20.32.170.0/24 [115 pref/20 metric] updated 01:27:12 ago
         via 20.170.172.170, Ethernet52/1
>I    20.47.170.0/24 [115 pref/20 metric] updated 03:17:47 ago
         via 20.170.172.170, Ethernet52/1
>I    20.50.149.0/24 [115 pref/20 metric] updated 03:19:01 ago
         via 20.149.172.149, Ethernet25
>I    20.50.170.0/24 [115 pref/20 metric] updated 03:19:00 ago
         via 20.170.172.170, Ethernet52/1
>I    20.57.149.0/24 [115 pref/20 metric] updated 03:17:24 ago
         via 20.149.172.149, Ethernet25
>I    20.57.155.0/24 [115 pref/30 metric] updated 03:17:21 ago
         via 20.149.172.149, Ethernet25
>I    20.57.170.0/24 [115 pref/20 metric] updated 03:17:24 ago
         via 20.170.172.170, Ethernet52/1
>I    20.57.179.0/24 [115 pref/30 metric] updated 03:17:21 ago
         via 20.149.172.149, Ethernet25
>I    20.59.170.0/24 [115 pref/20 metric] updated 03:20:40 ago
         via 20.170.172.170, Ethernet52/1
>I    20.111.149.0/24 [115 pref/20 metric] updated 02:24:27 ago
         via 20.149.172.149, Ethernet25
>I    20.143.149.0/24 [115 pref/20 metric] updated 03:37:06 ago
         via 20.149.172.149, Ethernet25
>I    20.149.155.0/24 [115 pref/20 metric] updated 03:40:25 ago
         via 20.149.172.149, Ethernet25
>I    20.149.171.0/24 [115 pref/20 metric] updated 03:40:23 ago
         via 20.149.172.149, Ethernet25
>I    20.149.179.0/24 [115 pref/20 metric] updated 03:33:31 ago
         via 20.149.172.149, Ethernet25
>I    20.149.254.0/24 [115 pref/20 metric] updated 02:55:07 ago
         via 20.149.172.149, Ethernet25
>I    20.155.170.0/24 [115 pref/20 metric] updated 03:39:26 ago
         via 20.170.172.170, Ethernet52/1
>I    20.170.179.0/24 [115 pref/20 metric] updated 03:33:29 ago
         via 20.170.172.170, Ethernet52/1
>I    20.170.212.0/24 [115 pref/20 metric] updated 03:39:26 ago
         via 20.170.172.170, Ethernet52/1
>I    31.9.1.0/24 [115 pref/20 metric] updated 02:42:35 ago
         via 20.149.172.149, Ethernet25
>I    100.0.0.27/32 [115 pref/30 metric] updated 02:42:29 ago
         via 20.170.172.170, Ethernet52/1
>I    100.0.1.27/32 [115 pref/30 metric] updated 02:42:29 ago
         via 20.170.172.170, Ethernet52/1
>I    192.168.0.0/19 [115 pref/20 metric] updated 02:42:35 ago
         via 20.149.172.149, Ethernet25
>I    192.168.20.0/23 [115 pref/20 metric] updated 03:40:24 ago
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
>P    ::/96 [1 pref/0 metric] updated 03:42:19 ago
         via Null0, directly connected [NF]
>P    ::ffff:127.0.0.0/104 [1 pref/0 metric] updated 03:42:19 ago
         via :: [1 pref/1 metric] type ipv6
            via , directly connected
>P    fe80::/10 [1 pref/0 metric] updated 03:42:19 ago
```

## show platform sand l3 summary

```text
Number of vrfs: 8

Ipv4:
  Routes:       77  backlog:  0  unprogrammed:  0
  Adjacencies:  32  backlog:  0  unprogrammed:  0
Ipv6:
  Routes:       4   backlog:  0  unprogrammed:  0
  Adjacencies:  32  backlog:  0  unprogrammed:  0
Mpls:
  Routes:       20  backlog:  0  unprogrammed:  0
  Adjacencies:  2   backlog:  0  unprogrammed:  0

Jericho2 Ip Fecs:
  Non-ecmp fecs:  4107  ecmp fecs:  0  fec entries:  4107
Jericho2 Mpls Fecs:
  Non-ecmp fecs:  2  ecmp fecs:  0  fec entries:  2
Jericho2 Vxlan Tunnel Fecs:
  Non-ecmp fecs:  0  ecmp fecs:  0  fec entries:  0
  Number of vxlan tunnels configured: 0

Jericho2 Lpm Routes:
  Routes:   77  unprogrammed:   0   
  Routes6:  4   unprogrammed6:  0   
  Backlog:  0 

Jericho2 Lpm:
  TCAM entries used:   3   Percent free:  99  ADS2 entries used:   6  Percent free:  99
  Pivot buckets used:  4   Rows used:     2   Entries Per Bucket:  1  Percent free:  99
  Route buckets used:  14  Rows used:     3   Entries Per Bucket:  5  Percent free:  99

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
  ReusedEcmp:  0  allocs:  834912  frees:  834901  shuffles:  0  cmds:  0
  Zombies:     0    purges:    0
  Quarantine:  0/0  shuffles:  0  deletes:  0   
  Fec insertion failures:  0
  Level1  Fecs:
    Non-ecmp fecs:            0    ecmp fecs:            1 
    Non-ecmp (Percent free):  100  ecmp (Percent free):  99
  Level2  Fecs:
    Non-ecmp fecs:            22  ecmp fecs:            0  
    Non-ecmp (Percent free):  99  ecmp (Percent free):  100
  Level3  Fecs:
    Non-ecmp fecs:            0    ecmp fecs:            0  
    Non-ecmp (Percent free):  100  ecmp (Percent free):  100

Lpm Detail:
  Requests:  137  cleanses:  75  batches:  75  avg batch size:  1

Jericho Arp:
  ArpTable writes:      6266987  queued      0   
  IngressTable writes:  2618382  queued      0   
  Coprocessors:         1        in CmdRing

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
|0  |10.0.0.5/32       |ROUTE| Et25               |1011 |103421  | c0:f8:7f:6a:4e:2a |  -  |288366|   -   
|0  |10.0.0.19/32      |ROUTE| Et25               |1011 |103421  | c0:f8:7f:6a:4e:2a |  -  |288366|   -   
|0  |10.0.0.24/32      |ROUTE| Et25               |1011 |103421  | c0:f8:7f:6a:4e:2a |  -  |288366|   -   
|0  |10.0.0.32/32      |ROUTE| Et52/1             |1012 |103422  | 28:99:3a:06:b4:e1 |  -  |288376|   -   
|0  |10.0.0.47/32      |ROUTE| Et52/1             |1012 |103422  | 28:99:3a:06:b4:e1 |  -  |288376|   -   
|0  |10.0.0.50/32      |ROUTE| Et25               |1011 |103421  | c0:f8:7f:6a:4e:2a |  -  |288366|   -   
|0  |10.0.0.57/32      |ROUTE| Et25               |1011 |103421  | c0:f8:7f:6a:4e:2a |  -  |288366|   -   
|0  |10.0.0.59/32      |ROUTE| Et52/1             |1012 |103422  | 28:99:3a:06:b4:e1 |  -  |288376|   -   
|0  |10.0.0.170/32     |ROUTE| Et52/1             |1012 |103422  | 28:99:3a:06:b4:e1 |  -  |288376|   -   
|0  |10.0.0.171/32     |ROUTE| Et25               |1011 |103421  | c0:f8:7f:6a:4e:2a |  -  |288366|   -   
|0  |10.0.0.172/32     |TRAP | CoppSystemIpUcast  |0    |  -     | Receive           |  -  |524291|   -   
|0  |10.0.0.179/32     |ROUTE| Et25               |1011 |103421  | c0:f8:7f:6a:4e:2a |  -  |288366|   -   
|0  |10.0.0.212/32     |ROUTE| Et52/1             |1012 |103422  | 28:99:3a:06:b4:e1 |  -  |288376|   -   
|0  |10.0.0.254/32     |ROUTE| Et25               |1011 |103421  | c0:f8:7f:6a:4e:2a |  -  |288366|   -   
|0  |10.0.1.43/32      |ROUTE| Et25               |1011 |103421  | c0:f8:7f:6a:4e:2a |  -  |288366|   -   
|0  |10.0.1.49/32      |ROUTE| Et25               |1011 |103421  | c0:f8:7f:6a:4e:2a |  -  |288366|   -   
|0  |10.0.1.55/32      |ROUTE| Et25               |1011 |103421  | c0:f8:7f:6a:4e:2a |  -  |288366|   -   
|0  |10.1.0.179/32     |ROUTE| Et25               |1011 |103421  | c0:f8:7f:6a:4e:2a |  -  |288366|   -   
|0  |20.5.149.0/24     |ROUTE| Et25               |1011 |103421  | c0:f8:7f:6a:4e:2a |  -  |288366|   -   
|0  |20.19.149.0/24    |ROUTE| Et25               |1011 |103421  | c0:f8:7f:6a:4e:2a |  -  |288366|   -   
|0  |20.19.170.0/24    |ROUTE| Et25               |1011 |103421  | c0:f8:7f:6a:4e:2a |  -  |288366|   -   
|0  |20.24.149.0/24    |ROUTE| Et25               |1011 |103421  | c0:f8:7f:6a:4e:2a |  -  |288366|   -   
|0  |20.27.180.0/24    |ROUTE| Et52/1             |1012 |103422  | 28:99:3a:06:b4:e1 |  -  |288376|   -   
|0  |20.32.155.0/24    |ROUTE| Et25               |1011 |103421  | c0:f8:7f:6a:4e:2a |  -  |288366|   -   
|0  |20.32.170.0/24    |ROUTE| Et52/1             |1012 |103422  | 28:99:3a:06:b4:e1 |  -  |288376|   -   
|0  |20.47.170.0/24    |ROUTE| Et52/1             |1012 |103422  | 28:99:3a:06:b4:e1 |  -  |288376|   -   
|0  |20.47.172.0/32    |TRAP | CoppSystemIpBcast  |0    |  -     | BcastReceive      |  -  |524288|   -   
|0  |20.47.172.172/32  |TRAP | CoppSystemIpUcast  |0    |  -     | Receive           |  -  |524291|   -   
|0  |20.47.172.255/32  |TRAP | CoppSystemIpBcast  |0    |  -     | BcastReceive      |  -  |524288|   -   
|0  |20.47.172.0/24    |TRAP | CoppSystemL3DstMiss|1010 |1010    | ArpTrap           |  -  |525304|   -   
|0  |20.50.149.0/24    |ROUTE| Et25               |1011 |103421  | c0:f8:7f:6a:4e:2a |  -  |288366|   -   
|0  |20.50.170.0/24    |ROUTE| Et52/1             |1012 |103422  | 28:99:3a:06:b4:e1 |  -  |288376|   -   
|0  |20.57.149.0/24    |ROUTE| Et25               |1011 |103421  | c0:f8:7f:6a:4e:2a |  -  |288366|   -   
|0  |20.57.155.0/24    |ROUTE| Et25               |1011 |103421  | c0:f8:7f:6a:4e:2a |  -  |288366|   -   
|0  |20.57.170.0/24    |ROUTE| Et52/1             |1012 |103422  | 28:99:3a:06:b4:e1 |  -  |288376|   -   
|0  |20.57.179.0/24    |ROUTE| Et25               |1011 |103421  | c0:f8:7f:6a:4e:2a |  -  |288366|   -   
|0  |20.59.170.0/24    |ROUTE| Et52/1             |1012 |103422  | 28:99:3a:06:b4:e1 |  -  |288376|   -   
|0  |20.111.149.0/24   |ROUTE| Et25               |1011 |103421  | c0:f8:7f:6a:4e:2a |  -  |288366|   -   
|0  |20.143.149.0/24   |ROUTE| Et25               |1011 |103421  | c0:f8:7f:6a:4e:2a |  -  |288366|   -   
|0  |20.149.155.0/24   |ROUTE| Et25               |1011 |103421  | c0:f8:7f:6a:4e:2a |  -  |288366|   -   
|0  |20.149.171.0/24   |ROUTE| Et25               |1011 |103421  | c0:f8:7f:6a:4e:2a |  -  |288366|   -   
|0  |20.149.172.0/32   |TRAP | CoppSystemIpBcast  |0    |  -     | BcastReceive      |  -  |524288|   -   
|0  |20.149.172.149/32 |ROUTE| Et25               |1011 |103421  | c0:f8:7f:6a:4e:2a |  -  |288368|   -   
|0  |20.149.172.172/32 |TRAP | CoppSystemIpUcast  |0    |  -     | Receive           |  -  |524291|   -   
|0  |20.149.172.255/32 |TRAP | CoppSystemIpBcast  |0    |  -     | BcastReceive      |  -  |524288|   -   
|0  |20.149.172.0/24   |TRAP | CoppSystemL3DstMiss|1011 |1011    | ArpTrap           |  -  |525305|   -   
|0  |20.149.179.0/24   |ROUTE| Et25               |1011 |103421  | c0:f8:7f:6a:4e:2a |  -  |288366|   -   
|0  |20.149.254.0/24   |ROUTE| Et25               |1011 |103421  | c0:f8:7f:6a:4e:2a |  -  |288366|   -   
|0  |20.155.170.0/24   |ROUTE| Et52/1             |1012 |103422  | 28:99:3a:06:b4:e1 |  -  |288376|   -   
|0  |20.170.172.0/32   |TRAP | CoppSystemIpBcast  |0    |  -     | BcastReceive      |  -  |524288|   -   
|0  |20.170.172.170/32 |ROUTE| Et52/1             |1012 |103422  | 28:99:3a:06:b4:e1 |  -  |288378|   -   
|0  |20.170.172.172/32 |TRAP | CoppSystemIpUcast  |0    |  -     | Receive           |  -  |524291|   -   
|0  |20.170.172.255/32 |TRAP | CoppSystemIpBcast  |0    |  -     | BcastReceive      |  -  |524288|   -   
|0  |20.170.172.0/24   |TRAP | CoppSystemL3DstMiss|1012 |1012    | ArpTrap           |  -  |525306|   -   
|0  |20.170.179.0/24   |ROUTE| Et52/1             |1012 |103422  | 28:99:3a:06:b4:e1 |  -  |288376|   -   
|0  |20.170.212.0/24   |ROUTE| Et52/1             |1012 |103422  | 28:99:3a:06:b4:e1 |  -  |288376|   -   
|0  |31.9.1.0/24       |ROUTE| Et25               |1011 |103421  | c0:f8:7f:6a:4e:2a |  -  |288366|   -   
|0  |100.0.0.27/32     |ROUTE| Et52/1             |1012 |103422  | 28:99:3a:06:b4:e1 |  -  |288376|   -   
|0  |100.0.1.27/32     |ROUTE| Et52/1             |1012 |103422  | 28:99:3a:06:b4:e1 |  -  |288376|   -   
|0  |100.0.1.111/32    |ROUTE| Et25               |1011 |103421  | c0:f8:7f:6a:4e:2a |  -  |288366|   -   
|0  |127.0.0.0/8       |TRAP | CoppSystemL3DstMiss|0    |  -     | ArpTrap           |  -  |524294|   -   
|0  |192.168.20.0/23   |ROUTE| Et25               |1011 |103421  | c0:f8:7f:6a:4e:2a |  -  |288366|   -   
|0  |192.168.0.0/19    |ROUTE| Et25               |1011 |103421  | c0:f8:7f:6a:4e:2a |  -  |288366|   -   
|0  |0.0.0.0/0         |TRAP | CoppSystemL3LpmOver|0    |  -     | SlowReceive       |  -  |524292|   -   
|1  |0.0.0.0/8         |DROP | DROP               |0    |  -     |                   |  -  |288364|   -   
|1  |127.0.0.0/8       |TRAP | CoppSystemL3DstMiss|0    |  -     | ArpTrap           |  -  |524294|   -   
|1  |192.168.20.0/32   |TRAP | CoppSystemIpBcast  |0    |  -     | BcastReceive      |  -  |524288|   -   
|1  |192.168.20.172/32 |TRAP | CoppSystemIpUcast  |0    |  -     | Receive           |  -  |524291|   -   
|1  |192.168.21.255/32 |TRAP | CoppSystemIpBcast  |0    |  -     | BcastReceive      |  -  |524288|   -   
|1  |192.168.20.0/23   |TRAP | CoppSystemL3DstMiss|0    |  -     | ArpTrap           |  -  |524294|   -   
|1  |0.0.0.0/0         |TRAP | CoppSystemL3DstMiss|0    |  -     | ArpTrap           |  -  |524294|   -   
|2  |0.0.0.0/8         |DROP | DROP               |0    |  -     |                   |  -  |288370|   -   
|2  |127.0.0.0/8       |TRAP | CoppSystemL3DstMiss|0    |  -     | ArpTrap           |  -  |524294|   -   
|2  |0.0.0.0/0         |TRAP | CoppSystemL3LpmOver|0    |  -     | SlowReceive       |  -  |524292|   -   
|7  |0.0.0.0/8         |DROP | DROP               |0    |  -     |                   |  -  |288372|   -   
|7  |127.0.0.0/8       |TRAP | CoppSystemL3DstMiss|0    |  -     | ArpTrap           |  -  |524294|   -   
|7  |0.0.0.0/0         |TRAP | CoppSystemL3LpmOver|0    |  -     | SlowReceive       |  -  |524292|   -   

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
|  -  |288362|DROP | DROP               |0    |  -     |                   |   -   
|  -  |288364|DROP | DROP               |0    |  -     |                   |   -   
|  -  |288366|ROUTE| Et25               |1011 |103421  | c0:f8:7f:6a:4e:2a |   -   
|  -  |288368|ROUTE| Et25               |1011 |103421  | c0:f8:7f:6a:4e:2a |   -   
|  -  |288370|DROP | DROP               |0    |  -     |                   |   -   
|  -  |288372|DROP | DROP               |0    |  -     |                   |   -   
|  -  |288374|ROUTE| Et25               |1011 |103421  | c0:f8:7f:6a:4e:2a |   -   
|  -  |288376|ROUTE| Et52/1             |1012 |103422  | 28:99:3a:06:b4:e1 |   -   
|  -  |288378|ROUTE| Et52/1             |1012 |103422  | 28:99:3a:06:b4:e1 |   -   
|  -  |288380|ROUTE| Et52/1             |1012 |103422  | 28:99:3a:06:b4:e1 |   -   
|  -  |524288|TRAP | CoppSystemIpBcast  |0    |  -     | BcastReceive      |   -   
|  -  |524291|TRAP | CoppSystemIpUcast  |0    |  -     | Receive           |   -   
|  -  |524292|TRAP | CoppSystemL3LpmOver|0    |  -     | SlowReceive       |   -   
|  -  |524294|TRAP | CoppSystemL3DstMiss|0    |  -     | ArpTrap           |   -   
|  -  |525304|TRAP | CoppSystemL3DstMiss|1010 |1010    | ArpTrap           |   -   
|  -  |525305|TRAP | CoppSystemL3DstMiss|1011 |1011    | ArpTrap           |   -   
|  -  |525306|TRAP | CoppSystemL3DstMiss|1012 |1012    | ArpTrap           |   -   

```

