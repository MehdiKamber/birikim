class HakanBirikim:
    def __init__(self, birikim_miktari, ev_fiyati, kira_geliri, pesinat_orani, kredi_suresi):
        self.birikim_miktari = birikim_miktari
        self.ev_fiyati = ev_fiyati
        self.kira_geliri = kira_geliri
        self.pesinat_orani = pesinat_orani
        self.kredi_suresi = kredi_suresi
        self.birikim = 0
        self.daire_sayisi = 0
        self.yas = 25
        self.kira_geliri_toplam = 0

    def ev_satinalma(self):
        pesinat = self.ev_fiyati * self.pesinat_orani
        kalan_kredi = self.ev_fiyati - pesinat
        kredi_odeme = kalan_kredi / (self.kredi_suresi * 12)

        while self.yas < 65:
            self.birikim += self.birikim_miktari
            self.birikim += self.kira_geliri * self.daire_sayisi

            if self.birikim >= pesinat:
                self.birikim -= pesinat
                self.daire_sayisi += 1

            if self.daire_sayisi > 0:
                self.birikim -= kredi_odeme * self.daire_sayisi
                self.kira_geliri_toplam += self.kira_geliri * self.daire_sayisi

            self.yas += 1

        return self.daire_sayisi, self.kira_geliri_toplam
