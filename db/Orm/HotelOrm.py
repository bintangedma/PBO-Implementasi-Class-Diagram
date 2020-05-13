from sqlalchemy import Column, String, Integer, Text, Enum
from db.base import Base, sessionFactory


class HotelOrm(Base):
    __tablename__ = 'Hotel'

    nama_hotel = Column(String, primary_key=True)
    alamat_hotel = Column(String)


    def __init__(self, nama_hotel, alamat_hotel):
        self.nama_hotel = nama_hotel
        self.alamat_hotel = alamat_hotel

    @staticmethod
    def showHotel():
        try:
            session = sessionFactory()
            for hotel in session.query(HotelOrm).all():
                for fas in hotel.fasilitas :
                print(
                    "Nama Hotel = {}\nAlamat Hotel = {}\nFasilitas : {}===================="
                        .format(hotel.nama_hotel, hotel.alamat_hotel, hotel.fasilitas))
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