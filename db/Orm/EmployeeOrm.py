from sqlalchemy import Column, String, Integer, Text, Enum
from db.base import Base, sessionFactory

class EmployeeOrm(Base):
    __tablename__ = 'Employee'

    id_emp = Column(integer, primary_key=True)
    nama_emp = Column(String)
    TL_emp = Column(String)
    jabatan_emp = Column(String)
    JK_emp = Column(String)
    alamat_emp = Column(String)

    def __init__(self, nama_emp, TL_emp, jabatan_emp, JK_emp, alamat_emp):
        self.nama_emp = nama_emp
        self.TL_emp = TL_emp
        self.jabatan_emp = jabatan_emp
        self.JK_emp = JK_emp
        self.alamat_emp = alamat_emp

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
            apotekerOrm = EmployeeOrm(self.__nama_emp, self.__TL_emp, self.__jabatan_emp, self.__JK_emp, self.__alamat_emp)
            session.add(employeeOrm)
            session.commit()
            session.close()
        except Exception as e:
            print("===>", e)
        else:
            print("Data Berhasil Disimpan!")

    @staticmethod
    def updateApoteker(id_emp):
        try:
            newNama = input("Masukkan Nama Baru: ")
            newTL = input("Masukkan Tanggal Lahir Baru: ")
            newJabatan = input("Masukkan Jabatan Baru: ")
            newJK = input("Masukkan Jenis Kelamin Baru: ")
            newAlamat = input("Masukkkan Spesialis Baru")
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