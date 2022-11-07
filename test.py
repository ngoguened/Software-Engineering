import gene_search
import unittest

class TestSearchControl(unittest.TestCase):
    def test_import(self):
        result = gene_search.search_control(None, None, None, None)
        self.assertEqual(result[0], None, f'')

class TestFileBoilerplate(unittest.TestCase):
    def test_read_input(self):
        #TODO: test input.
        self.assertEqual(0,0,f'')
    def test_write_output(self):
        #TODO: test output.
        self.assertEqual(0,0,f'')

if __name__ == '__main__':
    unittest.main()