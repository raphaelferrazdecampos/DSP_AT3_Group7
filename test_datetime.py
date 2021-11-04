# To be filled by students
import unittest
from datetime import DateColumn
import pandas as pd

#file_url = 'C:/Users/jinlei.han/Downloads/uber-raw-data-sep14.csv.gz'
#df = pd.read_csv(file_url, nrows=1000, parse_dates=['Date/Time'])
#col_name1 = 'Date/Time'

testDate = DateColumn()

class TestDateColumnMethods(unittest.TestCase):
    def setUp(self):
        ############
    def test_get_name(self):
        self.assertEqual(testDate.get_name(),"Date/Time")

    def test_get_unique(self):
        self.assertEqual(testDate.get_unique(),728)

    def test_get_missing(self):
        self.assertEqual(testDate.get_missing(),0)

    def test_get_weekend(self):
        self.assertEqual(testDate.get_weekend(),0)

    def test_get_weekday(self):
        self.assertEqual(testDate.get_weekday(),1000)

    def test_get_future(self):
        self.assertEqual(testDate.get_future(),0)

    def test_get_empty_1900(self):
        self.assertEqual(testDate.get_empty_1900(),0)

    def test_get_empty_1970(self):
        self.assertEqual(testDate.get_empty_1970(),0)

    def test_get_min(self):
        self.assertEqual(testDate.get_min(),'2014-09-01 00:01:00')

    def test_get_max(self):
        self.assertEqual(testDate.get_max(),'2014-09-02 11:18:00')

if __name__ == '__main__':
    unittest.main()
