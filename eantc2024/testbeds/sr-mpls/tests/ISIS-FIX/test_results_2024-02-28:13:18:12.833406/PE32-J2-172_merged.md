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

Uptime: 1 day, 22 hours and 21 minutes
Total memory: 8099732 kB
Free memory: 5465816 kB

```

## show mac address-table

```text
          Mac Address Table
------------------------------------------------------------------

Vlan    Mac Address       Type        Ports      Moves   Last Move
----    -----------       ----        -----      -----   ---------
2301    001b.0100.0002    DYNAMIC     Mt1        3       0:11:16 ago
2301    0056.5656.5656    STATIC      Mt1
2301    00aa.aaaa.aaaa    STATIC      Mt1
2302    0056.5656.5656    STATIC      Mt1
2302    00aa.aaaa.aaaa    STATIC      Router
2302    2cdd.e996.3abb    STATIC      Router
2303    0056.5656.5656    STATIC      Mt1
2303    00aa.aaaa.aaaa    STATIC      Router
2303    2cdd.e996.3abb    STATIC      Router
2304    0056.5656.5656    STATIC      Mt1
2304    00aa.aaaa.aaaa    STATIC      Router
2304    2cdd.e996.3abb    STATIC      Router
Total Mac Addresses for this criterion: 12

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
Ethernet2      20.180.182.182/24   up          up                 9000         
Ethernet5.2    20.111.172.172/24   down        lowerlayerdown     1500         
Ethernet5.171  20.111.172.172/24   down        lowerlayerdown     1500         
Ethernet25     20.149.172.172/24   up          up                 1500         
Ethernet45     20.172.211.172/24   down        notpresent         1500         
Ethernet47     20.171.172.172/24   admin down  down               1500         
Ethernet49/1   20.57.172.172/24    admin down  down               1500         
Ethernet50/1   20.32.172.172/24    admin down  down               1500         
Ethernet51/1   20.47.172.172/24    admin down  down               1500         
Ethernet52/1   20.170.172.172/24   up          up                 1500         
Ethernet55/1   20.19.172.172/24    admin down  notpresent         1500         
Loopback0      100.0.0.182/32      up          up                65535         
Loopback209    209.209.209.209/32  up          up                65535         
Management1    192.168.20.172/23   up          up                 1500         
Vlan2302       20.30.2.254/24      up          up                 1500         
Vlan2303       20.30.3.254/24      up          up                 1500         
Vlan2304       20.30.4.254/24      up          up                 1500         

```

## show interfaces counters rates | nz

```text
Port      Name        Intvl  In Mbps      %  In Kpps Out Mbps      % Out Kpps
Et2                    0:05      8.1   0.1%        1      0.0   0.0%        0
Et6                    0:05      0.0   0.0%        0      8.0   0.1%        1
Po100                  0:05      0.0   0.0%        0      8.0   0.1%        1
```

## show isis neighbors

```text
 
Instance  VRF      System Id        Type Interface          SNPA              State Hold time   Circuit Id          
sr_eantc  default  Spine2-J-180     L2   Ethernet2          P2P               UP    25          2B                  
```

## show isis database detail

```text
Legend:
H - hostname conflict
U - node unreachable

