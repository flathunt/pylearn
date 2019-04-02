"""
Demo Circle class

Circle objects may be added together or altered with +/*
"""

from math import pi, sqrt


class Circle:
    def __init__(self, radius):
        self._radius = radius

    @property
    def radius(self):
        return self._radius

    @radius.setter
    def radius(self, new_radius):
        self._radius = new_radius

    def increase_radius(self, inc):
        self._radius += inc

    @property
    def area(self):
        return pi * self._radius ** 2

    def __add__(self, other):
        if not isinstance(other, Circle):
            return NotImplemented

        new_radius = sqrt((self._radius + other._radius) / pi)
        return Circle(new_radius)

    def __sub__(self, other):
        if not isinstance(other, Circle):
            return NotImplemented

        if self._radius < other._radius:
            raise ValueError('Circle radius must be >= 0')

        new_radius = sqrt((self._radius - other._radius) / pi)

        return Circle(new_radius)

    def __str__(self):
        return '{:.2f} sized circle'.format(self._radius)

    def __repr__(self):
        return 'Circle({:})'.format(self._radius)

    def __iadd__(self, inc):
        self._radius += inc
        return self

    def __isub__(self, inc):
        self._radius -= inc
        return self

    def __imul__(self, factor):
        self._radius *= factor
        return self

    def __idiv__(self, divisor):
        self._radius *= divisor
        return self
