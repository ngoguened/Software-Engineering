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
    # Since the file is standardized to be in the order gene, species, database, algorithm, output will be in this order
    # and manipulated immediately in search_control which assumes this order of inputs.
    input = []
    file = open(filename, "r")
    for line in file:
        input.append(line[line.find(": ")+2:]) #+2 excludes the identifier chars.
    file.close()
    return input

def write_output(gene, species, database, algorithm, score, evalue):
    #TODO: Implement file write
    return

if __name__ == '__main__':
    search_control("search-input.txt")