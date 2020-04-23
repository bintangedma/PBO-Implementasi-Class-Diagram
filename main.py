class User : 
    #instance
    def __init__(self, username, password):
        self.username = username
        self.password = password

    def verifikasi(self):
        pass

class Administrator : 
    #instance
    def __init__(self, nama_admin, kode_admin):
        self.__nama_admin = nama_admin
        self.__kode_admin = kode_admin

    def add_visitor(self, nama, alamat, no_KTP, tanggal_lahir):
        pass
    
    def del_visitor(self, __id_visitor) :
        pass

    def upd_visitor(self, nama, alamat, no_KTP, tanggal_lahir):
        pass

    def add_employee(self, nama_emp, TL_emp, jabatan_emp, JK_emp, alamat_emp):
        pass
    
    def del_employee(self, __id_emp) :
        pass

    def upd_employee(self, nama_emp, TL_emp, jabatan_emp, JK_emp, alamat_emp):
        pass

    def search_room(room_number, room_code):
        pass

    def set_room_status(room_number, room_code):
        pass

    
class Employee(User) :
    #instance
    def __init__(self, nama_emp, id_emp, TL_emp, jabatan_emp, JK_emp, alamat_emp):
        self.nama_emp = nama_emp
        self.__id_emp = id_emp
        self.TL_emp = TL_emp
        self.jabatan_emp = jabatan_emp
        self.JK_emp = JK_emp
        self.alamat_emp = alamat_emp
        #self.info = "name {} : \n\t id_emp: {}\n\t jabatan: {}".format(self.nama_emp, self.__id_emp, self.jabatan_emp)

    def getNama(self):
        return self.nama_emp
    def setNama(self, new) :
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
    def id_emp(self, new):
        self.__id_emp = new

    def getTL(self):
        return self.TL_emp
    def setTL(self,new):
        self.TL_emp = new

    def getJabatan(self):
        return self.jabatan_emp
    def setJabatan(self, new):
        self.jabatan_emp = new

    def getJK(self):
        return self.JK_emp
    def setJK(self,new):
        self.setJK = new
    
    def getAlamat(self):
        return self.alamat_emp
    def setAlamat(self, new):
        self.alamat_emp = new

class harga_room:
  def __init__(self, room_number, room_code, harga, tanggal):
    self.room_number = room_number
    self.room_code = room_code
    self.harga = harga
    self.tanggal = tanggal
    
  def getHarga(self):
    return self.harga
    
  def setHarga(self, baru):
    self.harga = baru
      
class receptionist(Employee):
  def __init__(self,id_emp, time):
      employee.__init__(self, id_emp)
      self.time = time
    
  def book(self):
    pass
    
  def reservation(self):
    self.room_number = room_number
    self.room_code = room_code
    
  def perpanjang_book(self):
    self.room_code = room_code
    self.no_KTP = no_KTP
    
class room:
  def __init__(self, room_number, room_code):
      self.room_number = room_number
      self.room_code = room_code
  
  def search_room(room_number, room_code):
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

class user:
    def __init__(self, username, password):
        self.username = username
        self.password = password

    def verifikasi(self):
        pass

class marketing_crew(Employee):
    def __init__(self, id_emp):
        self.id_emp = id_emp
    def laporan(self):
        self.laporan = laporan
    def upd_harga(self, baru):
        self.harga = baru

class cashier (Employee):
    def __init__(self, id_emp, time, transaksi):
        self.id_emp = id_emp
        self.time = time
        self.transaksi = transaksi
    def receipt(self):
        self.receipt = receipt
    def getTransaksi(self):
        return self.transaksi
    def setTransaksi(self, baru):
        self.transaksi = baru

class login:
    pass

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
            
    def getNama(self):
        return self.nama
    def getId_visitor(self):
        return self.__id_visitor
    def getAlamat(self):
        return self.alamat
    def getNo_KTP(self):
        return self.no_KTP
    def getTgl_lahir(self):
        return self.tanggal_lahir

    def setNama(self, baru):
        self.nama = baru
    def setId_visitor(self, baru):
        self.__id_visitor = baru
    def setAlamat(self, baru):
        self.alamat = baru
    def setNo_KTP(self, baru):
        self.no_KTP = baru
    def setTgl_lahir(self, baru):
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