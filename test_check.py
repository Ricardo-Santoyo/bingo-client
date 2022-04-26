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

class TestCheckColumns(unittest.TestCase): # Tests for bingo in columns.
  def test_check_for_bingo_failure(self):
    actual = check.check_columns(board)
    expected = False
    self.assertEqual(actual, expected)

  def test_check_for_bingo_success_1(self): # Tests B column.
    new_board = board[:]
    new_board[0] = ['x', 'x', 'x', 'x', 'x']
    actual = check.check_columns(new_board)
    expected = True
    self.assertEqual(actual, expected)

  def test_check_for_bingo_success_2(self): # Tests N column.
    new_board = board[:]
    new_board[2] = ['x', 'x', 'x', 'x', 'x']
    actual = check.check_columns(new_board)
    expected = True
    self.assertEqual(actual, expected)

  def test_check_for_bingo_success_3(self): # Tests O column.
    new_board = board[:]
    new_board[4] = ['x', 'x', 'x', 'x', 'x']
    actual = check.check_columns(new_board)
    expected = True
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
    expected = True
    self.assertEqual(actual, expected)

  def test_check_for_bingo_success_2(self): # Tests diagonal running bottom to top.
    new_board = copy.deepcopy(board)
    for i in range(5):
      new_board[i][4 - i] = 'x'
    actual = check.check_diagonals(new_board)
    expected = True
    self.assertEqual(actual, expected)

class TestCheckRows(unittest.TestCase): # Tests for bingo in rows.
  def test_check_for_bingo_failure(self):
    actual = check.check_rows(board)
    expected = False
    self.assertEqual(actual, expected)
  
  def test_check_for_bingo_success_1(self): # Tests top row.
    new_board = copy.deepcopy(board)
    for col in range(5):
      new_board[col][0] = 'x'
    actual = check.check_columns(new_board)
    expected = True
    self.assertEqual(actual, expected)

  def test_check_for_bingo_success_2(self): # Tests middle row.
    new_board = copy.deepcopy(board)
    for col in range(5):
      new_board[col][2] = 'x'
    actual = check.check_columns(new_board)
    expected = True
    self.assertEqual(actual, expected)

  def test_check_for_bingo_success_3(self): # Tests bottom row.
    new_board = copy.deepcopy(board)
    for col in range(5):
      new_board[col][4] = 'x'
    actual = check.check_columns(new_board)
    expected = True
    self.assertEqual(actual, expected)