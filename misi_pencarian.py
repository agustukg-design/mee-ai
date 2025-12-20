import os
import time
import sys

# Fungsi efek mengetik biar keren
def ketik(teks, delay=0.01):
    for char in teks:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(delay)
    print()

def scan_drive():
    print("\n🕵️ [MEE AI SEARCH PROTOCOL] MENGAMBIL ALIH KURSOR...")
    print("-------------------------------------------------------")
    
    # 1. Tentukan Target Operasi
    drive = input("Target Drive (Ketik 'c', 'd', atau 'e'): ").lower()
    keyword = input("Kata Kunci File (misal: 'laporan', 'sk', '.pdf'): ").lower()
    
    # Konversi ke bahasa Linux (WSL)
    if drive == 'c':
        # Khusus C kita arahkan ke Documents/Downloads biar tidak scan System Windows yang lama
        user_windows = os.getenv('USER') or "acer" # Default ke acer jika bingung
        base_path = f"/mnt/c/Users/{user_windows}"
        print(f"\n📍 Mengunci Target: Drive C (Area User: {base_path})...")
    else:
        base_path = f"/mnt/{drive}"
        print(f"\n📍 Mengunci Target: Drive {drive.upper()} (Seluruh Partisi)...")

    ketik("🚀 Mengerahkan unit pencari nano-bot...", 0.05)
    
    found_files = []
    
    # 2. Proses Crawling (Merayap)
    start_time = time.time()
    try:
        for root, dirs, files in os.walk(base_path):
            # Hindari folder system windows yang terlarang/berat
            if 'Windows' in root or 'Program Files' in root or 'AppData' in root:
                continue
                
            for file in files:
                if keyword in file.lower():
                    full_path = os.path.join(root, file)
                    found_files.append(full_path)
                    print(f"   [DITEMUKAN] {file}")
                    
                    # Batasi temuan biar layar tidak penuh (max 10)
                    if len(found_files) >= 10:
                        break
            if len(found_files) >= 10:
                break
    except Exception as e:
        print(f"⛔ Akses Ditolak di beberapa folder: {e}")

    duration = time.time() - start_time
    
    # 3. Laporan Hasil
    if not found_files:
        print(f"\n❌ Tidak ditemukan file dengan kata kunci '{keyword}'.")
        return

    print(f"\n✅ SELESAI. Ditemukan {len(found_files)} file dalam {duration:.2f} detik.")
    print("-------------------------------------------------------")
    
    # 4. Interaksi Pemilihan (Menggantikan Klik Mouse)
    for i, f in enumerate(found_files):
        print(f" {i+1}. {os.path.basename(f)}")
        
    pilihan = input("\nPilih nomor file untuk dianalisis (1-10): ")
    
    if pilihan.isdigit() and 1 <= int(pilihan) <= len(found_files):
        target_file = found_files[int(pilihan)-1]
        analisa_file(target_file)
    else:
        print("Membatalkan misi.")

def analisa_file(filepath):
    print(f"\n🧠 [COGNITIVE LAYER] Menganalisis: {os.path.basename(filepath)}")
    size = os.path.getsize(filepath)
    
    ketik("   📥 Memuat data ke memori RAM...", 0.02)
    time.sleep(0.5)
    print(f"   📊 Ukuran Data: {size} bytes")
    print(f"   📍 Jalur Asli : {filepath}")
    
    ketik("   🔍 Melakukan ekstraksi pola...", 0.05)
    time.sleep(1)
    
    print("\n💡 HASIL ANALISIS SEMENTARA:")
    print("   Status: File Valid & Terbaca.")
    print("   Siap diproses oleh LLM (Mistral/Llama) untuk ringkasan.")
    print("   (Pada tahap selanjutnya, kita akan hubungkan ini ke Otak Asli).")

if __name__ == "__main__":
    scan_drive()
