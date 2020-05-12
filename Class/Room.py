
class Room:
    room_list = []
    daftar_harga = [["N", 500000], ["VIP", 750000], ["VVIP", 1000000]]
    def __init__(self, room_number, room_code):
        self.room_number = str(room_number)
        self.room_code = str(room_code)
        self.id_room = self.room_code+self.room_number
        self.tagihan = []
        Room.room_list.append(self)

    def search_room(self):
        kode = input("Masukkan tipe kamar : (N/VIP/VVIP)")
        cari = input("Masukkan nomor kamar : ")
        id = kode+cari
        for i in Room.room_list : 
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
                    
    #daftar harga disini tidak dipakai, yang dipakai adalah daftar harga yang ada pada Receptionist
    def getHarga(self):
        go = input("=====Daftar harga======\nApakah anda ingin melihat semua harga atau satu per satu?\n1. Tampilkan semua\n2. Tampilkan satu per satu\n(1/2)>")
        if go == "2":    
            tipe = input("Masukkan tipe ruangan : ")
            if tipe == "N" or type == "Normal":
                print("Rp.{},- per malam untuk kamar {}".format(Room.daftar_harga[0][1], Room.daftar_harga[0][0]))
            elif tipe == "VIP":
                print("Rp.{},- per malam untuk kamar {}".format(Room.daftar_harga[1][1], Room.daftar_harga[1][0]))
            elif tipe == "VVIP":
                print("Rp.{},- per malam untuk kamar {}".format(Room.daftar_harga[2][1], Room.daftar_harga[2][0]))
            else: 
                print("itu bukan tipe ruangan, masukkan tipe ruangan yang benar!")
                self.getHarga()
        elif go == "1":
            print("Rp.{},- per malam untuk kamar {}".format(Room.daftar_harga[0][1], Room.daftar_harga[0][0]))
            print("Rp.{},- per malam untuk kamar {}".format(Room.daftar_harga[1][1], Room.daftar_harga[1][0]))
            print("Rp.{},- per malam untuk kamar {}".format(Room.daftar_harga[2][1], Room.daftar_harga[2][0]))
        else : 
            print("tolong pilih angka 1 atau 2 saja")
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
        
    def getHarga(self):
        type = input("Masukkan tipe ruangan : ")
        if type == "N" or type == "Normal":
            print("Rp.{},- per malam untuk kamar {}".format(Harga.daftar_harga[0][1], self.daftar_harga[0][0]))
        elif type == "VIP":
            print("Rp.{},- per malam untuk kamar {}".format(self.daftar_harga[1][1], self.daftar_harga[1][0]))
        elif type == "VVIP":
            print("Rp.{},- per malam untuk kamar {}".format(self.daftar_harga[2][1], self.daftar_harga[2][0]))
        else: 
            print("itu bukan tipe ruangan")
            self.getHarga()
        
    def setHarga(self):
        baru = int(input("masukkan harga baru : "))
        untuk = input("harga tipe ruangan ini akan diganti per malamnya(N/VIP/VVIP) : ")
        if untuk == "N":
            Employee.Receptionist.daftar_harga[0][1] = baru
        elif untuk == "VIP":
            Employee.Receptionist.daftar_harga[1][1] = baru
        elif untuk == "VVIP":
            Employee.Receptionist.daftar_harga[2][1] = baru
        #for i in Employee.Receptionist.daftar_harga : 
         #   for a in i : 
          #      if untuk == "N":
                    
        
#print(Employee.Receptionist.daftar_harga.__dict__)
#r1 = Harga_room(10, 10)
#r1.setHarga()
#print(r1.id_room)
#r2 = Room("bintang", "bintang")
#r2.getHarga()
#r2.getHarga()
#r1.book()
#print(r1.room_list[0].__dict__)
#r1.search_room()