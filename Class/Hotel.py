class Hotel:
    def __init__(self, nama_hotel, alamat_hotel):
        self.nama_hotel = nama_hotel
        self.alamat_hotel = alamat_hotel
        self.fasilitas = []
    
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
        self.fasilitas.append([fac,cost, per])

#hotel1 = Hotel("Grand Senyiur", "gupas")
#hotel1.add_facility()
#print(hotel1.fasilitas[0])