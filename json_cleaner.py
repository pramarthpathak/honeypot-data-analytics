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
    
    num = l.find('{"eventid',10) 
    if num != -1:
        #print("####WRONG LINE####")
        #print(l)
        #print("position of error: " + str(num))
        #print("####FIXED LINE####")
        #print(l[num:])

        try:
            json.loads(l[num:])
            outf.write(l[num:])
        except:
            print("json error")
            print(l[num:])

    else:
        try:
            json.loads(l)
            outf.write(l)
        except:
            print("json error")
            print(l)



