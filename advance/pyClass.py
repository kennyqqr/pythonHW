class pyClass:
    def __init__(this):
        this.x = 1
        this.y = 2
        #constructor
    
    def getX(this):
        return this.x
    def setX(this,x):
        this.x = x
    def getY(this):
        return this.y
    def setY(this,y):
        this.y = y

def callClass():
    py = pyClass()
    print(py.getX())
    py.setX(5)
    print(py.getX())
    py.x = 7
    print(py.getX())
    # no need getter/setter
    py.x = 9
    print(py.x)