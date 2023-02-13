from turtle import *

def polygon(side , dis):
    for i in range(side):
        fd(dis)
        lt(360/side)
        
# 1 polygon(3, 100)

# 2 polygon(4, 100)
#polygon(5, 100)
#polygon(6, 100)
#polygon(7, 100)
#polygon(8, 100)
#polygon(9, 100)


# 3 for i in range(3 , 11):
   # polygon(i, 100)

# 4 for i in range (3, 11):
 # polygon(i, 100)

# 5 for i in range(3, 100):
    #polygon(3, i*10)
    #fd(20)

hideturtle()
mainloop()
