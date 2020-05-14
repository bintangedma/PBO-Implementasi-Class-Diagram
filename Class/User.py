from db.Orm.UserOrm import UserOrm
from db.base import sessionFactory
from Class.Authority import Authority

class User : 
    #instance
    def __init__(self, username, password, Authority):
        self.username = username
        self.password = password
        self.authority = Authority

    #method
    def GetAuthority(self):
        return self.authority
    def GetUsername(self):
        return self.username

    def SetUsername(self, new):
        new = input("masukkan username baru : ")
        self.username = new
    def SetPassword(self,new):
        self.password = new

    def verifikasi(self, use, pwd):
        if use == (self.username) and pwd == (self.password) :
            self.login()
        else:
            print ("Username dan/atau password yang anda masukkan salah")
            self.askUser()

    def askUser(self):
        username = input("username : ")
        password = input("password : ")
        self.verifikasi(username, password)

    def login(self):
        print("Anda telah berhasil masuk!")
        print("Selamat datang "+self.username)
        self.askCom()

    def askCom(self):
        command = input("Apa yang ingin anda lakukan? ")
        if command == "Keluar" or command == "Log off":
            username = ""
            password = ""
            print("you have logged off")
            self.askUser()
        else:
            print("Unknown command")
            self.askCom()

#bin = User("bintang", "bintang")
#bin.askUser()