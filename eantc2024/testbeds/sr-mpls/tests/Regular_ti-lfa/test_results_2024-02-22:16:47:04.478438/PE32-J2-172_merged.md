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

Uptime: 59 minutes
Total memory: 8099732 kB
Free memory: 5482044 kB

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
Ethernet5.2     20.111.172.172/24   up           up              1500          
Ethernet5.171   20.111.172.172/24   up           up              1500          
Ethernet45      20.172.211.172/24   down         notpresent      1500          
Ethernet47      20.171.172.172/24   admin down   down            1500          
Ethernet49/1    20.57.172.172/24    admin down   down            1500          
Ethernet50/1    20.32.172.172/24    up           up              1500          
Ethernet51/1    20.47.172.172/24    up           up              1500          
Loopback0       10.0.0.172/32       up           up             65535          
Management1     192.168.20.172/23   up           up              1500          

```

## show interfaces counters rates | nz

```text
Port      Name        Intvl  In Mbps      %  In Kpps Out Mbps      % Out Kpps
Et5                    0:05     79.7   0.8%        9     79.6   0.8%        9
Et50/1    Ribbon_32    0:05     76.7   0.8%        9     76.8   0.8%        9
Et51/1    ERIKSON_47   0:05      3.0   0.0%        0      2.9   0.0%        0
Ma1                    0:05      0.1   0.0%        0     22.8   2.3%        1
```

## show isis neighbors

```text
 
Instance  VRF      System Id        Type Interface          SNPA              State Hold time   Circuit Id          
IGP       default  Ribbon-32        L2   Ethernet50/1       P2P               UP    81          00                  
IGP       default  Ericsson_47      L2   Ethernet51/1       P2P               UP    22          02                  
```

## show isis database detail

```text
Legend:
H - hostname conflict
U - node unreachable

