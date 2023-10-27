class Kontur:
    QIYMETLER = {'mesaj': 0.5, 'zeng': 1.20, 'internet': 3}
    
    def __init__(self, initial_balance=10):
        self.balans = initial_balance

    def kontur_cix(self, operation):
        if operation in self.QIYMETLER:
            cost = self.QIYMETLER[operation]
            if cost <= self.balans:
                self.balans -= cost
                return f"Emeliyatdan sonraki balans: {self.balans}"
            else:
                return "Kifayet qeder balansiniz yoxdur."
        else:
            return "Emeliyat tesdiqlenmedi"

    def kontur_artir(self, amount):
        self.balans += amount
        return f"Balansiniza {amount} manat əlavə edildi. Yeni balans: {self.balans}"

telefon1 = Kontur(initial_balance=20)

class Telefon:
    def __init__(self, kontur):
        self.kontur = kontur
        self.gonderilen_mesajlar = []
        self.alinan_mesajlar = []

    def mesaj_gonder(self, hedef_telefon, gonderilen_mesaj):
        mesaj_qiymeti = self.kontur.kontur_cix('mesaj')
        if hedef_telefon.mesaj_al(gonderilen_mesaj):
            self.gonderilen_mesajlar.append(gonderilen_mesaj)
        return self.gonderilen_mesajlar

    def mesaj_al(self, alinan_mesaj):
        bildiris = f"Sizə '{alinan_mesaj}' kontentli bildiriş gəldi"
        self.alinan_mesajlar.append(bildiris)
        return self.alinan_mesajlar
kontur1 = Kontur()
telefon1 = Telefon(kontur1)

kontur2 = Kontur()
telefon2 = Telefon(kontur2)

telefon1.mesaj_gonder(telefon2, "Salam")
telefon1.mesaj_gonder(telefon2, "Necesen")
print(telefon2.alinan_mesajlar) 
print(telefon1.kontur.balans) 

