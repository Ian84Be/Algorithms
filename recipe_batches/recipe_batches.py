#!/usr/bin/python

import math

def recipe_batches(recipe, pantry):
    batch = {}
    for i in recipe:
        if i in pantry:
            batch[i] = pantry[i] // recipe[i]
        else:
            batch[i] = 0
    max = 0
    if 0 in batch.values():
        return max
    else:
        while 0 not in batch.values():
            max += 1
            for i in batch:
                batch[i] -= 1
        return max


if __name__ == '__main__':
  # Change the entries of these dictionaries to test 
  # your implementation with different inputs
  recipe = { 'milk': 100, 'butter': 50, 'flour': 5 }
  pantry = { 'milk': 132, 'butter': 48, 'flour': 51 }
  print("{batches} batches can be made from the available pantry: {pantry}.".format(batches=recipe_batches(recipe, pantry), pantry=pantry))