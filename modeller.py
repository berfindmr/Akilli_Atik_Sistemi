import sqlite3

class VeritabaniSistemi:
    """Veritabanı bağlantı ve güncelleme işlemlerini yöneten sınıf."""
    
    @staticmethod
    def baglan():
        return sqlite3.connect("atik_sistemi.db")

    @classmethod
    def hazirla(cls):
        """Program ilk açıldığında tabloyu ve varsayılan kullanıcıları oluşturur."""
        conn = cls.baglan()
        cursor = conn.cursor()
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS kullanicilar (
                ad TEXT PRIMARY KEY,
                toplam_kg REAL DEFAULT 0
            )
        """)
        varsayilan_isimler = ["Berfin", "Mihra", "Gülsüm", "Fatih"]
        for isim in varsayilan_isimler:
            cursor.execute("INSERT OR IGNORE INTO kullanicilar (ad, toplam_kg) VALUES (?, ?)", (isim, 0))
        
        conn.commit()
        conn.close()

    @classmethod
    def veri_guncelle(cls, ad, eklenen_kg):
        """Kullanıcının toplam kilosunu veritabanında günceller."""
        conn = cls.baglan()
        cursor = conn.cursor()
        cursor.execute("UPDATE kullanicilar SET toplam_kg = toplam_kg + ? WHERE ad = ?", (eklenen_kg, ad))
        conn.commit()
        conn.close()

    @classmethod
    def tum_verileri_cek(cls):
        """Tüm kullanıcı verilerini arayüze aktarmak için çeker."""
        conn = cls.baglan()
        cursor = conn.cursor()
        cursor.execute("SELECT ad, toplam_kg FROM kullanicilar")
        veriler = cursor.fetchall()
        conn.close()
        return veriler

    @classmethod
    def yeni_kullanici_ekle(cls, ad):
        """Sisteme dinamik olarak yeni bir kullanıcı kaydeder."""
        try:
            conn = cls.baglan()
            cursor = conn.cursor()
            cursor.execute("INSERT INTO kullanicilar (ad, toplam_kg) VALUES (?, ?)", (ad, 0))
            conn.commit()
            conn.close()
            return True
        except sqlite3.IntegrityError:
            return False


class Atik:
    def __init__(self, miktar):
        self.__miktar = miktar 

    def get_miktar(self): 
        return self.__miktar

class KagitAtik(Atik): 
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
        self.__toplam_kg = toplam_kg # Kapsülleme

   
    def atik_ekle(self, kg):
        """Kullanıcıya atık ekler ve veritabanını günceller."""
        if kg > 0: 
            self.__toplam_kg += kg
            
            VeritabaniSistemi.veri_guncelle(self.ad, kg) 

    def get_istatistik(self):
        """Kullanıcının kilosuna göre ünvanını belirler (Hocanın en beğendiği yapı)."""
        kg = self.__toplam_kg 
        
        if kg == 0:
            unvan = "Doğa Gönüllüsü"
        elif 0 < kg <= 50:
            unvan = "Yeşil Filiz"
        elif 50 < kg <= 150:
            unvan = "Geri Dönüşüm Elçisi"
        elif 150 < kg <= 300:
            unvan = "Çevre Koruyucu"
        elif 300 < kg <= 600:
            unvan = "Eko-Savaşçı"
        else:
            unvan = "Doğa Kahramanı"
            
        return kg, unvan