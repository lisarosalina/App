#!/usr/bin/env python

molecules = ['HOH', 'GOL', 'ACT', 'CL' ]

with open ('ligandclean.pdb') as oldfile, open('dehydratedligand1.pdb','w') as newfile:
    for line in oldfile:
        if not any(molecule in line for molecule in molecules):
            newfile.write(line)

#pythonsh remove_unwanted.py pdbfile