# Test results for PE32-J2-171

## show version

```text
Arista DCS-7280SR3K-48YC8-F
Hardware version: 11.02
Serial number: JPE21241259
Hardware MAC address: 2cdd.e996.1ab3
System MAC address: 2cdd.e996.1ab3

Software image version: 4.31.2F
Architecture: i686
Internal build version: 4.31.2F-35442146.4312F
Internal build ID: 635a071a-386e-447f-942c-bcc34d9ffd3c
Image format version: 3.0
Image optimization: Default

Uptime: 6 hours and 28 minutes
Total memory: 65734516 kB
Free memory: 62293312 kB

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
Ethernet1       20.170.171.171/24    up        up                1500          
Ethernet5       20.111.171.171/24    up        up                1500          
Ethernet24      20.149.171.171/24    up        up                1500          
Loopback0       10.0.0.171/32        up        up               65535          
Management1     192.168.20.171/23    up        up                1500          

```

## show interfaces counters rates | nz

```text
Port      Name             Intvl  In Mbps      %  In Kpps Out Mbps      %
Et1       Arista_Spine_170  0:05      7.7   0.1%        0      7.8   0.1%
Et5                         0:05     63.9   0.7%        8     55.9   0.6%
Et24      Cisco_Spine_349   0:05     46.9   0.5%        5     47.0   0.5%
Ma1                         0:05      0.0   0.0%        0      0.9   0.1%

Port      Out Kpps
Et5              7
Et24             5
```

## show isis neighbors

```text
 
Instance  VRF      System Id        Type Interface          SNPA              State Hold time   Circuit Id          
IGP       default  h49-N540-24Q8L2DD L2   Ethernet24         P2P               UP    26          00                  
IGP       default  Spine3-J-170     L2   Ethernet1          P2P               UP    25          3E                  
```

## show isis database detail

