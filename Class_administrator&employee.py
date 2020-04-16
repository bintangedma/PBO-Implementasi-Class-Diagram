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

#test
johnny = Employee("Johnny Bill", "EM0001", "1-feb-1995", "karyawan", "laki-laki", "Jalan Cempaka putih" )

print(johnny.nama_emp)
print(johnny.info)
print(johnny.__dict__)


print(Employee.getAlamat(johnny))