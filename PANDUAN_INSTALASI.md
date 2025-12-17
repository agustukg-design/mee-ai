#!/bin/bash
echo "--- MEMULAI PROSES HARDENING MEE AI ---"

# Mengaktifkan proteksi sistem pada unit service
sudo sed -i '/\[Service\]/a ProtectSystem=full\nProtectHome=read-only\nPrivateTmp=true' /etc/systemd/system/mee-ai.service

# Melakukan reload dan restart untuk menerapkan keamanan baru
sudo systemctl daemon-reload
sudo systemctl restart mee-ai.service

echo "--- STATUS KEAMANAN SEKARANG: TERKUNCI (HARDENED) ---"
sudo systemctl status mee-ai.service
