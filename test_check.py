import unittest
import check

board = [
  ['12', '9', '7', '14', '3'], 
  ['21', '29', '17', '18', '19'], 
  ['35', '40', 'x', '38', '37'], 
  ['50', '60', '53', '51', '46'], 
  ['75', '67', '73', '69', '70']
]

class TestCheckColumns(unittest.TestCase):
  def test_check_for_bingo_failure(self):
    actual = check.check_columns(board)
    expected = False
    self.assertEqual(actual, expected)

  def test_check_for_bingo_success_1(self):
    new_board = board[:]
    new_board[0] = ['x', 'x', 'x', 'x', 'x']
    actual = check.check_columns(new_board)
    expected = True
    self.assertEqual(actual, expected)

  def test_check_for_bingo_success_2(self):
    new_board = board[:]
    new_board[2] = ['x', 'x', 'x', 'x', 'x']
    actual = check.check_columns(new_board)
    expected = True
    self.assertEqual(actual, expected)

  def test_check_for_bingo_success_3(self):
    new_board = board[:]
    new_board[4] = ['x', 'x', 'x', 'x', 'x']
    actual = check.check_columns(new_board)
    expected = True
    self.assertEqual(actual, expected)