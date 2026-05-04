import re
from playwright.sync_api import Playwright, sync_playwright, expect


def run(playwright: Playwright) -> None:
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context(storage_state="auth.json")
    page = context.new_page()
    page.goto("https://ayo.co.id/")
    #Cart=page.get_by_role("link", name="1").click()
    #DeleteCart=page.get_by_role("img", name="Trash icon").click()
    page.get_by_role("link", name="Sewa Lapangan").click()
    page.get_by_placeholder("Cari nama venue").click()
    # Pilih salah satu venue, dalam case ini bestindo
    page.get_by_placeholder("Cari nama venue").fill("bestindo")
    page.get_by_role("button", name="Cari venue").click()
    page.get_by_role("link", name="Bestindo Sport Center Venue").click()
    page.get_by_role("button", name="Cek Ketersediaan").click()
    # Contoh memilih slot waktu paling awal di Bestindo Sport Center
    page.locator(".field-slot-item").first.click()
    page.get_by_label("Jadwal Dipilih").get_by_text("Rp1.500.000").click()
    page.get_by_role("button", name="Selanjutnya").click()
    page.get_by_role("button", name="Lanjutkan ke Pembayaran").click()
    page.get_by_role("button", name="Ya, Lanjutkan").click()
    page.get_by_role("button", name="Transfer Virtual Account ").click()
    page.locator(".payment-method-lists > div:nth-child(8) > .form-check-label > .payment-method-item > .payment-method-fee-charge > .form-check").click()
    page.get_by_role("button", name="Lakukan Pembayaran").click()
    page.get_by_role("button", name="Ya, Lanjutkan").click()
    page.get_by_role("img", name="Qrcode QRIS").click()
   
    # ---------------------
    context.close()
    browser.close()


with sync_playwright() as playwright:
    run(playwright)
