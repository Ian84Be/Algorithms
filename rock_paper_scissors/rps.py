#!/usr/bin/python

import sys

def rock_paper_scissors(n):
  rps = [['rock'],['paper'],['scissors']]
  if n < 1:
    return [[]]
  if n == 1:
    return rps
  def rpsTree(L, n):
    if n == 0:
      return [[]]
    return [x + y for x in rpsTree(L, n-1) for y in L]
  res = rpsTree(rps, n)
  return res


if __name__ == "__main__":
  if len(sys.argv) > 1:
    num_plays = int(sys.argv[1])
    print(rock_paper_scissors(num_plays))
  else:
    print('Usage: rps.py [num_plays]')