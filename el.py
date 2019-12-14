class LaPinga:
    var_1 = "this is a variable"
    var_2 = 100
    
    def __init__(self, param1, param2):
        self.instance_1 = param1
        self.instance_2 = param2


class SomeClass:
    def create_arr(self):
        self.arr = []

    def insert_to_arr(self, value):
        self.arr.append(value)

class AnotherClass:
    def __init__(self):
        self.arr = []
        
        
    def insert_arr(self, value):
        self.arr.append(value)
