# Test results for PE32-J2-172

## show version

```text
Arista DCS-7280SR3-48YC8-F
Hardware version: 12.01
Serial number: JPE21210788
Hardware MAC address: 2cdd.e996.3abb
System MAC address: 2cdd.e996.3abb

Software image version: 4.32.0F-35668851.binoshmonsrv6EFTFeb20240 (engineering build)
Architecture: x86_64
Internal build version: 4.32.0F-35668851.binoshmonsrv6EFTFeb20240
Internal build ID: 93cbcec4-274c-4247-b5c2-478b9fcaa07c
Image format version: 3.0
Image optimization: Default

Uptime: 15 hours and 38 minutes
Total memory: 8099732 kB
Free memory: 5066876 kB

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
Ethernet25     20.149.172.172/24  admin down   down               1500         
Ethernet45     20.172.211.172/24  admin down   notpresent         1500         
Ethernet47     20.171.172.172/24  admin down   down               1500         
Ethernet49/1   20.57.172.172/24   admin down   down               1500         
Ethernet50/1   20.32.172.172/24   admin down   down               1500         
Ethernet51/1   20.47.172.172/24   admin down   down               1500         
Ethernet52/1   20.170.172.172/24  admin down   down               1500         
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
IPV6      default  juniper_303_mx204 L2   Ethernet55/1       P2P               UP    23          01                  
IPV6      default  NOKIA-SR2-57     L2   Ethernet53/1       P2P               UP    22          00                  
```

## show isis database detail

```text
Legend:
H - hostname conflict
U - node unreachable

IS-IS Instance: IPV6 VRF: default
  IS-IS Level 2 Link State Database
    LSPID                   Seq Num  Cksum  Life Length IS  Received LSPID        Flags
    juniper_303_mx204.00-00      1353  28991  1043    564 L2  0000.0003.0300.00-00  <>
      Remaining lifetime received: 1198 s Modified to: 1200 s
      NLPID: 0xCC(IPv4) 0x8E(IPv6)
      Hostname: juniper_303_mx204
      Area addresses: 49.0001.00
      Interface address: 192.168.21.3
      IS Neighbor          : NOKIA-SR2-57.00     Metric: 10
        IPv6 Neighbor Address: 2001:0:57:303::57
        Global IPv6 Interface Address: 2001:0:57:303::303
        Adj-sid: 20 flags: [L V F] weight: 0x0
      IS Neighbor          : PE32-J2-172.00      Metric: 10
        Global IPv6 Interface Address: 2001:0:172:303::303
        Adj-sid: 25 flags: [L V F] weight: 0x0
      IS Neighbor          : juniper_304_mx204.00 Metric: 10
        IPv6 Neighbor Address: 2001:0:303:304::304
        Global IPv6 Interface Address: 2001:0:303:304::303
        Adj-sid: 17 flags: [L V F] weight: 0x0
      Reachability          : 2002::303/128 Metric: 0 Type: 1 Up
        SR Prefix-SID: 303 Flags: [N] Algorithm: 0
        SR Prefix-SID: 1103 Flags: [N] Algorithm: 128
      Reachability          : 2001:0:303:304::/64 Metric: 10 Type: 1 Up
      Reachability          : 2001:0:57:303::/64 Metric: 10 Type: 1 Up
      Reachability          : 2001:0:172:303::/64 Metric: 10 Type: 1 Up
      Router Capabilities: Router Id: 192.168.21.3 Flags: []
        Maximum SID depth:
          Base MPLS imposition (MSD type 1):  15
        SR Capability: Flags: [I V]
          SRGB Base: 20000 Range: 2000
        Algorithms:  0, 1, 128
        Flex Algo: Algorithm: 128 Metric: Min Unidirectional Delay Metric (1) Calc: SPF (0) Prio: 0
      Unsupported TLV: Type: 14 Length: 2
    juniper_304_mx204.00-00      2665  22551  1187    545 L2  0000.0003.0400.00-00  <>
      Remaining lifetime received: 1198 s Modified to: 1200 s
      NLPID: 0xCC(IPv4) 0x8E(IPv6)
      Hostname: juniper_304_mx204
      Area addresses: 49.0001.00
      Interface address: 192.168.21.4
      IS Neighbor          : NOKIA-SR2-57.00     Metric: 10
        IPv6 Neighbor Address: 2001:0:57:304::57
        Global IPv6 Interface Address: 2001:0:57:304::304
        Adj-sid: 19 flags: [L V F] weight: 0x0
      IS Neighbor          : juniper_303_mx204.00 Metric: 10
        IPv6 Neighbor Address: 2001:0:303:304::303
        Global IPv6 Interface Address: 2001:0:303:304::304
        Adj-sid: 16 flags: [L V F] weight: 0x0
      IS Neighbor          : Nokia-59-IXRe2.00   Metric: 10
        IPv6 Neighbor Address: 2001:0:59:304::59
        Global IPv6 Interface Address: 2001:0:59:304::304
        Adj-sid: 17 flags: [L V F] weight: 0x0
      Reachability          : 2002::304/128 Metric: 0 Type: 1 Up
        SR Prefix-SID: 304 Flags: [N] Algorithm: 0
        SR Prefix-SID: 1104 Flags: [N] Algorithm: 128
      Reachability          : 2001:0:303:304::/64 Metric: 10 Type: 1 Up
      Reachability          : 2001:0:59:304::/64 Metric: 10 Type: 1 Up
      Reachability          : 2001:0:57:304::/64 Metric: 10 Type: 1 Up
      Router Capabilities: Router Id: 192.168.21.4 Flags: []
        Maximum SID depth:
          Base MPLS imposition (MSD type 1):  15
        SR Capability: Flags: [I V]
          SRGB Base: 20000 Range: 2000
        Algorithms:  0, 1, 128
        Flex Algo: Algorithm: 128 Metric: Min Unidirectional Delay Metric (1) Calc: SPF (0) Prio: 0
      Unsupported TLV: Type: 14 Length: 2
    Nokia-59-IXRe2.00-00       1426  45713  1196    435 L2  0002.3124.4180.00-00  <>
      NLPID: 0xCC(IPv4) 0x8E(IPv6)
      Hostname: Nokia-59-IXRe2
      Area addresses: 49.0000.0000.0059.00
      Interface address: 2001:0:57:59::59
      Interface address: 2001:0:59:304::59
      Interface address: 2002::59
      IS Neighbor          : juniper_304_mx204.00 Metric: 10
        IPv6 Neighbor Address: 2001:0:59:304::304
        Global IPv6 Interface Address: 2001:0:59:304::59
        Adj-sid: 1048572 flags: [L V B F] weight: 0x0
      IS Neighbor          : NOKIA-SR2-57.00     Metric: 10
        IPv6 Neighbor Address: 2001:0:57:59::57
        Global IPv6 Interface Address: 2001:0:57:59::59
        Adj-sid: 1048571 flags: [L V B F] weight: 0x0
      Reachability          : 2001:0:57:59::/64 Metric: 10 Type: 1 Up
      Reachability          : 2001:0:59:304::/64 Metric: 10 Type: 1 Up
      Reachability          : 2002::59/128 Metric: 0 Type: 1 Up
        SR Prefix-SID: 159 Flags: [N P] Algorithm: 0
        SR Prefix-SID: 928 Flags: [N P] Algorithm: 128
      Router Capabilities: Router Id: 0.231.244.180 Flags: []
        Maximum SID depth:
          Base MPLS imposition (MSD type 1):  9
        SR Capability: Flags: [I V]
          SRGB Base: 20000 Range: 2000
        Algorithms:  0, 128
        Flex Algo: Algorithm: 128 Metric: Min Unidirectional Delay Metric (1) Calc: SPF (0) Prio: 100
          Flags: [M] 0x80
    NOKIA-SR2-57.00-00        21783   4125  1186    605 L2  0100.0000.0057.00-00  <>
      NLPID: 0xCC(IPv4) 0x8E(IPv6)
      Hostname: NOKIA-SR2-57
      Area addresses: 49.0000.0000.0057.00
      Interface address: 10.0.0.57
      Interface address: 2001:0:57:59::57
      Interface address: 2001:0:57:172::57
      Interface address: 2001:0:57:303::57
      Interface address: 2001:0:57:304::57
      Interface address: 2002::57
      IS Neighbor          : juniper_303_mx204.00 Metric: 10
        IPv6 Neighbor Address: 2001:0:57:303::303
        Global IPv6 Interface Address: 2001:0:57:303::57
        Adj-sid: 524279 flags: [L V B F] weight: 0x0
      IS Neighbor          : juniper_304_mx204.00 Metric: 10
        IPv6 Neighbor Address: 2001:0:57:304::304
        Global IPv6 Interface Address: 2001:0:57:304::57
        Adj-sid: 524278 flags: [L V B F] weight: 0x0
      IS Neighbor          : Nokia-59-IXRe2.00   Metric: 10
        IPv6 Neighbor Address: 2001:0:57:59::59
        Global IPv6 Interface Address: 2001:0:57:59::57
        Adj-sid: 524248 flags: [L V B F] weight: 0x0
      IS Neighbor          : PE32-J2-172.00      Metric: 10
        Global IPv6 Interface Address: 2001:0:57:172::57
        Adj-sid: 524259 flags: [L V B F] weight: 0x0
      Reachability         : 10.0.0.57/32 Metric: 0 Type: 1 Up
        SR Prefix-SID: 57 Flags: [N P] Algorithm: 0
      Reachability          : 2001:0:57:59::/64 Metric: 10 Type: 1 Up
      Reachability          : 2001:0:57:172::/64 Metric: 10 Type: 1 Up
      Reachability          : 2001:0:57:303::/64 Metric: 10 Type: 1 Up
      Reachability          : 2001:0:57:304::/64 Metric: 10 Type: 1 Up
      Reachability          : 2002::57/128 Metric: 0 Type: 1 Up
        SR Prefix-SID: 157 Flags: [N P] Algorithm: 0
        SR Prefix-SID: 728 Flags: [N P] Algorithm: 128
      Router Capabilities: Router Id: 10.0.0.57 Flags: []
        Maximum SID depth:
          Base MPLS imposition (MSD type 1):  12
        SR Capability: Flags: [I V]
          SRGB Base: 20000 Range: 2000
        Algorithms:  0, 128
        Flex Algo: Algorithm: 128 Metric: Min Unidirectional Delay Metric (1) Calc: SPF (0) Prio: 255
          Flags: [M] 0x80
    PE32-J2-172.00-00            98   5261   478    235 L2  0100.0000.0172.00-00  <>
      LSP generation remaining wait time: 0 ms
      Time remaining until refresh: 178 s
      NLPID: 0x8E(IPv6)
      Hostname: PE32-J2-172
      Area addresses: 49.0000
      Interface address: 2001:0:172:303::172
      Interface address: 2001:0:57:172::172
      Interface address: 2002::172
      IS Neighbor          : juniper_303_mx204.00 Metric: 10
        Adj-sid: 362145 flags: [L V F] weight: 0x0
      IS Neighbor          : NOKIA-SR2-57.00     Metric: 100
        Adj-sid: 362144 flags: [L V F] weight: 0x0
      Reachability          : 2001:0:172:303::/64 Metric: 10 Type: 1 Up
      Reachability          : 2001:0:57:172::/64 Metric: 100 Type: 1 Up
      Reachability          : 2002::172/128 Metric: 0 Type: 1 Up
        SR Prefix-SID: 1172 Flags: [N] Algorithm: 0
      Router Capabilities: Router Id: 10.0.0.172 Flags: []
        SR Local Block:
          SRLB Base: 965536 Range: 65536
        Area leader priority: 250 algorithm: 0
        Maximum SID depth:
          Base MPLS imposition (MSD type 1):  12
        SR Capability: Flags: [V]
          SRGB Base: 20000 Range: 2000
```

