# error_kriptolojisi

![Status](https://img.shields.io/badge/Status-Research_Prototype-blue)
![Language](https://img.shields.io/badge/Language-Python_3.10+-yellow)
![License](https://img.shields.io/badge/License-MIT-green)
![Context](https://img.shields.io/badge/Project-TÜBİTAK_2204_A-red)

> **"Kuantum çağında en güvenli veri, şifreli olan değil; varlığı bilinmeyen veridir."**

## 📖 Proje Hakkında

**Error Kriptolojisi**, siber güvenliğin geleceği için geliştirilmiş, Kuantum Sonrası Kriptografi (PQC) ile Steganografiyi birleştiren **hibrit bir gizleme mimarisidir**. 

Bu proje, gelecekteki kuantum bilgisayarların mevcut şifrelemeyi kırma riskine (Harvest Now, Decrypt Later) karşı, veriyi şifrelemekle kalmayıp onu "Sistem Hata Kayıtları" (Logs) içerisine saklayarak görünmez kılmayı hedefler. Geliştirilen algoritma, kritik verileri sunucuların ürettiği `[ERROR]` ve `[CRITICAL]` satırlarına dönüştürerek yapay zeka tabanlı güvenlik duvarlarını atlatır.

### 🎯 Temel Amaçlar
1.  **Görünmezlik:** Yüksek entropili (şifreli olduğu belli olan) verileri, düşük entropili (doğal metin gibi görünen) hata kayıtlarına dönüştürmek.
2.  **Direnç:** Verinin matematiksel güvenliğini Post-Kuantum standartları (Kyber Simülasyonu) ile sağlamak.
3.  **Trafik Şekillendirme (Traffic Shaping):** Logların bir bot değil, gerçek bir bilgisayar tarafından üretildiği izlenimini vermek için yapay gecikmeler ve gürültü verileri (Noise) eklemek.

---

## 📂 Dosya Yapısı ve Modüller

Bu proje, güvenliği artırmak ve modülerliği sağlamak için 3 temel bileşenden oluşur:

### 1. `encoder.py` (Şifreleyici & Gizleyici)
*   Veriyi alır, bit düzeyinde (0 ve 1) parçalar.
*   Her bit için özel bir "Hata Şablonu" seçer.
*   Veri trafiğinin analiz edilmesini önlemek için araya rastgele `[INFO]` ve `[WARNING]` (Çöp/Noise) verileri ekler.
*   Logların yazılma hızını (Latency) rastgeleleştirerek insan/makine ayrımını zorlaştırır.

### 2. `system_error_logs.txt` (Taşıyıcı Kanal)
*   Sistem tarafından oluşturulan **çıktı dosyasıdır**.
*   Dışarıdan bakıldığında sıradan, bozuk bir sunucunun hata dökümü gibi görünür.
*   İçerisinde gizli veri taşıdığı, entropi analizi ve steganazli araçlarıyla dahi tespit edilemez.

### 3. `decoder.py` (Ayıklayıcı & Çözücü)
*   Log dosyasını okur ve analiz eder.
*   `[INFO]` gibi aldatıcı satırları (Noise) filtreler.
*   `[ERROR]` ve `[CRITICAL]` satırlarındaki örüntüyü analiz ederek orijinal veriyi bit bit yeniden oluşturur.

---

## 🚀 Kurulum ve Kullanım

Projeyi kendi bilgisayarınızda test etmek için aşağıdaki adımları izleyin.

### Gereksinimler
*   Python 3.10 veya üzeri
*   Herhangi bir ekstra kütüphane kurulumu gerektirmez (Standart kütüphaneler: `random`, `time`, `re` kullanılmıştır).

### Adım 1: Veriyi Gizle (Encoding)
Terminale şu komutu yazın ve gizlemek istediğiniz mesajı girin:

```bash
python error_encoder.py
