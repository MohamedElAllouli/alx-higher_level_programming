#!/usr/bin/python3
'''Square class.'''
from models.rectangle import Rectangle


class Square(Rectangle):
    '''Square class.'''

    def __init__(self, size, x=0, y=0, id=None):
        '''Constructor.'''
        super().__init__(size, size, x, y, id)

    def __str__(self):
        '''Returns string info about this square.'''
        return '[{}] ({}) {}/{} - {}'.\
            format(type(self).__name__, self.id, self.x, self.y, self.width)

    @property
    def size(self):
        '''Size of this square.'''
        return self.width

    @size.setter
    def size(self, value):
        """ seter of size """
        self.width = value
        self.height = value

    def update(self, *args, **kwargs):
        """ method update """
        if args is not None and len(args) is not 0:
            listofatr = ['id', 'size', 'x', 'y']
            for i in range(len(args)):
                if listofatr[i] == 'size':
                    setattr(self, 'width', args[i])
                    setattr(self, 'height', args[i])
                else:
                    setattr(self, listofatr[i], args[i])
        else:
            for key, value in kwargs.items():
                if key == 'size':
                    setattr(self, 'width', value)
                    setattr(self, 'height', value)
                else:
                    setattr(self, key, value)

    def to_dictionary(self):
        '''dictionary representation of this class.'''
        return {"id": self.id, "size": self.width,
                "x": self.x, "y": self.y}
