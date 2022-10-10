class Bird:
    def flihght(self):
        print('Many birds can fly')

class Sparrow(Bird):
    def flihght(self):
        print('Sparrows can fly')

class Ostrich(Bird):
    def flihght(self):
        print('Ostriches cannot fly')

obj1 = Bird()
obj2 = Sparrow()
obj3 = Ostrich()
obj1.flihght()
obj2.flihght()
obj3.flihght()