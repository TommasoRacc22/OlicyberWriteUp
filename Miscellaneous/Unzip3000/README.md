# Unzip3000

**Categoria:** Miscellaneous · **Flag:** `flag{Un0_z1p_d3n7r0_un0_z1p_1mp0551b1l3!}`

## Descrizione
Un archivio zip che contiene un altro zip, che ne contiene un altro… per **3000
livelli** di annidamento. Aprirli a mano è impossibile.

## Soluzione
Script che estrae ricorsivamente ogni `flagN.zip`, cancella l'archivio appena
estratto e passa al successivo (da 3000 a 1), finché non resta il file finale con
la flag:

```python
with zipfile.ZipFile(current_zip) as z:
    z.extractall()
os.remove(current_zip)
```

Vedi `Unzip.py`. Al termine rimane `flag.txt`.
