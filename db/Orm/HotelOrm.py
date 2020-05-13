from sqlalchemy import Column, String, Integer, Text, Enum
from db.base import Base, sessionFactory


class HotelOrm(Base):
    __tablename__ = 'Hotel'

    nama_hotel = Column(String, primary_key=True)
    alamat_hotel = Column(String)
    fasilitas = Column(String)


    def __init__(self, nama_hotel, alamat_hotel):
        self.nama_hotel = nama_hotel
        self.alamat_hotel = alamat_hotel
        self.fasilitas = []

    @staticmethod
    def showHotel():
        try:
            session = sessionFactory()
            for hotel in session.query(HotelOrm).all():
                print(
                    "Nama Hotel = {}\nAlamat Hotel = {}\nFasilitas : {}===================="
                        .format(hotel.nama_hotel, hotel.alamat_hotel, hotel.fasilitas))
            session.close()
        except Exception as e:
            print("===>", e)

    def insertHotel(self):
        try:
            session = sessionFactory()
            HotelOrm = HotelOrm(self.__nama_hotel, self.__alamat_hotel, self.__fasilitas)
            session.add(HotelOrm)
            session.commit()
            session.close()
        except Exception as e:
            print("===>", e)
        else:
            print("Data Berhasil Disimpan!")

    @staticmethod
    def updateHotel(nama_hotel):
        try:
            newNama = input("Masukkan Nama Baru: ")
            newAlamat = input("Masukkkan Alamat Baru")
            session = sessionFactory()
            session.query(HotelOrm).filter_by(id=nama_hotel).update({
                HotelOrm.nama_hotel: newNama, HotelOrm.alamat_hotel: newAlamat
            }, synchronize_session=False)
            session.commit()
            session.close()
        except Exception as e:
            print("===>", e)
        else:
            print("Data Berhasil DiUpdate!")

    @staticmethod
    def deleteHotel(nama_hotel):
        try:
            session = sessionFactory()
            session.query(HotelOrm).filter_by(id=nama_hotel).delete()
            session.commit()
            session.close()
        except Exception as e:
            print("===>", e)
        else:
            print("Data Berhasil Dihapus!")