import numpy as np


class PointToPointMeter():

    def check(self, o1, o2):
        pass


class MinkovskyMeter(PointToPointMeter):

    def __init__(self, alpha):
        self.alpha = alpha

    def calc(self, o1, o2):
        return \
            (np.abs(o1[0] - o2[0]) ** self.alpha +
             np.abs(o1[1] - o2[1]) ** self.alpha) ** \
            (1 / self.alpha)


class EuclidMeter(PointToPointMeter):

    def calc(self, o1, o2):
        return MinkovskyMeter(2).calc(o1, o2)


class SumabsMeter(PointToPointMeter):

    def calc(self, o1, o2):
        return np.abs(o1[0] - o2[0]) + np.abs(o1[1] - o2[1])


class MinabsMeter(PointToPointMeter):

    def calc(self, o1, o2):
        return np.min([np.abs(o1[0] - o2[0]), np.abs(o1[1] - o2[1])])


class MaxabsMeter(PointToPointMeter):

    def calc(self, o1, o2):
        return np.max([np.abs(o1[0] - o2[0]), np.abs(o1[1] - o2[1])])


class PointToClassMeter():

    def check(self, o1, o2):
        pass


class Centroid(PointToClassMeter):

    def calc(self, o, c, pointToPointMeter):
        centroid = [np.mean(c[:, 0]), np.mean(c[:, 1])]

        return pointToPointMeter.calc(o, centroid)


class Neares(PointToClassMeter):

    def calc(self, o, c, pointToPointMeter):
        lenghts = []

        for element in c:
            lenghts.append(pointToPointMeter.calc(o, element))

        return np.min(lenghts)


class Mean(PointToClassMeter):

    def calc(self, o, c, pointToPointMeter):
        lenghts = []

        for element in c:
            lenghts.append(pointToPointMeter.calc(o, element))

        return np.mean(lenghts)


class Furthest(PointToClassMeter):

    def calc(self, o, c, pointToPointMeter):
        lenghts = []

        for element in c:
            lenghts.append(pointToPointMeter.calc(o, element))

        return np.max(lenghts)


class TwoNeares(PointToClassMeter):

    def calc(self, o, c, pointToPointMeter):
        lenghts = []

        for element in c:
            lenghts.append(pointToPointMeter.calc(o, element))

        nearest1 = np.min(lenghts)

        lenghts.remove(nearest1)

        nearest2 = np.min(lenghts)

        return nearest1 + nearest2
