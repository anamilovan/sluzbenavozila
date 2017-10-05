from SluzbeniAvtomobili import vozilo

def menu():
    print "1. Dodaj vozilo"
    print "2. Izpisi vozilo"
    print "3. Izbrisi vozilo"
    print "4. Shrani vozilo"
    print "5. Izpis vseh vozil"
    print "6. Izhod"
    return int(raw_input())

def dodaj():
        from SluzbeniAvtomobili import vozilo

        znamka = raw_input("Vnesite znamko vozila: ")
        model = raw_input("Vnesite model vozila: ")
        km = int(raw_input("Vnesite stevilo prevozenih kilometrov: "))
        zadnji_servis = raw_input("Vnesite datum zadnjega servisa: ")

        vozilo = vozilo(znamka=znamka, model=model, km=km, zadnji_servis=zadnji_servis)

        return vozilo

def izpis_vozil(vozila_list):
    i=0
    for x in vozila_list:
        print str(i) + "."
        x.izpis()
        i += 1

def shrani(vozila_list):
    file = open("vozila.txt", "w+")

    for vozilo in vozila_list:
        file.write(vozilo.znamka + ";")
        file.write(vozilo.model + ";")
        file.write(str(vozilo.km) + ";")
        file.write(vozilo.zadnji_servis + ";")

def preberi():
    file = open("vozila.txt", "r+")
    temp_vozila = []
    for line in file:
        a = line.split(";")
        av = vozilo(a[0], a[1], int(a[2]), a[3])
        temp_vozila.append(av)
    return temp_vozila

vozila = []

while True:
    x = menu()

    if x == 1:
        vozilo = dodaj()
        vozila.append(vozilo)
        vozilo.izpis()

    if x == 2:
        izpis_vozil(vozila)

    if x == 3:
        izpis_vozil(vozila)
        st_vozila = int(raw_input("Stevilka vozila za izpis"))
        vozila.remove(vozila[st_vozila])

    if x == 4:
        shrani(vozila)

    if x == 5:
        vozila = preberi()

    if x == 6:
        break