```text
Legend:
H - hostname conflict
U - node unreachable

IS-IS Instance: IGP VRF: default
  IS-IS Level 2 Link State Database
    LSPID                   Seq Num  Cksum  Life Length IS  Received LSPID        Flags
 U  juniper_379_MX304.00-00        26  58531  1177    175 L2  0000.0000.0017.00-00  <>
      NLPID: 0xCC(IPv4) 0x8E(IPv6)
      Hostname: juniper_379_MX304
      Area addresses: 49.0001.00
      Interface address: 10.0.0.179
      IS Neighbor          : h55-8201-24H8FH.00  Metric: 10
        IPv4 Neighbor Address: 20.155.179.155
        IPv4 Interface Address: 20.155.179.179
        Adj-sid: 16 flags: [L V] weight: 0x0
      Reachability         : 20.155.179.0/24 Metric: 10 Type: 1 Up
      Reachability         : 10.0.0.179/32 Metric: 0 Type: 1 Up
        SR Prefix-SID: 379 Flags: [N] Algorithm: 0
      Router Capabilities: Router Id: 10.0.0.179 Flags: []
        Maximum SID depth:
          Base MPLS imposition (MSD type 1):  4
        SR Capability: Flags: [I V]
          SRGB Base: 20000 Range: 2000
        Algorithms:  0, 1
      Unsupported TLV: Type: 14 Length: 2
    0000.0000.0019.00-00         21  24189  1178    138 L2  0000.0000.0019.00-00  <>
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
      Reachability         : 192.168.0.0/19 Metric: 0 Type: 1 Up
      Router Capabilities: Router Id: 10.0.0.19 Flags: []
        Maximum SID depth:
          Base MPLS imposition (MSD type 1):  13
        SR Capability: Flags: [I]
          SRGB Base: 20000 Range: 2000
    12502-1.00-00                63   6609  1177    266 L2  0000.0000.0024.00-00  <>
      NLPID: 0xCC(IPv4)
      Hostname: 12502-1
      Area addresses: 49
      Interface address: 10.0.0.24
      Interface address: 20.24.149.24
      IS Neighbor          : h49-N540-24Q8L2DD.00 Metric: 10
        IPv4 Neighbor Address: 20.24.149.149
        IPv4 Interface Address: 20.24.149.24
        Adj-sid: 56383 flags: [L V] weight: 0x0
      Reachability         : 10.0.0.24/32 Metric: 0 Type: 1 Up
        SR Prefix-SID: 24 Flags: [N] Algorithm: 0
      Reachability         : 20.24.149.0/24 Metric: 10 Type: 1 Up
      Reachability         : 192.168.20.0/23 Metric: 0 Type: 1 Up
      Router Capabilities: Router Id: 10.0.0.24 Flags: []
        SR Local Block:
          SRLB Base: 15000 Range: 1000
        Maximum SID depth:
          Base MPLS imposition (MSD type 1):  10
        SR Capability: Flags: [I]
          SRGB Base: 20000 Range: 2000
    Ericsson_47.00-00            34  29528   770    149 L2  0000.0000.0047.00-00  <>
      Remaining lifetime received: 1199 s Modified to: 1200 s
      NLPID: 0xCC(IPv4)
      Hostname: Ericsson_47
      Area addresses: 49
      Interface address: 10.0.0.47
      IS Neighbor          : h49-N540-24Q8L2DD.00 Metric: 10
        IPv4 Interface Address: 20.47.149.47
      IS Neighbor          : Spine3-J-170.00     Metric: 10
        IPv4 Interface Address: 20.47.170.47
      Reachability         : 10.0.0.47/32 Metric: 10 Type: 1 Up
        SR Prefix-SID: 47 Flags: [N P] Algorithm: 0
      Router Capabilities: Router Id: 10.0.0.47 Flags: []
        Maximum SID depth:
          Base MPLS imposition (MSD type 1):  8
        SR Capability: Flags: [I]
          SRGB Base: 20000 Range: 2000
        Algorithms:  0
    huawei_34_NetEngine_8000_F8.00-00        18  51447  1025    167 L2  0000.0000.0254.00-00  <>
      NLPID: 0xCC(IPv4)
      Hostname: huawei_34_NetEngine_8000_F8
      Area addresses: 49
      Interface address: 10.0.0.254
      Interface address: 20.149.254.254
      Interface address: 20.171.254.254
      IS Neighbor          : h49-N540-24Q8L2DD.00 Metric: 10
        IPv4 Neighbor Address: 20.149.254.149
        IPv4 Interface Address: 20.149.254.254
        Adj-sid: 48030 flags: [L V] weight: 0x0
      Reachability         : 10.0.0.254/32 Metric: 0 Type: 1 Up
        SR Prefix-SID: 254 Flags: [N] Algorithm: 0
      Reachability         : 20.149.254.0/24 Metric: 10 Type: 1 Up
      Reachability         : 20.171.254.0/24 Metric: 10 Type: 1 Up
      Router Capabilities: Router Id: 10.0.0.254 Flags: []
        Maximum SID depth:
          Base MPLS imposition (MSD type 1):  10
        SR Capability: Flags: [I]
          SRGB Base: 20000 Range: 2000
    h49-N540-24Q8L2DD.00-00        72    611   789    673 L2  0000.0000.0349.00-00  <>
      NLPID: 0xCC(IPv4)
      Hostname: h49-N540-24Q8L2DD
      Area addresses: 49
      Interface address: 10.0.1.49
      IS Neighbor          : Ericsson_47.00      Metric: 10
        IPv4 Neighbor Address: 20.47.149.47
        IPv4 Interface Address: 20.47.149.149
        Adj-sid: 24007 flags: [L V] weight: 0x0
      IS Neighbor          : huawei_34_NetEngine_8000_F8.00 Metric: 10
        IPv4 Neighbor Address: 20.149.254.254
        IPv4 Interface Address: 20.149.254.149
        Adj-sid: 24009 flags: [L V] weight: 0x0
      IS Neighbor          : h55-8201-24H8FH.00  Metric: 10
        IPv4 Neighbor Address: 20.149.155.155
        IPv4 Interface Address: 20.149.155.149
        Adj-sid: 24005 flags: [L V] weight: 0x0
      IS Neighbor          : 0010.0010.0005.00   Metric: 10
        IPv4 Neighbor Address: 20.5.149.5
        IPv4 Interface Address: 20.5.149.149
        Adj-sid: 24003 flags: [L V] weight: 0x0
      IS Neighbor          : SR1-SRMPLS.00       Metric: 10
        IPv4 Neighbor Address: 20.57.149.57
        IPv4 Interface Address: 20.57.149.149
        Adj-sid: 24011 flags: [L V] weight: 0x0
      IS Neighbor          : 0000.0000.0019.00   Metric: 10
        IPv4 Neighbor Address: 20.19.149.19
        IPv4 Interface Address: 20.19.149.149
        Adj-sid: 24017 flags: [L V] weight: 0x0
      IS Neighbor          : 12502-1.00          Metric: 10
        IPv4 Neighbor Address: 20.24.149.24
        IPv4 Interface Address: 20.24.149.149
        Adj-sid: 24015 flags: [L V] weight: 0x0
      IS Neighbor          : PE31-J2-171.00      Metric: 10
        IPv4 Neighbor Address: 20.149.171.171
        IPv4 Interface Address: 20.149.171.149
        Adj-sid: 24001 flags: [L V] weight: 0x0
      IS Neighbor          : 3800.0000.4111.00   Metric: 10
        IPv4 Neighbor Address: 20.111.149.1
        IPv4 Interface Address: 20.111.149.149
        Adj-sid: 24013 flags: [L V] weight: 0x0
      Reachability         : 10.0.1.49/32 Metric: 0 Type: 1 Up
        SR Prefix-SID: 349 Flags: [N] Algorithm: 0
      Reachability         : 20.5.149.0/24 Metric: 10 Type: 1 Up
      Reachability         : 20.19.149.0/24 Metric: 10 Type: 1 Up
      Reachability         : 20.24.149.0/24 Metric: 10 Type: 1 Up
      Reachability         : 20.47.149.0/24 Metric: 10 Type: 1 Up
      Reachability         : 20.57.149.0/24 Metric: 10 Type: 1 Up
      Reachability         : 20.111.149.0/24 Metric: 10 Type: 1 Up
      Reachability         : 20.143.149.0/24 Metric: 10 Type: 1 Up
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
        Algorithms:  0, 1
      Unsupported TLV: Type: 14 Length: 2
    h55-8201-24H8FH.00-00        36  64811   824    251 L2  0000.0000.0355.00-00  <>
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
        Adj-sid: 24003 flags: [L V] weight: 0x0
      Reachability         : 10.0.1.55/32 Metric: 0 Type: 1 Up
        SR Prefix-SID: 355 Flags: [N] Algorithm: 0
      Reachability         : 20.149.155.0/24 Metric: 10 Type: 1 Up
      Reachability         : 20.155.179.0/24 Metric: 10 Type: 1 Up
      Router Capabilities: Router Id: 10.0.1.55 Flags: []
        SR Local Block:
          SRLB Base: 15000 Range: 1000
        Maximum SID depth:
          Base MPLS imposition (MSD type 1):  8
        SR Capability: Flags: [I]
          SRGB Base: 20000 Range: 2000
        Algorithms:  0, 1
      Unsupported TLV: Type: 14 Length: 2
    0010.0010.0005.00-00         31  32444  1103    218 L2  0010.0010.0005.00-00  <>
      NLPID: 0xCC(IPv4)
      Area addresses: 49.0005
      Interface address: 10.0.0.5
      IS Neighbor          : h49-N540-24Q8L2DD.00 Metric: 10
        IPv4 Neighbor Address: 20.5.149.149
        IPv4 Interface Address: 20.5.149.5
        Adj-sid: 24000 flags: [L V] weight: 0x0
      Reachability         : 20.5.149.0/24 Metric: 10 Type: 1 Up
      Reachability         : 10.0.0.5/32 Metric: 10 Type: 1 Up
        SR Prefix-SID: 5 Flags: [N] Algorithm: 0
      Reachability          : fcbb:0:3::/48 Metric: 10 Type: 1 Up
      Reachability          : fcba:0:0:3::/64 Metric: 10 Type: 1 Up
      Router Capabilities: Router Id: 10.0.0.5 Flags: []
        SR Capability: Flags: [I]
          SRGB Base: 16000 Range: 8000
        Algorithms:  0
    SR1-SRMPLS.00-00             31  11922   761    400 L2  0100.0000.0057.00-00  <>
      Remaining lifetime received: 1199 s Modified to: 1200 s
      NLPID: 0xCC(IPv4) 0x8E(IPv6)
      Hostname: SR1-SRMPLS
      Area addresses: 49.0000.0000.0057.00
      Interface address: 10.0.0.57
      Interface address: 20.57.59.57
      Interface address: 20.57.149.57
      Interface address: 20.57.170.57
      Interface address: 2002::57
      IS Neighbor (Narrow metrics, unsupported): h49-N540-24Q8L2DD.00 Metric: 10
      IS Neighbor (Narrow metrics, unsupported): Spine3-J-170.00     Metric: 10
      IS Neighbor (Narrow metrics, unsupported): IXRE2.00            Metric: 10
      IS Neighbor          : h49-N540-24Q8L2DD.00 Metric: 10
        IPv4 Neighbor Address: 20.57.149.149
        IPv4 Interface Address: 20.57.149.57
        Adj-sid: 30149 flags: [L V] weight: 0x0
      IS Neighbor          : Spine3-J-170.00     Metric: 10
        IPv4 Neighbor Address: 20.57.170.170
        IPv4 Interface Address: 20.57.170.57
        Adj-sid: 30170 flags: [L V] weight: 0x0
      IS Neighbor          : IXRE2.00            Metric: 10
        IPv4 Neighbor Address: 20.57.59.59
        IPv4 Interface Address: 20.57.59.57
        Adj-sid: 30059 flags: [L V] weight: 0x0
      Reachability (Narrow metrics, unsupported): 10.0.0.57/32 Metric: 0 Type: 1
      Reachability (Narrow metrics, unsupported): 20.57.59.0/24 Metric: 10 Type: 1
      Reachability (Narrow metrics, unsupported): 20.57.149.0/24 Metric: 10 Type: 1
      Reachability (Narrow metrics, unsupported): 20.57.170.0/24 Metric: 10 Type: 1
      Reachability         : 10.0.0.57/32 Metric: 0 Type: 1 Up
        SR Prefix-SID: 57 Flags: [N P] Algorithm: 0
      Reachability         : 20.57.59.0/24 Metric: 10 Type: 1 Up
      Reachability         : 20.57.149.0/24 Metric: 10 Type: 1 Up
      Reachability         : 20.57.170.0/24 Metric: 10 Type: 1 Up
      Reachability          : 2002::57/128 Metric: 0 Type: 1 Up
      Router Capabilities: Router Id: 10.0.0.57 Flags: []
        Maximum SID depth:
          Base MPLS imposition (MSD type 1):  12
        SR Capability: Flags: [I V]
          SRGB Base: 20000 Range: 2000
        Algorithms:  0
    IXRE2.00-00                  27  46719   636    247 L2  0100.0000.0059.00-00  <>
      Remaining lifetime received: 1199 s Modified to: 1200 s
      NLPID: 0xCC(IPv4) 0x8E(IPv6)
      Hostname: IXRE2
      Area addresses: 49.0000.0000.0059.00
      Topology: 0 (IPv4)
      Topology: 2 (IPv6)
      Interface address: 10.0.0.59
      Interface address: 20.57.59.59
      Interface address: 2001:0:59:161::59
      Interface address: 2001:1:59:352::59
      Interface address: 2002::59
      IS Neighbor          : SR1-SRMPLS.00       Metric: 10
        IPv4 Neighbor Address: 20.57.59.57
        IPv4 Interface Address: 20.57.59.59
      Reachability         : 20.57.59.0/24 Metric: 10 Type: 1 Up
      Reachability         : 10.0.0.59/32 Metric: 0 Type: 1 Up
      Reachability (MT-IPv6): 2001:0:59:161::/64 Metric: 10 Type: 1 Up
      Reachability (MT-IPv6): 2001:1:59:352::/64 Metric: 10 Type: 1 Up
      Reachability (MT-IPv6): 2002::59/128 Metric: 0 Type: 1 Up
      Router Capabilities: Router Id: 10.0.0.59 Flags: []
    Spine3-J-170.00-00           35  10509   717    253 L2  0100.0000.0170.00-00  <>
      Remaining lifetime received: 1199 s Modified to: 1200 s
      NLPID: 0xCC(IPv4)
      Hostname: Spine3-J-170
      Area addresses: 49.0000
      Interface address: 20.47.170.170
      Interface address: 20.170.254.170
      Interface address: 20.57.170.170
      Interface address: 10.0.0.170
      Interface address: 20.170.171.170
      IS Neighbor          : Ericsson_47.00      Metric: 10
        IPv4 Neighbor Address: 20.47.170.47
        IPv4 Interface Address: 20.47.170.170
        Adj-sid: 362146 flags: [L V] weight: 0x0
      IS Neighbor          : SR1-SRMPLS.00       Metric: 10
        IPv4 Neighbor Address: 20.57.170.57
        IPv4 Interface Address: 20.57.170.170
        Adj-sid: 362145 flags: [L V] weight: 0x0
      IS Neighbor          : PE31-J2-171.00      Metric: 10
        IPv4 Neighbor Address: 20.170.171.171
        IPv4 Interface Address: 20.170.171.170
        Adj-sid: 362144 flags: [L V] weight: 0x0
      Reachability         : 20.47.170.0/24 Metric: 10 Type: 1 Up
      Reachability         : 20.170.254.0/24 Metric: 10 Type: 1 Up
      Reachability         : 20.57.170.0/24 Metric: 10 Type: 1 Up
      Reachability         : 10.0.0.170/32 Metric: 10 Type: 1 Up
        SR Prefix-SID: 170 Flags: [N] Algorithm: 0
      Reachability         : 20.170.171.0/24 Metric: 10 Type: 1 Up
      Router Capabilities: Router Id: 100.0.0.170 Flags: []
        SR Local Block:
          SRLB Base: 965536 Range: 65536
        Area leader priority: 250 algorithm: 0
        Maximum SID depth:
          Base MPLS imposition (MSD type 1):  6
        SR Capability: Flags: [I]
          SRGB Base: 20000 Range: 2000
    PE31-J2-171.00-00            34  54894   783    198 L2  0100.0000.0171.00-00  <>
      LSP generation remaining wait time: 0 ms
      Time remaining until refresh: 483 s
      NLPID: 0xCC(IPv4)
      Hostname: PE31-J2-171
      Area addresses: 49.0000
      Interface address: 20.170.171.171
      Interface address: 10.0.0.171
      Interface address: 20.149.171.171
      IS Neighbor          : h49-N540-24Q8L2DD.00 Metric: 10
        IPv4 Neighbor Address: 20.149.171.149
        IPv4 Interface Address: 20.149.171.171
        Adj-sid: 362145 flags: [L V] weight: 0x0
      IS Neighbor          : Spine3-J-170.00     Metric: 10
        IPv4 Neighbor Address: 20.170.171.170
        IPv4 Interface Address: 20.170.171.171
        Adj-sid: 362144 flags: [L V] weight: 0x0
      Reachability         : 10.0.0.171/32 Metric: 10 Type: 1 Up
        SR Prefix-SID: 171 Flags: [N] Algorithm: 0
      Reachability         : 20.170.171.0/24 Metric: 10 Type: 1 Up
      Reachability         : 20.149.171.0/24 Metric: 10 Type: 1 Up
      Router Capabilities: Router Id: 100.0.0.172 Flags: []
        SR Local Block:
          SRLB Base: 965536 Range: 65536
        Area leader priority: 250 algorithm: 0
        Maximum SID depth:
          Base MPLS imposition (MSD type 1):  12
        SR Capability: Flags: [I]
          SRGB Base: 20000 Range: 2000
    juniper_379_MX304.00-00         5  13848  1154    178 L2  1000.0000.0079.00-00  <>
      NLPID: 0xCC(IPv4) 0x8E(IPv6)
      Hostname: juniper_379_MX304
      Area addresses: 49.0001.0000.0000
      Interface address: 100.0.0.79
      IS Neighbor          : h55-8201-24H8FH.00  Metric: 10
        IPv4 Neighbor Address: 20.155.179.155
        IPv4 Interface Address: 20.155.179.179
        Adj-sid: 16 flags: [L V] weight: 0x0
      Reachability         : 20.155.179.0/24 Metric: 10 Type: 1 Up
      Reachability         : 100.0.0.79/32 Metric: 0 Type: 1 Up
        SR Prefix-SID: 379 Flags: [N] Algorithm: 0
      Router Capabilities: Router Id: 100.0.0.79 Flags: []
        Maximum SID depth:
          Base MPLS imposition (MSD type 1):  3
        SR Capability: Flags: [I V]
          SRGB Base: 20000 Range: 2000
        Algorithms:  0, 1
      Unsupported TLV: Type: 14 Length: 2
    3800.0000.4111.00-00         22   9554   788    115 L2  3800.0000.4111.00-00  <DefaultAtt>
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
  Index     Endpoint           Next Hop/Tunnel Index     Interface    Labels   
--------- ------------------ ------------------------- -------------- ---------
  1         10.0.0.170/32      TI-LFA (0)                -            [ 3 ]    
  3         10.0.0.254/32      TI-LFA (2)                -            [ 20254 ]
  5         10.0.0.24/32       TI-LFA (2)                -            [ 20024 ]
  6         10.0.0.5/32        TI-LFA (2)                -            [ 20005 ]
  7         10.0.1.49/32       TI-LFA (1)                -            [ 3 ]    
  8         10.0.1.55/32       TI-LFA (2)                -            [ 20355 ]
  10        100.0.1.111/32     TI-LFA (3)                -            [ 20411 ]
  11        10.0.0.57/32       20.149.171.149            Ethernet24   [ 20057 ]
                               20.170.171.170            Ethernet1    [ 20057 ]
  12        10.0.0.19/32       TI-LFA (2)                -            [ 20019 ]
  13        10.0.0.47/32       20.149.171.149            Ethernet24   [ 20047 ]
                               20.170.171.170            Ethernet1    [ 20047 ]
  14        100.0.0.79/32      TI-LFA (2)                -            [ 20379 ]

```

