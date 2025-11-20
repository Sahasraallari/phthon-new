class India():
    def capital(self):
        print("New Delhi is capital of India")


def language(self):
    print("Hindi is most widely spoken language of India")


def type(self):
    print("India is developing country")



class USA():
    def capital(self):
        print(" Washington DC is capital of USA")


    def language(self):
        print("English is most primary spoken language of USA")


    def type(self):
        print("USA is developing country")

obj_ind = India()
obj_usa = USA()




for country in (obj_ind, obj_usa):

country.capital()
country.type()
country.language()

























