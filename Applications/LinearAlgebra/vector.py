# Basic class of a user-defined vector data type
class Vector(object):
    def __init__(self, coordinates):
        try:
            if not coordinates:
                raise ValueError
            self.coordinates = tuple(coordinates)
            self.dimension = len(coordinates)

        except ValueError:
            raise ValueError('The coordinates must be nonempty')

        except TypeError:
            raise TypeError('The coordinates must be an iterable')


    def __str__(self):
        return 'Vector: {}'.format(self.coordinates)


    def __len__(self):          # polymorphism of len function
        return len(self.coordinates)


    def __eq__(self, v):        # polymorphism of equal check operator
        return self.coordinates == v.coordinates