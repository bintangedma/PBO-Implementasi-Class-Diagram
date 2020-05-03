import Visitor
import Employee
import Room
#from db.base import Base, sessionFactory

class Administrator : 
    #instance
    def __init__(self, nama_admin, kode_admin):
        self.__nama_admin = nama_admin
        self.__kode_admin = kode_admin
        self.list_visitor = []
        self.list_employee = []
        self.room_list = []
    #method
    def add_visitor(self):
         nama = input("masukkan nama : ")
         id_visitor = input("masukkan id_visitor : ")
         alamat = input("masukkan alamat : ")
         no_KTP = input("masukkan no_KTP : ")
         tanggal_lahir = input("masukkan tanggal_lahir : ")
         self.list_visitor.append(Visitor.Visitor(nama, id_visitor, alamat, no_KTP, tanggal_lahir))
    
    def del_visitor(self) :
        hapus = input("masukkan id_visitor : ")
        for i in self.list_visitor:
            if hapus == i.id_visitor:
                self.list_visitor.remove(i)
            else :
                print("id yang anda masukkan tidak ada!")
                self.del_visitor()

    def upd_visitor(self):
        ganti = input("masukkan id_visitor : ")
        for i in self.list_visitor:
            if ganti == i.id_visitor:
                i.setNama()
                i.setAlamat()
                i.setNo_KTP()
                i.setTgl_lahir()
            else :
                print("id tersebut tidak ada di database!")
                self.upd_visitor()

    def add_employee(self):
        nama_emp = input("masukkan nama : ")
        TL_emp = input("masukkan tanggal lahir : ")
        jabatan_emp = input("masukkan jabatan karyawan : ")
        JK_emp = input("masukkan jenis kelamin : ")
        alamat_emp = input("masukkan alamat : ")
        self.list_employee.append(Employee.Employee(nama_emp, TL_emp, jabatan_emp, JK_emp, alamat_emp))
    
    def del_employee(self) :
        hapus = input("masukkan id_employee : ")
        for i in self.list_employee:
            if hapus == i.id_emp:
                self.list_employee.remove(i)
            else :
                print("id yang anda masukkan tidak ada!")
                self.del_employee()

    def upd_employee(self):
        ganti = input("masukkan id_employee : ")
        for i in self.list_employee:
            if ganti == i.id_emp:
                i.setNama()
                i.setTL()
                i.setJabatan()
                i.setJK()
                i.setAlamat()
            else :
                print("id tersebut tidak ada di database!")
                self.upd_employee()

    def book(self):
        room_code = input("Masukkan tipe kamar : (N/VIP/VVIP)")
        room_number = input("Masukkan nomor kamar : ")
        self.room_list.append(Room.Room(room_number, room_code))

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

#bintang = Administrator("bintang", "bintang")
#bintang.add_employee()
#print(bintang.list_employee[0].__dict__)
#bintang.upd_employee()
#print(bintang.list_employee[0].__dict__)
#bintang.del_employee()
#print(bintang.list_employee[0].__dict__)
#bintang.book()
#print(bintang.room_list[0].__dict__)
#bintang.search_room()