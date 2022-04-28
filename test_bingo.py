import unittest
import bingo

board = [
  ['12', '9', '7', '14', '3'], 
  ['21', '29', '17', '18', '19'], 
  ['35', '40', 'x', '38', '37'], 
  ['50', '60', '53', '51', '46'], 
  ['75', '67', '73', '69', '70']
]

class TestGetColumn(unittest.TestCase): # Tests that the proper column value is returned.

  def test_check_for_column_1(self): # Tests for last column.
    actual = bingo.get_column('69')
    self.assertEqual(actual, 4)

  def test_check_for_column_2(self): # Tests for middle-last column.
    actual = bingo.get_column('47')
    self.assertEqual(actual, 3)

  def test_check_for_column_3(self): # Tests for middle column.
    actual = bingo.get_column('35')
    self.assertEqual(actual, 2)

  def test_check_for_column_4(self): # Tests for middle-first column.
    actual = bingo.get_column('23')
    self.assertEqual(actual, 1)

  def test_check_for_column_5(self): # Tests for first column.
    actual = bingo.get_column('11')
    self.assertEqual(actual, 0)