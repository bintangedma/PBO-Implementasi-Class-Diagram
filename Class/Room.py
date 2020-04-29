class Room:
    def __init__(self, room_number, room_code):
        self.room_number = room_number
        self.room_code = room_code
  
    def search_room(self, room_number, room_code):
        return room_number
        return room_code
        
    def room_status(self):
        self.room_number
        self.room_code
        
    def getRoom_number(self):
        return self.room_number
    def getRoom_code(self):
        return self.room_code
        
    def setRoom_number(self, baru):
        self.room_number = baru
    def setRoom_code(self, baru):
        self.room_code = baru

class Harga_room:
    def __init__(self, room_number, room_code, harga):
        self.room_number = room_number
        self.room_code = room_code
        self.harga = harga
        self.tanggal = tanggal
        
    def getHarga(self):
        return self.harga
        
    def setHarga(self):
        baru = input("masukkan harga baru : ")
        self.harga = baru