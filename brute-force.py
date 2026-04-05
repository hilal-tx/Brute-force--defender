import blake3
import os
import time

def simulasyon_baslat():
    hedef_parola = "gizlisifre123"
    sozluk = ["123456", "password", "deneme", "admin", "gizlisifre123", "qwerty"]
    
    print("--- BRUTE-FORCE DEFENDER SİMÜLASYONU ---")
    
    # SENARYO 1: TUZLAMA YAPILMAYAN SİSTEM
    print("\n[ Senaryo 1: Tuzlama Yapılmayan Güvensiz Sistem ]")
    tuzsuz_hash = blake3.blake3(hedef_parola.encode()).hexdigest()
    print(f"Veritabanında Tutulan Hash: {tuzsuz_hash}")
    
    print("Hacker saldırıya başlıyor...")
    baslangic = time.time()
    for kelime in sozluk:
        deneme_hash = blake3.blake3(kelime.encode()).hexdigest()
        if deneme_hash == tuzsuz_hash:
            bitis = time.time()
            print(f"🚨 TEHLİKE! Şifre kırıldı: '{kelime}' (Süre: {bitis - baslangic:.5f} saniye)")
            break

    # SENARYO 2: TUZLAMA AKTİF GÜVENLİ SİSTEM
    print("\n" + "-"*50)
    print("[ Senaryo 2: Tuzlama Aktif - Güvenli Sistem ]")
    
    # 16-byte rastgele tuz (salt) üretimi
    rastgele_tuz = os.urandom(16).hex()
    # Tuz + Parola birleştirilerek hashlenir
    tuzlu_hash = blake3.blake3((rastgele_tuz + hedef_parola).encode()).hexdigest()
    
    print(f"Veritabanında Tutulan Tuz: {rastgele_tuz}")
    print(f"Yeni Hash: {tuzlu_hash}")
    
    print("\nHacker tekrar deniyor...")
    kirdi_mi = False
    for kelime in sozluk:
        # Hacker tuzlama yapıldığını bilmediği için sadece kelimeleri hashler
        deneme_hash_hacker = blake3.blake3(kelime.encode()).hexdigest()
        if deneme_hash_hacker == tuzlu_hash:
            kirdi_mi = True
            break
            
    if not kirdi_mi:
        print("✅ GÜVENLİ! Hacker'ın saldırısı boşa düştü.")
        print("[!] Sonuç: Tuzlama işlemi zafiyeti başarıyla engellemiştir.")

if __name__ == "__main__":
    simulasyon_baslat()
