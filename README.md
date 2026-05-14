# 🌍 **Akıllı Atık Yönetim Sistemi (Smart Waste Management)**

Bu proje, **Nesne Tabanlı Programlama (OOP)** prensipleri kullanılarak geliştirilmiş, çevre bilincini artırmayı ve atık takibini dijitalleştirmeyi amaçlayan modüler bir masaüstü uygulamasıdır.

---

## 🚀 **Projenin Amacı**
* Kullanıcıların günlük atık miktarlarını (Kağıt, Plastik, Metal) takip ederek doğaya sağladıkları katkıyı hesaplamak.
* Bu verileri **SQLite** tabanlı kalıcı bir veritabanında güvenli bir şekilde saklamaktır.

🖥 Uygulama Paneli ve Çalışma Mantığı
Uygulama, kullanıcı dostu bir arayüz ile atık girişlerini yönetir ve sonuçları anlık olarak tabloda günceller.


<img width="1890" height="652" alt="image" src="https://github.com/user-attachments/assets/55a5aa99-4bb9-493a-bdfe-9a914fa33d9a" />
<img width="401" height="338" alt="image" src="https://github.com/user-attachments/assets/942fbcd8-4fe0-4110-bcc3-9474370a9b51" />
<img width="350" height="183" alt="image" src="https://github.com/user-attachments/assets/d5e01f6b-0254-4e9a-892c-3cc798e517f9" />



## 🔄 **Sistemin İşleyişi (Logic)**

Uygulamanın çalışma mantığı, modüler yapı prensiplerine uygun olarak şu adımlarla gerçekleşmektedir:

* **1. Kullanıcı Seçimi:** Mevcut çevrecilerden biri seçilir veya sisteme yeni bir kullanıcı kaydı eklenir.
* **2. Atık Girişi:** Geri dönüştürülecek atık türü (Kağıt, Plastik, Metal) seçilerek miktar kg cinsinden girilir.
* **3. Anlık Hesaplama:** Arka planda `hesaplamalar.py` modülü çalışarak doğaya sağlanan katkıyı (ağaç, enerji vb.) hesaplar.
* **4. Ünvan Güncelleme:** Toplam kg miktarına göre kullanıcının ünvanı (Örn: Yeşil Filiz -> Eko-Savaşçı) anlık olarak belirlenir.
* **5. Kalıcı Kayıt:** Tüm bu veriler **SQLite** veritabanına işlenerek güvenli ve kalıcı bir şekilde saklanır.



## 🛠 **Kullanılan Teknolojiler**
* **Programlama Dili:** Python 3.x
* **Arayüz (GUI):** Tkinter
* **Veritabanı (SQL):** SQLite3
* **Versiyon Kontrol:** Git & GitHub

---

## 📂 **Proje Modülleri ve Amacı**
Proje, modülerlik ilkesine uygun olarak 3 ana Python dosyasından oluşmaktadır:

### **1. main.py**
* Uygulamanın görsel gelişimini (GUI) yönetir.
* Kullanıcının etkileşimlerini ve veri tabanı arasındaki köprüyü sağlar.

### **2. modeller.py**
* [cite_start]Projenin "beyni" ve veri yönetim merkezidir.
* [cite_start]**OOP Prensipleri:** `Atik` ve `Kullanici` sınıfları aracılığıyla **Kalıtım (Inheritance)** ve **Kapsülleme (Encapsulation)** uygulanmıştır.
* **SQL Katmanı:** Veritabanı oluşturma, veri çekme ve güncelleme fonksiyonlarını içerir.

### **3. hesaplamalar.py**
* Atık türlerine göre tasarruf sağlayan azaltıcı katmandır.

---

## 💾 **Veritabanı Yapısı**
* Projede **SQLite** kayıtlı verilerin programın kapanması dahi silinmemesi sağlandı.
* Uygulama ilk kez çalıştırıldığında `atik_sistemi.db` otomatik olarak oluşturulur.

---

## 💻 **Nasıl Çalıştırılır?**
1. Bilgisayarınızda Python'un yüklü olduğundan emin olun.
2. Bu depoyu kopyalayın ve terminale `python main.py` yazarak uygulamayı başlatın.

---
**Hazırlayan:** Berfin Demir
**Kurum:** Kastamonu Üniversitesi - Tosya MYO