IS-IS Instance: IGP VRF: default
  IS-IS Level 2 Link State Database
    LSPID                   Seq Num  Cksum  Life Length IS  Received LSPID        Flags
    h3c_19_CR16010E-F.00-00      2221  25455  1186    403 L2  0000.0000.0019.00-00  <>
      Remaining lifetime received: 1197 s Modified to: 1200 s
      NLPID: 0xCC(IPv4)
      Hostname: h3c_19_CR16010E-F
      Area addresses: 49
      Interface address: 10.0.0.19
      Interface address: 20.19.32.19
      Interface address: 20.19.47.19
      IS Neighbor          : Ribbon-32.00        Metric: 10
        IPv4 Neighbor Address: 20.19.32.32
        IPv4 Interface Address: 20.19.32.19
        Adj-sid: 1661 flags: [L V] weight: 0x0
      IS Neighbor          : Ericsson_47.00      Metric: 10
        IPv4 Neighbor Address: 20.19.47.47
        IPv4 Interface Address: 20.19.47.19
        Adj-sid: 1662 flags: [L V] weight: 0x0
      Reachability         : 10.0.0.19/32 Metric: 0 Type: 1 Up
        SR Prefix-SID: 19 Flags: [N] Algorithm: 0
      Reachability         : 20.19.32.0/24 Metric: 10 Type: 1 Up
      Reachability         : 20.19.47.0/24 Metric: 10 Type: 1 Up
      Reachability         : 192.168.0.0/19 Metric: 0 Type: 1 Up
      Router Capabilities: Router Id: 10.0.0.19 Flags: []
        Maximum SID depth:
          Base MPLS imposition (MSD type 1):  13
        SR Capability: Flags: [I]
          SRGB Base: 20000 Range: 2000
 U  eantc-jcnr2.00-00           684  21012   842    229 L2  0000.0000.0020.00-00  <>
      Remaining lifetime received: 419 s Modified to: 1200 s
      NLPID: 0xCC(IPv4) 0x8E(IPv6)
      Hostname: eantc-jcnr2
      Area addresses: 49.0001.00
      Interface address: 10.0.0.83
      IS Neighbor          : 0000.0000.0349.00   Metric: 10
        IPv4 Neighbor Address: 20.83.149.149
        IPv4 Interface Address: 20.83.149.83
        Adj-sid: 16 flags: [L V] weight: 0x0
      Reachability         : 10.0.0.83/32 Metric: 0 Type: 1 Up
        SR Prefix-SID: 83 Flags: [N] Algorithm: 0
      Reachability         : 20.83.149.0/24 Metric: 10 Type: 1 Up
      Reachability          : fe80::cc33:4dff:fe3e:5c1d/128 Metric: 0 Type: 1 Up
      Router Capabilities: Router Id: 10.0.0.83 Flags: []
        Maximum SID depth:
          Base MPLS imposition (MSD type 1):  0
        SR Capability: Flags: [I V]
          SRGB Base: 20000 Range: 2000
        Algorithms:  0, 1
      Unsupported TLV: Type: 14 Length: 2
    Ribbon-32.00-00              35   7221   842     79 L2  0000.0000.0032.00-00  <>
      Remaining lifetime received: 1166 s Modified to: 1200 s
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
    Ribbon-32.00-03              24  25544   842     38 L2  0000.0000.0032.00-03  <>
      Remaining lifetime received: 1044 s Modified to: 1200 s
      Hostname: Ribbon-32
    Ribbon-32.00-04             274  33935  1186    285 L2  0000.0000.0032.00-04  <>
      Remaining lifetime received: 1195 s Modified to: 1200 s
      Interface address: 10.0.0.32
      Interface address: 20.19.32.32
      Interface address: 20.32.172.32
      IS Neighbor          : h3c_19_CR16010E-F.00 Metric: 10
        IPv4 Neighbor Address: 20.19.32.19
        IPv4 Interface Address: 20.19.32.32
        Adj-sid: 756647 flags: [L V] weight: 0x0
        Adj-sid: 756648 flags: [L V B] weight: 0x0
      IS Neighbor          : PE32-J2-172.00      Metric: 10
        IPv4 Neighbor Address: 20.32.172.172
        IPv4 Interface Address: 20.32.172.32
        Adj-sid: 756653 flags: [L V B] weight: 0x0
        Adj-sid: 756646 flags: [L V] weight: 0x0
      Reachability         : 10.0.0.32/32 Metric: 0 Type: 1 Up
        SR Prefix-SID: 32 Flags: [N] Algorithm: 0
      Reachability         : 20.19.32.0/24 Metric: 10 Type: 1 Up
      Reachability         : 20.32.172.0/24 Metric: 10 Type: 1 Up
    Ericsson_47.00-00            83  60816   844    325 L2  0000.0000.0047.00-00  <>
      Remaining lifetime received: 1199 s Modified to: 1200 s
      NLPID: 0xCC(IPv4)
      Hostname: Ericsson_47
      Area addresses: 49
      Interface address: 10.0.0.47
      Interface address: 2002::47
      IS Neighbor          : h3c_19_CR16010E-F.00 Metric: 10
        IPv4 Neighbor Address: 20.19.47.19
        IPv4 Interface Address: 20.19.47.47
        Adj-sid: 983042 flags: [L V] weight: 0x0
      IS Neighbor          : PE32-J2-172.00      Metric: 40
        IPv4 Neighbor Address: 20.47.172.172
        IPv4 Interface Address: 20.47.172.47
        Adj-sid: 983041 flags: [L V] weight: 0x0
      Reachability         : 10.0.0.47/32 Metric: 1 Type: 1 Up
        SR Prefix-SID: 47 Flags: [N P] Algorithm: 0
      Reachability         : 20.19.47.0/24 Metric: 10 Type: 1 Up
      Reachability         : 20.47.172.0/24 Metric: 40 Type: 1 Up
      Router Capabilities: Router Id: 10.0.0.47 Flags: []
        Maximum SID depth:
          Base MPLS imposition (MSD type 1):  8
        SR Capability: Flags: [I]
          SRGB Base: 20000 Range: 2000
        Algorithms:  0
 U  huawei_254_NetEngine_8000_F8.00-00      8982  64813   843    220 L2  0000.0000.0254.00-00  <>
      Remaining lifetime received: 419 s Modified to: 1200 s
      NLPID: 0xCC(IPv4)
      Hostname: huawei_254_NetEngine_8000_F8
      Area addresses: 49
      Interface address: 10.0.0.254
      Interface address: 20.57.254.254
      Interface address: 20.179.254.254
      Interface address: 20.149.254.254
      IS Neighbor          : 0000.0001.7900.00   Metric: 10
        IPv4 Neighbor Address: 20.179.254.179
        IPv4 Interface Address: 20.179.254.254
        Adj-sid: 48041 flags: [L V] weight: 0x0
      IS Neighbor          : 0000.0000.0349.00   Metric: 10
        IPv4 Neighbor Address: 20.149.254.149
        IPv4 Interface Address: 20.149.254.254
        Adj-sid: 48043 flags: [L V] weight: 0x0
      Reachability         : 10.0.0.254/32 Metric: 0 Type: 1 Up
        SR Prefix-SID: 254 Flags: [N] Algorithm: 0
      Reachability         : 20.57.254.0/24 Metric: 10 Type: 1 Up
      Reachability         : 20.179.254.0/24 Metric: 10 Type: 1 Up
      Reachability         : 20.149.254.0/24 Metric: 10 Type: 1 Up
      Router Capabilities: Router Id: 10.0.0.254 Flags: []
        Maximum SID depth:
          Base MPLS imposition (MSD type 1):  10
        SR Capability: Flags: [I]
          SRGB Base: 20000 Range: 2000
 U  PE31-J2-171.00-00           553  37534   843    275 L2  0100.0000.0171.00-00  <>
      Remaining lifetime received: 1199 s Modified to: 1200 s
      NLPID: 0xCC(IPv4)
      Hostname: PE31-J2-171
      Area addresses: 49.0000
      Interface address: 20.171.172.171
      Interface address: 20.57.171.171
      Interface address: 10.0.0.171
      IS Neighbor          : PE32-J2-172.00      Metric: 10
        IPv4 Neighbor Address: 20.171.172.172
        IPv4 Interface Address: 20.171.172.171
        Adj-sid: 362146 flags: [L V] weight: 0x0
      Reachability         : 20.171.172.0/24 Metric: 10 Type: 1 Up
      Reachability         : 10.0.0.171/32 Metric: 0 Type: 1 Up
        SR Prefix-SID: 171 Flags: [N] Algorithm: 0
        SR Prefix-SID: 1171 Flags: [N] Algorithm: 128
        SR Prefix-SID: 1271 Flags: [N] Algorithm: 129
        SR Prefix-SID: 1371 Flags: [N] Algorithm: 130
        SR Prefix-SID: 1471 Flags: [N] Algorithm: 131
      Reachability         : 20.57.171.0/24 Metric: 10 Type: 1 Up
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
    PE32-J2-172.00-00            77   3911  1181    310 L2  0100.0000.0172.00-00  <>
      LSP generation remaining wait time: 0 ms
      Time remaining until refresh: 881 s
      NLPID: 0xCC(IPv4)
      Hostname: PE32-J2-172
      Area addresses: 49.0000
      Interface address: 20.32.172.172
      Interface address: 20.47.172.172
      Interface address: 10.0.0.172
      IS Neighbor          : Ribbon-32.00        Metric: 10
        IPv4 Neighbor Address: 20.32.172.32
        IPv4 Interface Address: 20.32.172.172
        Adj-sid: 394917 flags: [L V B] weight: 0x0
      IS Neighbor          : Ericsson_47.00      Metric: 30
        IPv4 Neighbor Address: 20.47.172.47
        IPv4 Interface Address: 20.47.172.172
        Adj-sid: 394916 flags: [L V B] weight: 0x0
      Reachability         : 20.32.172.0/24 Metric: 10 Type: 1 Up
      Reachability         : 20.47.172.0/24 Metric: 30 Type: 1 Up
      Reachability         : 10.0.0.172/32 Metric: 0 Type: 1 Up
        SR Prefix-SID: 172 Flags: [N] Algorithm: 0
        SR Prefix-SID: 1272 Flags: [N] Algorithm: 129
        SR Prefix-SID: 1372 Flags: [N] Algorithm: 130
        SR Prefix-SID: 1472 Flags: [N] Algorithm: 131
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
    h3c_19_CR16010E-F.00-00      2221  25455  1185    403 L2  0000.0000.0019.00-00  <>
      Remaining lifetime received: 1197 s Modified to: 1200 s
      NLPID: 0xCC(IPv4)
      Hostname: h3c_19_CR16010E-F
      TE IPv4 router ID: 10.0.0.19
      Area addresses: 49
      Interface address: 10.0.0.19
      Interface address: 20.19.32.19
      Interface address: 20.19.47.19
      IS Neighbor          : Ribbon-32.00        Metric: 10
        IPv4 Neighbor Address: 20.19.32.32
        IPv4 Interface Address: 20.19.32.19
        Adj-sid: 1661 flags: [L V] weight: 0x0
        TE default metric: 10
        Maximum link BW: 0.00 bps
        Maximum reservable link BW: 0.00 bps
        Unreserved BW:
            TE class 0: 0.00 bps	TE class 1: 0.00 bps	TE class 2: 0.00 bps
            TE class 3: 0.00 bps	TE class 4: 0.00 bps	TE class 5: 0.00 bps
            TE class 6: 0.00 bps	TE class 7: 0.00 bps
      IS Neighbor          : Ericsson_47.00      Metric: 10
        IPv4 Neighbor Address: 20.19.47.47
        IPv4 Interface Address: 20.19.47.19
        Adj-sid: 1662 flags: [L V] weight: 0x0
        TE default metric: 10
        Maximum link BW: 0.00 bps
        Maximum reservable link BW: 0.00 bps
        Unreserved BW:
            TE class 0: 0.00 bps	TE class 1: 0.00 bps	TE class 2: 0.00 bps
            TE class 3: 0.00 bps	TE class 4: 0.00 bps	TE class 5: 0.00 bps
            TE class 6: 0.00 bps	TE class 7: 0.00 bps
      Reachability         : 10.0.0.19/32 Metric: 0 Type: 1 Up
        SR Prefix-SID: 19 Flags: [N] Algorithm: 0
      Reachability         : 20.19.32.0/24 Metric: 10 Type: 1 Up
      Reachability         : 20.19.47.0/24 Metric: 10 Type: 1 Up
      Reachability         : 192.168.0.0/19 Metric: 0 Type: 1 Up
      Router Capabilities: Router Id: 10.0.0.19 Flags: []
        Maximum SID depth:
          Base MPLS imposition (MSD type 1):  13
        SR Capability: Flags: [I]
          SRGB Base: 20000 Range: 2000
 U  eantc-jcnr2.00-00           684  21012   842    229 L2  0000.0000.0020.00-00  <>
      Remaining lifetime received: 419 s Modified to: 1200 s
      NLPID: 0xCC(IPv4) 0x8E(IPv6)
      Hostname: eantc-jcnr2
      TE IPv4 router ID: 10.0.0.83
      TE IPv6 router ID: ::7f00:1
      Area addresses: 49.0001.00
      Interface address: 10.0.0.83
      IS Neighbor          : 0000.0000.0349.00   Metric: 10
        IPv4 Neighbor Address: 20.83.149.149
        IPv4 Interface Address: 20.83.149.83
        Adj-sid: 16 flags: [L V] weight: 0x0
      Reachability         : 10.0.0.83/32 Metric: 0 Type: 1 Up
        SR Prefix-SID: 83 Flags: [N] Algorithm: 0
      Reachability         : 20.83.149.0/24 Metric: 10 Type: 1 Up
      Reachability          : fe80::cc33:4dff:fe3e:5c1d/128 Metric: 0 Type: 1 Up
      Router Capabilities: Router Id: 10.0.0.83 Flags: []
        Maximum SID depth:
          Base MPLS imposition (MSD type 1):  0
        SR Capability: Flags: [I V]
          SRGB Base: 20000 Range: 2000
        Algorithms:  0, 1
      Unsupported TLV: Type: 14 Length: 2
    Ribbon-32.00-00              35   7221   842     79 L2  0000.0000.0032.00-00  <>
      Remaining lifetime received: 1166 s Modified to: 1200 s
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
    Ribbon-32.00-03              24  25544   842     38 L2  0000.0000.0032.00-03  <>
      Remaining lifetime received: 1044 s Modified to: 1200 s
      Hostname: Ribbon-32
    Ribbon-32.00-04             274  33935  1185    285 L2  0000.0000.0032.00-04  <>
      Remaining lifetime received: 1195 s Modified to: 1200 s
      Interface address: 10.0.0.32
      Interface address: 20.19.32.32
      Interface address: 20.32.172.32
      IS Neighbor          : h3c_19_CR16010E-F.00 Metric: 10
        IPv4 Neighbor Address: 20.19.32.19
        IPv4 Interface Address: 20.19.32.32
        Adj-sid: 756647 flags: [L V] weight: 0x0
        Adj-sid: 756648 flags: [L V B] weight: 0x0
        TE default metric: 10
        Maximum link BW: 0.00 bps
        Maximum reservable link BW: 0.00 bps
        Unreserved BW:
            TE class 0: 0.00 bps	TE class 1: 0.00 bps	TE class 2: 0.00 bps
            TE class 3: 0.00 bps	TE class 4: 0.00 bps	TE class 5: 0.00 bps
            TE class 6: 0.00 bps	TE class 7: 0.00 bps
      IS Neighbor          : PE32-J2-172.00      Metric: 10
        IPv4 Neighbor Address: 20.32.172.172
        IPv4 Interface Address: 20.32.172.32
        Adj-sid: 756653 flags: [L V B] weight: 0x0
        Adj-sid: 756646 flags: [L V] weight: 0x0
        TE default metric: 10
        Maximum link BW: 10.00 Gbps
        Maximum reservable link BW: 10.00 Gbps
        Unreserved BW:
            TE class 0: 10.00 Gbps	TE class 1: 10.00 Gbps	TE class 2: 10.00 Gbps
            TE class 3: 10.00 Gbps	TE class 4: 10.00 Gbps	TE class 5: 10.00 Gbps
            TE class 6: 10.00 Gbps	TE class 7: 10.00 Gbps
      Reachability         : 10.0.0.32/32 Metric: 0 Type: 1 Up
        SR Prefix-SID: 32 Flags: [N] Algorithm: 0
      Reachability         : 20.19.32.0/24 Metric: 10 Type: 1 Up
      Reachability         : 20.32.172.0/24 Metric: 10 Type: 1 Up
    Ericsson_47.00-00            83  60816   844    325 L2  0000.0000.0047.00-00  <>
      Remaining lifetime received: 1199 s Modified to: 1200 s
      NLPID: 0xCC(IPv4)
      Hostname: Ericsson_47
      TE IPv4 router ID: 10.0.0.47
      Area addresses: 49
      Interface address: 10.0.0.47
      Interface address: 2002::47
      IS Neighbor          : h3c_19_CR16010E-F.00 Metric: 10
        IPv4 Neighbor Address: 20.19.47.19
        IPv4 Interface Address: 20.19.47.47
        Adj-sid: 983042 flags: [L V] weight: 0x0
        Maximum link BW: 100.00 Gbps
        Maximum reservable link BW: 100.00 Gbps
        Unreserved BW:
            TE class 0: 100.00 Gbps	TE class 1: 100.00 Gbps	TE class 2: 100.00 Gbps
            TE class 3: 100.00 Gbps	TE class 4: 100.00 Gbps	TE class 5: 100.00 Gbps
            TE class 6: 100.00 Gbps	TE class 7: 100.00 Gbps
      IS Neighbor          : PE32-J2-172.00      Metric: 40
        IPv4 Neighbor Address: 20.47.172.172
        IPv4 Interface Address: 20.47.172.47
        Adj-sid: 983041 flags: [L V] weight: 0x0
        Maximum link BW: 100.00 Gbps
        Maximum reservable link BW: 100.00 Gbps
        Unreserved BW:
            TE class 0: 100.00 Gbps	TE class 1: 100.00 Gbps	TE class 2: 100.00 Gbps
            TE class 3: 100.00 Gbps	TE class 4: 100.00 Gbps	TE class 5: 100.00 Gbps
            TE class 6: 100.00 Gbps	TE class 7: 100.00 Gbps
      Reachability         : 10.0.0.47/32 Metric: 1 Type: 1 Up
        SR Prefix-SID: 47 Flags: [N P] Algorithm: 0
      Reachability         : 20.19.47.0/24 Metric: 10 Type: 1 Up
      Reachability         : 20.47.172.0/24 Metric: 40 Type: 1 Up
      Router Capabilities: Router Id: 10.0.0.47 Flags: []
        Maximum SID depth:
          Base MPLS imposition (MSD type 1):  8
        SR Capability: Flags: [I]
          SRGB Base: 20000 Range: 2000
        Algorithms:  0
 U  huawei_254_NetEngine_8000_F8.00-00      8982  64813   842    220 L2  0000.0000.0254.00-00  <>
      Remaining lifetime received: 419 s Modified to: 1200 s
      NLPID: 0xCC(IPv4)
      Hostname: huawei_254_NetEngine_8000_F8
      Area addresses: 49
      Interface address: 10.0.0.254
      Interface address: 20.57.254.254
      Interface address: 20.179.254.254
      Interface address: 20.149.254.254
      IS Neighbor          : 0000.0001.7900.00   Metric: 10
        IPv4 Neighbor Address: 20.179.254.179
        IPv4 Interface Address: 20.179.254.254
        Adj-sid: 48041 flags: [L V] weight: 0x0
      IS Neighbor          : 0000.0000.0349.00   Metric: 10
        IPv4 Neighbor Address: 20.149.254.149
        IPv4 Interface Address: 20.149.254.254
        Adj-sid: 48043 flags: [L V] weight: 0x0
        Min/Max unidirectional link delay: 217/375 us
      Reachability         : 10.0.0.254/32 Metric: 0 Type: 1 Up
        SR Prefix-SID: 254 Flags: [N] Algorithm: 0
      Reachability         : 20.57.254.0/24 Metric: 10 Type: 1 Up
      Reachability         : 20.179.254.0/24 Metric: 10 Type: 1 Up
      Reachability         : 20.149.254.0/24 Metric: 10 Type: 1 Up
      Router Capabilities: Router Id: 10.0.0.254 Flags: []
        Maximum SID depth:
          Base MPLS imposition (MSD type 1):  10
        SR Capability: Flags: [I]
          SRGB Base: 20000 Range: 2000
 U  PE31-J2-171.00-00           553  37534   842    275 L2  0100.0000.0171.00-00  <>
      Remaining lifetime received: 1199 s Modified to: 1200 s
      NLPID: 0xCC(IPv4)
      Hostname: PE31-J2-171
      Area addresses: 49.0000
      Interface address: 20.171.172.171
      Interface address: 20.57.171.171
      Interface address: 10.0.0.171
      IS Neighbor          : PE32-J2-172.00      Metric: 10
        IPv4 Neighbor Address: 20.171.172.172
        IPv4 Interface Address: 20.171.172.171
        Adj-sid: 362146 flags: [L V] weight: 0x0
        Application Specific Link Attributes:
          Standard applications: Flex-Algo
            TE default metric: 12
            Min/Max unidirectional link delay: 11/11 us
      Reachability         : 20.171.172.0/24 Metric: 10 Type: 1 Up
      Reachability         : 10.0.0.171/32 Metric: 0 Type: 1 Up
        SR Prefix-SID: 171 Flags: [N] Algorithm: 0
        SR Prefix-SID: 1171 Flags: [N] Algorithm: 128
        SR Prefix-SID: 1271 Flags: [N] Algorithm: 129
        SR Prefix-SID: 1371 Flags: [N] Algorithm: 130
        SR Prefix-SID: 1471 Flags: [N] Algorithm: 131
      Reachability         : 20.57.171.0/24 Metric: 10 Type: 1 Up
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
    PE32-J2-172.00-00            77   3911  1180    310 L2  0100.0000.0172.00-00  <>
      LSP generation remaining wait time: 0 ms
      Time remaining until refresh: 880 s
      NLPID: 0xCC(IPv4)
      Hostname: PE32-J2-172
      Area addresses: 49.0000
      Interface address: 20.32.172.172
      Interface address: 20.47.172.172
      Interface address: 10.0.0.172
      IS Neighbor          : Ribbon-32.00        Metric: 10
        IPv4 Neighbor Address: 20.32.172.32
        IPv4 Interface Address: 20.32.172.172
        Adj-sid: 394917 flags: [L V B] weight: 0x0
        Application Specific Link Attributes:
          Standard applications: Flex-Algo
            TE default metric: 12
            Min/Max unidirectional link delay: 11/11 us
      IS Neighbor          : Ericsson_47.00      Metric: 30
        IPv4 Neighbor Address: 20.47.172.47
        IPv4 Interface Address: 20.47.172.172
        Adj-sid: 394916 flags: [L V B] weight: 0x0
        Application Specific Link Attributes:
          Standard applications: Flex-Algo
            TE default metric: 12
            Min/Max unidirectional link delay: 11/11 us
      Reachability         : 20.32.172.0/24 Metric: 10 Type: 1 Up
      Reachability         : 20.47.172.0/24 Metric: 30 Type: 1 Up
      Reachability         : 10.0.0.172/32 Metric: 0 Type: 1 Up
        SR Prefix-SID: 172 Flags: [N] Algorithm: 0
        SR Prefix-SID: 1272 Flags: [N] Algorithm: 129
        SR Prefix-SID: 1372 Flags: [N] Algorithm: 130
        SR Prefix-SID: 1472 Flags: [N] Algorithm: 131
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
------------- ---------- ----- ------- -----------
MIN-TE        yes        L2    TE      PE32-J2-172
MIN-IGP       yes        L2    default PE32-J2-172
MIN-IGP-ADMIN yes        L2    default PE32-J2-172

