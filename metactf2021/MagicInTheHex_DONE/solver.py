#!/usr/bin/env python3

with open("/mnt/f/VMs/Windows 10/Windows 10 x64.vmdk") as f:
    firstline = f.readline().rstrip()

print(firstline)
