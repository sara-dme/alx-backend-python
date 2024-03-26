#!/usr/bin/env python3
""" type-annotated function  """


import typing


def sum_mixed_list(mxd_lst: typing.List[typing.Union[int, float]) -> float:
    """ return the sum of the float """
    return float(sum(mxd_lst))