## show isis database traffic-engineering

```text
Legend:
H - hostname conflict
U - node unreachable

IS-IS Instance: IPV6 VRF: default
  IS-IS Level 2 Link State Database
    LSPID                   Seq Num  Cksum  Life Length IS  Received LSPID        Flags
    juniper_303_mx204.00-00      1353  28991  1042    564 L2  0000.0003.0300.00-00  <>
      Remaining lifetime received: 1198 s Modified to: 1200 s
      NLPID: 0xCC(IPv4) 0x8E(IPv6)
      Hostname: juniper_303_mx204
      TE IPv4 router ID: 192.168.21.3
      TE IPv6 router ID: 2002::303
      Area addresses: 49.0001.00
      Interface address: 192.168.21.3
      IS Neighbor          : NOKIA-SR2-57.00     Metric: 10
        IPv6 Neighbor Address: 2001:0:57:303::57
        Global IPv6 Interface Address: 2001:0:57:303::303
        Adj-sid: 20 flags: [L V F] weight: 0x0
        Maximum link BW: 10.00 Gbps
        Min/Max unidirectional link delay: 100000/100000 us
        Average unidirectional link delay: 100000 us
        Application Specific Link Attributes:
          Standard applications: Flex-Algo
            Min/Max unidirectional link delay: 100000/100000 us
      IS Neighbor          : PE32-J2-172.00      Metric: 10
        Global IPv6 Interface Address: 2001:0:172:303::303
        Adj-sid: 25 flags: [L V F] weight: 0x0
        Maximum link BW: 10.00 Gbps
        Min/Max unidirectional link delay: 100000/100000 us
        Average unidirectional link delay: 100000 us
        Application Specific Link Attributes:
          Standard applications: Flex-Algo
            Min/Max unidirectional link delay: 100000/100000 us
      IS Neighbor          : juniper_304_mx204.00 Metric: 10
        IPv6 Neighbor Address: 2001:0:303:304::304
        Global IPv6 Interface Address: 2001:0:303:304::303
        Adj-sid: 17 flags: [L V F] weight: 0x0
        Administrative group (Color): 3
        Maximum link BW: 10.00 Gbps
        Min/Max unidirectional link delay: 130/149 us
        Average unidirectional link delay: 141 us
        Unidirectional link delay variation: 11 us
        Application Specific Link Attributes:
          Standard applications: Flex-Algo
            Min/Max unidirectional link delay: 130/149 us
      Reachability          : 2002::303/128 Metric: 0 Type: 1 Up
        SR Prefix-SID: 303 Flags: [N] Algorithm: 0
        SR Prefix-SID: 1103 Flags: [N] Algorithm: 128
      Reachability          : 2001:0:303:304::/64 Metric: 10 Type: 1 Up
      Reachability          : 2001:0:57:303::/64 Metric: 10 Type: 1 Up
      Reachability          : 2001:0:172:303::/64 Metric: 10 Type: 1 Up
      Router Capabilities: Router Id: 192.168.21.3 Flags: []
        Maximum SID depth:
          Base MPLS imposition (MSD type 1):  15
        SR Capability: Flags: [I V]
          SRGB Base: 20000 Range: 2000
        Algorithms:  0, 1, 128
        Flex Algo: Algorithm: 128 Metric: Min Unidirectional Delay Metric (1) Calc: SPF (0) Prio: 0
      Unsupported TLV: Type: 14 Length: 2
    juniper_304_mx204.00-00      2665  22551  1186    545 L2  0000.0003.0400.00-00  <>
      Remaining lifetime received: 1198 s Modified to: 1200 s
      NLPID: 0xCC(IPv4) 0x8E(IPv6)
      Hostname: juniper_304_mx204
      TE IPv4 router ID: 192.168.21.4
      TE IPv6 router ID: 2002::304
      Area addresses: 49.0001.00
      Interface address: 192.168.21.4
      IS Neighbor          : NOKIA-SR2-57.00     Metric: 10
        IPv6 Neighbor Address: 2001:0:57:304::57
        Global IPv6 Interface Address: 2001:0:57:304::304
        Adj-sid: 19 flags: [L V F] weight: 0x0
        Administrative group (Color): 3
        Maximum link BW: 10.00 Gbps
      IS Neighbor          : juniper_303_mx204.00 Metric: 10
        IPv6 Neighbor Address: 2001:0:303:304::303
        Global IPv6 Interface Address: 2001:0:303:304::304
        Adj-sid: 16 flags: [L V F] weight: 0x0
        Administrative group (Color): 3
        Maximum link BW: 10.00 Gbps
        Min/Max unidirectional link delay: 133/158 us
        Average unidirectional link delay: 146 us
        Unidirectional link delay variation: 15 us
        Application Specific Link Attributes:
          Standard applications: Flex-Algo
            Min/Max unidirectional link delay: 133/158 us
      IS Neighbor          : Nokia-59-IXRe2.00   Metric: 10
        IPv6 Neighbor Address: 2001:0:59:304::59
        Global IPv6 Interface Address: 2001:0:59:304::304
        Adj-sid: 17 flags: [L V F] weight: 0x0
        Maximum link BW: 10.00 Gbps
        Min/Max unidirectional link delay: 82/134 us
        Average unidirectional link delay: 115 us
        Unidirectional link delay variation: 51 us
        Application Specific Link Attributes:
          Standard applications: Flex-Algo
            Min/Max unidirectional link delay: 82/134 us
      Reachability          : 2002::304/128 Metric: 0 Type: 1 Up
        SR Prefix-SID: 304 Flags: [N] Algorithm: 0
        SR Prefix-SID: 1104 Flags: [N] Algorithm: 128
      Reachability          : 2001:0:303:304::/64 Metric: 10 Type: 1 Up
      Reachability          : 2001:0:59:304::/64 Metric: 10 Type: 1 Up
      Reachability          : 2001:0:57:304::/64 Metric: 10 Type: 1 Up
      Router Capabilities: Router Id: 192.168.21.4 Flags: []
        Maximum SID depth:
          Base MPLS imposition (MSD type 1):  15
        SR Capability: Flags: [I V]
          SRGB Base: 20000 Range: 2000
        Algorithms:  0, 1, 128
        Flex Algo: Algorithm: 128 Metric: Min Unidirectional Delay Metric (1) Calc: SPF (0) Prio: 0
      Unsupported TLV: Type: 14 Length: 2
    Nokia-59-IXRe2.00-00       1426  45713  1195    435 L2  0002.3124.4180.00-00  <>
      NLPID: 0xCC(IPv4) 0x8E(IPv6)
      Hostname: Nokia-59-IXRe2
      TE IPv4 router ID: 0.231.244.180
      TE IPv6 router ID: 2002::59
      Area addresses: 49.0000.0000.0059.00
      Interface address: 2001:0:57:59::59
      Interface address: 2001:0:59:304::59
      Interface address: 2002::59
      IS Neighbor          : juniper_304_mx204.00 Metric: 10
        IPv6 Neighbor Address: 2001:0:59:304::304
        Global IPv6 Interface Address: 2001:0:59:304::59
        Adj-sid: 1048572 flags: [L V B F] weight: 0x0
        Application Specific Link Attributes:
          Standard applications: SR-TE
            TE default metric: 12
            Maximum link BW: 10.00 Gbps
        Application Specific Link Attributes:
          Standard applications: Flex-Algo
            TE default metric: 12
            Min/Max unidirectional link delay: 113/113 us
      IS Neighbor          : NOKIA-SR2-57.00     Metric: 10
        IPv6 Neighbor Address: 2001:0:57:59::57
        Global IPv6 Interface Address: 2001:0:57:59::59
        Adj-sid: 1048571 flags: [L V B F] weight: 0x0
        Application Specific Link Attributes:
          Standard applications: SR-TE
            Administrative group (Color): 3
            TE default metric: 12
            Maximum link BW: 10.00 Gbps
        Application Specific Link Attributes:
          Standard applications: Flex-Algo
            TE default metric: 12
            Min/Max unidirectional link delay: 46/46 us
      Reachability          : 2001:0:57:59::/64 Metric: 10 Type: 1 Up
      Reachability          : 2001:0:59:304::/64 Metric: 10 Type: 1 Up
      Reachability          : 2002::59/128 Metric: 0 Type: 1 Up
        SR Prefix-SID: 159 Flags: [N P] Algorithm: 0
        SR Prefix-SID: 928 Flags: [N P] Algorithm: 128
      Router Capabilities: Router Id: 0.231.244.180 Flags: []
        Maximum SID depth:
          Base MPLS imposition (MSD type 1):  9
        SR Capability: Flags: [I V]
          SRGB Base: 20000 Range: 2000
        Algorithms:  0, 128
        Flex Algo: Algorithm: 128 Metric: Min Unidirectional Delay Metric (1) Calc: SPF (0) Prio: 100
          Flags: [M] 0x80
    NOKIA-SR2-57.00-00        21783   4125  1185    605 L2  0100.0000.0057.00-00  <>
      NLPID: 0xCC(IPv4) 0x8E(IPv6)
      Hostname: NOKIA-SR2-57
      TE IPv4 router ID: 10.0.0.57
      TE IPv6 router ID: 2002::57
      Area addresses: 49.0000.0000.0057.00
      Interface address: 10.0.0.57
      Interface address: 2001:0:57:59::57
      Interface address: 2001:0:57:172::57
      Interface address: 2001:0:57:303::57
      Interface address: 2001:0:57:304::57
      Interface address: 2002::57
      IS Neighbor          : juniper_303_mx204.00 Metric: 10
        IPv6 Neighbor Address: 2001:0:57:303::303
        Global IPv6 Interface Address: 2001:0:57:303::57
        Adj-sid: 524279 flags: [L V B F] weight: 0x0
        Application Specific Link Attributes:
          Standard applications: Flex-Algo
            Min/Max unidirectional link delay: 100000/100000 us
      IS Neighbor          : juniper_304_mx204.00 Metric: 10
        IPv6 Neighbor Address: 2001:0:57:304::304
        Global IPv6 Interface Address: 2001:0:57:304::57
        Adj-sid: 524278 flags: [L V B F] weight: 0x0
        Application Specific Link Attributes:
          Standard applications: Flex-Algo
            Administrative group (Color): 3
      IS Neighbor          : Nokia-59-IXRe2.00   Metric: 10
        IPv6 Neighbor Address: 2001:0:57:59::59
        Global IPv6 Interface Address: 2001:0:57:59::57
        Adj-sid: 524248 flags: [L V B F] weight: 0x0
        Application Specific Link Attributes:
          Standard applications: SR-TE
            Administrative group (Color): 3
            TE default metric: 12
            Maximum link BW: 10.00 Gbps
        Application Specific Link Attributes:
          Standard applications: Flex-Algo
            TE default metric: 12
            Min/Max unidirectional link delay: 54/54 us
      IS Neighbor          : PE32-J2-172.00      Metric: 10
        Global IPv6 Interface Address: 2001:0:57:172::57
        Adj-sid: 524259 flags: [L V B F] weight: 0x0
      Reachability         : 10.0.0.57/32 Metric: 0 Type: 1 Up
        SR Prefix-SID: 57 Flags: [N P] Algorithm: 0
      Reachability          : 2001:0:57:59::/64 Metric: 10 Type: 1 Up
      Reachability          : 2001:0:57:172::/64 Metric: 10 Type: 1 Up
      Reachability          : 2001:0:57:303::/64 Metric: 10 Type: 1 Up
      Reachability          : 2001:0:57:304::/64 Metric: 10 Type: 1 Up
      Reachability          : 2002::57/128 Metric: 0 Type: 1 Up
        SR Prefix-SID: 157 Flags: [N P] Algorithm: 0
        SR Prefix-SID: 728 Flags: [N P] Algorithm: 128
      Router Capabilities: Router Id: 10.0.0.57 Flags: []
        Maximum SID depth:
          Base MPLS imposition (MSD type 1):  12
        SR Capability: Flags: [I V]
          SRGB Base: 20000 Range: 2000
        Algorithms:  0, 128
        Flex Algo: Algorithm: 128 Metric: Min Unidirectional Delay Metric (1) Calc: SPF (0) Prio: 255
          Flags: [M] 0x80
    PE32-J2-172.00-00            98   5261   478    235 L2  0100.0000.0172.00-00  <>
      LSP generation remaining wait time: 0 ms
      Time remaining until refresh: 178 s
      NLPID: 0x8E(IPv6)
      Hostname: PE32-J2-172
      Area addresses: 49.0000
      Interface address: 2001:0:172:303::172
      Interface address: 2001:0:57:172::172
      Interface address: 2002::172
      IS Neighbor          : juniper_303_mx204.00 Metric: 10
        Adj-sid: 362145 flags: [L V F] weight: 0x0
      IS Neighbor          : NOKIA-SR2-57.00     Metric: 100
        Adj-sid: 362144 flags: [L V F] weight: 0x0
      Reachability          : 2001:0:172:303::/64 Metric: 10 Type: 1 Up
      Reachability          : 2001:0:57:172::/64 Metric: 100 Type: 1 Up
      Reachability          : 2002::172/128 Metric: 0 Type: 1 Up
        SR Prefix-SID: 1172 Flags: [N] Algorithm: 0
      Router Capabilities: Router Id: 10.0.0.172 Flags: []
        SR Local Block:
          SRLB Base: 965536 Range: 65536
        Area leader priority: 250 algorithm: 0
        Maximum SID depth:
          Base MPLS imposition (MSD type 1):  12
        SR Capability: Flags: [V]
          SRGB Base: 20000 Range: 2000
```

