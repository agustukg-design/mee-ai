import cv2
import os
import mediapipe as mp
import numpy as np

# Konfigurasi Drive
DRIVES = ['C:\\Users\\acer\\Downloads', 'E:\\'] # Fokus ke drive utama dulu agar rapi

# Inisialisasi Mediapipe
mp_hands = mp.solutions.hands
mp_drawing = mp.solutions.drawing_utils
hands = mp_hands.Hands(min_detection_confidence=0.7, min_tracking_confidence=0.7)

def get_drive_data():
    all_files = []
    for drive in DRIVES:
        if os.path.exists(drive):
            try:
                # Ambil 3 file teratas dari setiap drive agar layar tidak penuh
                files = os.listdir(drive)[:3]
                all_files.extend([f"{drive[:2]} > {f[:15]}..." for f in files])
            except: pass
    return all_files

cap = cv2.VideoCapture(0)
display_data = []
show_hologram = False

print("\n--- MEE AI: HOLOGRAPHIC INTERFACE STARTING ---")

while cap.isOpened():
    success, frame = cap.read()
    if not success: break

    frame = cv2.flip(frame, 1)
    h, w, c = frame.shape
    img_rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    results = hands.process(img_rgb)

    # UI Statis (Header)
    cv2.rectangle(frame, (0,0), (w, 50), (20, 20, 20), -1)
    cv2.putText(frame, "MEE OS | HOLOGRAPHIC MODE", (20, 35), 1, 1.5, (0, 255, 255), 2)

    if results.multi_hand_landmarks:
        for hand_landmarks in results.multi_hand_landmarks:
            # Gambar titik tangan dengan warna neon
            mp_drawing.draw_landmarks(frame, hand_landmarks, mp_hands.HAND_CONNECTIONS,
                                     mp_drawing.DrawingSpec(color=(0,255,0), thickness=2, circle_radius=2))
            
            # Koordinat telunjuk (Landmark 8) untuk posisi teks melayang
            index_finger = hand_landmarks.landmark[8]
            cx, cy = int(index_finger.x * w), int(index_finger.y * h)
            
            # Deteksi Pinch (Jempol & Telunjuk)
            thumb = hand_landmarks.landmark[4]
            dist = ((thumb.x - index_finger.x)**2 + (thumb.y - index_finger.y)**2)**0.5
            
            if dist < 0.04:
                show_hologram = True
                if not display_data:
                    display_data = get_drive_data()
                # Efek visual saat menekan
                cv2.circle(frame, (cx, cy), 15, (0, 255, 0), -1)
            else:
                show_hologram = False
                display_data = []

            # TAMPILKAN DATA MELAYANG
            if show_hologram:
                # Gambar kotak background transparan untuk data
                overlay = frame.copy()
                cv2.rectangle(overlay, (cx + 20, cy - 100), (cx + 300, cy + 20), (50, 50, 50), -1)
                cv2.addWeighted(overlay, 0.6, frame, 0.4, 0, frame)
                
                # Tampilkan daftar file
                for i, text in enumerate(display_data):
                    cv2.putText(frame, text, (cx + 30, cy - 70 + (i*30)), 
                                cv2.FONT_HERSHEY_SIMPLEX, 0.6, (255, 255, 0), 2)
                
                cv2.putText(frame, "STATUS: SCANNING DRIVE", (cx + 30, cy + 10), 
                            cv2.FONT_HERSHEY_SIMPLEX, 0.4, (0, 255, 0), 1)

    cv2.imshow('Mee AI - Hologram Engine', frame)
    if cv2.waitKey(1) & 0xFF == 27: break

cap.release()
cv2.destroyAllWindows()