# CorruptedFlag

**Categoria:** Miscellaneous (Forensics)

## Descrizione
Viene fornito un file GIF che non si apre. Ispezionando l'header con `xxd` si nota
che i primi byte sono errati:

```
00000000: 4748 4946 5f4f 5f47 4946 3839 61   GHIF_O_GIF89a
```

Il magic number di una GIF valida è `GIF89a` (`47 49 46 38 39 61`), ma il file inizia
con `GHIF_O_` prima della sequenza corretta.

## Soluzione
Si ripara l'header rimuovendo i 7 byte spuri iniziali, in modo che il file inizi
esattamente con `GIF89a`:

```bash
tail -c +8 corrupted_file.gif > fixed.gif
```

Aperta l'immagine riparata si legge la flag.
