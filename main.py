from single import Singleton
from bridge import Red, Blue, Circle, Square
from visitor import Car, Flat, TaxCalculator, PriceWithTax

def main():
    #  Задание 1  
    s1 = Singleton()
    s2 = Singleton()
    print("--- Задание 1 ---")
    a = int(input("На сколько изменить volume: "))
    print("--- Меняем громкость ---")
    s1.Change_volume("volume", a)
    print(f"Текущие настройки в s2: {s2.get_config()}")

    print("--- Задание 2 ---")
    krasniy = Red()
    siniy = Blue()
    krug = Circle(krasniy)
    kvadrat = Square(siniy)

    print(krug.draw())
    print(kvadrat.draw())

    #  Задание 3  
    print("--- Задание 3 ---")
    mashina2 = Car(150000, 200)
    kvartira2 = Flat(800000, 80)
    
    nalog_visitor = TaxCalculator()
    itogo_visitor = PriceWithTax()
    
    print(f"Налог на машину 2: {mashina2.accept(nalog_visitor)}")
    print(f"Налог на квартиру 2: {kvartira2.accept(nalog_visitor)}")
    print(f"Итоговая стоимость машины 2 с налогом: {mashina2.accept(itogo_visitor)}")
    print(f"Итоговая стоимость квартиры 2 с налогом: {kvartira2.accept(itogo_visitor)}")

if __name__ == "__main__":
    main()
