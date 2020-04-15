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
