from Bio import Blast
EMAIL = "s2013017@ed.ac.uk"

#_________________________________________________________
# Search functions

def search_control(filename):
    #TODO: Implement search control.
    gene, species, database, algorithm = read_input(filename)
    score = None
    evalue = None
    return [gene, species, database, algorithm, score, evalue]

#_________________________________________________________
# File Boilerplate

def read_input(filename):
    #TODO: Implement file read
    gene = None
    species = None
    database = None
    algorithm = None
    return [gene, species, database, algorithm]

def write_output(gene, species, database, algorithm, score, evalue):
    #TODO: Implement file write
    return

if __name__ == '__main__':
    search_control("search-input.txt")