```

## show isis flex-algo path detail

```text
Flex algo paths for IPv4 address family
Topology ID: Level-2
Destination: PE32-J2-172
Path ID: 641
Path constraints: algo MIN-TE
                  metric type TE
Request sequence number: 10
Response sequence number: 10
Number of times path updated: 10
Last updated: 0:00:38 ago
Next Hop Interface
-------- ---------

Destination: PE32-J2-172
Path ID: 642
Path constraints: algo MIN-IGP
                  metric type IGP
                  administrative-group exclude 1
Request sequence number: 10
Response sequence number: 10
Number of times path updated: 10
Last updated: 0:00:38 ago
Next Hop Interface
-------- ---------

Destination: PE32-J2-172
Path ID: 643
Path constraints: algo MIN-IGP-ADMIN
                  metric type IGP
                  administrative-group exclude 127
Request sequence number: 7
Response sequence number: 7
Number of times path updated: 7
Last updated: 0:00:38 ago
Next Hop Interface
-------- ---------

```

## show isis segment-routing tunnel

```text
  Index     Endpoint         Next Hop/Tunnel Index     Interface      Labels   
--------- ---------------- ------------------------- ---------------- ---------
  1         10.0.0.32/32     TI-LFA (4)                -              [ 3 ]    
  2         10.0.0.47/32     20.32.172.32              Ethernet50/1   [ 20047 ]
                             20.47.172.47              Ethernet51/1   [ 20047 ]
  5         10.0.0.19/32     TI-LFA (5)                -              [ 20019 ]

