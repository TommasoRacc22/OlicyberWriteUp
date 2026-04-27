import zipfile
import os
import glob

def unzip_all():
    contatore = 0
    i = 3000

    while True:
        zip_files = glob.glob('flag' + str(i) + '.zip')
        i = i - 1
        if not zip_files:
            print(f"\nFinito! Estrazioni totali completate: {contatore}")
            print("Guarda nella cartella per scoprire il file finale.")
            break
            
        current_zip = zip_files[0]
        print(f"Estraggo: {current_zip} ...", end="\r")
        
        try:

            with zipfile.ZipFile(current_zip, 'r') as zip_ref:
                zip_ref.extractall()
            
            os.remove(current_zip)
            contatore += 1
            
        except zipfile.BadZipFile:
            print(f"\nErrore: {current_zip} non è un file zip valido o è corrotto.")
            break

if __name__ == '__main__':
    print("Inizio estrazione automatica...")
    unzip_all()