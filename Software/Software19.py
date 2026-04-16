from pwn import *

InOut = remote("software-19.challs.olicyber.it",  13002)

exe = ELF("/home/tommasoraccuia/Dev/CyberChallenge/Software/sw-19")

InOut.recvuntil(b'... Invia un qualsiasi carattere per iniziare ...')
InOut.sendline(b'a')

for _ in range(20):
    InOut.recvuntil(b'-> ')
    funcName = InOut.recvuntil(b': ')
    funcName = funcName[:-2]

    print(funcName)
    #Conversione in hex dell'indirizzo
    addr = exe.sym[funcName]
    addr_hex = hex(addr)

    print(f"Indirizzo trovato: {addr_hex}")

    InOut.sendline(addr_hex)
    
print(InOut.recvline())