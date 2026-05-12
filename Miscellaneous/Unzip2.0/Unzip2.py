import zipfile
import zlib

def crack_zip(zip_name, file_to_extract, password_list):
    print(f"Tentativo di crack su {zip_name}...")
    
    with zipfile.ZipFile(zip_name) as z:
        for pwd in password_list:
            pwd = pwd.strip()
            try:
                content = z.read(file_to_extract, pwd=pwd.encode())
                
                with open(file_to_extract, 'wb') as f:
                    f.write(content)
                print(f"✅ Successo! Password trovata: {pwd}")
                return True 
                
            except (RuntimeError, zipfile.BadZipFile, zlib.error):
                continue
    
    print(f"❌ Fallito: Nessuna password in lista funziona per {zip_name}")
    return False

if __name__ == '__main__':
    
    with open('rockyou.txt', 'r', encoding='utf-8', errors='ignore') as f:
        lines = f.readlines()

    for i in range(100):
        index = 100 - i
        current_zip = str(index) + ".zip"
        next_file = str(index - 1) + ".zip"
        
        if current_zip == "1.zip":
            crack_zip("1.zip", "flag.txt", lines)

        if crack_zip(current_zip, next_file, lines):
            print("Ora puoi procedere con il file successivo.")
        
        