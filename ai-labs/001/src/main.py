import matplotlib.pyplot as plt
import numpy as np

from distance_meter import MinkovskyMeter, Furthest, SumabsMeter
from distance_meter import Centroid

classes = np.array(
    [[[0.05, 0.91],
      [0.14, 0.96],
      [0.16, 0.9],
      [0.07, 0.7],
      [0.2, 0.63]],

     [[0.49, 0.89],
      [0.34, 0.81],
      [0.36, 0.67],
      [0.47, 0.49],
      [0.52, 0.53]],

     [[0.62, 0.83],
      [0.79, 0.92],
      [0.71, 0.92],
      [0.78, 0.83],
      [0.87, 0.92]],

     [[0.55, 0.4],
      [0.66, 0.32],
      [0.74, 0.49],
      [0.89, 0.3],
      [0.77, 0.2]],

     [[0.31, 0.43],
      [0.45, 0.27],
      [0.33, 0.16],
      [0.56, 0.29],
      [0.54, 0.13]],

     [[0.05, 0.15],
      [0.09, 0.39],
      [0.13, 0.51],
      [0.25, 0.34],
      [0.15, 0.36]]])


def user_input():
    while True:
        try:
            x = float(input('enter x value: '))
            y = float(input('enter y value: '))
            return [x, y]
        except ValueError:
            continue

def classify(lens):
    index = lens.index(min(lens))

    return str(index + 1)


new_object = user_input()
print('\n************\n************\n')
print('\nMinkovsky lambda=5, centroid')
lens = [Centroid().calc(new_object, i, MinkovskyMeter(5)) for i in classes]
print(lens)
print('Classified to class ' + classify(lens))

print('\nMinkovsky labmda=5, furthest')
lens = [Furthest().calc(new_object, i, MinkovskyMeter(5)) for i in classes]
print(lens)
print('Classified to class ' + classify(lens))

print('\nSumabs, centroid')
lens = [Centroid().calc(new_object, i, SumabsMeter()) for i in classes]
print(lens)
print('Classified to class ' + classify(lens))

print('\nSumabs, furthest')
lens = [Furthest().calc(new_object, i, SumabsMeter()) for i in classes]
print(lens)
print('Classified to class ' + classify(lens))

for i, class_i in enumerate(classes):
    plt.plot(class_i[:, 0], class_i[:, 1], '*')

plt.legend(['1','2','3','4','5','6'])
plt.plot(new_object[0], new_object[1], 'X', c='000')

plt.show()
