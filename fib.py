#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Feb  2 15:24:26 2019

@author: nishtha
"""

fib_cache = {}

def fibonacci(n):
    if n in fib_cache:
        return (fib_cache[n])
    if n <= 0:
        value = 0
    elif n == 1:
        value = 1
    else:
        value = fibonacci(n-1) + fibonacci(n-2)
    
    fib_cache[n] = value
    return (value)

for i in range(1000):
    print("for", i, ":", fibonacci(i))