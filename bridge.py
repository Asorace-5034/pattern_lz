class Red:
    def fill(self):
        return "Красный"

class Blue:
    def fill(self):
        return "Синий"

class Green:
    def fill(self):
        return "Зелёный"
        
class Circle:
    def __init__(self, color):  
        self.color = color      
    
    def draw(self):
        return f"{self.color.fill()} круг"

class Square:
    def __init__(self, color):
        self.color = color
    
    def draw(self):
        return f"{self.color.fill()} квадрат"

red = Red()
blue = Blue()
circle = Circle(red)
square = Square(blue)
print(circle.draw()) 
print(square.draw()) 

