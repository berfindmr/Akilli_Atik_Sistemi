import tkinter as tk
from tkinter import messagebox, ttk
from hesaplamalar import atik_isleme_merkezi
from modeller import Kullanici

class AtikUygulamasi:
    def __init__(self, pencere):
        self.pencere = pencere
        self.pencere.title("Akıllı Atık Sistemi")
        self.pencere.geometry("500x550")
        self.pencere.configure(bg="#e8f5e9") # Açık yeşil arka plan

        # Kullanıcılar
        self.kullanicilar = {ad: Kullanici(ad) for ad in ["Berfin", "Mihra", "Gülsüm", "Fatih"]}

        # Stil Ayarları
        stil = ttk.Style()
        stil.configure("TButton", font=("Arial", 10, "bold"))

        # Başlık
        tk.Label(pencere, text="DOĞA DOSTU TAKİP PANELİ", font=("Arial", 14, "bold"), 
                 bg="#2d5a27", fg="white", pady=10).pack(fill="x")

        # Seçim Alanları
        frame = tk.Frame(pencere, bg="#e8f5e9", pady=20)
        frame.pack()

        tk.Label(frame, text="Kullanıcı:", bg="#e8f5e9", font=("Arial", 10, "bold")).grid(row=0, column=0)
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

        # Buton
        tk.Button(pencere, text="DÖNÜŞÜMÜ KAYDET", command=self.kaydet, 
                  bg="#2d5a27", fg="white", font=("Arial", 11, "bold"), width=20).pack(pady=10)

        # Durum Tablosu
        self.stats_label = tk.Label(pencere, text="", font=("Consolas", 10), 
                                    bg="white", relief="sunken", bd=2, justify="left", padx=10, pady=10)
        self.stats_label.pack(pady=20, fill="both", padx=20)
        self.guncelle_tablo()

    def guncelle_tablo(self):
        tablo = f"{'İsim':<10} | {'Miktar':<8} | {'Ünvan'}\n" + "-"*35 + "\n"
        for ad, obj in self.kullanicilar.items():
            kg, unvan = obj.get_istatistik()
            tablo += f"{ad:<10} | {kg:>5} kg | {unvan}\n"
        self.stats_label.config(text=tablo)

    def kaydet(self):
        try:
            ad, miktar, tur = self.user_combo.get(), float(self.entry_miktar.get()), self.tur_var.get()
            sonuc = atik_isleme_merkezi(tur, miktar)
            self.kullanicilar[ad].atik_ekle(miktar)
            self.guncelle_tablo()
            messagebox.showinfo("Başarılı", f"Kayıt Tamamlandı!\n{sonuc}")
        except:
            messagebox.showerror("Hata", "Geçerli bir miktar giriniz!")

if __name__ == "__main__":
    root = tk.Tk()
    AtikUygulamasi(root)
    root.mainloop()