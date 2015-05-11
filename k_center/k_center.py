# -*- coding: utf-8 -*-
# CREATED ON DATE: 11.05.15
__author__ = 'mail@pythonic.ninja'

import random
from collections import namedtuple

from helpers.point import Point


PointWihDist = namedtuple('PointWithDist', ['x', 'y', 'dist'], verbose=False)


class KCenter(object):

    def __init__(self, points):
        self.points = points

        for p1 in self.points:
            for p2 in self.points:
                if p1 != p2:
                    p1.distances[p2] = p1.dist(p2)

    def furtherst_first(self, k, start_location=None):
        if start_location is None:
            s = random.choice(self.points)
        else:
            s = start_location
        locations = [s]

        for i in range(2, k+2):
            min_distance = []
            for point in self.points:
                distances = []
                for s in locations:
                    if s is not point:
                        distances.append(PointWihDist(point.x, point.y, point.dist(s)))
                if distances:
                    min_distance.append(min(distances, key=lambda point_with_dist: point_with_dist.dist))
            locations.append(max(min_distance,  key=lambda point_with_dist: point_with_dist.dist))

        return locations

if __name__ == '__main__':
    points = [
        Point(1, 1),
        Point(2, 3),
        Point(2, -2),
        Point(-2, -1),
        Point(-2, -3),
        Point(-2, 2),
        Point(-4, 1),
    ]
    k_center = KCenter(points)
    print k_center.furtherst_first(3, start_location=points[0])