IS-IS Instance: sr_eantc VRF: default
  IS-IS Level 2 Link State Database
    LSPID                   Seq Num  Cksum  Life Length IS  Received LSPID        Flags
    CIEN-5169-3.00-00            28  33567 52245    203 L2  0000.0000.0003.00-00  <>
      NLPID: 0xCC(IPv4)
      Hostname: CIEN-5169-3
      Area addresses: 49.0001
      Interface address: 100.0.0.3
      IS Neighbor          : Spine2-J-180.00     Metric: 10
        IPv4 Neighbor Address: 20.3.180.180
        IPv4 Interface Address: 20.3.180.3
        Adj-sid: 16000 flags: [L V] weight: 0x0
      Reachability         : 20.3.180.0/24 Metric: 10 Type: 1 Up
      Reachability         : 100.0.0.3/32 Metric: 10 Type: 1 Up
        SR Prefix-SID: 3 Flags: [N] Algorithm: 0
      Router Capabilities: Router Id: 100.0.0.3 Flags: []
        SR Capability: Flags: [I]
          SRGB Base: 20000 Range: 2000
        Algorithms:  0
    h3c_20_CR16010E-F.00-00      4355  52849  1183   1389 L2  0000.0000.0020.00-00  <>
      Remaining lifetime received: 1199 s Modified to: 1200 s
      NLPID: 0xCC(IPv4) 0x8E(IPv6)
      Hostname: h3c_20_CR16010E-F
      Area addresses: 49.0000
      Interface address: 2001:0:20:36::20
      Interface address: 2001:0:20:336::20
      Interface address: 2001:0:20:352::20
      Interface address: 2002::20
      IS Neighbor          : huawei_36.00        Metric: 10
        IPv6 Neighbor Address: 2001:0:20:36::36
        Global IPv6 Interface Address: 2001:0:20:36::20
      IS Neighbor          : huawei_36.00        Metric: 10
        IPv6 Neighbor Address: 2001:0:20:36::36
        Global IPv6 Interface Address: 2001:0:20:36::20
      IS Neighbor          : ZTE_336_ZXR10_M6000-8SE.00 Metric: 10
        IPv6 Neighbor Address: 2001:0:20:336::336
        Global IPv6 Interface Address: 2001:0:20:336::20
      IS Neighbor          : Cisco352-N540.00    Metric: 10
        IPv6 Neighbor Address: 2001:0:20:352::352
        Global IPv6 Interface Address: 2001:0:20:352::20
      IS Neighbor          : Cisco352-N540.00    Metric: 10
        IPv6 Neighbor Address: 2001:0:20:352::352
        Global IPv6 Interface Address: 2001:0:20:352::20
      Reachability          : 2001:0:20:36::/64 Metric: 10 Type: 1 Up
      Reachability          : 2001:0:20:336::/64 Metric: 10 Type: 1 Up
      Reachability          : 2001:0:20:352::/64 Metric: 10 Type: 1 Up
      Reachability          : 2002::20/128 Metric: 0 Type: 1 Up
      Reachability          : fcbb:0:20::/48 Metric: 0 Type: 1 Up
      SRv6 Locator: fcbb:0:20::/48 Topology: 0
        Metric: 0 Algorithm: 0 Flags: []
        SRv6 SID End with NEXT-CSID PSP USD
          SID : fcbb:0:20::
          SID structure: Block length: 32 Node length: 16
                         Function length: 0 Argument length: 0
        SRv6 SID End
          SID : fcbb:0:20:e102::
          SID structure: Block length: 32 Node length: 16
                         Function length: 16 Argument length: 0
        SRv6 SID End with PSP USP USD
          SID : fcbb:0:20:e103::
          SID structure: Block length: 32 Node length: 16
                         Function length: 16 Argument length: 0
      SRv6 Locator: fcbb:1:20::/48 Topology: 0
        Metric: 0 Algorithm: 128 Flags: []
        SRv6 SID End with NEXT-CSID PSP USD
          SID : fcbb:1:20::
          SID structure: Block length: 32 Node length: 16
                         Function length: 0 Argument length: 0
        SRv6 SID End
          SID : fcbb:1:20:e102::
          SID structure: Block length: 32 Node length: 16
                         Function length: 16 Argument length: 0
        SRv6 SID End with PSP USP USD
          SID : fcbb:1:20:e103::
          SID structure: Block length: 32 Node length: 16
                         Function length: 16 Argument length: 0
    h3c_20_CR16010E-F.00-01      1921  17284  1182    856 L2  0000.0000.0020.00-01  <>
      Remaining lifetime received: 1199 s Modified to: 1200 s
      IS Neighbor          : huawei_36.00        Metric: 10
        IPv6 Neighbor Address: 2001:0:20:36::36
        Global IPv6 Interface Address: 2001:0:20:36::20
      IS Neighbor          : ZTE_336_ZXR10_M6000-8SE.00 Metric: 10
        IPv6 Neighbor Address: 2001:0:20:336::336
        Global IPv6 Interface Address: 2001:0:20:336::20
      IS Neighbor          : ZTE_336_ZXR10_M6000-8SE.00 Metric: 10
        IPv6 Neighbor Address: 2001:0:20:336::336
        Global IPv6 Interface Address: 2001:0:20:336::20
      IS Neighbor          : Cisco352-N540.00    Metric: 10
        IPv6 Neighbor Address: 2001:0:20:352::352
        Global IPv6 Interface Address: 2001:0:20:352::20
      Router Capabilities: Router Id: 0.0.0.0 Flags: []
        SRv6 Capability: Flags: []
        Algorithms:  0, 128, 129, 130, 131
        Flex Algo: Algorithm: 128 Metric: Min Unidirectional Delay Metric (1) Calc: SPF (0) Prio: 100
          Flags: [M] 0x80
        Flex Algo: Algorithm: 129 Metric: TE Metric (2) Calc: SPF (0) Prio: 100
          Flags: [M] 0x80
        Flex Algo: Algorithm: 130 Metric: IGP Metric (0) Calc: SPF (0) Prio: 100
          Exclude admin groups: 1
          Flags: [M] 0x80
        Flex Algo: Algorithm: 131 Metric: IGP Metric (0) Calc: SPF (0) Prio: 100
          Exclude admin groups: 255
          Flags: [M] 0x80
    0000.0000.0021.00-00        440  44683   670    128 L2  0000.0000.0021.00-00  <>
      Remaining lifetime received: 1199 s Modified to: 1200 s
      NLPID: 0xCC(IPv4) 0x8E(IPv6)
      Area addresses: 49.0001
      Topology: 0 (IPv4)
      Topology: 2 (IPv6)
      Interface address: 20.21.180.21
      Interface address: 100.0.0.21
      IS Neighbor          : Spine2-J-180.00     Metric: 10
      Reachability         : 20.21.180.0/24 Metric: 10 Type: 1 Up
      Reachability         : 100.0.0.21/32 Metric: 0 Type: 1 Up
        SR Prefix-SID: 21 Flags: [N] Algorithm: 0
      Reachability         : 192.168.20.0/23 Metric: 0 Type: 1 Up
      Router Capabilities: Router Id: 100.0.0.21 Flags: []
        Maximum SID depth:
          Base MPLS imposition (MSD type 1):  13
        SR Capability: Flags: [I]
          SRGB Base: 20000 Range: 2000
    h3c_26_S12500R-2L.00-00       290   5387   662    139 L2  0000.0000.0026.00-00  <>
      Remaining lifetime received: 1199 s Modified to: 1200 s
      NLPID: 0xCC(IPv4) 0x8E(IPv6)
      Hostname: h3c_26_S12500R-2L
      Area addresses: 49.0001
      Topology: 0 (IPv4)
      Topology: 2 (IPv6)
      Interface address: 20.26.180.26
      Interface address: 100.0.0.26
      IS Neighbor          : Spine2-J-180.00     Metric: 10
      Reachability         : 20.26.180.0/24 Metric: 10 Type: 1 Up
      Reachability         : 100.0.0.26/32 Metric: 0 Type: 1 Up
        SR Prefix-SID: 26 Flags: [N P] Algorithm: 0
      Router Capabilities: Router Id: 100.0.0.26 Flags: []
        Maximum SID depth:
          Base MPLS imposition (MSD type 1):  10
        SR Capability: Flags: [I]
          SRGB Base: 20000 Range: 2000
    h3c_28_S12500R-2L.00-00      1698  13914  1138    964 L2  0000.0000.0028.00-00  <>
      Remaining lifetime received: 1199 s Modified to: 1200 s
      NLPID: 0xCC(IPv4) 0x8E(IPv6)
      Hostname: h3c_28_S12500R-2L
      Area addresses: 49
      Interface address: 2001:0:28:316::28
      Interface address: 2001:0:28:336::28
      Interface address: 2001:0:28:352::28
      Interface address: 2002::28
      IS Neighbor          : JNPR-316-MX304.00   Metric: 10
        IPv6 Neighbor Address: 2001:0:28:316::316
        Global IPv6 Interface Address: 2001:0:28:316::28
      IS Neighbor          : JNPR-316-MX304.00   Metric: 10
        IPv6 Neighbor Address: 2001:0:28:316::316
        Global IPv6 Interface Address: 2001:0:28:316::28
      IS Neighbor          : ZTE_336_ZXR10_M6000-8SE.00 Metric: 10
        IPv6 Neighbor Address: 2001:0:28:336::336
        Global IPv6 Interface Address: 2001:0:28:336::28
      IS Neighbor          : ZTE_336_ZXR10_M6000-8SE.00 Metric: 10
        IPv6 Neighbor Address: 2001:0:28:336::336
        Global IPv6 Interface Address: 2001:0:28:336::28
      IS Neighbor          : Cisco352-N540.00    Metric: 10
        IPv6 Neighbor Address: 2001:0:28:352::352
        Global IPv6 Interface Address: 2001:0:28:352::28
      IS Neighbor          : Cisco352-N540.00    Metric: 10
        IPv6 Neighbor Address: 2001:0:28:352::352
        Global IPv6 Interface Address: 2001:0:28:352::28
      Reachability          : 2001:0:28:316::/64 Metric: 10 Type: 1 Up
      Reachability          : 2001:0:28:336::/64 Metric: 10 Type: 1 Up
      Reachability          : 2001:0:28:352::/64 Metric: 10 Type: 1 Up
      Reachability          : 2002::28/128 Metric: 0 Type: 1 Up
      Reachability          : fcbb:0:28::/48 Metric: 0 Type: 1 Up
      SRv6 Locator: fcbb:0:28::/48 Topology: 0
        Metric: 0 Algorithm: 0 Flags: []
        SRv6 SID End with NEXT-CSID PSP USD
          SID : fcbb:0:28::
          SID structure: Block length: 32 Node length: 16
                         Function length: 0 Argument length: 0
      SRv6 Locator: fcbb:1:28::/48 Topology: 0
        Metric: 0 Algorithm: 128 Flags: []
        SRv6 SID End with NEXT-CSID PSP USD
          SID : fcbb:1:28::
          SID structure: Block length: 32 Node length: 16
                         Function length: 0 Argument length: 0
      Router Capabilities: Router Id: 0.0.0.0 Flags: []
        SRv6 Capability: Flags: []
        Algorithms:  0, 128
        Flex Algo: Algorithm: 128 Metric: Min Unidirectional Delay Metric (1) Calc: SPF (0) Prio: 100
          Flags: [] 0x1
    Huawei-34.00-00             257  50426  1044    139 L2  0000.0000.0034.00-00  <>
      Remaining lifetime received: 1199 s Modified to: 1200 s
      NLPID: 0xCC(IPv4)
      Hostname: Huawei-34
      Area addresses: 49.0001
      Interface address: 100.0.0.34
      Interface address: 20.34.180.34
      IS Neighbor          : Spine2-J-180.00     Metric: 10
        IPv4 Neighbor Address: 20.34.180.180
        IPv4 Interface Address: 20.34.180.34
        Adj-sid: 48000 flags: [L V] weight: 0x0
      Reachability         : 100.0.0.34/32 Metric: 0 Type: 1 Up
        SR Prefix-SID: 34 Flags: [N] Algorithm: 0
      Reachability         : 20.34.180.0/24 Metric: 10 Type: 1 Up
      Router Capabilities: Router Id: 100.0.0.34 Flags: []
        Maximum SID depth:
          Base MPLS imposition (MSD type 1):  10
        SR Capability: Flags: [I]
          SRGB Base: 20000 Range: 2000
    huawei_36.00-00             253  62393  1044   1030 L2  0000.0000.0036.00-00  <>
      Remaining lifetime received: 1199 s Modified to: 1200 s
      NLPID: 0x8E(IPv6)
      Hostname: huawei_36
      Area addresses: 49.0000
      Topology: 0 (IPv4)
      Interface address: 2002::36
      Interface address: 2001:0:36:58::36
      Interface address: 2001:0:20:36::36
      IS Neighbor          : Nokia_58-SR1-3-SRv6.00 Metric: 10
        IPv6 Neighbor Address: 2001:0:36:58::58
        Global IPv6 Interface Address: 2001:0:36:58::36
      IS Neighbor          : Nokia_58-SR1-3-SRv6.00 Metric: 10
        IPv6 Neighbor Address: 2001:0:36:58::58
        Global IPv6 Interface Address: 2001:0:36:58::36
      Reachability          : 2002::36/128 Metric: 0 Type: 1 Up
      Reachability          : fcbb:0:36::/48 Metric: 0 Type: 1 Up
      Reachability          : 2001:0:36:58::/64 Metric: 10 Type: 1 Up
      Reachability          : 2001:0:20:36::/64 Metric: 10 Type: 1 Up
      SRv6 Locator: fcbb:1:36::/48 Topology: 0
        Metric: 0 Algorithm: 128 Flags: []
        SRv6 SID End with NEXT-CSID PSP USD
          SID : fcbb:1:36::
          SID structure: Block length: 32 Node length: 16
                         Function length: 0 Argument length: 80
        SRv6 SID Un Supported
          SID : fcbb:1:36:e004::
          SID structure: Block length: 32 Node length: 16
                         Function length: 16 Argument length: 64
        SRv6 SID End
          SID : fcbb:1:36:e005::
          SID structure: Block length: 32 Node length: 16
                         Function length: 16 Argument length: 0
        SRv6 SID End with PSP
          SID : fcbb:1:36:e006::
          SID structure: Block length: 32 Node length: 16
                         Function length: 16 Argument length: 0
        SRv6 SID End with PSP USP USD
          SID : fcbb:1:36:e007::
          SID structure: Block length: 32 Node length: 16
                         Function length: 16 Argument length: 0
      SRv6 Locator: fcbb:0:36::/48 Topology: 0
        Metric: 0 Algorithm: 0 Flags: []
        SRv6 SID End with NEXT-CSID PSP USD
          SID : fcbb:0:36::
          SID structure: Block length: 32 Node length: 16
                         Function length: 0 Argument length: 80
        SRv6 SID Un Supported
          SID : fcbb:0:36:e004::
          SID structure: Block length: 32 Node length: 16
                         Function length: 16 Argument length: 64
        SRv6 SID End
          SID : fcbb:0:36:e005::
          SID structure: Block length: 32 Node length: 16
                         Function length: 16 Argument length: 0
        SRv6 SID End with PSP
          SID : fcbb:0:36:e006::
          SID structure: Block length: 32 Node length: 16
                         Function length: 16 Argument length: 0
        SRv6 SID End with PSP USP USD
          SID : fcbb:0:36:e007::
          SID structure: Block length: 32 Node length: 16
                         Function length: 16 Argument length: 0
      Router Capabilities: Router Id: 0.0.0.0 Flags: []
        SRv6 Capability: Flags: []
        Algorithms:  0, 128, 129, 130
      Router Capabilities: Router Id: 0.0.0.0 Flags: []
        Flex Algo: Algorithm: 128 Metric: Min Unidirectional Delay Metric (1) Calc: SPF (0) Prio: 128
          Flags: [M] 0x80
        Flex Algo: Algorithm: 129 Metric: TE Metric (2) Calc: SPF (0) Prio: 128
          Flags: [M] 0x80
        Flex Algo: Algorithm: 130 Metric: IGP Metric (0) Calc: SPF (0) Prio: 128
          Exclude admin groups: 1
          Flags: [M] 0x80
    huawei_36.00-01             915  22718   946    465 L2  0000.0000.0036.00-01  <>
      Remaining lifetime received: 1199 s Modified to: 1200 s
      IS Neighbor          : h3c_20_CR16010E-F.00 Metric: 10
        IPv6 Neighbor Address: 2001:0:20:36::20
        Global IPv6 Interface Address: 2001:0:20:36::36
      IS Neighbor          : h3c_20_CR16010E-F.00 Metric: 10
        IPv6 Neighbor Address: 2001:0:20:36::20
        Global IPv6 Interface Address: 2001:0:20:36::36
    anet-161-R3.00-00           266   8442   986    334 L2  0000.0000.0161.00-00  <>
      Remaining lifetime received: 1199 s Modified to: 1200 s
      NLPID: 0xCC(IPv4) 0x8E(IPv6)
      Hostname: anet-161-R3
      Area addresses: 49.0000
      Interface address: 20.161.180.161
      Interface address: 100.0.0.161
      Interface address: 2001:0:59:161::161
      Interface address: 2001:0:161:342::161
      Interface address: 2002::161
      IS Neighbor          : Spine2-J-180.00     Metric: 10
        IPv4 Neighbor Address: 20.161.180.180
        IPv4 Interface Address: 20.161.180.161
        Adj-sid: 100001 flags: [L V] weight: 0x0
      IS Neighbor          : Cisco342-9902.00    Metric: 10
      Reachability         : 20.161.180.0/24 Metric: 10 Type: 1 Up
      Reachability         : 100.0.0.161/32 Metric: 10 Type: 1 Up
        SR Prefix-SID: 161 Flags: [N] Algorithm: 0
      Reachability          : fcbb:0:161::/48 Metric: 10 Type: 1 Up
      Reachability          : 2001:0:59:161::/64 Metric: 10 Type: 1 Up
      Reachability          : 2001:0:161:342::/64 Metric: 10 Type: 1 Up
      Reachability          : 2002::161/128 Metric: 10 Type: 1 Up
      SRv6 Locator: fcbb:0:161::/48 Topology: 0
        Metric: 10 Algorithm: 0 Flags: []
        SRv6 SID End with NEXT-CSID PSP USD
          SID : fcbb:0:161::
          SID structure: Block length: 32 Node length: 16
                         Function length: 16 Argument length: 0
      Router Capabilities: Router Id: 100.0.0.161 Flags: []
        SR Local Block:
          SRLB Base: 965536 Range: 65536
        Area leader priority: 250 algorithm: 0
        Maximum SID depth:
          Base MPLS imposition (MSD type 1):  12
        SRv6 Capability: Flags: []
        SR Capability: Flags: [I V]
          SRGB Base: 900000 Range: 65536
    JNPR-307-ACX7024.00-00      1636  51562  1134    666 L2  0000.0000.0307.00-00  <>
      Remaining lifetime received: 1199 s Modified to: 1200 s
      NLPID: 0x8E(IPv6)
      Hostname: JNPR-307-ACX7024
      Area addresses: 49.0000
      Interface address: 10.0.1.7
      IS Neighbor          : Cisco352-N540.00    Metric: 10
        IPv6 Neighbor Address: 2001:0:307:352::352
        Global IPv6 Interface Address: 2001:0:307:352::307
      IS Neighbor          : Cisco353-8201-24H8FH.00 Metric: 10
        IPv6 Neighbor Address: 2001:0:307:353::353
        Global IPv6 Interface Address: 2001:0:307:353::307
      Reachability          : 2002::307/128 Metric: 0 Type: 1 Up
      Reachability          : 2001:0:307:353::/64 Metric: 10 Type: 1 Up
      Reachability          : 2001:0:307:352::/64 Metric: 10 Type: 1 Up
      Reachability          : fcbb:0:307::/48 Metric: 0 Type: 1 Up
      Reachability          : fcbb:0:9307::/48 Metric: 0 Type: 1 Up
      SRv6 Locator: fcbb:7:307::/48 Topology: 0
        Metric: 0 Algorithm: 134 Flags: []
      SRv6 Locator: fcbb:5:307::/48 Topology: 0
        Metric: 0 Algorithm: 132 Flags: []
      SRv6 Locator: fcbb:0:307::/48 Topology: 0
        Metric: 0 Algorithm: 0 Flags: []
      SRv6 Locator: fcbb:1:307::/48 Topology: 0
        Metric: 0 Algorithm: 128 Flags: []
      SRv6 Locator: fcbb:0:9307::/48 Topology: 0
        Metric: 0 Algorithm: 0 Flags: []
        SRv6 SID End with NEXT-CSID PSP USP USD
          SID : fcbb:0:9307::
          SID structure: Block length: 32 Node length: 16
                         Function length: 0 Argument length: 80
      SRv6 Locator: fcbb:2:307::/48 Topology: 0
        Metric: 0 Algorithm: 129 Flags: []
      SRv6 Locator: fcbb:3:307::/48 Topology: 0
        Metric: 0 Algorithm: 130 Flags: []
      Router Capabilities: Router Id: 10.0.1.7 Flags: []
        Maximum SID depth:
          Base MPLS imposition (MSD type 1):  0
        SRv6 Capability: Flags: []
        Algorithms:  0, 1, 128, 129, 130, 132, 134
        Flex Algo: Algorithm: 134 Metric: IGP Metric (0) Calc: SPF (0) Prio: 255
        Flex Algo: Algorithm: 133 Metric: IGP Metric (0) Calc: SPF (0) Prio: 255
        Flex Algo: Algorithm: 132 Metric: IGP Metric (0) Calc: SPF (0) Prio: 255
        Flex Algo: Algorithm: 130 Metric: IGP Metric (0) Calc: SPF (0) Prio: 0
          Exclude admin groups: 1
        Flex Algo: Algorithm: 129 Metric: TE Metric (2) Calc: SPF (0) Prio: 0
      Unsupported TLV: Type: 14 Length: 2
    JNPR-310-ACX7100-48L.00-00     13503  30981  1179    774 L2  0000.0000.0310.00-00  <>
      Remaining lifetime received: 1199 s Modified to: 1200 s
      NLPID: 0x8E(IPv6)
      Hostname: JNPR-310-ACX7100-48L
      Area addresses: 49.0001
      Interface address: 10.0.1.10
      IS Neighbor          : Nokia_58-SR1-3-SRv6.00 Metric: 10
        IPv6 Neighbor Address: 2001:0:58:310::58
        Global IPv6 Interface Address: 2001:0:58:310::310
      IS Neighbor          : Cisco353-8201-24H8FH.00 Metric: 10
        IPv6 Neighbor Address: 2001:0:310:353::353
        Global IPv6 Interface Address: 2001:0:310:353::353
      Reachability          : 2002::310/128 Metric: 0 Type: 1 Up
      Reachability          : 2002::/72 Metric: 10 Type: 1 Up
      Reachability          : 2001:0:58:310::/64 Metric: 10 Type: 1 Up
      Reachability          : 2001:0:310:353::/64 Metric: 10 Type: 1 Up
      Reachability          : 2001:25:110:225::/64 Metric: 10 Type: 1 Up
      Reachability          : 2001:0:11:310::/64 Metric: 10 Type: 1 Up
      Reachability          : fcbb:0:1000::/36 Metric: 10 Type: 1 Up
      Reachability          : fcbb:0:9310::/48 Metric: 0 Type: 1 Up
      Reachability          : fcbb:0:1310::/48 Metric: 0 Type: 1 Up
      SRv6 Locator: fcbb:7:1310::/48 Topology: 0
        Metric: 0 Algorithm: 134 Flags: []
      SRv6 Locator: fcbb:5:1310::/48 Topology: 0
        Metric: 0 Algorithm: 132 Flags: []
      SRv6 Locator: fcbb:0:9310::/48 Topology: 0
        Metric: 0 Algorithm: 0 Flags: []
        SRv6 SID End with NEXT-CSID PSP USP USD
          SID : fcbb:0:9310::
          SID structure: Block length: 32 Node length: 16
                         Function length: 0 Argument length: 80
      SRv6 Locator: fcbb:2:1310::/48 Topology: 0
        Metric: 0 Algorithm: 129 Flags: []
      SRv6 Locator: fcbb:3:1310::/48 Topology: 0
        Metric: 0 Algorithm: 130 Flags: []
      SRv6 Locator: fcbb:0:1310::/48 Topology: 0
        Metric: 0 Algorithm: 0 Flags: []
      SRv6 Locator: fcbb:1:1310::/48 Topology: 0
        Metric: 0 Algorithm: 128 Flags: []
      SRv6 Locator: fcbb:0:1000::/36 Topology: 0
        Metric: 10 Algorithm: 0 Flags: []
      SRv6 Locator: fcbb:1:1000::/36 Topology: 0
        Metric: 10 Algorithm: 128 Flags: []
      Router Capabilities: Router Id: 10.0.1.10 Flags: []
        Maximum SID depth:
          Base MPLS imposition (MSD type 1):  0
        SRv6 Capability: Flags: []
        Algorithms:  0, 1, 128, 129, 130, 132, 134
        Flex Algo: Algorithm: 134 Metric: IGP Metric (0) Calc: SPF (0) Prio: 255
        Flex Algo: Algorithm: 133 Metric: IGP Metric (0) Calc: SPF (0) Prio: 255
        Flex Algo: Algorithm: 132 Metric: IGP Metric (0) Calc: SPF (0) Prio: 255
        Flex Algo: Algorithm: 130 Metric: IGP Metric (0) Calc: SPF (0) Prio: 0
          Exclude admin groups: 1
        Flex Algo: Algorithm: 129 Metric: TE Metric (2) Calc: SPF (0) Prio: 0
      Unsupported TLV: Type: 14 Length: 2
    JNPR-316-MX304.00-00       1313  41528  1044    839 L2  0000.0000.0316.00-00  <>
      Remaining lifetime received: 1199 s Modified to: 1200 s
      NLPID: 0x8E(IPv6)
      Hostname: JNPR-316-MX304
      Area addresses: 49.0000
      Interface address: 10.0.1.16
      IS Neighbor          : h3c_28_S12500R-2L.00 Metric: 10
        IPv6 Neighbor Address: 2001:0:28:316::28
        Global IPv6 Interface Address: 2001:0:28:316::316
      IS Neighbor          : Cisco342-9902.00    Metric: 10
        IPv6 Neighbor Address: 2001:0:316:342::342
        Global IPv6 Interface Address: 2001:0:316:342::316
      Reachability          : 2001:0:28:316::/64 Metric: 10 Type: 1 Up
      Reachability          : 2002::316/128 Metric: 0 Type: 1 Up
      Reachability          : 2001:0:316:342::/64 Metric: 10 Type: 1 Up
      Reachability          : fcbb:0:316::/48 Metric: 0 Type: 1 Up
      SRv6 Locator: fcbb:0:316::/48 Topology: 0
        Metric: 0 Algorithm: 0 Flags: []
        SRv6 SID End with NEXT-CSID PSP USP USD
          SID : fcbb:0:316::
          SID structure: Block length: 32 Node length: 16
                         Function length: 0 Argument length: 80
      SRv6 Locator: fcbb:1:316::/48 Topology: 0
        Metric: 0 Algorithm: 128 Flags: []
        SRv6 SID End with NEXT-CSID PSP USP USD
          SID : fcbb:1:316::
          SID structure: Block length: 32 Node length: 16
                         Function length: 0 Argument length: 80
      SRv6 Locator: fcbb:2:316::/48 Topology: 0
        Metric: 0 Algorithm: 129 Flags: []
        SRv6 SID End with NEXT-CSID PSP USP USD
          SID : fcbb:2:316::
          SID structure: Block length: 32 Node length: 16
                         Function length: 0 Argument length: 80
      SRv6 Locator: fcbb:3:316::/48 Topology: 0
        Metric: 0 Algorithm: 130 Flags: []
        SRv6 SID End with NEXT-CSID PSP USP USD
          SID : fcbb:3:316::
          SID structure: Block length: 32 Node length: 16
                         Function length: 0 Argument length: 80
      SRv6 Locator: fcbb:5:316::/48 Topology: 0
        Metric: 0 Algorithm: 132 Flags: []
        SRv6 SID End with NEXT-CSID PSP USP USD
          SID : fcbb:5:316::
          SID structure: Block length: 32 Node length: 16
                         Function length: 0 Argument length: 80
      SRv6 Locator: fcbb:6:316::/48 Topology: 0
        Metric: 0 Algorithm: 133 Flags: []
        SRv6 SID End with NEXT-CSID PSP USP USD
          SID : fcbb:6:316::
          SID structure: Block length: 32 Node length: 16
                         Function length: 0 Argument length: 80
      SRv6 Locator: fcbb:7:316::/48 Topology: 0
        Metric: 0 Algorithm: 134 Flags: []
        SRv6 SID End with NEXT-CSID PSP USP USD
          SID : fcbb:7:316::
          SID structure: Block length: 32 Node length: 16
                         Function length: 0 Argument length: 80
      Router Capabilities: Router Id: 10.0.1.16 Flags: []
        Maximum SID depth:
          Base MPLS imposition (MSD type 1):  0
        SRv6 Capability: Flags: []
        Algorithms:  0, 1, 128, 129, 130, 132, 133, 134
        Flex Algo: Algorithm: 134 Metric: IGP Metric (0) Calc: SPF (0) Prio: 255
        Flex Algo: Algorithm: 133 Metric: IGP Metric (0) Calc: SPF (0) Prio: 255
        Flex Algo: Algorithm: 132 Metric: IGP Metric (0) Calc: SPF (0) Prio: 255
        Flex Algo: Algorithm: 130 Metric: IGP Metric (0) Calc: SPF (0) Prio: 0
          Exclude admin groups: 1
        Flex Algo: Algorithm: 129 Metric: TE Metric (2) Calc: SPF (0) Prio: 0
      Unsupported TLV: Type: 14 Length: 2
    ZTE_336_ZXR10_M6000-8SE.00-00      3527  59579  1178   1198 L2  0000.0000.0336.00-00  <>
      Remaining lifetime received: 1199 s Modified to: 1200 s
      NLPID: 0xCC(IPv4) 0x8E(IPv6)
      Hostname: ZTE_336_ZXR10_M6000-8SE
      Area addresses: 49.0000
      Interface address: 10.0.1.36
      Interface address: 2002::336
      IS Neighbor          : h3c_20_CR16010E-F.00 Metric: 10
        IPv6 Neighbor Address: 2001:0:20:336::20
        Global IPv6 Interface Address: 2001:0:20:336::336
      IS Neighbor          : h3c_20_CR16010E-F.00 Metric: 10
        IPv6 Neighbor Address: 2001:0:20:336::20
        Global IPv6 Interface Address: 2001:0:20:336::336
      IS Neighbor          : h3c_28_S12500R-2L.00 Metric: 10
        IPv6 Neighbor Address: 2001:0:28:336::28
        Global IPv6 Interface Address: 2001:0:28:336::336
      IS Neighbor          : h3c_28_S12500R-2L.00 Metric: 10
        IPv6 Neighbor Address: 2001:0:28:336::28
        Global IPv6 Interface Address: 2001:0:28:336::336
      Reachability         : 10.0.1.36/32 Metric: 10 Type: 1 Up
      Reachability          : 2001:0:20:336::/64 Metric: 10 Type: 1 Up
      Reachability          : 2001:0:28:336::/64 Metric: 10 Type: 1 Up
      Reachability          : 2002::336/128 Metric: 10 Type: 1 Up
      Reachability          : fcbb:0:336::/48 Metric: 0 Type: 1 Up
      SRv6 Locator: fcbb:0:336::/48 Topology: 0
        Metric: 0 Algorithm: 0 Flags: []
        SRv6 SID End with NEXT-CSID PSP
          SID : fcbb:0:336::
          SID structure: Block length: 32 Node length: 16
                         Function length: 0 Argument length: 80
      SRv6 Locator: fcbb:1:336::/48 Topology: 0
        Metric: 0 Algorithm: 128 Flags: []
        SRv6 SID End with NEXT-CSID PSP
          SID : fcbb:1:336::
          SID structure: Block length: 32 Node length: 16
                         Function length: 0 Argument length: 80
      SRv6 Locator: fcbb:2:336::/48 Topology: 0
        Metric: 0 Algorithm: 129 Flags: []
        SRv6 SID End with NEXT-CSID PSP
          SID : fcbb:2:336::
          SID structure: Block length: 32 Node length: 16
                         Function length: 0 Argument length: 80
      SRv6 Locator: fcbb:3:336::/48 Topology: 0
        Metric: 0 Algorithm: 130 Flags: []
        SRv6 SID End with NEXT-CSID PSP
          SID : fcbb:3:336::
          SID structure: Block length: 32 Node length: 16
                         Function length: 0 Argument length: 80
      SRv6 Locator: fcbb:4:336::/48 Topology: 0
        Metric: 0 Algorithm: 131 Flags: []
        SRv6 SID End with NEXT-CSID PSP
          SID : fcbb:4:336::
          SID structure: Block length: 32 Node length: 16
                         Function length: 0 Argument length: 80
      Router Capabilities: Router Id: 10.0.1.36 Flags: []
        SR Local Block:
          SRLB Base: 965536 Range: 4096
        Maximum SID depth:
          Base MPLS imposition (MSD type 1):  20
        SRv6 Capability: Flags: []
        SR Capability: Flags: [I]
          SRGB Base: 900000 Range: 65536
        Algorithms:  0, 1, 128, 129, 130, 131
        Flex Algo: Algorithm: 128 Metric: Min Unidirectional Delay Metric (1) Calc: SPF (0) Prio: 100
        Flex Algo: Algorithm: 129 Metric: TE Metric (2) Calc: SPF (0) Prio: 128
        Flex Algo: Algorithm: 130 Metric: IGP Metric (0) Calc: SPF (0) Prio: 128
          Exclude admin groups: 1
        Flex Algo: Algorithm: 131 Metric: IGP Metric (0) Calc: SPF (0) Prio: 128
          Exclude admin groups: 1,231
    h41-9902.00-00              255  17663   480    176 L2  0000.0000.0341.00-00  <>
      Remaining lifetime received: 1199 s Modified to: 1200 s
      NLPID: 0xCC(IPv4)
      Hostname: h41-9902
      Area addresses: 49.0001
      Interface address: 100.0.3.41
      IS Neighbor          : Spine2-J-180.00     Metric: 10
        IPv4 Neighbor Address: 30.41.180.180
        IPv4 Interface Address: 30.41.180.41
        Adj-sid: 24004 flags: [L V] weight: 0x0
      Reachability         : 30.41.180.0/24 Metric: 10 Type: 1 Up
      Reachability         : 100.0.3.41/32 Metric: 10 Type: 1 Up
        SR Prefix-SID: 341 Flags: [N] Algorithm: 0
      Router Capabilities: Router Id: 100.0.3.41 Flags: []
        SR Local Block:
          SRLB Base: 15000 Range: 1000
        Maximum SID depth:
          Base MPLS imposition (MSD type 1):  10
        SR Capability: Flags: [I]
          SRGB Base: 20000 Range: 2000
        Algorithms:  0, 1
      Unsupported TLV: Type: 14 Length: 2
    Cisco342-9902.00-00         322  50800  1155    563 L2  0000.0000.0342.00-00  <>
      Remaining lifetime received: 1199 s Modified to: 1200 s
      NLPID: 0x8E(IPv6)
      Hostname: Cisco342-9902
      Area addresses: 49.0001
      Interface address: 2002::342
      IS Neighbor          : anet-161-R3.00      Metric: 10
        Global IPv6 Interface Address: 2001:0:161:342::342
      IS Neighbor          : JNPR-316-MX304.00   Metric: 10
        IPv6 Neighbor Address: 2001:0:316:342::316
        Global IPv6 Interface Address: 2001:0:316:342::342
      Reachability          : 2001:0:161:342::/64 Metric: 10 Type: 1 Up
      Reachability          : 2001:0:316:342::/64 Metric: 10 Type: 1 Up
      Reachability          : 2002::342/128 Metric: 10 Type: 1 Up
      Reachability          : fcbb:0:342::/48 Metric: 1 Type: 1 Up
      SRv6 Locator: fcbb:0:342::/48 Topology: 0
        Metric: 1 Algorithm: 0 Flags: []
        SRv6 SID End with NEXT-CSID PSP USD
          SID : fcbb:0:342::
          SID structure: Block length: 32 Node length: 16
                         Function length: 0 Argument length: 80
      SRv6 Locator: fcbb:1:342::/48 Topology: 0
        Metric: 1 Algorithm: 128 Flags: []
        SRv6 SID End with NEXT-CSID PSP USD
          SID : fcbb:1:342::
          SID structure: Block length: 32 Node length: 16
                         Function length: 0 Argument length: 80
      Router Capabilities: Router Id: 0.0.0.0 Flags: []
        SRv6 Capability: Flags: []
        Algorithms:  0, 1, 128
      Unsupported TLV: Type: 14 Length: 2
    h45-N57C1.00-00             257  29764   502    177 L2  0000.0000.0345.00-00  <>
      Remaining lifetime received: 1199 s Modified to: 1200 s
      NLPID: 0xCC(IPv4)
      Hostname: h45-N57C1
      Area addresses: 49.0001
      Interface address: 100.0.3.45
      IS Neighbor          : Spine2-J-180.00     Metric: 10
        IPv4 Neighbor Address: 30.45.180.180
        IPv4 Interface Address: 30.45.180.45
        Adj-sid: 28103 flags: [L V] weight: 0x0
      Reachability         : 30.45.180.0/24 Metric: 10 Type: 1 Up
      Reachability         : 100.0.3.45/32 Metric: 10 Type: 1 Up
        SR Prefix-SID: 345 Flags: [N] Algorithm: 0
      Router Capabilities: Router Id: 100.0.3.45 Flags: []
        SR Local Block:
          SRLB Base: 15000 Range: 1000
        Maximum SID depth:
          Base MPLS imposition (MSD type 1):  12
        SR Capability: Flags: [I]
          SRGB Base: 20000 Range: 2000
        Algorithms:  0, 1
      Unsupported TLV: Type: 14 Length: 2
    Cisco352-N540.00-00         311  10008   700    943 L2  0000.0000.0352.00-00  <>
      Remaining lifetime received: 1199 s Modified to: 1200 s
      NLPID: 0x8E(IPv6)
      Hostname: Cisco352-N540
      Area addresses: 49.0001
      Interface address: 2002::352
      IS Neighbor          : h3c_20_CR16010E-F.00 Metric: 10
        IPv6 Neighbor Address: 2001:0:20:352::20
        Global IPv6 Interface Address: 2001:0:20:352::352
      IS Neighbor          : h3c_28_S12500R-2L.00 Metric: 10
        IPv6 Neighbor Address: 2001:0:28:352::28
        Global IPv6 Interface Address: 2001:0:28:352::352
      IS Neighbor          : JNPR-307-ACX7024.00 Metric: 10
        IPv6 Neighbor Address: 2001:0:307:352::307
        Global IPv6 Interface Address: 2001:0:307:352::352
      IS Neighbor          : Nokia-59-IXRe2.00   Metric: 10
        IPv6 Neighbor Address: 2001:0:59:352::59
        Global IPv6 Interface Address: 2001:0:59:352::352
      Reachability          : 2001:0:20:352::/64 Metric: 10 Type: 1 Up
      Reachability          : 2001:0:28:352::/64 Metric: 10 Type: 1 Up
      Reachability          : 2001:0:59:352::/64 Metric: 10 Type: 1 Up
      Reachability          : 2001:0:307:352::/64 Metric: 10 Type: 1 Up
      Reachability          : 2002::352/128 Metric: 10 Type: 1 Up
      Reachability          : fcbb:0:352::/48 Metric: 1 Type: 1 Up
      SRv6 Locator: fcbb:0:352::/48 Topology: 0
        Metric: 1 Algorithm: 0 Flags: []
        SRv6 SID End with NEXT-CSID PSP USD
          SID : fcbb:0:352::
          SID structure: Block length: 32 Node length: 16
                         Function length: 0 Argument length: 80
      SRv6 Locator: fcbb:1:352::/48 Topology: 0
        Metric: 1 Algorithm: 128 Flags: []
        SRv6 SID End with NEXT-CSID PSP USD
          SID : fcbb:1:352::
          SID structure: Block length: 32 Node length: 16
                         Function length: 0 Argument length: 80
      Router Capabilities: Router Id: 0.0.0.0 Flags: []
        SRv6 Capability: Flags: []
        Algorithms:  0, 1, 128
      Unsupported TLV: Type: 14 Length: 2
    Cisco353-8201-24H8FH.00-00      2448  64258   659    979 L2  0000.0000.0353.00-00  <>
      Remaining lifetime received: 1199 s Modified to: 1200 s
      NLPID: 0x8E(IPv6)
      Hostname: Cisco353-8201-24H8FH
      Area addresses:
        49.0000
        49.0001
      Interface address: 2002::353
      IS Neighbor          : JNPR-307-ACX7024.00 Metric: 10
        IPv6 Neighbor Address: 2001:0:307:353::307
        Global IPv6 Interface Address: 2001:0:307:353::353
      IS Neighbor          : JNPR-310-ACX7100-48L.00 Metric: 10
        IPv6 Neighbor Address: 2001:0:310:353::353
        Global IPv6 Interface Address: 2001:0:310:353::353
      Reachability          : 2001:0:11:310::/64 Metric: 20 Type: 1 Up
      Reachability          : 2001:0:11:353::/64 Metric: 10 Type: 1 Up
      Reachability          : 2001:0:29:338::/64 Metric: 40 Type: 1 Up
      Reachability          : 2001:0:49:338::/64 Metric: 40 Type: 1 Up
      Reachability          : 2001:0:58:310::/64 Metric: 20 Type: 1 Up
      Reachability          : 2001:0:307:353::/64 Metric: 10 Type: 1 Up
      Reachability          : 2001:0:310:353::/64 Metric: 10 Type: 1 Up
      Reachability          : 2002::/72 Metric: 10 Type: 1 Up
      Reachability          : 2002::353/128 Metric: 10 Type: 1 Up
      Reachability          : fcbb:0:419::/48 Metric: 40 Type: 1 Up
      Reachability          : fcbb:0:1000::/36 Metric: 10 Type: 1 Up
      Reachability          : fcbb:0:1353::/48 Metric: 1 Type: 1 Up
      Reachability          : fcbb:0:9310::/48 Metric: 10 Type: 1 Up
      Reachability          : fcbb:1:1000::/36 Metric: 1 Type: 1 Up
      Reachability          : 2001:0:29:58::/64 Metric: 30 Type: 1 Up
      Reachability          : 2001:0:36:58::/64 Metric: 30 Type: 1 Up
      Reachability          : 2001:0:49:199::/64 Metric: 30 Type: 1 Up
      Reachability          : 2001:0:58:419::/64 Metric: 30 Type: 1 Up
      Reachability          : 2001:0:199:302::/64 Metric: 20 Type: 1 Up
      Reachability          : 2001:0:199:344::/64 Metric: 30 Type: 1 Up
      Reachability          : 2001:0:302:353::/64 Metric: 10 Type: 1 Up
      Reachability          : 2001:25:110:225::/64 Metric: 20 Type: 1 Up
      SRv6 Locator: fcbb:0:419::/48 Topology: 0
        Metric: 40 Algorithm: 0 Flags: []
      SRv6 Locator: fcbb:0:1000::/36 Topology: 0
        Metric: 10 Algorithm: 0 Flags: []
      SRv6 Locator: fcbb:0:1353::/48 Topology: 0
        Metric: 1 Algorithm: 0 Flags: []
        SRv6 SID End with NEXT-CSID PSP USD
          SID : fcbb:0:1353::
          SID structure: Block length: 32 Node length: 16
                         Function length: 0 Argument length: 80
      SRv6 Locator: fcbb:0:9310::/48 Topology: 0
        Metric: 10 Algorithm: 0 Flags: []
      SRv6 Locator: fcbb:1:1000::/36 Topology: 0
        Metric: 1 Algorithm: 0 Flags: []
      SRv6 Locator: fcbb:1:1353::/48 Topology: 0
        Metric: 1 Algorithm: 128 Flags: []
        SRv6 SID End with NEXT-CSID PSP USD
          SID : fcbb:1:1353::
          SID structure: Block length: 32 Node length: 16
                         Function length: 0 Argument length: 80
      Router Capabilities: Router Id: 0.0.0.0 Flags: []
        SRv6 Capability: Flags: []
        Algorithms:  0, 1, 128
        Flex Algo: Algorithm: 128 Metric: Min Unidirectional Delay Metric (1) Calc: SPF (0) Prio: 128
      Unsupported TLV: Type: 14 Length: 2
    evpn-rr-58.00-00            254  22859  1185    178 L2  0000.0000.0358.00-00  <>
      Remaining lifetime received: 1199 s Modified to: 1200 s
      NLPID: 0xCC(IPv4)
      Hostname: evpn-rr-58
      Area addresses: 49.0001
      Interface address: 100.0.3.58
      IS Neighbor          : Spine2-J-180.00     Metric: 10
        IPv4 Neighbor Address: 30.58.180.180
        IPv4 Interface Address: 30.58.180.58
        Adj-sid: 24001 flags: [L V] weight: 0x0
      Reachability         : 30.58.180.0/24 Metric: 10 Type: 1 Up
      Reachability         : 100.0.3.58/32 Metric: 10 Type: 1 Up
        SR Prefix-SID: 358 Flags: [N] Algorithm: 0
      Router Capabilities: Router Id: 100.0.3.58 Flags: []
        SR Local Block:
          SRLB Base: 15000 Range: 1000
        Maximum SID depth:
          Base MPLS imposition (MSD type 1):  10
        SR Capability: Flags: [I]
          SRGB Base: 16000 Range: 8000
        Algorithms:  0, 1
      Unsupported TLV: Type: 14 Length: 2
    evpn-rr2-60.00-00           253  30995  1153    179 L2  0000.0000.0360.00-00  <>
      Remaining lifetime received: 1199 s Modified to: 1200 s
      NLPID: 0xCC(IPv4)
      Hostname: evpn-rr2-60
      Area addresses: 49.0001
      Interface address: 100.0.3.60
      IS Neighbor          : Spine2-J-180.00     Metric: 10
        IPv4 Neighbor Address: 30.60.180.180
        IPv4 Interface Address: 30.60.180.60
        Adj-sid: 24001 flags: [L V] weight: 0x0
      Reachability         : 30.60.180.0/24 Metric: 10 Type: 1 Up
      Reachability         : 100.0.3.60/32 Metric: 10 Type: 1 Up
        SR Prefix-SID: 360 Flags: [N] Algorithm: 0
      Router Capabilities: Router Id: 100.0.3.60 Flags: []
        SR Local Block:
          SRLB Base: 15000 Range: 1000
        Maximum SID depth:
          Base MPLS imposition (MSD type 1):  10
        SR Capability: Flags: [I]
          SRGB Base: 16000 Range: 8000
        Algorithms:  0, 1
      Unsupported TLV: Type: 14 Length: 2
    Ribbon_31.00-00             246  12442   594     79 L2  0001.0000.0031.00-00  <>
      Remaining lifetime received: 1199 s Modified to: 1200 s
      NLPID: 0xCC(IPv4)
      Area addresses: 49.0001
      Router Capabilities: Router Id: 100.0.0.31 Flags: []
        SR Local Block:
          SRLB Base: 16 Range: 15344
        Maximum SID depth:
          Base MPLS imposition (MSD type 1):  10
        SR Capability: Flags: [I]
          SRGB Base: 20000 Range: 2000
      Unsupported TLV: Type: 14 Length: 2
    Ribbon_31.00-01             246  38790  1084     38 L2  0001.0000.0031.00-01  <>
      Remaining lifetime received: 1199 s Modified to: 1200 s
      Hostname: Ribbon_31
    Ribbon_31.00-02             248  33074   331    108 L2  0001.0000.0031.00-02  <>
      Remaining lifetime received: 1199 s Modified to: 1200 s
      Interface address: 100.0.0.31
      Interface address: 20.31.180.31
      IS Neighbor          : Spine2-J-180.00     Metric: 10
        IPv4 Neighbor Address: 20.31.180.180
        IPv4 Interface Address: 20.31.180.31
        Adj-sid: 756642 flags: [L V] weight: 0x0
        Adj-sid: 756643 flags: [L V B] weight: 0x0
      Reachability         : 100.0.0.31/32 Metric: 0 Type: 1 Up
        SR Prefix-SID: 31 Flags: [N] Algorithm: 0
      Reachability         : 20.31.180.0/24 Metric: 10 Type: 1 Up
    Spine2-J-180.00-00          494   1166   464    830 L2  0001.0001.0180.00-00  <>
      Remaining lifetime received: 1199 s Modified to: 1200 s
      NLPID: 0xCC(IPv4)
      Hostname: Spine2-J-180
      Area addresses: 49.0001
      Interface address: 20.180.183.180
      Interface address: 20.21.180.180
      Interface address: 20.34.180.180
      Interface address: 20.161.180.180
      Interface address: 30.79.180.180
      Interface address: 20.180.182.180
      Interface address: 20.180.181.180
      Interface address: 20.3.180.180
      Interface address: 20.180.184.180
      Interface address: 30.41.180.180
      Interface address: 20.31.180.180
      Interface address: 30.9.180.180
      Interface address: 20.56.180.180
      Interface address: 20.26.180.180
      Interface address: 30.14.180.180
      Interface address: 30.45.180.180
      Interface address: 30.60.180.180
      Interface address: 30.58.180.180
      IS Neighbor          : 0000.0000.0021.00   Metric: 10
        IPv4 Neighbor Address: 20.21.180.21
        IPv4 Interface Address: 20.21.180.180
        Adj-sid: 100009 flags: [L V] weight: 0x0
      IS Neighbor          : Huawei-34.00        Metric: 10
        IPv4 Neighbor Address: 20.34.180.34
        IPv4 Interface Address: 20.34.180.180
        Adj-sid: 100018 flags: [L V] weight: 0x0
      IS Neighbor          : juniper_379_MX304-evpn-mpls.00 Metric: 10
        IPv4 Neighbor Address: 30.79.180.79
        IPv4 Interface Address: 30.79.180.180
        Adj-sid: 100008 flags: [L V] weight: 0x0
      IS Neighbor          : PE21-J2-181.00      Metric: 10
        IPv4 Neighbor Address: 20.180.181.181
        IPv4 Interface Address: 20.180.181.180
        Adj-sid: 100000 flags: [L V] weight: 0x0
      IS Neighbor          : CIEN-5169-3.00      Metric: 10
        IPv4 Neighbor Address: 20.3.180.3
        IPv4 Interface Address: 20.3.180.180
        Adj-sid: 100001 flags: [L V] weight: 0x0
      IS Neighbor          : Ribbon_31.00        Metric: 10
        IPv4 Neighbor Address: 20.31.180.31
        IPv4 Interface Address: 20.31.180.180
        Adj-sid: 100019 flags: [L V] weight: 0x0
      IS Neighbor          : juniper-309-acx7332.00 Metric: 10
        IPv4 Neighbor Address: 30.9.180.9
        IPv4 Interface Address: 30.9.180.180
        Adj-sid: 100017 flags: [L V] weight: 0x0
      IS Neighbor          : SR1-EVPN.00         Metric: 10
        IPv4 Neighbor Address: 20.56.180.56
        IPv4 Interface Address: 20.56.180.180
        Adj-sid: 100016 flags: [L V] weight: 0x0
      IS Neighbor          : PE23-J2-183.00      Metric: 10
        IPv4 Neighbor Address: 20.180.183.183
        IPv4 Interface Address: 20.180.183.180
        Adj-sid: 100005 flags: [L V] weight: 0x0
      IS Neighbor          : anet-161-R3.00      Metric: 10
        IPv4 Neighbor Address: 20.161.180.161
        IPv4 Interface Address: 20.161.180.180
        Adj-sid: 100020 flags: [L V] weight: 0x0
      IS Neighbor          : PE32-J2-172.00      Metric: 10
        IPv4 Neighbor Address: 20.180.182.182
        IPv4 Interface Address: 20.180.182.180
        Adj-sid: 100004 flags: [L V] weight: 0x0
      IS Neighbor          : PE24-J2-184.00      Metric: 10
        IPv4 Neighbor Address: 20.180.184.184
        IPv4 Interface Address: 20.180.184.180
        Adj-sid: 100006 flags: [L V] weight: 0x0
      IS Neighbor          : h41-9902.00         Metric: 10
        IPv4 Neighbor Address: 30.41.180.41
        IPv4 Interface Address: 30.41.180.180
        Adj-sid: 100013 flags: [L V] weight: 0x0
      IS Neighbor          : evpn-rr2-60.00      Metric: 10
        IPv4 Neighbor Address: 30.60.180.60
        IPv4 Interface Address: 30.60.180.180
        Adj-sid: 100015 flags: [L V] weight: 0x0
      IS Neighbor          : evpn-rr-58.00       Metric: 10
        IPv4 Neighbor Address: 30.58.180.58
        IPv4 Interface Address: 30.58.180.180
        Adj-sid: 100014 flags: [L V] weight: 0x0
      IS Neighbor          : h3c_26_S12500R-2L.00 Metric: 10
        IPv4 Neighbor Address: 20.26.180.26
        IPv4 Interface Address: 20.26.180.180
        Adj-sid: 100010 flags: [L V] weight: 0x0
      IS Neighbor          : h45-N57C1.00        Metric: 10
        IPv4 Neighbor Address: 30.45.180.45
        IPv4 Interface Address: 30.45.180.180
        Adj-sid: 100002 flags: [L V] weight: 0x0
      Reachability         : 100.0.0.180/32 Metric: 0 Type: 1 Up
      Reachability         : 20.180.183.0/24 Metric: 10 Type: 1 Up
      Reachability         : 20.21.180.0/24 Metric: 10 Type: 1 Up
      Reachability         : 20.34.180.0/24 Metric: 10 Type: 1 Up
      Reachability         : 20.161.180.0/24 Metric: 10 Type: 1 Up
      Reachability         : 30.79.180.0/24 Metric: 10 Type: 1 Up
      Reachability         : 20.180.182.0/24 Metric: 10 Type: 1 Up
      Reachability         : 20.180.181.0/24 Metric: 10 Type: 1 Up
      Reachability         : 20.3.180.0/24 Metric: 10 Type: 1 Up
      Reachability         : 20.180.184.0/24 Metric: 10 Type: 1 Up
      Reachability         : 30.41.180.0/24 Metric: 10 Type: 1 Up
      Reachability         : 20.31.180.0/24 Metric: 10 Type: 1 Up
      Reachability         : 30.9.180.0/24 Metric: 10 Type: 1 Up
      Reachability         : 20.56.180.0/24 Metric: 10 Type: 1 Up
      Reachability         : 20.26.180.0/24 Metric: 10 Type: 1 Up
      Reachability         : 30.14.180.0/24 Metric: 10 Type: 1 Up
      Reachability         : 30.45.180.0/24 Metric: 10 Type: 1 Up
      Reachability         : 30.60.180.0/24 Metric: 10 Type: 1 Up
      Reachability         : 30.58.180.0/24 Metric: 10 Type: 1 Up
      Router Capabilities: Router Id: 100.0.0.180 Flags: []
        SR Local Block:
          SRLB Base: 965536 Range: 65536
        Area leader priority: 250 algorithm: 0
        SR Capability: Flags: [I]
          SRGB Base: 900000 Range: 65536
    PE21-J2-181.00-00           251  28400  1152    156 L2  0001.0001.0181.00-00  <>
      Remaining lifetime received: 1199 s Modified to: 1200 s
      NLPID: 0xCC(IPv4)
      Hostname: PE21-J2-181
      Area addresses: 49.0001
      Interface address: 20.180.181.181
      Interface address: 100.0.0.181
      IS Neighbor          : Spine2-J-180.00     Metric: 10
        IPv4 Neighbor Address: 20.180.181.180
        IPv4 Interface Address: 20.180.181.181
        Adj-sid: 100000 flags: [L V] weight: 0x0
      Reachability         : 20.180.181.0/24 Metric: 10 Type: 1 Up
      Reachability         : 100.0.0.181/32 Metric: 10 Type: 1 Up
        SR Prefix-SID: 181 Flags: [N] Algorithm: 0
      Router Capabilities: Router Id: 100.0.0.201 Flags: []
        SR Local Block:
          SRLB Base: 965536 Range: 65536
        Area leader priority: 250 algorithm: 0
        Maximum SID depth:
          Base MPLS imposition (MSD type 1):  6
        SR Capability: Flags: [I]
          SRGB Base: 900000 Range: 65536
    PE32-J2-172.00-00           262  36799   494    183 L2  0001.0001.0182.00-00  <>
      LSP generation remaining wait time: 0 ms
      Time remaining until refresh: 194 s
      NLPID: 0xCC(IPv4)
      Hostname: PE32-J2-172
      Area addresses: 49.0001
      Interface address: 100.0.0.182
      Interface address: 20.180.182.182
      IS Neighbor          : Spine2-J-180.00     Metric: 10
        IPv4 Neighbor Address: 20.180.182.180
        IPv4 Interface Address: 20.180.182.182
        Adj-sid: 362144 flags: [L V] weight: 0x0
      Reachability         : 20.170.172.0/24 Metric: 0 Type: 1 Up
      Reachability         : 20.149.172.0/24 Metric: 0 Type: 1 Up
      Reachability         : 209.209.209.209/32 Metric: 0 Type: 1 Up
      Reachability         : 100.0.0.182/32 Metric: 10 Type: 1 Up
        SR Prefix-SID: 182 Flags: [N] Algorithm: 0
      Reachability         : 20.180.182.0/24 Metric: 10 Type: 1 Up
      Router Capabilities: Router Id: 209.209.209.209 Flags: []
        SR Local Block:
          SRLB Base: 965536 Range: 65536
        Area leader priority: 250 algorithm: 0
        Maximum SID depth:
          Base MPLS imposition (MSD type 1):  12
        SR Capability: Flags: [I]
          SRGB Base: 20000 Range: 2000
    PE23-J2-183.00-00           274  26080   564    156 L2  0001.0001.0183.00-00  <>
      Remaining lifetime received: 1199 s Modified to: 1200 s
      NLPID: 0xCC(IPv4)
      Hostname: PE23-J2-183
      Area addresses: 49.0001
      Interface address: 20.180.183.183
      Interface address: 100.0.0.183
      IS Neighbor          : Spine2-J-180.00     Metric: 10
        IPv4 Neighbor Address: 20.180.183.180
        IPv4 Interface Address: 20.180.183.183
        Adj-sid: 100000 flags: [L V] weight: 0x0
      Reachability         : 20.180.183.0/24 Metric: 10 Type: 1 Up
      Reachability         : 100.0.0.183/32 Metric: 0 Type: 1 Up
        SR Prefix-SID: 183 Flags: [N] Algorithm: 0
      Router Capabilities: Router Id: 100.0.0.183 Flags: []
        SR Local Block:
          SRLB Base: 965536 Range: 65536
        Area leader priority: 250 algorithm: 0
        Maximum SID depth:
          Base MPLS imposition (MSD type 1):  12
        SR Capability: Flags: [I]
          SRGB Base: 900000 Range: 65536
    PE24-J2-184.00-00           254  48017   599    156 L2  0001.0001.0184.00-00  <>
      Remaining lifetime received: 1199 s Modified to: 1200 s
      NLPID: 0xCC(IPv4)
      Hostname: PE24-J2-184
      Area addresses: 49.0001
      Interface address: 20.180.184.184
      Interface address: 100.0.0.184
      IS Neighbor          : Spine2-J-180.00     Metric: 10
        IPv4 Neighbor Address: 20.180.184.180
        IPv4 Interface Address: 20.180.184.184
        Adj-sid: 100000 flags: [L V] weight: 0x0
      Reachability         : 20.180.184.0/24 Metric: 10 Type: 1 Up
      Reachability         : 100.0.0.184/32 Metric: 0 Type: 1 Up
        SR Prefix-SID: 184 Flags: [N] Algorithm: 0
      Router Capabilities: Router Id: 100.0.0.184 Flags: []
        SR Local Block:
          SRLB Base: 965536 Range: 65536
        Area leader priority: 250 algorithm: 0
        Maximum SID depth:
          Base MPLS imposition (MSD type 1):  12
        SR Capability: Flags: [I]
          SRGB Base: 900000 Range: 65536
    Nokia_58-SR1-3-SRv6.00-00      1479  59869 64986    581 L2  0100.0000.0058.00-00  <>
      NLPID: 0xCC(IPv4) 0x8E(IPv6)
      Hostname: Nokia_58-SR1-3-SRv6
      Area addresses:
        49.0000
        49.0001
      Interface address: 10.0.0.58
      Interface address: 2001:0:36:58::58
      Interface address: 2001:0:58:310::58
      Interface address: 2001:0:58:419::58
      Interface address: 2002::58
      IS Neighbor          : huawei_36.00        Metric: 10
        IPv6 Neighbor Address: 2001:0:36:58::36
        Global IPv6 Interface Address: 2001:0:36:58::58
      Reachability         : 10.0.0.58/32 Metric: 0 Type: 1 Up
      Reachability          : 2001:0:29:58::/64 Metric: 10 Type: 1 Up
      Reachability          : 2001:0:36:58::/64 Metric: 10 Type: 1 Up
      Reachability          : 2001:0:58:310::/64 Metric: 10 Type: 1 Up
      Reachability          : 2001:0:58:419::/64 Metric: 10 Type: 1 Up
      Reachability          : 2001:0:199:344::/64 Metric: 50 Type: 1 Up
      Reachability          : 2002::58/128 Metric: 0 Type: 1 Up
      Reachability          : 2002::199/128 Metric: 40 Type: 1 Up
      Reachability          : 2002::338/128 Metric: 30 Type: 1 Up
      Reachability          : 2002::344/128 Metric: 60 Type: 1 Up
      Reachability          : fcbb:0:1000::/36 Metric: 0 Type: 1 Up
      SRv6 Locator: fcbb:0:1000::/36 Topology: 0
        Metric: 0 Algorithm: 0 Flags: []
      Router Capabilities: Router Id: 10.0.0.58 Flags: []
        Maximum SID depth:
          Base MPLS imposition (MSD type 1):  0
        SRv6 Capability: Flags: []
        Algorithms:  0, 128
    Nokia_58-SR1-3-SRv6.00-01      4355  32473 65193   1254 L2  0100.0000.0058.00-01  <>
      IS Neighbor          : JNPR-310-ACX7100-48L.00 Metric: 10
        IPv6 Neighbor Address: 2001:0:58:310::310
        Global IPv6 Interface Address: 2001:0:58:310::58
      IS Neighbor          : Keys-Ixia-419.00    Metric: 10
        IPv6 Neighbor Address: 2001:0:58:419::419
        Global IPv6 Interface Address: 2001:0:58:419::58
      Reachability          : 2001:0:11:310::/64 Metric: 20 Type: 1 Up
      Reachability          : 2001:0:11:353::/64 Metric: 30 Type: 1 Up
      Reachability          : 2001:0:29:338::/64 Metric: 20 Type: 1 Up
      Reachability          : 2001:0:49:199::/64 Metric: 40 Type: 1 Up
      Reachability          : 2001:0:49:338::/64 Metric: 30 Type: 1 Up
      Reachability          : 2001:0:199:302::/64 Metric: 40 Type: 1 Up
      Reachability          : 2001:0:302:353::/64 Metric: 30 Type: 1 Up
      Reachability          : 2001:0:310:353::/64 Metric: 20 Type: 1 Up
      Reachability          : 2001:25:110:225::/64 Metric: 20 Type: 1 Up
      Reachability          : 2002::/71 Metric: 20 Type: 1 Up
      Reachability          : 2002::11/128 Metric: 20 Type: 1 Up
      Reachability          : 2002::29/128 Metric: 10 Type: 1 Up
      Reachability          : 2002::49/128 Metric: 40 Type: 1 Up
      Reachability          : 2002::302/128 Metric: 30 Type: 1 Up
      Reachability          : 2002::310/128 Metric: 10 Type: 1 Up
      Reachability          : 2002::353/128 Metric: 30 Type: 1 Up
      Reachability          : 2002::419/128 Metric: 20 Type: 1 Up
      Reachability          : fcbb:0:419::/48 Metric: 10 Type: 1 Up
      Reachability          : fcbb:0:9310::/48 Metric: 10 Type: 1 Up
      SRv6 Locator: fcbb:0:419::/48 Topology: 0
        Metric: 10 Algorithm: 0 Flags: []
        SRv6 SID End with NEXT-CSID PSP USD
          SID : fcbb:0:419:11::
          SID structure: Block length: 32 Node length: 16
                         Function length: 0 Argument length: 80
      SRv6 Locator: fcbb:0:9310::/48 Topology: 0
        Metric: 10 Algorithm: 0 Flags: []
        SRv6 SID End with NEXT-CSID PSP USP USD
          SID : fcbb:0:9310::
          SID structure: Block length: 32 Node length: 16
                         Function length: 0 Argument length: 80
      SRv6 Locator: fcbb:1:1011::/48 Topology: 0
        Metric: 77 Algorithm: 128 Flags: []
        SRv6 SID End with NEXT-CSID PSP USD
          SID : fcbb:1:1011::
          SID structure: Block length: 32 Node length: 16
                         Function length: 16 Argument length: 0
      SRv6 Locator: fcbb:1:1029::/48 Topology: 0
        Metric: 100 Algorithm: 128 Flags: []
        SRv6 SID End with NEXT-CSID PSP USD
          SID : fcbb:1:1029::
          SID structure: Block length: 32 Node length: 16
                         Function length: 0 Argument length: 0
      SRv6 Locator: fcbb:1:1058::/48 Topology: 0
        Metric: 0 Algorithm: 128 Flags: []
        SRv6 SID End with NEXT-CSID PSP USD
          SID : fcbb:1:1058::
          SID structure: Block length: 32 Node length: 16
                         Function length: 0 Argument length: 80
      SRv6 Locator: fcbb:1:1199::/48 Topology: 0
        Metric: 10606 Algorithm: 128 Flags: []
        SRv6 SID End with NEXT-CSID PSP USD
          SID : fcbb:1:1199::
          SID structure: Block length: 32 Node length: 16
                         Function length: 0 Argument length: 80
        SRv6 SID Un Supported
          SID : fcbb:1:1199:e001::
          SID structure: Block length: 32 Node length: 16
                         Function length: 16 Argument length: 64
        SRv6 SID End
          SID : fcbb:1:1199:e002::
          SID structure: Block length: 32 Node length: 16
                         Function length: 16 Argument length: 0
        SRv6 SID End with PSP
          SID : fcbb:1:1199:e003::
          SID structure: Block length: 32 Node length: 16
                         Function length: 16 Argument length: 0
        SRv6 SID End with PSP USP USD
          SID : fcbb:1:1199:e004::
          SID structure: Block length: 32 Node length: 16
                         Function length: 16 Argument length: 0
      SRv6 Locator: fcbb:1:1302::/48 Topology: 0
        Metric: 607 Algorithm: 128 Flags: []
        SRv6 SID End with NEXT-CSID PSP USP USD
          SID : fcbb:1:1302::
          SID structure: Block length: 32 Node length: 16
                         Function length: 0 Argument length: 80
      SRv6 Locator: fcbb:1:1310::/48 Topology: 0
        Metric: 54 Algorithm: 128 Flags: []
      SRv6 Locator: fcbb:1:1344::/48 Topology: 0
        Metric: 20606 Algorithm: 128 Flags: []
        SRv6 SID End with NEXT-CSID PSP USD
          SID : fcbb:1:1344::
          SID structure: Block length: 32 Node length: 16
                         Function length: 0 Argument length: 80
      SRv6 Locator: fcbb:1:1353::/48 Topology: 0
        Metric: 558 Algorithm: 128 Flags: []
        SRv6 SID End with NEXT-CSID PSP USD
          SID : fcbb:1:1353::
          SID structure: Block length: 32 Node length: 16
                         Function length: 0 Argument length: 80
    Nokia-59-IXRe2.00-00        420  39618   643    689 L2  0100.0000.0059.00-00  <>
      Remaining lifetime received: 1199 s Modified to: 1200 s
      NLPID: 0xCC(IPv4) 0x8E(IPv6)
      Hostname: Nokia-59-IXRe2
      Area addresses: 49.0000.0000.0059.00
      Interface address: 10.0.0.59
      Interface address: 2001:0:59:161::59
      Interface address: 2001:0:59:352::59
      Interface address: 2002::59
      IS Neighbor          : Cisco352-N540.00    Metric: 10
        IPv6 Neighbor Address: 2001:0:59:352::352
        Global IPv6 Interface Address: 2001:0:59:352::59
        Adj-sid: 1048573 flags: [L V B F] weight: 0x0
      Reachability         : 10.0.0.59/32 Metric: 0 Type: 1 Up
        SR Prefix-SID: 59 Flags: [N P] Algorithm: 0
      Reachability          : 2001:0:59:161::/64 Metric: 10 Type: 1 Up
      Reachability          : 2001:0:59:352::/64 Metric: 10 Type: 1 Up
      Reachability          : 2002::59/128 Metric: 0 Type: 1 Up
        SR Prefix-SID: 159 Flags: [N P] Algorithm: 0
      Reachability          : fcbb:0:59::/48 Metric: 0 Type: 1 Up
      Reachability          : fcbb:3:59::/48 Metric: 0 Type: 1 Up
      Reachability          : fcbb:4:59::/48 Metric: 0 Type: 1 Up
      SRv6 Locator: fcbb:0:59::/48 Topology: 0
        Metric: 0 Algorithm: 0 Flags: []
        SRv6 SID End with NEXT-CSID PSP USD
          SID : fcbb:0:59::
          SID structure: Block length: 32 Node length: 16
                         Function length: 0 Argument length: 80
      SRv6 Locator: fcbb:1:59::/48 Topology: 0
        Metric: 0 Algorithm: 128 Flags: []
        SRv6 SID End with NEXT-CSID PSP USD
          SID : fcbb:1:59::
          SID structure: Block length: 32 Node length: 16
                         Function length: 0 Argument length: 80
      SRv6 Locator: fcbb:3:59::/48 Topology: 0
        Metric: 0 Algorithm: 0 Flags: []
        SRv6 SID End with NEXT-CSID PSP USD
          SID : fcbb:3:59::
          SID structure: Block length: 32 Node length: 16
                         Function length: 0 Argument length: 80
      SRv6 Locator: fcbb:4:59::/48 Topology: 0
        Metric: 0 Algorithm: 0 Flags: []
        SRv6 SID End with NEXT-CSID PSP USD
          SID : fcbb:4:59::
          SID structure: Block length: 32 Node length: 16
                         Function length: 0 Argument length: 80
      Router Capabilities: Router Id: 10.0.0.59 Flags: []
        Maximum SID depth:
          Base MPLS imposition (MSD type 1):  9
        SRv6 Capability: Flags: []
        SR Capability: Flags: [I V]
          SRGB Base: 20000 Range: 2000
        Algorithms:  0, 128, 129, 130, 131
    SR1-EVPN.00-00              328  37311   896    198 L2  1000.0000.0056.00-00  <>
      Remaining lifetime received: 1199 s Modified to: 1200 s
      NLPID: 0xCC(IPv4) 0x8E(IPv6)
      Hostname: SR1-EVPN
      Area addresses: 49.0001
      Interface address: 20.56.180.56
      Interface address: 100.0.0.56
      Interface address: 2001::56
      IS Neighbor          : Spine2-J-180.00     Metric: 10
        IPv4 Neighbor Address: 20.56.180.180
        IPv4 Interface Address: 20.56.180.56
        Adj-sid: 524271 flags: [L V B] weight: 0x0
      Reachability         : 20.56.180.0/24 Metric: 10 Type: 1 Up
      Reachability         : 100.0.0.56/32 Metric: 0 Type: 1 Up
        SR Prefix-SID: 56 Flags: [N P] Algorithm: 0
      Reachability          : 2001::56/128 Metric: 0 Type: 1 Up
      Router Capabilities: Router Id: 100.0.0.56 Flags: []
        Maximum SID depth:
          Base MPLS imposition (MSD type 1):  12
        SR Capability: Flags: [I V]
          SRGB Base: 20000 Range: 2000
        Algorithms:  0
    juniper-309-acx7332.00-00       255  23065  1136    180 L2  1000.0003.0009.00-00  <>
      Remaining lifetime received: 1199 s Modified to: 1200 s
      NLPID: 0xCC(IPv4) 0x8E(IPv6)
      Hostname: juniper-309-acx7332
      Area addresses: 49.0001.0000.0000
      Interface address: 100.0.30.9
      IS Neighbor          : Spine2-J-180.00     Metric: 10
        IPv4 Neighbor Address: 30.9.180.180
        IPv4 Interface Address: 30.9.180.9
        Adj-sid: 33 flags: [L V] weight: 0x0
      Reachability         : 100.0.30.9/32 Metric: 0 Type: 1 Up
        SR Prefix-SID: 309 Flags: [N] Algorithm: 0
      Reachability         : 30.9.180.0/24 Metric: 10 Type: 1 Up
      Router Capabilities: Router Id: 100.0.30.9 Flags: []
        Maximum SID depth:
          Base MPLS imposition (MSD type 1):  3
        SR Capability: Flags: [I V]
          SRGB Base: 20000 Range: 2000
        Algorithms:  0, 1
      Unsupported TLV: Type: 14 Length: 2
    juniper_379_MX304-evpn-mpls.00-00       277  61772  1060    188 L2  1000.0003.7009.00-00  <>
      Remaining lifetime received: 1199 s Modified to: 1200 s
      NLPID: 0xCC(IPv4) 0x8E(IPv6)
      Hostname: juniper_379_MX304-evpn-mpls
      Area addresses: 49.0001.0000.0000
      Interface address: 100.0.37.9
      IS Neighbor          : Spine2-J-180.00     Metric: 10
        IPv4 Neighbor Address: 30.79.180.180
        IPv4 Interface Address: 30.79.180.79
        Adj-sid: 204 flags: [L V] weight: 0x0
      Reachability         : 30.79.180.0/24 Metric: 10 Type: 1 Up
      Reachability         : 100.0.37.9/32 Metric: 0 Type: 1 Up
        SR Prefix-SID: 379 Flags: [N] Algorithm: 0
      Router Capabilities: Router Id: 100.0.37.9 Flags: []
        Maximum SID depth:
          Base MPLS imposition (MSD type 1):  0
        SR Capability: Flags: [I V]
          SRGB Base: 20000 Range: 2000
        Algorithms:  0, 1
      Unsupported TLV: Type: 14 Length: 2
    Keys-Ixia-419.00-00         489   1396   669    315 L2  3800.0000.0419.00-00  <DefaultAtt>
      Remaining lifetime received: 1199 s Modified to: 1200 s
      NLPID: 0xCC(IPv4) 0x8E(IPv6) 0x81(CLNP)
      Hostname: Keys-Ixia-419
      Area addresses: 49.0001
      Interface address: 2001:0:58:419::419
      IS Neighbor          : Nokia_58-SR1-3-SRv6.00 Metric: 10
      Reachability          : 2002::419/128 Metric: 10 Type: 1 Up
      Reachability          : fcbb:0:419::/48 Metric: 10 Type: 1 Up
      Reachability          : 2001:0:58:419::/64 Metric: 10 Type: 1 Up
      SRv6 Locator: fcbb:0:419::/48 Topology: 0
        Metric: 0 Algorithm: 0 Flags: []
        SRv6 SID End with NEXT-CSID PSP USD
          SID : fcbb:0:419:11::
          SID structure: Block length: 32 Node length: 16
                         Function length: 0 Argument length: 80
      Router Capabilities: Router Id: 10.0.1.119 Flags: []
        SRv6 Capability: Flags: []
        Algorithms:  0
