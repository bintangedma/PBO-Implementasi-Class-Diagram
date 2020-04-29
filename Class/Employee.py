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
        Receptionist.jumlahRec += 1

    def book(self):
        pass
        
    def reservation(self):
        self.room_number = room_number
        self.room_code = room_code
        
    def perpanjang_book(self):
        self.room_code = room_code

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