
# STUDI KASUS 1
Dari studi kasus yang diberikan permasalahan yang ada menunjukkan adanya gap di level arsitektur sistem yaitu data integrity + concurrency control. Perlu dilakukan pengecekan lebih lanjut :
* Harga selalu divalidasi dan diambil dari sumber yang benar (database & server-side validation)
* Tidak ada dua booking pada schedule yang sama (constraint & concurrency control)
* Semua proses booking dilakukan secara aman dan konsisten

Berikut beberapa scenario dan _insight_ testing yang dapat dijalankan : 

### Price Validation (Data Integrity Testing)
> Untuk memastikan data booking match dengan master price / schedule dan memastikan backend trust boundary terhadap input dari frontend

| No  | Test Case | Expected Result  |
| :---|:--------- | :--------------- |
| 1 | (Positive) Verify to Book a schedule with valid price  |  Successfully booked a schedule |
| 2 | (Positive) Compare booking price with master/schedule price   | Booking price match with master/schedule price|
| 3 | (Positive) Make a  booking with multiple schedule | Accurate total price is as booked |
| 4 | (Negative) Request to booking with different schedule price (API Contract Testing) |  System flag error, override the price in the backend from the database, not from the request|
| 5 | (Negative) Bookings when the schedule price changes during the checkout process | Booking rejected, system flag error : The price has been updated, please confirm again |
 

### Double Book Prevention (Concurrency Testing )
> Untuk mendeteksi double booking akibat duplicate request ataupun paralel

| No  | Test Case | Expected Result  |
| :---|:--------- | :--------------- |
| 1 | (Positive) Verify to ensure no overlapping booking exist  | No duplicate or double schedule bookings |
| 2 | (Positive) Booking schedule in sequence | Successfully booked |
| 3 | (Negative) Send request booking multiple times (double submission) | If there are two concurrent requests, one must succeed and one must fail (race condition) | 
| 4 | (Negative) Booking with 2 users for the same schedule at the same time (parallel requests) | Only one succeeded; the others failed or conflict  |
| 5 | (Negative) Bookings from multiple browser tabs for the same schedule | The first tab succeeded, then the second tab failed (the schedule is already taken) |
| 6 | (Negative) Retry requests after a timeout (idempotency issue) | Doesn't cause double bookings |


### Booking Schedule Consistency (Database Integrity )
> Untuk mendeteksi double booking akibat duplicate request ataupun paralel

| No  | Test Case | Expected Result  |
| :---|:--------- | :--------------- |
| 1 | (Positive) Booking with valid schedule | Successful bookings |
| 2 | (Negative) Booking schedule that has already been booked | Schedule read-only/inactive and can't be book|
| 3 | (Negative) Schedule Taken During Checkout | API returns 409 Conflict with error message: Schedule already booked, user is asked to reselect|



### Additinal test coverage
1. End to End Testing
> Untuk memastikan flow user berjalan dengan lancar dan konsisten dari awal sampai akhir,

2. Edge Case / Exploratory Testing
> Untuk menyelami lebih luas dan menemukan bug yang tidak tercover oleh test lainnya
> System tahan terhadap behavior user yang tidak ideal

3. API Testing (Security Layer)
> Untuk memastikan valid request, invalid payloads, dan jika ada manipulation data menampilkan respon sesuai yang diharapkan 

4. Performance & Load Testing
> Untuk melihat bagaimana sistem tetap stabil saat load tinggi
> Booking tetap cepat walaupun banyak user, mengoptimasisasi loading lama, random error maupun gagal/crash tanpa alasan.



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


## Mekanisme atau strategi testing yang disarankan dengan gabungkan pendekatan sebagai berikut.

### 1. Risk-Based Testing

* Auth
* Payment
* API stability

### 2. End-to-End Testing

Flow utama:
Register → Login → Booking → Payment

### 3. Exploratory Testing

Cocok untuk UX issues dan navigation inconsistencies

### 4. Optimasi automation 

* Login flow
* Regression critical path
* API validation

