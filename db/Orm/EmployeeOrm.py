from sqlalchemy import Column, String, Integer, Enum
from db.base import Base, sessionFactory
from Class.JenKel import JenKel
from Class.Emptype import Emptype

class EmployeeOrm(Base):
    __tablename__ = 'Employee'

    id_emp = Column(String, primary_key=True)
    nama_emp = Column(String, unique=True)
    TL_emp = Column(String)
    jabatan_emp = Column(Enum(Emptype))
    JK_emp = Column(Enum(JenKel))
    alamat_emp = Column(String)

    jumlahEmp = 0
    def __init__(self, id_emp, nama_emp, TL_emp, jabatan_emp, JK_emp, alamat_emp):
        #self.id_emp = str("EMP00") + str(EmployeeOrm.jumlahEmp)
        self.id_emp = str("EMP00") + nama_emp + TL_emp
        self.nama_emp = nama_emp
        self.TL_emp = TL_emp
        self.jabatan_emp = jabatan_emp
        self.JK_emp = JK_emp
        self.alamat_emp = alamat_emp
        EmployeeOrm.jumlahEmp+=1

    @staticmethod
    def showEmployee():
        try:
            session = sessionFactory()
            for employee in session.query(EmployeeOrm).all():
                print(
                    "Id Karyawan = {}\nNama = {}\nTanggal Lahir = {}\nJabatan= {}\nJenis Kelamin = {}\nAlamat = {}\n===================="
                        .format(employee.id_emp, employee.nama_emp, employee.TL_emp, employee.jabatan_emp,
                                employee.JK_emp, employee.alamat_emp))
            session.close()
        except Exception as e:
            print("===>", e)

    def insertEmployee(self):
        try:
            session = sessionFactory()
            employeeOrm = EmployeeOrm(self.id_emp, self.nama_emp, self.TL_emp, self.jabatan_emp, self.JK_emp, self.alamat_emp)
            session.add(employeeOrm)
            session.commit()
            session.close()
        except Exception as e:
            print("===>", e)
        else:
            print("Data Berhasil Disimpan!")

    @staticmethod
    def updateEmployee(id_emp):
        try:
            newNama = input("Masukkan Nama Baru: ")
            newTL = input("Masukkan Tanggal Lahir Baru: ")
            newJabatan = input("Masukkan Jabatan Baru: ")
            newJK = input("Masukkan Jenis Kelamin Baru: ")
            newAlamat = input("Masukkkan Alamat Baru")
            session = sessionFactory()
            session.query(EmployeeOrm).filter_by(id=id_emp).update({
                EmployeeOrm.nama_emp: newNama, EmployeeOrm.TL_emp: newTL,
                EmployeeOrm.JK_emp: newJK, EmployeeOrm.alamat_emp: newAlamat
            }, synchronize_session=False)
            session.commit()
            session.close()
        except Exception as e:
            print("===>", e)
        else:
            print("Data Berhasil DiUpdate!")

    @staticmethod
    def deleteEmployee(id_emp):
        try:
            session = sessionFactory()
            session.query(EmployeeOrm).filter_by(id=id_emp).delete()
            session.commit()
            session.close()
        except Exception as e:
            print("===>", e)
        else:
            print("Data Berhasil Dihapus!")