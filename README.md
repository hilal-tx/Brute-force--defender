# 🛡️ Brute-Force Defender & Cryptographic Salting Simulator

📘 **Ders:** Tersine Mühendislik (Reverse Engineering)  
🎯 **Görev:** Vize Projesi  
👤 **Hazırlayan:** Hilal Şengül  

🇹🇷 **Türkçe** | 🇬🇧 **English**

---

## 📖 Proje Özeti
Bu proje, modern siber güvenlik mimarilerinde parolaların veritabanında "düz (tuzsuz) hash" olarak tutulmasının yarattığı kritik zafiyetleri ve bu zafiyetlerin **"Kriptografik Tuzlama (Salting)"** yöntemiyle nasıl proaktif olarak engellendiğini kanıtlayan Python tabanlı bir simülasyon motorudur. 

Yüksek performanslı **BLAKE3** algoritması kullanılarak, donanım hızlandırmalı sözlük (dictionary) saldırılarının deterministik hash'leri saniyeler içinde nasıl kırabildiği gösterilmiş; ardından `os.urandom` tabanlı 16-byte'lık dinamik tuzlama ile bu saldırı vektörü tamamen etkisiz hale getirilmiştir.



---

## 💻 Çekirdek Kod Mimarisi (Core Implementation)

Zafiyetin ve savunmanın teknik olarak nasıl simüle edildiğine dair çekirdek mantık aşağıdadır:

### 1. Senaryo: Zafiyetli Sistem (No Salt)
Eğer parola doğrudan hashlenirse, deterministik yapı nedeniyle sözlükteki kelimelerle anında eşleşir.

```python
# Zafiyetli (Tuzsuz) Hash Üretimi
tuzsuz_hash = blake3.blake3(hedef_parola.encode()).hexdigest()

# Saldırı Simülasyonu
for kelime in sozluk:
    if blake3.blake3(kelime.encode()).hexdigest() == tuzsuz_hash:
        print("Şifre Kırıldı!")

🇹🇷 **Türkçe** 

---

## 📖 Proje Özeti
Bu proje, modern siber güvenlik mimarilerinde parolaların veritabanında "düz (tuzsuz) hash" olarak tutulmasının yarattığı kritik zafiyetleri ve bu zafiyetlerin **"Kriptografik Tuzlama (Salting)"** yöntemiyle nasıl proaktif olarak engellendiğini kanıtlayan Python tabanlı bir simülasyon motorudur. 

Yüksek performanslı **BLAKE3** algoritması kullanılarak, donanım hızlandırmalı sözlük (dictionary) saldırılarının deterministik hash'leri saniyeler içinde nasıl kırabildiği gösterilmiş; ardından `os.urandom` tabanlı 16-byte'lık dinamik tuzlama ile bu saldırı vektörü tamamen etkisiz hale getirilmiştir.



---

## 💻 Çekirdek Kod Mimarisi (Core Implementation)

Zafiyetin ve savunmanın teknik olarak nasıl simüle edildiğine dair çekirdek mantık aşağıdadır:

### 1. Senaryo: Zafiyetli Sistem (No Salt)
Eğer parola doğrudan hashlenirse, deterministik yapı nedeniyle sözlükteki kelimelerle anında eşleşir.

```python
# Zafiyetli (Tuzsuz) Hash Üretimi
tuzsuz_hash = blake3.blake3(hedef_parola.encode()).hexdigest()

# Saldırı Simülasyonu
for kelime in sozluk:
    if blake3.blake3(kelime.encode()).hexdigest() == tuzsuz_hash:
        print("Şifre Kırıldı!")
