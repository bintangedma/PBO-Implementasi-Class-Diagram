import main

#Test memasukkan data Employee & Visitor dan memanggil nama masing masing
#johnny = main.Employee("Johnny Walkerine", "10101", "01-02-1990", "Receptionist", "Male", "Wall Street 9th Avenue")
#terry = main.Visitor("Terrijaki", "EMP001", "9th Avenue", "200000752136", "01020304")
#print(johnny.nama_emp)
#print(terry.nama)

#test login
#bintang = main.User("bintang", "bintang")
#bintang.askUser()

#test admin
#terry = main.Visitor("Terrijaki", "EMP001", "9th Avenue", "200000752136", "01020304")
#print(terry.__dict__)

#benny = main.Visitor("Benny", "VIS002", "wall street", "200000752133", "01020301")
bintang = main.Administrator("bintang", "bintang")
#print(type(bintang))
#print(type(benny))
#bintang.add_visitor()
bintang.add_employee()
#print(type(benny)) 

#a = bintang.list_visitor[0].nama
#print(a)
#print(bintang.list_visitor[0].__dict__)
print(bintang.list_employee[0].__dict__)
#print(benny.nama)
#print(benny.__dict__)

#print(terry.__dict__)
#bintang.del_employee()
bintang.upd_employee()
#bintang.upd_visitor()

#print(bintang.list_visitor[0].__dict__)
print(bintang.list_employee[0].__dict__)