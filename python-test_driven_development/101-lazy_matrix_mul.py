#!/usr/bin/python3
""" Module that multiplicate two matrix with module Numpy"""
import numpy as np


def lazy_matrix_mul(m_a, m_b):
    """ This function check and mul two matrix"""
    check_int_float_m_a = "m_a should contain only integers or floats"
    check_int_float_m_b = "m_b should contain only integers or floats"

    if type(m_a) != list:
        raise TypeError("m_a must be a list")
    if type(m_b) != list:
        raise TypeError("m_b must be a list")
    if len(m_a) == 0:
        raise ValueError("m_a can't be empty")
    if len(m_b) == 0:
        raise ValueError("m_b can't be empty")

    for col in range(len(m_a)):
        for row in range(len(m_b[col])):
            for pos in range(len(m_a[col])):
                if type(m_a[col][pos]) != int and type(m_a[col][pos]) != float:
                    raise TypeError(check_int_float_m_a)
                if type(m_b[col][pos]) != int and type(m_b[col][pos]) != float:
                    raise TypeError(check_int_float_m_b)
    new = np.dot(m_a, m_b)
    return new
