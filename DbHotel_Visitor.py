import pymysql
import datetime

class DbHotel_Visitor:
    def __init__(self, db):
        self.conn = pymysql.connect(db)
        self.cur = self.conn.cursor()
        self.cur.execute("CREATE TABLE IF NOT EXISTS Visitor (nama text, id_visitor INTEGER PRIMARY KEY, alamat text, no_ktp text, tanggal_lahir datetime)")
        self.conn.commit()
    
    def fetch(self):
        self.cur.execute("SELECT * FROM Visitor")
        rows = self.cur.fetchall()
        return rows

    def insert(self,nama,id_visitor,alamat,no_ktp,tanggal_lahir):
        self.cur.execute("INSERT INTO Visitor VALUES (NULL, ?, ?, ?, ?, ?)",
        (nama,id_visitor,alamat,no_ktp,tanggal_lahir))
        self.conn.commit()

    def remove(self, id_visitor):
        self.cur.execute("DELETE FROM Visitor WHERE id_visitor=?", (id_visitor,))
        self.conn.commit()

    def update(self,nama,id_visitor,alamat,no_ktp,tanggal_lahir):
        self.cur.execute("UPDATE Users SET nama = ?, id_visitor = ?, alamat = ?, no_ktp = ?, tanggal_lahir = ? WHERE id = ?" , (nama,id_visitor,alamat,no_ktp,tanggal_lahir))
        self.conn.commit()

    def __del__(self):
        self.conn.close()

DbHotel_Visitor.insert("Terrijaki", "EMP001", "9th Avenue", "200000752136", "01020304")
DbHotel_Visitor.fetch()