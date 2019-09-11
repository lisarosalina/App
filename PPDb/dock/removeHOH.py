#!/usr/bin/env python
import sys

def removeHOH(userPDBfile=""):
    file = sys.argv[1]
    molecules = ['HOH']
    
    with open (file) as oldfile, open(file.split(".")[0]+"_dehydrated.pdb",'w') as newfile:
        for line in oldfile:
            if not any(molecule in line for molecule in molecules):
                newfile.write(line)

#pythonsh remove_unwanted.py pdbfile