```

## show isis segment-routing prefix-segments

```text

System ID: PE32-J2-172			Instance: 'IGP'
SR supported Data-plane: MPLS			SR Router ID: 10.0.0.172

Node: 7      Proxy-Node: 0      Prefix: 0       Total Segments: 7

Flag Descriptions: R: Re-advertised, N: Node Segment, P: no-PHP
                   E: Explicit-NULL, V: Value, L: Local
Segment status codes: * - Self originated Prefix, L1 - level 1, L2 - level 2, ! - SR-unreachable,
                      # - Some IS-IS next-hops are SR-unreachable
   Prefix                      SID Type       Flags                        System ID       Level Protection  Algorithm   
   ------------------------- ----- ---------- ---------------------------- --------------- ----- ----------- -------------
   10.0.0.19/32                 19 Node       R:0 N:1 P:0 E:0 V:0 L:0      h3c_19_CR16010E-F L2    node        SPF         
   10.0.0.32/32                 32 Node       R:0 N:1 P:0 E:0 V:0 L:0      Ribbon-32       L2    node        SPF         
   10.0.0.47/32                 47 Node       R:0 N:1 P:1 E:0 V:0 L:0      Ericsson_47     L2    unprotected SPF         
*  10.0.0.172/32               172 Node       R:0 N:1 P:0 E:0 V:0 L:0      PE32-J2-172     L2    unprotected SPF         
*  10.0.0.172/32              1272 Node       R:0 N:1 P:0 E:0 V:0 L:0      PE32-J2-172     L2    unprotected MIN-TE      
*  10.0.0.172/32              1372 Node       R:0 N:1 P:0 E:0 V:0 L:0      PE32-J2-172     L2    unprotected MIN-IGP     
*  10.0.0.172/32              1472 Node       R:0 N:1 P:0 E:0 V:0 L:0      PE32-J2-172     L2    unprotected MIN-IGP-ADMIN
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

 I L2     10.0.0.19/32 [115/20]
           via 20.32.172.32, Ethernet50/1
 I L2     10.0.0.32/32 [115/10]
           via 20.32.172.32, Ethernet50/1
 I L2     10.0.0.47/32 [115/31]
           via 20.32.172.32, Ethernet50/1
           via 20.47.172.47, Ethernet51/1
 C        10.0.0.172/32
           directly connected, Loopback0
 I L2     20.19.32.0/24 [115/20]
           via 20.32.172.32, Ethernet50/1
 I L2     20.19.47.0/24 [115/30]
           via 20.32.172.32, Ethernet50/1
 C        20.32.172.0/24
           directly connected, Ethernet50/1
 C        20.47.172.0/24
           directly connected, Ethernet51/1
 I L2     192.168.0.0/19 [115/20]
           via 20.32.172.32, Ethernet50/1

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

 I L2     10.0.0.19/32 [115/20]
           via 20.32.172.32, Ethernet50/1
 I L2     10.0.0.32/32 [115/10]
           via 20.32.172.32, Ethernet50/1
 I L2     10.0.0.47/32 [115/31]
           via 20.32.172.32, Ethernet50/1
           via 20.47.172.47, Ethernet51/1
 C        10.0.0.172/32
           directly connected, Loopback0
 I L2     20.19.32.0/24 [115/20]
           via 20.32.172.32, Ethernet50/1
 I L2     20.19.47.0/24 [115/30]
           via 20.32.172.32, Ethernet50/1
 C        20.32.172.0/24
           directly connected, Ethernet50/1
 C        20.47.172.0/24
           directly connected, Ethernet51/1
 I L2     192.168.0.0/19 [115/20]
           via 20.32.172.32, Ethernet50/1


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

 B I      20.32.111.0/24 [200/0]
           via 10.0.0.32/32, IS-IS SR tunnel index 1, label 756651
              via TI-LFA tunnel index 4, label imp-null(3)
                 via 20.32.172.32, Ethernet50/1, label imp-null(3)
                 backup via 20.47.172.47, Ethernet51/1, label 20032
 C        20.111.172.0/24
           directly connected, Ethernet5.171


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
MPLS forwarding table (Label [metric] Vias) - 7 routes 
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
                  via TI-LFA tunnel index 5
                    via 20.32.172.32, Ethernet50/1, label imp-null(3)
                    backup via 20.47.172.47, Ethernet51/1, label imp-null(3)
 20032   A[1]
                via M, ::, pop
                    EgressACL: apply
                  via TI-LFA tunnel index 4
                    via 20.32.172.32, Ethernet50/1, label imp-null(3)
                    backup via 20.47.172.47, Ethernet51/1, label 20032
 20047   A[1]
                via M, forward
                    EgressACL: apply
                    20.32.172.32 Ethernet50/1
                    20.47.172.47 Ethernet51/1
 362144   [0]
                via I, ipv4, vrf OSPF-SR-L3VPN
 362146   [0]
                via I, ipv4, vrf ISIS-SR-L3VPN
 394916  A[1]
                via M, ::, pop
                    EgressACL: apply
                  via TI-LFA tunnel index 2
                    via 20.47.172.47, Ethernet51/1, label imp-null(3)
                    backup via 20.32.172.32, Ethernet50/1, label 20047
 394917  A[1]
                via M, ::, pop
                    EgressACL: apply
                  via TI-LFA tunnel index 4
                    via 20.32.172.32, Ethernet50/1, label imp-null(3)
                    backup via 20.47.172.47, Ethernet51/1, label 20032
