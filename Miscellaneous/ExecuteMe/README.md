# ExecuteMe

**Categoria:** Miscellaneous

## Descrizione
Catena di file annidati che porta alla flag. Il binario ELF `execute-me` è un
depistaggio: le sue stringhe dicono *"La flag non è qui :)"*.

## Catena di file
1. `CopyExe.zip` → contiene `listen-to-me.mp3`.
2. `listen-to-me.zip` → contiene `scan-me.png`.
3. `scan-me.png` è un'immagine **547×547 in bianco e nero**: un **QR code**.

## Soluzione
Si estraggono gli archivi in cascata (entrambi hanno alcuni byte extra all'inizio,
ma `unzip` li processa comunque) fino ad arrivare a `scan-me.png`. Scansionando il
QR code si ottiene la flag.

```bash
unzip CopyExe.zip        # -> listen-to-me.mp3
unzip listen-to-me.zip   # -> scan-me.png (QR code)
```
