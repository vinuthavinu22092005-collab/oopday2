class father:
    def __init__(self,surname,name):
        self.surname=surname
        self.father_name=name

    def display_surname(self):
        print("surname is ", self.surname)
    def display_father_name(self):
        print("The fathername is ", self.father_name)

class son(father):
    def __init__(self,name,surname,father_name):
        self.name=name
        super().__init__(surname,father_name)

    def display_name(self):
        print("name is ", self.name)
class daughter(father):
    def __init__(self,name,surname,father_name):
        self.name=name
        super().__init__(surname,father_name)

    def display_name(self):
        print("name is ", self.name)
child_obj=son("john", "K","Rajesh")
child_obj.display_name()
child_obj.display_surname()
child_obj.display_father_name()
daughter_obj=daughter("Jane", "K","Rajesh")
daughter_obj.display_surname()
daughter_obj.display_name()
daughter_obj.display_father_name()
