import time
import datetime
from pymysql import *
import Administrator
import Employee
import Hotel
import Room
import User
import Visitor

bintang = Administrator("bintang", "bintang")

bintang.add_employee()

print(bintang.list_employee[0].__dict__)