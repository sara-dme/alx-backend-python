#!/usr/bin/env python3
""" type-annotated function  """


from typing import List


def sum_list(input_list: List[float]) -> float:
    """ return the sum of the float """
    return float(sum(input_list))
