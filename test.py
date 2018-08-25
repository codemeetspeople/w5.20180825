class Point:
    __slots__ = ['_x', '_y']

    def __init__(self, x=10, y=15):
        self._x = x
        self._y = y

    @property
    def x(self):
        return self._x
    
    @x.setter
    def x(self, value):
        if int(value) < 0:
            raise ValueError()
        self._x = value

point = Point()
print(point.x)
point.x = 42

try:
    point.x = 'ololo'
except ValueError as e:
    print('Got ValueError')

print(point.x)

point.z = 10