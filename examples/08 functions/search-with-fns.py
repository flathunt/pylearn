#!/usr/local/bin/python

import re
import sys

UNDERLINE = '='


def get_arguments():

    # check for correct number of arguments...
    
    if len(sys.argv) != 3:
        print("Usage: review2-search.py search_terms_file data_file", file=sys.stderr)
        sys.exit(1)
    
    # return...
    
    terms_file, data_file = sys.argv[1:3]
    return terms_file, data_file

    
def build_pattern(terms_file): 
        
    # Read the file of search terms and build a (RegEx) pattern...

    terms_list = []
    with open(terms_file) as search_words:
        for entry in search_words:
            terms_list.append(entry.rstrip())

    pattern = '|'. join(terms_list)
    # print('Pattern:', pattern, end='\n\n') # for debugging purposes
    
    return pattern

    
def search_file(pattern, data_file):
    
    # Check the data file for matches...

    with open(data_file) as data:
        for ln, line in enumerate(data, start=1):
            m = re.search(pattern, line)
            if m:
                print("{:04d} {:s}".format(ln, line), end='')
                print(' ' * (5 + m.start()) + UNDERLINE * (m.end() - m.start()))

                
# =====================================================================
# main processing: Search a file for terms provided by another file.

# Usage: search-with-fns.py search_terms_file file_to_search    
# =====================================================================

def main():
    terms_file, data_file = get_arguments()

    pattern = build_pattern(terms_file)

    search_file(pattern, data_file)
    
    
main()
