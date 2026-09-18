# OlicyberWriteUp

Write-up delle challenge affrontate durante le **OliCyber** (Olimpiadi Italiane di Cybersecurity).

Ogni sfida ha la sua cartella con dentro i file originali e un `README.md` che spiega
il ragionamento, la vulnerabilità e la soluzione (con lo script di exploit dove presente).

## Indice

### Crittografia
| Challenge | Argomento |
|-----------|-----------|
| [ClassicCipher](Crittografia/ClassicCipher/) | Cifrario a rotore, bruteforce delle chiavi |
| [Introduzione — Cripto13](Crittografia/Introduzione/) | Diffie-Hellman + decifratura AES-CBC |
| [Introduzione — Cripto14](Crittografia/Introduzione/) | Hashing (SHA-3 / HMAC), import chiave DSA, generazione primi |

### Software (Pwn / Reverse)
| Challenge | Argomento |
|-----------|-----------|
| [Introduzione — Software19](Software/Introduzione/) | Risoluzione veloce indirizzi funzioni con pwntools |
| [Introduzione — Software20](Software/Introduzione/) | Iniezione di shellcode |
| [ReverseSPN](Software/ReverseSPN/) | Reverse engineering di un login (cifrario SPN) |
| [Formatted](Software/) | Format string exploit |

### Web
| Challenge | Argomento |
|-----------|-----------|
| [Introduzione — Web20](Web/Introduzione/) | SQL injection time-based blind |

### Miscellaneous
| Challenge | Argomento |
|-----------|-----------|
| [Unzip3000](Miscellaneous/Unzip3000/) | Estrazione automatica di zip annidati |
| [Unzip2.0](Miscellaneous/Unzip2.0/) | Zip annidati protetti da password (rockyou) |
| [CorruptedFlag](Miscellaneous/CorruptedFlag/) | Riparazione di un file GIF corrotto |
| [ExecuteMe](Miscellaneous/ExecuteMe/) | Catena di file annidati (mp3 → zip → QR) |

---
> ⚠️ Le flag riportate sono quelle delle istanze usate durante l'allenamento e servono
> solo a scopo didattico.
