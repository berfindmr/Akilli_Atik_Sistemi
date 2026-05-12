from modeller import KagitAtik, PlastikAtik, MetalAtik

def atik_isleme_merkezi(tur, miktar):
    if tur == "1":
        obj = KagitAtik(miktar)
    elif tur == "2":
        obj = PlastikAtik(miktar)
    elif tur == "3":
        obj = MetalAtik(miktar)
    else:
        return "Geçersiz Tür!"
    
    return obj.hesapla()