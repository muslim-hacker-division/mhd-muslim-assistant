# 🛡️ MHD-Muslim-Assistant
<p align="center">
  <img src="https://img.shields.io/badge/Status-ONLINE-brightgreen?style=for-the-badge">
  <img src="https://img.shields.io/badge/Division-Muslim%20Hacker-green?style=for-the-badge">
  <img src="https://img.shields.io/badge/Optimized-Low--Spec%20Hardware-blue?style=for-the-badge">
</p>

---

### **"Sesungguhnya shalat itu adalah fardhu yang ditentukan waktunya atas orang-orang yang beriman." (QS. An-Nisa: 103)**

Sebuah asisten terminal (CLI) super ringan yang dirancang khusus untuk kaum Muslim yang sering bekerja di depan layar terminal Linux atau Termux. Dibangun dengan fokus pada efisiensi penggunaan RAM untuk perangkat spesifikasi rendah.

## ✨ Fitur Utama
* 🟢 **Jadwal Sholat Real-Time:** Mengambil data otomatis via API (Default: Surabaya).
* 🟢 **Tactical ASCII UI:** Tampilan visual gahar khas *Muslim Hacker Division*.
* 🟢 **Low Resource:** Sangat bersahabat dengan laptop RAM terbatas (1.4 GiB - 4 GiB).
* 🟢 **Cross-Platform:** Lancar dijalankan di Linux (Ubuntu, Debian, Linux Lite) maupun Android (Termux).

## 🚀 Cara Menjalankan
Pastikan Python sudah terinstall, lalu jalankan perintah berikut:

```bash
# Clone repository
git clone [https://github.com/muslim-hacker-division/mhd-muslim-assistant.git](https://github.com/muslim-hacker-division/mhd-muslim-assistant.git)

# Masuk ke direktori
cd mhd-muslim-assistant

# Install library pendukung
pip install rich requests

# Jalankan alat
python3 mhd_assistant.py
