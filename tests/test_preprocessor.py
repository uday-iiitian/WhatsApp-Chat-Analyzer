import unittest
import os
from preprocessor import preprocess


class TestPreprocessor(unittest.TestCase):
    def setUp(self):
        base = os.path.dirname(os.path.dirname(__file__))
        sample_path = os.path.join(base, 'sample_chat.txt')
        with open(sample_path, 'r', encoding='utf-8') as f:
            self.data = f.read()

    def test_preprocess_creates_expected_columns(self):
        df = preprocess(self.data)
        # Basic sanity checks
        expected_columns = {'date', 'only_date', 'year', 'month_num', 'month', 'day', 'day_name', 'hour', 'minute', 'period', 'user', 'message'}
        self.assertTrue(expected_columns.issubset(set(df.columns)))
        # We expect 6 messages from the sample file
        self.assertGreaterEqual(df.shape[0], 5)


if __name__ == '__main__':
    unittest.main()
