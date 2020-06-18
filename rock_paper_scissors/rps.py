#!/usr/bin/python

import sys

def rock_paper_scissors(n):
  # init output array
  out = [] 
  plays = ['rock', 'paper', 'scissors']
  
  # innner recursive function (READMe hinted at)
  def round(combo, round_number):
    # loop through the nubmer of rounds
    for i in range(3):
      # add a play to this combination
      combo.append(plays[i])
      # if combination is n long, add it to output array
      if round_number == n:
        return out.append(combo)
      else:
        # increment this round
        round_number += 1
        # recurse back through function
        round(combo, round_number)
  
  # call recursive function
  # initialize with [], so we can append to combo
  round([], 1)

  # return solution after recursive function is done
  return out


if __name__ == "__main__":
  # if len(sys.argv) > 1:
  #   num_plays = int(sys.argv[1])
  #   print(rock_paper_scissors(num_plays))
  # else:
  #   print('Usage: rps.py [num_plays]')
  num_plays = 2
  print(rock_paper_scissors(num_plays))