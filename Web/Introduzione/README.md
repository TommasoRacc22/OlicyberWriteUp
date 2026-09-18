# Web — Introduzione (SQL Injection)

File: `Web20.py`

## Descrizione
L'applicazione espone alcune API (`/api/logic`, `/api/union`, `/api/blind`,
`/api/time`) che inoltrano una `query` a un database, protette da un token
anti-CSRF ottenibile via `/api/get_token`. La flag è memorizzata nella tabella
`flags`.

## Vulnerabilità
Gli endpoint sono vulnerabili a **SQL injection**. L'endpoint `/api/time` in
particolare non restituisce il risultato in chiaro ma permette una
**blind injection time-based** tramite `SLEEP()`.

## Soluzione
Estrazione carattere per carattere della flag:
1. Si recupera e allega il token CSRF ad ogni richiesta.
2. Per ogni posizione e per ogni valore ASCII (32–126) si invia:
   ```sql
   1' AND (SELECT SLEEP(1) FROM flags WHERE HEX(flag) LIKE '<prefix_hex>%')='1
   ```
3. Se la risposta impiega ≥ 1 secondo, il carattere ipotizzato è corretto e si
   passa al successivo. Si usa `HEX(flag) LIKE ...` per confronti byte-esatti e
   case-sensitive.

Lo script ricostruisce così l'intera flag.
