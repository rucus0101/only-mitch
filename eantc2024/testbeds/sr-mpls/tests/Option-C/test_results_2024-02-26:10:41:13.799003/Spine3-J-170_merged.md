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

Uptime: 3 hours and 43 minutes
Total memory: 8051592 kB
Free memory: 5873680 kB

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
Interface       IP Address           Status        Protocol       MTU   Owner  
--------------- -------------------- ------------- ----------- -------- -------
Ethernet1       20.170.171.170/24    admin down    down          1500          
Ethernet3       20.47.170.170/24     up            up            1500          
Ethernet43      20.32.170.170/24     up            up            1500          
Ethernet45      20.57.170.170/24     up            up            1500          
Ethernet48      20.170.254.170/24    admin down    down          1500          
Ethernet49/1    20.170.179.170/24    up            up            1500          
Ethernet49/2    20.170.212.170/24    up            up            1500          
Ethernet50/1    20.50.170.170/24     up            up            1500          
Ethernet51/1    20.155.170.170/24    up            up            1500          
Ethernet52/1    20.170.172.170/24    up            up            1500          
Ethernet53/1    20.19.170.170/24     up            up            1500          
Ethernet54/1    20.59.170.170/24     up            up            1500          
Loopback0       10.0.0.170/32        up            up           65535          
Management1     192.168.20.170/23    up            up            1500          

```

## show interfaces counters rates | nz

```text
Port      Name            Intvl  In Mbps      %  In Kpps Out Mbps      %
Et3       Ericson          0:05     76.5   0.8%        9     55.0   0.6%
Et43      RIBBON_32        0:05     76.5   0.8%        9     54.8   0.6%
Et49/2    Juniper_302      0:05    193.5   2.0%       24     54.8   0.6%
Et51/1    Cisco_355        0:05    219.9   0.2%       27    421.3   0.4%
Et54/1    Nokia_59         0:05     76.5   0.8%        9     55.0   0.6%

Port      Out Kpps
Et3              6
Et43             6
Et49/2           6
Et51/1          52
Et54/1           6
```

## show isis neighbors

```text
 
Instance  VRF      System Id        Type Interface          SNPA              State Hold time   Circuit Id          
IGP       default  Ribbon-32        L2   Ethernet43         P2P               UP    73          00                  
IGP       default  Ericsson_47      L2   Ethernet3          P2P               UP    23          02                  
IGP       default  R6676-50         L2   Ethernet50/1       P2P               UP    22          02                  
IGP       default  juniper_379_MX304 L2   Ethernet49/1       P2P               UP    25          01                  
IGP       default  JNPR-312-ACX7100-48L L2   Ethernet49/2       P2P               UP    20          01                  
IGP       default  h3c_19_CR16010E-F-2 L2   Ethernet53/1       P2P               UP    27          01                  
IGP       default  h55-8201-24H8FH  L2   Ethernet51/1       P2P               UP    29          00                  
IGP       default  NOKIA-SR2-57     L2   Ethernet45         P2P               UP    19          00                  
IGP       default  Nokia-59-IXRe2   L2   Ethernet54/1       P2P               UP    21          00                  
IGP       default  PE32-J2-172      L2   Ethernet52/1       P2P               UP    29          65                  
```

## show isis database detail

```text
Legend:
H - hostname conflict
U - node unreachable

