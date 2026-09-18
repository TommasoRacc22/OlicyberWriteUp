# Crittografia — Introduzione

Due sfide introduttive sull'uso della libreria PyCryptodome.

## Cripto13 — Diffie-Hellman + AES-CBC
File: `Cripto13.py`

Viene fornito un gruppo di Diffie-Hellman (il primo `p` è il classico primo MODP a
1536 bit), la chiave pubblica di Alice e un messaggio cifrato in **AES-CBC**.

Passi della soluzione:
1. Si calcola la chiave condivisa elevando la chiave pubblica di Alice al proprio
   esponente segreto modulo `p`.
2. Dalla chiave condivisa si ricava la chiave AES a 128 bit.
3. Si decifra il messaggio con `AES.MODE_CBC` usando l'IV fornito e si rimuove il
   padding PKCS#7 con `unpad`, ottenendo la flag.

## Cripto14 — Hash, HMAC, DSA
File: `Cripto14.py`

Sfida a risposte multiple che verifica la conoscenza delle primitive:
- **SHA3-384** di una stringa data;
- **HMAC-SHA224** di un messaggio con chiave fornita;
- import di una **chiave DSA** in formato DER (hex) per leggerne i parametri
  `p, q, g, x, y`;
- generazione di un **numero primo** di lunghezza fissata (1230 bit) con
  `Crypto.Util.number.getPrime`.

Ogni `print` produce una delle risposte richieste dal server.