## show isis segment-routing prefix-segments

```text

System ID: PE31-J2-171			Instance: 'IGP'
SR supported Data-plane: MPLS			SR Router ID: 100.0.0.172

Node: 12     Proxy-Node: 0      Prefix: 0       Total Segments: 12

Flag Descriptions: R: Re-advertised, N: Node Segment, P: no-PHP
                   E: Explicit-NULL, V: Value, L: Local
Segment status codes: * - Self originated Prefix, L1 - level 1, L2 - level 2, ! - SR-unreachable,
                      # - Some IS-IS next-hops are SR-unreachable
   Prefix                      SID Type       Flags                        System ID       Level Protection  Algorithm   
   ------------------------- ----- ---------- ---------------------------- --------------- ----- ----------- -------------
   10.0.0.5/32                   5 Node       R:0 N:1 P:0 E:0 V:0 L:0      0010.0010.0005  L2    node        SPF         
   10.0.0.19/32                 19 Node       R:0 N:1 P:0 E:0 V:0 L:0      0000.0000.0019  L2    node        SPF         
   10.0.0.24/32                 24 Node       R:0 N:1 P:0 E:0 V:0 L:0      12502-1         L2    node        SPF         
   10.0.0.47/32                 47 Node       R:0 N:1 P:1 E:0 V:0 L:0      Ericsson_47     L2    unprotected SPF         
   10.0.0.57/32                 57 Node       R:0 N:1 P:1 E:0 V:0 L:0      SR1-SRMPLS      L2    unprotected SPF         
   10.0.0.170/32               170 Node       R:0 N:1 P:0 E:0 V:0 L:0      Spine3-J-170    L2    node        SPF         
*  10.0.0.171/32               171 Node       R:0 N:1 P:0 E:0 V:0 L:0      PE31-J2-171     L2    unprotected SPF         
   10.0.0.254/32               254 Node       R:0 N:1 P:0 E:0 V:0 L:0      huawei_34_NetEngine_8000_F8 L2    node        SPF         
   10.0.1.49/32                349 Node       R:0 N:1 P:0 E:0 V:0 L:0      h49-N540-24Q8L2DD L2    node        SPF         
   10.0.1.55/32                355 Node       R:0 N:1 P:0 E:0 V:0 L:0      h55-8201-24H8FH L2    node        SPF         
   100.0.0.79/32               379 Node       R:0 N:1 P:0 E:0 V:0 L:0      juniper_379_MX304 L2    node        SPF         
   100.0.1.111/32              411 Node       R:0 N:1 P:0 E:0 V:0 L:0      3800.0000.4111  L2    node        SPF         
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
 I L2     10.0.0.47/32 [115/30]
           via 20.170.171.170, Ethernet1
           via 20.149.171.149, Ethernet24
 I L2     10.0.0.57/32 [115/20]
           via 20.170.171.170, Ethernet1
           via 20.149.171.149, Ethernet24
 I L2     10.0.0.59/32 [115/30]
           via 20.170.171.170, Ethernet1
           via 20.149.171.149, Ethernet24
 I L2     10.0.0.170/32 [115/20]
           via 20.170.171.170, Ethernet1
 C        10.0.0.171/32
           directly connected, Loopback0
 I L2     10.0.0.254/32 [115/20]
           via 20.149.171.149, Ethernet24
 I L2     10.0.1.49/32 [115/10]
           via 20.149.171.149, Ethernet24
 I L2     10.0.1.55/32 [115/20]
           via 20.149.171.149, Ethernet24
 I L2     20.5.149.0/24 [115/20]
           via 20.149.171.149, Ethernet24
 I L2     20.19.149.0/24 [115/20]
           via 20.149.171.149, Ethernet24
 I L2     20.24.149.0/24 [115/20]
           via 20.149.171.149, Ethernet24
 I L2     20.47.149.0/24 [115/20]
           via 20.149.171.149, Ethernet24
 I L2     20.47.170.0/24 [115/20]
           via 20.170.171.170, Ethernet1
 I L2     20.57.59.0/24 [115/30]
           via 20.170.171.170, Ethernet1
           via 20.149.171.149, Ethernet24
 I L2     20.57.149.0/24 [115/20]
           via 20.149.171.149, Ethernet24
 I L2     20.57.170.0/24 [115/20]
           via 20.170.171.170, Ethernet1
 I L2     20.111.149.0/24 [115/20]
           via 20.149.171.149, Ethernet24
 I L2     20.143.149.0/24 [115/20]
           via 20.149.171.149, Ethernet24
 I L2     20.149.155.0/24 [115/20]
           via 20.149.171.149, Ethernet24
 C        20.149.171.0/24
           directly connected, Ethernet24
 I L2     20.149.254.0/24 [115/20]
           via 20.149.171.149, Ethernet24
 I L2     20.155.179.0/24 [115/30]
           via 20.149.171.149, Ethernet24
 C        20.170.171.0/24
           directly connected, Ethernet1
 I L2     20.170.254.0/24 [115/20]
           via 20.170.171.170, Ethernet1
 I L2     20.171.254.0/24 [115/30]
           via 20.149.171.149, Ethernet24
 I L2     100.0.0.79/32 [115/30]
           via 20.149.171.149, Ethernet24
 I L2     100.0.1.111/32 [115/30]
           via 20.149.171.149, Ethernet24
 I L2     192.168.20.0/23 [115/20]
           via 20.149.171.149, Ethernet24
 I L2     192.168.0.0/19 [115/20]
           via 20.149.171.149, Ethernet24

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
MPLS forwarding table (Label [metric] Vias) - 14 routes 
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
                  via TI-LFA tunnel index 2
                    via 20.149.171.149, Ethernet24, label imp-null(3)
                    backup via 20.170.171.170, Ethernet1, label 20057
 20019   A[1]
                via M, ::, forward
                    EgressACL: apply
                  via TI-LFA tunnel index 2
                    via 20.149.171.149, Ethernet24, label imp-null(3)
                    backup via 20.170.171.170, Ethernet1, label 20057
 20024   A[1]
                via M, ::, forward
                    EgressACL: apply
                  via TI-LFA tunnel index 2
                    via 20.149.171.149, Ethernet24, label imp-null(3)
                    backup via 20.170.171.170, Ethernet1, label 20057
 20047   A[1]
                via M, forward
                    EgressACL: apply
                    20.149.171.149 Ethernet24
                    20.170.171.170 Ethernet1
 20057   A[1]
                via M, forward
                    EgressACL: apply
                    20.149.171.149 Ethernet24
                    20.170.171.170 Ethernet1
 20170   A[1]
                via M, ::, pop
                    EgressACL: apply
                  via TI-LFA tunnel index 0
                    via 20.170.171.170, Ethernet1, label imp-null(3)
                    backup via 20.149.171.149, Ethernet24, label 20057 20170
 20254   A[1]
                via M, ::, forward
                    EgressACL: apply
                  via TI-LFA tunnel index 2
                    via 20.149.171.149, Ethernet24, label imp-null(3)
                    backup via 20.170.171.170, Ethernet1, label 20057
 20349   A[1]
                via M, ::, pop
                    EgressACL: apply
                  via TI-LFA tunnel index 1
                    via 20.149.171.149, Ethernet24, label imp-null(3)
                    backup via 20.170.171.170, Ethernet1, label 20057 20349
 20355   A[1]
                via M, ::, forward
                    EgressACL: apply
                  via TI-LFA tunnel index 2
                    via 20.149.171.149, Ethernet24, label imp-null(3)
                    backup via 20.170.171.170, Ethernet1, label 20057
 20379   A[1]
                via M, ::, forward
                    EgressACL: apply
                  via TI-LFA tunnel index 2
                    via 20.149.171.149, Ethernet24, label imp-null(3)
                    backup via 20.170.171.170, Ethernet1, label 20057
 20411   A[1]
                via M, ::, forward
                    EgressACL: apply
                  via TI-LFA tunnel index 3
                    via 20.149.171.149, Ethernet24, label imp-null(3)
                    backup via 20.170.171.170, Ethernet1, label 20047
 362144  A[1]
                via M, 20.170.171.170, pop
                    EgressACL: apply
                    directly connected, Ethernet1
                    28:99:3a:06:b4:e1, vlan 1050
 362145  A[1]
                via M, 20.149.171.149, pop
                    EgressACL: apply
                    directly connected, Ethernet24
                    c0:f8:7f:6a:4e:1c, vlan 1031
 378528   [0]
                via I, ipv4, vrf ISIS-SR-L3VPN
```