IS-IS Instance: IGP VRF: default
  IS-IS Level 2 Link State Database
    LSPID                   Seq Num  Cksum  Life Length IS  Received LSPID        Flags
    Ribbon-32.00-00              14  17952   597     79 L2  0000.0000.0032.00-00  <>
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
    Ribbon-32.00-01              14  33716   757     38 L2  0000.0000.0032.00-01  <>
      Hostname: Ribbon-32
    Ribbon-32.00-02              18   4966   579    179 L2  0000.0000.0032.00-02  <>
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
    Ericsson_47.00-00            32  22689   675    166 L2  0000.0000.0047.00-00  <>
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
    R6676-50.00-00               32  37629   692    145 L2  0000.0000.0050.00-00  <>
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
    h3c_27_S12500R-2L.00-00        43  44321   860    187 L2  0000.0001.0027.00-00  <>
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
      Remaining lifetime received: 1198 s Modified to: 1200 s
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
      Remaining lifetime received: 1198 s Modified to: 1200 s
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
    Nokia-59-IXRe2.00-00         24  40126   676    271 L2  0100.0000.0059.00-00  <>
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
      LSP generation remaining wait time: 0 ms
      Time remaining until refresh: 325 s
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
      Remaining lifetime received: 1199 s Modified to: 1200 s
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

IS-IS Instance: IGP VRF: default
  IS-IS Level 2 Link State Database
    LSPID                   Seq Num  Cksum  Life Length IS  Received LSPID        Flags
    Ribbon-32.00-00              14  17952   596     79 L2  0000.0000.0032.00-00  <>
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
    Ribbon-32.00-01              14  33716   756     38 L2  0000.0000.0032.00-01  <>
      Hostname: Ribbon-32
    Ribbon-32.00-02              18   4966   579    179 L2  0000.0000.0032.00-02  <>
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
    Ericsson_47.00-00            32  22689   674    166 L2  0000.0000.0047.00-00  <>
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
    R6676-50.00-00               32  37629   691    145 L2  0000.0000.0050.00-00  <>
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
    h3c_27_S12500R-2L.00-00        43  44321   860    187 L2  0000.0001.0027.00-00  <>
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
    juniper_379_MX304.00-00        28  34054   980    211 L2  0000.0001.7900.00-00  <>
      Remaining lifetime received: 1198 s Modified to: 1200 s
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
    JNPR-312-ACX7100-48L.00-00        24  44147   551    178 L2  0000.0003.1200.00-00  <>
      Remaining lifetime received: 1198 s Modified to: 1200 s
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
    h3c_19_CR16010E-F-2.00-00        28  13235  1076    295 L2  0001.0000.0019.00-00  <>
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
    h55-8201-24H8FH.00-00        23  54171  1176    193 L2  0001.0000.0355.00-00  <>
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
    NOKIA-SR2-57.00-00           24   4741   912    271 L2  0100.0000.0057.00-00  <>
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
    Nokia-59-IXRe2.00-00         24  40126   675    271 L2  0100.0000.0059.00-00  <>
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
      LSP generation remaining wait time: 0 ms
      Time remaining until refresh: 324 s
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
    PE32-J2-172.00-00            20  11510   823    162 L2  0100.0000.0172.00-00  <>
      Remaining lifetime received: 1199 s Modified to: 1200 s
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

IS-IS Instance: IGP VRF: default

```

## show isis flex-algo path detail

```text
```

## show isis segment-routing tunnel

```text
 Index     Endpoint          Next Hop/Tunnel Index     Interface      Labels   
-------- ----------------- ------------------------- ---------------- ---------
 1         10.0.1.55/32      20.155.170.155            Ethernet51/1   [ 3 ]    
 2         10.0.0.212/32     20.170.212.212            Ethernet49/2   [ 3 ]    
 3         10.0.0.172/32     20.170.172.172            Ethernet52/1   [ 3 ]    
 4         10.0.0.179/32     20.170.179.179            Ethernet49/1   [ 3 ]    
 5         10.0.0.19/32      20.19.170.19              Ethernet53/1   [ 20019 ]
 6         100.0.1.27/32     20.19.170.19              Ethernet53/1   [ 20270 ]
 7         10.0.0.59/32      20.59.170.59              Ethernet54/1   [ 20059 ]
 8         10.0.0.50/32      20.50.170.50              Ethernet50/1   [ 20050 ]
 9         10.0.0.47/32      20.47.170.47              Ethernet3      [ 20047 ]
 10        10.0.0.57/32      20.57.170.57              Ethernet45     [ 20057 ]
 11        10.0.0.32/32      20.32.170.32              Ethernet43     [ 3 ]    
 12        10.1.0.179/32     20.170.179.179            Ethernet49/1   [ 3 ]    

