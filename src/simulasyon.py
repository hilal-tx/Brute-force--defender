import blake3
import os
import time

sozluk = ["123456", "admin", "qwerty", "password", "gizlisifre123", "iloveyou"]
hedef_parola = "gizlisifre123"

print("="*50)
print("🛡️ BRUTE-FORCE DEFENDER SİMÜLASYONU 🛡️")
print("="*50)

# DURUM 1: TUZSUZ
print("\n[ Senaryo 1: Tuzlama Yapılmayan Güvensiz Sistem ]")
tuzsuz_hash = blake3.blake3(hedef_parola.encode()).hexdigest()
print(f"Veritabanında Tutulan Hash: {tuzsuz_hash}")

print("\nHacker saldırıya başlıyor...")
baslangic_zamani = time.time()

for kelime in sozluk:
    deneme_hash = blake3.blake3(kelime.encode()).hexdigest()
    if deneme_hash == tuzsuz_hash:
        gecen_sure = time.time() - baslangic_zamani
        print(f"🚨 TEHLİKE! Şifre kırıldı: '{kelime}' (Süre: {gecen_sure:.5f} saniye)")
        break

# DURUM 2: TUZLU
print("\n" + "-"*50)
print("\n[ Senaryo 2: Tuzlama Aktif - Güvenli Sistem ]")
rastgele_tuz = os.urandom(16).hex()
tuzlu_hash = blake3.blake3((rastgele_tuz + hedef_parola).encode()).hexdigest()

print(f"Veritabanında Tutulan Tuz: {rastgele_tuz}")
print(f"Yeni Hash: {tuzlu_hash}")

print("\nHacker tekrar deniyor...")
kirildi_mi = False

for kelime in sozluk:
    deneme_hash_hacker = blake3.blake3(kelime.encode()).hexdigest()
    if deneme_hash_hacker == tuzlu_hash:
        print("Şifre kırıldı!")
        kirildi_mi = True
        break

if not kirildi_mi:
    print("✅ GÜVENLİ! Hacker'ın saldırısı boşa düştü.")
    
print("\n[!] Sonuç: Tuzlama işlemi zafiyeti başarıyla engellemiştir.\n")
