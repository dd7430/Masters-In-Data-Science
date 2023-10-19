class person():
    def __init__(self, name, gender, work, age):
        self.name = name
        self.gender = gender
        self.work = work
        self.age = age
    def show_something(self):
        print(self.name)
        print(self.gender)
        
    def where_work(self):
        print(self.work)
        
    def my_age(self):
        print(self.age)
        
p1= person('virat', 'male', 'batsman', 36)
p1.show_something()
p1.my_age()
