import gene_search
import unittest
import os

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
    # Since I am assuming that the proper file input will be respected, it is impossible for the input values to not be strings.
    def test_runs(self):
        f = open("test-search-input.txt", "w")
        f.write("Gene of interest: [genefile]\nSpecies: [species]\nDatabase: [database]\nAlgorithm: [algorithm]\n")
        f.close()
        [genefile, species, database, algorithm] = gene_search.read_input("test-search-input.txt")

        os.remove("test-search-input.txt")

        self.assertEqual(genefile, "[genefile]", f"given gene does not match expected output")
        self.assertEqual(species, "[species]", f"given species does not match expected output")
        self.assertEqual(database, "[database]", f"given database does not match expected output")
        self.assertEqual(algorithm, "[algorithm]", f"given algorithm does not match expected output")


class TestWriteInput(unittest.TestCase):
    def test_runs(self):
        gene_search.write_output("test-search-output.txt", "[genefile]", "[species]", "[database]", "[algorithm]", "[score]", "[evalue]")
        os.remove("test-search-output.txt")
        # ad hoc views ascertain the method runs.
    assert True

    def test_unexpected_input(self):
        assert True

class TestReadFastaSequence(unittest.TestCase):
    def test_runs(self):
        assert True
        #TODO: finish writing tests
        f = open("test-search-input.txt", "w")
        f.write("Gene of interest: /home/nicholas/Downloads/sequence.fasta\nSpecies: [species]\nDatabase: [database]\nAlgorithm: [algorithm]\n")
        f.close()
        gene_search.search_control("test-search-input.txt")
        os.remove("test-search-input.txt")
        

if __name__ == '__main__':
    unittest.main()