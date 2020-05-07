class Room:
    def __init__(self, room_number, room_code):
        self.room_number = str(room_number)
        self.room_code = str(room_code)
        self.id_room = self.room_code+self.room_number
        self.room_list = []
        self.daftar_harga = [["N", 500000], ["VIP", 750000], ["VVIP", 1000000]]
        self.tagihan = []

    def book(self):
        room_code = input("Masukkan tipe kamar(N/VIP/VVIP) : ")
        room_number = input("Masukkan nomor kamar : ")
        if room_code == "N":
            harga = self.daftar_harga[0][1]
            self.tagihan.append(harga)
            self.room_list.append(Room(room_number, room_code))
            print("booking berhasil! \nAngka yang harus anda bayar adalah senilai {} Rupiah".format(self.tagihan[0]))
        elif room_code == "VIP":
            harga = self.daftar_harga[1][1]
            self.tagihan.append(harga)
            self.room_list.append(Room(room_number, room_code))
            print("booking berhasil! \nAngka yang harus anda bayar adalah senilai {} Rupiah".format(self.tagihan[0]))
        elif room_code == "VVIP":
            harga = self.daftar_harga[2][1]
            self.tagihan.append(harga)
            self.room_list.append(Room(room_number, room_code))
            print("booking berhasil! \nAngka yang harus anda bayar adalah senilai {} Rupiah".format(self.tagihan[0]))
        else:
            print("masukkan tipe ruangan dengan benar! ikuti contoh")
            self.book()

    def search_room(self):
        kode = input("Masukkan tipe kamar : (N/VIP/VVIP)")
        cari = input("Masukkan nomor kamar : ")
        id = kode+cari
        for i in self.room_list : 
            if id == i.id_room:
                print("Ruangan ini telah dibooking")
                ask = input("apakah anda ingin mencari ruangan lagi?(Y/N) : ")
                if ask == "Y":
                    self.search_room()
                else:
                    return
            else :
                print("Ruangan ini tersedia")
                ask = input("apakah anda ingin mencari ruangan lagi?(Y/N) : ")
                if ask == "Y":
                    self.search_room()
                else:
                    return
    def getHarga(self):
        type = input("Masukkan tipe ruangan : ")
        if type == "N" or type == "Normal":
            print("Rp.{},- per malam untuk kamar {}".format(self.daftar_harga[0][1], self.daftar_harga[0][0]))
        elif type == "VIP":
            print("Rp.{},- per malam untuk kamar {}".format(self.daftar_harga[1][1], self.daftar_harga[1][0]))
        elif type == "VVIP":
            print("Rp.{},- per malam untuk kamar {}".format(self.daftar_harga[2][1], self.daftar_harga[2][0]))
        else: 
            print("itu bukan tipe ruangan")
            self.getHarga()
        
    def getRoom_number(self):
        return self.room_number
    def getRoom_code(self):
        return self.room_code
        
    def setRoom_number(self):
        baru = input("masukkan nomor ruangan baru : ")
        self.room_number = baru
    def setRoom_code(self):
        baru = input("masukkan kode ruangan baru : ")
        self.room_code = baru

class Harga_room:
    def __init__(self, room_code, harga):
        self.room_code = room_code
        self.harga = harga
        self.daftar_harga = [["N", 500000], ["VIP", 750000], ["VVIP", 1000000]]
        
    def getHarga(self):
        type = input("Masukkan tipe ruangan : ")
        if type == "N" or type == "Normal":
            print("Rp.{},- per malam untuk kamar {}".format(self.daftar_harga[0][1], self.daftar_harga[0][0]))
        elif type == "VIP":
            print("Rp.{},- per malam untuk kamar {}".format(self.daftar_harga[1][1], self.daftar_harga[1][0]))
        elif type == "VVIP":
            print("Rp.{},- per malam untuk kamar {}".format(self.daftar_harga[2][1], self.daftar_harga[2][0]))
        else: 
            print("itu bukan tipe ruangan")
            self.getHarga()
        
    def setHarga(self):
        baru = input("masukkan harga baru : ")
        self.harga = baru

#r1 = Room(10, 10)
#r1.book()
#print(r1.id_room)
#r2 = Harga_room("bintang", "bintang")
#r2.getHarga()
#r1.book()
#print(r1.room_list[0].__dict__)
#r1.search_room()