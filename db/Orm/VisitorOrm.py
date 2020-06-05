from sqlalchemy import Column, String, Integer, Text, Enum
from db.base import Base, sessionFactory
from Class.JenKel import JenKel

class VisitorOrm(Base) :
    __tablename__ = 'Visitor'

    id_visitor = Column(String, primary_key=True)
    nama = Column(String)
    jk = Column(Enum(JenKel))
    alamat = Column(String)
    no_KTP = Column(String, unique=True)
    tanggal_lahir = Column(String)

    jumlahVis = 0
    def __init__(self, id_visitor, nama, jk, alamat, no_KTP, tanggal_lahir):
        #self.id_visitor = str("VIS00")+str(VisitorOrm.jumlahVis)
        self.id_visitor = str("VIS00") + no_KTP
        self.nama = nama
        self.jk = jk
        self.alamat = alamat
        self.no_KTP = no_KTP
        self.tanggal_lahir = tanggal_lahir

    @staticmethod
    def showVisitor():
        try:
            session = sessionFactory()
            for visitor in session.query(VisitorOrm).all():
                print(
                    "Id Visitor = {}\nNama = {}\nAlamat = {}\nJabatan= {}\nJenis Kelamin = {}\nAlamat = {}\n===================="
                        .format(visitor.id_visitor, visitor.nama, visitor.alamat, visitor.no_KTP,
                                visitor.tanggal_lahir))
            session.close()
        except Exception as e:
            print("===>", e)

    def insertVisitor(self):
        try:
            session = sessionFactory()
            visitorOrm = VisitorOrm(self.id_visitor, self.nama, self.jk, self.alamat, self.no_KTP, self.tanggal_lahir)
            session.add(visitorOrm)
            session.commit()
            session.close()
        except Exception as e:
            print("===>", e)
        else:
            print("Data Berhasil Disimpan!")

    @staticmethod
    def updateVisitor(id_visitor):
        try:
            newNama = input("Masukkan Nama Baru: ")
            newAlamat = input("Masukkan Alamat Baru: ")
            newNo_KTP = input("Masukkan Nomor KTP Baru: ")
            newTanggalLahir = input("Masukkan Tanggal Lahir Baru: ")
            session = sessionFactory()
            session.query(VisitorOrm).filter_by(id=id_visitor).update({
                VisitorOrm.nama: newNama, VisitorOrm.alamat: newAlamat,
                VisitorOrm.no_KTP: newNo_KTP, VisitorOrm.tanggal_lahir: newTanggalLahir
            }, synchronize_session=False)
            session.commit()
            session.close()
        except Exception as e:
            print("===>", e)
        else:
            print("Data Berhasil DiUpdate!")

    @staticmethod
    def deleteVisitor(id_visitor):
        try:
            session = sessionFactory()
            session.query(VisitorOrm).filter_by(id=id_visitor).delete()
            session.commit()
            session.close()
        except Exception as e:
            print("===>", e)
        else:
            print("Data Berhasil Dihapus!")