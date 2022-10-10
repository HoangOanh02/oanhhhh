class Dog:
    DogCount = 0
    def __init__(self, name, size, age, color,sex):
        self.name = name
        self.size = size
        self.age = age
        self.color = color
        self.sex = sex
    def Go(self, place ):
        print("trẫm đang ngự giá đến {}".format(place))
    def Stay(self, place):
        print("trẫm đang ở   {}".format(place))
    def Lie(self, place):
        print("Trẫm đang sống tại {}".format(place))
    def Bark(self, got):
        print("Trầm ra lệnh {}".format(got))
    def Eat(self, food):
        print(" {}".format(food))
    def G(self):
        print(self.sex)
Mapdit = Dog("Hoàng thượng", "mập địt", 2, "đen thui","ĐỰC RỰA");
Mapdit.Go("CUng điện")
Mapdit.Bark("ĐƯa kiệu cho trẫm")
Mapdit.G()