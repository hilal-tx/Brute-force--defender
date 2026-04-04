# 🛡️ Brute-Force Defender & Cryptographic Salting Simulator
📘 **Ders:** Tersine Mühendislik (Reverse Engineering)  
🎯 **Görev:** Vize Projesi
  Hazırlayan:Hilal Şengül
🇹🇷 **Türkçe** 

## 📖 Proje Özeti
Bu proje, modern siber güvenlik mimarilerinde parolaların veritabanında "düz (tuzsuz) hash" olarak tutulmasının yarattığı kritik zafiyetleri ve bu zafiyetlerin "Kriptografik Tuzlama (Salting)" yöntemiyle nasıl proaktif olarak engellendiğini kanıtlayan Python tabanlı bir simülasyon motorudur. 

Yüksek performanslı **BLAKE3** algoritması kullanılarak, donanım hızlandırmalı sözlük (dictionary) saldırılarının deterministik hash'leri saniyeler içinde nasıl kırabildiği gösterilmiş; ardından `os.urandom` tabanlı 16-byte'lık dinamik tuzlama ile bu saldırı vektörü tamamen etkisiz hale getirilmiştir.

---

## 💻 Çekirdek Kod Mimarisi (Core Implementation)

Zafiyetin ve savunmanın teknik olarak nasıl simüle edildiğine dair çekirdek kod blokları aşağıdadır:

### 1. Zafiyetli Sistem (No Salt)
Eğer parola doğrudan hashlenirse, deterministik yapı nedeniyle sözlükteki kelimelerle anında eşleşir.
```python
# Zafiyetli (Tuzsuz) Hash Üretimi
tuzsuz_hash = blake3.blake3(hedef_parola.encode()).hexdigest()

# Brute-Force / Sözlük Saldırısı Simülasyonu
for kelime in sozluk:
    deneme_hash = blake3.blake3(kelime.encode()).hexdigest()
    if deneme_hash == tuzsuz_hash:
        print(f"🚨 TEHLİKE! Şifre kırıldı: '{kelime}'")
        break
# 16-byte Dinamik Tuz Üretimi ve Güvenli Hashleme
rastgele_tuz = os.urandom(16).hex()
tuzlu_hash = blake3.blake3((rastgele_tuz + hedef_parola).encode()).hexdigest()

# Rainbow Table / Sözlük Saldırısı Başarısız Olur
for kelime in sozluk:
    deneme_hash_hacker = blake3.blake3(kelime.encode()).hexdigest()
    if deneme_hash_hacker == tuzlu_hash:
        # Bu bloğa asla girilemez, sistem güvendedir.
        print("Şifre kırıldı!")
[ Senaryo 1: Tuzlama Yapılmayan Güvensiz Sistem ]
Veritabanında Tutulan Hash: cc58bb92127d8351b3071aa8b78c213cbee9d1efabfe999825cc8f891ca64805
🚨 TEHLİKE! Şifre kırıldı: 'gizlisifre123' (Süre: 0.00006 saniye)

--------------------------------------------------
[ Senaryo 2: Tuzlama Aktif - Güvenli Sistem ]
Veritabanında Tutulan Tuz: 15e005423fcdda2fee2e1607cfa07bcc
Yeni Hash: 6e90a48ade23a0ec2fa00e7bbfed9c7b05de27ed16743b1ce6fff7adddb8361a
✅ GÜVENLİ! Hacker'ın saldırısı boşa düştü.

[!] Sonuç: Tuzlama işlemi zafiyeti başarıyla engellemiştir.
