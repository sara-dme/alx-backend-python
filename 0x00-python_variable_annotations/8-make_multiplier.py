#!/usr/bin/env python3
""" type-annotated function  """


import typing


def make_multiplier(multiplier: float) -> typing.Callable[[float], float]:
    """ return a function that multiples a float """
    def mult(m: float) -> float:
        return m * multiplier
    return mult
