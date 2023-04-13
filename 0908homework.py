# -*- coding: utf-8 -*-
"""
Created on Wed Sep 21 15:09:29 2022

@author: User
"""
def math(i):
    if i>1:
        return math(i-1)+math(i-2)
    return i

for i in range(1,25):
    print(math(i))




 




    
  


       
    