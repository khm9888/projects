# import math

# class Print2D:
#     def __init__(self,x,y):
#         self.x = x
#         self.y = y
    
    
# p1 = Print2D(30,20)
# p2 = Print2D(60,50)

# print(p1.x, p1.y)
# print(p2.x, p2.y)

# a = p1.x - p2.x
# b = p1.y - p2.y

# c = math.sqrt(a**2+b**2)

# print(c)

#################################

# class Rectangle:
#     def __init__(self,x1,y1,x2,y2):
#         self.x1 = x1
#         self.y1 = y1
#         self.x2 = x2
#         self.y2 = y2
        
# rect = Rectangle(x1=20, y1=20, x2=40, y2=30)

# area = abs(rect.x1-rect.x2)*abs(rect.y1-rect.y2)

# print(area)

##################################

import math
 
class Point2D:
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y
 
length = 0.0
p = [Point2D(), Point2D(), Point2D(), Point2D()]
p[0].x, p[0].y, p[1].x, p[1].y, p[2].x, p[2].y, p[3].x, p[3].y = map(int, input().split())

for i, point in enumerate(p):
    if i == 0 :
        continue
    b_x = p[i-1].x
    b_y = p[i-1].y
    x = point.x
    y = point.y
    
    length += ((b_x-x)**2+(b_y-y)**2)**0.5
    # print(i,b_x,b_y,x,y)
    # print(length)
    
print(length)


    
    
    
    