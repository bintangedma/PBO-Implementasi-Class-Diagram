import Room
class Visitor:
    jumlahVis = 0;
    def __init__(self, nama, alamat, no_KTP, tanggal_lahir):
        self.nama = nama
        self.__id_visitor = "VIS"+str(Visitor.jumlahVis+1)+no_KTP
        self.alamat = alamat
        self.no_KTP = no_KTP
        self.tanggal_lahir = tanggal_lahir
        self.tagihan = []
        self.daftar_harga = [["N", 500000], ["VIP", 750000], ["VVIP", 1000000]]
        Visitor.jumlahVis += 1

    def book(self):
        room_code = input("Masukkan tipe kamar : (N/VIP/VVIP)")
        room_number = input("Masukkan nomor kamar : ")
        if room_code == "N":
            harga = self.daftar_harga[0][1]
            self.tagihan.append(harga)
            Room.Room.room_list.append(Room.Room(room_number, room_code))
            print("booking berhasil! \nAngka yang harus anda bayar adalah senilai {} Rupiah".format(self.tagihan[0]))
        elif room_code == "VIP":
            harga = self.daftar_harga[1][1]
            self.tagihan.append(harga)
            Room.Room.room_list.append(Room.Room(room_number, room_code))
            print("booking berhasil! \nAngka yang harus anda bayar adalah senilai {} Rupiah".format(self.tagihan[0]))
        elif room_code == "VVIP":
            harga = self.daftar_harga[2][1]
            self.tagihan.append(harga)
            Room.Room.room_list.append(Room.Room(room_number, room_code))
            print("booking berhasil! \nAngka yang harus anda bayar adalah senilai {} Rupiah".format(self.tagihan[0]))
        else:
            print("masukkan tipe ruangan dengan benar!")
            self.book()
        
    
    def check_out(self):
        pass

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
#bintang.book()
#print(bintang.__dict__)