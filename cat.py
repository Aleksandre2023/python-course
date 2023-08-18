class Cat:
    name: None
    age: None
    __isHappy: None

    #constructor
    def __init__(self, name, age, isHappy = True):
        self.name = name
        self.age = age
        self.__isHappy = isHappy

    def sound(self):
        print("meow")
        
    def display(self):
        print("*** cat ***")
        print("name:", self.name)
        print("age:", self.age)
        print("happy", self.__isHappy)

    # getter 
    def get_isHappy(self):
        return self.__isHappy        
