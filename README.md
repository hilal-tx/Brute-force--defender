# Brute-force--defender
BLAKE3 kullanarak hash kırma ve salting (tuzlama) simülasyonu
# 🛡️ Brute-Force Defender & Cryptographic Salting Simulator

🇹🇷 **Türkçe** | 🇬🇧 **English**

## Proje Özeti
Bu proje, modern siber güvenlik mimarilerinde parolaların veritabanında "düz (tuzsuz) hash" olarak tutulmasının yarattığı kritik zafiyetleri ve bu zafiyetlerin "Kriptografik Tuzlama (Salting)" yöntemiyle nasıl proaktif olarak engellendiğini kanıtlayan Python tabanlı bir simülasyon motorudur. 

Yüksek performanslı **BLAKE3** algoritması kullanılarak, donanım hızlandırmalı sözlük (dictionary) saldırılarının deterministik hash'leri saniyeler içinde nasıl kırabildiği gösterilmiş; ardından `os.urandom` tabanlı 16-byte'lık dinamik tuzlama ile bu saldırı vektörü tamamen etkisiz hale getirilmiştir.

---

## 📌 Execution Sandbox Roadmap

**ENGLISH BLUEPRINT**
1. Build core mathematically sound BLAKE3 hashing module.
2. Implement dictionary attack simulator with execution timer.
3. Design and integrate dynamic cryptographic salting defense.

**TURKISH BLUEPRINT**
1. Çekirdek BLAKE3 özetleme (hashing) modülünün inşası.
2. Süre ölçümlü sözlük saldırısı (dictionary attack) simülatörünün kodlanması.
3. Dinamik kriptografik tuzlama (salting) savunmasının tasarlanıp entegre edilmesi.
