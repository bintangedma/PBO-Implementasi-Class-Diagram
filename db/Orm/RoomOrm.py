from sqlalchemy import Column, String, Enum
from Class.Room import Room
from Class.RoomCode import RoomCode
from Class.RoomNumber import RoomNumber
from db.base import Base, sessionFactory

class RoomOrm(Base):
    __tablename__ = 'Room'

    id = Column(String, primary_key=True, unique=True)
    room_number = Column(Enum(RoomNumber))
    room_code = Column(Enum(RoomCode))
    status = Column(String)

    def __init__(self, id, room_number, room_code, status):
        self.id = room_code + room_number
        self.room_number = room_number
        self.room_code = room_code
        self.status = str("Occupied")

    @staticmethod
    def showRoom():
        try:
            session = sessionFactory()
            for room in session.query(RoomOrm).all():
                print(
                    "Room Number = {}\nRoom Code = {}\n--------------------"
                        .format(room.room_number, room.room_code))
            session.close()
        except Exception as e:
            print("--->", e)

    def insertRoom(self):
        try:
            session = sessionFactory()
            roomORM = RoomOrm(self.id, self.room_number, self.room_code, self.status)
            session.add(roomORM)
            session.commit()
            session.close()
        except Exception as e:
            print("--->", e)
        else:
            print("Data Berhasil Di Simpan")

    @staticmethod
    def roomStatus(room_number) -> bool:
        try:
            session = sessionFactory()
            if((session.query(RoomOrm).filter_by(room_number=room_number).count()) == 1):
                return True
            else:
                return False
            session.close()
        except Exception as e:
            print("--->", e)
