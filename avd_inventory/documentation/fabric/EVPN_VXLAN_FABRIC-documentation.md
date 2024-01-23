# EVPN_VXLAN_FABRIC

## Table of Contents

- [Fabric Switches and Management IP](#fabric-switches-and-management-ip)
  - [Fabric Switches with inband Management IP](#fabric-switches-with-inband-management-ip)
- [Fabric Topology](#fabric-topology)
- [Fabric IP Allocation](#fabric-ip-allocation)
  - [Fabric Point-To-Point Links](#fabric-point-to-point-links)
  - [Point-To-Point Links Node Allocation](#point-to-point-links-node-allocation)
  - [Loopback Interfaces (BGP EVPN Peering)](#loopback-interfaces-bgp-evpn-peering)
  - [Loopback0 Interfaces Node Allocation](#loopback0-interfaces-node-allocation)
  - [VTEP Loopback VXLAN Tunnel Source Interfaces (VTEPs Only)](#vtep-loopback-vxlan-tunnel-source-interfaces-vteps-only)
  - [VTEP Loopback Node allocation](#vtep-loopback-node-allocation)

## Fabric Switches and Management IP

| POD | Type | Node | Management IP | Platform | Provisioned in CloudVision | Serial Number |
| --- | ---- | ---- | ------------- | -------- | -------------------------- | ------------- |
| EVPN_VXLAN_FABRIC | l3leaf | Leaf11-T3-3 | 192.168.0.21/24 | cEOS | Provisioned | - |
| EVPN_VXLAN_FABRIC | l3leaf | Leaf12-T3-4 | 192.168.0.22/24 | cEOS | Provisioned | - |
| EVPN_VXLAN_FABRIC | l3leaf | Leaf21-Jp-5 | 192.168.0.23/24 | cEOS | Provisioned | - |
| EVPN_VXLAN_FABRIC | l3leaf | Leaf22-Jp-6 | 192.168.0.24/24 | cEOS | Provisioned | - |
| EVPN_VXLAN_FABRIC | spine | Spine1-J-2 | 192.168.0.11/24 | cEOS | Provisioned | - |

> Provision status is based on Ansible inventory declaration and do not represent real status from CloudVision.

### Fabric Switches with inband Management IP

| POD | Type | Node | Management IP | Inband Interface |
| --- | ---- | ---- | ------------- | ---------------- |

## Fabric Topology

| Type | Node | Node Interface | Peer Type | Peer Node | Peer Interface |
| ---- | ---- | -------------- | --------- | ----------| -------------- |
| l3leaf | Leaf11-T3-3 | Ethernet1 | spine | Spine1-J-2 | Ethernet1 |
| l3leaf | Leaf11-T3-3 | Ethernet47 | mlag_peer | Leaf12-T3-4 | Ethernet47 |
| l3leaf | Leaf11-T3-3 | Ethernet48 | mlag_peer | Leaf12-T3-4 | Ethernet48 |
| l3leaf | Leaf12-T3-4 | Ethernet1 | spine | Spine1-J-2 | Ethernet2 |
| l3leaf | Leaf21-Jp-5 | Ethernet1 | spine | Spine1-J-2 | Ethernet3 |
| l3leaf | Leaf21-Jp-5 | Ethernet47 | mlag_peer | Leaf22-Jp-6 | Ethernet47 |
| l3leaf | Leaf21-Jp-5 | Ethernet48 | mlag_peer | Leaf22-Jp-6 | Ethernet48 |
| l3leaf | Leaf22-Jp-6 | Ethernet1 | spine | Spine1-J-2 | Ethernet4 |

## Fabric IP Allocation

### Fabric Point-To-Point Links

| Uplink IPv4 Pool | Available Addresses | Assigned addresses | Assigned Address % |
| ---------------- | ------------------- | ------------------ | ------------------ |
| 172.30.255.0/24 | 256 | 8 | 3.13 % |

### Point-To-Point Links Node Allocation

| Node | Node Interface | Node IP Address | Peer Node | Peer Interface | Peer IP Address |
| ---- | -------------- | --------------- | --------- | -------------- | --------------- |
| Leaf11-T3-3 | Ethernet1 | 172.30.255.1/31 | Spine1-J-2 | Ethernet1 | 172.30.255.0/31 |
| Leaf12-T3-4 | Ethernet1 | 172.30.255.3/31 | Spine1-J-2 | Ethernet2 | 172.30.255.2/31 |
| Leaf21-Jp-5 | Ethernet1 | 172.30.255.5/31 | Spine1-J-2 | Ethernet3 | 172.30.255.4/31 |
| Leaf22-Jp-6 | Ethernet1 | 172.30.255.7/31 | Spine1-J-2 | Ethernet4 | 172.30.255.6/31 |

### Loopback Interfaces (BGP EVPN Peering)

| Loopback Pool | Available Addresses | Assigned addresses | Assigned Address % |
| ------------- | ------------------- | ------------------ | ------------------ |
| 192.0.255.0/24 | 256 | 5 | 1.96 % |

### Loopback0 Interfaces Node Allocation

| POD | Node | Loopback0 |
| --- | ---- | --------- |
| EVPN_VXLAN_FABRIC | Leaf11-T3-3 | 192.0.255.3/32 |
| EVPN_VXLAN_FABRIC | Leaf12-T3-4 | 192.0.255.4/32 |
| EVPN_VXLAN_FABRIC | Leaf21-Jp-5 | 192.0.255.5/32 |
| EVPN_VXLAN_FABRIC | Leaf22-Jp-6 | 192.0.255.6/32 |
| EVPN_VXLAN_FABRIC | Spine1-J-2 | 192.0.255.1/32 |

### VTEP Loopback VXLAN Tunnel Source Interfaces (VTEPs Only)

| VTEP Loopback Pool | Available Addresses | Assigned addresses | Assigned Address % |
| --------------------- | ------------------- | ------------------ | ------------------ |
| 192.0.254.0/24 | 256 | 4 | 1.57 % |

### VTEP Loopback Node allocation

| POD | Node | Loopback1 |
| --- | ---- | --------- |
| EVPN_VXLAN_FABRIC | Leaf11-T3-3 | 192.0.254.3/32 |
| EVPN_VXLAN_FABRIC | Leaf12-T3-4 | 192.0.254.3/32 |
| EVPN_VXLAN_FABRIC | Leaf21-Jp-5 | 192.0.254.5/32 |
| EVPN_VXLAN_FABRIC | Leaf22-Jp-6 | 192.0.254.5/32 |
