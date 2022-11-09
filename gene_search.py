from Bio import Blast
import datetime
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

def write_output(filename, gene, species, database, algorithm, score, evalue):
    file = open(filename, "w")

    date = datetime.datetime.now()

    file.write("Date created: " + str(date) + "\nGene of interest: " + gene + "\nSpecies specified: " + species + 
    "\nDatabase searched: " + database + "\nAlgorithm used: " + algorithm + "\nMax bit score: " + str(score) +
    "\nE-value: " + str(evalue))

    file.close()


if __name__ == '__main__':
    search_control("search-input.txt")