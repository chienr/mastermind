import unittest
import mastermind

class MasterMindGameTest(unittest.TestCase):

  def setUp(self):
    self.mm = mastermind.MasterMindGame()
    
  def testGenerateCandidates(self):
    candidates = self.mm.candidates
    self.assertEqual(len(candidates), 1296)

  def testCandidatesNoDuplicates(self):
    candidates = self.mm.candidates
    # This takes O(n^2) time.
    self.assertFalse(any(candidates.count(c) > 1 for c in candidates))
  
  def testCandidatesWithinRange(self):
    self.assertEqual(
      filter(lambda i: 
        filter(lambda j:
          j not in [1,2,3,4,5,6],
          i),
        self.mm.candidates),
      [])

  def testEvaluateNonRepeatingSecret(self):
    secret = [1, 2, 3, 4]
    self.assertEqual(self.mm.Evaluate([1, 1, 2, 2], secret[:]), 'BW')
    self.assertEqual(self.mm.Evaluate([4, 3, 2, 1], secret[:]), 'WWWW')
    self.assertEqual(self.mm.Evaluate([1, 2, 3, 4], secret[:]), 'BBBB')
    
  def testEvaluateRepeatingSecret(self):
    secret = [1, 1, 2, 3]
    self.assertEqual(self.mm.Evaluate([1, 2, 3, 4], secret[:]), 'BWW')
  
  def testValidGuess(self):
    self.assertTrue(self.mm.IsValidGuess('1234'))

  def testInvalidGuess(self):
    self.assertFalse(self.mm.IsValidGuess('abcd'))

  def testGuessNotInRange(self):
    self.assertFalse(self.mm.IsValidGuess('9999'))
    self.assertFalse(self.mm.IsValidGuess('123'))
    self.assertFalse(self.mm.IsValidGuess('12345'))

if __name__ == '__main__':
  unittest.main()