## show isis flex-algo

```text

IS-IS Instance: IPV6 VRF: default

```

## show isis flex-algo path detail

```text
```

## show isis segment-routing tunnel

```text
  Index     Endpoint          Next Hop/Tunnel Index      Interface    Labels   
--------- ----------------- -------------------------- -------------- ---------
  1         2002::59/128      TI-LFA (1)                 -            [ 20159 ]
  2         2002::57/128      TI-LFA (1)                 -            [ 20157 ]
  3         2002::303/128     TI-LFA (2)                 -            [ 3 ]    
  4         2002::304/128     TI-LFA (1)                 -            [ 20304 ]

```

## show isis segment-routing prefix-segments

```text

System ID: PE32-J2-172			Instance: 'IPV6'
SR supported Data-plane: MPLS			SR Router ID: 10.0.0.172

Node: 10     Proxy-Node: 0      Prefix: 0       Total Segments: 10

Flag Descriptions: R: Re-advertised, N: Node Segment, P: no-PHP
                   E: Explicit-NULL, V: Value, L: Local
Segment status codes: * - Self originated Prefix, L1 - level 1, L2 - level 2, ! - SR-unreachable,
                      # - Some IS-IS next-hops are SR-unreachable
   Prefix                      SID   Label Type       Flags                        System ID       Level Protection  Algorithm   
   ------------------------- ----- ------- ---------- ---------------------------- --------------- ----- ----------- -------------
   10.0.0.57/32                 57   20057 Node       R:0 N:1 P:1 E:0 V:0 L:0      NOKIA-SR2-57    L2    unprotected SPF         
   2002::57/128                157   20157 Node       R:0 N:1 P:1 E:0 V:0 L:0      NOKIA-SR2-57    L2    node        SPF         
   2002::57/128                728   20728 Node       R:0 N:1 P:1 E:0 V:0 L:0      NOKIA-SR2-57    L2    unprotected 128         
   2002::59/128                159   20159 Node       R:0 N:1 P:1 E:0 V:0 L:0      Nokia-59-IXRe2  L2    node        SPF         
   2002::59/128                928   20928 Node       R:0 N:1 P:1 E:0 V:0 L:0      Nokia-59-IXRe2  L2    unprotected 128         
*  2002::172/128              1172   21172 Node       R:0 N:1 P:0 E:0 V:0 L:0      PE32-J2-172     L2    unprotected SPF         
   2002::303/128               303   20303 Node       R:0 N:1 P:0 E:0 V:0 L:0      juniper_303_mx204 L2    node        SPF         
   2002::303/128              1103   21103 Node       R:0 N:1 P:0 E:0 V:0 L:0      juniper_303_mx204 L2    unprotected 128         
   2002::304/128               304   20304 Node       R:0 N:1 P:0 E:0 V:0 L:0      juniper_304_mx204 L2    node        SPF         
   2002::304/128              1104   21104 Node       R:0 N:1 P:0 E:0 V:0 L:0      juniper_304_mx204 L2    unprotected 128         
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

 C        10.0.0.172/32
           directly connected, Loopback0

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

 C        10.0.0.172/32
           directly connected, Loopback0


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
Displaying 12 of 17 IPv6 routing table entries
Source Codes:
       C - connected, S - static, K - kernel, O3 - OSPFv3,
       B - Other BGP Routes, A B - BGP Aggregate, R - RIP,
       I L1 - IS-IS level 1, I L2 - IS-IS level 2, DH - DHCP,
       NG - Nexthop Group Static Route, M - Martian,
       DP - Dynamic Policy Route, L - VRF Leaked,
       G  - gRIBI, RC - Route Cache Route,
       CL - CBF Leaked Route

 I L2     2001:0:57:59::/64 [115/30]
           via fe80::7a50:7cff:fe46:541d, Ethernet55/1
 C        2001:0:57:172::/64 [0/0]
           via Ethernet53/1, directly connected
 I L2     2001:0:57:303::/64 [115/20]
           via fe80::7a50:7cff:fe46:541d, Ethernet55/1
 I L2     2001:0:57:304::/64 [115/30]
           via fe80::7a50:7cff:fe46:541d, Ethernet55/1
 I L2     2001:0:59:304::/64 [115/30]
           via fe80::7a50:7cff:fe46:541d, Ethernet55/1
 C        2001:0:172:303::/64 [0/0]
           via Ethernet55/1, directly connected
 I L2     2001:0:303:304::/64 [115/20]
           via fe80::7a50:7cff:fe46:541d, Ethernet55/1
 I L2     2002::57/128 [115/20]
           via fe80::7a50:7cff:fe46:541d, Ethernet55/1
 I L2     2002::59/128 [115/30]
           via fe80::7a50:7cff:fe46:541d, Ethernet55/1
 C        2002::172/128 [0/0]
           via Loopback0, directly connected
 I L2     2002::303/128 [115/10]
           via fe80::7a50:7cff:fe46:541d, Ethernet55/1
 I L2     2002::304/128 [115/20]
           via fe80::7a50:7cff:fe46:541d, Ethernet55/1

```