```

## show isis segment-routing prefix-segments

```text

System ID: Spine3-J-170			Instance: 'IGP'
SR supported Data-plane: MPLS			SR Router ID: 10.0.0.170

Node: 14     Proxy-Node: 0      Prefix: 1       Total Segments: 15

Flag Descriptions: R: Re-advertised, N: Node Segment, P: no-PHP
                   E: Explicit-NULL, V: Value, L: Local
Segment status codes: * - Self originated Prefix, L1 - level 1, L2 - level 2, ! - SR-unreachable,
                      # - Some IS-IS next-hops are SR-unreachable
   Prefix                      SID Type       Flags                        System ID       Level Protection  Algorithm   
   ------------------------- ----- ---------- ---------------------------- --------------- ----- ----------- -------------
   10.0.0.19/32                 19 Prefix     R:1 N:0 P:1 E:0 V:0 L:0      h3c_19_CR16010E-F-2 L2    node        SPF         
   10.0.0.32/32                 32 Node       R:0 N:1 P:0 E:0 V:0 L:0      Ribbon-32       L2    node        SPF         
   10.0.0.47/32                 47 Node       R:0 N:1 P:1 E:0 V:0 L:0      Ericsson_47     L2    node        SPF         
   10.0.0.50/32                 50 Node       R:0 N:1 P:1 E:0 V:0 L:0      R6676-50        L2    node        SPF         
   10.0.0.57/32                 57 Node       R:0 N:1 P:1 E:0 V:0 L:0      NOKIA-SR2-57    L2    node        SPF         
   10.0.0.59/32                 59 Node       R:0 N:1 P:1 E:0 V:0 L:0      Nokia-59-IXRe2  L2    node        SPF         
