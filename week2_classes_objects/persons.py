person = {}

person["name"] = "andy"
person["age"] = 42
person["height"] = 77

name = "andy"
age = 42
height = 77

having_fun = True


class Person:
    def __init__(self, name, age, height):
        self.name = name
        self.age = age
        self.height = height
        
    def __str__(self):
        return self.name + " is " + str(self.age) + " years old, and " + str(self.height) + " inches tall"
    
    
person1 = Person("andy", 42, 77)
print(person1)
print(person1.name)
print(person1.age)
print(person1.height)

person2 = Person("oliver", 22, 67)
print(person2)
print(person2.name)
print(person2.age)
print(person2.height)

person3 = Person("Reagan", 20, 63)
print(person3)
print(person3.name)
print(person3.age)
print(person3.height)




if __name__ == "main":
    main()
    
    