```

## show isis database traffic-engineering

```text
Legend:
H - hostname conflict
U - node unreachable

IS-IS Instance: sr_eantc VRF: default
  IS-IS Level 2 Link State Database
    LSPID                   Seq Num  Cksum  Life Length IS  Received LSPID        Flags
    CIEN-5169-3.00-00            28  33567 52245    203 L2  0000.0000.0003.00-00  <>
      NLPID: 0xCC(IPv4)
      Hostname: CIEN-5169-3
      TE IPv4 router ID: 100.0.0.3
      Area addresses: 49.0001
      Interface address: 100.0.0.3
      IS Neighbor          : Spine2-J-180.00     Metric: 10
        IPv4 Neighbor Address: 20.3.180.180
        IPv4 Interface Address: 20.3.180.3
        Adj-sid: 16000 flags: [L V] weight: 0x0
        Maximum link BW: 10.00 Gbps
        Maximum reservable link BW: 10.00 Gbps
        Unreserved BW:
            TE class 0: 10.00 Gbps	TE class 1: 10.00 Gbps	TE class 2: 10.00 Gbps
            TE class 3: 10.00 Gbps	TE class 4: 10.00 Gbps	TE class 5: 10.00 Gbps
            TE class 6: 10.00 Gbps	TE class 7: 10.00 Gbps
        Application Specific Link Attributes:
          Standard applications: [L] RSVP-TE SR-TE LFA Flex-Algo
      Reachability         : 20.3.180.0/24 Metric: 10 Type: 1 Up
      Reachability         : 100.0.0.3/32 Metric: 10 Type: 1 Up
        SR Prefix-SID: 3 Flags: [N] Algorithm: 0
      Router Capabilities: Router Id: 100.0.0.3 Flags: []
        SR Capability: Flags: [I]
          SRGB Base: 20000 Range: 2000
        Algorithms:  0
    h3c_20_CR16010E-F.00-00      4355  52849  1183   1389 L2  0000.0000.0020.00-00  <>
      Remaining lifetime received: 1199 s Modified to: 1200 s
      NLPID: 0xCC(IPv4) 0x8E(IPv6)
      Hostname: h3c_20_CR16010E-F
      TE IPv6 router ID: 2002::20
      Area addresses: 49.0000
      Interface address: 2001:0:20:36::20
      Interface address: 2001:0:20:336::20
      Interface address: 2001:0:20:352::20
      Interface address: 2002::20
      IS Neighbor          : huawei_36.00        Metric: 10
        IPv6 Neighbor Address: 2001:0:20:36::36
        Global IPv6 Interface Address: 2001:0:20:36::20
        Min/Max unidirectional link delay: 9999/9999 us
      IS Neighbor          : huawei_36.00        Metric: 10
        IPv6 Neighbor Address: 2001:0:20:36::36
        Global IPv6 Interface Address: 2001:0:20:36::20
        TE default metric: 11
        Maximum link BW: 0.00 bps
        Maximum reservable link BW: 0.00 bps
        Unreserved BW:
            TE class 0: 0.00 bps	TE class 1: 0.00 bps	TE class 2: 0.00 bps
            TE class 3: 0.00 bps	TE class 4: 0.00 bps	TE class 5: 0.00 bps
            TE class 6: 0.00 bps	TE class 7: 0.00 bps
      IS Neighbor          : ZTE_336_ZXR10_M6000-8SE.00 Metric: 10
        IPv6 Neighbor Address: 2001:0:20:336::336
        Global IPv6 Interface Address: 2001:0:20:336::20
        TE default metric: 11
        Maximum link BW: 0.00 bps
        Maximum reservable link BW: 0.00 bps
        Unreserved BW:
            TE class 0: 0.00 bps	TE class 1: 0.00 bps	TE class 2: 0.00 bps
            TE class 3: 0.00 bps	TE class 4: 0.00 bps	TE class 5: 0.00 bps
            TE class 6: 0.00 bps	TE class 7: 0.00 bps
      IS Neighbor          : Cisco352-N540.00    Metric: 10
        IPv6 Neighbor Address: 2001:0:20:352::352
        Global IPv6 Interface Address: 2001:0:20:352::20
        Min/Max unidirectional link delay: 9999/9999 us
      IS Neighbor          : Cisco352-N540.00    Metric: 10
        IPv6 Neighbor Address: 2001:0:20:352::352
        Global IPv6 Interface Address: 2001:0:20:352::20
        TE default metric: 11
        Maximum link BW: 0.00 bps
        Maximum reservable link BW: 0.00 bps
        Unreserved BW:
            TE class 0: 0.00 bps	TE class 1: 0.00 bps	TE class 2: 0.00 bps
            TE class 3: 0.00 bps	TE class 4: 0.00 bps	TE class 5: 0.00 bps
            TE class 6: 0.00 bps	TE class 7: 0.00 bps
      Reachability          : 2001:0:20:36::/64 Metric: 10 Type: 1 Up
      Reachability          : 2001:0:20:336::/64 Metric: 10 Type: 1 Up
      Reachability          : 2001:0:20:352::/64 Metric: 10 Type: 1 Up
      Reachability          : 2002::20/128 Metric: 0 Type: 1 Up
      Reachability          : fcbb:0:20::/48 Metric: 0 Type: 1 Up
      SRv6 Locator: fcbb:0:20::/48 Topology: 0
        Metric: 0 Algorithm: 0 Flags: []
        SRv6 SID End with NEXT-CSID PSP USD
          SID : fcbb:0:20::
          SID structure: Block length: 32 Node length: 16
                         Function length: 0 Argument length: 0
        SRv6 SID End
          SID : fcbb:0:20:e102::
          SID structure: Block length: 32 Node length: 16
                         Function length: 16 Argument length: 0
        SRv6 SID End with PSP USP USD
          SID : fcbb:0:20:e103::
          SID structure: Block length: 32 Node length: 16
                         Function length: 16 Argument length: 0
      SRv6 Locator: fcbb:1:20::/48 Topology: 0
        Metric: 0 Algorithm: 128 Flags: []
        SRv6 SID End with NEXT-CSID PSP USD
          SID : fcbb:1:20::
          SID structure: Block length: 32 Node length: 16
                         Function length: 0 Argument length: 0
        SRv6 SID End
          SID : fcbb:1:20:e102::
          SID structure: Block length: 32 Node length: 16
                         Function length: 16 Argument length: 0
        SRv6 SID End with PSP USP USD
          SID : fcbb:1:20:e103::
          SID structure: Block length: 32 Node length: 16
                         Function length: 16 Argument length: 0
    h3c_20_CR16010E-F.00-01      1921  17284  1182    856 L2  0000.0000.0020.00-01  <>
      Remaining lifetime received: 1199 s Modified to: 1200 s
      IS Neighbor          : huawei_36.00        Metric: 10
        IPv6 Neighbor Address: 2001:0:20:36::36
        Global IPv6 Interface Address: 2001:0:20:36::20
        Application Specific Link Attributes:
          Standard applications: Flex-Algo
          User-defined applications: APP3
            TE default metric: 11
            Maximum link BW: 0.00 bps
            Maximum reservable link BW: 0.00 bps
            Unreserved BW:
                TE class 0: 0.00 bps	TE class 1: 0.00 bps	TE class 2: 0.00 bps
                TE class 3: 0.00 bps	TE class 4: 0.00 bps	TE class 5: 0.00 bps
                TE class 6: 0.00 bps	TE class 7: 0.00 bps
            Min/Max unidirectional link delay: 9999/9999 us
      IS Neighbor          : ZTE_336_ZXR10_M6000-8SE.00 Metric: 10
        IPv6 Neighbor Address: 2001:0:20:336::336
        Global IPv6 Interface Address: 2001:0:20:336::20
        Min/Max unidirectional link delay: 9999/9999 us
      IS Neighbor          : ZTE_336_ZXR10_M6000-8SE.00 Metric: 10
        IPv6 Neighbor Address: 2001:0:20:336::336
        Global IPv6 Interface Address: 2001:0:20:336::20
        Application Specific Link Attributes:
          Standard applications: Flex-Algo
          User-defined applications: APP3
            TE default metric: 11
            Maximum link BW: 0.00 bps
            Maximum reservable link BW: 0.00 bps
            Unreserved BW:
                TE class 0: 0.00 bps	TE class 1: 0.00 bps	TE class 2: 0.00 bps
                TE class 3: 0.00 bps	TE class 4: 0.00 bps	TE class 5: 0.00 bps
                TE class 6: 0.00 bps	TE class 7: 0.00 bps
            Min/Max unidirectional link delay: 9999/9999 us
      IS Neighbor          : Cisco352-N540.00    Metric: 10
        IPv6 Neighbor Address: 2001:0:20:352::352
        Global IPv6 Interface Address: 2001:0:20:352::20
        Application Specific Link Attributes:
          Standard applications: Flex-Algo
          User-defined applications: APP3
            TE default metric: 11
            Maximum link BW: 0.00 bps
            Maximum reservable link BW: 0.00 bps
            Unreserved BW:
                TE class 0: 0.00 bps	TE class 1: 0.00 bps	TE class 2: 0.00 bps
                TE class 3: 0.00 bps	TE class 4: 0.00 bps	TE class 5: 0.00 bps
                TE class 6: 0.00 bps	TE class 7: 0.00 bps
            Min/Max unidirectional link delay: 9999/9999 us
      Router Capabilities: Router Id: 0.0.0.0 Flags: []
        SRv6 Capability: Flags: []
        Algorithms:  0, 128, 129, 130, 131
        Flex Algo: Algorithm: 128 Metric: Min Unidirectional Delay Metric (1) Calc: SPF (0) Prio: 100
          Flags: [M] 0x80
        Flex Algo: Algorithm: 129 Metric: TE Metric (2) Calc: SPF (0) Prio: 100
          Flags: [M] 0x80
        Flex Algo: Algorithm: 130 Metric: IGP Metric (0) Calc: SPF (0) Prio: 100
          Exclude admin groups: 1
          Flags: [M] 0x80
        Flex Algo: Algorithm: 131 Metric: IGP Metric (0) Calc: SPF (0) Prio: 100
          Exclude admin groups: 255
          Flags: [M] 0x80
    0000.0000.0021.00-00        440  44683   669    128 L2  0000.0000.0021.00-00  <>
      Remaining lifetime received: 1199 s Modified to: 1200 s
      NLPID: 0xCC(IPv4) 0x8E(IPv6)
      Area addresses: 49.0001
      Topology: 0 (IPv4)
      Topology: 2 (IPv6)
      Interface address: 20.21.180.21
      Interface address: 100.0.0.21
      IS Neighbor          : Spine2-J-180.00     Metric: 10
      Reachability         : 20.21.180.0/24 Metric: 10 Type: 1 Up
      Reachability         : 100.0.0.21/32 Metric: 0 Type: 1 Up
        SR Prefix-SID: 21 Flags: [N] Algorithm: 0
      Reachability         : 192.168.20.0/23 Metric: 0 Type: 1 Up
      Router Capabilities: Router Id: 100.0.0.21 Flags: []
        Maximum SID depth:
          Base MPLS imposition (MSD type 1):  13
        SR Capability: Flags: [I]
          SRGB Base: 20000 Range: 2000
    h3c_26_S12500R-2L.00-00       290   5387   662    139 L2  0000.0000.0026.00-00  <>
      Remaining lifetime received: 1199 s Modified to: 1200 s
      NLPID: 0xCC(IPv4) 0x8E(IPv6)
      Hostname: h3c_26_S12500R-2L
      Area addresses: 49.0001
      Topology: 0 (IPv4)
      Topology: 2 (IPv6)
      Interface address: 20.26.180.26
      Interface address: 100.0.0.26
      IS Neighbor          : Spine2-J-180.00     Metric: 10
      Reachability         : 20.26.180.0/24 Metric: 10 Type: 1 Up
      Reachability         : 100.0.0.26/32 Metric: 0 Type: 1 Up
        SR Prefix-SID: 26 Flags: [N P] Algorithm: 0
      Router Capabilities: Router Id: 100.0.0.26 Flags: []
        Maximum SID depth:
          Base MPLS imposition (MSD type 1):  10
        SR Capability: Flags: [I]
          SRGB Base: 20000 Range: 2000
    h3c_28_S12500R-2L.00-00      1698  13914  1138    964 L2  0000.0000.0028.00-00  <>
      Remaining lifetime received: 1199 s Modified to: 1200 s
      NLPID: 0xCC(IPv4) 0x8E(IPv6)
      Hostname: h3c_28_S12500R-2L
      TE IPv6 router ID: 2002::28
      Area addresses: 49
      Interface address: 2001:0:28:316::28
      Interface address: 2001:0:28:336::28
      Interface address: 2001:0:28:352::28
      Interface address: 2002::28
      IS Neighbor          : JNPR-316-MX304.00   Metric: 10
        IPv6 Neighbor Address: 2001:0:28:316::316
        Global IPv6 Interface Address: 2001:0:28:316::28
        Min/Max unidirectional link delay: 9999/9999 us
      IS Neighbor          : JNPR-316-MX304.00   Metric: 10
        IPv6 Neighbor Address: 2001:0:28:316::316
        Global IPv6 Interface Address: 2001:0:28:316::28
        Application Specific Link Attributes:
          Standard applications: Flex-Algo
          User-defined applications: APP3
            Min/Max unidirectional link delay: 9999/9999 us
      IS Neighbor          : ZTE_336_ZXR10_M6000-8SE.00 Metric: 10
        IPv6 Neighbor Address: 2001:0:28:336::336
        Global IPv6 Interface Address: 2001:0:28:336::28
        Min/Max unidirectional link delay: 9999/9999 us
      IS Neighbor          : ZTE_336_ZXR10_M6000-8SE.00 Metric: 10
        IPv6 Neighbor Address: 2001:0:28:336::336
        Global IPv6 Interface Address: 2001:0:28:336::28
        Application Specific Link Attributes:
          Standard applications: Flex-Algo
          User-defined applications: APP3
            Min/Max unidirectional link delay: 9999/9999 us
      IS Neighbor          : Cisco352-N540.00    Metric: 10
        IPv6 Neighbor Address: 2001:0:28:352::352
        Global IPv6 Interface Address: 2001:0:28:352::28
        Min/Max unidirectional link delay: 9999/9999 us
      IS Neighbor          : Cisco352-N540.00    Metric: 10
        IPv6 Neighbor Address: 2001:0:28:352::352
        Global IPv6 Interface Address: 2001:0:28:352::28
        Application Specific Link Attributes:
          Standard applications: Flex-Algo
          User-defined applications: APP3
            Min/Max unidirectional link delay: 9999/9999 us
      Reachability          : 2001:0:28:316::/64 Metric: 10 Type: 1 Up
      Reachability          : 2001:0:28:336::/64 Metric: 10 Type: 1 Up
      Reachability          : 2001:0:28:352::/64 Metric: 10 Type: 1 Up
      Reachability          : 2002::28/128 Metric: 0 Type: 1 Up
      Reachability          : fcbb:0:28::/48 Metric: 0 Type: 1 Up
      SRv6 Locator: fcbb:0:28::/48 Topology: 0
        Metric: 0 Algorithm: 0 Flags: []
        SRv6 SID End with NEXT-CSID PSP USD
          SID : fcbb:0:28::
          SID structure: Block length: 32 Node length: 16
                         Function length: 0 Argument length: 0
      SRv6 Locator: fcbb:1:28::/48 Topology: 0
        Metric: 0 Algorithm: 128 Flags: []
        SRv6 SID End with NEXT-CSID PSP USD
          SID : fcbb:1:28::
          SID structure: Block length: 32 Node length: 16
                         Function length: 0 Argument length: 0
      Router Capabilities: Router Id: 0.0.0.0 Flags: []
        SRv6 Capability: Flags: []
        Algorithms:  0, 128
        Flex Algo: Algorithm: 128 Metric: Min Unidirectional Delay Metric (1) Calc: SPF (0) Prio: 100
          Flags: [] 0x1
    Huawei-34.00-00             257  50426  1044    139 L2  0000.0000.0034.00-00  <>
      Remaining lifetime received: 1199 s Modified to: 1200 s
      NLPID: 0xCC(IPv4)
      Hostname: Huawei-34
      Area addresses: 49.0001
      Interface address: 100.0.0.34
      Interface address: 20.34.180.34
      IS Neighbor          : Spine2-J-180.00     Metric: 10
        IPv4 Neighbor Address: 20.34.180.180
        IPv4 Interface Address: 20.34.180.34
        Adj-sid: 48000 flags: [L V] weight: 0x0
      Reachability         : 100.0.0.34/32 Metric: 0 Type: 1 Up
        SR Prefix-SID: 34 Flags: [N] Algorithm: 0
      Reachability         : 20.34.180.0/24 Metric: 10 Type: 1 Up
      Router Capabilities: Router Id: 100.0.0.34 Flags: []
        Maximum SID depth:
          Base MPLS imposition (MSD type 1):  10
        SR Capability: Flags: [I]
          SRGB Base: 20000 Range: 2000
    huawei_36.00-00             253  62393  1044   1030 L2  0000.0000.0036.00-00  <>
      Remaining lifetime received: 1199 s Modified to: 1200 s
      NLPID: 0x8E(IPv6)
      Hostname: huawei_36
      Area addresses: 49.0000
      Topology: 0 (IPv4)
      Interface address: 2002::36
      Interface address: 2001:0:36:58::36
      Interface address: 2001:0:20:36::36
      IS Neighbor          : Nokia_58-SR1-3-SRv6.00 Metric: 10
        IPv6 Neighbor Address: 2001:0:36:58::58
        Global IPv6 Interface Address: 2001:0:36:58::36
        Application Specific Link Attributes:
          Standard applications: Flex-Algo
            TE default metric: 11
            Min/Max unidirectional link delay: 3600/3600 us
      IS Neighbor          : Nokia_58-SR1-3-SRv6.00 Metric: 10
        IPv6 Neighbor Address: 2001:0:36:58::58
        Global IPv6 Interface Address: 2001:0:36:58::36
      Reachability          : 2002::36/128 Metric: 0 Type: 1 Up
      Reachability          : fcbb:0:36::/48 Metric: 0 Type: 1 Up
      Reachability          : 2001:0:36:58::/64 Metric: 10 Type: 1 Up
      Reachability          : 2001:0:20:36::/64 Metric: 10 Type: 1 Up
      SRv6 Locator: fcbb:1:36::/48 Topology: 0
        Metric: 0 Algorithm: 128 Flags: []
        SRv6 SID End with NEXT-CSID PSP USD
          SID : fcbb:1:36::
          SID structure: Block length: 32 Node length: 16
                         Function length: 0 Argument length: 80
        SRv6 SID Un Supported
          SID : fcbb:1:36:e004::
          SID structure: Block length: 32 Node length: 16
                         Function length: 16 Argument length: 64
        SRv6 SID End
          SID : fcbb:1:36:e005::
          SID structure: Block length: 32 Node length: 16
                         Function length: 16 Argument length: 0
        SRv6 SID End with PSP
          SID : fcbb:1:36:e006::
          SID structure: Block length: 32 Node length: 16
                         Function length: 16 Argument length: 0
        SRv6 SID End with PSP USP USD
          SID : fcbb:1:36:e007::
          SID structure: Block length: 32 Node length: 16
                         Function length: 16 Argument length: 0
      SRv6 Locator: fcbb:0:36::/48 Topology: 0
        Metric: 0 Algorithm: 0 Flags: []
        SRv6 SID End with NEXT-CSID PSP USD
          SID : fcbb:0:36::
          SID structure: Block length: 32 Node length: 16
                         Function length: 0 Argument length: 80
        SRv6 SID Un Supported
          SID : fcbb:0:36:e004::
          SID structure: Block length: 32 Node length: 16
                         Function length: 16 Argument length: 64
        SRv6 SID End
          SID : fcbb:0:36:e005::
          SID structure: Block length: 32 Node length: 16
                         Function length: 16 Argument length: 0
        SRv6 SID End with PSP
          SID : fcbb:0:36:e006::
          SID structure: Block length: 32 Node length: 16
                         Function length: 16 Argument length: 0
        SRv6 SID End with PSP USP USD
          SID : fcbb:0:36:e007::
          SID structure: Block length: 32 Node length: 16
                         Function length: 16 Argument length: 0
      Router Capabilities: Router Id: 0.0.0.0 Flags: []
        SRv6 Capability: Flags: []
        Algorithms:  0, 128, 129, 130
      Router Capabilities: Router Id: 0.0.0.0 Flags: []
        Flex Algo: Algorithm: 128 Metric: Min Unidirectional Delay Metric (1) Calc: SPF (0) Prio: 128
          Flags: [M] 0x80
        Flex Algo: Algorithm: 129 Metric: TE Metric (2) Calc: SPF (0) Prio: 128
          Flags: [M] 0x80
        Flex Algo: Algorithm: 130 Metric: IGP Metric (0) Calc: SPF (0) Prio: 128
          Exclude admin groups: 1
          Flags: [M] 0x80
    huawei_36.00-01             915  22718   946    465 L2  0000.0000.0036.00-01  <>
      Remaining lifetime received: 1199 s Modified to: 1200 s
      IS Neighbor          : h3c_20_CR16010E-F.00 Metric: 10
        IPv6 Neighbor Address: 2001:0:20:36::20
        Global IPv6 Interface Address: 2001:0:20:36::36
        Application Specific Link Attributes:
          Standard applications: Flex-Algo
            TE default metric: 11
            Min/Max unidirectional link delay: 100/100 us
      IS Neighbor          : h3c_20_CR16010E-F.00 Metric: 10
        IPv6 Neighbor Address: 2001:0:20:36::20
        Global IPv6 Interface Address: 2001:0:20:36::36
    anet-161-R3.00-00           266   8442   986    334 L2  0000.0000.0161.00-00  <>
      Remaining lifetime received: 1199 s Modified to: 1200 s
      NLPID: 0xCC(IPv4) 0x8E(IPv6)
      Hostname: anet-161-R3
      Area addresses: 49.0000
      Interface address: 20.161.180.161
      Interface address: 100.0.0.161
      Interface address: 2001:0:59:161::161
      Interface address: 2001:0:161:342::161
      Interface address: 2002::161
      IS Neighbor          : Spine2-J-180.00     Metric: 10
        IPv4 Neighbor Address: 20.161.180.180
        IPv4 Interface Address: 20.161.180.161
        Adj-sid: 100001 flags: [L V] weight: 0x0
      IS Neighbor          : Cisco342-9902.00    Metric: 10
      Reachability         : 20.161.180.0/24 Metric: 10 Type: 1 Up
      Reachability         : 100.0.0.161/32 Metric: 10 Type: 1 Up
        SR Prefix-SID: 161 Flags: [N] Algorithm: 0
      Reachability          : fcbb:0:161::/48 Metric: 10 Type: 1 Up
      Reachability          : 2001:0:59:161::/64 Metric: 10 Type: 1 Up
      Reachability          : 2001:0:161:342::/64 Metric: 10 Type: 1 Up
      Reachability          : 2002::161/128 Metric: 10 Type: 1 Up
      SRv6 Locator: fcbb:0:161::/48 Topology: 0
        Metric: 10 Algorithm: 0 Flags: []
        SRv6 SID End with NEXT-CSID PSP USD
          SID : fcbb:0:161::
          SID structure: Block length: 32 Node length: 16
                         Function length: 16 Argument length: 0
      Router Capabilities: Router Id: 100.0.0.161 Flags: []
        SR Local Block:
          SRLB Base: 965536 Range: 65536
        Area leader priority: 250 algorithm: 0
        Maximum SID depth:
          Base MPLS imposition (MSD type 1):  12
        SRv6 Capability: Flags: []
        SR Capability: Flags: [I V]
          SRGB Base: 900000 Range: 65536
    JNPR-307-ACX7024.00-00      1636  51562  1133    666 L2  0000.0000.0307.00-00  <>
      Remaining lifetime received: 1199 s Modified to: 1200 s
      NLPID: 0x8E(IPv6)
      Hostname: JNPR-307-ACX7024
      TE IPv4 router ID: 10.0.1.7
      TE IPv6 router ID: 2002::307
      Area addresses: 49.0000
      Interface address: 10.0.1.7
      IS Neighbor          : Cisco352-N540.00    Metric: 10
        IPv6 Neighbor Address: 2001:0:307:352::352
        Global IPv6 Interface Address: 2001:0:307:352::307
        TE default metric: 11
        Min/Max unidirectional link delay: 420/517 us
        Application Specific Link Attributes:
          Standard applications: Flex-Algo
            Min/Max unidirectional link delay: 420/517 us
      IS Neighbor          : Cisco353-8201-24H8FH.00 Metric: 10
        IPv6 Neighbor Address: 2001:0:307:353::353
        Global IPv6 Interface Address: 2001:0:307:353::307
        TE default metric: 11
        Min/Max unidirectional link delay: 597/2010 us
        Application Specific Link Attributes:
          Standard applications: Flex-Algo
            Min/Max unidirectional link delay: 597/2010 us
      Reachability          : 2002::307/128 Metric: 0 Type: 1 Up
      Reachability          : 2001:0:307:353::/64 Metric: 10 Type: 1 Up
      Reachability          : 2001:0:307:352::/64 Metric: 10 Type: 1 Up
      Reachability          : fcbb:0:307::/48 Metric: 0 Type: 1 Up
      Reachability          : fcbb:0:9307::/48 Metric: 0 Type: 1 Up
      SRv6 Locator: fcbb:7:307::/48 Topology: 0
        Metric: 0 Algorithm: 134 Flags: []
      SRv6 Locator: fcbb:5:307::/48 Topology: 0
        Metric: 0 Algorithm: 132 Flags: []
      SRv6 Locator: fcbb:0:307::/48 Topology: 0
        Metric: 0 Algorithm: 0 Flags: []
      SRv6 Locator: fcbb:1:307::/48 Topology: 0
        Metric: 0 Algorithm: 128 Flags: []
      SRv6 Locator: fcbb:0:9307::/48 Topology: 0
        Metric: 0 Algorithm: 0 Flags: []
        SRv6 SID End with NEXT-CSID PSP USP USD
          SID : fcbb:0:9307::
          SID structure: Block length: 32 Node length: 16
                         Function length: 0 Argument length: 80
      SRv6 Locator: fcbb:2:307::/48 Topology: 0
        Metric: 0 Algorithm: 129 Flags: []
      SRv6 Locator: fcbb:3:307::/48 Topology: 0
        Metric: 0 Algorithm: 130 Flags: []
      Router Capabilities: Router Id: 10.0.1.7 Flags: []
        Maximum SID depth:
          Base MPLS imposition (MSD type 1):  0
        SRv6 Capability: Flags: []
        Algorithms:  0, 1, 128, 129, 130, 132, 134
        Flex Algo: Algorithm: 134 Metric: IGP Metric (0) Calc: SPF (0) Prio: 255
        Flex Algo: Algorithm: 133 Metric: IGP Metric (0) Calc: SPF (0) Prio: 255
        Flex Algo: Algorithm: 132 Metric: IGP Metric (0) Calc: SPF (0) Prio: 255
        Flex Algo: Algorithm: 130 Metric: IGP Metric (0) Calc: SPF (0) Prio: 0
          Exclude admin groups: 1
        Flex Algo: Algorithm: 129 Metric: TE Metric (2) Calc: SPF (0) Prio: 0
      Unsupported TLV: Type: 14 Length: 2
    JNPR-310-ACX7100-48L.00-00     13503  30981  1179    774 L2  0000.0000.0310.00-00  <>
      Remaining lifetime received: 1199 s Modified to: 1200 s
      NLPID: 0x8E(IPv6)
      Hostname: JNPR-310-ACX7100-48L
      TE IPv4 router ID: 10.0.1.10
      TE IPv6 router ID: 2002::310
      Area addresses: 49.0001
      Interface address: 10.0.1.10
      IS Neighbor          : Nokia_58-SR1-3-SRv6.00 Metric: 10
        IPv6 Neighbor Address: 2001:0:58:310::58
        Global IPv6 Interface Address: 2001:0:58:310::310
        TE default metric: 11
        Min/Max unidirectional link delay: 31/68 us
        Application Specific Link Attributes:
          Standard applications: Flex-Algo
            Min/Max unidirectional link delay: 31/68 us
      IS Neighbor          : Cisco353-8201-24H8FH.00 Metric: 10
        IPv6 Neighbor Address: 2001:0:310:353::353
        Global IPv6 Interface Address: 2001:0:310:353::353
        TE default metric: 11
        Min/Max unidirectional link delay: 673/1968 us
        Application Specific Link Attributes:
          Standard applications: Flex-Algo
            Min/Max unidirectional link delay: 673/1968 us
      Reachability          : 2002::310/128 Metric: 0 Type: 1 Up
      Reachability          : 2002::/72 Metric: 10 Type: 1 Up
      Reachability          : 2001:0:58:310::/64 Metric: 10 Type: 1 Up
      Reachability          : 2001:0:310:353::/64 Metric: 10 Type: 1 Up
      Reachability          : 2001:25:110:225::/64 Metric: 10 Type: 1 Up
      Reachability          : 2001:0:11:310::/64 Metric: 10 Type: 1 Up
      Reachability          : fcbb:0:1000::/36 Metric: 10 Type: 1 Up
      Reachability          : fcbb:0:9310::/48 Metric: 0 Type: 1 Up
      Reachability          : fcbb:0:1310::/48 Metric: 0 Type: 1 Up
      SRv6 Locator: fcbb:7:1310::/48 Topology: 0
        Metric: 0 Algorithm: 134 Flags: []
      SRv6 Locator: fcbb:5:1310::/48 Topology: 0
        Metric: 0 Algorithm: 132 Flags: []
      SRv6 Locator: fcbb:0:9310::/48 Topology: 0
        Metric: 0 Algorithm: 0 Flags: []
        SRv6 SID End with NEXT-CSID PSP USP USD
          SID : fcbb:0:9310::
          SID structure: Block length: 32 Node length: 16
                         Function length: 0 Argument length: 80
      SRv6 Locator: fcbb:2:1310::/48 Topology: 0
        Metric: 0 Algorithm: 129 Flags: []
      SRv6 Locator: fcbb:3:1310::/48 Topology: 0
        Metric: 0 Algorithm: 130 Flags: []
      SRv6 Locator: fcbb:0:1310::/48 Topology: 0
        Metric: 0 Algorithm: 0 Flags: []
      SRv6 Locator: fcbb:1:1310::/48 Topology: 0
        Metric: 0 Algorithm: 128 Flags: []
      SRv6 Locator: fcbb:0:1000::/36 Topology: 0
        Metric: 10 Algorithm: 0 Flags: []
      SRv6 Locator: fcbb:1:1000::/36 Topology: 0
        Metric: 10 Algorithm: 128 Flags: []
      Router Capabilities: Router Id: 10.0.1.10 Flags: []
        Maximum SID depth:
          Base MPLS imposition (MSD type 1):  0
        SRv6 Capability: Flags: []
        Algorithms:  0, 1, 128, 129, 130, 132, 134
        Flex Algo: Algorithm: 134 Metric: IGP Metric (0) Calc: SPF (0) Prio: 255
        Flex Algo: Algorithm: 133 Metric: IGP Metric (0) Calc: SPF (0) Prio: 255
        Flex Algo: Algorithm: 132 Metric: IGP Metric (0) Calc: SPF (0) Prio: 255
        Flex Algo: Algorithm: 130 Metric: IGP Metric (0) Calc: SPF (0) Prio: 0
          Exclude admin groups: 1
        Flex Algo: Algorithm: 129 Metric: TE Metric (2) Calc: SPF (0) Prio: 0
      Unsupported TLV: Type: 14 Length: 2
    JNPR-316-MX304.00-00       1313  41528  1044    839 L2  0000.0000.0316.00-00  <>
      Remaining lifetime received: 1199 s Modified to: 1200 s
      NLPID: 0x8E(IPv6)
      Hostname: JNPR-316-MX304
      TE IPv4 router ID: 10.0.1.16
      TE IPv6 router ID: 2002::316
      Area addresses: 49.0000
      Interface address: 10.0.1.16
      IS Neighbor          : h3c_28_S12500R-2L.00 Metric: 10
        IPv6 Neighbor Address: 2001:0:28:316::28
        Global IPv6 Interface Address: 2001:0:28:316::316
        TE default metric: 11
        Min/Max unidirectional link delay: 9999/9999 us
        Application Specific Link Attributes:
          Standard applications: Flex-Algo
            Min/Max unidirectional link delay: 9999/9999 us
      IS Neighbor          : Cisco342-9902.00    Metric: 10
        IPv6 Neighbor Address: 2001:0:316:342::342
        Global IPv6 Interface Address: 2001:0:316:342::316
        TE default metric: 11
        Min/Max unidirectional link delay: 186/284 us
        Application Specific Link Attributes:
          Standard applications: Flex-Algo
            Min/Max unidirectional link delay: 186/284 us
      Reachability          : 2001:0:28:316::/64 Metric: 10 Type: 1 Up
      Reachability          : 2002::316/128 Metric: 0 Type: 1 Up
      Reachability          : 2001:0:316:342::/64 Metric: 10 Type: 1 Up
      Reachability          : fcbb:0:316::/48 Metric: 0 Type: 1 Up
      SRv6 Locator: fcbb:0:316::/48 Topology: 0
        Metric: 0 Algorithm: 0 Flags: []
        SRv6 SID End with NEXT-CSID PSP USP USD
          SID : fcbb:0:316::
          SID structure: Block length: 32 Node length: 16
                         Function length: 0 Argument length: 80
      SRv6 Locator: fcbb:1:316::/48 Topology: 0
        Metric: 0 Algorithm: 128 Flags: []
        SRv6 SID End with NEXT-CSID PSP USP USD
          SID : fcbb:1:316::
          SID structure: Block length: 32 Node length: 16
                         Function length: 0 Argument length: 80
      SRv6 Locator: fcbb:2:316::/48 Topology: 0
        Metric: 0 Algorithm: 129 Flags: []
        SRv6 SID End with NEXT-CSID PSP USP USD
          SID : fcbb:2:316::
          SID structure: Block length: 32 Node length: 16
                         Function length: 0 Argument length: 80
      SRv6 Locator: fcbb:3:316::/48 Topology: 0
        Metric: 0 Algorithm: 130 Flags: []
        SRv6 SID End with NEXT-CSID PSP USP USD
          SID : fcbb:3:316::
          SID structure: Block length: 32 Node length: 16
                         Function length: 0 Argument length: 80
      SRv6 Locator: fcbb:5:316::/48 Topology: 0
        Metric: 0 Algorithm: 132 Flags: []
        SRv6 SID End with NEXT-CSID PSP USP USD
          SID : fcbb:5:316::
          SID structure: Block length: 32 Node length: 16
                         Function length: 0 Argument length: 80
      SRv6 Locator: fcbb:6:316::/48 Topology: 0
        Metric: 0 Algorithm: 133 Flags: []
        SRv6 SID End with NEXT-CSID PSP USP USD
          SID : fcbb:6:316::
          SID structure: Block length: 32 Node length: 16
                         Function length: 0 Argument length: 80
      SRv6 Locator: fcbb:7:316::/48 Topology: 0
        Metric: 0 Algorithm: 134 Flags: []
        SRv6 SID End with NEXT-CSID PSP USP USD
          SID : fcbb:7:316::
          SID structure: Block length: 32 Node length: 16
                         Function length: 0 Argument length: 80
      Router Capabilities: Router Id: 10.0.1.16 Flags: []
        Maximum SID depth:
          Base MPLS imposition (MSD type 1):  0
        SRv6 Capability: Flags: []
        Algorithms:  0, 1, 128, 129, 130, 132, 133, 134
        Flex Algo: Algorithm: 134 Metric: IGP Metric (0) Calc: SPF (0) Prio: 255
        Flex Algo: Algorithm: 133 Metric: IGP Metric (0) Calc: SPF (0) Prio: 255
        Flex Algo: Algorithm: 132 Metric: IGP Metric (0) Calc: SPF (0) Prio: 255
        Flex Algo: Algorithm: 130 Metric: IGP Metric (0) Calc: SPF (0) Prio: 0
          Exclude admin groups: 1
        Flex Algo: Algorithm: 129 Metric: TE Metric (2) Calc: SPF (0) Prio: 0
      Unsupported TLV: Type: 14 Length: 2
    ZTE_336_ZXR10_M6000-8SE.00-00      3527  59579  1178   1198 L2  0000.0000.0336.00-00  <>
      Remaining lifetime received: 1199 s Modified to: 1200 s
      NLPID: 0xCC(IPv4) 0x8E(IPv6)
      Hostname: ZTE_336_ZXR10_M6000-8SE
      TE IPv6 router ID: 2002::336
      Area addresses: 49.0000
      Interface address: 10.0.1.36
      Interface address: 2002::336
      IS Neighbor          : h3c_20_CR16010E-F.00 Metric: 10
        IPv6 Neighbor Address: 2001:0:20:336::20
        Global IPv6 Interface Address: 2001:0:20:336::336
        Min/Max unidirectional link delay: 25/44 us
        Application Specific Link Attributes:
          Standard applications: Flex-Algo
            TE default metric: 100
            Maximum link BW: 100.00 Gbps
            Min/Max unidirectional link delay: 25/44 us
      IS Neighbor          : h3c_20_CR16010E-F.00 Metric: 10
        IPv6 Neighbor Address: 2001:0:20:336::20
        Global IPv6 Interface Address: 2001:0:20:336::336
      IS Neighbor          : h3c_28_S12500R-2L.00 Metric: 10
        IPv6 Neighbor Address: 2001:0:28:336::28
        Global IPv6 Interface Address: 2001:0:28:336::336
        Min/Max unidirectional link delay: 4/4 us
        Application Specific Link Attributes:
          Standard applications: Flex-Algo
            TE default metric: 100
            Maximum link BW: 100.00 Gbps
            Min/Max unidirectional link delay: 4/4 us
      IS Neighbor          : h3c_28_S12500R-2L.00 Metric: 10
        IPv6 Neighbor Address: 2001:0:28:336::28
        Global IPv6 Interface Address: 2001:0:28:336::336
      Reachability         : 10.0.1.36/32 Metric: 10 Type: 1 Up
      Reachability          : 2001:0:20:336::/64 Metric: 10 Type: 1 Up
      Reachability          : 2001:0:28:336::/64 Metric: 10 Type: 1 Up
      Reachability          : 2002::336/128 Metric: 10 Type: 1 Up
      Reachability          : fcbb:0:336::/48 Metric: 0 Type: 1 Up
      SRv6 Locator: fcbb:0:336::/48 Topology: 0
        Metric: 0 Algorithm: 0 Flags: []
        SRv6 SID End with NEXT-CSID PSP
          SID : fcbb:0:336::
          SID structure: Block length: 32 Node length: 16
                         Function length: 0 Argument length: 80
      SRv6 Locator: fcbb:1:336::/48 Topology: 0
        Metric: 0 Algorithm: 128 Flags: []
        SRv6 SID End with NEXT-CSID PSP
          SID : fcbb:1:336::
          SID structure: Block length: 32 Node length: 16
                         Function length: 0 Argument length: 80
      SRv6 Locator: fcbb:2:336::/48 Topology: 0
        Metric: 0 Algorithm: 129 Flags: []
        SRv6 SID End with NEXT-CSID PSP
          SID : fcbb:2:336::
          SID structure: Block length: 32 Node length: 16
                         Function length: 0 Argument length: 80
      SRv6 Locator: fcbb:3:336::/48 Topology: 0
        Metric: 0 Algorithm: 130 Flags: []
        SRv6 SID End with NEXT-CSID PSP
          SID : fcbb:3:336::
          SID structure: Block length: 32 Node length: 16
                         Function length: 0 Argument length: 80
      SRv6 Locator: fcbb:4:336::/48 Topology: 0
        Metric: 0 Algorithm: 131 Flags: []
        SRv6 SID End with NEXT-CSID PSP
          SID : fcbb:4:336::
          SID structure: Block length: 32 Node length: 16
                         Function length: 0 Argument length: 80
      Router Capabilities: Router Id: 10.0.1.36 Flags: []
        SR Local Block:
          SRLB Base: 965536 Range: 4096
        Maximum SID depth:
          Base MPLS imposition (MSD type 1):  20
        SRv6 Capability: Flags: []
        SR Capability: Flags: [I]
          SRGB Base: 900000 Range: 65536
        Algorithms:  0, 1, 128, 129, 130, 131
        Flex Algo: Algorithm: 128 Metric: Min Unidirectional Delay Metric (1) Calc: SPF (0) Prio: 100
        Flex Algo: Algorithm: 129 Metric: TE Metric (2) Calc: SPF (0) Prio: 128
        Flex Algo: Algorithm: 130 Metric: IGP Metric (0) Calc: SPF (0) Prio: 128
          Exclude admin groups: 1
        Flex Algo: Algorithm: 131 Metric: IGP Metric (0) Calc: SPF (0) Prio: 128
          Exclude admin groups: 1,231
    h41-9902.00-00              255  17663   480    176 L2  0000.0000.0341.00-00  <>
      Remaining lifetime received: 1199 s Modified to: 1200 s
      NLPID: 0xCC(IPv4)
      Hostname: h41-9902
      Area addresses: 49.0001
      Interface address: 100.0.3.41
      IS Neighbor          : Spine2-J-180.00     Metric: 10
        IPv4 Neighbor Address: 30.41.180.180
        IPv4 Interface Address: 30.41.180.41
        Adj-sid: 24004 flags: [L V] weight: 0x0
        Maximum link BW: 10.00 Gbps
      Reachability         : 30.41.180.0/24 Metric: 10 Type: 1 Up
      Reachability         : 100.0.3.41/32 Metric: 10 Type: 1 Up
        SR Prefix-SID: 341 Flags: [N] Algorithm: 0
      Router Capabilities: Router Id: 100.0.3.41 Flags: []
        SR Local Block:
          SRLB Base: 15000 Range: 1000
        Maximum SID depth:
          Base MPLS imposition (MSD type 1):  10
        SR Capability: Flags: [I]
          SRGB Base: 20000 Range: 2000
        Algorithms:  0, 1
      Unsupported TLV: Type: 14 Length: 2
    Cisco342-9902.00-00         322  50800  1155    563 L2  0000.0000.0342.00-00  <>
      Remaining lifetime received: 1199 s Modified to: 1200 s
      NLPID: 0x8E(IPv6)
      Hostname: Cisco342-9902
      Area addresses: 49.0001
      Interface address: 2002::342
      IS Neighbor          : anet-161-R3.00      Metric: 10
        Global IPv6 Interface Address: 2001:0:161:342::342
        Maximum link BW: 10.00 Gbps
      IS Neighbor          : JNPR-316-MX304.00   Metric: 10
        IPv6 Neighbor Address: 2001:0:316:342::316
        Global IPv6 Interface Address: 2001:0:316:342::342
        Maximum link BW: 100.00 Gbps
        Min/Max unidirectional link delay: 55/132246 us
        Application Specific Link Attributes:
          Standard applications: Flex-Algo
          User-defined applications: APP3
            Min/Max unidirectional link delay: 55/132246 us
      Reachability          : 2001:0:161:342::/64 Metric: 10 Type: 1 Up
      Reachability          : 2001:0:316:342::/64 Metric: 10 Type: 1 Up
      Reachability          : 2002::342/128 Metric: 10 Type: 1 Up
      Reachability          : fcbb:0:342::/48 Metric: 1 Type: 1 Up
      SRv6 Locator: fcbb:0:342::/48 Topology: 0
        Metric: 1 Algorithm: 0 Flags: []
        SRv6 SID End with NEXT-CSID PSP USD
          SID : fcbb:0:342::
          SID structure: Block length: 32 Node length: 16
                         Function length: 0 Argument length: 80
      SRv6 Locator: fcbb:1:342::/48 Topology: 0
        Metric: 1 Algorithm: 128 Flags: []
        SRv6 SID End with NEXT-CSID PSP USD
          SID : fcbb:1:342::
          SID structure: Block length: 32 Node length: 16
                         Function length: 0 Argument length: 80
      Router Capabilities: Router Id: 0.0.0.0 Flags: []
        SRv6 Capability: Flags: []
        Algorithms:  0, 1, 128
      Unsupported TLV: Type: 14 Length: 2
    h45-N57C1.00-00             257  29764   502    177 L2  0000.0000.0345.00-00  <>
      Remaining lifetime received: 1199 s Modified to: 1200 s
      NLPID: 0xCC(IPv4)
      Hostname: h45-N57C1
      Area addresses: 49.0001
      Interface address: 100.0.3.45
      IS Neighbor          : Spine2-J-180.00     Metric: 10
        IPv4 Neighbor Address: 30.45.180.180
        IPv4 Interface Address: 30.45.180.45
        Adj-sid: 28103 flags: [L V] weight: 0x0
        Maximum link BW: 10.00 Gbps
      Reachability         : 30.45.180.0/24 Metric: 10 Type: 1 Up
      Reachability         : 100.0.3.45/32 Metric: 10 Type: 1 Up
        SR Prefix-SID: 345 Flags: [N] Algorithm: 0
      Router Capabilities: Router Id: 100.0.3.45 Flags: []
        SR Local Block:
          SRLB Base: 15000 Range: 1000
        Maximum SID depth:
          Base MPLS imposition (MSD type 1):  12
        SR Capability: Flags: [I]
          SRGB Base: 20000 Range: 2000
        Algorithms:  0, 1
      Unsupported TLV: Type: 14 Length: 2
    Cisco352-N540.00-00         311  10008   700    943 L2  0000.0000.0352.00-00  <>
      Remaining lifetime received: 1199 s Modified to: 1200 s
      NLPID: 0x8E(IPv6)
      Hostname: Cisco352-N540
      Area addresses: 49.0001
      Interface address: 2002::352
      IS Neighbor          : h3c_20_CR16010E-F.00 Metric: 10
        IPv6 Neighbor Address: 2001:0:20:352::20
        Global IPv6 Interface Address: 2001:0:20:352::352
        Maximum link BW: 10.00 Gbps
        Min/Max unidirectional link delay: 26/54 us
        Application Specific Link Attributes:
          Standard applications: Flex-Algo
          User-defined applications: APP3
            Min/Max unidirectional link delay: 26/54 us
      IS Neighbor          : h3c_28_S12500R-2L.00 Metric: 10
        IPv6 Neighbor Address: 2001:0:28:352::28
        Global IPv6 Interface Address: 2001:0:28:352::352
        Maximum link BW: 100.00 Gbps
      IS Neighbor          : JNPR-307-ACX7024.00 Metric: 10
        IPv6 Neighbor Address: 2001:0:307:352::307
        Global IPv6 Interface Address: 2001:0:307:352::352
        Maximum link BW: 10.00 Gbps
        Min/Max unidirectional link delay: 38/72 us
        Application Specific Link Attributes:
          Standard applications: Flex-Algo
          User-defined applications: APP3
            Min/Max unidirectional link delay: 38/72 us
      IS Neighbor          : Nokia-59-IXRe2.00   Metric: 10
        IPv6 Neighbor Address: 2001:0:59:352::59
        Global IPv6 Interface Address: 2001:0:59:352::352
        Maximum link BW: 10.00 Gbps
        Min/Max unidirectional link delay: 31/64 us
        Application Specific Link Attributes:
          Standard applications: Flex-Algo
          User-defined applications: APP3
            Min/Max unidirectional link delay: 31/64 us
      Reachability          : 2001:0:20:352::/64 Metric: 10 Type: 1 Up
      Reachability          : 2001:0:28:352::/64 Metric: 10 Type: 1 Up
      Reachability          : 2001:0:59:352::/64 Metric: 10 Type: 1 Up
      Reachability          : 2001:0:307:352::/64 Metric: 10 Type: 1 Up
      Reachability          : 2002::352/128 Metric: 10 Type: 1 Up
      Reachability          : fcbb:0:352::/48 Metric: 1 Type: 1 Up
      SRv6 Locator: fcbb:0:352::/48 Topology: 0
        Metric: 1 Algorithm: 0 Flags: []
        SRv6 SID End with NEXT-CSID PSP USD
          SID : fcbb:0:352::
          SID structure: Block length: 32 Node length: 16
                         Function length: 0 Argument length: 80
      SRv6 Locator: fcbb:1:352::/48 Topology: 0
        Metric: 1 Algorithm: 128 Flags: []
        SRv6 SID End with NEXT-CSID PSP USD
          SID : fcbb:1:352::
          SID structure: Block length: 32 Node length: 16
                         Function length: 0 Argument length: 80
      Router Capabilities: Router Id: 0.0.0.0 Flags: []
        SRv6 Capability: Flags: []
        Algorithms:  0, 1, 128
      Unsupported TLV: Type: 14 Length: 2
    Cisco353-8201-24H8FH.00-00      2448  64258   658    979 L2  0000.0000.0353.00-00  <>
      Remaining lifetime received: 1199 s Modified to: 1200 s
      NLPID: 0x8E(IPv6)
      Hostname: Cisco353-8201-24H8FH
      Area addresses:
        49.0000
        49.0001
      Interface address: 2002::353
      IS Neighbor          : JNPR-307-ACX7024.00 Metric: 10
        IPv6 Neighbor Address: 2001:0:307:353::307
        Global IPv6 Interface Address: 2001:0:307:353::353
        Maximum link BW: 10.00 Gbps
        Min/Max unidirectional link delay: 38/11083 us
        Application Specific Link Attributes:
          Standard applications: Flex-Algo
          User-defined applications: APP3
            Min/Max unidirectional link delay: 38/11083 us
      IS Neighbor          : JNPR-310-ACX7100-48L.00 Metric: 10
        IPv6 Neighbor Address: 2001:0:310:353::353
        Global IPv6 Interface Address: 2001:0:310:353::353
        Maximum link BW: 100.00 Gbps
      Reachability          : 2001:0:11:310::/64 Metric: 20 Type: 1 Up
      Reachability          : 2001:0:11:353::/64 Metric: 10 Type: 1 Up
      Reachability          : 2001:0:29:338::/64 Metric: 40 Type: 1 Up
      Reachability          : 2001:0:49:338::/64 Metric: 40 Type: 1 Up
      Reachability          : 2001:0:58:310::/64 Metric: 20 Type: 1 Up
      Reachability          : 2001:0:307:353::/64 Metric: 10 Type: 1 Up
      Reachability          : 2001:0:310:353::/64 Metric: 10 Type: 1 Up
      Reachability          : 2002::/72 Metric: 10 Type: 1 Up
      Reachability          : 2002::353/128 Metric: 10 Type: 1 Up
      Reachability          : fcbb:0:419::/48 Metric: 40 Type: 1 Up
      Reachability          : fcbb:0:1000::/36 Metric: 10 Type: 1 Up
      Reachability          : fcbb:0:1353::/48 Metric: 1 Type: 1 Up
      Reachability          : fcbb:0:9310::/48 Metric: 10 Type: 1 Up
      Reachability          : fcbb:1:1000::/36 Metric: 1 Type: 1 Up
      Reachability          : 2001:0:29:58::/64 Metric: 30 Type: 1 Up
      Reachability          : 2001:0:36:58::/64 Metric: 30 Type: 1 Up
      Reachability          : 2001:0:49:199::/64 Metric: 30 Type: 1 Up
      Reachability          : 2001:0:58:419::/64 Metric: 30 Type: 1 Up
      Reachability          : 2001:0:199:302::/64 Metric: 20 Type: 1 Up
      Reachability          : 2001:0:199:344::/64 Metric: 30 Type: 1 Up
      Reachability          : 2001:0:302:353::/64 Metric: 10 Type: 1 Up
      Reachability          : 2001:25:110:225::/64 Metric: 20 Type: 1 Up
      SRv6 Locator: fcbb:0:419::/48 Topology: 0
        Metric: 40 Algorithm: 0 Flags: []
      SRv6 Locator: fcbb:0:1000::/36 Topology: 0
        Metric: 10 Algorithm: 0 Flags: []
      SRv6 Locator: fcbb:0:1353::/48 Topology: 0
        Metric: 1 Algorithm: 0 Flags: []
        SRv6 SID End with NEXT-CSID PSP USD
          SID : fcbb:0:1353::
          SID structure: Block length: 32 Node length: 16
                         Function length: 0 Argument length: 80
      SRv6 Locator: fcbb:0:9310::/48 Topology: 0
        Metric: 10 Algorithm: 0 Flags: []
      SRv6 Locator: fcbb:1:1000::/36 Topology: 0
        Metric: 1 Algorithm: 0 Flags: []
      SRv6 Locator: fcbb:1:1353::/48 Topology: 0
        Metric: 1 Algorithm: 128 Flags: []
        SRv6 SID End with NEXT-CSID PSP USD
          SID : fcbb:1:1353::
          SID structure: Block length: 32 Node length: 16
                         Function length: 0 Argument length: 80
      Router Capabilities: Router Id: 0.0.0.0 Flags: []
        SRv6 Capability: Flags: []
        Algorithms:  0, 1, 128
        Flex Algo: Algorithm: 128 Metric: Min Unidirectional Delay Metric (1) Calc: SPF (0) Prio: 128
      Unsupported TLV: Type: 14 Length: 2
    evpn-rr-58.00-00            254  22859  1185    178 L2  0000.0000.0358.00-00  <>
      Remaining lifetime received: 1199 s Modified to: 1200 s
      NLPID: 0xCC(IPv4)
      Hostname: evpn-rr-58
      Area addresses: 49.0001
      Interface address: 100.0.3.58
      IS Neighbor          : Spine2-J-180.00     Metric: 10
        IPv4 Neighbor Address: 30.58.180.180
        IPv4 Interface Address: 30.58.180.58
        Adj-sid: 24001 flags: [L V] weight: 0x0
        Maximum link BW: 1.00 Gbps
      Reachability         : 30.58.180.0/24 Metric: 10 Type: 1 Up
      Reachability         : 100.0.3.58/32 Metric: 10 Type: 1 Up
        SR Prefix-SID: 358 Flags: [N] Algorithm: 0
      Router Capabilities: Router Id: 100.0.3.58 Flags: []
        SR Local Block:
          SRLB Base: 15000 Range: 1000
        Maximum SID depth:
          Base MPLS imposition (MSD type 1):  10
        SR Capability: Flags: [I]
          SRGB Base: 16000 Range: 8000
        Algorithms:  0, 1
      Unsupported TLV: Type: 14 Length: 2
    evpn-rr2-60.00-00           253  30995  1152    179 L2  0000.0000.0360.00-00  <>
      Remaining lifetime received: 1199 s Modified to: 1200 s
      NLPID: 0xCC(IPv4)
      Hostname: evpn-rr2-60
      Area addresses: 49.0001
      Interface address: 100.0.3.60
      IS Neighbor          : Spine2-J-180.00     Metric: 10
        IPv4 Neighbor Address: 30.60.180.180
        IPv4 Interface Address: 30.60.180.60
        Adj-sid: 24001 flags: [L V] weight: 0x0
        Maximum link BW: 1.00 Gbps
      Reachability         : 30.60.180.0/24 Metric: 10 Type: 1 Up
      Reachability         : 100.0.3.60/32 Metric: 10 Type: 1 Up
        SR Prefix-SID: 360 Flags: [N] Algorithm: 0
      Router Capabilities: Router Id: 100.0.3.60 Flags: []
        SR Local Block:
          SRLB Base: 15000 Range: 1000
        Maximum SID depth:
          Base MPLS imposition (MSD type 1):  10
        SR Capability: Flags: [I]
          SRGB Base: 16000 Range: 8000
        Algorithms:  0, 1
      Unsupported TLV: Type: 14 Length: 2
    Ribbon_31.00-00             246  12442   594     79 L2  0001.0000.0031.00-00  <>
      Remaining lifetime received: 1199 s Modified to: 1200 s
      NLPID: 0xCC(IPv4)
      TE IPv4 router ID: 100.0.0.31
      Area addresses: 49.0001
      Router Capabilities: Router Id: 100.0.0.31 Flags: []
        SR Local Block:
          SRLB Base: 16 Range: 15344
        Maximum SID depth:
          Base MPLS imposition (MSD type 1):  10
        SR Capability: Flags: [I]
          SRGB Base: 20000 Range: 2000
      Unsupported TLV: Type: 14 Length: 2
    Ribbon_31.00-01             246  38790  1084     38 L2  0001.0000.0031.00-01  <>
      Remaining lifetime received: 1199 s Modified to: 1200 s
      Hostname: Ribbon_31
    Ribbon_31.00-02             248  33074   331    108 L2  0001.0000.0031.00-02  <>
      Remaining lifetime received: 1199 s Modified to: 1200 s
      Interface address: 100.0.0.31
      Interface address: 20.31.180.31
      IS Neighbor          : Spine2-J-180.00     Metric: 10
        IPv4 Neighbor Address: 20.31.180.180
        IPv4 Interface Address: 20.31.180.31
        Adj-sid: 756642 flags: [L V] weight: 0x0
        Adj-sid: 756643 flags: [L V B] weight: 0x0
      Reachability         : 100.0.0.31/32 Metric: 0 Type: 1 Up
        SR Prefix-SID: 31 Flags: [N] Algorithm: 0
      Reachability         : 20.31.180.0/24 Metric: 10 Type: 1 Up
    Spine2-J-180.00-00          494   1166   464    830 L2  0001.0001.0180.00-00  <>
      Remaining lifetime received: 1199 s Modified to: 1200 s
      NLPID: 0xCC(IPv4)
      Hostname: Spine2-J-180
      Area addresses: 49.0001
      Interface address: 20.180.183.180
      Interface address: 20.21.180.180
      Interface address: 20.34.180.180
      Interface address: 20.161.180.180
      Interface address: 30.79.180.180
      Interface address: 20.180.182.180
      Interface address: 20.180.181.180
      Interface address: 20.3.180.180
      Interface address: 20.180.184.180
      Interface address: 30.41.180.180
      Interface address: 20.31.180.180
      Interface address: 30.9.180.180
      Interface address: 20.56.180.180
      Interface address: 20.26.180.180
      Interface address: 30.14.180.180
      Interface address: 30.45.180.180
      Interface address: 30.60.180.180
      Interface address: 30.58.180.180
      IS Neighbor          : 0000.0000.0021.00   Metric: 10
        IPv4 Neighbor Address: 20.21.180.21
        IPv4 Interface Address: 20.21.180.180
        Adj-sid: 100009 flags: [L V] weight: 0x0
      IS Neighbor          : Huawei-34.00        Metric: 10
        IPv4 Neighbor Address: 20.34.180.34
        IPv4 Interface Address: 20.34.180.180
        Adj-sid: 100018 flags: [L V] weight: 0x0
      IS Neighbor          : juniper_379_MX304-evpn-mpls.00 Metric: 10
        IPv4 Neighbor Address: 30.79.180.79
        IPv4 Interface Address: 30.79.180.180
        Adj-sid: 100008 flags: [L V] weight: 0x0
      IS Neighbor          : PE21-J2-181.00      Metric: 10
        IPv4 Neighbor Address: 20.180.181.181
        IPv4 Interface Address: 20.180.181.180
        Adj-sid: 100000 flags: [L V] weight: 0x0
      IS Neighbor          : CIEN-5169-3.00      Metric: 10
        IPv4 Neighbor Address: 20.3.180.3
        IPv4 Interface Address: 20.3.180.180
        Adj-sid: 100001 flags: [L V] weight: 0x0
      IS Neighbor          : Ribbon_31.00        Metric: 10
        IPv4 Neighbor Address: 20.31.180.31
        IPv4 Interface Address: 20.31.180.180
        Adj-sid: 100019 flags: [L V] weight: 0x0
      IS Neighbor          : juniper-309-acx7332.00 Metric: 10
        IPv4 Neighbor Address: 30.9.180.9
        IPv4 Interface Address: 30.9.180.180
        Adj-sid: 100017 flags: [L V] weight: 0x0
      IS Neighbor          : SR1-EVPN.00         Metric: 10
        IPv4 Neighbor Address: 20.56.180.56
        IPv4 Interface Address: 20.56.180.180
        Adj-sid: 100016 flags: [L V] weight: 0x0
      IS Neighbor          : PE23-J2-183.00      Metric: 10
        IPv4 Neighbor Address: 20.180.183.183
        IPv4 Interface Address: 20.180.183.180
        Adj-sid: 100005 flags: [L V] weight: 0x0
      IS Neighbor          : anet-161-R3.00      Metric: 10
        IPv4 Neighbor Address: 20.161.180.161
        IPv4 Interface Address: 20.161.180.180
        Adj-sid: 100020 flags: [L V] weight: 0x0
      IS Neighbor          : PE32-J2-172.00      Metric: 10
        IPv4 Neighbor Address: 20.180.182.182
        IPv4 Interface Address: 20.180.182.180
        Adj-sid: 100004 flags: [L V] weight: 0x0
      IS Neighbor          : PE24-J2-184.00      Metric: 10
        IPv4 Neighbor Address: 20.180.184.184
        IPv4 Interface Address: 20.180.184.180
        Adj-sid: 100006 flags: [L V] weight: 0x0
      IS Neighbor          : h41-9902.00         Metric: 10
        IPv4 Neighbor Address: 30.41.180.41
        IPv4 Interface Address: 30.41.180.180
        Adj-sid: 100013 flags: [L V] weight: 0x0
      IS Neighbor          : evpn-rr2-60.00      Metric: 10
        IPv4 Neighbor Address: 30.60.180.60
        IPv4 Interface Address: 30.60.180.180
        Adj-sid: 100015 flags: [L V] weight: 0x0
      IS Neighbor          : evpn-rr-58.00       Metric: 10
        IPv4 Neighbor Address: 30.58.180.58
        IPv4 Interface Address: 30.58.180.180
        Adj-sid: 100014 flags: [L V] weight: 0x0
      IS Neighbor          : h3c_26_S12500R-2L.00 Metric: 10
        IPv4 Neighbor Address: 20.26.180.26
        IPv4 Interface Address: 20.26.180.180
        Adj-sid: 100010 flags: [L V] weight: 0x0
      IS Neighbor          : h45-N57C1.00        Metric: 10
        IPv4 Neighbor Address: 30.45.180.45
        IPv4 Interface Address: 30.45.180.180
        Adj-sid: 100002 flags: [L V] weight: 0x0
      Reachability         : 100.0.0.180/32 Metric: 0 Type: 1 Up
      Reachability         : 20.180.183.0/24 Metric: 10 Type: 1 Up
      Reachability         : 20.21.180.0/24 Metric: 10 Type: 1 Up
      Reachability         : 20.34.180.0/24 Metric: 10 Type: 1 Up
      Reachability         : 20.161.180.0/24 Metric: 10 Type: 1 Up
      Reachability         : 30.79.180.0/24 Metric: 10 Type: 1 Up
      Reachability         : 20.180.182.0/24 Metric: 10 Type: 1 Up
      Reachability         : 20.180.181.0/24 Metric: 10 Type: 1 Up
      Reachability         : 20.3.180.0/24 Metric: 10 Type: 1 Up
      Reachability         : 20.180.184.0/24 Metric: 10 Type: 1 Up
      Reachability         : 30.41.180.0/24 Metric: 10 Type: 1 Up
      Reachability         : 20.31.180.0/24 Metric: 10 Type: 1 Up
      Reachability         : 30.9.180.0/24 Metric: 10 Type: 1 Up
      Reachability         : 20.56.180.0/24 Metric: 10 Type: 1 Up
      Reachability         : 20.26.180.0/24 Metric: 10 Type: 1 Up
      Reachability         : 30.14.180.0/24 Metric: 10 Type: 1 Up
      Reachability         : 30.45.180.0/24 Metric: 10 Type: 1 Up
      Reachability         : 30.60.180.0/24 Metric: 10 Type: 1 Up
      Reachability         : 30.58.180.0/24 Metric: 10 Type: 1 Up
      Router Capabilities: Router Id: 100.0.0.180 Flags: []
        SR Local Block:
          SRLB Base: 965536 Range: 65536
        Area leader priority: 250 algorithm: 0
        SR Capability: Flags: [I]
          SRGB Base: 900000 Range: 65536
    PE21-J2-181.00-00           251  28400  1152    156 L2  0001.0001.0181.00-00  <>
      Remaining lifetime received: 1199 s Modified to: 1200 s
      NLPID: 0xCC(IPv4)
      Hostname: PE21-J2-181
      Area addresses: 49.0001
      Interface address: 20.180.181.181
      Interface address: 100.0.0.181
      IS Neighbor          : Spine2-J-180.00     Metric: 10
        IPv4 Neighbor Address: 20.180.181.180
        IPv4 Interface Address: 20.180.181.181
        Adj-sid: 100000 flags: [L V] weight: 0x0
      Reachability         : 20.180.181.0/24 Metric: 10 Type: 1 Up
      Reachability         : 100.0.0.181/32 Metric: 10 Type: 1 Up
        SR Prefix-SID: 181 Flags: [N] Algorithm: 0
      Router Capabilities: Router Id: 100.0.0.201 Flags: []
        SR Local Block:
          SRLB Base: 965536 Range: 65536
        Area leader priority: 250 algorithm: 0
        Maximum SID depth:
          Base MPLS imposition (MSD type 1):  6
        SR Capability: Flags: [I]
          SRGB Base: 900000 Range: 65536
    PE32-J2-172.00-00           262  36799   494    183 L2  0001.0001.0182.00-00  <>
      LSP generation remaining wait time: 0 ms
      Time remaining until refresh: 194 s
      NLPID: 0xCC(IPv4)
      Hostname: PE32-J2-172
      Area addresses: 49.0001
      Interface address: 100.0.0.182
      Interface address: 20.180.182.182
      IS Neighbor          : Spine2-J-180.00     Metric: 10
        IPv4 Neighbor Address: 20.180.182.180
        IPv4 Interface Address: 20.180.182.182
        Adj-sid: 362144 flags: [L V] weight: 0x0
      Reachability         : 20.170.172.0/24 Metric: 0 Type: 1 Up
      Reachability         : 20.149.172.0/24 Metric: 0 Type: 1 Up
      Reachability         : 209.209.209.209/32 Metric: 0 Type: 1 Up
      Reachability         : 100.0.0.182/32 Metric: 10 Type: 1 Up
        SR Prefix-SID: 182 Flags: [N] Algorithm: 0
      Reachability         : 20.180.182.0/24 Metric: 10 Type: 1 Up
      Router Capabilities: Router Id: 209.209.209.209 Flags: []
        SR Local Block:
          SRLB Base: 965536 Range: 65536
        Area leader priority: 250 algorithm: 0
        Maximum SID depth:
          Base MPLS imposition (MSD type 1):  12
        SR Capability: Flags: [I]
          SRGB Base: 20000 Range: 2000
    PE23-J2-183.00-00           274  26080   564    156 L2  0001.0001.0183.00-00  <>
      Remaining lifetime received: 1199 s Modified to: 1200 s
      NLPID: 0xCC(IPv4)
      Hostname: PE23-J2-183
      Area addresses: 49.0001
      Interface address: 20.180.183.183
      Interface address: 100.0.0.183
      IS Neighbor          : Spine2-J-180.00     Metric: 10
        IPv4 Neighbor Address: 20.180.183.180
        IPv4 Interface Address: 20.180.183.183
        Adj-sid: 100000 flags: [L V] weight: 0x0
      Reachability         : 20.180.183.0/24 Metric: 10 Type: 1 Up
      Reachability         : 100.0.0.183/32 Metric: 0 Type: 1 Up
        SR Prefix-SID: 183 Flags: [N] Algorithm: 0
      Router Capabilities: Router Id: 100.0.0.183 Flags: []
        SR Local Block:
          SRLB Base: 965536 Range: 65536
        Area leader priority: 250 algorithm: 0
        Maximum SID depth:
          Base MPLS imposition (MSD type 1):  12
        SR Capability: Flags: [I]
          SRGB Base: 900000 Range: 65536
    PE24-J2-184.00-00           254  48017   599    156 L2  0001.0001.0184.00-00  <>
      Remaining lifetime received: 1199 s Modified to: 1200 s
      NLPID: 0xCC(IPv4)
      Hostname: PE24-J2-184
      Area addresses: 49.0001
      Interface address: 20.180.184.184
      Interface address: 100.0.0.184
      IS Neighbor          : Spine2-J-180.00     Metric: 10
        IPv4 Neighbor Address: 20.180.184.180
        IPv4 Interface Address: 20.180.184.184
        Adj-sid: 100000 flags: [L V] weight: 0x0
      Reachability         : 20.180.184.0/24 Metric: 10 Type: 1 Up
      Reachability         : 100.0.0.184/32 Metric: 0 Type: 1 Up
        SR Prefix-SID: 184 Flags: [N] Algorithm: 0
      Router Capabilities: Router Id: 100.0.0.184 Flags: []
        SR Local Block:
          SRLB Base: 965536 Range: 65536
        Area leader priority: 250 algorithm: 0
        Maximum SID depth:
          Base MPLS imposition (MSD type 1):  12
        SR Capability: Flags: [I]
          SRGB Base: 900000 Range: 65536
    Nokia_58-SR1-3-SRv6.00-00      1479  59869 64986    581 L2  0100.0000.0058.00-00  <>
      NLPID: 0xCC(IPv4) 0x8E(IPv6)
      Hostname: Nokia_58-SR1-3-SRv6
      TE IPv4 router ID: 10.0.0.58
      TE IPv6 router ID: 2002::58
      Area addresses:
        49.0000
        49.0001
      Interface address: 10.0.0.58
      Interface address: 2001:0:36:58::58
      Interface address: 2001:0:58:310::58
      Interface address: 2001:0:58:419::58
      Interface address: 2002::58
      IS Neighbor          : huawei_36.00        Metric: 10
        IPv6 Neighbor Address: 2001:0:36:58::36
        Global IPv6 Interface Address: 2001:0:36:58::58
        Min/Max unidirectional link delay: 100/100 us
        Application Specific Link Attributes:
          Standard applications: Flex-Algo
            Min/Max unidirectional link delay: 100/100 us
      Reachability         : 10.0.0.58/32 Metric: 0 Type: 1 Up
      Reachability          : 2001:0:29:58::/64 Metric: 10 Type: 1 Up
      Reachability          : 2001:0:36:58::/64 Metric: 10 Type: 1 Up
      Reachability          : 2001:0:58:310::/64 Metric: 10 Type: 1 Up
      Reachability          : 2001:0:58:419::/64 Metric: 10 Type: 1 Up
      Reachability          : 2001:0:199:344::/64 Metric: 50 Type: 1 Up
      Reachability          : 2002::58/128 Metric: 0 Type: 1 Up
      Reachability          : 2002::199/128 Metric: 40 Type: 1 Up
      Reachability          : 2002::338/128 Metric: 30 Type: 1 Up
      Reachability          : 2002::344/128 Metric: 60 Type: 1 Up
      Reachability          : fcbb:0:1000::/36 Metric: 0 Type: 1 Up
      SRv6 Locator: fcbb:0:1000::/36 Topology: 0
        Metric: 0 Algorithm: 0 Flags: []
      Router Capabilities: Router Id: 10.0.0.58 Flags: []
        Maximum SID depth:
          Base MPLS imposition (MSD type 1):  0
        SRv6 Capability: Flags: []
        Algorithms:  0, 128
    Nokia_58-SR1-3-SRv6.00-01      4355  32473 65192   1254 L2  0100.0000.0058.00-01  <>
      IS Neighbor          : JNPR-310-ACX7100-48L.00 Metric: 10
        IPv6 Neighbor Address: 2001:0:58:310::310
        Global IPv6 Interface Address: 2001:0:58:310::58
        Min/Max unidirectional link delay: 54/54 us
        Application Specific Link Attributes:
          Standard applications: Flex-Algo
            Min/Max unidirectional link delay: 54/54 us
      IS Neighbor          : Keys-Ixia-419.00    Metric: 10
        IPv6 Neighbor Address: 2001:0:58:419::419
        Global IPv6 Interface Address: 2001:0:58:419::58
        Min/Max unidirectional link delay: 40/40 us
        Application Specific Link Attributes:
          Standard applications: Flex-Algo
            Min/Max unidirectional link delay: 40/40 us
      Reachability          : 2001:0:11:310::/64 Metric: 20 Type: 1 Up
      Reachability          : 2001:0:11:353::/64 Metric: 30 Type: 1 Up
      Reachability          : 2001:0:29:338::/64 Metric: 20 Type: 1 Up
      Reachability          : 2001:0:49:199::/64 Metric: 40 Type: 1 Up
      Reachability          : 2001:0:49:338::/64 Metric: 30 Type: 1 Up
      Reachability          : 2001:0:199:302::/64 Metric: 40 Type: 1 Up
      Reachability          : 2001:0:302:353::/64 Metric: 30 Type: 1 Up
      Reachability          : 2001:0:310:353::/64 Metric: 20 Type: 1 Up
      Reachability          : 2001:25:110:225::/64 Metric: 20 Type: 1 Up
      Reachability          : 2002::/71 Metric: 20 Type: 1 Up
      Reachability          : 2002::11/128 Metric: 20 Type: 1 Up
      Reachability          : 2002::29/128 Metric: 10 Type: 1 Up
      Reachability          : 2002::49/128 Metric: 40 Type: 1 Up
      Reachability          : 2002::302/128 Metric: 30 Type: 1 Up
      Reachability          : 2002::310/128 Metric: 10 Type: 1 Up
      Reachability          : 2002::353/128 Metric: 30 Type: 1 Up
      Reachability          : 2002::419/128 Metric: 20 Type: 1 Up
      Reachability          : fcbb:0:419::/48 Metric: 10 Type: 1 Up
      Reachability          : fcbb:0:9310::/48 Metric: 10 Type: 1 Up
      SRv6 Locator: fcbb:0:419::/48 Topology: 0
        Metric: 10 Algorithm: 0 Flags: []
        SRv6 SID End with NEXT-CSID PSP USD
          SID : fcbb:0:419:11::
          SID structure: Block length: 32 Node length: 16
                         Function length: 0 Argument length: 80
      SRv6 Locator: fcbb:0:9310::/48 Topology: 0
        Metric: 10 Algorithm: 0 Flags: []
        SRv6 SID End with NEXT-CSID PSP USP USD
          SID : fcbb:0:9310::
          SID structure: Block length: 32 Node length: 16
                         Function length: 0 Argument length: 80
      SRv6 Locator: fcbb:1:1011::/48 Topology: 0
        Metric: 77 Algorithm: 128 Flags: []
        SRv6 SID End with NEXT-CSID PSP USD
          SID : fcbb:1:1011::
          SID structure: Block length: 32 Node length: 16
                         Function length: 16 Argument length: 0
      SRv6 Locator: fcbb:1:1029::/48 Topology: 0
        Metric: 100 Algorithm: 128 Flags: []
        SRv6 SID End with NEXT-CSID PSP USD
          SID : fcbb:1:1029::
          SID structure: Block length: 32 Node length: 16
                         Function length: 0 Argument length: 0
      SRv6 Locator: fcbb:1:1058::/48 Topology: 0
        Metric: 0 Algorithm: 128 Flags: []
        SRv6 SID End with NEXT-CSID PSP USD
          SID : fcbb:1:1058::
          SID structure: Block length: 32 Node length: 16
                         Function length: 0 Argument length: 80
      SRv6 Locator: fcbb:1:1199::/48 Topology: 0
        Metric: 10606 Algorithm: 128 Flags: []
        SRv6 SID End with NEXT-CSID PSP USD
          SID : fcbb:1:1199::
          SID structure: Block length: 32 Node length: 16
                         Function length: 0 Argument length: 80
        SRv6 SID Un Supported
          SID : fcbb:1:1199:e001::
          SID structure: Block length: 32 Node length: 16
                         Function length: 16 Argument length: 64
        SRv6 SID End
          SID : fcbb:1:1199:e002::
          SID structure: Block length: 32 Node length: 16
                         Function length: 16 Argument length: 0
        SRv6 SID End with PSP
          SID : fcbb:1:1199:e003::
          SID structure: Block length: 32 Node length: 16
                         Function length: 16 Argument length: 0
        SRv6 SID End with PSP USP USD
          SID : fcbb:1:1199:e004::
          SID structure: Block length: 32 Node length: 16
                         Function length: 16 Argument length: 0
      SRv6 Locator: fcbb:1:1302::/48 Topology: 0
        Metric: 607 Algorithm: 128 Flags: []
        SRv6 SID End with NEXT-CSID PSP USP USD
          SID : fcbb:1:1302::
          SID structure: Block length: 32 Node length: 16
                         Function length: 0 Argument length: 80
      SRv6 Locator: fcbb:1:1310::/48 Topology: 0
        Metric: 54 Algorithm: 128 Flags: []
      SRv6 Locator: fcbb:1:1344::/48 Topology: 0
        Metric: 20606 Algorithm: 128 Flags: []
        SRv6 SID End with NEXT-CSID PSP USD
          SID : fcbb:1:1344::
          SID structure: Block length: 32 Node length: 16
                         Function length: 0 Argument length: 80
      SRv6 Locator: fcbb:1:1353::/48 Topology: 0
        Metric: 558 Algorithm: 128 Flags: []
        SRv6 SID End with NEXT-CSID PSP USD
          SID : fcbb:1:1353::
          SID structure: Block length: 32 Node length: 16
                         Function length: 0 Argument length: 80
    Nokia-59-IXRe2.00-00        420  39618   643    689 L2  0100.0000.0059.00-00  <>
      Remaining lifetime received: 1199 s Modified to: 1200 s
      NLPID: 0xCC(IPv4) 0x8E(IPv6)
      Hostname: Nokia-59-IXRe2
      TE IPv4 router ID: 10.0.0.59
      TE IPv6 router ID: 2002::59
      Area addresses: 49.0000.0000.0059.00
      Interface address: 10.0.0.59
      Interface address: 2001:0:59:161::59
      Interface address: 2001:0:59:352::59
      Interface address: 2002::59
      IS Neighbor          : Cisco352-N540.00    Metric: 10
        IPv6 Neighbor Address: 2001:0:59:352::352
        Global IPv6 Interface Address: 2001:0:59:352::59
        Adj-sid: 1048573 flags: [L V B F] weight: 0x0
        Application Specific Link Attributes:
          Standard applications: SR-TE
            TE default metric: 10
            Maximum link BW: 10.00 Gbps
        Application Specific Link Attributes:
          Standard applications: Flex-Algo
            TE default metric: 10
            Min/Max unidirectional link delay: 39/39 us
      Reachability         : 10.0.0.59/32 Metric: 0 Type: 1 Up
        SR Prefix-SID: 59 Flags: [N P] Algorithm: 0
      Reachability          : 2001:0:59:161::/64 Metric: 10 Type: 1 Up
      Reachability          : 2001:0:59:352::/64 Metric: 10 Type: 1 Up
      Reachability          : 2002::59/128 Metric: 0 Type: 1 Up
        SR Prefix-SID: 159 Flags: [N P] Algorithm: 0
      Reachability          : fcbb:0:59::/48 Metric: 0 Type: 1 Up
      Reachability          : fcbb:3:59::/48 Metric: 0 Type: 1 Up
      Reachability          : fcbb:4:59::/48 Metric: 0 Type: 1 Up
      SRv6 Locator: fcbb:0:59::/48 Topology: 0
        Metric: 0 Algorithm: 0 Flags: []
        SRv6 SID End with NEXT-CSID PSP USD
          SID : fcbb:0:59::
          SID structure: Block length: 32 Node length: 16
                         Function length: 0 Argument length: 80
      SRv6 Locator: fcbb:1:59::/48 Topology: 0
        Metric: 0 Algorithm: 128 Flags: []
        SRv6 SID End with NEXT-CSID PSP USD
          SID : fcbb:1:59::
          SID structure: Block length: 32 Node length: 16
                         Function length: 0 Argument length: 80
      SRv6 Locator: fcbb:3:59::/48 Topology: 0
        Metric: 0 Algorithm: 0 Flags: []
        SRv6 SID End with NEXT-CSID PSP USD
          SID : fcbb:3:59::
          SID structure: Block length: 32 Node length: 16
                         Function length: 0 Argument length: 80
      SRv6 Locator: fcbb:4:59::/48 Topology: 0
        Metric: 0 Algorithm: 0 Flags: []
        SRv6 SID End with NEXT-CSID PSP USD
          SID : fcbb:4:59::
          SID structure: Block length: 32 Node length: 16
                         Function length: 0 Argument length: 80
      Router Capabilities: Router Id: 10.0.0.59 Flags: []
        Maximum SID depth:
          Base MPLS imposition (MSD type 1):  9
        SRv6 Capability: Flags: []
        SR Capability: Flags: [I V]
          SRGB Base: 20000 Range: 2000
        Algorithms:  0, 128, 129, 130, 131
    SR1-EVPN.00-00              328  37311   895    198 L2  1000.0000.0056.00-00  <>
      Remaining lifetime received: 1199 s Modified to: 1200 s
      NLPID: 0xCC(IPv4) 0x8E(IPv6)
      Hostname: SR1-EVPN
      TE IPv4 router ID: 100.0.0.56
      Area addresses: 49.0001
      Interface address: 20.56.180.56
      Interface address: 100.0.0.56
      Interface address: 2001::56
      IS Neighbor          : Spine2-J-180.00     Metric: 10
        IPv4 Neighbor Address: 20.56.180.180
        IPv4 Interface Address: 20.56.180.56
        Adj-sid: 524271 flags: [L V B] weight: 0x0
      Reachability         : 20.56.180.0/24 Metric: 10 Type: 1 Up
      Reachability         : 100.0.0.56/32 Metric: 0 Type: 1 Up
        SR Prefix-SID: 56 Flags: [N P] Algorithm: 0
      Reachability          : 2001::56/128 Metric: 0 Type: 1 Up
      Router Capabilities: Router Id: 100.0.0.56 Flags: []
        Maximum SID depth:
          Base MPLS imposition (MSD type 1):  12
        SR Capability: Flags: [I V]
          SRGB Base: 20000 Range: 2000
        Algorithms:  0
    juniper-309-acx7332.00-00       255  23065  1136    180 L2  1000.0003.0009.00-00  <>
      Remaining lifetime received: 1199 s Modified to: 1200 s
      NLPID: 0xCC(IPv4) 0x8E(IPv6)
      Hostname: juniper-309-acx7332
      TE IPv4 router ID: 100.0.30.9
      Area addresses: 49.0001.0000.0000
      Interface address: 100.0.30.9
      IS Neighbor          : Spine2-J-180.00     Metric: 10
        IPv4 Neighbor Address: 30.9.180.180
        IPv4 Interface Address: 30.9.180.9
        Adj-sid: 33 flags: [L V] weight: 0x0
      Reachability         : 100.0.30.9/32 Metric: 0 Type: 1 Up
        SR Prefix-SID: 309 Flags: [N] Algorithm: 0
      Reachability         : 30.9.180.0/24 Metric: 10 Type: 1 Up
      Router Capabilities: Router Id: 100.0.30.9 Flags: []
        Maximum SID depth:
          Base MPLS imposition (MSD type 1):  3
        SR Capability: Flags: [I V]
          SRGB Base: 20000 Range: 2000
        Algorithms:  0, 1
      Unsupported TLV: Type: 14 Length: 2
    juniper_379_MX304-evpn-mpls.00-00       277  61772  1060    188 L2  1000.0003.7009.00-00  <>
      Remaining lifetime received: 1199 s Modified to: 1200 s
      NLPID: 0xCC(IPv4) 0x8E(IPv6)
      Hostname: juniper_379_MX304-evpn-mpls
      TE IPv4 router ID: 100.0.37.9
      Area addresses: 49.0001.0000.0000
      Interface address: 100.0.37.9
      IS Neighbor          : Spine2-J-180.00     Metric: 10
        IPv4 Neighbor Address: 30.79.180.180
        IPv4 Interface Address: 30.79.180.79
        Adj-sid: 204 flags: [L V] weight: 0x0
      Reachability         : 30.79.180.0/24 Metric: 10 Type: 1 Up
      Reachability         : 100.0.37.9/32 Metric: 0 Type: 1 Up
        SR Prefix-SID: 379 Flags: [N] Algorithm: 0
      Router Capabilities: Router Id: 100.0.37.9 Flags: []
        Maximum SID depth:
          Base MPLS imposition (MSD type 1):  0
        SR Capability: Flags: [I V]
          SRGB Base: 20000 Range: 2000
        Algorithms:  0, 1
      Unsupported TLV: Type: 14 Length: 2
    Keys-Ixia-419.00-00         489   1396   668    315 L2  3800.0000.0419.00-00  <DefaultAtt>
      Remaining lifetime received: 1199 s Modified to: 1200 s
      NLPID: 0xCC(IPv4) 0x8E(IPv6) 0x81(CLNP)
      Hostname: Keys-Ixia-419
      TE IPv6 router ID: 2002::419
      Area addresses: 49.0001
      Interface address: 2001:0:58:419::419
      IS Neighbor          : Nokia_58-SR1-3-SRv6.00 Metric: 10
        TE default metric: 0
        Maximum link BW: 1.00 Gbps
        Maximum reservable link BW: 1.00 Gbps
        Unreserved BW:
            TE class 0: 1.00 Gbps	TE class 1: 1.00 Gbps	TE class 2: 1.00 Gbps
            TE class 3: 1.00 Gbps	TE class 4: 1.00 Gbps	TE class 5: 1.00 Gbps
            TE class 6: 1.00 Gbps	TE class 7: 1.00 Gbps
      Reachability          : 2002::419/128 Metric: 10 Type: 1 Up
      Reachability          : fcbb:0:419::/48 Metric: 10 Type: 1 Up
      Reachability          : 2001:0:58:419::/64 Metric: 10 Type: 1 Up
      SRv6 Locator: fcbb:0:419::/48 Topology: 0
        Metric: 0 Algorithm: 0 Flags: []
        SRv6 SID End with NEXT-CSID PSP USD
          SID : fcbb:0:419:11::
          SID structure: Block length: 32 Node length: 16
                         Function length: 0 Argument length: 80
      Router Capabilities: Router Id: 10.0.1.119 Flags: []
        SRv6 Capability: Flags: []
        Algorithms:  0
