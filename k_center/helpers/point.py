# -*- coding: utf-8 -*-
# CREATED ON DATE: 11.05.15
__author__ = 'mail@pythonic.ninja'

from math import sqrt, atan2, degrees, pi


class Point(object):
    """
    Class of point which consists of x,y
    >>> Point(x=0, y=0).x
    0
    >>> Point(x=0, y=0).y
    0
    >>> Point(x=1, y=3).x + Point(x=1, y=3).y
    4
    >>> Point(x=0, y=0).y + Point(x=0, y=0).y
    0
    """

    def __init__(self, x=0, y=0):
        """
        >>> p = Point(0,0)
        >>> p.x
        0
        >>> p.y
        0
        """
        self.x = x
        self.y = y
        self.distances = dict()

    def dist(self, p):
        """
        return the Euclidian distance between self and p
        >>> p1 = Point()
        >>> p2 = Point(1,1)
        >>> p1.dist(p2)
        1.4142135623730951
        """
        dx = self.x - p.x
        dy = self.y - p.y
        return sqrt(dx*dx + dy*dy)

    def angle(self, p):
        """
        >>> p1 = Point(0,0)
        >>> p2 = Point(1,1)
        >>> p1.angle(p2)
        45.0
        :return: angle between self and p
        """
        dx = p.x - self.x
        dy = p.y - self.y
        rads = atan2(dy, dx)
        rads %= 2*pi
        return degrees(rads)

    def angle_tree_points(self, p2, p3):
        rads = atan2(p2.y - self.y, p2.x - self.x) - atan2(p3.y - self.y, p3.x - self.x)
        rads %= 2*pi
        out = degrees(rads)
        print out
        return out

    def reset(self):
        """
        >>> p1 = Point(1,1)
        >>> p1.reset()
        >>> p1.x
        0
        >>> p1.y
        0
        """
        self.x = 0
        self.y = 0

    def __add__(self, p):
        """
        return a new point found by adding self and p. This method is
        called by e.g. p+q for points p and q
        >>> p1 = Point(1,1)
        >>> p2 = Point()
        >>> (p1 + p2).x
        1
        >>> (p1 + p2).y
        1
        """
        return Point(self.x+p.x, self.y+p.y)

    def __repr__(self):
        """
        return a string representation of this point. This method is
        called by the repr() function, and
        also the str() function. It should produce a string that, when
        evaluated, returns a point with the
        same data.
        >>> Point(0,1).__repr__()
        'Point(0,1)'
        """
        return 'Point(%d,%d)' % (self.x, self.y)