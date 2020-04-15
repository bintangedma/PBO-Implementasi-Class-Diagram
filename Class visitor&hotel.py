class Visitor:
    def __init__(self, nama, id_visitor, alamat, no_KTP, tanggal_lahir):
        self.nama = nama
        self.__id_visitor = id_visitor
        self.alamat = alamat
        self.no_KTP = no_KTP
        self.tanggal_lahir = tanggal_lahir

    def check_in(self):
        self.nama
        self.no_KTP
    def check_out(self):
        self.__id_visitor
    def book(self):
        self.room_code
        self.no_KTP
            
    def getNama(self):
        return self.nama
    def getId_visitor(self):
        return self.__id_visitor
    def getAlamat(self):
        return self.alamat
    def getNo_KTP(self):
        return self.no_KTP
    def getTgl_lahir(self):
        return self.tanggal_lahir

    def setNama(self, baru):
        self.nama = baru
    def setId_visitor(self, baru):
        self.__id_visitor = baru
    def setAlamat(self, baru):
        self.alamat = baru
    def setNo_KTP(self, baru):
        self.no_KTP = baru
    def setTgl_lahir(self, baru):
        self.tanggal_lahir = baru



class Hotel:
    def __init__(self, nama_hotel, alamat, fasilitas):
        self.nama = nama_hotel
        self.alamat = alamat
        self.fasilitas = fasilitas
    
    def getNama_hotel(self):
        return self.nama_hotel
    def getAlamat(self):
        return self.alamat
    def getFasilitas(self):
        return self.fasilitas
    
    def setNama_hotel(self, baru):
        self.nama_hotel = baru
    def setAlamat(self):
        self.alamat = baru
    def setFasilitas(self):
        self.fasilitas = baru