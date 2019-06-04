#import tensorflow as tf
import numpy as np
from PIL import Image
import random
DEFAULT_SHIPS = [5, 4, 4, 3, 3, 3, 2, 2, 2, 2]


def cell_available(field,  y, x):
    if field[y, x] != 0:
        return False
    if x > 0 and field[y, x-1] != 0:
        return False
    if x < 9 and field[y, x+1] != 0:
        return False
    if y > 0 and field[y-1, x] != 0:
        return False
    if y < 9 and field[y+1, x] != 0:
        return False
    return True


def location_available(field, ship):
    for coord in ship:
        if not cell_available(field, coord[0], coord[1]):
            return False
    return True


def random_fill_boats(ships):
    field = np.zeros((10, 10))
    for ship in ships:
        direction = np.random.randint(0, 2)
        max_x = 10-ship
        max_y = 10-ship
        if direction == 0:
            # boat is vertical
            max_x = 10
        else:
            max_y = 10
        while True:
            start_x = np.random.randint(0, max_x)
            start_y = np.random.randint(0, max_y)
            cells = 0
            if direction == 0:
                cells = [[x+start_y, start_x] for x in range(ship)]
            else:
                cells = [[start_y, x+start_x] for x in range(ship)]
            print(cells)
            if location_available(field, cells):
                for cell in cells:
                    field[cell[0], cell[1]] = 1
                break
    return field


COORDINATES = [[x % 10, x//10] for x in range(100)]
print(COORDINATES)
# If ships are hit or destroyed


def modify_field(ships):
    shots = random.sample(COORDINATES, np.random.randint(0, 101))
    for shot in range(shots):
        print(shot)


test_field = random_fill_boats(DEFAULT_SHIPS)
print(test_field)
for s in range(20):
    test_field[0:10, 1] = 1
print(test_field)
img = Image.fromarray(test_field, '1')
# img.show()