*  10.0.0.170/32               170 Node       R:0 N:1 P:0 E:0 V:0 L:0      Spine3-J-170    L2    unprotected SPF         
   10.0.0.172/32               172 Node       R:0 N:1 P:0 E:0 V:0 L:0      PE32-J2-172     L2    node        SPF         
   10.0.0.179/32               379 Node       R:0 N:1 P:0 E:0 V:0 L:0      juniper_379_MX304 L2    node        SPF         
   10.0.0.212/32               212 Node       R:0 N:1 P:0 E:0 V:0 L:0      JNPR-312-ACX7100-48L L2    node        SPF         
   10.0.1.55/32                355 Node       R:0 N:1 P:0 E:0 V:0 L:0      h55-8201-24H8FH L2    node        SPF         
   10.1.0.179/32                79 Node       R:0 N:1 P:0 E:0 V:0 L:0      juniper_379_MX304 L2    node        SPF         
   100.0.1.27/32               270 Node       R:0 N:1 P:1 E:0 V:0 L:0      h3c_27_S12500R-2L L2    node        SPF         
   2002::57/128                157 Node       R:0 N:1 P:1 E:0 V:0 L:0      NOKIA-SR2-57    L2    unprotected SPF         
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

 I L2     10.0.0.19/32 [115/10]
           via 20.19.170.19, Ethernet53/1
 I L2     10.0.0.32/32 [115/10]
           via 20.32.170.32, Ethernet43
 I L2     10.0.0.47/32 [115/20]
           via 20.47.170.47, Ethernet3
 I L2     10.0.0.50/32 [115/20]
           via 20.50.170.50, Ethernet50/1
 I L2     10.0.0.57/32 [115/10]
           via 20.57.170.57, Ethernet45
 I L2     10.0.0.59/32 [115/10]
           via 20.59.170.59, Ethernet54/1
 C        10.0.0.170/32
           directly connected, Loopback0
 I L2     10.0.0.172/32 [115/20]
           via 20.170.172.172, Ethernet52/1
 I L2     10.0.0.179/32 [115/10]
           via 20.170.179.179, Ethernet49/1
 I L2     10.0.0.212/32 [115/10]
           via 20.170.212.212, Ethernet49/2
 I L2     10.0.1.55/32 [115/10]
           via 20.155.170.155, Ethernet51/1
 I L2     10.1.0.179/32 [115/10]
           via 20.170.179.179, Ethernet49/1
 C        20.19.170.0/24
           directly connected, Ethernet53/1
 I L2     20.27.180.0/24 [115/20]
           via 20.19.170.19, Ethernet53/1
 C        20.32.170.0/24
           directly connected, Ethernet43
 C        20.47.170.0/24
           directly connected, Ethernet3
 C        20.50.170.0/24
           directly connected, Ethernet50/1
 C        20.57.170.0/24
           directly connected, Ethernet45
 C        20.59.170.0/24
           directly connected, Ethernet54/1
 C        20.155.170.0/24
           directly connected, Ethernet51/1
 C        20.170.172.0/24
           directly connected, Ethernet52/1
 C        20.170.179.0/24
           directly connected, Ethernet49/1
 C        20.170.212.0/24
           directly connected, Ethernet49/2
 I L2     31.9.1.0/24 [115/20]
           via 20.19.170.19, Ethernet53/1
 I L2     100.0.0.27/32 [115/20]
           via 20.19.170.19, Ethernet53/1
 I L2     100.0.1.27/32 [115/20]
           via 20.19.170.19, Ethernet53/1
 I L2     192.168.20.0/23 [115/20]
           via 20.19.170.19, Ethernet53/1

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

 I L2     10.0.0.19/32 [115/10]
           via 20.19.170.19, Ethernet53/1
 I L2     10.0.0.32/32 [115/10]
           via 20.32.170.32, Ethernet43
 I L2     10.0.0.47/32 [115/20]
           via 20.47.170.47, Ethernet3
 I L2     10.0.0.50/32 [115/20]
           via 20.50.170.50, Ethernet50/1
 I L2     10.0.0.57/32 [115/10]
           via 20.57.170.57, Ethernet45
 I L2     10.0.0.59/32 [115/10]
           via 20.59.170.59, Ethernet54/1
 C        10.0.0.170/32
           directly connected, Loopback0
 I L2     10.0.0.172/32 [115/20]
           via 20.170.172.172, Ethernet52/1
 I L2     10.0.0.179/32 [115/10]
           via 20.170.179.179, Ethernet49/1
 I L2     10.0.0.212/32 [115/10]
           via 20.170.212.212, Ethernet49/2
 I L2     10.0.1.55/32 [115/10]
           via 20.155.170.155, Ethernet51/1
 I L2     10.1.0.179/32 [115/10]
           via 20.170.179.179, Ethernet49/1
 C        20.19.170.0/24
           directly connected, Ethernet53/1
 I L2     20.27.180.0/24 [115/20]
           via 20.19.170.19, Ethernet53/1
 C        20.32.170.0/24
           directly connected, Ethernet43
 C        20.47.170.0/24
           directly connected, Ethernet3
 C        20.50.170.0/24
           directly connected, Ethernet50/1
 C        20.57.170.0/24
           directly connected, Ethernet45
 C        20.59.170.0/24
           directly connected, Ethernet54/1
 C        20.155.170.0/24
           directly connected, Ethernet51/1
 C        20.170.172.0/24
           directly connected, Ethernet52/1
 C        20.170.179.0/24
           directly connected, Ethernet49/1
 C        20.170.212.0/24
           directly connected, Ethernet49/2
 I L2     31.9.1.0/24 [115/20]
           via 20.19.170.19, Ethernet53/1
 I L2     100.0.0.27/32 [115/20]
           via 20.19.170.19, Ethernet53/1
 I L2     100.0.1.27/32 [115/20]
           via 20.19.170.19, Ethernet53/1
 I L2     192.168.20.0/23 [115/20]
           via 20.19.170.19, Ethernet53/1


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
MPLS forwarding table (Label [metric] Vias) - 22 routes 
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
                    20.19.170.19 Ethernet53/1
 20032   A[1]
                via M, pop
                    EgressACL: apply
                    20.32.170.32 Ethernet43
 20047   A[1]
                via M, forward
                    EgressACL: apply
                    20.47.170.47 Ethernet3
 20050   A[1]
                via M, forward
                    EgressACL: apply
                    20.50.170.50 Ethernet50/1
 20057   A[1]
                via M, forward
                    EgressACL: apply
                    20.57.170.57 Ethernet45
 20059   A[1]
                via M, forward
                    EgressACL: apply
                    20.59.170.59 Ethernet54/1
 20079   A[1]
                via M, pop
                    EgressACL: apply
                    20.170.179.179 Ethernet49/1
 20172   A[1]
                via M, pop
                    EgressACL: apply
                    20.170.172.172 Ethernet52/1
 20212   A[1]
                via M, pop
                    EgressACL: apply
                    20.170.212.212 Ethernet49/2
 20270   A[1]
                via M, forward
                    EgressACL: apply
                    20.19.170.19 Ethernet53/1
 20355   A[1]
                via M, pop
                    EgressACL: apply
                    20.155.170.155 Ethernet51/1
 20379   A[1]
                via M, pop
                    EgressACL: apply
                    20.170.179.179 Ethernet49/1
 362144  A[1]
                via M, 20.155.170.155, pop
                    EgressACL: apply
                    directly connected, Ethernet51/1
                    34:88:18:bf:4a:3c, vlan 1014
 362145  A[1]
                via M, 20.170.212.212, pop
                    EgressACL: apply
                    directly connected, Ethernet49/2
                    68:22:8e:16:e3:10, vlan 1009
 362146  A[1]
                via M, 20.170.172.172, pop
                    EgressACL: apply
                    directly connected, Ethernet52/1
                    2c:dd:e9:96:3a:bb, vlan 1008
 362147  A[1]
                via M, 20.170.179.179, pop
                    EgressACL: apply
                    directly connected, Ethernet49/1
                    60:c7:8d:2d:3c:c7, vlan 1012
 362148  A[1]
                via M, 20.19.170.19, pop
                    EgressACL: apply
                    directly connected, Ethernet53/1
                    c4:07:78:58:80:af, vlan 1015
 362149  A[1]
                via M, 20.59.170.59, pop
                    EgressACL: apply
                    directly connected, Ethernet54/1
                    8c:7a:00:e7:f5:47, vlan 1011
 362150  A[1]
                via M, 20.50.170.50, pop
                    EgressACL: apply
                    directly connected, Ethernet50/1
                    58:70:7f:6c:0e:89, vlan 1006
 362151  A[1]
                via M, 20.47.170.47, pop
                    EgressACL: apply
                    directly connected, Ethernet3
                    58:70:7f:9f:ca:04, vlan 1010
 362152  A[1]
                via M, 20.57.170.57, pop
                    EgressACL: apply
                    directly connected, Ethernet45
                    c0:14:b8:21:ca:74, vlan 1007
 362153  A[1]
                via M, 20.32.170.32, pop
                    EgressACL: apply
                    directly connected, Ethernet43
                    30:c5:07:1f:33:0c, vlan 1013
