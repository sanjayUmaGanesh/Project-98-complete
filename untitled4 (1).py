# -*- coding: utf-8 -*-
"""Untitled4.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1uflbUepFG_7Qvo91g2L_t4acz6-S6lcQ
"""

def swap():
 
  fileName1 = input("Enter file Name 1: ")
  file = open(fileName1 , 'r')
  data_a = file.read()


  fileName2 = input("Enter file Name 2: ")
  file2 = open(fileName2 , 'r')
  data_b = file2.read()

  print("swaping...")

  
  file = open(fileName1 , 'w')
  file.write(data_b)


  file2 = open(fileName2 , 'w')
  file2.write(data_a)

  print('swaped successfully')
  
swap()