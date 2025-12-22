
class Shape:
    def __init__(self,color,is_filled):
        self.color = color
        self.is_filled = is_filled


class Circles:
    def __init__(self,color,is_filled,radius):
        super.__init__(color,is_filled)
        self.radius = radius


class square:
    def __init__(self,color,is_filled,width):
        super.__init__(color,is_filled)
        self.radius = width

class triangle:
    def __init__(self,color,is_filled,width,height):
        self.height = height
        super.__init__(color,is_filled)
        self.radius = width

circles = Circles(color="Blue",is_filled=True,radius=10)

print(circles.color)