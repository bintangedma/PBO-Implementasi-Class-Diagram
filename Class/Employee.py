#from db.base import Base, sessionFactory
#from db.orm.EmployeeORM import EmployeeORM
import Room
import Visitor
class Employee :
    #Class variable
    jumlahEmp = 0;
    list_employee = []
    #instance
    def __init__(self, nama_emp, TL_emp, jabatan_emp, JK_emp, alamat_emp):
        self.nama_emp = nama_emp
        self.__id_emp = "EMP"+str(Employee.jumlahEmp+1)
        self.TL_emp = TL_emp
        self.jabatan_emp = jabatan_emp
        self.JK_emp = JK_emp
        self.alamat_emp = alamat_emp
        Employee.list_employee.append(self)
        Employee.jumlahEmp += 1

        #self.info = "name {} : \n\t id_emp: {}\n\t jabatan: {}".format(self.nama_emp, self.__id_emp, self.jabatan_emp)
    #method

    def getNama(self):
        return self.nama_emp
    def setNama(self) :
        new = input("masukkan nama baru : ")
        self.nama_emp = new
    @property
    def info(self):
        return "name {} : \n\t id_emp: {}\n\t jabatan: {}".format(self.nama_emp, self.__id_emp, self.jabatan_emp)
    @property
    def id_emp(self):
        pass
    @id_emp.getter
    def id_emp(self):
        return self.__id_emp
    @id_emp.setter
    def id_emp(self):
        new = input("masukkan id baru : ")
        self.__id_emp = new

    def getTL(self):
        return self.TL_emp
    def setTL(self):
        new = input("masukkan tanggal lahir baru : ")
        self.TL_emp = new

    def getJabatan(self):
        return self.jabatan_emp
    def setJabatan(self):
        new = input("masukkan jabatan baru : ")
        self.jabatan_emp = new

    def getJK(self):
        return self.JK_emp
    def setJK(self):
        new = input("masukkan jenis kelamin baru : ")
        self.JK_emp = new
    
    def getAlamat(self):
        return self.alamat_emp
    def setAlamat(self):
        new = input("masukkan alamat baru : ")
        self.alamat_emp = new

class Receptionist(Employee):
    list_receptionist = []
    daftar_harga = [["N", 500000], ["VIP", 750000], ["VVIP", 1000000]]
    jumlahRec = 0
    def __init__(self, nama_emp, TL_emp, JK_emp, alamat_emp):
        super().__init__(nama_emp, TL_emp, "Receptionist", JK_emp, alamat_emp)
        self.daftar_harga = [["N", 500000], ["VIP", 750000], ["VVIP", 1000000]]
        self.tagihan = []
        Receptionist.jumlahRec += 1

    def menu(self):
        menu = input("Selamat datang, Apa yang ingin anda lakukan? \n1. Booking\n2. Cari Ruangan \n3. Check Out\n ===[>")
        if menu == "1" or menu == "Booking" or menu == "booking":
            self.book()
        elif menu == "2" or menu == "cari" or menu == "Cari":
            self.search_room()
        elif menu == "3" or menu == "checkout" or menu == "out":
            self.checkOut()
        else : 
            print("mohon masukkan kata kunci yang benar!")
            self.menu()

    def book(self):
        KTP = input("masukkan nomor KTP anda : ")
        for i in Visitor.Visitor.list_visitor : 
            if KTP == i.no_KTP :
                room_code = input("Masukkan tipe kamar : (N/VIP/VVIP)")
                room_number = input("Masukkan nomor kamar : ")
                durasi = int(input("Ingin booking kamar berapa malam?"))
                if room_code == "N":
                    harga = Receptionist.daftar_harga[0][1]
                    i.tagihan.append(harga*durasi)
                    Room.Room.room_list.append(Room.Room(room_number, room_code))
                    print("booking berhasil! \nNama\t\t:  {}\nTagihan \t: {} Rupiah".format(i.nama, i.tagihan[0]))
                elif room_code == "VIP":
                    harga = Receptionist.daftar_harga[1][1]
                    i.tagihan.append(harga*durasi)
                    Room.Room.room_list.append(Room.Room(room_number, room_code))
                    print("booking berhasil! \nNama\t\t: {}\nTagihan \t: {} Rupiah".format(i.nama, i.tagihan[0]))
                elif room_code == "VVIP":
                    harga = Receptionist.daftar_harga[2][1]
                    i.tagihan.append(harga*durasi)
                    Room.Room.room_list.append(Room.Room(room_number, room_code))
                    print("booking berhasil! \nNama\t\t: {}\nTagihan \t: {} Rupiah".format(i.nama, i.tagihan[0]))
                else:
                    print("masukkan tipe ruangan dengan benar!")
                    self.book()
            else : 
                print("data tidak ditemukan")
                self.book()
        #id = room_code+room_number
        #self.room_list.append(Room.Room(room_number, room_code))
        #for i in self.room_list:
        #    if id not in i.id_room:
        #        self.room_list.append(Room.Room(room_number, room_code))
        #    else : 
        #        print("room ini telah dibooking! coba cari yang lain")
        #        ask = input("ingin cari kamar lain ?(Y/N) : ")
        #        if ask =="Y":
        #            self.book()
        #        else:
        #            return
        
    def search_room(self):
        kode = input("Masukkan tipe kamar : (N/VIP/VVIP)")
        cari = input("Masukkan nomor kamar : ")
        id = kode+cari
        for i in Room.Room.room_list : 
            if id == i.id_room:
                print("Ruangan ini telah dibooking")
                ask = input("apakah anda ingin mencari ruangan lagi?(Y/N) : ")
                if ask == "Y":
                    self.search_room()
                else:
                    return
            else :
                if kode == "N" or kode == "VIP" or kode == "VVIP":
                    print("Ruangan ini tersedia")
                    ask = input("apakah anda ingin mencari ruangan lagi?(Y/N) : ")
                    if ask == "Y":
                        self.search_room()
                    else:
                        return
                else : 
                    print("itu bukan kode ruangan! gunakan huruf kapital (N/VIP/VVIP)")
                    self.search_room()
    
    def checkOut(self):
        kode = input("Masukkan tipe kamar : (N/VIP/VVIP)")
        cari = input("Masukkan nomor kamar : ")
        id = kode+cari
        for i in Room.Room.room_list:
            if id == i.id_room:
                print("Terima kasih telah berkunjung")
                Room.Room.room_list.remove(i)
            else: 
                print("data tidak ditemukan")
                ask = input("apakah anda ingin mengulanginya lagi?(Y/N) : ")
                if ask == "Y":
                    self.checkOut()
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

    def reservation(self):
        pass
        
    #def perpanjang_book(self):
    #    room_code = input("Masukkan tipe kamar : (N/VIP/VVIP)")
    #    room_number = input("Masukkan nomor kamar : ")
    #    self.room_list.append(Room.Room(room_number, room_code))

