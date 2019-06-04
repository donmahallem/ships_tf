import numpy as np


class Ship:

    def __init__(self):
        self.coords = []

    def has(self, y, x):
        return [y, x] in self.coords

    def setCoords(self, coords):
        self.coords = coords
