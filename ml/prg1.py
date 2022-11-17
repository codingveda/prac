# -*- coding: utf-8 -*-
"""
Created on Thu Nov 17 06:55:47 2022

@author: VEDANT
"""

def gradient_desecent(func, start, step, itrs, tol=0.01):
    steps = [start]
    x=start
    for i in range(itrs):
        diff = - step*func(x)
        if abs(diff) <= tol:
            break
        x += diff
        steps.append(x)
    return steps, step, x

def cost_function(x):
    return x*x + 6*x + 9

def gradient_function(x):
    return 2*x + 6

history, learning_rate, minima = gradient_desecent(gradient_function, 2, 0.1, 100)

print(history,"\n", learning_rate, "\n", minima, "\n", len(history))