```

## show mpls lfib route

```text
MPLS forwarding table (Label [metric] Vias) - 7 routes 
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
                via TI-LFA tunnel index 5, forward
                 payload autoDecide, ttlMode uniform, dscpMode uniform, apply egress-acl
                    via 20.32.172.32, Ethernet50/1, label imp-null(3)
                    backup via 20.47.172.47, Ethernet51/1, label imp-null(3)
 IP    20032    [1], 10.0.0.32/32
                via TI-LFA tunnel index 4, pop
                 payload autoDecide, ttlMode uniform, dscpMode uniform, apply egress-acl
                    via 20.32.172.32, Ethernet50/1, label imp-null(3)
                    backup via 20.47.172.47, Ethernet51/1, label 20032
 IP    20047    [1], 10.0.0.47/32
                via M, 20.32.172.32, forward
                 payload autoDecide, ttlMode uniform, dscpMode uniform, apply egress-acl
                 interface Ethernet50/1
                via M, 20.47.172.47, forward
                 payload autoDecide, ttlMode uniform, dscpMode uniform, apply egress-acl
                 interface Ethernet51/1
 B3    362144   [0]
                via I, ipv4, vrf OSPF-SR-L3VPN
 B3    362146   [0]
                via I, ipv4, vrf ISIS-SR-L3VPN
 IA    394916   [1]
                via TI-LFA tunnel index 2, pop
                 payload autoDecide, ttlMode uniform, apply egress-acl
                    via 20.47.172.47, Ethernet51/1, label imp-null(3)
                    backup via 20.32.172.32, Ethernet50/1, label 20047
 IA    394917   [1]
                via TI-LFA tunnel index 4, pop
                 payload autoDecide, ttlMode uniform, apply egress-acl
                    via 20.32.172.32, Ethernet50/1, label imp-null(3)
                    backup via 20.47.172.47, Ethernet51/1, label 20032
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
 * >      RD: 65000:1 IPv4 prefix 20.32.111.0/24
                                 10.0.0.32             -       100     0       i
 * >      RD: 65000:128 IPv4 prefix 20.32.111.0/24
                                 10.0.0.32             -       100     0       i
 * >      RD: 65000:129 IPv4 prefix 20.32.111.0/24
                                 10.0.0.32             -       100     0       i
 * >      RD: 65000:130 IPv4 prefix 20.32.111.0/24
                                 10.0.0.32             -       100     0       i
 * >      RD: 10.0.0.172:1 IPv4 prefix 20.111.172.0/24
                                 -                     -       -       0       i
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
BGP neighbor is 10.0.0.32, remote AS 65000, internal link
  BGP version 4, remote router ID 10.0.0.32, VRF default
  Inherits configuration from and member of peer-group IBGP-PEER
  Last read 00:00:01, last write 00:00:04
  Hold time is 180, keepalive interval is 60 seconds
  Configured hold time is 180, keepalive interval is 60 seconds
  Effective minimum hold time is 3 seconds
  Send failure hold time is 0 seconds
  Hold timer is active, time left: 00:02:59
  Keepalive timer is active, time left: 00:00:42
  Connect timer is inactive
  Idle-restart timer is inactive
  BGP state is Established, up for 00:33:28
  Number of transitions to established: 1
  Last state was OpenConfirm
  Last event was RecvKeepAlive
  Last rcvd notification:Cease/connection rejected, Last time 00:33:56, First time 00:41:15, Repeats 9
  Types of communities advertised: standard extended large
  Enhanced route refresh stale path removal disabled
  Outbound enhanced route refresh enabled
  Neighbor Capabilities:
    Multiprotocol IPv4 Unicast: advertised
    Multiprotocol VPN-IPv4: advertised and received and negotiated
    Multiprotocol L2VPN EVPN: advertised
    Four Octet ASN: advertised and received and negotiated
    Route Refresh: advertised and received and negotiated
    Enhanced route refresh: advertised and received and negotiated
    Send End-of-RIB messages: advertised
    Additional-paths recv capability:
      IPv4 Unicast: advertised
      VPN-IPv4: advertised
      L2VPN EVPN: advertised
    Additional-paths send capability:
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
    Opens:                          11         1
    Notifications:                   0        10
    Updates:                         4         4
    Keepalives:                     40        94
    Enhanced Route Refresh:          0         0
    Begin of Route Refresh:          0         0
    End of Route Refresh:            0         0
    Total messages:                 55       109
  Prefix Statistics:
                                   Sent      Rcvd     Best Paths     Best ECMP Paths
    IPv4 Unicast:                     0         0              0                   0
    VPN-IPv4:                         2         4              4                   0
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
    VPN-IPv4 NLRIs dropped due to maximum route limit violation: 0
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
Local TCP address is 10.0.0.172, local port is 179
Remote TCP address is 10.0.0.32, remote port is 36873
Local next hop for next hop self:
  VPN-IPv4: 10.0.0.172
