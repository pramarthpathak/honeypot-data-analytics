#!/bin/python

import json
import argparse

parser = argparse.ArgumentParser()
parser.add_argument("input_file", help="input text file")
parser.add_argument("output_file", help="output filename (will be a pickle file containing a list of strings that represent the lines of the input file")



args = parser.parse_args()

inpf = open(args.input_file, "r")
outf = open(args.output_file, "w+")


i = 0
for l in inpf.readlines():
    # get line and search for {"eventid from position 10
    
    try:
        a = json.loads(l)
        if (a['eventid'] == 'cowrie.command.input'):
            if (a['input'].find('Accept') == -1
                and a['input'].find('Connection') == -1
                and a['input'].find('User-Agent') == -1
                and a['input'].find('Win64') == -1
                and a['input'].find('development') == -1):        
    
                outf.write(l)
            else:
                print(a)
        else:
            outf.write(l)



    except:
        print("json error")
        print(l)




