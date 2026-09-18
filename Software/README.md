# Software

Challenge di **binary exploitation** e **reverse engineering**.

- [Introduzione](Introduzione/) — Software19 (symbol lookup con pwntools) e
  Software20 (iniezione di shellcode).
- [ReverseSPN](ReverseSPN/) — reversing di un login basato su cifrario SPN.
- **Formatted** (`Formatted.py`) — vedi sotto.

## Formatted — Format String
File: `Formatted.py`

Il programma passa l'input dell'utente direttamente a una funzione della famiglia
`printf` senza format string, creando una **format string vulnerability**.

Soluzione con pwntools: si usa `fmtstr_payload(offset, {target_addr: value})` per
scrivere il valore `10` all'indirizzo `0x40404c` (una variabile di controllo).
L'offset degli argomenti sullo stack è `6`. Una volta scritto il valore atteso, il
programma stampa la flag.