TCP Socket Information:
  TCP state is ESTABLISHED
  Recv-Q: 0/32768
  Send-Q: 0/46080
  Outgoing Maximum Segment Size (MSS): 36
  Total Number of TCP retransmissions: 0
  Options:
    Timestamps enabled: yes
    Selective Acknowledgments enabled: yes
    Window Scale enabled: yes
    Explicit Congestion Notification (ECN) enabled: no
  Socket Statistics:
    Window Scale (wscale): 0,7
    Retransmission Timeout (rto): 204.0ms
    Round-trip Time (rtt/rtvar): 0.2ms/0.0ms
    Delayed Ack Timeout (ato): 40.0ms
    Congestion Window (cwnd): 10
    TCP Throughput: 11.66 Mbps
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
  Connect timer is active, time left: 00:00:16
  Connection interval is 148 seconds
  Failed connection attempts is 27
  Idle-restart timer is inactive
  BGP state is Active
  Number of transitions to established: 0
  Last state was Connect
  Last event was TransportError
  Last sent socket-error:Connect (Network is unreachable), Last time 00:02:23, First time 00:57:40, Repeats 26
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
  Connect timer is active, time left: 00:01:02
  Connection interval is 148 seconds
  Failed connection attempts is 27
  Idle-restart timer is inactive
  BGP state is Active
  Number of transitions to established: 0
  Last state was Connect
  Last event was TransportError
  Last sent socket-error:Connect (Network is unreachable), Last time 00:01:57, First time 00:57:39, Repeats 26
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
Local TCP address is 10.0.0.172
Remote TCP address is 10.0.1.49, remote port is 179

```

## show tunnel rib system-tunnel-rib brief

```text
Tunnel RIB: system-tunnel-rib
Endpoint     Tunnel Type   Index(es) Tunnel Preference IGP Preference IGP Metric
------------ ------------- --------- ----------------- -------------- ----------
10.0.0.19/32 IS-IS SR IPv4 5         65                115            20        
10.0.0.32/32 IS-IS SR IPv4 1         65                115            10        
10.0.0.47/32 IS-IS SR IPv4 2         65                115            31        

Metric Type
-----------
metric     
metric     
metric     

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
>C    10.0.0.172/32 [0 pref/0 metric] updated 00:57:57 ago
         via Loopback0, directly connected
>C    20.32.172.0/24 [0 pref/0 metric] updated 00:00:43 ago
         via Ethernet50/1, directly connected
>C    20.47.172.0/24 [0 pref/0 metric] updated 00:55:59 ago
         via Ethernet51/1, directly connected
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
>P    0.0.0.0/8 [1 pref/0 metric] updated 00:57:55 ago
         via Null0, directly connected [NF]
>P    127.0.0.0/8 [1 pref/0 metric] updated 00:57:55 ago
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
>I    10.0.0.19/32 [115 pref/20 metric] updated 00:00:24 ago
         via 20.32.172.32, Ethernet50/1
>I    10.0.0.32/32 [115 pref/10 metric] updated 00:00:24 ago
         via 20.32.172.32, Ethernet50/1
>I    10.0.0.47/32 [115 pref/31 metric] updated 00:00:24 ago
         via 20.32.172.32, Ethernet50/1
         via 20.47.172.47, Ethernet51/1
