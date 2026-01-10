import cv2
import os
import sys
import time
import pandas as pd
import mediapipe as mp

# TEKNIK BOOTSTRAP: Memaksa akses ke modul internal
try:
    # Cara 1: Standar
    mp_hands = mp.solutions.hands
    mp_drawing = mp.solutions.drawing_utils
except AttributeError:
    # Cara 2: Jika Cara 1 Gagal (Untuk masalah AttributeError Anda)
    import mediapipe.python.solutions.hands as mp_hands
    import mediapipe.python.solutions.drawing_utils as mp_drawing

# Inisialisasi
hands = mp_hands.Hands(
    static_image_mode=False,
    max_num_hands=1,
    min_detection_confidence=0.7,
    min_tracking_confidence=0.7
)

def analisis_data(file):
    if os.path.exists(file):
        print(f"\n✨ [MEE AI] Menganalisis: {file}...")
        try:
            df = pd.read_excel(file)
            print(f"📊 Hasil: Terdeteksi {len(df)} baris data.")
        except Exception as e:
            print(f"❌ Gagal: {e}")
    else:
        print(f"\n⚠️ File 'data.xlsx' tidak ditemukan di folder ini.")

cap = cv2.VideoCapture(0)
print("\n--- MEE AI: SISTEM VISI AKTIF ---")

while cap.isOpened():
    success, image = cap.read()
    if not success: break

    image = cv2.flip(image, 1)
    results = hands.process(cv2.cvtColor(image, cv2.COLOR_BGR2RGB))

    if results.multi_hand_landmarks:
        for hand_landmarks in results.multi_hand_landmarks:
            mp_drawing.draw_landmarks(image, hand_landmarks, mp_hands.HAND_CONNECTIONS)
            
            # Deteksi Pinch
            thumb = hand_landmarks.landmark[4]
            index = hand_landmarks.landmark[8]
            dist = ((thumb.x - index.x)**2 + (thumb.y - index.y)**2)**0.5
            
            if dist < 0.05:
                cv2.putText(image, "ACTION: ANALYZING", (50, 50), 1, 2, (0, 255, 0), 2)
                analisis_data("data.xlsx")
                time.sleep(1)

    cv2.imshow('Mee AI - Vision Layer', image)
    if cv2.waitKey(1) & 0xFF == 27: break

cap.release()
cv2.destroyAllWindows()