## show mpls lfib route

```text
MPLS forwarding table (Label [metric] Vias) - 14 routes 
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
                via TI-LFA tunnel index 2, forward
                 payload autoDecide, ttlMode uniform, dscpMode uniform, apply egress-acl
                    via 20.149.171.149, Ethernet24, label imp-null(3)
                    backup via 20.170.171.170, Ethernet1, label 20057
 IP    20019    [1], 10.0.0.19/32
                via TI-LFA tunnel index 2, forward
                 payload autoDecide, ttlMode uniform, dscpMode uniform, apply egress-acl
                    via 20.149.171.149, Ethernet24, label imp-null(3)
                    backup via 20.170.171.170, Ethernet1, label 20057
 IP    20024    [1], 10.0.0.24/32
                via TI-LFA tunnel index 2, forward
                 payload autoDecide, ttlMode uniform, dscpMode uniform, apply egress-acl
                    via 20.149.171.149, Ethernet24, label imp-null(3)
                    backup via 20.170.171.170, Ethernet1, label 20057
 IP    20047    [1], 10.0.0.47/32
                via M, 20.149.171.149, forward
                 payload autoDecide, ttlMode uniform, dscpMode uniform, apply egress-acl
                 interface Ethernet24
                via M, 20.170.171.170, forward
                 payload autoDecide, ttlMode uniform, dscpMode uniform, apply egress-acl
                 interface Ethernet1
 IP    20057    [1], 10.0.0.57/32
                via M, 20.149.171.149, forward
                 payload autoDecide, ttlMode uniform, dscpMode uniform, apply egress-acl
                 interface Ethernet24
                via M, 20.170.171.170, forward
                 payload autoDecide, ttlMode uniform, dscpMode uniform, apply egress-acl
                 interface Ethernet1
 IP    20170    [1], 10.0.0.170/32
                via TI-LFA tunnel index 0, pop
                 payload autoDecide, ttlMode uniform, dscpMode uniform, apply egress-acl
                    via 20.170.171.170, Ethernet1, label imp-null(3)
                    backup via 20.149.171.149, Ethernet24, label 20057 20170
 IP    20254    [1], 10.0.0.254/32
                via TI-LFA tunnel index 2, forward
                 payload autoDecide, ttlMode uniform, dscpMode uniform, apply egress-acl
                    via 20.149.171.149, Ethernet24, label imp-null(3)
                    backup via 20.170.171.170, Ethernet1, label 20057
 IP    20349    [1], 10.0.1.49/32
                via TI-LFA tunnel index 1, pop
                 payload autoDecide, ttlMode uniform, dscpMode uniform, apply egress-acl
                    via 20.149.171.149, Ethernet24, label imp-null(3)
                    backup via 20.170.171.170, Ethernet1, label 20057 20349
 IP    20355    [1], 10.0.1.55/32
                via TI-LFA tunnel index 2, forward
                 payload autoDecide, ttlMode uniform, dscpMode uniform, apply egress-acl
                    via 20.149.171.149, Ethernet24, label imp-null(3)
                    backup via 20.170.171.170, Ethernet1, label 20057
 IP    20379    [1], 100.0.0.79/32
                via TI-LFA tunnel index 2, forward
                 payload autoDecide, ttlMode uniform, dscpMode uniform, apply egress-acl
                    via 20.149.171.149, Ethernet24, label imp-null(3)
                    backup via 20.170.171.170, Ethernet1, label 20057
 IP    20411    [1], 100.0.1.111/32
                via TI-LFA tunnel index 3, forward
                 payload autoDecide, ttlMode uniform, dscpMode uniform, apply egress-acl
                    via 20.149.171.149, Ethernet24, label imp-null(3)
                    backup via 20.170.171.170, Ethernet1, label 20047
 IA    362144   [1]
                via M, 20.170.171.170, pop
                 payload autoDecide, ttlMode uniform, apply egress-acl
                 interface Ethernet1
 IA    362145   [1]
                via M, 20.149.171.149, pop
                 payload autoDecide, ttlMode uniform, apply egress-acl
                 interface Ethernet24
 B3    378528   [0]
                via I, ipv4, vrf ISIS-SR-L3VPN
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
 * >      RD: 65000:19 IPv4 prefix 20.19.111.0/24
                                 10.0.0.19             0       100     0       ? Or-ID: 10.0.0.19 C-LST: 10.0.1.49 
 * >      RD: 65000:24 IPv4 prefix 20.24.111.0/24
                                 10.0.0.24             0       100     0       ? Or-ID: 10.0.0.24 C-LST: 10.0.1.49 
 * >      RD: 10.0.0.47:1 IPv4 prefix 20.47.111.0/24
                                 10.0.0.47             0       100     0       ? Or-ID: 10.0.0.47 C-LST: 10.0.1.49 
 * >      RD: 10.0.1.55:1 IPv4 prefix 20.55.111.0/24
                                 10.0.1.55             0       100     0       ? Or-ID: 10.0.1.55 C-LST: 10.0.1.49 
 * >      RD: 10.0.0.57:1 IPv4 prefix 20.57.111.0/24
                                 10.0.0.57             -       100     0       i Or-ID: 10.0.0.57 C-LST: 10.0.1.49 
 * >      RD: 65000:1 IPv4 prefix 20.111.111.0/24
                                 100.0.1.111           -       0       0       i Or-ID: 194.0.0.1 C-LST: 10.0.1.49 
 * >      RD: 10.0.0.171:1 IPv4 prefix 20.111.171.0/24
                                 -                     -       -       0       i
 * >      RD: 65000:254 IPv4 prefix 20.111.254.0/24
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
  Last read 00:00:46, last write 00:00:09
  Hold time is 180, keepalive interval is 60 seconds
  Configured hold time is 180, keepalive interval is 60 seconds
  Effective minimum hold time is 3 seconds
  Send failure hold time is 0 seconds
  Hold timer is active, time left: 00:02:14
  Keepalive timer is active, time left: 00:00:38
  Connect timer is inactive
  Idle-restart timer is inactive
  BGP state is Established, up for 02:12:10
  Number of transitions to established: 3
  Last state was OpenConfirm
  Last event was RecvKeepAlive
  Last sent notification:Cease/administrative reset, Last time 02:12:16, First time 02:20:04, Repeats 1
  Last sent socket-error:Connect (Connection refused), Last time 02:28:12, First time 02:31:21, Repeats 1
  Last rcvd socket-error:Connection reset by peer, Last time 02:12:15, First time 02:20:03, Repeats 1
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
    Opens:                  5         3
    Notifications:          2         0
    Updates:                7        70
    Keepalives:           174       134
    Route Refresh:          0         0
    Total messages:       188       207
  Prefix Statistics:
                                   Sent      Rcvd     Best Paths     Best ECMP Paths
    IPv4 Unicast:                     0         0              0                   0
    VPN-IPv4:                         1         8              8                   0
    IPv6 Unicast:                     0         0              0                   0
  Configured maximum total number of routes is 0
  Inbound updates dropped by reason:
    AS path loop detection: 0
    Cluster ID loop detection: 0
    Enforced First AS: 0
    Malformed MPBGP routes: 0
    Originator ID matches local router ID: 0
    Nexthop matches local IP address: 3
    Unexpected IPv6 nexthop for IPv4 routes: 0
  Inbound updates with attribute errors:
    Resulting in removal of all paths in update (treat as withdraw): 3
    Resulting in AFI/SAFI disable: 0
    Resulting in attribute ignore: 0
    Disabled AFI/SAFIs: None
    Last treat-as-withdraw attribute error: Nexthop is local address
    Last update with error received at: 00:38:16
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
Local TCP address is 10.0.0.171, local port is 43583
Remote TCP address is 10.0.1.49, remote port is 179
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
    Round-trip Time (rtt/rtvar): 200.6ms/0.5ms
    Delayed Ack Timeout (ato): 40.0ms
    Congestion Window (cwnd): 2
    Slow-start Threshold (ssthresh): 7
    TCP Throughput: 0.10 Mbps
    Advertised Recv Window (rcv_space): 14600

```

