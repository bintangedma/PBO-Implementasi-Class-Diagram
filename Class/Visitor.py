import Room
from db.Orm.VisitorOrm import VisitorOrm
class Visitor:
    list_visitor = []
    jumlahVis = 0;
    revenue = 0
    daftar_harga = Room.Room.daftar_harga
    def __init__(self, nama, alamat, no_KTP, tanggal_lahir):
        self.nama = nama
        self.__id_visitor = "VIS"+str(Visitor.jumlahVis+1)+no_KTP
        self.alamat = alamat
        self.no_KTP = no_KTP
        self.tanggal_lahir = tanggal_lahir
        self.tagihan = []
        self.riwayat = []
        self.kamar = []
        Visitor.list_visitor.append(self)
        Visitor.jumlahVis += 1

    def book(self):
        room_code = input("Masukkan tipe kamar : (N/VIP/VVIP)")
        room_number = input("Masukkan nomor kamar : ")
        durasi = int(input("Ingin booking kamar berapa malam? : "))
        id = room_code+room_number
        if room_code == "N":
            harga = Visitor.daftar_harga[0][1]
            self.tagihan.append(harga*durasi)
            Room.Room.room_list.append(Room.Room(room_number, room_code))
            self.kamar.append(id)
            print("booking berhasil! \nAngka yang harus anda bayar adalah senilai {} Rupiah".format(self.tagihan[0]))
            a = int(self.tagihan[0])
            Visitor.revenue+=a
            return Visitor.revenue

        elif room_code == "VIP":
            harga = Visitor.daftar_harga[1][1]
            self.tagihan.append(harga*durasi)
            Room.Room.room_list.append(Room.Room(room_number, room_code))
            self.kamar.append(id)
            print("booking berhasil! \nAngka yang harus anda bayar adalah senilai {} Rupiah".format(self.tagihan[0]))
            a = int(self.tagihan[0])
            Visitor.revenue+=a
            return Visitor.revenue

        elif room_code == "VVIP":
            harga = Visitor.daftar_harga[2][1]
            self.tagihan.append(harga*durasi)
            Room.Room.room_list.append(Room.Room(room_number, room_code))
            self.kamar.append(id)
            print("booking berhasil! \nAngka yang harus anda bayar adalah senilai {} Rupiah".format(self.tagihan[0]))
            a = int(self.tagihan[0])
            Visitor.revenue+=a
            return Visitor.revenue

        else:
            print("masukkan tipe ruangan dengan benar!")
            self.book()
        
    
    def checkOut(self):
        a = sum(self.tagihan)
        print("Biaya sewa kamar : Rp.{},-\nTotal : Rp.{},-".format(self.tagihan[0], a))
        self.pay()

    def pay(self):
        a = sum(self.tagihan)
        pay = int(input("masukkan nominal pembayaran :"))
        paid = pay - a
        if pay >= a:
            receipt = ("Total pembayaran : Rp.{},-\nDibayarkan\t : Rp.{},-\nKembalian\t : Rp.{},-".format(a, pay, paid))
            print(receipt)
            for i in self.tagihan : 
                self.tagihan.remove(i)
            for kamar in self.kamar :
                self.riwayat.append(kamar)
                self.kamar.remove(kamar)
            self.riwayat.append(receipt)
            for room in Room.Room.room_list : 
                if kamar == room.id_room : 
                    Room.Room.room_list.remove(room)

        else : 
            print("maaf uang anda kurang Rp{},-".format(-paid))
            self.pay()
        
            
        


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
#print(Visitor.list_visitor[0].__dict__)
#print(Visitor.revenue)

#print(Room.Room.room_list)
#bintang.book()
#print(bintang.__dict__)
#print(Room.Room.room_list)
#print(Room.Room.room_list[0].__dict__)
#bintang.checkOut()
#print(Room.Room.room_list)
#bintang.checkOut()
#print(Visitor.revenue)
#print(bintang.__dict__)
