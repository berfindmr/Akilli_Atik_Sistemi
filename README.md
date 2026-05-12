# 🌍 Akıllı Atık Yönetim Sistemi (Smart Waste Management)

Bu proje, Nesne Tabanlı Programlama (OOP) prensipleri kullanılarak geliştirilmiş, çevre bilincini artırmayı ve atık takibini dijitalleştirmeyi amaçlayan bir masaüstü uygulamasıdır.

## 🚀 Projenin Amacı
Kullanıcıların günlük atık miktarlarını (Kağıt, Plastik, Metal) takip ederek doğaya sağladıkları katkıyı (kurtarılan ağaç, enerji tasarrufu vb.) hesaplamak ve bu verileri kalıcı bir veritabanında saklamaktır.

## 🛠 Kullanılan Teknolojiler
* **Programlama Dili:** Python 3.x
* **Arayüz (GUI):** Tkinter
* **Veritabanı (SQL):** SQLite3
* **Versiyon Kontrol:** Git & GitHub

## 📂 Proje Modülleri ve Amacı
Proje, sürdürülebilirlik ve modülerlik ilkesine uygun olarak 3 ana Python dosyasından oluşmaktadır:
1. **main.py:** Uygulamanın görsel arayüzünü (GUI), kullanıcı etkileşimlerini ve veritabanı ile arayüz arasındaki köprüyü yönetir.
2. **modeller.py:** Projenin "beyni"dir. 
   - **OOP Prensipleri:** `Atik` ve `Kullanici` sınıfları aracılığıyla **Kalıtım (Inheritance)** ve **Kapsülleme (Encapsulation)** uygulanmıştır.
   - **SQL Katmanı:** Veritabanı oluşturma, veri çekme ve güncelleme fonksiyonlarını içerir.
3. **hesaplamalar.py:** Atık türlerine göre bilimsel tasarruf verilerini işleyen mantıksal katmandır.

## 💾 Veritabanı Yapısı
Projede **SQLite** kullanılarak verilerin program kapansa dahi silinmemesi sağlanmıştır. Uygulama ilk kez çalıştırıldığında `atik_sistemi.db` dosyasını otomatik olarak oluşturur ve kullanıcı bazlı toplam atık miktarını güncel tutar.

## 💻 Nasıl Çalıştırılır?
1. Bilgisayarınızda Python'un yüklü olduğundan emin olun.
2. Bu depoyu (repository) indirin veya kopyalayın.
3. Terminal veya komut satırına `python main.py` yazarak uygulamayı başlatın.