```

## show mpls lfib route

```text
MPLS forwarding table (Label [metric] Vias) - 22 routes 
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
                via M, 20.19.170.19, forward
                 payload autoDecide, ttlMode uniform, dscpMode uniform, apply egress-acl
                 interface Ethernet53/1
 IP    20032    [1], 10.0.0.32/32
                via M, 20.32.170.32, pop
                 payload autoDecide, ttlMode uniform, dscpMode uniform, apply egress-acl
                 interface Ethernet43
 IP    20047    [1], 10.0.0.47/32
                via M, 20.47.170.47, forward
                 payload autoDecide, ttlMode uniform, dscpMode uniform, apply egress-acl
                 interface Ethernet3
 IP    20050    [1], 10.0.0.50/32
                via M, 20.50.170.50, forward
                 payload autoDecide, ttlMode uniform, dscpMode uniform, apply egress-acl
                 interface Ethernet50/1
 IP    20057    [1], 10.0.0.57/32
                via M, 20.57.170.57, forward
                 payload autoDecide, ttlMode uniform, dscpMode uniform, apply egress-acl
                 interface Ethernet45
 IP    20059    [1], 10.0.0.59/32
                via M, 20.59.170.59, forward
                 payload autoDecide, ttlMode uniform, dscpMode uniform, apply egress-acl
                 interface Ethernet54/1
 IP    20079    [1], 10.1.0.179/32
                via M, 20.170.179.179, pop
                 payload autoDecide, ttlMode uniform, dscpMode uniform, apply egress-acl
                 interface Ethernet49/1
 IP    20172    [1], 10.0.0.172/32
                via M, 20.170.172.172, pop
                 payload autoDecide, ttlMode uniform, dscpMode uniform, apply egress-acl
                 interface Ethernet52/1
 IP    20212    [1], 10.0.0.212/32
                via M, 20.170.212.212, pop
                 payload autoDecide, ttlMode uniform, dscpMode uniform, apply egress-acl
                 interface Ethernet49/2
 IP    20270    [1], 100.0.1.27/32
                via M, 20.19.170.19, forward
                 payload autoDecide, ttlMode uniform, dscpMode uniform, apply egress-acl
                 interface Ethernet53/1
 IP    20355    [1], 10.0.1.55/32
                via M, 20.155.170.155, pop
                 payload autoDecide, ttlMode uniform, dscpMode uniform, apply egress-acl
                 interface Ethernet51/1
 IP    20379    [1], 10.0.0.179/32
                via M, 20.170.179.179, pop
                 payload autoDecide, ttlMode uniform, dscpMode uniform, apply egress-acl
                 interface Ethernet49/1
 IA    362144   [1]
                via M, 20.155.170.155, pop
                 payload autoDecide, ttlMode uniform, apply egress-acl
                 interface Ethernet51/1
 IA    362145   [1]
                via M, 20.170.212.212, pop
                 payload autoDecide, ttlMode uniform, apply egress-acl
                 interface Ethernet49/2
 IA    362146   [1]
                via M, 20.170.172.172, pop
                 payload autoDecide, ttlMode uniform, apply egress-acl
                 interface Ethernet52/1
 IA    362147   [1]
                via M, 20.170.179.179, pop
                 payload autoDecide, ttlMode uniform, apply egress-acl
                 interface Ethernet49/1
 IA    362148   [1]
                via M, 20.19.170.19, pop
                 payload autoDecide, ttlMode uniform, apply egress-acl
                 interface Ethernet53/1
 IA    362149   [1]
                via M, 20.59.170.59, pop
                 payload autoDecide, ttlMode uniform, apply egress-acl
                 interface Ethernet54/1
 IA    362150   [1]
                via M, 20.50.170.50, pop
                 payload autoDecide, ttlMode uniform, apply egress-acl
                 interface Ethernet50/1
 IA    362151   [1]
                via M, 20.47.170.47, pop
                 payload autoDecide, ttlMode uniform, apply egress-acl
                 interface Ethernet3
 IA    362152   [1]
                via M, 20.57.170.57, pop
                 payload autoDecide, ttlMode uniform, apply egress-acl
                 interface Ethernet45
 IA    362153   [1]
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
10.0.0.19/32    IS-IS SR IPv4   5           65                  115            
10.0.0.32/32    IS-IS SR IPv4   11          65                  115            
10.0.0.47/32    IS-IS SR IPv4   9           65                  115            
10.0.0.50/32    IS-IS SR IPv4   8           65                  115            
10.0.0.57/32    IS-IS SR IPv4   10          65                  115            
10.0.0.59/32    IS-IS SR IPv4   7           65                  115            
10.0.0.172/32   IS-IS SR IPv4   3           65                  115            
10.0.0.179/32   IS-IS SR IPv4   4           65                  115            
10.0.0.212/32   IS-IS SR IPv4   2           65                  115            
10.0.1.55/32    IS-IS SR IPv4   1           65                  115            
10.1.0.179/32   IS-IS SR IPv4   12          65                  115            
100.0.1.27/32   IS-IS SR IPv4   6           65                  115            

   IGP Metric    Metric Type
