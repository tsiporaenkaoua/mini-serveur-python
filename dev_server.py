import os
import time
import subprocess

FILENAME = "serveur.py"  # Ton fichier serveur principal

def run_server():
    return subprocess.Popen(["python", FILENAME])

def watch_file():
    last_mtime = None
    process = run_server()
    try:
        while True:
            mtime = os.path.getmtime(FILENAME)
            if last_mtime is None:
                last_mtime = mtime

            if mtime != last_mtime:
                print("🔄 Changement détecté, redémarrage du serveur...")
                process.terminate()
                process.wait()
                process = run_server()
                last_mtime = mtime

            time.sleep(1)
    except KeyboardInterrupt:
        print("🛑 Arrêt manuel.")
        process.terminate()
        process.wait()

if __name__ == "__main__":
    watch_file()
