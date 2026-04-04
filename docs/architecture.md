# Proje Mimarisi ve QLine Raporu

### Yönetici Özeti
Python 3 kullanılarak tasarlanmış, siber güvenlik eğitimlerinde temel kriptografi zafiyetlerini uygulamalı olarak göstermeyi hedefleyen bir savunma simülasyonudur. Proje, endüstri standardı olan yüksek performanslı BLAKE3 algoritmasını temel alır. Sistem, deterministik (tuzsuz) hashlerin Brute-Force/Dictionary saldırılarına karşı ne kadar zayıf olduğunu süre bazlı ölçümlerle kanıtlarken; kriptografik tuzlama (salting) entegrasyonu ile "Rainbow Table" saldırılarının matematiksel olarak nasıl boşa düşürüldüğünü ispatlar.

### 1. Proje Mimarisi ve Kurulumu
Sistem tamamen Python 3 üzerinde, dış bağımlılıkların izole edildiği bir Virtual Environment (venv) içinde çalışacak şekilde tasarlanmıştır. Çekirdek kriptografi kütüphanesi olarak MD5 veya SHA-256 yerine, modern ve hız odaklı `blake3` kütüphanesi tercih edilmiştir. Mimari veri akışı; "Zafiyetli Sistem Kurulumu -> Saldırı Vektörü Çalıştırma -> Güvenli Mimari İnşası -> Başarısız Saldırı İspatı" şeklinde senkron bir akışla ilerler.

### 2. Çekirdek Analiz Motoru
Simülasyonun çekirdeği iki ana iş parçacığından oluşur. İlk motor, hedef parolayı doğrudan BLAKE3 ile şifreler ve `time.time()` ile nanosaniye hassasiyetinde bir saldırı döngüsü başlatır. İkinci motor ise `os.urandom(16).hex()` fonksiyonunu kullanarak işletim sistemi çekirdeği seviyesinde rastgele entropi üretir (Salt). Bu dinamik entropi, parolaya "pre-pend" (ön ek) yapılarak hashlenir ve sistemin veri bütünlüğü dinamik olarak korunur.

### 3. İnovasyon ve Farklılaşma
Bu projenin en büyük farkı, zafiyeti sadece teorik olarak anlatmak yerine, canlı bir "Threat Modeling" (Tehdit Modelleme) senaryosu içinde kod bazında yarıştırmasıdır. BLAKE3 gibi saniyede gigabaytlarca veri işleyebilen bir algoritmanın bile, "Tuzlama" yapılmadığı takdirde anında kırılabileceğini göstermesi, kriptografide "algoritma hızı" ile "sistem güvenliği" arasındaki farkı üniversite seviyesinde vurgulayan yenilikçi bir yaklaşımdır.
