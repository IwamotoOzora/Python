class Vehicle:
    def __init__(self, name, tool, way):
        self.name = name
        self.tool = tool
        self.way = way
    
    def move(self):
        print(self.name + "は" + self.tool + "を" + self.way + "と動きます")

class Car(Vehicle):
    pass

class Bicycle(Vehicle):
    pass

class Ship(Vehicle):
    pass

class Airplane(Vehicle):
    pass

car = Car("自動車", "アクセル", "踏む")
car.move()
    
bicycle = Bicycle("自転車", "ペダル", "漕ぐ")
bicycle.move()

ship = Ship("船", "スクリュー", "回す")
ship.move()

airplane = Airplane("飛行機", "プロペラ", "回す")
airplane.move()