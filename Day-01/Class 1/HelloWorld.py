#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed May 30 17:13:44 2018

@author: aidantollefson
"""
#^^^that thing between triple quotes is called a doc(k?) string.


age = 20

print("aidan")

print(age)

#keywords: any word that python already knows about

def square_it(number):
    """ square and number
    
    Parameters
    __________
    number : float
        the number to square
        
    Returns
    _______
    float
        the square input number
    """
    #indentation means you are still in that function
    return number**2

print(square_it(3))

print(len('ai dan'))

# put comments here. Make it easy on your future self.