## show tunnel rib system-tunnel-rib brief

```text
Tunnel RIB: system-tunnel-rib
Endpoint        Tunnel Type     Index(es)   Tunnel Preference   IGP Preference 
--------------- -------------- ----------- ------------------- ----------------
10.0.0.5/32     IS-IS SR IPv4   6           65                  115            
10.0.0.19/32    IS-IS SR IPv4   12          65                  115            
10.0.0.24/32    IS-IS SR IPv4   5           65                  115            
10.0.0.47/32    IS-IS SR IPv4   13          65                  115            
10.0.0.57/32    IS-IS SR IPv4   11          65                  115            
10.0.0.170/32   IS-IS SR IPv4   1           65                  115            
10.0.0.254/32   IS-IS SR IPv4   3           65                  115            
10.0.1.49/32    IS-IS SR IPv4   7           65                  115            
10.0.1.55/32    IS-IS SR IPv4   8           65                  115            
100.0.0.79/32   IS-IS SR IPv4   14          65                  115            
100.0.1.111/32  IS-IS SR IPv4   10          65                  115            

   IGP Metric    Metric Type
---------------- -----------
   30            metric     
   20            metric     
   20            metric     
   30            metric     
   20            metric     
   20            metric     
   20            metric     
   10            metric     
   20            metric     
   30            metric     
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
>C    10.0.0.171/32 [0 pref/0 metric] updated 04:52:32 ago
         via Loopback0, directly connected
>C    20.149.171.0/24 [0 pref/0 metric] updated 05:13:49 ago
         via Ethernet24, directly connected
>C    20.170.171.0/24 [0 pref/0 metric] updated 02:27:00 ago
         via Ethernet1, directly connected
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
>P    0.0.0.0/8 [1 pref/0 metric] updated 06:25:49 ago
         via Null0, directly connected [NF]
>P    127.0.0.0/8 [1 pref/0 metric] updated 06:25:49 ago
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
>I    10.0.0.5/32 [115 pref/30 metric] updated 01:16:38 ago
         via 20.149.171.149, Ethernet24
>I    10.0.0.19/32 [115 pref/20 metric] updated 00:58:44 ago
         via 20.149.171.149, Ethernet24
>I    10.0.0.24/32 [115 pref/20 metric] updated 01:07:27 ago
         via 20.149.171.149, Ethernet24
>I    10.0.0.47/32 [115 pref/30 metric] updated 01:19:40 ago
         via 20.149.171.149, Ethernet24
         via 20.170.171.170, Ethernet1
>I    10.0.0.57/32 [115 pref/20 metric] updated 02:08:13 ago
         via 20.149.171.149, Ethernet24
         via 20.170.171.170, Ethernet1
>I    10.0.0.59/32 [115 pref/30 metric] updated 01:48:04 ago
         via 20.149.171.149, Ethernet24
         via 20.170.171.170, Ethernet1
>I    10.0.0.170/32 [115 pref/20 metric] updated 02:21:40 ago
         via 20.170.171.170, Ethernet1
>I    10.0.0.254/32 [115 pref/20 metric] updated 02:45:34 ago
         via 20.149.171.149, Ethernet24
>I    10.0.1.49/32 [115 pref/10 metric] updated 03:03:46 ago
         via 20.149.171.149, Ethernet24
>I    10.0.1.55/32 [115 pref/20 metric] updated 03:03:46 ago
         via 20.149.171.149, Ethernet24
>I    20.5.149.0/24 [115 pref/20 metric] updated 03:03:46 ago
         via 20.149.171.149, Ethernet24
>I    20.19.149.0/24 [115 pref/20 metric] updated 03:03:46 ago
         via 20.149.171.149, Ethernet24
>I    20.24.149.0/24 [115 pref/20 metric] updated 03:03:46 ago
         via 20.149.171.149, Ethernet24
>I    20.47.149.0/24 [115 pref/20 metric] updated 03:03:46 ago
         via 20.149.171.149, Ethernet24
>I    20.47.170.0/24 [115 pref/20 metric] updated 02:04:57 ago
         via 20.170.171.170, Ethernet1
>I    20.57.59.0/24 [115 pref/30 metric] updated 01:48:14 ago
         via 20.149.171.149, Ethernet24
         via 20.170.171.170, Ethernet1
>I    20.57.149.0/24 [115 pref/20 metric] updated 03:01:02 ago
         via 20.149.171.149, Ethernet24
>I    20.57.170.0/24 [115 pref/20 metric] updated 02:08:17 ago
         via 20.170.171.170, Ethernet1
>I    20.111.149.0/24 [115 pref/20 metric] updated 02:52:30 ago
         via 20.149.171.149, Ethernet24
>I    20.143.149.0/24 [115 pref/20 metric] updated 03:03:46 ago
         via 20.149.171.149, Ethernet24
>I    20.149.155.0/24 [115 pref/20 metric] updated 03:03:46 ago
         via 20.149.171.149, Ethernet24
>I    20.149.254.0/24 [115 pref/20 metric] updated 03:03:46 ago
         via 20.149.171.149, Ethernet24
>I    20.155.179.0/24 [115 pref/30 metric] updated 02:33:30 ago
         via 20.149.171.149, Ethernet24
>I    20.170.254.0/24 [115 pref/20 metric] updated 02:06:42 ago
         via 20.170.171.170, Ethernet1
>I    20.171.254.0/24 [115 pref/30 metric] updated 02:30:58 ago
         via 20.149.171.149, Ethernet24
>I    100.0.0.79/32 [115 pref/30 metric] updated 00:06:18 ago
         via 20.149.171.149, Ethernet24
>I    100.0.1.111/32 [115 pref/30 metric] updated 00:06:54 ago
         via 20.149.171.149, Ethernet24
>I    192.168.0.0/19 [115 pref/20 metric] updated 00:58:44 ago
         via 20.149.171.149, Ethernet24
>I    192.168.20.0/23 [115 pref/20 metric] updated 01:07:27 ago
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
>P    ::/96 [1 pref/0 metric] updated 03:36:31 ago
         via Null0, directly connected [NF]
>P    ::ffff:127.0.0.0/104 [1 pref/0 metric] updated 03:36:31 ago
         via :: [1 pref/1 metric] type ipv6
            via , directly connected
>P    fe80::/10 [1 pref/0 metric] updated 03:36:31 ago
```

