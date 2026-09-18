# Software — Introduzione (Pwntools)

Due sfide introduttive di sfruttamento con [pwntools](https://docs.pwntools.com/).

## Software19 — Risoluzione veloce di indirizzi
File: `Software19.py` · binario: `../sw-19`

Il server invia una lista di 20 nomi di funzione e per ciascuno chiede il relativo
indirizzo nel binario, in esadecimale, **entro 10 secondi**. Impossibile a mano,
banale via script.

Soluzione: si carica il binario con `ELF()`, si legge ogni nome, si recupera
l'indirizzo con `exe.sym[funcName]` e lo si rinvia in hex. Venti iterazioni in loop
completano la sfida in tempo e restituiscono la flag.

## Software20 — Iniezione di shellcode
File: `Software20.py`

Il server chiede di inviare esattamente N byte che verranno eseguiti come codice.

Soluzione:
1. Si genera lo shellcode `execve("/bin/sh")` con
   `shellcraft.amd64.linux.sh()` + `asm()`.
2. Si dichiara la dimensione (100 byte) e si fa il **padding con NOP** (`\x90`)
   fino a 100 byte con `rjust`.
3. Si invia e si ottiene una shell (`interactive()`), da cui si legge la flag.
