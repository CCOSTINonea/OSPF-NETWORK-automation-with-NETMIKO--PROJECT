# OSPF Network Automation with Netmiko

This project automates Cisco router configuration in GNS3 using Python and Netmiko. It supports:

## Features
- **Interface IP setup**: Interactive script asks for interface name, IP, and subnet.
- **OSPF configuration**: Automatically converts subnet mask to wildcard and applies `network` commands.
- **SSH backup**: Connects to devices from a `.csv` file and saves `show run` output with timestamped filenames.

## Tech stack
- Python 3
- Netmiko
- CSV
- SSH
- GNS3 + Cisco IOS images

Tested on a topology with 4 routers, a switch, VMs, and access via a loopback cloud connection.