## show mpls route

```text
MPLS forwarding table (Label [metric] Vias) - 6 routes 
MPLS next-hop resolution allow default route: False
Metric Codes:
          A - Active metric
Via Type Codes:
          M - MPLS via, LP - LDP pseudowire via,
          I - IP lookup via, V - VLAN via,
          VA - EVPN VLAN aware via, ES - EVPN ethernet segment via,
          VF - EVPN VLAN flood via, AF - EVPN VLAN aware flood via,
          NG - Nexthop group via, BP - BGP pseudowire via,
          VP - VPWS pseudowire via, MSP - Static pseudowire via

 20157   A[1]
                via M, ::, forward
                    EgressACL: apply
                  via TI-LFA tunnel index 1
                    via fe80::7a50:7cff:fe46:541d, Ethernet55/1, label imp-null(3)
                    backup via fe80::c214:b8ff:fe21:ca6d, Ethernet53/1, label imp-null(3)
 20159   A[1]
                via M, ::, forward
                    EgressACL: apply
                  via TI-LFA tunnel index 1
                    via fe80::7a50:7cff:fe46:541d, Ethernet55/1, label imp-null(3)
                    backup via fe80::c214:b8ff:fe21:ca6d, Ethernet53/1, label imp-null(3)
 20303   A[1]
                via M, ::, pop
                    EgressACL: apply
                  via TI-LFA tunnel index 2
                    via fe80::7a50:7cff:fe46:541d, Ethernet55/1, label imp-null(3)
                    backup via fe80::c214:b8ff:fe21:ca6d, Ethernet53/1, label 20303
 20304   A[1]
                via M, ::, forward
                    EgressACL: apply
                  via TI-LFA tunnel index 1
                    via fe80::7a50:7cff:fe46:541d, Ethernet55/1, label imp-null(3)
                    backup via fe80::c214:b8ff:fe21:ca6d, Ethernet53/1, label imp-null(3)
 362144  A[1]
                via M, fe80::c214:b8ff:fe21:ca6d, pop
                    EgressACL: apply
                    directly connected, Ethernet53/1
                    c0:14:b8:21:ca:6e, vlan 1011
 362145  A[1]
                via M, fe80::7a50:7cff:fe46:541d, pop
                    EgressACL: apply
                    directly connected, Ethernet55/1
                    78:50:7c:46:54:1d, vlan 1009
```