>I    20.19.32.0/24 [115 pref/20 metric] updated 00:00:24 ago
         via 20.32.172.32, Ethernet50/1
>I    20.19.47.0/24 [115 pref/30 metric] updated 00:00:24 ago
         via 20.32.172.32, Ethernet50/1
>I    192.168.0.0/19 [115 pref/20 metric] updated 00:00:24 ago
         via 20.32.172.32, Ethernet50/1
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
>P    ::/96 [1 pref/0 metric] updated 00:39:19 ago
         via Null0, directly connected [NF]
>P    ::ffff:127.0.0.0/104 [1 pref/0 metric] updated 00:39:19 ago
         via :: [1 pref/1 metric] type ipv6
            via , directly connected
>P    fe80::/10 [1 pref/0 metric] updated 00:39:19 ago
```

## show platform sand l3 summary

```text
Number of vrfs: 8

Ipv4:
  Routes:       43  backlog:  0  unprogrammed:  0
  Adjacencies:  41  backlog:  0  unprogrammed:  0
Ipv6:
  Routes:       4   backlog:  0  unprogrammed:  0
  Adjacencies:  41  backlog:  0  unprogrammed:  0
Mpls:
  Routes:       5  backlog:  0  unprogrammed:  0
  Adjacencies:  0  backlog:  0  unprogrammed:  0

Jericho2 Ip Fecs:
  Non-ecmp fecs:  4114  ecmp fecs:  1  fec entries:  4116
Jericho2 Mpls Fecs:
  Non-ecmp fecs:  0  ecmp fecs:  0  fec entries:  0
Jericho2 Vxlan Tunnel Fecs:
  Non-ecmp fecs:  0  ecmp fecs:  0  fec entries:  0
  Number of vxlan tunnels configured: 0

Jericho2 Lpm Routes:
  Routes:   43  unprogrammed:   0   
  Routes6:  4   unprogrammed6:  0   
  Backlog:  0 

Jericho2 Lpm:
  TCAM entries used:   3  Percent free:  99  ADS2 entries used:   5  Percent free:  99
  Pivot buckets used:  4  Rows used:     1   Entries Per Bucket:  1  Percent free:  99
  Route buckets used:  9  Rows used:     2   Entries Per Bucket:  5  Percent free:  99

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
  FixedSystem: 7
Egress Sflow rewrite entries in use (in each fap):
  FixedSystem: 0

Egress rewrite chains in backlog: resource-full 0, no-interface 0

Glem entries used per fap :
  FixedSystem: 4108

Jericho2 Fec:
  Maximum FEC hierarchy levels:  3
  ReusedEcmp:  0  allocs:  48  frees:  31  shuffles:  0  cmds:  0
  Zombies:     0    purges:    0
  Quarantine:  0/0  shuffles:  0  deletes:  0   
  Fec insertion failures:  0
  Level1  Fecs:
    Non-ecmp fecs:            6   ecmp fecs:            1 
    Non-ecmp (Percent free):  99  ecmp (Percent free):  99
  Level2  Fecs:
    Non-ecmp fecs:            18  ecmp fecs:            0  
    Non-ecmp (Percent free):  99  ecmp (Percent free):  100
  Level3  Fecs:
    Non-ecmp fecs:            12  ecmp fecs:            1 
    Non-ecmp (Percent free):  99  ecmp (Percent free):  99

Lpm Detail:
  Requests:  101  cleanses:  14  batches:  14  avg batch size:  7

Jericho Arp:
  ArpTable writes:      17062  queued      0   
  IngressTable writes:  74635  queued      0   
  Coprocessors:         1      in CmdRing

