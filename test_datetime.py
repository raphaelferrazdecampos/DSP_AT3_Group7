# To be filled by students
import unittest
from datetime import DateColumn
import pandas as pd
import numpy as np

class TestDateColumnMethods(unittest.TestCase):
    def setUp(self):
        rng = pd.date_range('2021-01-01', periods=100, freq='T')
        df = pd.DataFrame({ 'Date': rng, 'Val': np.random.randn(len(rng)) })
        self.date_column = df['Date']
        self.testDate = DateColumn(df,'Date')

    def test_get_name(self):
        self.assertEqual(self.testDate.get_name(),"Date")

    def test_get_unique(self):
        self.assertEqual(self.testDate.get_unique(),100)

    def test_get_missing(self):
        self.assertEqual(self.testDate.get_missing(),0)

    def test_get_weekend(self):
        self.assertEqual(self.testDate.get_weekend(),0)

    def test_get_weekday(self):
        self.assertEqual(self.testDate.get_weekday(),100)

    def test_get_future(self):
        self.assertEqual(self.testDate.get_future(),0)

    def test_get_empty_1900(self):
        self.assertEqual(self.testDate.get_empty_1900(),0)

    def test_get_empty_1970(self):
        self.assertEqual(self.testDate.get_empty_1970(),0)

    def test_get_min(self):
        self.assertEqual(self.testDate.get_min(),'2021-01-01 00:00:00')

    def test_get_max(self):
        self.assertEqual(self.testDate.get_max(),'2021-01-01 01:39:00')

if __name__ == '__main__':
    unittest.main()