```

## show isis flex-algo

```text

IS-IS Instance: sr_eantc VRF: default

```

## show isis flex-algo path detail

```text
```

## show isis segment-routing tunnel

```text
  Index     Endpoint           Next Hop/Tunnel Index     Interface   Labels    
--------- ------------------ ------------------------- ------------- ----------
  1         100.0.0.3/32       20.180.182.180            Ethernet2   [ 900003 ]
  2         100.0.0.181/32     20.180.182.180            Ethernet2   [ 900181 ]
  3         100.0.3.45/32      20.180.182.180            Ethernet2   [ 900345 ]
  4         100.0.37.9/32      20.180.182.180            Ethernet2   [ 900379 ]
  5         100.0.3.60/32      20.180.182.180            Ethernet2   [ 900360 ]
  6         100.0.0.183/32     20.180.182.180            Ethernet2   [ 900183 ]
  7         100.0.0.26/32      20.180.182.180            Ethernet2   [ 900026 ]
  8         100.0.0.34/32      20.180.182.180            Ethernet2   [ 900034 ]
  9         100.0.0.56/32      20.180.182.180            Ethernet2   [ 900056 ]
  10        100.0.3.41/32      20.180.182.180            Ethernet2   [ 900341 ]
  11        100.0.30.9/32      20.180.182.180            Ethernet2   [ 900309 ]
  13        100.0.0.31/32      20.180.182.180            Ethernet2   [ 900031 ]
  14        100.0.3.58/32      20.180.182.180            Ethernet2   [ 900358 ]
  15        100.0.0.21/32      20.180.182.180            Ethernet2   [ 900021 ]
  16        100.0.0.184/32     20.180.182.180            Ethernet2   [ 900184 ]
  17        100.0.0.161/32     20.180.182.180            Ethernet2   [ 900161 ]
  18        10.0.0.59/32       20.180.182.180            Ethernet2   [ 900059 ]

