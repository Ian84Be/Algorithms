#!/usr/bin/python

import sys

cache = {}
def rock_paper_scissors(n):
  rps = [['rock'],['paper'],['scissors']]
  if n < 1:
    return [[]]
  if n == 1:
    return rps
  def rpsTree(L, n):
    global cache
    if n == 0:
      return [[]]
    if n not in cache:
        cache[n] = [x + y for x in rpsTree(L, n-1) for y in L]
    return cache[n]
  res = rpsTree(rps, n)
  return res


if __name__ == "__main__":
  if len(sys.argv) > 1:
    num_plays = int(sys.argv[1])
    print(rock_paper_scissors(num_plays))
  else:
    print('Usage: rps.py [num_plays]')