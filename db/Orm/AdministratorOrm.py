from sqlalchemy import Column, String, Integer
from db.base import Base, sessionFactory

class AdministratorOrm(Base):
    __tablename__ = 'Administrator'

    id_admin = Column(String, primary_key=True)
    nama_admin = Column(String, unique=True)
    kode_admin = Column(String)

    def __init__(self, nama_admin, kode_admin):
        self.nama_admin = nama_admin
        self.kode_admin = kode_admin

    @staticmethod
    def showAdmin():
        try:
            session = sessionFactory()
            for admin in session.query(AdministratorOrm).all():
                print(
                    "Nama = {}\n===================="
                        .format(admin.nama_admin))
            session.close()
        except Exception as e:
            print("===>", e)

    def insertAdmin(self):
        try:
            session = sessionFactory()
            adminOrm = AdministratorOrm(self.__nama_admin, self.__kode_admin)
            session.add(adminOrm)
            session.commit()
            session.close()
        except Exception as e:
            print("===>", e)
        else:
            print("Data Berhasil Disimpan!")

    @staticmethod
    def updateAdmin(nama_admin):
        try:
            newNama = input("Masukkan Nama Baru: ")
            newKode = input("Masukkan Kode Baru: ")
            session = sessionFactory()
            session.query(AdministratorOrm).filter_by(id=nama_admin).update({
                AdministratorOrm.nama_admin: newNama, AdministratorOrm.kode_admin: newKode
            }, synchronize_session=False)
            session.commit()
            session.close()
        except Exception as e:
            print("===>", e)
        else:
            print("Data Berhasil DiUpdate!")

    @staticmethod
    def delAdmin(nama_admin):
        try:
            session = sessionFactory()
            session.query(AdministratorOrm).filter_by(id=nama_admin).delete()
            session.commit()
            session.close()
        except Exception as e:
            print("===>", e)
        else:
            print("Data Berhasil Dihapus!")