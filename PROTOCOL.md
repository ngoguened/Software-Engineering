# I/O Protocol

Input:
* Input will be assumed to exist in the file search-input.txt.
* Input must be formatted as such:
    * "Date created: [date] \n
    * Gene of interest: [genefile] \n
    * Species: [species] \n
    * Database: [database] \n
    * Algorithm: [algorithm] \n"
* All fields must be initialized to be a valid input.

Output:
* Output will be assumed exist in the file search-output.txt.
* Output will be formatted as such:
    * "Date created: [date] \n
    * Gene of interest: [genefile] \n
    * Species specified: [species] \n
    * Database searched: [database] \n
    * Algorithm used: [algorithm] \n
    * Max bit score: [score] \n
    * E-value: [evalue] \n"

Parameters:
* [date]: A date object which documents exactly when an input or output was created. Initialized by the program.
* [genefile]: A string denoting the FASTA file name for the gene of interest. Will return an error if the filepath does not exist.
* [species]: A string of the specific species the gene of interest is searching for. The empty string will perform a search across all species.
* [database]: A string of the specific database being searched. The empty string will perform a search across all databases.
* [algorithm]: The specific BLAST algorithm used between BLASTP, BLASTN, and TBLASTN. The empty string will perform TBLASTN. 
* [score]: The integer max bit score evaluated from the BLAST search.
* [evalue]: The scientific notation E-value evaluated from the BLAST search of the form (raw, magnitude).