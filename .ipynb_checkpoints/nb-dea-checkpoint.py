#!/usr/bin/env python

import argparse

def main():
    parser = argparse.ArgumentParser(
        prog="nb-dea",
        description="Command-script to perform differential expression analysis"
    )
    #Input 
    parser.add_argument("nb-dea", help="Whatever Whatever", \
                        type=str)

    #Output
    parser.add_argument("-o", "--out", help="write output to file. " \
                        "Default: stdout", metavar="FILE", type=str, \
                        required=False)

    #Other Options
    parser.add_argument("-n", "--normalization", \
                        help="normalization factor you want to use", \
                        type=str, required=False)

    parser.add_argument("-f", "--filter", \
                        help="filter you want to use", \
                        type=str, required=False)
    
    args = parser.parse_args()

if __name__ == "__main__":
    main()