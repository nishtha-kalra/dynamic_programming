#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Feb  2 16:08:56 2019

@author: nishtha
"""


def power(n):
    if n == 1:
        return (2)
    else:
        return (2 * power(n-1))

print(power(100))