# ReverseSPN

**Categoria:** Software / Reverse Engineering

## Descrizione
Binario ELF a 64 bit (`reverSPN`) che simula un login. Chiede *Username* e *Password*
e confronta l'input con una password valida usando un **cifrario SPN**
(Substitution-Permutation Network) implementato internamente.

## Analisi
Il binario è *stripped*, ma le stringhe rivelano il flusso: banner "Login",
messaggi `[+] Correct password!` / `[!] Incorrect password!`. Il confronto avviene
tramite `strncmp`/`memcmp` dopo aver passato l'input attraverso i round di
sostituzione (S-box) e permutazione.

## Soluzione
Si reversa la routine di cifratura (S-box e permutazione dei round) e, dato che una
rete SP è invertibile, si applica la **funzione inversa** (S-box inversa +
permutazione inversa) al valore target hardcoded per recuperare la password/flag
corretta. In alternativa, per uno spazio ridotto, si può fare bruteforce.

> Nota: `ReserveSPN.py` è il file di lavoro per lo script di soluzione.
