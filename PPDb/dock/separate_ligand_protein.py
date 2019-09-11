#!/usr/bin/env python
import sys
file = sys.argv[1]

import re
byline = [] #list to store results
byline2 = []
linenum = 0
re1 =r'(^ATOM)'
re2 =r'(^TER)'
re3 =r'(^HETATM)'
re4 =r'(^CONECT)'
patternProtein = re.compile("(%s|%s)" % (re1, re2))
patternLigand = re.compile("(%s|%s)" % (re3, re4))
with open (file, 'r') as myfile:
    for line in myfile:
        linenum += 1
        if patternProtein.search(line) !=None:
            byline.append((linenum))
            print(line, end='')
            with open(file.split(".")[0]+"_protein.pdb", "a+") as output:
                output.write (str(line))

with open (file, 'r') as myfile:
    for line in myfile:
        linenum += 1
        if patternLigand.search(line) !=None:
            byline2.append((linenum))
            print(line, end='')
            with open(file.split(".")[0]+"_ligand.pdb", "a+") as output:
                output.write (str(line))           

#pythonsh separate_ligand_protein.py pdbfile