---------------- -----------
   10            metric     
   10            metric     
   20            metric     
   20            metric     
   10            metric     
   10            metric     
   20            metric     
   10            metric     
   10            metric     
   10            metric     
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
>C    10.0.0.170/32 [0 pref/0 metric] updated 03:41:40 ago
         via Loopback0, directly connected
>C    20.19.170.0/24 [0 pref/0 metric] updated 03:32:47 ago
         via Ethernet53/1, directly connected
>C    20.32.170.0/24 [0 pref/0 metric] updated 01:27:13 ago
         via Ethernet43, directly connected
>C    20.47.170.0/24 [0 pref/0 metric] updated 03:17:48 ago
         via Ethernet3, directly connected
>C    20.50.170.0/24 [0 pref/0 metric] updated 03:19:01 ago
         via Ethernet50/1, directly connected
>C    20.57.170.0/24 [0 pref/0 metric] updated 03:17:25 ago
         via Ethernet45, directly connected
>C    20.59.170.0/24 [0 pref/0 metric] updated 03:20:41 ago
         via Ethernet54/1, directly connected
>C    20.155.170.0/24 [0 pref/0 metric] updated 03:39:41 ago
         via Ethernet51/1, directly connected
>C    20.170.172.0/24 [0 pref/0 metric] updated 03:39:37 ago
         via Ethernet52/1, directly connected
