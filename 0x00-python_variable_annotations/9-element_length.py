#!/usr/bin/env python3
""" type-annotated function  """


import typing


def element_length(lst: typing.Iterable[typing.Sequence]) -> \
        typing.List[typing.Tuple[typing.Sequence, int]]:
    """ return a list of tuples"""
    return [(i, len(i)) for i in lst]
