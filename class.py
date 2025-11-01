class Employee:
    def get_init_(self):
        print('Employee created')

    def _del_(self):
        print("Destructor called")


def Create_obj():
    print('Making object .....')
    obj = Employee()
    print('function end.....')
    return obj



print('Calling Create_obj()   function.....')
obj = Create_obj()
print('Programm End.....')