```

## show isis segment-routing prefix-segments

```text

System ID: PE32-J2-172			Instance: 'sr_eantc'
SR supported Data-plane: MPLS			SR Router ID: 209.209.209.209

Node: 19     Proxy-Node: 0      Prefix: 0       Total Segments: 19

Flag Descriptions: R: Re-advertised, N: Node Segment, P: no-PHP
                   E: Explicit-NULL, V: Value, L: Local
Segment status codes: * - Self originated Prefix, L1 - level 1, L2 - level 2, ! - SR-unreachable,
                      # - Some IS-IS next-hops are SR-unreachable
   Prefix                      SID Type       Flags                        System ID       Level Protection  Algorithm   
   ------------------------- ----- ---------- ---------------------------- --------------- ----- ----------- -------------
   10.0.0.59/32                 59 Node       R:0 N:1 P:1 E:0 V:0 L:0      Nokia-59-IXRe2  L2    link        SPF         
   100.0.0.3/32                  3 Node       R:0 N:1 P:0 E:0 V:0 L:0      CIEN-5169-3     L2    link        SPF         
   100.0.0.21/32                21 Node       R:0 N:1 P:0 E:0 V:0 L:0      0000.0000.0021  L2    link        SPF         
   100.0.0.26/32                26 Node       R:0 N:1 P:1 E:0 V:0 L:0      h3c_26_S12500R-2L L2    link        SPF         
   100.0.0.31/32                31 Node       R:0 N:1 P:0 E:0 V:0 L:0      Ribbon_31       L2    link        SPF         
   100.0.0.34/32                34 Node       R:0 N:1 P:0 E:0 V:0 L:0      Huawei-34       L2    link        SPF         
   100.0.0.56/32                56 Node       R:0 N:1 P:1 E:0 V:0 L:0      SR1-EVPN        L2    link        SPF         
   100.0.0.161/32              161 Node       R:0 N:1 P:0 E:0 V:0 L:0      anet-161-R3     L2    link        SPF         
   100.0.0.181/32              181 Node       R:0 N:1 P:0 E:0 V:0 L:0      PE21-J2-181     L2    link        SPF         
