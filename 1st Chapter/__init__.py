#Let discuss about __init__ & self
#What's __init__ in python programming??
# __init__ is a instance class called method.
# Also self is called an object name instancly

class Human():
    def  __init__(self, name, drink, color, age, nationality ):
        self.name = name
        self.drink = drink
        self.color = color
        self.age = age
        self.nationality = nationality
vubon = Human("Vubon", "No Drink", "Yellow","25","Bangladeshi")
print (vubon.name)
print (vubon.drink)
print (vubon.color)
print (vubon.age)
print (vubon.nationality)