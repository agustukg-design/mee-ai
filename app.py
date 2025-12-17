import os
import sys
import time

# MENDAPATKAN JALUR PASTI (ABSOLUTE PATH)
# Ini kunci agar Linux tidak bingung mencari file di latar belakang
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
DATA_PATH = os.path.join(BASE_DIR, 'data.pdf')

def starting_cognitive_layer():
    print("--- MEE AI COGNITIVE LAYER STARTING ---")
    
    # Validasi keberadaan file data.pdf agar sistem tidak crash
    if not os.path.exists(DATA_PATH):
        print(f"ERROR: File {DATA_PATH} tidak ditemukan.")
        sys.exit(1)
        
    print(f"STATUS: Berhasil terhubung ke basis data kognitif.")
    print("MEE AI sedang berjalan di latar belakang sebagai Daemon...")
    
    # Loop abadi agar layanan tetap hidup (Running)
    while True:
        time.sleep(60)

if __name__ == "__main__":
    try:
        starting_cognitive_layer()
    except Exception as e:
        print(f"CRITICAL ERROR: {str(e)}")
        sys.exit(1)
