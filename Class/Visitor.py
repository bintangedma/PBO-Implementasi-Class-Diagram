class Visitor:
    jumlahVis = 0;
    def __init__(self, nama, alamat, no_KTP, tanggal_lahir):
        self.nama = nama
        self.__id_visitor = "VIS"+str(Visitor.jumlahVis+1)+no_KTP
        self.alamat = alamat
        self.no_KTP = no_KTP
        self.tanggal_lahir = tanggal_lahir
        Visitor.jumlahVis += 1

    def check_in(self):
        self.nama
        self.no_KTP
    def check_out(self):
        self.__id_visitor
    def book(self):
        self.room_code
        self.no_KTP

    @property
    def id_visitor(self):
        pass
    @id_visitor.getter
    def id_visitor(self):
        return self.__id_visitor
    @id_visitor.setter
    def id_visitor(self, new):
        new = input("masukkan id baru : ")
        self.__id_visitor = new

    def getNama(self):
        return self.nama
    def getAlamat(self):
        return self.alamat
    def getNo_KTP(self):
        return self.no_KTP
    def getTgl_lahir(self):
        return self.tanggal_lahir

    def setNama(self):
        baru = input("masukkan nama baru : ")
        self.nama = baru
    def setAlamat(self):
        baru = input("masukkan alamat baru : ")
        self.alamat = baru
    def setNo_KTP(self):
        baru = input("masukkan nomor KTP baru : ")
        self.no_KTP = baru
    def setTgl_lahir(self):
        baru = input("masukkan tanggal lahir baru : ")
        self.tanggal_lahir = baru

#bintang = Visitor("bintang", "asdas", "10101", "91273")
#print(bintang.__dict__)