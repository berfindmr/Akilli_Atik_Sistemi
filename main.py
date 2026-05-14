import tkinter as tk
from tkinter import messagebox, ttk
from hesaplamalar import atik_isleme_merkezi
from modeller import Kullanici, VeritabaniSistemi

class AtikUygulamasi:
    def __init__(self, pencere):
        self.pencere = pencere
        self.pencere.title("Akıllı Atık Sistemi")
        self.pencere.geometry("500x700") 
        self.pencere.configure(bg="#e8f5e9")

        
        VeritabaniSistemi.hazirla()
        db_verileri = VeritabaniSistemi.tum_verileri_cek()
        
        self.kullanicilar = {ad: Kullanici(ad, kg) for ad, kg in db_verileri}

        tk.Label(pencere, text="DOĞA DOSTU TAKİP PANELİ", font=("Arial", 14, "bold"), 
                 bg="#2d5a27", fg="white", pady=10).pack(fill="x")

        frame = tk.Frame(pencere, bg="#e8f5e9", pady=10)
        frame.pack()

        tk.Label(frame, text="Kullanıcı Seç:", bg="#e8f5e9", font=("Arial", 10, "bold")).grid(row=0, column=0)
        self.user_combo = ttk.Combobox(frame, values=list(self.kullanicilar.keys()), state="readonly")
        self.user_combo.current(0)
        self.user_combo.grid(row=0, column=1, padx=10)

        tk.Label(frame, text="Atık Türü:", bg="#e8f5e9", font=("Arial", 10, "bold")).grid(row=1, column=0, pady=10)
        self.tur_var = tk.StringVar(value="1")
        tk.Radiobutton(frame, text="Kağıt", variable=self.tur_var, value="1", bg="#e8f5e9").grid(row=1, column=1, sticky="w")
        tk.Radiobutton(frame, text="Plastik", variable=self.tur_var, value="2", bg="#e8f5e9").grid(row=2, column=1, sticky="w")
        tk.Radiobutton(frame, text="Metal", variable=self.tur_var, value="3", bg="#e8f5e9").grid(row=3, column=1, sticky="w")

        tk.Label(frame, text="Miktar (kg):", bg="#e8f5e9", font=("Arial", 10, "bold")).grid(row=4, column=0, pady=10)
        self.entry_miktar = tk.Entry(frame)
        self.entry_miktar.grid(row=4, column=1)

        tk.Button(pencere, text="DÖNÜŞÜMÜ KAYDET", command=self.kaydet, 
                  bg="#2d5a27", fg="white", font=("Arial", 11, "bold"), width=20).pack(pady=5)

      
      

        ekle_frame = tk.LabelFrame(pencere, text=" Yeni Çevreci Ekle ", bg="#e8f5e9", font=("Arial", 10, "bold"), pady=10)
        ekle_frame.pack(fill="x", padx=20, pady=10)

        self.entry_yeni_ad = tk.Entry(ekle_frame)
        self.entry_yeni_ad.pack(side="left", padx=10, expand=True, fill="x")
        
        tk.Button(ekle_frame, text="Sisteme Ekle", command=self.yeni_kullanici_ekle, 
                  bg="#10b981", fg="white", font=("Arial", 9, "bold")).pack(side="right", padx=10)

      

        self.stats_label = tk.Label(pencere, text="", font=("Consolas", 10), 
                                    bg="white", relief="sunken", bd=2, justify="left", padx=10, pady=10)
        self.stats_label.pack(pady=10, fill="both", padx=20)
        self.guncelle_tablo()

    def guncelle_tablo(self):
        tablo = f"{'İsim':<10} | {'Miktar':<8} | {'Ünvan'}\n" + "-"*35 + "\n"
        for ad, obj in self.kullanicilar.items():
            kg, unvan = obj.get_istatistik()
            tablo += f"{ad:<10} | {kg:>5.1f} kg | {unvan}\n"
        self.stats_label.config(text=tablo)

    def yeni_kullanici_ekle(self):
        yeni_ad = self.entry_yeni_ad.get().strip()
        if yeni_ad:
           
            if VeritabaniSistemi.yeni_kullanici_ekle(yeni_ad): 
                self.kullanicilar[yeni_ad] = Kullanici(yeni_ad, 0)
                self.user_combo['values'] = list(self.kullanicilar.keys())
                self.guncelle_tablo()
                self.entry_yeni_ad.delete(0, tk.END)
                messagebox.showinfo("Başarılı", f"{yeni_ad} sisteme dahil edildi!")
            else:
                messagebox.showerror("Hata", "Bu isim zaten kayıtlı!")
        else:
            messagebox.showwarning("Uyarı", "Lütfen bir isim giriniz!")

    def kaydet(self):
        try:
            ad = self.user_combo.get()
            miktar = float(self.entry_miktar.get())
            tur = self.tur_var.get()
            if miktar <= 0: raise ValueError
            
            sonuc = atik_isleme_merkezi(tur, miktar)
            self.kullanicilar[ad].atik_ekle(miktar)
            self.guncelle_tablo()
            
            messagebox.showinfo("Başarılı", f"Kayıt Tamamlandı!\n{sonuc}")
            self.entry_miktar.delete(0, tk.END)
        except ValueError:
            messagebox.showerror("Hata", "Lütfen geçerli bir miktar giriniz!")

if __name__ == "__main__":
    root = tk.Tk()
    AtikUygulamasi(root)
    root.mainloop()