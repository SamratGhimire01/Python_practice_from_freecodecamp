import math
class Rectangle:
    def __init__(self,width,height):
        self.width = width
        self.height = height
    
    def set_width(self,width):
        self.width=width
    def set_height(self,height):
        self.height=height
    def get_area(self):
        return self.width * self.height
    def get_perimeter(self):
        return 2*(self.width+self.height)
    def get_diagonal(self):
        return math.sqrt((self.width**2)+(self.height**2))
    
    def __str__(self):
        return f"Rectangle(width={self.width}, height={self.height})"

    def get_picture(self):
        if self.width > 50 or self.height > 50:
            return "Too big for picture."
        line = self.width*('*')+'\n'
        result =self.height *line
        return result
        
        
    def get_amount_inside(self,shape):
        h=self.width // shape.width
        v=self.height // shape.height
        return h*v

class Square(Rectangle):
    def __init__(self,length):
        super().__init__(length,length)
    
    def set_side(self,length):
        self.width=length
        self.height=length 

    def set_width(self,width):
        self.set_side(width)
    
    def set_height(self,height):
        self.set_side(height)
    def __str__(self):
        return f"Square(side={self.height})"
    
    
    
    

r=Rectangle(10,5)
a=r.get_area()
s=Square(4)
print(r)
print(r.get_picture())
print(s.get_perimeter())
r.set_height(8)
r.set_width(16)
print(r.get_amount_inside(s))