class Car:
    def __init__(self, price, power):
        self.price = price
        self.power = power

    def accept(self, visitor):
        return visitor.visit_car(self)

class Flat:
    def __init__(self, price, area):
        self.price = price
        self.area = area

    def accept(self, visitor):
        return visitor.visit_flat(self)

class TaxCalculator:
    def visit_car(self, car):
        return car.price * 0.05 + car.power * 10

    def visit_flat(self, flat):
        return flat.price * 0.03 + flat.area * 20

class PriceWithTax:
    def visit_car(self, car):
        return car.price + (car.price * 0.05 + car.power * 10)

    def visit_flat(self, flat):
        return flat.price + (flat.price * 0.03 + flat.area * 20)

mashina = Car(100000, 150)
kvartira = Flat(500000, 60)
nalog_calc = TaxCalculator()

print(f"Налог на машину: {mashina.accept(nalog_calc)}")
print(f"Налог на квартиру: {kvartira.accept(nalog_calc)}")
