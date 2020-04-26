import time

class User : 
    #instance
    def __init__(self, username, password):
        self.username = username
        self.password = password
    #method
    def GetUsername(self):
        return username
    def SetUsername(self, new):
        self.username = new

    def SetPassword(self,new):
        self.password = new

    def verifikasi(self, use, pwd):
        if use == (self.username) and pwd == (self.password) :
            self.login()
        else:
            print ("Username dan/atau password yang anda masukkan salah")
            self.askUser()

    def askUser(self):
        username = input("username : ")
        password = input("password : ")
        self.verifikasi(username, password)

    def login(self):
        print("Anda telah berhasil masuk!")
        print("Selamat datang "+self.username)
        self.askCom()

    def askCom(self):
        command = input("Apa yang ingin anda lakukan? ")
        if command == "Keluar" or command == "Log off":
            username = ""
            password = ""
            print("you have logged off")
            self.askUser()
        else:
            print("Unknown command")
            self.askCom()



        
class Administrator : 
    #instance
    def __init__(self, nama_admin, kode_admin):
        self.__nama_admin = nama_admin
        self.__kode_admin = kode_admin
        self.list_visitor = []
        self.list_employee = []
    #method
    def add_visitor(self):
         nama = input("masukkan nama : ")
         id_visitor = input("masukkan id_visitor : ")
         alamat = input("masukkan alamat : ")
         no_KTP = input("masukkan no_KTP : ")
         tanggal_lahir = input("masukkan tanggal_lahir : ")
         self.list_visitor.append(Visitor(nama, id_visitor, alamat, no_KTP, tanggal_lahir))
    
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
        id_emp = input("masukkan id : ")
        TL_emp = input("masukkan tanggal lahir : ")
        jabatan_emp = input("masukkan jabatan karyawan : ")
        JK_emp = input("masukkan jenis kelamin : ")
        alamat_emp = input("masukkan alamat : ")
        self.list_employee.append(Employee(nama_emp, id_emp, TL_emp, jabatan_emp, JK_emp, alamat_emp))
    
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

    def search_room(room_number, room_code):
        pass

    def set_room_status(room_number, room_code):
        pass

    
class Employee() :
    #instance
    def __init__(self, nama_emp, id_emp, TL_emp, jabatan_emp, JK_emp, alamat_emp):
        self.nama_emp = nama_emp
        self.__id_emp = id_emp
        self.TL_emp = TL_emp
        self.jabatan_emp = jabatan_emp
        self.JK_emp = JK_emp
        self.alamat_emp = alamat_emp
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

class harga_room:
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
      
class Receptionist(Employee):
  def __init__(self):
      super().__init__(nama_emp, id_emp, TL_emp, jabatan_emp, JK_emp, alamat_emp)
      self.time = time.localtime(time.time())
    
  def book(self):
    pass
    
  def reservation(self):
    self.room_number = room_number
    self.room_code = room_code
    
  def perpanjang_book(self):
    self.room_code = room_code
    
class Room:
  def __init__(self, room_number, room_code):
      self.room_number = room_number
      self.room_code = room_code
  
  def search_room(self, room_number, room_code):
      return room_number
      return room_code
    
  def room_status(self):
      self.room_number
      self.room_code
    
  def getRoom_number(self):
      return self.room_number
  def getRoom_code(self):
      return self.room_code
    
  def setRoom_number(self, baru):
    self.room_number = baru
  def setRoom_code(self, baru):
    self.room_code = baru

class Marketing_crew(Employee):
    def __init__(self):
        super().__init__(nama_emp, id_emp, TL_emp, jabatan_emp, JK_emp, alamat_emp)

    def laporan(self):
        pass
    
    def upd_harga(self):
        baru = input("masukkan harga baru : ")
        self.harga = baru

class Cashier(Employee):
    def __init__(self):
        super().__init__(nama_emp, id_emp, TL_emp, jabatan_emp, JK_emp, alamat_emp)
        self.id_emp = id_emp
        self.time = time
        self.transaksi = []

    def receipt(self):
        print("receipt")
        print(self.transaksi)


class login:
    def __init__(self, time):
        self.time = time

class Visitor:
    def __init__(self, nama, id_visitor, alamat, no_KTP, tanggal_lahir):
        self.nama = nama
        self.__id_visitor = id_visitor
        self.alamat = alamat
        self.no_KTP = no_KTP
        self.tanggal_lahir = tanggal_lahir

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



class Hotel:
    def __init__(self, nama_hotel, alamat, fasilitas):
        self.nama = nama_hotel
        self.alamat = alamat
        self.fasilitas = fasilitas
    
    def getNama_hotel(self):
        return self.nama_hotel
    def getAlamat(self):
        return self.alamat
    def getFasilitas(self):
        return self.fasilitas
    
    def setNama_hotel(self, baru):
        self.nama_hotel = baru
    def setAlamat(self):
        self.alamat = baru
    def setFasilitas(self):
        self.fasilitas = baru