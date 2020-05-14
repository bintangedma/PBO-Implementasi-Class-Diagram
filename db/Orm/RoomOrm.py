from sqlalchemy import Column, String
from Class.Room import Room
from db.base import Base, sessionFactory

class RoomORM(Base):
    __tablename__ = 'room'

    room_number = Column(String, primary_key=True)
    room_code = Column(String)

    def __init__(self, room_number, room_code):
        self.room_number = room_number
        self.room_code = room_code

    @staticmethod
    def showroom():
        try:
            session = sessionFactory()
            for room in session.query(RoomORM).all():
                print(
                    "Room Number = {}\nRoom Code = {}\n--------------------"
                        .format(room.room_number, room.room_code))
            session.close()
        except Exception as e:
            print("--->", e)

    @staticmethod
    def insertvisitor(room):
        try:
            session = sessionFactory()
            roomORM = RoomORM(room.room_number, room.room_code)
            session.add(roomORM)
            session.commit()
            session.close()
        except Exception as e:
            print("--->", e)
        else:
            print("Data Berhasil Di Simpan")

    @staticmethod
    def roomstatus(room_number) -> bool:
        try:
            session = sessionFactory()
            if((session.query(RoomORM).filter_by(room_number=room_number).count()) == 1):
                return True
            else:
                return False
            session.close()
        except Exception as e:
            print("--->", e)