## show mpls lfib route

```text
MPLS forwarding table (Label [metric] Vias) - 6 routes 
MPLS next-hop resolution allow default route: False
Via Type Codes:
          M - MPLS via, LP - LDP pseudowire via,
          I - IP lookup via, V - VLAN via,
          VA - EVPN VLAN aware via, ES - EVPN ethernet segment via,
          VF - EVPN VLAN flood via, AF - EVPN VLAN aware flood via,
          NG - Nexthop group via, BP - BGP pseudowire via,
          VP - VPWS pseudowire via, MSP - Static pseudowire via
Source Codes:
          G - gRIBI, S - Static MPLS route,
          B2 - BGP L2 EVPN, B3 - BGP L3 VPN,
          R - RSVP, P - Pseudowire,
          L - LDP, M - MLDP,
          I>BL - IS-IS SR to BGP LU, IP - IS-IS SR prefix segment,
          IA - IS-IS SR adjacency segment, I>L - IS-IS SR to LDP,
          L>I - LDP to IS-IS SR, OP - Ospf SR prefix segment,
          OA - Ospf SR adjacency segment, OL - Ospf SR segment to LDP,
          L0 - LDP to Ospf SR segment, BL - BGP LU,
          BL>L - BGP LU to LDP, L>BL - LDP to BGP LU,
          ST - SR TE policy, SMP - SR P2MP,
          BL>I - BGP LU to IS-IS SR, DE - Debug LFIB

 IP    20157    [1], 2002::57/128
                via TI-LFA tunnel index 1, forward
                 payload autoDecide, ttlMode uniform, dscpMode uniform, apply egress-acl
                    via fe80::7a50:7cff:fe46:541d, Ethernet55/1, label imp-null(3)
                    backup via fe80::c214:b8ff:fe21:ca6d, Ethernet53/1, label imp-null(3)
 IP    20159    [1], 2002::59/128
                via TI-LFA tunnel index 1, forward
                 payload autoDecide, ttlMode uniform, dscpMode uniform, apply egress-acl
                    via fe80::7a50:7cff:fe46:541d, Ethernet55/1, label imp-null(3)
                    backup via fe80::c214:b8ff:fe21:ca6d, Ethernet53/1, label imp-null(3)
 IP    20303    [1], 2002::303/128
                via TI-LFA tunnel index 2, pop
                 payload autoDecide, ttlMode uniform, dscpMode uniform, apply egress-acl
                    via fe80::7a50:7cff:fe46:541d, Ethernet55/1, label imp-null(3)
                    backup via fe80::c214:b8ff:fe21:ca6d, Ethernet53/1, label 20303
 IP    20304    [1], 2002::304/128
                via TI-LFA tunnel index 1, forward
                 payload autoDecide, ttlMode uniform, dscpMode uniform, apply egress-acl
                    via fe80::7a50:7cff:fe46:541d, Ethernet55/1, label imp-null(3)
                    backup via fe80::c214:b8ff:fe21:ca6d, Ethernet53/1, label imp-null(3)
 IA    362144   [1]
                via M, fe80::c214:b8ff:fe21:ca6d, pop
                 payload autoDecide, ttlMode uniform, apply egress-acl
                 interface Ethernet53/1
 IA    362145   [1]
                via M, fe80::7a50:7cff:fe46:541d, pop
                 payload autoDecide, ttlMode uniform, apply egress-acl
                 interface Ethernet55/1
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
 * >      RD: 10.0.0.57:6002 ip-prefix 57.57.57.57/32
                                 2002::57              -       100     0       i
 * >      RD: 10.0.0.57:6002 ip-prefix 5757::/64
                                 2002::57              -       100     0       i
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
 * >      RD: 10.0.0.57:10000 IPv4 prefix 20.54.1.0/24
                                 10.0.0.57             -       100     0       i
 * >      RD: 10.0.0.57:1 IPv4 prefix 20.57.111.0/24
                                 10.0.0.57             -       100     0       i
 * >      RD: 10.0.0.57:128 IPv4 prefix 20.57.111.0/24
                                 10.0.0.57             -       100     0       i
 * >      RD: 10.0.0.57:129 IPv4 prefix 20.57.111.0/24
                                 10.0.0.57             -       100     0       i
 * >      RD: 10.0.0.57:130 IPv4 prefix 20.57.111.0/24
                                 10.0.0.57             -       100     0       i
 * >      RD: 10.0.0.57:131 IPv4 prefix 20.57.111.0/24
                                 10.0.0.57             -       100     0       i
 * >      RD: 10.0.0.57:132 IPv4 prefix 20.57.111.0/24
                                 10.0.0.57             -       100     0       i
 * >      RD: 10.0.0.57:211 IPv4 prefix 20.57.111.0/24
                                 10.0.0.57             -       100     0       i
 * >      RD: 10.0.0.57:6001 IPv4 prefix 57.1.0.0/24
                                 10.0.0.57             -       100     0       i
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
 * >      RD: 10.0.0.57:1 IPv6 prefix 2600:50:10:57::/64
                                 2002::57              -       100     0       i
 * >      RD: 10.0.0.57:6001 IPv6 prefix 5757:1::/64
                                 2002::57              -       100     0       i
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
BGP neighbor is 1.1.1.1, remote AS 65000, internal link
  BGP version 4, remote router ID 0.0.0.0, VRF default
  Last read never, last write never
  Hold time is 0, keepalive interval is 0 seconds
  Configured hold time is 180, keepalive interval is 60 seconds
  Effective minimum hold time is 3 seconds
  Send failure hold time is 0 seconds
  Hold timer is inactive
  Keepalive timer is inactive
  Connect timer is inactive
  Idle-restart timer is inactive
  BGP state is Idle, Peer is not activated in any address-family mode
  Peering failure hint: Peer is not activated in any address-family mode
  Number of transitions to established: 0
  Last state was Idle
  Last event was ReapplyInboundPolicy
  Types of communities advertised: none
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
Local AS is 65000, local router ID 10.0.0.172
TTL is 255
! Sending extended community not configured, updates will be sent without extended communities or route targets

BGP neighbor is 2002::57, remote AS 65000, internal link
  BGP version 4, remote router ID 10.0.0.57, VRF default
  Inherits configuration from and member of peer-group IBGP-IPV6
  Last read 00:00:01, last write 00:00:02
  Hold time is 90, keepalive interval is 30 seconds
  Configured hold time is 180, keepalive interval is 60 seconds
  Effective minimum hold time is 3 seconds
  Send failure hold time is 0 seconds
  Hold timer is active, time left: 00:01:29
  Keepalive timer is active, time left: 00:00:19
  Connect timer is inactive
  Idle-restart timer is inactive
  BGP state is Established, up for 00:42:32
  Number of transitions to established: 5
  Last state was OpenConfirm
  Last event was RecvUpdate
  Last sent notification:Cease/other configuration change, Last time 00:42:32, First time 15:19:33, Repeats 3
  Types of communities advertised: standard extended large
  Neighbor is a route reflector client
  Neighbor is using global cluster ID 10.0.0.172
  Neighbor Capabilities:
    Multiprotocol IPv4 Unicast: advertised
    Multiprotocol VPN-IPv4: advertised and received and negotiated
    Multiprotocol VPN-IPv6: advertised and received and negotiated
    Multiprotocol L2VPN EVPN: advertised and received and negotiated
    Four Octet ASN: advertised and received and negotiated
    Route Refresh: advertised and received and negotiated
    Enhanced route refresh: advertised
    Send End-of-RIB messages: advertised and received and negotiated
    Additional-paths recv capability:
      IPv4 Unicast: advertised
      VPN-IPv4: advertised
      VPN-IPv6: advertised
      L2VPN EVPN: advertised
    Additional-paths send capability:
    Extended Next-Hop Capability:
      VPN-IPv4: received
  Restart timer is inactive
  End of rib timer is inactive
    VPN-IPv4 End-of-RIB received: Yes
      Received 00:42:05
      Number of stale paths removed after graceful restart: 0
      Number of paths received before End-of-RIB: 9
    VPN-IPv6 End-of-RIB received: Yes
      Received 00:42:05
      Number of stale paths removed after graceful restart: 0
      Number of paths received before End-of-RIB: 2
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
    Opens:                  5         5
    Notifications:          4         0
    Updates:             2161        42
    Keepalives:          2083      1863
    Route Refresh:          0         0
    Total messages:      4253      1910
  Prefix Statistics:
                                   Sent      Rcvd     Best Paths     Best ECMP Paths
    IPv4 Unicast:                     0         0              0                   0
    VPN-IPv4:                         0         9              9                   0
    IPv6 Unicast:                     0         0              0                   0
    VPN-IPv6:                         0         2              2                   0
    EVPN:                             0         2              2                   0
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
    VPN-IPv6 NLRIs dropped due to maximum route limit violation: 0
    L2VPN EVPN NLRIs dropped due to route import match failure: 0
    L2VPN EVPN NLRIs dropped due to unsupported route type: 0
    L2VPN EVPN NLRIs dropped due to maximum route limit violation: 0
    Link-state NLRIs dropped because reception is unsupported: 0
    RT Membership NLRIs dropped due to local origin ASN received from external peer: 0
  Outbound paths dropped by reason:
    IPv4 local address not available: 0
    IPv6 local address not available: 0
  Soft reconfiguration inbound is "None"
Local AS is 65000, local router ID 10.0.0.172
TTL is 255
Local TCP address is 2002::172, local port is 179
Remote TCP address is 2002::57, remote port is 61091
Local next hop for next hop self:
  VPN-IPv4: 10.0.0.172
  VPN-IPv6: 2002::172
  L2VPN EVPN: 2002::172
TCP Socket Information:
  TCP state is ESTABLISHED
  Recv-Q: 0/32768
  Send-Q: 0/46080
  Outgoing Maximum Segment Size (MSS): 1208
  Total Number of TCP retransmissions: 0
  Options:
    Timestamps enabled: yes
    Selective Acknowledgments enabled: no
    Window Scale enabled: yes
    Explicit Congestion Notification (ECN) enabled: no
  Socket Statistics:
    Window Scale (wscale): 0,7
    Retransmission Timeout (rto): 204.0ms
    Round-trip Time (rtt/rtvar): 0.5ms/0.1ms
    Delayed Ack Timeout (ato): 40.0ms
    Congestion Window (cwnd): 10
    TCP Throughput: 191.37 Mbps
    Advertised Recv Window (rcv_space): 14400

BGP neighbor is 2002::303, remote AS 65000, internal link
  BGP version 4, remote router ID 192.168.21.3, VRF default
  Inherits configuration from and member of peer-group IBGP-IPV6
  Last read 00:00:01, last write 00:00:01
  Hold time is 90, keepalive interval is 30 seconds
  Configured hold time is 180, keepalive interval is 60 seconds
  Effective minimum hold time is 3 seconds
  Send failure hold time is 0 seconds
  Hold timer is inactive
  Keepalive timer is inactive
  Connect timer is active, time left: 00:00:00
  Connection interval is 1 seconds
  Failed connection attempts is 1
  Idle-restart timer is inactive
  BGP state is Active
  Peering failure hint: Update Message Error/error with optional attribute
  Number of transitions to established: 37103
  Last state was Idle
  Last event was Start
  Last rcvd notification:Update Message Error/error with optional attribute, Last time 00:00:01, First time 15:22:46, Repeats 37102
  Types of communities advertised: standard extended large
  Neighbor is a route reflector client
  Neighbor is using global cluster ID 10.0.0.172
  Neighbor Capabilities:
    Multiprotocol IPv4 Unicast: advertised
    Multiprotocol VPN-IPv4: advertised and received
    Multiprotocol VPN-IPv6: advertised and received
    Multiprotocol L2VPN EVPN: advertised
    Four Octet ASN: advertised and received
    Route Refresh: advertised and received
    Enhanced route refresh: advertised
    Send End-of-RIB messages: advertised and received
    Additional-paths recv capability:
      IPv4 Unicast: advertised
      VPN-IPv4: advertised
      VPN-IPv6: advertised
      L2VPN EVPN: advertised
    Additional-paths send capability:
    Long Lived Graceful Restart received:
      Helper only
    Extended Next-Hop Capability:
      VPN-IPv4: received
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
    Opens:              37103     37103
    Notifications:          0     37103
    Updates:            85932     37866
    Keepalives:         74218     37114
    Route Refresh:          0         0
    Total messages:    197253    149186
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
  Soft reconfiguration inbound is "None"
Local AS is 65000, local router ID 10.0.0.172
TTL is 255
Local TCP address is 2002::172
Remote TCP address is 2002::303, remote port is 179

```