>C    20.170.179.0/24 [0 pref/0 metric] updated 03:33:30 ago
         via Ethernet49/1, directly connected
>C    20.170.212.0/24 [0 pref/0 metric] updated 03:39:39 ago
         via Ethernet49/2, directly connected
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
>P    0.0.0.0/8 [1 pref/0 metric] updated 03:41:38 ago
         via Null0, directly connected [NF]
>P    127.0.0.0/8 [1 pref/0 metric] updated 03:41:38 ago
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
>I    10.0.0.19/32 [115 pref/10 metric] updated 02:42:30 ago
         via 20.19.170.19, Ethernet53/1
>I    10.0.0.32/32 [115 pref/10 metric] updated 01:26:14 ago
         via 20.32.170.32, Ethernet43
>I    10.0.0.47/32 [115 pref/20 metric] updated 03:17:38 ago
         via 20.47.170.47, Ethernet3
>I    10.0.0.50/32 [115 pref/20 metric] updated 03:18:52 ago
         via 20.50.170.50, Ethernet50/1
>I    10.0.0.57/32 [115 pref/10 metric] updated 03:17:25 ago
         via 20.57.170.57, Ethernet45
>I    10.0.0.59/32 [115 pref/10 metric] updated 03:20:40 ago
         via 20.59.170.59, Ethernet54/1
>I    10.0.0.172/32 [115 pref/20 metric] updated 03:39:28 ago
         via 20.170.172.172, Ethernet52/1
>I    10.0.0.179/32 [115 pref/10 metric] updated 03:33:20 ago
         via 20.170.179.179, Ethernet49/1
