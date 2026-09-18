# Unzip2.0

**Categoria:** Miscellaneous · **Flag:** `flag{1snt3asyUnzipTh4t}`

## Descrizione
Evoluzione di Unzip3000: **100 zip annidati** (`100.zip` → … → `1.zip` →
`flag.txt`), ma ciascuno è **protetto da password**.

## Soluzione
Per ogni livello si fa **dictionary attack** con la wordlist `rockyou.txt`: si prova
ogni password finché `z.read(...)` non solleva più eccezioni, poi si scrive il file
estratto e si passa al livello successivo (da 100 a 1).

```python
content = z.read(file_to_extract, pwd=pwd.encode())
```

Vedi `Unzip2.py`. La `rockyou.txt` non è inclusa nel repo per dimensione.
