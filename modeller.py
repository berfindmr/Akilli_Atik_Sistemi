import sqlite3

# --- VERİTABANI İŞLEMLERİ ---
def veritabani_hazirla():
    conn = sqlite3.connect("atik_sistemi.db")
    cursor = conn.cursor()
    # Program her açıldığında tablo yoksa oluşturur
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS kullanicilar (
            ad TEXT PRIMARY KEY,
            toplam_kg REAL DEFAULT 0
        )
    """)
    # Başlangıç kullanıcılarını ekle (yoksa)
    varsayilan_isimler = ["Berfin", "Mihra", "Gülsüm", "Fatih"]
    for isim in varsayilan_isimler:
        cursor.execute("INSERT OR IGNORE INTO kullanicilar (ad, toplam_kg) VALUES (?, ?)", (isim, 0))
    
    conn.commit()
    conn.close()

def veri_guncelle(ad, yeni_kg):
    conn = sqlite3.connect("atik_sistemi.db")
    cursor = conn.cursor()
    cursor.execute("UPDATE kullanicilar SET toplam_kg = toplam_kg + ? WHERE ad = ?", (yeni_kg, ad))
    conn.commit()
    conn.close()

def tum_verileri_cek():
    conn = sqlite3.connect("atik_sistemi.db")
    cursor = conn.cursor()
    cursor.execute("SELECT ad, toplam_kg FROM kullanicilar")
    veriler = cursor.fetchall()
    conn.close()
    return veriler

# --- SINIF YAPILARI (OOP) ---
class Atik:
    def __init__(self, miktar):
        self.__miktar = miktar # Kapsülleme

    def get_miktar(self):
        return self.__miktar

class KagitAtik(Atik): # Kalıtım
    def hesapla(self):
        return f"{(self.get_miktar() / 1000) * 17:.2f} adet ağaç kurtarıldı."

class PlastikAtik(Atik):
    def hesapla(self):
        return f"{(self.get_miktar() / 1000) * 5774:.2f} kWh enerji tasarrufu sağlandı."

class MetalAtik(Atik):
    def hesapla(self):
        return f"{(self.get_miktar() / 1000) * 1.1:.2f} ton hammadde tasarrufu sağlandı."

class Kullanici:
    def __init__(self, ad, toplam_kg=0):
        self.ad = ad
        self.__toplam_kg = toplam_kg

    def atik_ekle(self, kg):
        if kg > 0: 
            self.__toplam_kg += kg
            veri_guncelle(self.ad, kg) # Veritabanına kaydet

    def get_istatistik(self):
        kg = self.__toplam_kg
        if kg == 0: unvan = "Doğa Gönüllüsü"
        elif kg <= 30: unvan = "Yeşil Filiz"
        elif kg <= 100: unvan = "Geri Dönüşüm Elçisi"
        elif kg <= 250: unvan = "Çevre Koruyucu"
        elif kg <= 500: unvan = "Eko-Savaşçı"
        else: unvan = "Doğa Kahramanı"
        return kg, unvan