>I    10.0.0.212/32 [115 pref/10 metric] updated 03:39:30 ago
         via 20.170.212.212, Ethernet49/2
>I    10.0.1.55/32 [115 pref/10 metric] updated 03:39:36 ago
         via 20.155.170.155, Ethernet51/1
>I    10.1.0.179/32 [115 pref/10 metric] updated 01:53:15 ago
         via 20.170.179.179, Ethernet49/1
>I    20.27.180.0/24 [115 pref/20 metric] updated 02:42:30 ago
         via 20.19.170.19, Ethernet53/1
>I    31.9.1.0/24 [115 pref/20 metric] updated 02:42:30 ago
         via 20.19.170.19, Ethernet53/1
>I    100.0.0.27/32 [115 pref/20 metric] updated 02:42:30 ago
         via 20.19.170.19, Ethernet53/1
>I    100.0.1.27/32 [115 pref/20 metric] updated 02:42:30 ago
         via 20.19.170.19, Ethernet53/1
>I    192.168.20.0/23 [115 pref/20 metric] updated 02:42:30 ago
         via 20.19.170.19, Ethernet53/1
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
>P    ::/96 [1 pref/0 metric] updated 03:41:39 ago
         via Null0, directly connected [NF]
>P    ::ffff:127.0.0.0/104 [1 pref/0 metric] updated 03:41:39 ago
         via :: [1 pref/1 metric] type ipv6
            via , directly connected
>P    fe80::/10 [1 pref/0 metric] updated 03:41:39 ago
```

## show platform sand l3 summary

```text
Number of vrfs: 2

Ipv4:
  Routes:       77  backlog:  0  unprogrammed:  0
  Adjacencies:  73  backlog:  0  unprogrammed:  0
Ipv6:
  Routes:       4   backlog:  0  unprogrammed:  0
  Adjacencies:  73  backlog:  0  unprogrammed:  0
Mpls:
  Routes:       22  backlog:  0  unprogrammed:  0
  Adjacencies:  10  backlog:  0  unprogrammed:  0

Jericho Ip Fecs:
  Non-ecmp fecs:  4121  ecmp fecs:  0  fec entries:  4121
Jericho Mpls Fecs:
  Non-ecmp fecs:  10  ecmp fecs:  0  fec entries:  10
Jericho Vxlan Overlay Fecs:
  Non-ecmp fecs:  0  ecmp fecs:  0  fec entries:  0
Jericho Vxlan Tunnel Fecs:
  Non-ecmp fecs:  0  ecmp fecs:  0  fec entries:  0
  Number of vxlan tunnels configured: 0

Jericho Lpm Routes:
  Routes:   67  unprogrammed:   0   
  Routes6:  4   unprogrammed6:  0   
  Backlog:  0 

Jericho Lpm:
  TCAM pivots used:  3   Percent free:  99
  Buckets used:      12  Rows used:     2   Entries Per Bucket:  5     Percent free:  99  

Lem:
  IPv4  Host in Lem:            enabled
  IPv4  Hosts:                  10     
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
  FixedSystem: 18
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
  Used:                     33  ecmp:                 1   reusedEcmp:  0     allocs:  40    frees:  7     shuffles:  0     cmds:  0   
  Non-ecmp (Percent free):  99  ecmp (Percent free):  99
  Zombies:     0    purges:    0
  Quarantine:  0/0  shuffles:  0  deletes:  0   
  Fec insertion failures:  0
  Banks in use (level, used, Percent free):
     2 (2, 33, 99%)

Lpm Detail:
  Requests:  103  cleanses:  33  batches:  33  avg batch size:  3

Lem Cmds:
  Adds:  38  dels:  6  mods:  0  fails:  0  cmds:  44

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
  ArpTable writes:      189   queued      0   
  IngressTable writes:  7960  queued      0   
  Coprocessors:         1     in CmdRing

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

