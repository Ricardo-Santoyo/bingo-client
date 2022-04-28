import unittest
import check
import copy

board = [
  ['12', '9', '7', '14', '3'], 
  ['21', '29', '17', '18', '19'], 
  ['35', '40', 'x', '38', '37'], 
  ['50', '60', '53', '51', '46'], 
  ['75', '67', '73', '69', '70']
]

def make_board(place, isColumn=False):
  new_board = copy.deepcopy(board)
  if isColumn:
    new_board[place] = ['x', 'x', 'x', 'x', 'x']
  else:
    for col in range(5):
      new_board[col][place] = 'x'
  return new_board

class TestCheckColumns(unittest.TestCase): # Tests for bingo in columns.
  def test_check_for_bingo_failure(self):
    actual = check.check_columns(board)
    expected = False
    self.assertEqual(actual, expected)

  def test_check_for_bingo_success_1(self): # Tests B column.
    actual = check.check_columns(make_board(0, True))
    expected = "C1"
    self.assertEqual(actual, expected)

  def test_check_for_bingo_success_2(self): # Tests N column.
    actual = check.check_columns(make_board(2, True))
    expected = "C3"
    self.assertEqual(actual, expected)

  def test_check_for_bingo_success_3(self): # Tests O column.
    actual = check.check_columns(make_board(4, True))
    expected = "C5"
    self.assertEqual(actual, expected)

class TestCheckDiagonals(unittest.TestCase): # Tests for bingo in diagonals.
  def test_check_for_bingo_failure(self):
    actual = check.check_diagonals(board)
    expected = False
    self.assertEqual(actual, expected)

  def test_check_for_bingo_success_1(self): # Tests diagonal running from top to bottom.
    new_board = copy.deepcopy(board)
    for i in range(5):
      new_board[i][i] = 'x'
    actual = check.check_diagonals(new_board)
    expected = "DL"
    self.assertEqual(actual, expected)

  def test_check_for_bingo_success_2(self): # Tests diagonal running bottom to top.
    new_board = copy.deepcopy(board)
    for i in range(5):
      new_board[i][4 - i] = 'x'
    actual = check.check_diagonals(new_board)
    expected = "DR"
    self.assertEqual(actual, expected)

class TestCheckRows(unittest.TestCase): # Tests for bingo in rows.
  def test_check_for_bingo_failure(self):
    actual = check.check_rows(board)
    expected = False
    self.assertEqual(actual, expected)
  
  def test_check_for_bingo_success_1(self): # Tests top row.
    actual = check.check_rows(make_board(0))
    expected = "R1"
    self.assertEqual(actual, expected)

  def test_check_for_bingo_success_2(self): # Tests middle row.
    actual = check.check_rows(make_board(2))
    expected = "R3"
    self.assertEqual(actual, expected)

  def test_check_for_bingo_success_3(self): # Tests bottom row.
    actual = check.check_rows(make_board(4))
    expected = "R5"
    self.assertEqual(actual, expected)