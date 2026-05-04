
# STUDI KASUS 1


## Automation Test (Playwright - Python)
## Booking Venue

### Overview

Automation testing menggunakan Playwright untuk menguji flow utama pada website ayo.co.id, khususnya:
* Booking flow (basic navigation)
* Validasi elemen UI utama


## Prerequisites
```
Python 3.8+ 
pip
```

## Installation

```playwright install```

## Auth State (auth.json)

File auth.json digunakan untuk menyimpan session login agar tidak perlu login berulang kali.

## Run Test

1. Persiapan Folder
Pastikan dua file utama berada dalam satu folder yang sama:
* ayo_booking.py (Script hasil rekaman/coding)
* auth.json (File sesi login yang sudah dibuat sebelumnya)
2. Membuka Terminal<br>a. Buka aplikasi Terminal atau dari folder klik kanan klik New Terminal at folder<br>
b. Konfirmasi keberadaan file<br>
Pastikan ayo_booking.py dan auth.json muncul di daftar.

3. Eksekusi Script<br>
Jalankan perintah berikut untuk memulai tes:<br>
`python ayo_booking.py` 
atau
`python3 ayo_booking.py`

4. Observasi Jalannya Tes<br>
Saat perintah dijalankan, sistem akan melakukan hal berikut secara otomatis:<br>
* Membuka Browser: Browser Chromium akan muncul.
* Login Otomatis: Menggunakan sesi dari auth.json.
* Aksi UI: Memilih memilih item booking dan menekan tombol selanjutnya sampai halaman pembayaran
* Validasi: Mengecek apakah harga yang muncul sesuai dengan item yang dipilih dan berhasil melakukan pemesanan dengan metode pembayaran yang sesuai


# STUDI KASUS 2

Pengguna melakukan peninjauan pada website dan aplikasi Ayo Indonesia dengan perangkat:
* Browser Safari for website ayo.co.id
* Mobile App for iPhone
(iPhone 11, version 6.7.0)

Hasil temuan dapat dilihat pada link berikut : 
https://docs.google.com/spreadsheets/d/12wv6WZdgONX3LciIJFhSltVxQkKYIEYpnQKRgOK4GYA/edit?usp=sharing


## Strategi Testing yang Disarankan

Gabungkan pendekatan berikut:

### 1. Risk-Based Testing


* Auth
* Payment
* API stability

### 2. End-to-End Testing

Flow utama:
Register → Login → Booking → Payment

### 3. Exploratory Testing

Cocok untuk UX issues dan Navigation inconsistencies

### 4. Automation Candidate

* Login flow
* Regression critical path
* API validation

