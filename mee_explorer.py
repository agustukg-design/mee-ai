import cv2
import os
import time
import mediapipe as mp

# Konfigurasi Drive yang akan dijelajahi
# Catatan: Pastikan drive E dan F terpasang di laptop Anda
DRIVES = ['C:\\Users\\acer\\Downloads', 'E:\\', 'F:\\']

# Inisialisasi Mediapipe
mp_hands = mp.solutions.hands
mp_drawing = mp.solutions.drawing_utils
hands = mp_hands.Hands(min_detection_confidence=0.8, min_tracking_confidence=0.8)

def jelajahi_data():
    print("\n🚀 [MEE AI] MEMULAI PEMINDAIAN GLOBAL (C, E, F)...")
    for drive in DRIVES:
        if os.path.exists(drive):
            print(f"--- Folder: {drive} ---")
            try:
                # Mengambil 5 file/folder pertama sebagai contoh data yang "melayang"
                items = os.listdir(drive)[:5]
                for item in items:
                    print(f" 📂 DATA TERDETEKSI: {item}")
            except Exception as e:
                print(f" ⚠️ Akses Drive {drive} Terbatas.")
        else:
            print(f" ❌ Drive {drive} Tidak Terdeteksi.")
    print("✨ PEMINDAIAN SELESAI. DATA SIAP DIOLAH.")

cap = cv2.VideoCapture(0)
print("\n--- MEE AI: SPATIAL EXPLORER AKTIF ---")
print("Gunakan gerakan PINCH (Jempol + Telunjuk) untuk memindai semua drive.")

while cap.isOpened():
    success, image = cap.read()
    if not success: break

    image = cv2.flip(image, 1)
    results = hands.process(cv2.cvtColor(image, cv2.COLOR_BGR2RGB))

    if results.multi_hand_landmarks:
        for hand_landmarks in results.multi_hand_landmarks:
            mp_drawing.draw_landmarks(image, hand_landmarks, mp_hands.HAND_CONNECTIONS)
            
            # Logika Deteksi Pinch
            thumb = hand_landmarks.landmark[4]
            index = hand_landmarks.landmark[8]
            distance = ((thumb.x - index.x)**2 + (thumb.y - index.y)**2)**0.5
            
            if distance < 0.04: # Jika mencubit
                cv2.putText(image, "EXPLORING DRIVES...", (50, 50), 1, 2, (0, 255, 255), 2)
                jelajahi_data()
                time.sleep(2) # Delay agar tidak scanning berkali-kali

    cv2.imshow('Mee AI - Spatial Explorer', image)
    if cv2.waitKey(1) & 0xFF == 27: break # Tekan ESC untuk keluar

cap.release()
cv2.destroyAllWindows()