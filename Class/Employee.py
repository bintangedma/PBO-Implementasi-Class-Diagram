#from db.base import Base, sessionFactory
#from db.orm.EmployeeORM import EmployeeORM
import Room
class Employee :
    #Class variable
    jumlahEmp = 0;
    #instance
    def __init__(self, nama_emp, TL_emp, jabatan_emp, JK_emp, alamat_emp):
        self.nama_emp = nama_emp
        self.__id_emp = "EMP"+str(Employee.jumlahEmp+1)
        self.TL_emp = TL_emp
        self.jabatan_emp = jabatan_emp
        self.JK_emp = JK_emp
        self.alamat_emp = alamat_emp
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
        self.setJK = new
    
    def getAlamat(self):
        return self.alamat_emp
    def setAlamat(self):
        new = input("masukkan alamat baru : ")
        self.alamat_emp = new

class Receptionist(Employee):
    jumlahRec = 0
    def __init__(self, nama_emp, TL_emp, JK_emp, alamat_emp):
        super().__init__(nama_emp, TL_emp, "Receptionist", JK_emp, alamat_emp)
        self.room_list = []
        Receptionist.jumlahRec += 1

    def book(self):
        room_code = input("Masukkan tipe kamar : (N/VIP/VVIP)")
        room_number = input("Masukkan nomor kamar : ")
        #id = room_code+room_number
        self.room_list.append(Room.Room(room_number, room_code))
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
    
    def checkOut(self):
        kode = input("Masukkan tipe kamar : (N/VIP/VVIP)")
        cari = input("Masukkan nomor kamar : ")
        id = kode+cari
        for i in self.room_list:
            if id == i.id_room:
                self.room_list.remove(i)
                print("Terima kasih telah berkunjung")
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
        
    def perpanjang_book(self):
        room_code = input("Masukkan tipe kamar : (N/VIP/VVIP)")
        room_number = input("Masukkan nomor kamar : ")
        self.room_list.append(Room.Room(room_number, room_code))

class Marketing_crew(Employee):
    jumlahMC = 0
    def __init__(self, nama_emp, TL_emp, JK_emp, alamat_emp):
        super().__init__(nama_emp, TL_emp, "Marketing Crew", JK_emp, alamat_emp)
        Marketing_crew.jumlahMC += 1

    def laporan(self):
        pass
    
    def upd_harga(self):
        baru = input("masukkan harga baru : ")
        Room.harga = baru

class Cashier(Employee):
    jumlahCashier = 0
    def __init__(self, nama_emp, TL_emp, JK_emp, alamat_emp):
        super().__init__(nama_emp, TL_emp, "Cashier", JK_emp, alamat_emp)
        self.transaksi = []
        Cashier.jumlahCashier += 1


    def receipt(self):
        print("receipt")
        print(self.transaksi)


#johnny = Employee("Johnny Walkerine", "19283", "Supervisor", "male", "Cluster")
#print(johnny.__dict__)

#rec1 = Receptionist("bintang", "california", "BOY", "NYC")
#print(rec1.__dict__)
#rec1.book()
#print(rec1.room_list[0].__dict__)
#rec1.checkOut()
#print(rec1.room_list[0].__dict__)
#rec1.search_room()
#print(rec1.room_list)