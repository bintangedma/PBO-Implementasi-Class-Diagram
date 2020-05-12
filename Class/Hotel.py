class Hotel:
    fasilitas = []
    def __init__(self, nama_hotel, alamat_hotel):
        self.nama_hotel = nama_hotel
        self.alamat_hotel = alamat_hotel
    
    def getNama_hotel(self):
        return self.nama_hotel
    def getAlamat(self):
        return self.alamat_hotel

    def setNama_hotel(self, baru):
        self.nama_hotel = baru
    def setAlamat(self, baru):
        self.alamat_hotel = baru

    def add_facility(self):
        print("tambah fasilitas baru ")
        fac = input("nama fasilitas baru : ")
        cost = input("berapa harganya : ")
        per = input("per ? : ")
        Hotel.fasilitas.append([fac,cost, per])
        ask = input("ingin tambah lagi (y/n)? ")
        if ask == "y" or ask == "Y" or ask == "ya":
            self.add_facility()
        else : 
            return

    def get_facility(self):
        print("berikut adalah fasilitas dari hotel ini")
        for a in Hotel.fasilitas : 
            print(a[0]," : ", a[1],"per", a[2],"\n", end='')

#hotel1 = Hotel("Grand Senyiur", "gupas")
#hotel1.add_facility()
#print(hotel1.fasilitas[0])
#hotel1.get_facility()