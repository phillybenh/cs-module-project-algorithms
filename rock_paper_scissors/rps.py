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
      nonlocal out
      # add a play to this combination
      combo.append(plays[i])
      # if combination is n long, add it to output array
      if round_number == n:
        out.append(combo)
      else:
        # increment this round
        # recurse back through function
        round(combo, round_number + 1)
      
      # pop off the last appended play
      # b/c each iteration only get's one play?
      # combo.pop(-1)

    
  
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
  num_plays = 1
  print(rock_paper_scissors(num_plays))
