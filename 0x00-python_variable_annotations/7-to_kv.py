#!/usr/bin/env python3
""" type-annotated function  """


import typing


def to_kv(k: str, v: typing.Union[int, float]) -> typing.Tuple[str, float]:
    """ return a tuple of the str and square of the float """
    return (k, float(v * v))
