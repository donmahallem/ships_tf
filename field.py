import numpy as np


class Field:
    def __init__(self):
        # layer 1 boat
        # layer 2 hit water
        # layer 3 hit boat
        # layer 4 boat destroyed
        self.field = np.zeros((10, 10, 4))

    def shot(self, y, x):
        self.field[y, x] = 1
