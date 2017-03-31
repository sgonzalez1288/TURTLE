def tear(t):
    for times in range(10):
        t.circle(times * 2)
        t.left(10)
        t.forward(10)
        
def L(t,distance,angle):
    t.forward(distance)
    t.left(angle)
    t.forward(distance)
    

def fillpolygon(t, sides, distance):
    angle = 360 / sides
    t.begin_fill()
    for times in range(sides):
        t.forward(distance)
        t.left(angle)
    t.end_fill()

def cool(t):
    t.color("black")
    polygon(t,4,100)
    t.color("orange")
    polygon(t,3,100)

def coolsquare(t): 
    for times in range(4):
        cool(t)
        t.left(90)

def jump(t,x,y):
    t.pu()
    t.goto(x,y)
    t.pd()

def fillcircle(t,x):
    t.width(0)
    t.begin_fill()
    t.circle(x)
    t.end_fill()

def dumbell(t,size):
    t.width(10)
    t.begin_fill()
    t.circle(size/2)
    t.forward(size*2)
    t.left(180)
    t.circle(size/2)
    t.end_fill()

def polygon(t, sides, distance):
    angle = 360 / sides
    for times in range(sides):
        t.forward(distance)
        t.left(angle)    
def star(t,size):
    angle = 120
    for side in range(5):
        t.forward(size)
        t.right(angle)
        t.forward(size)
        t.right(72 - angle)


    








    