*  100.0.0.182/32              182 Node       R:0 N:1 P:0 E:0 V:0 L:0      PE32-J2-172     L2    unprotected SPF         
   100.0.0.183/32              183 Node       R:0 N:1 P:0 E:0 V:0 L:0      PE23-J2-183     L2    link        SPF         
   100.0.0.184/32              184 Node       R:0 N:1 P:0 E:0 V:0 L:0      PE24-J2-184     L2    link        SPF         
   100.0.3.41/32               341 Node       R:0 N:1 P:0 E:0 V:0 L:0      h41-9902        L2    link        SPF         
   100.0.3.45/32               345 Node       R:0 N:1 P:0 E:0 V:0 L:0      h45-N57C1       L2    link        SPF         
   100.0.3.58/32               358 Node       R:0 N:1 P:0 E:0 V:0 L:0      evpn-rr-58      L2    link        SPF         
   100.0.3.60/32               360 Node       R:0 N:1 P:0 E:0 V:0 L:0      evpn-rr2-60     L2    link        SPF         
   100.0.30.9/32               309 Node       R:0 N:1 P:0 E:0 V:0 L:0      juniper-309-acx7332 L2    link        SPF         
   100.0.37.9/32               379 Node       R:0 N:1 P:0 E:0 V:0 L:0      juniper_379_MX304-evpn-mpls L2    link        SPF         
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

 I L2     10.0.0.58/32 [115/90]
           via 20.180.182.180, Ethernet2
 I L2     10.0.0.59/32 [115/70]
           via 20.180.182.180, Ethernet2
 I L2     10.0.1.36/32 [115/70]
           via 20.180.182.180, Ethernet2
 I L2     20.3.180.0/24 [115/20]
           via 20.180.182.180, Ethernet2
 I L2     20.21.180.0/24 [115/20]
           via 20.180.182.180, Ethernet2
 I L2     20.26.180.0/24 [115/20]
           via 20.180.182.180, Ethernet2
 I L2     20.31.180.0/24 [115/20]
           via 20.180.182.180, Ethernet2
 I L2     20.34.180.0/24 [115/20]
           via 20.180.182.180, Ethernet2
 I L2     20.56.180.0/24 [115/20]
           via 20.180.182.180, Ethernet2
 C        20.149.172.0/24
           directly connected, Ethernet25
 I L2     20.161.180.0/24 [115/20]
           via 20.180.182.180, Ethernet2
 C        20.170.172.0/24
           directly connected, Ethernet52/1
 I L2     20.180.181.0/24 [115/20]
           via 20.180.182.180, Ethernet2
 C        20.180.182.0/24
           directly connected, Ethernet2
 I L2     20.180.183.0/24 [115/20]
           via 20.180.182.180, Ethernet2
 I L2     20.180.184.0/24 [115/20]
           via 20.180.182.180, Ethernet2
 I L2     30.9.180.0/24 [115/20]
           via 20.180.182.180, Ethernet2
 I L2     30.14.180.0/24 [115/20]
           via 20.180.182.180, Ethernet2
 I L2     30.41.180.0/24 [115/20]
           via 20.180.182.180, Ethernet2
 I L2     30.45.180.0/24 [115/20]
           via 20.180.182.180, Ethernet2
 I L2     30.58.180.0/24 [115/20]
           via 20.180.182.180, Ethernet2
 I L2     30.60.180.0/24 [115/20]
           via 20.180.182.180, Ethernet2
 I L2     30.79.180.0/24 [115/20]
           via 20.180.182.180, Ethernet2
 I L2     100.0.0.3/32 [115/30]
           via 20.180.182.180, Ethernet2
 I L2     100.0.0.21/32 [115/20]
           via 20.180.182.180, Ethernet2
 I L2     100.0.0.26/32 [115/20]
           via 20.180.182.180, Ethernet2
 I L2     100.0.0.31/32 [115/20]
           via 20.180.182.180, Ethernet2
 I L2     100.0.0.34/32 [115/20]
           via 20.180.182.180, Ethernet2
 I L2     100.0.0.56/32 [115/20]
           via 20.180.182.180, Ethernet2
 I L2     100.0.0.161/32 [115/30]
           via 20.180.182.180, Ethernet2
 I L2     100.0.0.180/32 [115/10]
           via 20.180.182.180, Ethernet2
 I L2     100.0.0.181/32 [115/30]
           via 20.180.182.180, Ethernet2
 C        100.0.0.182/32
           directly connected, Loopback0
 I L2     100.0.0.183/32 [115/20]
           via 20.180.182.180, Ethernet2
 I L2     100.0.0.184/32 [115/20]
           via 20.180.182.180, Ethernet2
 I L2     100.0.3.41/32 [115/30]
           via 20.180.182.180, Ethernet2
 I L2     100.0.3.45/32 [115/30]
           via 20.180.182.180, Ethernet2
 I L2     100.0.3.58/32 [115/30]
           via 20.180.182.180, Ethernet2
 I L2     100.0.3.60/32 [115/30]
           via 20.180.182.180, Ethernet2
 I L2     100.0.30.9/32 [115/20]
           via 20.180.182.180, Ethernet2
 I L2     100.0.37.9/32 [115/20]
           via 20.180.182.180, Ethernet2
 I L2     192.168.20.0/23 [115/20]
           via 20.180.182.180, Ethernet2
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

 I L2     10.0.0.58/32 [115/90]
           via 20.180.182.180, Ethernet2
 I L2     10.0.0.59/32 [115/70]
           via 20.180.182.180, Ethernet2
 I L2     10.0.1.36/32 [115/70]
           via 20.180.182.180, Ethernet2
 I L2     20.3.180.0/24 [115/20]
           via 20.180.182.180, Ethernet2
 I L2     20.21.180.0/24 [115/20]
           via 20.180.182.180, Ethernet2
 I L2     20.26.180.0/24 [115/20]
           via 20.180.182.180, Ethernet2
 I L2     20.31.180.0/24 [115/20]
           via 20.180.182.180, Ethernet2
 I L2     20.34.180.0/24 [115/20]
           via 20.180.182.180, Ethernet2
 I L2     20.56.180.0/24 [115/20]
           via 20.180.182.180, Ethernet2
 C        20.149.172.0/24
           directly connected, Ethernet25
 I L2     20.161.180.0/24 [115/20]
           via 20.180.182.180, Ethernet2
 C        20.170.172.0/24
           directly connected, Ethernet52/1
 I L2     20.180.181.0/24 [115/20]
           via 20.180.182.180, Ethernet2
 C        20.180.182.0/24
           directly connected, Ethernet2
 I L2     20.180.183.0/24 [115/20]
           via 20.180.182.180, Ethernet2
 I L2     20.180.184.0/24 [115/20]
           via 20.180.182.180, Ethernet2
 I L2     30.9.180.0/24 [115/20]
           via 20.180.182.180, Ethernet2
 I L2     30.14.180.0/24 [115/20]
           via 20.180.182.180, Ethernet2
 I L2     30.41.180.0/24 [115/20]
           via 20.180.182.180, Ethernet2
 I L2     30.45.180.0/24 [115/20]
           via 20.180.182.180, Ethernet2
 I L2     30.58.180.0/24 [115/20]
           via 20.180.182.180, Ethernet2
 I L2     30.60.180.0/24 [115/20]
           via 20.180.182.180, Ethernet2
 I L2     30.79.180.0/24 [115/20]
           via 20.180.182.180, Ethernet2
 I L2     100.0.0.3/32 [115/30]
           via 20.180.182.180, Ethernet2
 I L2     100.0.0.21/32 [115/20]
           via 20.180.182.180, Ethernet2
 I L2     100.0.0.26/32 [115/20]
           via 20.180.182.180, Ethernet2
 I L2     100.0.0.31/32 [115/20]
           via 20.180.182.180, Ethernet2
 I L2     100.0.0.34/32 [115/20]
           via 20.180.182.180, Ethernet2
 I L2     100.0.0.56/32 [115/20]
           via 20.180.182.180, Ethernet2
 I L2     100.0.0.161/32 [115/30]
           via 20.180.182.180, Ethernet2
 I L2     100.0.0.180/32 [115/10]
           via 20.180.182.180, Ethernet2
 I L2     100.0.0.181/32 [115/30]
           via 20.180.182.180, Ethernet2
 C        100.0.0.182/32
           directly connected, Loopback0
 I L2     100.0.0.183/32 [115/20]
           via 20.180.182.180, Ethernet2
 I L2     100.0.0.184/32 [115/20]
           via 20.180.182.180, Ethernet2
 I L2     100.0.3.41/32 [115/30]
           via 20.180.182.180, Ethernet2
 I L2     100.0.3.45/32 [115/30]
           via 20.180.182.180, Ethernet2
 I L2     100.0.3.58/32 [115/30]
           via 20.180.182.180, Ethernet2
 I L2     100.0.3.60/32 [115/30]
           via 20.180.182.180, Ethernet2
 I L2     100.0.30.9/32 [115/20]
           via 20.180.182.180, Ethernet2
 I L2     100.0.37.9/32 [115/20]
           via 20.180.182.180, Ethernet2
 I L2     192.168.20.0/23 [115/20]
           via 20.180.182.180, Ethernet2
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


VRF: tenant-a
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

 B I      20.10.56.0/24 [200/0]
           via 100.0.0.56/32, IS-IS SR tunnel index 9, label 524281
              via 20.180.182.180, Ethernet2, label 900056
 B I      20.30.1.0/24 [200/0]
           via 100.0.0.56/32, IS-IS SR tunnel index 9, label 524281
              via 20.180.182.180, Ethernet2, label 900056
 C        20.30.2.0/24
           directly connected, Vlan2302
 C        20.30.3.0/24
           directly connected, Vlan2303
 C        20.30.4.0/24
           directly connected, Vlan2304

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
MPLS forwarding table (Label [metric] Vias) - 26 routes 
MPLS next-hop resolution allow default route: False
Metric Codes:
          A - Active metric
Via Type Codes:
          M - MPLS via, P - Pseudowire via,
          I - IP lookup via, V - VLAN via,
          VA - EVPN VLAN aware via, ES - EVPN ethernet segment via,
          VF - EVPN VLAN flood via, AF - EVPN VLAN aware flood via,
          NG - Nexthop group via

 20003   A[1]
                via M, 20.180.182.180, swap 900003
                    EgressACL: apply
                    directly connected, Ethernet2
                    44:4c:a8:73:9c:0d, vlan 1007
 20021   A[1]
                via M, 20.180.182.180, swap 900021
                    EgressACL: apply
                    directly connected, Ethernet2
                    44:4c:a8:73:9c:0d, vlan 1007
 20026   A[1]
                via M, 20.180.182.180, swap 900026
                    EgressACL: apply
                    directly connected, Ethernet2
                    44:4c:a8:73:9c:0d, vlan 1007
 20031   A[1]
                via M, 20.180.182.180, swap 900031
                    EgressACL: apply
                    directly connected, Ethernet2
                    44:4c:a8:73:9c:0d, vlan 1007
 20034   A[1]
                via M, 20.180.182.180, swap 900034
                    EgressACL: apply
                    directly connected, Ethernet2
                    44:4c:a8:73:9c:0d, vlan 1007
 20056   A[1]
                via M, 20.180.182.180, swap 900056
                    EgressACL: apply
                    directly connected, Ethernet2
                    44:4c:a8:73:9c:0d, vlan 1007
 20059   A[1]
                via M, 20.180.182.180, swap 900059
                    EgressACL: apply
                    directly connected, Ethernet2
                    44:4c:a8:73:9c:0d, vlan 1007
 20161   A[1]
                via M, 20.180.182.180, swap 900161
                    EgressACL: apply
                    directly connected, Ethernet2
                    44:4c:a8:73:9c:0d, vlan 1007
 20181   A[1]
                via M, 20.180.182.180, swap 900181
                    EgressACL: apply
                    directly connected, Ethernet2
                    44:4c:a8:73:9c:0d, vlan 1007
 20183   A[1]
                via M, 20.180.182.180, swap 900183
                    EgressACL: apply
                    directly connected, Ethernet2
                    44:4c:a8:73:9c:0d, vlan 1007
 20184   A[1]
                via M, 20.180.182.180, swap 900184
                    EgressACL: apply
                    directly connected, Ethernet2
                    44:4c:a8:73:9c:0d, vlan 1007
 20309   A[1]
                via M, 20.180.182.180, swap 900309
                    EgressACL: apply
                    directly connected, Ethernet2
                    44:4c:a8:73:9c:0d, vlan 1007
 20341   A[1]
                via M, 20.180.182.180, swap 900341
                    EgressACL: apply
                    directly connected, Ethernet2
                    44:4c:a8:73:9c:0d, vlan 1007
 20345   A[1]
                via M, 20.180.182.180, swap 900345
                    EgressACL: apply
                    directly connected, Ethernet2
                    44:4c:a8:73:9c:0d, vlan 1007
 20358   A[1]
                via M, 20.180.182.180, swap 900358
                    EgressACL: apply
                    directly connected, Ethernet2
                    44:4c:a8:73:9c:0d, vlan 1007
 20360   A[1]
                via M, 20.180.182.180, swap 900360
                    EgressACL: apply
                    directly connected, Ethernet2
                    44:4c:a8:73:9c:0d, vlan 1007
 20379   A[1]
                via M, 20.180.182.180, swap 900379
                    EgressACL: apply
                    directly connected, Ethernet2
                    44:4c:a8:73:9c:0d, vlan 1007
 362144  A[1]
                via M, 20.180.182.180, pop
                    EgressACL: apply
                    directly connected, Ethernet2
                    44:4c:a8:73:9c:0d, vlan 1007
 378528   [0]
                via I, ipv4, vrf tenant-a
 1036782  [0]
                via AF, control word present
                     dot1q   vlan
                    | 2303 | 2303 |
                    | 2304 | 2304 |
 1041343  [0]
                via ES, Port-Channel100
 1041533  [0]
                via V, vlan2301, control word present
 1041763  [0]
                via VF, vlan2302, control word present
 1042318  [0]
                via VA, control word present
                     dot1q   vlan
                    | 2303 | 2303 |
                    | 2304 | 2304 |
 1045184  [0]
                via V, vlan2302, control word present
 1047448  [0]
                via VF, vlan2301, control word present
