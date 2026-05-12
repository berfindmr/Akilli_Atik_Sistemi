class Atik:
    def __init__(self, miktar):
        # Kapsülleme: Miktarı dışarıdan doğrudan erişime kapatıyoruz
        self.__miktar = miktar 

    def get_miktar(self):
        return self.__miktar

    def hesapla(self):
        pass

# Kalıtım: Atik sınıfından türetilen alt sınıflar
class KagitAtik(Atik):
    def hesapla(self):
        # 1 ton kağıt yaklaşık 17 ağaç kurtarır
        kurtarilan_agac = (self.get_miktar() / 1000) * 17
        return f"{kurtarilan_agac:.2f} adet ağaç kurtarıldı."

class PlastikAtik(Atik):
    def hesapla(self):
        # 1 ton plastik geri dönüşümü 5774 kWh enerji tasarrufu sağlar
        enerji_tasarrufu = (self.get_miktar() / 1000) * 5774
        return f"{enerji_tasarrufu:.2f} kWh enerji tasarrufu sağlandı."

class MetalAtik(Atik):
    def hesapla(self):
        # 1 ton metal geri dönüşümü 1.1 ton demir cevheri tasarrufu sağlar
        hammadde_tasarrufu = (self.get_miktar() / 1000) * 1.1
        return f"{hammadde_tasarrufu:.2f} ton hammadde tasarrufu sağlandı."
    


class Kullanici:
    def __init__(self, ad):
        self.ad = ad
        self.__toplam_tasarruf = 0 # Kapsülleme: Dışarıdan değiştirilemez 

    def tasarruf_ekle(self, miktar):
        self.__toplam_tasarruf += miktar

    def seviye_getir(self):
        if self.__toplam_tasarruf > 1000:
            return "Doğa Elçisi"
        return "Yeni Başlayan"
    

class Kullanici:
    def __init__(self, ad):
        self.ad = ad
        self.__toplam_kg = 0  # Kapsülleme: Dışarıdan doğrudan değiştirilemez 

    def atik_ekle(self, kg):
        if kg > 0:
            self.__toplam_kg += kg

    def get_istatistik(self):
        # Ünvan belirleme mantığı
        if self.__toplam_kg == 0:
            unvan = "Yeni Gönüllü"
        elif self.__toplam_kg < 50:
            unvan = "Doğa Dostu"
        elif self.__toplam_kg < 200:
            unvan = "Geri Dönüşüm Uzmanı"
        else:
            unvan = "Dünya Kahramanı"
        
        return self.__toplam_kg, unvan
    
class Atik:
    def __init__(self, miktar):
        self.__miktar = miktar # Kapsülleme (Encapsulation) 

    def get_miktar(self):
        return self.__miktar

class KagitAtik(Atik): # Kalıtım (Inheritance) 
    def hesapla(self):
        return f"{(self.get_miktar() / 1000) * 17:.2f} adet ağaç kurtarıldı."

class PlastikAtik(Atik):
    def hesapla(self):
        return f"{(self.get_miktar() / 1000) * 5774:.2f} kWh enerji tasarrufu sağlandı."

class MetalAtik(Atik):
    def hesapla(self):
        return f"{(self.get_miktar() / 1000) * 1.1:.2f} ton hammadde tasarrufu sağlandı."

class Kullanici:
    def __init__(self, ad):
        self.ad = ad
        self.__toplam_kg = 0

    def atik_ekle(self, kg):
        if kg > 0: self.__toplam_kg += kg

    def get_istatistik(self):
        kg = self.__toplam_kg
        if kg == 0: unvan = "Doğa Gönüllüsü"
        elif kg <= 30: unvan = "Yeşil Filiz"
        elif kg <= 100: unvan = "Geri Dönüşüm Elçisi"
        elif kg <= 250: unvan = "Çevre Koruyucu"
        elif kg <= 500: unvan = "Eko-Savaşçı"
        else: unvan = "Doğa Kahramanı"
        return kg, unvan