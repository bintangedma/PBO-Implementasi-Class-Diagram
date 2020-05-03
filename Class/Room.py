class Room:
    def __init__(self, room_number, room_code):
        self.room_number = str(room_number)
        self.room_code = str(room_code)
        self.id_room = self.room_code+self.room_number
        self.room_list = []

    def book(self):
        room_code = input("Masukkan tipe kamar : (N/VIP/VVIP)")
        room_number = input("Masukkan nomor kamar : ")
        self.room_list.append(Room(room_number, room_code))

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
    def __init__(self, room_number, room_code, harga):
        self.room_number = room_number
        self.room_code = room_code
        self.harga = harga
        self.tanggal = tanggal
        
    def getHarga(self):
        return self.harga
        
    def setHarga(self):
        baru = input("masukkan harga baru : ")
        self.harga = baru

#r1 = Room(10, 10)
#print(r1.id_room)

#r1.book()
#print(r1.room_list[0].__dict__)
#r1.search_room()