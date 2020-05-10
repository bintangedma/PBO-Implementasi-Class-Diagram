import Visitor
import Employee
import Room
#from db.base import Base, sessionFactory

class Administrator : 
    #instance
    def __init__(self, nama_admin, kode_admin):
        self.__nama_admin = nama_admin
        self.__kode_admin = kode_admin
    #method
    def add_visitor(self):
         nama = input("masukkan nama : ")
         alamat = input("masukkan alamat : ")
         no_KTP = input("masukkan no_KTP : ")
         tanggal_lahir = input("masukkan tanggal_lahir : ")
         Visitor.Visitor.list_visitor.append(Visitor.Visitor(nama, alamat, no_KTP, tanggal_lahir))
    
    def del_visitor(self) :
        hapus = input("masukkan id_visitor : ")
        for i in Visitor.Visitor.list_visitor:
            if hapus == i.id_visitor:
                Visitor.Visitor.list_visitor.remove(i)
            else :
                print("id yang anda masukkan tidak ada!")
                self.del_visitor()

    def upd_visitor(self):
        ganti = input("masukkan id_visitor : ")
        for i in Visitor.Visitor.list_visitor:
            if ganti == i.id_visitor:
                i.setNama()
                i.setAlamat()
                i.setNo_KTP()
                i.setTgl_lahir()
            else :
                print("id tersebut tidak ada di database!")
                self.upd_visitor()

    def find_visitor(self):
        pil = input("ingin mencari menggunakan apa? (nama/id) : ")
        if pil == "nama":
            fullname = input("masukkan nama lengkap visitor : ")
            for data in Visitor.Visitor.list_visitor:
                if fullname == data.nama:
                    print("nama visitor\t|\tid visitor\t|\talamat\t\t|\tno ktp\t|\ttanggal lahir\t|\ttagihan\t")
                    print("{}\t{}\t{}\t{}\t{}\t\t\t{}".format(data.nama, data.id_visitor, data.alamat, data.no_KTP, data.tanggal_lahir, data.tagihan))
                else : 
                    print("maaf nama visitor tidak ditemukan, silahkan ulangi")
                    self.find_visitor()
        elif pil == "id":
            id = input("masukkan id visitor : ")
            for data in Visitor.Visitor.list_visitor:
                if id == data.id_visitor:
                    print("nama visitor\t|\tid visitor\t|\talamat\t\t|\tno ktp\t|\ttanggal lahir\t|\ttagihan\t")
                    print("{}\t{}\t{}\t{}\t{}\t\t\t{}".format(data.nama, data.id_visitor, data.alamat, data.no_KTP, data.tanggal_lahir, data.tagihan))
                else : 
                    print("maaf id visitor tidak ditemukan, silahkan ulangi")
                    self.find_visitor()
        else : 
            print("masukkan 'nama' jika ingin mencari menggunakan nama, \nmasukkan 'id' jika ingin mencari menggunakan id >")
            self.find_visitor()

    def add_employee(self):
        nama_emp = input("masukkan nama : ")
        TL_emp = input("masukkan tanggal lahir : ")
        jabatan_emp = input("masukkan jabatan karyawan : ")
        JK_emp = input("masukkan jenis kelamin : ")
        alamat_emp = input("masukkan alamat : ")
        #Employee.Employee.list_employee.append(Employee.Employee(nama_emp, TL_emp, jabatan_emp, JK_emp, alamat_emp))
        if jabatan_emp == "Employee" : 
            Employee.Employee.list_employee.append(Employee.Employee(nama_emp, TL_emp, jabatan_emp, JK_emp, alamat_emp))
        elif jabatan_emp == "Receptionist":
            Employee.Receptionist.list_employee.append(Employee.Receptionist(nama_emp, TL_emp, JK_emp, alamat_emp))
            Employee.Receptionist.list_receptionist.append(Employee.Receptionist(nama_emp, TL_emp, JK_emp, alamat_emp))
        elif jabatan_emp == "Marketing Crew":
            Employee.Marketing_crew.list_employee.append(Employee.Marketing_crew(nama_emp, TL_emp, JK_emp, alamat_emp))
            Employee.Marketing_crew.list_MC.append(Employee.Marketing_crew(nama_emp, TL_emp, JK_emp, alamat_emp))
        elif jabatan_emp == "Cashier":
            Employee.Cashier.list_employee.append(Employee.Cashier(nama_emp, TL_emp, JK_emp, alamat_emp))
            Employee.Cashier.list_cashier.append(Employee.Cashier(nama_emp, TL_emp, JK_emp, alamat_emp))
        else : 
            Employee.Employee.list_employee.append(Employee.Employee(nama_emp, TL_emp, jabatan_emp, JK_emp, alamat_emp))


    def del_employee(self) :
        hapus = input("masukkan id_employee : ")
        for i in Employee.Employee.list_employee:
            if hapus == i.id_emp:
                Employee.Employee.list_employee.remove(i)
                print("data berhasil dihapus!")
            else :
                print("id yang anda masukkan tidak ada!")
                self.del_employee()

    def upd_employee(self):
        ganti = input("masukkan id_employee : ")
        for i in Employee.Employee.list_employee:
            if ganti == i.id_emp:
                i.setNama()
                i.setTL()
                i.setJabatan()
                i.setJK()
                i.setAlamat()
            else :
                print("id tersebut tidak ada di database!")
                self.upd_employee()

    def find_employee(self):
        cari = input("masukkan id employee : ")
        for data in Employee.Employee.list_employee:
            if cari == data.id_emp:
                print("nama employee\t|\tid employee\t|\tTanggal lahir\t\t|\tJabatan \t|\tJenis Kelamin\t|\tAlamat\t")
                print("{}\t\t{}\t\t{}\t\t{}\t\t{}\t\t\t{}".format(data.nama_emp, data.id_emp, data.TL_emp, data.jabatan_emp, data.JK_emp, data.alamat_emp))
            else : 
                print("maaf data tidak ditemukan, silahkan ulangi")
                self.find_employee()

    def book(self):
        room_code = input("Masukkan tipe kamar : (N/VIP/VVIP)")
        room_number = input("Masukkan nomor kamar : ")
        if room_code == "N" or room_code == "VIP" or room_code == "VVIP":
            Room.Room.room_list.append(Room.Room(room_number, room_code))
        else : 
            print("that's not a room code silly, choose one for the room code, capitallized. (N/VIP/VVIP)")
            self.book()

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

#bintang = Administrator("bintang", "bintang")
#bintang.add_employee()
#print(Employee.Employee.list_employee[0].__dict__)
#bintang.find_employee()
#print(Employee.Cashier.list_cashier[0].__dict__)
#bintang.upd_employee()
#print(bintang.list_employee[0].__dict__)
#bintang.del_employee()
#print(bintang.list_employee[0].__dict__)
#bintang.book()
#print(Room.Room.room_list[0].__dict__)
#bintang.search_room()
#bintang.search_room()
#bintang.add_visitor()
#print(Visitor.Visitor.list_visitor[0].__dict__)
#bintang.find_visitor()
#a = Visitor.Visitor.list_visitor[0].__dict__
#print(a)
bintang = Visitor.Visitor("bintang", "asdas", "10101", "91273")
print(Visitor.Visitor.list_visitor[0].__dict__)
rec1 = Employee.Receptionist("bintang", "california", "BOY", "NYC")
rec1.book()
