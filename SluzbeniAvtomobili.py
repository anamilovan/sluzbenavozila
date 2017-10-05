class vozilo(object):
    znamka = ""
    model = ""
    km = ""
    zadnji_servis = "1. 1. 2017"

    def __init__(self, znamka, model, km, zadnji_servis):
        self.znamka = znamka
        self.model = model
        self.km = km
        self.zadnji_servis = zadnji_servis


    def izpis(self):
        print " Znamka: %s \n Model: %s \n Prevozeni kilometri: %d \n Zadnji servis: %s "% (self.znamka, self.model, self.km, self.zadnji_servis)




