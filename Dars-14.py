'''
14/1
class user:
    def __init__(self, ism, familiya, yosh, email):
        self.ism = ism
        self.familiya = familiya
        self.yosh = yosh
        self.email = email
user_1 = user("Ibroxm", "Ziyovuddinov", 19, "mutalovv@internet.ru")
user_2 = user("Ismoil", "Ziyovuddinov", 16, "ismoil12211@gmail.com")

print(user_1.ism, user_1.familiya, user_1.yosh, user_1.email)
print(user_2.ism, user_2.familiya, user_2.yosh, user_2.email)
'''

'''
14/2
class info:
    def __init__(self,ism, familiya, t_yil, manzil, email):
        self.ism = ism
        self.familiya = familiya
        self.t_yil = t_yil
        self.manzil = manzil
        self.email = email
    def get_info(self):
        return f"Ismim {self.ism} familiyam {self.familiya} tugilgan yilim {self.t_yil} manzilim {self.manzil} emailm {self.email}"
info_1 = info("Ibroxm", "Ziyovuddinov", 2004, "Chilonzor", "redmi5plus787@gmail.com" )
print(info_1.get_info())
'''

'''
14/3
class Talaba:
    def __init__(self, ism, familiya, o_ism, t_yil, manzil, ):
        self.ism = ism
        self.familiya = familiya
        self.o_ism = o_ism
        self.t_yil = t_yil
        self.manzil = manzil
    def get_fullname(self):
        return f"Ismim {self.ism} familiyam {self.familiya} {self.o_ism} ogli"
    def get_loc(self):
        return f"Mening manzilim {self.manzil} tumani"
    def get_yosh(self):
        return f"Tugilgan yilim {self.t_yil}"
talaba = Talaba("Ibroxm", "Ziyovuddinov", 'Qahramonovich', 2004, "Chilonzor")
print(talaba.get_fullname())
print(talaba.get_loc())
print(talaba.get_yosh())
'''

'''
class Talaba:
    def __init__(self, ism, familiya, o_ism, t_yil, manzil, telefon ):
        self.ism = ism
        self.familiya = familiya
        self.o_ism = o_ism
        self.t_yil = t_yil
        self.manzil = manzil
        self.telefon = telefon
    def get_fullname(self):
        return f"Mening ismim {self.ism} familiyam {self.familiya}"
    def get_o(self):
        return f"{self.o_ism} ogli"
    def get_loc(self):
        return f"Mening manzilim {self.manzil} tumani"
    def get_yosh(self):
        return f"Tugilgan yilim {self.t_yil}"
    def get_phone(self):
        return f"{self.telefon} mening telefon raqamim"
talaba = Talaba("Ibroxm", "Ziyovuddinov", "Qahramon", 2004, "Chilonzor", 901671701)
print(talaba.get_fullname())
print(talaba.get_o())
print(talaba.get_loc())
print(talaba.get_yosh())
print(talaba.get_phone())
'''