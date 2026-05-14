# 🌍 **Akıllı Atık Yönetim Sistemi (Smart Waste Management)**

Bu proje, **Nesne Tabanlı Programlama (OOP)** prensipleri kullanılarak geliştirilmiş, çevre bilincini artırmayı ve atık takibini dijitalleştirmeyi amaçlayan modüler bir masaüstü uygulamasıdır.

---

## 🚀 **Projenin Amacı**
* Kullanıcıların günlük atık miktarlarını (Kağıt, Plastik, Metal) takip ederek doğaya sağladıkları katkıyı hesaplamak.
* Bu verileri **SQLite** tabanlı kalıcı bir veritabanında güvenli bir şekilde saklamaktır.



<img width="1890" height="652" alt="image" src="https://github.com/user-attachments/assets/55a5aa99-4bb9-493a-bdfe-9a914fa33d9a" />




## 🛠 **Kullanılan Teknolojiler**
* **Programlama Dili:** Python 3.x
* **Arayüz (GUI):** Tkinter
* **Veritabanı (SQL):** SQLite3
* **Versiyon Kontrol:** Git & GitHub

---

## 📂 **Proje Modülleri ve Amacı**
Proje, modülerlik ilkesine uygun olarak 3 ana Python dosyasından oluşmaktadır:

### **1. main.py**
* Uygulamanın görsel gelişimini (GUI) yönetir. [cite: 31]
* Kullanıcının etkileşimlerini ve veri tabanı arasındaki köprüyü sağlar.

### **2. modeller.py**
* [cite_start]Projenin "beyni" ve veri yönetim merkezidir. [cite: 31]
* [cite_start]**OOP Prensipleri:** `Atik` ve `Kullanici` sınıfları aracılığıyla **Kalıtım (Inheritance)** ve **Kapsülleme (Encapsulation)** uygulanmıştır. [cite: 31]
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