## show tunnel rib system-tunnel-rib brief

```text
Tunnel RIB: system-tunnel-rib
Endpoint        Tunnel Type     Index(es)   Tunnel Preference   IGP Preference 
-------------- --------------- ----------- ------------------- ----------------
2002::57/128    IS-IS SR IPv6   2           65                  115            
2002::304/128   IS-IS SR IPv6   4           65                  115            
2002::59/128    IS-IS SR IPv6   1           65                  115            
2002::303/128   IS-IS SR IPv6   3           65                  115            

   IGP Metric    Metric Type
---------------- -----------
   20            metric     
   20            metric     
   30            metric     
   10            metric     

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
>C    10.0.0.172/32 [0 pref/0 metric] updated 15:37:24 ago
         via Loopback0, directly connected
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
>P    0.0.0.0/8 [1 pref/0 metric] updated 15:37:23 ago
         via Null0, directly connected [NF]
>P    127.0.0.0/8 [1 pref/0 metric] updated 15:37:23 ago
         via :: [1 pref/1 metric] type ipv4
            via , directly connected
```

## show rib route ipv6

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
>C    2001:0:57:172::/64 [0 pref/0 metric] updated 15:35:45 ago
         via Ethernet53/1, directly connected
>C    2001:0:172:303::/64 [0 pref/0 metric] updated 15:35:42 ago
         via Ethernet55/1, directly connected