```

## show mpls lfib route

```text
MPLS forwarding table (Label [metric] Vias) - 26 routes 
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

 IP    20003    [1], 100.0.0.3/32
                via M, 20.180.182.180, swap 900003
                 payload autoDecide, ttlMode uniform, apply egress-acl
                 interface Ethernet2
 IP    20021    [1], 100.0.0.21/32
                via M, 20.180.182.180, swap 900021
                 payload autoDecide, ttlMode uniform, apply egress-acl
                 interface Ethernet2
 IP    20026    [1], 100.0.0.26/32
                via M, 20.180.182.180, swap 900026
                 payload autoDecide, ttlMode uniform, apply egress-acl
                 interface Ethernet2
 IP    20031    [1], 100.0.0.31/32
                via M, 20.180.182.180, swap 900031
                 payload autoDecide, ttlMode uniform, apply egress-acl
                 interface Ethernet2
 IP    20034    [1], 100.0.0.34/32
                via M, 20.180.182.180, swap 900034
                 payload autoDecide, ttlMode uniform, apply egress-acl
                 interface Ethernet2
 IP    20056    [1], 100.0.0.56/32
                via M, 20.180.182.180, swap 900056
                 payload autoDecide, ttlMode uniform, apply egress-acl
                 interface Ethernet2
 IP    20059    [1], 10.0.0.59/32
                via M, 20.180.182.180, swap 900059
                 payload autoDecide, ttlMode uniform, apply egress-acl
                 interface Ethernet2
 IP    20161    [1], 100.0.0.161/32
                via M, 20.180.182.180, swap 900161
                 payload autoDecide, ttlMode uniform, apply egress-acl
                 interface Ethernet2
 IP    20181    [1], 100.0.0.181/32
                via M, 20.180.182.180, swap 900181
                 payload autoDecide, ttlMode uniform, apply egress-acl
                 interface Ethernet2
 IP    20183    [1], 100.0.0.183/32
                via M, 20.180.182.180, swap 900183
                 payload autoDecide, ttlMode uniform, apply egress-acl
                 interface Ethernet2
 IP    20184    [1], 100.0.0.184/32
                via M, 20.180.182.180, swap 900184
                 payload autoDecide, ttlMode uniform, apply egress-acl
                 interface Ethernet2
 IP    20309    [1], 100.0.30.9/32
                via M, 20.180.182.180, swap 900309
                 payload autoDecide, ttlMode uniform, apply egress-acl
                 interface Ethernet2
 IP    20341    [1], 100.0.3.41/32
                via M, 20.180.182.180, swap 900341
                 payload autoDecide, ttlMode uniform, apply egress-acl
                 interface Ethernet2
 IP    20345    [1], 100.0.3.45/32
                via M, 20.180.182.180, swap 900345
                 payload autoDecide, ttlMode uniform, apply egress-acl
                 interface Ethernet2
 IP    20358    [1], 100.0.3.58/32
                via M, 20.180.182.180, swap 900358
                 payload autoDecide, ttlMode uniform, apply egress-acl
                 interface Ethernet2
 IP    20360    [1], 100.0.3.60/32
                via M, 20.180.182.180, swap 900360
                 payload autoDecide, ttlMode uniform, apply egress-acl
                 interface Ethernet2
 IP    20379    [1], 100.0.37.9/32
                via M, 20.180.182.180, swap 900379
                 payload autoDecide, ttlMode uniform, apply egress-acl
                 interface Ethernet2
 IA    362144   [1]
                via M, 20.180.182.180, pop
                 payload autoDecide, ttlMode uniform, apply egress-acl
                 interface Ethernet2
 B3    378528   [0]
                via I, ipv4, vrf tenant-a
 B2    1036782  [0]
                via AF, control word present
                     dot1q   vlan
                    | 2303 | 2303 |
                    | 2304 | 2304 |
 B2    1041343  [0]
                via ES, Port-Channel100
 B2    1041533  [0]
                via V, vlan2301, control word present
 B2    1041763  [0]
                via VF, vlan2302, control word present
 B2    1042318  [0]
                via VA, control word present
                     dot1q   vlan
                    | 2303 | 2303 |
                    | 2304 | 2304 |
 B2    1045184  [0]
                via V, vlan2302, control word present
 B2    1047448  [0]
                via VF, vlan2301, control word present
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
Router identifier 100.0.0.182, local AS number 64512
Route status codes: * - valid, > - active, S - Stale, E - ECMP head, e - ECMP
                    c - Contributing to ECMP, % - Pending best path selection
Origin codes: i - IGP, e - EGP, ? - incomplete
AS Path Attributes: Or-ID - Originator ID, C-LST - Cluster List, LL Nexthop - Link Local Nexthop

          Network                Next Hop              Metric  LocPref Weight  Path
 * >Ec    RD: 100.0.0.56:4556 auto-discovery 56 0000:0000:0000:0000:0000
                                 100.0.0.56            -       100     0       i Or-ID: 100.0.0.56 C-LST: 100.0.0.180 
 *  ec    RD: 100.0.0.56:4556 auto-discovery 56 0000:0000:0000:0000:0000
                                 100.0.0.56            -       100     0       i Or-ID: 100.0.0.56 C-LST: 100.0.3.58 
 * >      RD: 100.0.0.182:2301 auto-discovery 0 0000:0000:0000:0123:0123
                                 -                     -       -       0       i
 * >      RD: 100.0.0.182:2302 auto-discovery 0 0000:0000:0000:0123:0123
                                 -                     -       -       0       i
 * >      RD: 100.0.0.182:2303 auto-discovery 0 0000:0000:0000:0123:0123
                                 -                     -       -       0       i
 * >      RD: 100.0.0.182:1 auto-discovery 0000:0000:0000:0123:0123
                                 -                     -       -       0       i
 * >      RD: 100.0.3.41:3311 auto-discovery 0 0000:0000:0000:0183:0184
                                 100.0.3.41            -       100     0       i Or-ID: 100.0.0.184 C-LST: 100.0.0.180 100.0.3.41 
   %      RD: 100.0.0.183:3301 auto-discovery 0 0000:00d1:0000:0000:00d1
                                 100.0.0.183           -       100     0       i Or-ID: 100.0.0.183 C-LST: 100.0.0.180 
   %      RD: 100.0.0.183:3302 auto-discovery 0 0000:00d1:0000:0000:00d1
                                 100.0.0.183           -       100     0       i Or-ID: 100.0.0.183 C-LST: 100.0.0.180 
   %      RD: 100.0.3.41:3311 auto-discovery 0 0000:00d1:0000:0000:00d1
                                 100.0.3.41            -       100     0       i Or-ID: 100.0.3.41 C-LST: 100.0.0.180 
   %      RD: 100.0.3.41:3312 auto-discovery 0 0000:00d1:0000:0000:00d1
                                 100.0.3.41            -       100     0       i Or-ID: 100.0.3.41 C-LST: 100.0.0.180 
   %      RD: 100.0.0.183:1 auto-discovery 0000:00d1:0000:0000:00d1
                                 100.0.0.183           -       100     0       i Or-ID: 100.0.0.183 C-LST: 100.0.0.180 
   %      RD: 100.0.3.41:2 auto-discovery 0000:00d1:0000:0000:00d1
                                 100.0.3.41            -       100     0       i Or-ID: 100.0.3.41 C-LST: 100.0.0.180 
 * >Ec    RD: 100.0.0.56:4558 auto-discovery 0 0048:5648:5648:5648:5648
                                 100.0.0.56            -       100     0       i Or-ID: 100.0.0.56 C-LST: 100.0.0.180 
 *  ec    RD: 100.0.0.56:4558 auto-discovery 0 0048:5648:5648:5648:5648
                                 100.0.0.56            -       100     0       i Or-ID: 100.0.0.56 C-LST: 100.0.3.58 
 * >Ec    RD: 100.0.0.56:4558 auto-discovery 0048:5648:5648:5648:5648
                                 100.0.0.56            -       100     0       i Or-ID: 100.0.0.56 C-LST: 100.0.0.180 
 *  ec    RD: 100.0.0.56:4558 auto-discovery 0048:5648:5648:5648:5648
                                 100.0.0.56            -       100     0       i Or-ID: 100.0.0.56 C-LST: 100.0.3.58 
   %      RD: 100.0.0.181:3301 mac-ip 0000.0181.0181
                                 100.0.0.181           -       100     0       i Or-ID: 100.0.0.181 C-LST: 100.0.0.180 
   %      RD: 100.0.0.183:3301 mac-ip 0000.0184.0184
                                 100.0.0.183           -       100     0       i Or-ID: 100.0.0.183 C-LST: 100.0.0.180 
 * >      RD: 100.0.3.41:3311 mac-ip 0000.0184.0184
                                 100.0.3.41            -       100     0       i Or-ID: 100.0.0.184 C-LST: 100.0.0.180 100.0.3.41 
   %      RD: 100.0.0.183:3301 mac-ip 0018.6380.ef68
                                 100.0.0.183           -       100     0       i Or-ID: 100.0.0.183 C-LST: 100.0.0.180 
 * >      RD: 100.0.3.41:3311 mac-ip 0018.6380.ef68
                                 100.0.3.41            -       100     0       i Or-ID: 100.0.0.184 C-LST: 100.0.0.180 100.0.3.41 
 * >Ec    RD: 100.0.30.9:2301 mac-ip 001b.0100.0002
                                 100.0.30.9            -       100     0       i Or-ID: 100.0.30.9 C-LST: 100.0.0.180 
 *  ec    RD: 100.0.30.9:2301 mac-ip 001b.0100.0002
                                 100.0.30.9            -       100     0       i Or-ID: 100.0.30.9 C-LST: 100.0.3.58 
 * >Ec    RD: 100.0.0.56:2056 mac-ip 0056.5656.5656 20.10.56.253
                                 100.0.0.56            -       100     0       i Or-ID: 100.0.0.56 C-LST: 100.0.0.180 
 *  ec    RD: 100.0.0.56:2056 mac-ip 0056.5656.5656 20.10.56.253
                                 100.0.0.56            -       100     0       i Or-ID: 100.0.0.56 C-LST: 100.0.3.58 
 * >Ec    RD: 100.0.0.56:2301 mac-ip 0056.5656.5656 20.30.1.254
                                 100.0.0.56            -       100     0       i Or-ID: 100.0.0.56 C-LST: 100.0.0.180 
 *  ec    RD: 100.0.0.56:2301 mac-ip 0056.5656.5656 20.30.1.254
                                 100.0.0.56            -       100     0       i Or-ID: 100.0.0.56 C-LST: 100.0.3.58 
 * >Ec    RD: 100.0.0.56:2302 mac-ip 0056.5656.5656 20.30.2.254
                                 100.0.0.56            -       100     0       i Or-ID: 100.0.0.56 C-LST: 100.0.0.180 
 *  ec    RD: 100.0.0.56:2302 mac-ip 0056.5656.5656 20.30.2.254
                                 100.0.0.56            -       100     0       i Or-ID: 100.0.0.56 C-LST: 100.0.3.58 
 * >Ec    RD: 100.0.0.56:2056 mac-ip 00aa.aaaa.aaaa 20.10.56.254
                                 100.0.0.56            -       100     0       i Or-ID: 100.0.0.56 C-LST: 100.0.0.180 
 *  ec    RD: 100.0.0.56:2056 mac-ip 00aa.aaaa.aaaa 20.10.56.254
                                 100.0.0.56            -       100     0       i Or-ID: 100.0.0.56 C-LST: 100.0.3.58 
 * >Ec    RD: 100.0.0.56:2301 mac-ip 00aa.aaaa.aaaa 20.30.1.254
                                 100.0.0.56            -       100     0       i Or-ID: 100.0.0.56 C-LST: 100.0.0.180 
 *  ec    RD: 100.0.0.56:2301 mac-ip 00aa.aaaa.aaaa 20.30.1.254
                                 100.0.0.56            -       100     0       i Or-ID: 100.0.0.56 C-LST: 100.0.3.58 
 * >Ec    RD: 100.0.0.56:2302 mac-ip 00aa.aaaa.aaaa 20.30.2.254
                                 100.0.0.56            -       100     0       i Or-ID: 100.0.0.56 C-LST: 100.0.0.180 
 *  ec    RD: 100.0.0.56:2302 mac-ip 00aa.aaaa.aaaa 20.30.2.254
                                 100.0.0.56            -       100     0       i Or-ID: 100.0.0.56 C-LST: 100.0.3.58 
   %      RD: 100.0.0.183:3301 mac-ip b0aa.fb45.eeee
                                 100.0.0.183           -       100     0       i Or-ID: 100.0.0.183 C-LST: 100.0.0.180 
 * >      RD: 100.0.3.41:3311 mac-ip b0aa.fb45.eeee
                                 100.0.3.41            -       100     0       i Or-ID: 100.0.0.184 C-LST: 100.0.0.180 100.0.3.41 
 * >Ec    RD: 100.0.0.56:2303 mac-ip 2303 0056.5656.5656 20.30.3.254
                                 100.0.0.56            -       100     0       i Or-ID: 100.0.0.56 C-LST: 100.0.0.180 
 *  ec    RD: 100.0.0.56:2303 mac-ip 2303 0056.5656.5656 20.30.3.254
                                 100.0.0.56            -       100     0       i Or-ID: 100.0.0.56 C-LST: 100.0.3.58 
 * >Ec    RD: 100.0.0.56:2303 mac-ip 2303 00aa.aaaa.aaaa 20.30.3.254
                                 100.0.0.56            -       100     0       i Or-ID: 100.0.0.56 C-LST: 100.0.0.180 
 *  ec    RD: 100.0.0.56:2303 mac-ip 2303 00aa.aaaa.aaaa 20.30.3.254
                                 100.0.0.56            -       100     0       i Or-ID: 100.0.0.56 C-LST: 100.0.3.58 
 * >Ec    RD: 100.0.0.56:2304 mac-ip 2304 0056.5656.5656 20.30.4.254
                                 100.0.0.56            -       100     0       i Or-ID: 100.0.0.56 C-LST: 100.0.0.180 
 *  ec    RD: 100.0.0.56:2304 mac-ip 2304 0056.5656.5656 20.30.4.254
                                 100.0.0.56            -       100     0       i Or-ID: 100.0.0.56 C-LST: 100.0.3.58 
 * >Ec    RD: 100.0.0.56:2304 mac-ip 2304 00aa.aaaa.aaaa 20.30.4.254
                                 100.0.0.56            -       100     0       i Or-ID: 100.0.0.56 C-LST: 100.0.0.180 
 *  ec    RD: 100.0.0.56:2304 mac-ip 2304 00aa.aaaa.aaaa 20.30.4.254
                                 100.0.0.56            -       100     0       i Or-ID: 100.0.0.56 C-LST: 100.0.3.58 
 * >Ec    RD: 100.0.0.3:1 imet 100.0.0.3
                                 100.0.0.3             -       100     0       i Or-ID: 100.0.0.3 C-LST: 100.0.0.180 
 *  ec    RD: 100.0.0.3:1 imet 100.0.0.3
                                 100.0.0.3             -       100     0       i Or-ID: 100.0.0.3 C-LST: 100.0.3.58 
 * >Ec    RD: 100.0.0.26:2026 imet 100.0.0.26
                                 100.0.0.26            0       100     0       i Or-ID: 100.0.0.26 C-LST: 100.0.0.180 
 *  ec    RD: 100.0.0.26:2026 imet 100.0.0.26
                                 100.0.0.26            0       100     0       i Or-ID: 100.0.0.26 C-LST: 100.0.3.58 
 * >Ec    RD: 100.0.0.26:2301 imet 100.0.0.26
                                 100.0.0.26            0       100     0       i Or-ID: 100.0.0.26 C-LST: 100.0.0.180 
 *  ec    RD: 100.0.0.26:2301 imet 100.0.0.26
                                 100.0.0.26            0       100     0       i Or-ID: 100.0.0.26 C-LST: 100.0.3.58 
 * >Ec    RD: 100.0.0.26:2302 imet 100.0.0.26
                                 100.0.0.26            0       100     0       i Or-ID: 100.0.0.26 C-LST: 100.0.0.180 
 *  ec    RD: 100.0.0.26:2302 imet 100.0.0.26
                                 100.0.0.26            0       100     0       i Or-ID: 100.0.0.26 C-LST: 100.0.3.58 
 * >Ec    RD: 100.0.0.31:2301 imet 100.0.0.31
                                 100.0.0.31            -       100     0       ? Or-ID: 100.0.0.31 C-LST: 100.0.0.180 
 *  ec    RD: 100.0.0.31:2301 imet 100.0.0.31
                                 100.0.0.31            -       100     0       ? Or-ID: 100.0.0.31 C-LST: 100.0.3.58 
 * >      RD: 100.0.0.34:2301 imet 100.0.0.34
                                 100.0.0.34            -       100     0       i Or-ID: 100.0.0.34 C-LST: 100.0.0.180 
 * >Ec    RD: 100.0.0.56:2056 imet 100.0.0.56
                                 100.0.0.56            -       100     0       i Or-ID: 100.0.0.56 C-LST: 100.0.0.180 
 *  ec    RD: 100.0.0.56:2056 imet 100.0.0.56
                                 100.0.0.56            -       100     0       i Or-ID: 100.0.0.56 C-LST: 100.0.3.58 
 * >Ec    RD: 100.0.0.56:2301 imet 100.0.0.56
                                 100.0.0.56            -       100     0       i Or-ID: 100.0.0.56 C-LST: 100.0.0.180 
 *  ec    RD: 100.0.0.56:2301 imet 100.0.0.56
                                 100.0.0.56            -       100     0       i Or-ID: 100.0.0.56 C-LST: 100.0.3.58 
 * >Ec    RD: 100.0.0.56:2302 imet 100.0.0.56
                                 100.0.0.56            -       100     0       i Or-ID: 100.0.0.56 C-LST: 100.0.0.180 
 *  ec    RD: 100.0.0.56:2302 imet 100.0.0.56
                                 100.0.0.56            -       100     0       i Or-ID: 100.0.0.56 C-LST: 100.0.3.58 
 * >Ec    RD: 100.0.0.56:4557 imet 100.0.0.56
                                 100.0.0.56            -       100     0       i Or-ID: 100.0.0.56 C-LST: 100.0.0.180 
 *  ec    RD: 100.0.0.56:4557 imet 100.0.0.56
                                 100.0.0.56            -       100     0       i Or-ID: 100.0.0.56 C-LST: 100.0.3.58 
 * >Ec    RD: 100.0.0.56:4558 imet 100.0.0.56
                                 100.0.0.56            -       100     0       i Or-ID: 100.0.0.56 C-LST: 100.0.0.180 
 *  ec    RD: 100.0.0.56:4558 imet 100.0.0.56
                                 100.0.0.56            -       100     0       i Or-ID: 100.0.0.56 C-LST: 100.0.3.58 
   %      RD: 100.0.0.181:3301 imet 100.0.0.181
                                 100.0.0.181           -       100     0       i Or-ID: 100.0.0.181 C-LST: 100.0.0.180 
   %      RD: 100.0.0.181:3302 imet 100.0.0.181
                                 100.0.0.181           -       100     0       i Or-ID: 100.0.0.181 C-LST: 100.0.0.180 
 * >      RD: 100.0.0.182:2301 imet 100.0.0.182
                                 -                     -       -       0       i
 * >      RD: 100.0.0.182:2302 imet 100.0.0.182
                                 -                     -       -       0       i
   %      RD: 100.0.0.183:3301 imet 100.0.0.183
                                 100.0.0.183           -       100     0       i Or-ID: 100.0.0.183 C-LST: 100.0.0.180 
   %      RD: 100.0.0.183:3302 imet 100.0.0.183
                                 100.0.0.183           -       100     0       i Or-ID: 100.0.0.183 C-LST: 100.0.0.180 
   %      RD: 100.0.3.41:3311 imet 100.0.3.41
                                 100.0.3.41            -       100     0       i Or-ID: 100.0.3.41 C-LST: 100.0.0.180 
   %      RD: 100.0.3.41:3312 imet 100.0.3.41
                                 100.0.3.41            -       100     0       i Or-ID: 100.0.3.41 C-LST: 100.0.0.180 
 * >Ec    RD: 100.0.30.9:2301 imet 100.0.30.9
                                 100.0.30.9            -       100     0       i Or-ID: 100.0.30.9 C-LST: 100.0.0.180 
 *  ec    RD: 100.0.30.9:2301 imet 100.0.30.9
                                 100.0.30.9            -       100     0       i Or-ID: 100.0.30.9 C-LST: 100.0.3.58 
 * >Ec    RD: 100.0.0.26:2303 imet 2303 100.0.0.26
                                 100.0.0.26            0       100     0       i Or-ID: 100.0.0.26 C-LST: 100.0.0.180 
 *  ec    RD: 100.0.0.26:2303 imet 2303 100.0.0.26
                                 100.0.0.26            0       100     0       i Or-ID: 100.0.0.26 C-LST: 100.0.3.58 
 * >Ec    RD: 100.0.0.56:2303 imet 2303 100.0.0.56
                                 100.0.0.56            -       100     0       i Or-ID: 100.0.0.56 C-LST: 100.0.0.180 
 *  ec    RD: 100.0.0.56:2303 imet 2303 100.0.0.56
                                 100.0.0.56            -       100     0       i Or-ID: 100.0.0.56 C-LST: 100.0.3.58 
 * >      RD: 100.0.0.182:2303 imet 2303 100.0.0.182
                                 -                     -       -       0       i
 * >Ec    RD: 100.0.0.26:2304 imet 2304 100.0.0.26
                                 100.0.0.26            0       100     0       i Or-ID: 100.0.0.26 C-LST: 100.0.0.180 
 *  ec    RD: 100.0.0.26:2304 imet 2304 100.0.0.26
                                 100.0.0.26            0       100     0       i Or-ID: 100.0.0.26 C-LST: 100.0.3.58 
 * >Ec    RD: 100.0.0.56:2304 imet 2304 100.0.0.56
                                 100.0.0.56            -       100     0       i Or-ID: 100.0.0.56 C-LST: 100.0.0.180 
 *  ec    RD: 100.0.0.56:2304 imet 2304 100.0.0.56
                                 100.0.0.56            -       100     0       i Or-ID: 100.0.0.56 C-LST: 100.0.3.58 
 * >      RD: 100.0.0.182:2303 imet 2304 100.0.0.182
                                 -                     -       -       0       i
 * >      RD: 100.0.0.182:1 ethernet-segment 0000:0000:0000:0123:0123 100.0.0.182
                                 -                     -       -       0       i
   %      RD: 100.0.0.183:1 ethernet-segment 0000:00d1:0000:0000:00d1 100.0.0.183
                                 100.0.0.183           -       100     0       i Or-ID: 100.0.0.183 C-LST: 100.0.0.180 
 * >      RD: 100.0.3.41:0 ethernet-segment 0000:00d1:0000:0000:00d1 100.0.3.41
                                 100.0.3.41            -       100     0       i Or-ID: 100.0.3.41 C-LST: 100.0.0.180 
 * >Ec    RD: 100.0.0.56:0 ethernet-segment 0048:5648:5648:5648:5648 100.0.0.56
                                 100.0.0.56            -       100     0       i Or-ID: 100.0.0.56 C-LST: 100.0.0.180 
 *  ec    RD: 100.0.0.56:0 ethernet-segment 0048:5648:5648:5648:5648 100.0.0.56
                                 100.0.0.56            -       100     0       i Or-ID: 100.0.0.56 C-LST: 100.0.3.58 
 * >Ec    RD: 100.0.0.56:2000 ip-prefix 20.10.56.0/24
                                 100.0.0.56            -       100     0       i Or-ID: 100.0.0.56 C-LST: 100.0.0.180 
 *  ec    RD: 100.0.0.56:2000 ip-prefix 20.10.56.0/24
                                 100.0.0.56            -       100     0       i Or-ID: 100.0.0.56 C-LST: 100.0.3.58 
 * >Ec    RD: 100.0.0.56:2000 ip-prefix 20.30.1.0/24
                                 100.0.0.56            -       100     0       i Or-ID: 100.0.0.56 C-LST: 100.0.0.180 
 *  ec    RD: 100.0.0.56:2000 ip-prefix 20.30.1.0/24
                                 100.0.0.56            -       100     0       i Or-ID: 100.0.0.56 C-LST: 100.0.3.58 
 * >Ec    RD: 100.0.0.56:2000 ip-prefix 20.30.2.0/24
                                 100.0.0.56            -       100     0       i Or-ID: 100.0.0.56 C-LST: 100.0.0.180 
 *  ec    RD: 100.0.0.56:2000 ip-prefix 20.30.2.0/24
                                 100.0.0.56            -       100     0       i Or-ID: 100.0.0.56 C-LST: 100.0.3.58 
 * >      RD: 100.0.0.182:2000 ip-prefix 20.30.2.0/24
                                 -                     -       -       0       i
 * >Ec    RD: 100.0.0.56:2000 ip-prefix 20.30.3.0/24
                                 100.0.0.56            -       100     0       i Or-ID: 100.0.0.56 C-LST: 100.0.0.180 
 *  ec    RD: 100.0.0.56:2000 ip-prefix 20.30.3.0/24
                                 100.0.0.56            -       100     0       i Or-ID: 100.0.0.56 C-LST: 100.0.3.58 
 * >      RD: 100.0.0.182:2000 ip-prefix 20.30.3.0/24
                                 -                     -       -       0       i
 * >Ec    RD: 100.0.0.56:2000 ip-prefix 20.30.4.0/24
                                 100.0.0.56            -       100     0       i Or-ID: 100.0.0.56 C-LST: 100.0.0.180 
 *  ec    RD: 100.0.0.56:2000 ip-prefix 20.30.4.0/24
                                 100.0.0.56            -       100     0       i Or-ID: 100.0.0.56 C-LST: 100.0.3.58 
 * >      RD: 100.0.0.182:2000 ip-prefix 20.30.4.0/24
                                 -                     -       -       0       i
   %      RD: 100.0.0.181:1023 ip-prefix 30.30.1.0/24
                                 100.0.0.181           -       100     0       i Or-ID: 100.0.0.181 C-LST: 100.0.0.180 
   %      RD: 100.0.0.181:1023 ip-prefix 30.30.2.0/24
                                 100.0.0.181           -       100     0       i Or-ID: 100.0.0.181 C-LST: 100.0.0.180 
```

## show bgp vpn-ipv4

```text
BGP routing table information for VRF default
Router identifier 100.0.0.182, local AS number 64512
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
Router identifier 100.0.0.182, local AS number 64512
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
Router identifier 100.0.0.182, local AS number 64512
Route status codes: s - suppressed contributor, * - valid, > - active, E - ECMP head, e - ECMP
                    S - Stale, c - Contributing to ECMP, b - backup, L - labeled-unicast
                    % - Pending best path selection
Origin codes: i - IGP, e - EGP, ? - incomplete
AS Path Attributes: Or-ID - Originator ID, C-LST - Cluster List, LL Nexthop - Link Local Nexthop

          Network                Next Hop              Metric  AIGP       LocPref Weight  Path
```

## show bgp neighbors

```text
BGP neighbor is 100.0.0.180, remote AS 64512, internal link
 Description: RR_ANET
  BGP version 4, remote router ID 100.0.0.180, VRF default
  Inherits configuration from and member of peer-group RR_EVPN
  Last read 00:00:44, last write 00:00:41
  Hold time is 180, keepalive interval is 60 seconds
  Configured hold time is 180, keepalive interval is 60 seconds
  Effective minimum hold time is 3 seconds
  Send failure hold time is 0 seconds
  Hold timer is active, time left: 00:02:16
  Keepalive timer is active, time left: 00:00:09
  Connect timer is inactive
  Idle-restart timer is inactive
  BGP state is Established, up for 04:06:52
  Number of transitions to established: 1
  Last state was OpenConfirm
  Last event was RecvUpdate
  Types of communities advertised: extended
  Enhanced route refresh stale path removal disabled
  Outbound enhanced route refresh enabled
  Neighbor Capabilities:
    Multiprotocol L2VPN EVPN: advertised and received and negotiated
    Four Octet ASN: advertised and received and negotiated
    Route Refresh: advertised and received and negotiated
    Enhanced route refresh: advertised and received and negotiated
    Send End-of-RIB messages: advertised and received and negotiated
    Additional-paths recv capability:
      L2VPN EVPN: negotiated
    Additional-paths send capability:
      L2VPN EVPN: received
  Restart timer is inactive
  End of rib timer is inactive
    L2VPN EVPN End-of-RIB received: Yes
      Received 04:06:52
      Number of stale paths removed after graceful restart: 0
  AIGP attribute send and receive for IPv4 Unicast are enabled
  AIGP attribute send and receive for IPv4 with MPLS Labels are enabled
  AIGP attribute send and receive for IPv6 Unicast are enabled
  AIGP attribute send and receive for IPv6 with MPLS Labels are enabled
  BGP session driven failover for IPv6 Unicast is disabled
  BGP session driven failover for IPv4 Unicast is disabled
  Message Statistics:
                                  Sent      Rcvd
    Opens:                           1         1
    Notifications:                   0         0
    Updates:                        70       521
    Keepalives:                    275       226
    Enhanced Route Refresh:          0         0
    Begin of Route Refresh:          0         0
    End of Route Refresh:            0         0
    Total messages:                346       748
  Prefix Statistics:
                                   Sent      Rcvd     Best Paths     Best ECMP Paths
    IPv4 Unicast:                     0         0              0                   0
    IPv6 Unicast:                     0         0              0                   0
    EVPN:                            12        60             41                  35
  Configured maximum total number of routes is 12000
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
    L2VPN EVPN NLRIs dropped due to maximum route limit violation: 0
    Link-state NLRIs dropped because reception is unsupported: 0
    RT Membership NLRIs dropped due to local origin ASN received from external peer: 0
  Outbound paths dropped by reason:
    IPv4 local address not available: 0
    IPv6 local address not available: 0