## show platform sand l3 summary

```text
Number of vrfs: 3

Ipv4:
  Routes:       66  backlog:  0  unprogrammed:  0
  Adjacencies:  50  backlog:  0  unprogrammed:  0
Ipv6:
  Routes:       0   backlog:  0  unprogrammed:  0
  Adjacencies:  50  backlog:  0  unprogrammed:  0
Mpls:
  Routes:       13  backlog:  0  unprogrammed:  0
  Adjacencies:  2   backlog:  0  unprogrammed:  0

Jericho2 Ip Fecs:
  Non-ecmp fecs:  4118  ecmp fecs:  2  fec entries:  4122
Jericho2 Mpls Fecs:
  Non-ecmp fecs:  2  ecmp fecs:  0  fec entries:  2
Jericho2 Vxlan Tunnel Fecs:
  Non-ecmp fecs:  0  ecmp fecs:  0  fec entries:  0
  Number of vxlan tunnels configured: 0

Jericho2 Lpm Routes:
  Routes:   66  unprogrammed:   0   
  Routes6:  1   unprogrammed6:  0   
  Backlog:  0 

Jericho2 Lpm:
  TCAM entries used:   3   Percent free:  99  ADS2 entries used:   4  Percent free:  99
  Pivot buckets used:  4   Rows used:     1   Entries Per Bucket:  1  Percent free:  99
  Route buckets used:  10  Rows used:     2   Entries Per Bucket:  6  Percent free:  99

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
  FixedSystem: 0
Egress Mpls (for inner 2 labels) rewrite entries in use (in each fap):
  FixedSystem: 8
Egress Sflow rewrite entries in use (in each fap):
  FixedSystem: 0

Egress rewrite chains in backlog: resource-full 0, no-interface 0

Glem entries used per fap :
  FixedSystem: 4107

Jericho2 Fec:
  Maximum FEC hierarchy levels:  2
  ReusedEcmp:  0  allocs:  41  frees:  17  shuffles:  0  cmds:  0
  Zombies:     0    purges:    0
  Quarantine:  0/0  shuffles:  0  deletes:  0   
  Fec insertion failures:  0
  Level1  Fecs:
    Non-ecmp fecs:            8   ecmp fecs:            1 
    Non-ecmp (Percent free):  99  ecmp (Percent free):  99
  Level2  Fecs:
    Non-ecmp fecs:            18  ecmp fecs:            2 
    Non-ecmp (Percent free):  99  ecmp (Percent free):  99
  Level3  Fecs:
    Non-ecmp fecs:            0    ecmp fecs:            0  
    Non-ecmp (Percent free):  100  ecmp (Percent free):  100

Lpm Detail:
  Requests:  249  cleanses:  158  batches:  158  avg batch size:  1

Jericho Arp:
  ArpTable writes:      16955  queued      0   
  IngressTable writes:  79704  queued      0   
  Coprocessors:         1      in CmdRing

Tunnel Counter Status
  Number of MPLS tunnels:                  8    
  Number of uncountable MPLS tunnels:      8    
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
|0  |10.0.0.5/32       |ROUTE| Et24               |1031 |103421  | c0:f8:7f:6a:4e:1c |  -  |288362|   -   
|0  |10.0.0.19/32      |ROUTE| Et24               |1031 |103421  | c0:f8:7f:6a:4e:1c |  -  |288362|   -   
|0  |10.0.0.24/32      |ROUTE| Et24               |1031 |103421  | c0:f8:7f:6a:4e:1c |  -  |288362|   -   
|0  |10.0.0.47/32      |ROUTE| Et24               |1031 |103421  | c0:f8:7f:6a:4e:1c |16384|288369|   -   
|0  |10.0.0.47/32      |ROUTE| Et1                |1050 |103422  | 28:99:3a:06:b4:e1 |16384|288370|   -   
|0  |10.0.0.57/32      |ROUTE| Et24               |1031 |103421  | c0:f8:7f:6a:4e:1c |16384|288369|   -   
|0  |10.0.0.57/32      |ROUTE| Et1                |1050 |103422  | 28:99:3a:06:b4:e1 |16384|288370|   -   
|0  |10.0.0.59/32      |ROUTE| Et24               |1031 |103421  | c0:f8:7f:6a:4e:1c |16384|288369|   -   
|0  |10.0.0.59/32      |ROUTE| Et1                |1050 |103422  | 28:99:3a:06:b4:e1 |16384|288370|   -   
|0  |10.0.0.170/32     |ROUTE| Et1                |1050 |103422  | 28:99:3a:06:b4:e1 |  -  |288366|   -   
|0  |10.0.0.171/32     |TRAP | CoppSystemIpUcast  |0    |  -     | Receive           |  -  |524291|   -   
|0  |10.0.0.179/32     |ROUTE| Et24               |1031 |103421  | c0:f8:7f:6a:4e:1c |  -  |288362|   -   
|0  |10.0.0.254/32     |ROUTE| Et24               |1031 |103421  | c0:f8:7f:6a:4e:1c |  -  |288362|   -   
|0  |10.0.1.49/32      |ROUTE| Et24               |1031 |103421  | c0:f8:7f:6a:4e:1c |  -  |288362|   -   
|0  |10.0.1.55/32      |ROUTE| Et24               |1031 |103421  | c0:f8:7f:6a:4e:1c |  -  |288362|   -   
|0  |20.5.149.0/24     |ROUTE| Et24               |1031 |103421  | c0:f8:7f:6a:4e:1c |  -  |288362|   -   
|0  |20.19.149.0/24    |ROUTE| Et24               |1031 |103421  | c0:f8:7f:6a:4e:1c |  -  |288362|   -   
|0  |20.24.149.0/24    |ROUTE| Et24               |1031 |103421  | c0:f8:7f:6a:4e:1c |  -  |288362|   -   
|0  |20.47.149.0/24    |ROUTE| Et24               |1031 |103421  | c0:f8:7f:6a:4e:1c |  -  |288362|   -   
|0  |20.47.170.0/24    |ROUTE| Et1                |1050 |103422  | 28:99:3a:06:b4:e1 |  -  |288366|   -   
|0  |20.57.59.0/24     |ROUTE| Et24               |1031 |103421  | c0:f8:7f:6a:4e:1c |16384|288369|   -   
|0  |20.57.59.0/24     |ROUTE| Et1                |1050 |103422  | 28:99:3a:06:b4:e1 |16384|288370|   -   
|0  |20.57.149.0/24    |ROUTE| Et24               |1031 |103421  | c0:f8:7f:6a:4e:1c |  -  |288362|   -   
|0  |20.57.170.0/24    |ROUTE| Et1                |1050 |103422  | 28:99:3a:06:b4:e1 |  -  |288366|   -   
|0  |20.111.149.0/24   |ROUTE| Et24               |1031 |103421  | c0:f8:7f:6a:4e:1c |  -  |288362|   -   
|0  |20.143.149.0/24   |ROUTE| Et24               |1031 |103421  | c0:f8:7f:6a:4e:1c |  -  |288362|   -   
|0  |20.149.155.0/24   |ROUTE| Et24               |1031 |103421  | c0:f8:7f:6a:4e:1c |  -  |288362|   -   
|0  |20.149.171.0/32   |TRAP | CoppSystemIpBcast  |0    |  -     | BcastReceive      |  -  |524288|   -   
|0  |20.149.171.149/32 |ROUTE| Et24               |1031 |103421  | c0:f8:7f:6a:4e:1c |  -  |288363|   -   
|0  |20.149.171.171/32 |TRAP | CoppSystemIpUcast  |0    |  -     | Receive           |  -  |524291|   -   
|0  |20.149.171.255/32 |TRAP | CoppSystemIpBcast  |0    |  -     | BcastReceive      |  -  |524288|   -   
|0  |20.149.171.0/24   |TRAP | CoppSystemL3DstMiss|1031 |1031    | ArpTrap           |  -  |525325|   -   
|0  |20.149.254.0/24   |ROUTE| Et24               |1031 |103421  | c0:f8:7f:6a:4e:1c |  -  |288362|   -   
|0  |20.155.179.0/24   |ROUTE| Et24               |1031 |103421  | c0:f8:7f:6a:4e:1c |  -  |288362|   -   
|0  |20.170.171.0/32   |TRAP | CoppSystemIpBcast  |0    |  -     | BcastReceive      |  -  |524288|   -   
|0  |20.170.171.170/32 |ROUTE| Et1                |1050 |103422  | 28:99:3a:06:b4:e1 |  -  |288364|   -   
|0  |20.170.171.171/32 |TRAP | CoppSystemIpUcast  |0    |  -     | Receive           |  -  |524291|   -   
|0  |20.170.171.255/32 |TRAP | CoppSystemIpBcast  |0    |  -     | BcastReceive      |  -  |524288|   -   
|0  |20.170.171.0/24   |TRAP | CoppSystemL3DstMiss|1050 |1050    | ArpTrap           |  -  |525344|   -   
|0  |20.170.254.0/24   |ROUTE| Et1                |1050 |103422  | 28:99:3a:06:b4:e1 |  -  |288366|   -   
|0  |20.171.254.0/24   |ROUTE| Et24               |1031 |103421  | c0:f8:7f:6a:4e:1c |  -  |288362|   -   
|0  |100.0.1.111/32    |ROUTE| Et24               |1031 |103421  | c0:f8:7f:6a:4e:1c |  -  |288362|   -   
|0  |127.0.0.0/8       |TRAP | CoppSystemL3DstMiss|0    |  -     | ArpTrap           |  -  |524294|   -   
|0  |192.168.20.0/23   |ROUTE| Et24               |1031 |103421  | c0:f8:7f:6a:4e:1c |  -  |288362|   -   
|0  |192.168.0.0/19    |ROUTE| Et24               |1031 |103421  | c0:f8:7f:6a:4e:1c |  -  |288362|   -   
|0  |0.0.0.0/0         |TRAP | CoppSystemL3LpmOver|0    |  -     | SlowReceive       |  -  |524292|   -   
|1  |0.0.0.0/8         |DROP | DROP               |0    |  -     |                   |  -  |288361|   -   
|1  |127.0.0.0/8       |TRAP | CoppSystemL3DstMiss|0    |  -     | ArpTrap           |  -  |524294|   -   
|1  |192.168.20.0/32   |TRAP | CoppSystemIpBcast  |0    |  -     | BcastReceive      |  -  |524288|   -   
|1  |192.168.20.171/32 |TRAP | CoppSystemIpUcast  |0    |  -     | Receive           |  -  |524291|   -   
|1  |192.168.21.255/32 |TRAP | CoppSystemIpBcast  |0    |  -     | BcastReceive      |  -  |524288|   -   
|1  |192.168.20.0/23   |TRAP | CoppSystemL3DstMiss|0    |  -     | ArpTrap           |  -  |524294|   -   
|1  |0.0.0.0/0         |TRAP | CoppSystemL3DstMiss|0    |  -     | ArpTrap           |  -  |524294|   -   
|2  |0.0.0.0/8         |DROP | DROP               |0    |  -     |                   |  -  |288365|   -   
|2  |20.5.111.0/24     |ROUTE| FEC 288372         |0    |2097145 | 00:00:00:00:00:00 |  -  |157294|M 20005 68001
|2  |20.19.111.0/24    |ROUTE| FEC 288372         |0    |2097149 | 00:00:00:00:00:00 |  -  |157291|M 20019 1279
|2  |20.24.111.0/24    |ROUTE| FEC 288372         |0    |2097150 | 00:00:00:00:00:00 |  -  |157290|M 20024 56510
|2  |20.47.111.0/24    |ROUTE| FEC 16385          |0    |2097146 | 00:00:00:00:00:00 |  -  |157293|M 20047 720896
|2  |20.55.111.0/24    |ROUTE| FEC 288372         |0    |2097151 | 00:00:00:00:00:00 |  -  |157289|M 20355 24004
|2  |20.57.111.0/24    |ROUTE| FEC 16385          |0    |2097144 | 00:00:00:00:00:00 |  -  |157295|M 20057 524287
|2  |20.111.111.0/24   |ROUTE| FEC 288375         |0    |2097147 | 00:00:00:00:00:00 |  -  |157288|M 20411 16
|2  |20.111.171.0/32   |TRAP | CoppSystemIpBcast  |0    |  -     | BcastReceive      |  -  |524288|   -   
|2  |20.111.171.1/32   |ROUTE| Et5                |1033 |103423  | 00:14:01:00:00:01 |  -  |288371|   -   
|2  |20.111.171.171/32 |TRAP | CoppSystemIpUcast  |0    |  -     | Receive           |  -  |524291|   -   
|2  |20.111.171.255/32 |TRAP | CoppSystemIpBcast  |0    |  -     | BcastReceive      |  -  |524288|   -   
|2  |20.111.171.0/24   |TRAP | CoppSystemL3DstMiss|1033 |1033    | ArpTrap           |  -  |525327|   -   
|2  |20.111.254.0/24   |ROUTE| FEC 288372         |0    |2097148 | 00:00:00:00:00:00 |  -  |157292|M 20254 48060
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
|16384|288369|ROUTE| Et24               |1031 |103421  | c0:f8:7f:6a:4e:1c |   -   
|16384|288370|ROUTE| Et1                |1050 |103422  | 28:99:3a:06:b4:e1 |   -   
|16385|288376|ROUTE| Et24               |1031 |103421  | c0:f8:7f:6a:4e:1c |   -   
|16385|288377|ROUTE| Et1                |1050 |103422  | 28:99:3a:06:b4:e1 |   -   
|  -  |157288|ROUTE| FEC 288375         |   - |2097147 |                 - |Mpush 20411 16
|  -  |157289|ROUTE| FEC 288372         |   - |2097151 |                 - |Mpush 20355 24004
|  -  |157290|ROUTE| FEC 288372         |   - |2097150 |                 - |Mpush 20024 56510
|  -  |157291|ROUTE| FEC 288372         |   - |2097149 |                 - |Mpush 20019 1279
|  -  |157292|ROUTE| FEC 288372         |   - |2097148 |                 - |Mpush 20254 48060
|  -  |157293|ROUTE| FEC 16385          |   - |2097146 |                 - |Mpush 20047 720896
|  -  |157294|ROUTE| FEC 288372         |   - |2097145 |                 - |Mpush 20005 68001
|  -  |157295|ROUTE| FEC 16385          |   - |2097144 |                 - |Mpush 20057 524287
|  -  |288360|DROP | DROP               |0    |  -     |                   |   -   
|  -  |288361|DROP | DROP               |0    |  -     |                   |   -   
|  -  |288362|ROUTE| Et24               |1031 |103421  | c0:f8:7f:6a:4e:1c |   -   
|  -  |288363|ROUTE| Et24               |1031 |103421  | c0:f8:7f:6a:4e:1c |   -   
|  -  |288364|ROUTE| Et1                |1050 |103422  | 28:99:3a:06:b4:e1 |   -   
|  -  |288365|DROP | DROP               |0    |  -     |                   |   -   
|  -  |288366|ROUTE| Et1                |1050 |103422  | 28:99:3a:06:b4:e1 |   -   
|  -  |288367|ROUTE| Et24               |1031 |103421  | c0:f8:7f:6a:4e:1c |   -   
|  -  |288368|ROUTE| Et1                |1050 |103422  | 28:99:3a:06:b4:e1 |   -   
|  -  |288371|ROUTE| Et5                |1033 |103423  | 00:14:01:00:00:01 |   -   
|  -  |288372|ROUTE| Et24               |1031 |103421  | c0:f8:7f:6a:4e:1c |   -   
|  -  |288373|ROUTE| Et1                |1050 |103422  | 28:99:3a:06:b4:e1 |   -   
|  -  |288374|ROUTE| Et24               |1031 |103421  | c0:f8:7f:6a:4e:1c |   -   
|  -  |288375|ROUTE| Et24               |1031 |103421  | c0:f8:7f:6a:4e:1c |   -   
|  -  |524288|TRAP | CoppSystemIpBcast  |0    |  -     | BcastReceive      |   -   
|  -  |524291|TRAP | CoppSystemIpUcast  |0    |  -     | Receive           |   -   
|  -  |524292|TRAP | CoppSystemL3LpmOver|0    |  -     | SlowReceive       |   -   
|  -  |524293|TRAP | CoppSystemL3LpmOver|0    |  -     | SlowReceive       |   -   
|  -  |524294|TRAP | CoppSystemL3DstMiss|0    |  -     | ArpTrap           |   -   
|  -  |525325|TRAP | CoppSystemL3DstMiss|1031 |1031    | ArpTrap           |   -   
|  -  |525327|TRAP | CoppSystemL3DstMiss|1033 |1033    | ArpTrap           |   -   
|  -  |525344|TRAP | CoppSystemL3DstMiss|1050 |1050    | ArpTrap           |   -   

```

