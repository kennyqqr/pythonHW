class pyClass:
    def __init__(self):
        self.x = 1
        self.y = 2
        #constructor
    
    def getX(self):
        return self.x
    def setX(self,x):
        self.x = x
    def getY(self):
        return self.y
    def setY(self,y):
        self.y = y

py = pyClass()

print(py.getX())
py.setX(5)
print(py.getX())
py.x = 7
print(py.getX())
# no need getter/setter
py.x = 9
print(py.x)