Local AS is 64512, local router ID 100.0.0.182
TTL is 255
Local TCP address is 100.0.0.182, local port is 44383
Remote TCP address is 100.0.0.180, remote port is 179
Local next hop for next hop self:
  L2VPN EVPN: 100.0.0.182
TCP Socket Information:
  TCP state is ESTABLISHED
  Recv-Q: 0/32768
  Send-Q: 0/332800
  Outgoing Maximum Segment Size (MSS): 8948
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
    TCP Throughput: 2898.14 Mbps
    Recv Round-trip Time (rcv_rtt): 1.0ms
    Advertised Recv Window (rcv_space): 56588

BGP neighbor is 100.0.3.58, remote AS 64512, internal link
 Description: RR_Cisco
  BGP version 4, remote router ID 100.0.3.58, VRF default
  Inherits configuration from and member of peer-group RR_EVPN
  Last read 00:00:21, last write 00:00:40
  Hold time is 180, keepalive interval is 60 seconds
  Configured hold time is 180, keepalive interval is 60 seconds
  Effective minimum hold time is 3 seconds
  Send failure hold time is 0 seconds
  Hold timer is active, time left: 00:02:39
  Keepalive timer is active, time left: 00:00:05
  Connect timer is inactive
  Idle-restart timer is inactive
  BGP state is Established, up for 04:06:52
  Number of transitions to established: 1
  Last state was OpenConfirm
  Last event was RecvKeepAlive
  Types of communities advertised: extended
  Neighbor Capabilities:
    Multiprotocol VPN-IPv4: received
    Multiprotocol L2VPN EVPN: advertised and received and negotiated
    Four Octet ASN: advertised and received and negotiated
    Route Refresh: advertised and received and negotiated
    Enhanced route refresh: advertised
    Send End-of-RIB messages: advertised
    Additional-paths recv capability:
      L2VPN EVPN: advertised
    Additional-paths send capability:
    Extended Next-Hop Capability:
      IPv4 Unicast: received
      VPN-IPv4: received
  Restart timer is inactive
  End of rib timer is inactive
    L2VPN EVPN End-of-RIB received: No
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
    Updates:               70       399
    Keepalives:           274       207
    Route Refresh:          0         0
    Total messages:       345       607
  Prefix Statistics:
                                   Sent      Rcvd     Best Paths     Best ECMP Paths
    IPv4 Unicast:                     0         0              0                   0
    IPv6 Unicast:                     0         0              0                   0
    EVPN:                            12        35             35                   0
  Configured maximum total number of routes is 12000
  Inbound updates dropped by reason:
    AS path loop detection: 0
    Cluster ID loop detection: 0
    Enforced First AS: 0
    Malformed MPBGP routes: 0
    Originator ID matches local router ID: 0
    Nexthop matches local IP address: 44
    Unexpected IPv6 nexthop for IPv4 routes: 0
  Inbound updates with attribute errors:
    Resulting in removal of all paths in update (treat as withdraw): 44
    Resulting in AFI/SAFI disable: 0
    Resulting in attribute ignore: 0
    Disabled AFI/SAFIs: None
    Last treat-as-withdraw attribute error: Nexthop is local address
    Last update with error received at: 01:01:21
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
    L2VPN EVPN NLRIs dropped due to maximum route limit violation: 0
    Link-state NLRIs dropped because reception is unsupported: 0
    RT Membership NLRIs dropped due to local origin ASN received from external peer: 0
  Outbound paths dropped by reason:
    IPv4 local address not available: 0
    IPv6 local address not available: 0
Local AS is 64512, local router ID 100.0.0.182
TTL is 255
Local TCP address is 100.0.0.182, local port is 36323
Remote TCP address is 100.0.3.58, remote port is 179
Local next hop for next hop self:
  L2VPN EVPN: 100.0.0.182
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
    Round-trip Time (rtt/rtvar): 201.3ms/0.6ms
    Delayed Ack Timeout (ato): 40.0ms
    Congestion Window (cwnd): 4
    Slow-start Threshold (ssthresh): 7
    TCP Throughput: 0.20 Mbps
    Recv Round-trip Time (rcv_rtt): 184539.0ms
    Advertised Recv Window (rcv_space): 61770

```

## show tunnel rib system-tunnel-rib brief

```text
Tunnel RIB: system-tunnel-rib
Endpoint        Tunnel Type     Index(es)   Tunnel Preference   IGP Preference 
--------------- -------------- ----------- ------------------- ----------------
10.0.0.59/32    IS-IS SR IPv4   18          30                  115            
100.0.0.3/32    IS-IS SR IPv4   1           30                  115            
100.0.0.21/32   IS-IS SR IPv4   15          30                  115            
100.0.0.26/32   IS-IS SR IPv4   7           30                  115            
100.0.0.31/32   IS-IS SR IPv4   13          30                  115            
100.0.0.34/32   IS-IS SR IPv4   8           30                  115            
100.0.0.56/32   IS-IS SR IPv4   9           30                  115            
100.0.0.161/32  IS-IS SR IPv4   17          30                  115            
100.0.0.181/32  IS-IS SR IPv4   2           30                  115            
100.0.0.183/32  IS-IS SR IPv4   6           30                  115            
100.0.0.184/32  IS-IS SR IPv4   16          30                  115            
100.0.3.41/32   IS-IS SR IPv4   10          30                  115            
100.0.3.45/32   IS-IS SR IPv4   3           30                  115            
100.0.3.58/32   IS-IS SR IPv4   14          30                  115            
100.0.3.60/32   IS-IS SR IPv4   5           30                  115            
100.0.30.9/32   IS-IS SR IPv4   11          30                  115            
100.0.37.9/32   IS-IS SR IPv4   4           30                  115            

   IGP Metric    Metric Type
---------------- -----------
   70            metric     
   30            metric     
   20            metric     
   20            metric     
   20            metric     
   20            metric     
   20            metric     
   30            metric     
   30            metric     
   20            metric     
   20            metric     
   30            metric     
   30            metric     
   30            metric     
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
>C    20.149.172.0/24 [0 pref/0 metric] updated 1d22h ago
         via Ethernet25, directly connected
>C    20.170.172.0/24 [0 pref/0 metric] updated 1d04h ago
         via Ethernet52/1, directly connected
>C    20.180.182.0/24 [0 pref/0 metric] updated 04:11:14 ago
         via Ethernet2, directly connected
>C    100.0.0.182/32 [0 pref/0 metric] updated 04:09:45 ago
         via Loopback0, directly connected
>C    209.209.209.209/32 [0 pref/0 metric] updated 1d22h ago
         via Loopback209, directly connected
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
>I    10.0.0.58/32 [115 pref/90 metric] updated 02:51:46 ago
         via 20.180.182.180, Ethernet2
>I    10.0.0.59/32 [115 pref/70 metric] updated 02:51:46 ago
         via 20.180.182.180, Ethernet2
>I    10.0.1.36/32 [115 pref/70 metric] updated 02:51:46 ago
         via 20.180.182.180, Ethernet2
>I    20.3.180.0/24 [115 pref/20 metric] updated 04:10:19 ago
         via 20.180.182.180, Ethernet2
>I    20.21.180.0/24 [115 pref/20 metric] updated 02:19:49 ago
         via 20.180.182.180, Ethernet2
>I    20.26.180.0/24 [115 pref/20 metric] updated 04:10:19 ago
         via 20.180.182.180, Ethernet2
>I    20.31.180.0/24 [115 pref/20 metric] updated 04:10:19 ago
         via 20.180.182.180, Ethernet2
>I    20.34.180.0/24 [115 pref/20 metric] updated 02:22:43 ago
         via 20.180.182.180, Ethernet2
>I    20.56.180.0/24 [115 pref/20 metric] updated 04:10:19 ago
         via 20.180.182.180, Ethernet2
>I    20.161.180.0/24 [115 pref/20 metric] updated 03:08:23 ago
         via 20.180.182.180, Ethernet2
>I    20.180.181.0/24 [115 pref/20 metric] updated 04:10:19 ago
         via 20.180.182.180, Ethernet2
>I    20.180.183.0/24 [115 pref/20 metric] updated 02:10:57 ago
         via 20.180.182.180, Ethernet2
>I    20.180.184.0/24 [115 pref/20 metric] updated 04:10:19 ago
         via 20.180.182.180, Ethernet2
>I    30.9.180.0/24 [115 pref/20 metric] updated 04:10:19 ago
         via 20.180.182.180, Ethernet2
>I    30.14.180.0/24 [115 pref/20 metric] updated 04:10:19 ago
         via 20.180.182.180, Ethernet2
>I    30.41.180.0/24 [115 pref/20 metric] updated 04:10:19 ago
         via 20.180.182.180, Ethernet2
>I    30.45.180.0/24 [115 pref/20 metric] updated 04:10:19 ago
         via 20.180.182.180, Ethernet2
>I    30.58.180.0/24 [115 pref/20 metric] updated 04:10:19 ago
         via 20.180.182.180, Ethernet2
>I    30.60.180.0/24 [115 pref/20 metric] updated 04:10:19 ago
         via 20.180.182.180, Ethernet2
>I    30.79.180.0/24 [115 pref/20 metric] updated 03:29:25 ago
         via 20.180.182.180, Ethernet2
>I    100.0.0.3/32 [115 pref/30 metric] updated 04:10:19 ago
         via 20.180.182.180, Ethernet2
>I    100.0.0.21/32 [115 pref/20 metric] updated 02:19:49 ago
         via 20.180.182.180, Ethernet2
>I    100.0.0.26/32 [115 pref/20 metric] updated 04:10:19 ago
         via 20.180.182.180, Ethernet2
>I    100.0.0.31/32 [115 pref/20 metric] updated 04:10:19 ago
         via 20.180.182.180, Ethernet2
>I    100.0.0.34/32 [115 pref/20 metric] updated 02:22:42 ago
         via 20.180.182.180, Ethernet2
>I    100.0.0.56/32 [115 pref/20 metric] updated 04:10:19 ago
         via 20.180.182.180, Ethernet2
>I    100.0.0.161/32 [115 pref/30 metric] updated 02:51:46 ago
         via 20.180.182.180, Ethernet2
>I    100.0.0.180/32 [115 pref/10 metric] updated 04:10:19 ago
         via 20.180.182.180, Ethernet2
>I    100.0.0.181/32 [115 pref/30 metric] updated 04:10:19 ago
         via 20.180.182.180, Ethernet2
>I    100.0.0.183/32 [115 pref/20 metric] updated 02:10:48 ago
         via 20.180.182.180, Ethernet2
>I    100.0.0.184/32 [115 pref/20 metric] updated 04:10:19 ago
         via 20.180.182.180, Ethernet2
>I    100.0.3.41/32 [115 pref/30 metric] updated 04:10:19 ago
         via 20.180.182.180, Ethernet2
>I    100.0.3.45/32 [115 pref/30 metric] updated 04:10:19 ago
         via 20.180.182.180, Ethernet2
>I    100.0.3.58/32 [115 pref/30 metric] updated 04:10:19 ago
         via 20.180.182.180, Ethernet2
>I    100.0.3.60/32 [115 pref/30 metric] updated 04:10:19 ago
         via 20.180.182.180, Ethernet2
>I    100.0.30.9/32 [115 pref/20 metric] updated 04:10:19 ago
         via 20.180.182.180, Ethernet2
>I    100.0.37.9/32 [115 pref/20 metric] updated 03:29:16 ago
         via 20.180.182.180, Ethernet2
>I    192.168.20.0/23 [115 pref/20 metric] updated 02:19:49 ago
         via 20.180.182.180, Ethernet2
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
>P    ::/96 [1 pref/0 metric] updated 04:05:32 ago
         via Null0, directly connected [NF]
>P    ::ffff:127.0.0.0/104 [1 pref/0 metric] updated 04:05:32 ago
         via :: [1 pref/1 metric] type ipv6
            via , directly connected
>P    fe80::/10 [1 pref/0 metric] updated 04:05:32 ago
```

## show platform sand l3 summary

```text
Number of vrfs: 9

Ipv4:
  Routes:       88  backlog:  0  unprogrammed:  0
  Adjacencies:  85  backlog:  0  unprogrammed:  0
Ipv6:
  Routes:       4   backlog:  0  unprogrammed:  0
  Adjacencies:  85  backlog:  0  unprogrammed:  0
Mpls:
  Routes:       18  backlog:  0  unprogrammed:  0
  Adjacencies:  18  backlog:  0  unprogrammed:  0

Jericho2 Ip Fecs:
  Non-ecmp fecs:  4118  ecmp fecs:  0  fec entries:  4118
Jericho2 Mpls Fecs:
  Non-ecmp fecs:  18  ecmp fecs:  0  fec entries:  18
Jericho2 Vxlan Tunnel Fecs:
  Non-ecmp fecs:  0  ecmp fecs:  0  fec entries:  0
  Number of vxlan tunnels configured: 0

Jericho2 Lpm Routes:
  Routes:   88  unprogrammed:   0   
  Routes6:  4   unprogrammed6:  0   
  Backlog:  0 

Jericho2 Lpm:
  TCAM entries used:   3   Percent free:  99  ADS2 entries used:   7  Percent free:  99
  Pivot buckets used:  4   Rows used:     1   Entries Per Bucket:  1  Percent free:  99
  Route buckets used:  16  Rows used:     3   Entries Per Bucket:  5  Percent free:  99

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
  FixedSystem: 12
Egress Mpls (for inner 2 labels) rewrite entries in use (in each fap):
  FixedSystem: 18
Egress Sflow rewrite entries in use (in each fap):
  FixedSystem: 0

Egress rewrite chains in backlog: resource-full 0, no-interface 0

Glem entries used per fap :
  FixedSystem: 4137

Jericho2 Fec:
  Maximum FEC hierarchy levels:  3
  ReusedEcmp:  0  allocs:  1128  frees:  1090  shuffles:  0  cmds:  0
  Zombies:     0    purges:    0
  Quarantine:  0/0  shuffles:  0  deletes:  0   
  Fec insertion failures:  0
  Level1  Fecs:
    Non-ecmp fecs:            12  ecmp fecs:            1 
    Non-ecmp (Percent free):  99  ecmp (Percent free):  99
  Level2  Fecs:
    Non-ecmp fecs:            62  ecmp fecs:            0  
    Non-ecmp (Percent free):  99  ecmp (Percent free):  100
  Level3  Fecs:
    Non-ecmp fecs:            2   ecmp fecs:            0  
    Non-ecmp (Percent free):  99  ecmp (Percent free):  100

Lpm Detail:
  Requests:  4982  cleanses:  1444  batches:  1444  avg batch size:  3

Jericho Arp:
  ArpTable writes:      34877  queued      0   
  IngressTable writes:  90848  queued      0   
  Coprocessors:         1      in CmdRing

Tunnel Counter Status
  Number of MPLS tunnels:                  38   
  Number of uncountable MPLS tunnels:      23   
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
|0  |10.0.0.58/32      |ROUTE| Et2                |1007 |103423  | 44:4c:a8:73:9c:0d |  -  |288374|   -   
|0  |10.0.0.59/32      |ROUTE| Et2                |1007 |103423  | 44:4c:a8:73:9c:0d |  -  |288374|   -   
|0  |10.0.1.36/32      |ROUTE| Et2                |1007 |103423  | 44:4c:a8:73:9c:0d |  -  |288374|   -   
|0  |20.3.180.0/24     |ROUTE| Et2                |1007 |103423  | 44:4c:a8:73:9c:0d |  -  |288374|   -   
|0  |20.21.180.0/24    |ROUTE| Et2                |1007 |103423  | 44:4c:a8:73:9c:0d |  -  |288374|   -   
|0  |20.26.180.0/24    |ROUTE| Et2                |1007 |103423  | 44:4c:a8:73:9c:0d |  -  |288374|   -   
|0  |20.31.180.0/24    |ROUTE| Et2                |1007 |103423  | 44:4c:a8:73:9c:0d |  -  |288374|   -   
|0  |20.34.180.0/24    |ROUTE| Et2                |1007 |103423  | 44:4c:a8:73:9c:0d |  -  |288374|   -   
|0  |20.56.180.0/24    |ROUTE| Et2                |1007 |103423  | 44:4c:a8:73:9c:0d |  -  |288374|   -   
|0  |20.149.172.0/32   |TRAP | CoppSystemIpBcast  |0    |  -     | BcastReceive      |  -  |524288|   -   
|0  |20.149.172.149/32 |ROUTE| Et25               |1011 |103421  | c0:f8:7f:6a:4e:2a |  -  |288368|   -   
|0  |20.149.172.172/32 |TRAP | CoppSystemIpUcast  |0    |  -     | Receive           |  -  |524291|   -   
|0  |20.149.172.255/32 |TRAP | CoppSystemIpBcast  |0    |  -     | BcastReceive      |  -  |524288|   -   
|0  |20.149.172.0/24   |TRAP | CoppSystemL3DstMiss|1011 |1011    | ArpTrap           |  -  |525305|   -   
|0  |20.161.180.0/24   |ROUTE| Et2                |1007 |103423  | 44:4c:a8:73:9c:0d |  -  |288374|   -   
|0  |20.170.172.0/32   |TRAP | CoppSystemIpBcast  |0    |  -     | BcastReceive      |  -  |524288|   -   
|0  |20.170.172.170/32 |ROUTE| Et52/1             |1013 |103422  | 28:99:3a:06:b4:e1 |  -  |288378|   -   
|0  |20.170.172.172/32 |TRAP | CoppSystemIpUcast  |0    |  -     | Receive           |  -  |524291|   -   
|0  |20.170.172.255/32 |TRAP | CoppSystemIpBcast  |0    |  -     | BcastReceive      |  -  |524288|   -   
|0  |20.170.172.0/24   |TRAP | CoppSystemL3DstMiss|1013 |1013    | ArpTrap           |  -  |525307|   -   
|0  |20.180.181.0/24   |ROUTE| Et2                |1007 |103423  | 44:4c:a8:73:9c:0d |  -  |288374|   -   
|0  |20.180.182.0/32   |TRAP | CoppSystemIpBcast  |0    |  -     | BcastReceive      |  -  |524288|   -   
|0  |20.180.182.180/32 |ROUTE| Et2                |1007 |103423  | 44:4c:a8:73:9c:0d |  -  |288364|   -   
|0  |20.180.182.182/32 |TRAP | CoppSystemIpUcast  |0    |  -     | Receive           |  -  |524291|   -   
|0  |20.180.182.255/32 |TRAP | CoppSystemIpBcast  |0    |  -     | BcastReceive      |  -  |524288|   -   
|0  |20.180.182.0/24   |TRAP | CoppSystemL3DstMiss|1007 |1007    | ArpTrap           |  -  |525301|   -   
|0  |20.180.183.0/24   |ROUTE| Et2                |1007 |103423  | 44:4c:a8:73:9c:0d |  -  |288374|   -   
|0  |20.180.184.0/24   |ROUTE| Et2                |1007 |103423  | 44:4c:a8:73:9c:0d |  -  |288374|   -   
|0  |30.9.180.0/24     |ROUTE| Et2                |1007 |103423  | 44:4c:a8:73:9c:0d |  -  |288374|   -   
|0  |30.14.180.0/24    |ROUTE| Et2                |1007 |103423  | 44:4c:a8:73:9c:0d |  -  |288374|   -   
|0  |30.41.180.0/24    |ROUTE| Et2                |1007 |103423  | 44:4c:a8:73:9c:0d |  -  |288374|   -   
|0  |30.45.180.0/24    |ROUTE| Et2                |1007 |103423  | 44:4c:a8:73:9c:0d |  -  |288374|   -   
|0  |30.58.180.0/24    |ROUTE| Et2                |1007 |103423  | 44:4c:a8:73:9c:0d |  -  |288374|   -   
|0  |30.60.180.0/24    |ROUTE| Et2                |1007 |103423  | 44:4c:a8:73:9c:0d |  -  |288374|   -   
|0  |30.79.180.0/24    |ROUTE| Et2                |1007 |103423  | 44:4c:a8:73:9c:0d |  -  |288374|   -   
|0  |100.0.0.3/32      |ROUTE| Et2                |1007 |103423  | 44:4c:a8:73:9c:0d |  -  |288374|   -   
|0  |100.0.0.21/32     |ROUTE| Et2                |1007 |103423  | 44:4c:a8:73:9c:0d |  -  |288374|   -   
|0  |100.0.0.26/32     |ROUTE| Et2                |1007 |103423  | 44:4c:a8:73:9c:0d |  -  |288374|   -   
|0  |100.0.0.31/32     |ROUTE| Et2                |1007 |103423  | 44:4c:a8:73:9c:0d |  -  |288374|   -   
|0  |100.0.0.34/32     |ROUTE| Et2                |1007 |103423  | 44:4c:a8:73:9c:0d |  -  |288374|   -   
|0  |100.0.0.56/32     |ROUTE| Et2                |1007 |103423  | 44:4c:a8:73:9c:0d |  -  |288374|   -   
|0  |100.0.0.161/32    |ROUTE| Et2                |1007 |103423  | 44:4c:a8:73:9c:0d |  -  |288374|   -   
|0  |100.0.0.180/32    |ROUTE| Et2                |1007 |103423  | 44:4c:a8:73:9c:0d |  -  |288374|   -   
|0  |100.0.0.181/32    |ROUTE| Et2                |1007 |103423  | 44:4c:a8:73:9c:0d |  -  |288374|   -   
|0  |100.0.0.182/32    |TRAP | CoppSystemIpUcast  |0    |  -     | Receive           |  -  |524291|   -   
|0  |100.0.0.183/32    |ROUTE| Et2                |1007 |103423  | 44:4c:a8:73:9c:0d |  -  |288374|   -   
|0  |100.0.0.184/32    |ROUTE| Et2                |1007 |103423  | 44:4c:a8:73:9c:0d |  -  |288374|   -   
|0  |100.0.3.41/32     |ROUTE| Et2                |1007 |103423  | 44:4c:a8:73:9c:0d |  -  |288374|   -   
|0  |100.0.3.45/32     |ROUTE| Et2                |1007 |103423  | 44:4c:a8:73:9c:0d |  -  |288374|   -   
|0  |100.0.3.58/32     |ROUTE| Et2                |1007 |103423  | 44:4c:a8:73:9c:0d |  -  |288374|   -   
|0  |100.0.3.60/32     |ROUTE| Et2                |1007 |103423  | 44:4c:a8:73:9c:0d |  -  |288374|   -   
|0  |100.0.30.9/32     |ROUTE| Et2                |1007 |103423  | 44:4c:a8:73:9c:0d |  -  |288374|   -   
|0  |100.0.37.9/32     |ROUTE| Et2                |1007 |103423  | 44:4c:a8:73:9c:0d |  -  |288374|   -   
|0  |127.0.0.0/8       |TRAP | CoppSystemL3DstMiss|0    |  -     | ArpTrap           |  -  |524294|   -   
|0  |192.168.20.0/23   |ROUTE| Et2                |1007 |103423  | 44:4c:a8:73:9c:0d |  -  |288374|   -   
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
|8  |0.0.0.0/8         |DROP | DROP               |0    |  -     |                   |  -  |288362|   -   
|8  |20.10.56.0/24     |ROUTE| FEC 288414         |0    |2097135 | 00:00:00:00:00:00 |  -  |91762 |M 524281
|8  |20.30.1.0/24      |ROUTE| FEC 288414         |0    |2097135 | 00:00:00:00:00:00 |  -  |91762 |M 524281
|8  |20.30.2.0/32      |TRAP | CoppSystemIpBcast  |0    |  -     | BcastReceive      |  -  |524288|   -   
|8  |20.30.2.254/32    |TRAP | CoppSystemIpUcast  |0    |  -     | Receive           |  -  |524291|   -   
|8  |20.30.2.255/32    |TRAP | CoppSystemIpBcast  |0    |  -     | BcastReceive      |  -  |524288|   -   
|8  |20.30.2.0/24      |TRAP | CoppSystemL3DstMiss|2302 |2302    | ArpTrap           |  -  |526596|   -   
|8  |20.30.3.0/32      |TRAP | CoppSystemIpBcast  |0    |  -     | BcastReceive      |  -  |524288|   -   
|8  |20.30.3.254/32    |TRAP | CoppSystemIpUcast  |0    |  -     | Receive           |  -  |524291|   -   
|8  |20.30.3.255/32    |TRAP | CoppSystemIpBcast  |0    |  -     | BcastReceive      |  -  |524288|   -   
|8  |20.30.3.0/24      |TRAP | CoppSystemL3DstMiss|2303 |2303    | ArpTrap           |  -  |526597|   -   
|8  |20.30.4.0/32      |TRAP | CoppSystemIpBcast  |0    |  -     | BcastReceive      |  -  |524288|   -   
|8  |20.30.4.254/32    |TRAP | CoppSystemIpUcast  |0    |  -     | Receive           |  -  |524291|   -   
|8  |20.30.4.255/32    |TRAP | CoppSystemIpBcast  |0    |  -     | BcastReceive      |  -  |524288|   -   
|8  |20.30.4.0/24      |TRAP | CoppSystemL3DstMiss|2304 |2304    | ArpTrap           |  -  |526598|   -   
|8  |127.0.0.0/8       |TRAP | CoppSystemL3DstMiss|0    |  -     | ArpTrap           |  -  |524294|   -   
|8  |0.0.0.0/0         |TRAP | CoppSystemL3LpmOver|0    |  -     | SlowReceive       |  -  |524292|   -   

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
|  -  |91752 |ROUTE| FEC 288414         |   - |2097141 |                 - |Mpush 524277
|  -  |91754 |ROUTE| FEC 288416         |   - |2097149 |                 - |Mpush 3636
|  -  |91756 |ROUTE| FEC 288414         |   - |2097151 |                 - |Mpush 524276
|  -  |91758 |ROUTE| FEC 288414         |   - |2097148 |                 - |Mpush 524278
|  -  |91760 |ROUTE| FEC 288414         |   - |2097142 |                 - |Mpush 524279
|  -  |91762 |ROUTE| FEC 288414         |   - |2097135 |                 - |Mpush 524281
|  -  |288360|DROP | DROP               |0    |  -     |                   |   -   
|  -  |288362|DROP | DROP               |0    |  -     |                   |   -   
|  -  |288364|ROUTE| Et2                |1007 |103423  | 44:4c:a8:73:9c:0d |   -   
|  -  |288366|DROP | DROP               |0    |  -     |                   |   -   
|  -  |288368|ROUTE| Et25               |1011 |103421  | c0:f8:7f:6a:4e:2a |   -   
|  -  |288370|DROP | DROP               |0    |  -     |                   |   -   
|  -  |288372|DROP | DROP               |0    |  -     |                   |   -   
|  -  |288374|ROUTE| Et2                |1007 |103423  | 44:4c:a8:73:9c:0d |   -   
|  -  |288376|ROUTE| Et2                |1007 |103423  | 44:4c:a8:73:9c:0d |   -   
|  -  |288378|ROUTE| Et52/1             |1013 |103422  | 28:99:3a:06:b4:e1 |   -   
|  -  |288380|ROUTE| Et2                |1007 |103442  | 44:4c:a8:73:9c:0d |Mswap 900183
|  -  |288386|ROUTE| Et2                |1007 |103427  | 44:4c:a8:73:9c:0d |Mswap 900031
|  -  |288388|ROUTE| Et2                |1007 |103428  | 44:4c:a8:73:9c:0d |Mswap 900003
|  -  |288390|ROUTE| Et2                |1007 |103429  | 44:4c:a8:73:9c:0d |Mswap 900358
|  -  |288392|ROUTE| Et2                |1007 |103440  | 44:4c:a8:73:9c:0d |Mswap 900021
|  -  |288394|ROUTE| Et2                |1007 |103431  | 44:4c:a8:73:9c:0d |Mswap 900309
|  -  |288396|ROUTE| Et2                |1007 |103432  | 44:4c:a8:73:9c:0d |Mswap 900360
|  -  |288398|ROUTE| Et2                |1007 |103433  | 44:4c:a8:73:9c:0d |Mswap 900341
|  -  |288400|ROUTE| Et2                |1007 |103434  | 44:4c:a8:73:9c:0d |Mswap 900184
|  -  |288402|ROUTE| Et2                |1007 |103435  | 44:4c:a8:73:9c:0d |Mswap 900345
|  -  |288404|ROUTE| Et2                |1007 |103436  | 44:4c:a8:73:9c:0d |Mswap 900181
|  -  |288406|ROUTE| Et2                |1007 |103444  | 44:4c:a8:73:9c:0d |Mswap 900379
|  -  |288408|ROUTE| Et2                |1007 |103438  | 44:4c:a8:73:9c:0d |Mswap 900056
|  -  |288410|ROUTE| Et2                |1007 |103439  | 44:4c:a8:73:9c:0d |Mswap 900026
|  -  |288412|DROP | DROP               |0    |  -     |                   |   -   
|  -  |288414|ROUTE| FEC 528482         |   - |2097150 |                 - |Mpush 900056
|  -  |288416|ROUTE| FEC 528482         |   - |2097147 |                 - |Mpush 900309
|  -  |288418|ROUTE| Et2                |1007 |103425  | 44:4c:a8:73:9c:0d |Mswap 900034
|  -  |288420|ROUTE| Et2                |1007 |103445  | 44:4c:a8:73:9c:0d |Mswap 900059
|  -  |288422|ROUTE| Et2                |1007 |103447  | 44:4c:a8:73:9c:0d |Mswap 900161
|  -  |524288|TRAP | CoppSystemIpBcast  |0    |  -     | BcastReceive      |   -   
|  -  |524291|TRAP | CoppSystemIpUcast  |0    |  -     | Receive           |   -   
|  -  |524292|TRAP | CoppSystemL3LpmOver|0    |  -     | SlowReceive       |   -   
|  -  |524294|TRAP | CoppSystemL3DstMiss|0    |  -     | ArpTrap           |   -   
|  -  |525301|TRAP | CoppSystemL3DstMiss|1007 |1007    | ArpTrap           |   -   
|  -  |525305|TRAP | CoppSystemL3DstMiss|1011 |1011    | ArpTrap           |   -   
|  -  |525307|TRAP | CoppSystemL3DstMiss|1013 |1013    | ArpTrap           |   -   
|  -  |526596|TRAP | CoppSystemL3DstMiss|2302 |2302    | ArpTrap           |   -   
|  -  |526597|TRAP | CoppSystemL3DstMiss|2303 |2303    | ArpTrap           |   -   
|  -  |526598|TRAP | CoppSystemL3DstMiss|2304 |2304    | ArpTrap           |   -   
|  -  |528482|ROUTE| Et2                |1007 |103423  | 44:4c:a8:73:9c:0d |   -   

```

