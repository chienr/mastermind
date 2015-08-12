#!/usr/bin/env python2.7
import random
import readline
import sys


class MasterMindGame(object):
  
  def __init__(self):
    self.GenerateCandidates()
    self.secret = random.choice(self.candidates)
    self.tries = 1
  
  def GenerateCandidates(self):
    self.candidates = []
    for h in range(1, 7):
      for i in range(1, 7):
        for j in range(1, 7):
          for k in range(1, 7):
            self.candidates.append([h, i, j, k])

  def IsValidGuess(self, guess):
    if guess.lower() in ['quit', 'exit']:
      raise Exception('Exit requested.')
    if not guess.isdigit():
      return False
    guess = [int(i) for i in guess]
    if guess not in self.candidates:
      return False
    self.guess = guess
    self.tries = self.tries + 1    
    return True
      
  def Evaluate(self, guess, secret):
    pegs = ""
    for pos, val in enumerate(guess):
      if secret[pos] == val:
        pegs = pegs + 'B'
        secret[pos] = None
        guess[pos] = None
    for i in range(4):
      if guess[i] and guess[i] in secret:
        pegs = pegs + 'W'
        secret[secret.index(guess[i])] = None
    return pegs

  def PrettyPrintPegs(self, pegs):
    # Unicode BLACK CIRCLE: U+25cf
    # Unicode WHITE CIRCLE: U+25cb
    black = pegs.count('B')
    white = pegs.count('W')
    print(u'\u25cf'*black + u'\u25cb'*white)


def main():
  print("Welcome to MasterMind! (type ^C to quit)")
  try:
    while (1):
      mm = MasterMindGame()
      print("\nGenerating new code... done.")
      while (1):
        guess = raw_input('Guess #%2d: ' % mm.tries)
        if not mm.IsValidGuess(guess):
          print(guess + ' is not a valid guess. Only use 4 digits between 1 to 6.')
          continue
        pegs = mm.Evaluate(mm.guess[:], mm.secret[:])
        mm.PrettyPrintPegs(pegs)
        if pegs.count('B') == 4:
          print("Awesome! You broke the code!")
          break
  except (KeyboardInterrupt, EOFError, Exception):
    print("Goodbye.")
    sys.exit(0)


if __name__ == '__main__':
  main()