>C    2002::172/128 [0 pref/0 metric] updated 15:37:24 ago
         via Loopback0, directly connected
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
>P    ::/96 [1 pref/0 metric] updated 15:37:23 ago
         via Null0, directly connected [NF]
>P    ::ffff:127.0.0.0/104 [1 pref/0 metric] updated 15:37:23 ago
         via :: [1 pref/1 metric] type ipv6
            via , directly connected
>P    fe80::/10 [1 pref/0 metric] updated 15:37:23 ago
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
>I    2001:0:57:59::/64 [115 pref/30 metric] updated 15:35:31 ago
         via fe80::7a50:7cff:fe46:541d, Ethernet55/1
 I    2001:0:57:172::/64 [115 pref/30 metric] updated 15:35:31 ago
         via fe80::7a50:7cff:fe46:541d, Ethernet55/1
>I    2001:0:57:303::/64 [115 pref/20 metric] updated 15:35:31 ago
         via fe80::7a50:7cff:fe46:541d, Ethernet55/1
>I    2001:0:57:304::/64 [115 pref/30 metric] updated 15:35:31 ago
         via fe80::7a50:7cff:fe46:541d, Ethernet55/1
>I    2001:0:59:304::/64 [115 pref/30 metric] updated 15:35:31 ago
         via fe80::7a50:7cff:fe46:541d, Ethernet55/1
