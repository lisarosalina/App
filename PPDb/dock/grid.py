#!/usr/bin/env python

import os
import sys
import subprocess

subprocess.call(['/home/rosalina/Documents/App/mgltools/bin/pythonsh','/home/rosalina/Documents/App/mgltools/autodocksuite/autogrid4 -p ./4PMM_protein.gpf -r ./4PMM_protein.glg &'])
#os.system("/home/rosalina/Documents/App/mgltools/bin/pythonsh /home/rosalina/Documents/App/mgltools/autodocksuite/autogrid4 -p ./4PMM_protein.gpf -r ./4PMM_protein.glg &")
#pythonsh autogrid4 -p my_receptor.gpf -l my_receptor.glg &

#File "/home/rosalina/Documents/App/mgltools/autodocksuite/autogrid4", line 1
#SyntaxError: Non-ASCII character '\xfe' in file /home/rosalina/Documents/App/mgltools/autodocksuite/autogrid4 on line 2, but no encoding declared; see http://www.python.org/peps/pep-0263.html for details 
