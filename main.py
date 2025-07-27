import sys
from stats import report_generator

def main(): 

    #path_to_file = "./books/frankenstein.txt"

    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)

    path_to_file = sys.argv[1]

    with open(path_to_file) as f:
        file_contents = f.read() 
        print (report_generator(path_to_file, file_contents))
 
main()


