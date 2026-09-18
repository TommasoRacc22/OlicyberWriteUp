# ClassicCipher

**Categoria:** Crittografia · **Flag:** `flag{simple_rotor_bruteforcing}`

## Descrizione
Viene fornito lo script `challenge.py` con le funzioni di `encrypt`/`decrypt` e un
ciphertext hardcoded:

```
xcqv{gvyavn_zvztv_etvtddlnxcgy}
```

## Analisi
Il cifrario è una variante di **cifrario a rotore/Cesare** in cui la chiave è
l'alfabeto ruotato di `i` posizioni (`generateKey(i)`) e viene ulteriormente ruotata
di un carattere ad ogni lettera cifrata. Di fatto la sicurezza dipende da un solo
parametro `i` compreso tra 1 e 24: lo spazio delle chiavi è minuscolo.

## Soluzione
Bruteforce di tutte le 24 rotazioni possibili, cercando l'output che ha la forma di
una flag (`flag{...}`):

```python
for i in range(1, 25):
    key = generateKey(i)
    print(decrypt(ciphertext, key))
```

Una sola rotazione produce testo leggibile → la flag.
