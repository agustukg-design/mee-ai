import os

DATA_DIR = "data_ocean"

print("🧠 MEE-AI Cognitive Layer aktif")
print("Membaca lautan data...\n")

for fname in os.listdir(DATA_DIR):
    path = os.path.join(DATA_DIR, fname)
    print(f"📄 Membaca: {fname}")
    with open(path, "r") as f:
        content = f.read()
        print(content)
        print("-" * 40)

print("\n🔎 Analisis konseptual:")
print("→ Dokumen terkait proyek infrastruktur")
print("→ Terdapat hubungan invoice dan kontrak")
print("→ Rekomendasi: siapkan ringkasan eksekutif")