Tunnel Counter Status
  Number of MPLS tunnels:                  9    
  Number of uncountable MPLS tunnels:      1    
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
|0  |0.0.0.0/8         |DROP | DROP               |0    |  -     |                   |  -  |288374|   -   
|0  |10.0.0.19/32      |ROUTE| Et50/1             |1008 |103421  | 30:c5:07:1f:33:10 |  -  |288368|   -   
|0  |10.0.0.32/32      |ROUTE| Et50/1             |1008 |103421  | 30:c5:07:1f:33:10 |  -  |288368|   -   
|0  |10.0.0.47/32      |ROUTE| Et51/1             |1007 |103422  | 58:70:7f:9f:ca:0d |24576|528486|   -   
|0  |10.0.0.47/32      |ROUTE| Et50/1             |1008 |103421  | 30:c5:07:1f:33:10 |24576|528487|   -   
|0  |10.0.0.47/32      |ROUTE| Et50/1             |1008 |103421  | 30:c5:07:1f:33:10 |24576|528488|   -   
|0  |10.0.0.47/32      |ROUTE| Et51/1             |1007 |103422  | 58:70:7f:9f:ca:0d |24576|528489|   -   
|0  |10.0.0.172/32     |TRAP | CoppSystemIpUcast  |0    |  -     | Receive           |  -  |524291|   -   
|0  |20.19.32.0/24     |ROUTE| Et50/1             |1008 |103421  | 30:c5:07:1f:33:10 |  -  |288368|   -   
|0  |20.19.47.0/24     |ROUTE| Et50/1             |1008 |103421  | 30:c5:07:1f:33:10 |  -  |288368|   -   
|0  |20.32.172.0/32    |TRAP | CoppSystemIpBcast  |0    |  -     | BcastReceive      |  -  |524288|   -   
|0  |20.32.172.32/32   |ROUTE| Et50/1             |1008 |103421  | 30:c5:07:1f:33:10 |  -  |288366|   -   
|0  |20.32.172.172/32  |TRAP | CoppSystemIpUcast  |0    |  -     | Receive           |  -  |524291|   -   
|0  |20.32.172.255/32  |TRAP | CoppSystemIpBcast  |0    |  -     | BcastReceive      |  -  |524288|   -   
|0  |20.32.172.0/24    |TRAP | CoppSystemL3DstMiss|1008 |1008    | ArpTrap           |  -  |525302|   -   
|0  |20.47.172.0/32    |TRAP | CoppSystemIpBcast  |0    |  -     | BcastReceive      |  -  |524288|   -   
|0  |20.47.172.47/32   |ROUTE| Et51/1             |1007 |103422  | 58:70:7f:9f:ca:0d |  -  |288370|   -   
|0  |20.47.172.172/32  |TRAP | CoppSystemIpUcast  |0    |  -     | Receive           |  -  |524291|   -   
|0  |20.47.172.255/32  |TRAP | CoppSystemIpBcast  |0    |  -     | BcastReceive      |  -  |524288|   -   
|0  |20.47.172.0/24    |TRAP | CoppSystemL3DstMiss|1007 |1007    | ArpTrap           |  -  |525301|   -   
|0  |127.0.0.0/8       |TRAP | CoppSystemL3DstMiss|0    |  -     | ArpTrap           |  -  |524294|   -   
|0  |192.168.0.0/19    |ROUTE| Et50/1             |1008 |103421  | 30:c5:07:1f:33:10 |  -  |288368|   -   
|0  |0.0.0.0/0         |TRAP | CoppSystemL3LpmOver|0    |  -     | SlowReceive       |  -  |524292|   -   
|1  |0.0.0.0/8         |DROP | DROP               |0    |  -     |                   |  -  |288380|   -   
|1  |127.0.0.0/8       |TRAP | CoppSystemL3DstMiss|0    |  -     | ArpTrap           |  -  |524294|   -   
|1  |192.168.20.0/32   |TRAP | CoppSystemIpBcast  |0    |  -     | BcastReceive      |  -  |524288|   -   
|1  |192.168.20.172/32 |TRAP | CoppSystemIpUcast  |0    |  -     | Receive           |  -  |524291|   -   
|1  |192.168.21.255/32 |TRAP | CoppSystemIpBcast  |0    |  -     | BcastReceive      |  -  |524288|   -   
|1  |192.168.20.0/23   |TRAP | CoppSystemL3DstMiss|0    |  -     | ArpTrap           |  -  |524294|   -   
|1  |0.0.0.0/0         |TRAP | CoppSystemL3DstMiss|0    |  -     | ArpTrap           |  -  |524294|   -   
|3  |0.0.0.0/8         |DROP | DROP               |0    |  -     |                   |  -  |288378|   -   
|3  |20.111.172.0/32   |TRAP | CoppSystemIpBcast  |0    |  -     | BcastReceive      |  -  |524288|   -   
|3  |20.111.172.172/32 |TRAP | CoppSystemIpUcast  |0    |  -     | Receive           |  -  |524291|   -   
|3  |20.111.172.255/32 |TRAP | CoppSystemIpBcast  |0    |  -     | BcastReceive      |  -  |524288|   -   
|3  |20.111.172.0/24   |TRAP | CoppSystemL3DstMiss|1011 |1011    | ArpTrap           |  -  |525305|   -   
|3  |127.0.0.0/8       |TRAP | CoppSystemL3DstMiss|0    |  -     | ArpTrap           |  -  |524294|   -   
|3  |0.0.0.0/0         |TRAP | CoppSystemL3LpmOver|0    |  -     | SlowReceive       |  -  |524292|   -   
|6  |0.0.0.0/8         |DROP | DROP               |0    |  -     |                   |  -  |288382|   -   
|6  |20.32.111.0/24    |ROUTE| FEC 528490         |0    |2097151 | 00:00:00:00:00:00 |  -  |91752 |M 756651
|6  |20.111.172.0/32   |TRAP | CoppSystemIpBcast  |0    |  -     | BcastReceive      |  -  |524288|   -   
|6  |20.111.172.1/32   |ROUTE| Et5                |1014 |103423  | 00:14:01:00:00:01 |  -  |288372|   -   
|6  |20.111.172.172/32 |TRAP | CoppSystemIpUcast  |0    |  -     | Receive           |  -  |524291|   -   
|6  |20.111.172.255/32 |TRAP | CoppSystemIpBcast  |0    |  -     | BcastReceive      |  -  |524288|   -   
|6  |20.111.172.0/24   |TRAP | CoppSystemL3DstMiss|1014 |1014    | ArpTrap           |  -  |525308|   -   
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
|24576|528486|ROUTE| Et51/1             |1007 |103422  | 58:70:7f:9f:ca:0d |   -   
|24576|528487|ROUTE| Et50/1             |1008 |103421  | 30:c5:07:1f:33:10 |   -   
|24576|528488|ROUTE| Et50/1             |1008 |103421  | 30:c5:07:1f:33:10 |   -   
|24576|528489|ROUTE| Et51/1             |1007 |103422  | 58:70:7f:9f:ca:0d |   -   
|  -  |91752 |ROUTE| FEC 528490         |   - |2097151 |                 - |Mpush 756651
|  -  |91754 |ROUTE| FEC 528482         |   - |  -     |                   |   -   
|  -  |91756 |ROUTE| FEC 528496         |   - |  -     |                   |   -   
|  -  |288366|ROUTE| Et50/1             |1008 |103421  | 30:c5:07:1f:33:10 |   -   
|  -  |288368|ROUTE| Et50/1             |1008 |103421  | 30:c5:07:1f:33:10 |   -   
|  -  |288370|ROUTE| Et51/1             |1007 |103422  | 58:70:7f:9f:ca:0d |   -   
|  -  |288372|ROUTE| Et5                |1014 |103423  | 00:14:01:00:00:01 |   -   
|  -  |288374|DROP | DROP               |0    |  -     |                   |   -   
|  -  |288376|DROP | DROP               |0    |  -     |                   |   -   
|  -  |288378|DROP | DROP               |0    |  -     |                   |   -   
|  -  |288380|DROP | DROP               |0    |  -     |                   |   -   
|  -  |288382|DROP | DROP               |0    |  -     |                   |   -   
|  -  |524288|TRAP | CoppSystemIpBcast  |0    |  -     | BcastReceive      |   -   
|  -  |524291|TRAP | CoppSystemIpUcast  |0    |  -     | Receive           |   -   
|  -  |524292|TRAP | CoppSystemL3LpmOver|0    |  -     | SlowReceive       |   -   
|  -  |524294|TRAP | CoppSystemL3DstMiss|0    |  -     | ArpTrap           |   -   
|  -  |525301|TRAP | CoppSystemL3DstMiss|1007 |1007    | ArpTrap           |   -   
|  -  |525302|TRAP | CoppSystemL3DstMiss|1008 |1008    | ArpTrap           |   -   
|  -  |525305|TRAP | CoppSystemL3DstMiss|1011 |1011    | ArpTrap           |   -   
|  -  |525308|TRAP | CoppSystemL3DstMiss|1014 |1014    | ArpTrap           |   -   
|  -  |528482|ROUTE| Et51/1             |1007 |103427  | 58:70:7f:9f:ca:0d |   -   
|  -  |528483|ROUTE| Et50/1             |1008 |103428  | 30:c5:07:1f:33:10 |Mpush 20047
|  -  |528490|ROUTE| Et50/1             |1008 |103434  | 30:c5:07:1f:33:10 |   -   
|  -  |528491|ROUTE| Et51/1             |1007 |103426  | 58:70:7f:9f:ca:0d |Mpush 20032
|  -  |528494|ROUTE| Et50/1             |1008 |103430  | 30:c5:07:1f:33:10 |   -   
|  -  |528495|ROUTE| Et51/1             |1007 |103431  | 58:70:7f:9f:ca:0d |   -   
|  -  |528496|ROUTE| Et50/1             |1008 |103435  | 30:c5:07:1f:33:10 |   -   
|  -  |528497|ROUTE| Et51/1             |1007 |103436  | 58:70:7f:9f:ca:0d |Mpush 20032

```