class Marketing_crew(Employee):
    list_MC = []
    jumlahMC = 0
    rev_vis = Visitor.Visitor.revenue
    def __init__(self, nama_emp, TL_emp, JK_emp, alamat_emp):
        super().__init__(nama_emp, TL_emp, "Marketing Crew", JK_emp, alamat_emp)
        Marketing_crew.jumlahMC += 1

    def laporan(self):
        total_vis = Visitor.Visitor.jumlahVis
        total_emp = Employee.jumlahEmp
        revenue = Marketing_crew.rev_vis
        print("Jumlah pengunjung : {} \nJumlah Karyawan : {}\nPendapatan : {}".format(total_vis, total_emp, revenue))

    def getHarga(self):
        type = input("Masukkan tipe ruangan(N/VIP/VVIP) : ")
        if type == "N" or type == "Normal":
            print("Rp.{},- per malam untuk kamar {}".format(Receptionist.daftar_harga[0][1], Receptionist.daftar_harga[0][0]))
            ulang = input("ulangi lagi ?(y/n) : ")
            if ulang == "y" or ulang == "ya" or ulang == "Y":
                self.getHarga()
            else : 
                return
        elif type == "VIP":
            print("Rp.{},- per malam untuk kamar {}".format(Receptionist.daftar_harga[1][1], Receptionist.daftar_harga[1][0]))
            ulang = input("ulangi lagi ?(y/n) : ")
            if ulang == "y" or ulang == "ya" or ulang == "Y":
                self.getHarga()
            else : 
                return
        elif type == "VVIP":
            print("Rp.{},- per malam untuk kamar {}".format(Receptionist.daftar_harga[2][1], Receptionist.daftar_harga[2][0]))
            ulang = input("ulangi lagi ?(y/n) : ")
            if ulang == "y" or ulang == "ya" or ulang == "Y":
                self.getHarga()
            else : 
                return
        else: 
            print("itu bukan tipe ruangan")
            self.getHarga()

    def upd_harga(self):
        baru = input("masukkan harga baru : ")
        Room.harga = baru

    def setHarga(self):
        untuk = input("harga tipe ruangan ini akan diganti per malamnya(N/VIP/VVIP) : ")
        baru = int(input("masukkan harga baru : "))
        if untuk == "N":
            Receptionist.daftar_harga[0][1] = baru
        elif untuk == "VIP":
            Receptionist.daftar_harga[1][1] = baru
        elif untuk == "VVIP":
            Receptionist.daftar_harga[2][1] = baru
        else : 
            print("hanya ada 3 tipe ruangan di hotel ini yaitu N/VIP/VVIP, mohon ulangi ya")
            self.setHarga()
        #for i in Employee.Receptionist.daftar_harga : 
         #   for a in i : 
          #      if untuk == "N":
class Cashier(Employee):
    list_cashier = []
    jumlahCashier = 0
    def __init__(self, nama_emp, TL_emp, JK_emp, alamat_emp):
        super().__init__(nama_emp, TL_emp, "Cashier", JK_emp, alamat_emp)
        Cashier.jumlahCashier += 1


    def receipt(self):
        KTP = input("masukkan nomor KTP anda : ")
        for i in Visitor.Visitor.list_visitor : 
            if KTP == i.no_KTP :
                print("========receipt=========")
                print("Total yang harus dibayar : {}".format(i.tagihan[0]))


#johnny = Employee("Johnny Walkerine", "19283", "Supervisor", "male", "Cluster")
#print(johnny.__dict__)
#m1 = Marketing_crew("bintang", "California", "Man", "NYC")
#m1.getHarga()
#print(Receptionist.daftar_harga)
#rec1 = Receptionist("bintang", "california", "BOY", "NYC")
#print(rec1.__dict__)
#rec1.menu()
#rec1.menu()
#rec1.menu()
#print(rec1.room_list[0].__dict__)
#rec1.checkOut()
#print(rec1.room_list[0].__dict__)
#rec1.search_room()
#print(rec1.room_list)