>I    2001:0:303:304::/64 [115 pref/20 metric] updated 15:35:31 ago
         via fe80::7a50:7cff:fe46:541d, Ethernet55/1
>I    2002::57/128 [115 pref/20 metric] updated 15:35:31 ago
         via fe80::7a50:7cff:fe46:541d, Ethernet55/1
>I    2002::59/128 [115 pref/30 metric] updated 15:35:31 ago
         via fe80::7a50:7cff:fe46:541d, Ethernet55/1
>I    2002::303/128 [115 pref/10 metric] updated 15:35:31 ago
         via fe80::7a50:7cff:fe46:541d, Ethernet55/1
>I    2002::304/128 [115 pref/20 metric] updated 15:35:31 ago
         via fe80::7a50:7cff:fe46:541d, Ethernet55/1
```

## show platform sand l3 summary

```text
Number of vrfs: 2

Ipv4:
  Routes:       11  backlog:  0  unprogrammed:  0
  Adjacencies:  23  backlog:  0  unprogrammed:  0
Ipv6:
  Routes:       18  backlog:  0  unprogrammed:  0
  Adjacencies:  23  backlog:  0  unprogrammed:  0
Mpls:
  Routes:       6  backlog:  0  unprogrammed:  0
  Adjacencies:  2  backlog:  0  unprogrammed:  0

Jericho2 Ip Fecs:
  Non-ecmp fecs:  4104  ecmp fecs:  0  fec entries:  4104
Jericho2 Mpls Fecs:
  Non-ecmp fecs:  2  ecmp fecs:  0  fec entries:  2
Jericho2 Vxlan Tunnel Fecs:
  Non-ecmp fecs:  0  ecmp fecs:  0  fec entries:  0
  Number of vxlan tunnels configured: 0

Jericho2 Lpm Routes:
  Routes:   11  unprogrammed:   0   
  Routes6:  18  unprogrammed6:  0   
  Backlog:  0 

Jericho2 Lpm:
  TCAM entries used:   3  Percent free:  99  ADS2 entries used:   3  Percent free:  99
  Pivot buckets used:  4  Rows used:     2   Entries Per Bucket:  0  Percent free:  99
  Route buckets used:  8  Rows used:     3   Entries Per Bucket:  3  Percent free:  99

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
  FixedSystem: 4
Egress Sflow rewrite entries in use (in each fap):
  FixedSystem: 0

Egress rewrite chains in backlog: resource-full 0, no-interface 0

Glem entries used per fap :
  FixedSystem: 4102

Jericho2 Fec:
  Maximum FEC hierarchy levels:  3
  ReusedEcmp:  0  allocs:  14  frees:  6  shuffles:  0  cmds:  0
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
    Non-ecmp fecs:            4   ecmp fecs:            0  
    Non-ecmp (Percent free):  99  ecmp (Percent free):  100

Lpm Detail:
  Requests:  81  cleanses:  18  batches:  18  avg batch size:  4

Jericho Arp:
  ArpTable writes:      16847  queued      0   
  IngressTable writes:  74452  queued      0   
  Coprocessors:         1      in CmdRing

Tunnel Counter Status
  Number of MPLS tunnels:                  4    
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
|0  |10.0.0.172/32     |TRAP | CoppSystemIpUcast  |0    |  -     | Receive           |  -  |524291|   -   
|0  |127.0.0.0/8       |TRAP | CoppSystemL3DstMiss|0    |  -     | ArpTrap           |  -  |524294|   -   
|0  |0.0.0.0/0         |TRAP | CoppSystemL3LpmOver|0    |  -     | SlowReceive       |  -  |524292|   -   
|2  |0.0.0.0/8         |DROP | DROP               |0    |  -     |                   |  -  |288368|   -   
|2  |127.0.0.0/8       |TRAP | CoppSystemL3DstMiss|0    |  -     | ArpTrap           |  -  |524294|   -   
|2  |192.168.20.0/32   |TRAP | CoppSystemIpBcast  |0    |  -     | BcastReceive      |  -  |524288|   -   
|2  |192.168.20.172/32 |TRAP | CoppSystemIpUcast  |0    |  -     | Receive           |  -  |524291|   -   
|2  |192.168.21.255/32 |TRAP | CoppSystemIpBcast  |0    |  -     | BcastReceive      |  -  |524288|   -   
|2  |192.168.20.0/23   |TRAP | CoppSystemL3DstMiss|0    |  -     | ArpTrap           |  -  |524294|   -   
|2  |0.0.0.0/0         |TRAP | CoppSystemL3DstMiss|0    |  -     | ArpTrap           |  -  |524294|   -   

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
|  -  |288368|DROP | DROP               |0    |  -     |                   |   -   
|  -  |288370|ROUTE| Et53/1             |1011 |107517  | c0:14:b8:21:ca:6e |   -   
|  -  |288374|ROUTE| Et55/1             |1009 |107518  | 78:50:7c:46:54:1d |   -   
|  -  |288376|ROUTE| Et55/1             |1009 |107518  | 78:50:7c:46:54:1d |   -   
|  -  |524288|TRAP | CoppSystemIpBcast  |0    |  -     | BcastReceive      |   -   
|  -  |524291|TRAP | CoppSystemIpUcast  |0    |  -     | Receive           |   -   
|  -  |524292|TRAP | CoppSystemL3LpmOver|0    |  -     | SlowReceive       |   -   
|  -  |524294|TRAP | CoppSystemL3DstMiss|0    |  -     | ArpTrap           |   -   
|  -  |525303|TRAP | CoppSystemL3DstMiss|1009 |1009    | ArpTrap           |   -   
|  -  |525305|TRAP | CoppSystemL3DstMiss|1011 |1011    | ArpTrap           |   -   
|  -  |528484|ROUTE| Et55/1             |1009 |107520  | 78:50:7c:46:54:1d |   -   
|  -  |528485|ROUTE| Et53/1             |1011 |107521  | c0:14:b8:21:ca:6e |   -   
|  -  |528486|ROUTE| Et55/1             |1009 |107522  | 78:50:7c:46:54:1d |   -   
|  -  |528487|ROUTE| Et53/1             |1011 |107523  | c0:14:b8:21:ca:6e |Mpush 20303

```

