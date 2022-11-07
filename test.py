import gene_search
import unittest

class TestSearchControl(unittest.TestCase):
    def test_runs(self):
        assert True

    def test_expected_input(self):
        assert True
    
    def test_unexpected_input_gene(self):
        assert True

    def test_unexpected_input_species(self):
        assert True

    def test_unexpected_input_database(self):
        assert True

    def test_unexpected_input_algorithm(self):
        assert True
    

class TestReadInput(unittest.TestCase):
    def test_runs(self):
        [gene, species, database, algorithm] = gene_search.read_input("search-input.txt")
        self.assertEqual(gene, "[genefile]\n", f"given gene does not match expected output")
        self.assertEqual(species, "[species]\n", f"given species does not match expected output")
        self.assertEqual(database, "[database]\n", f"given database does not match expected output")
        self.assertEqual(algorithm, "[algorithm]\n", f"given algorithm does not match expected output")

    def test_expected_input(self):
        assert True
    
    def test_unexpected_input(self):
        assert True


class TestWriteInput(unittest.TestCase):
    def test_runs(self):
        assert True
    
    def test_expected_input(self):
        assert True
    
    def test_unexpected_input(self):
        assert True

if __name__ == '__main__':
    unittest.main()