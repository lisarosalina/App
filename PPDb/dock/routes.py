import subprocess
import os
from flask import Flask, render_template, request, redirect, url_for, Response, Blueprint
from flask_uploads import UploadSet, ALL
from PPDb.config import Config
from flask_wtf import FlaskForm
from flask_wtf.file import FileField
from wtforms import SubmitField, StringField, SelectField


#from flask_sqlalchemy import SQLAlchemy
#from wtforms.ext.sqlalchemy.fields import QuerySelectField
#from PPDb.models import Protein_profile, Ligand_information
#from os import listdir
#from os.path import isfile, join

dock = Blueprint('dock', __name__)

userPDB = UploadSet('userPDB',ALL)
userPDBQT = UploadSet('userPDBQT', ALL)

#choose_protein = [f for f in listdir(/home/rosalina/Documents/App/static/protein_pdbqt) if isfile(join(/home/rosalina/Documents/App/static/protein_pdbqt, f))]
#choose_ligand = [f for f in listdir(/home/rosalina/Documents/App/static/protein_pdbqt) if isfile(join(/home/rosalina/Documents/App/static/ligand_pdbqt, f))]

class  DockForm(FlaskForm):
        Job_name = StringField('Job name here')
        protein = SelectField(u'Protein', choices=[('./4PMM.pdbqt'),('./4PMP.pdbqt'),('./4PMS.pdbqt'),('./4PMT.pdbqt')])
        ligand = SelectField(u'Ligand', choices=[('./4PMM_ligand.pdbqt'),('./4PMM_ligand.pdbqt'),('./4PMM_ligand.pdbqt'),('./4PMM_ligand.pdbqt')])
        userPDBQT = FileField(u'Upload your own ligand in pdbqt format here')
        submitfile = SubmitField('Upload')
        submitform = SubmitField('Run')
        
@dock.route('/dock', methods=['POST','GET'])
def docking():
        form = DockForm()
        if request.method == 'POST':
                Job_name=request.form.get["Job_name"]
                protein = request.form.get["protein"]
                ligand = request.form.get["ligand"]
                userPDBQT = request.file["userPDBQT"]

                #prepare_gpf4.py -l ligand_pdbqt_file -r receptor_pdbqt_file
                #os.system("/home/rosalina/Documents/App/mgltools/bin/pythonsh /home/rosalina/Documents/App/mgltools/MGLToolsPckgs/AutoDockTools/Utilities24/prepare_gpf4.py -l %s -r %s" % (ligand,protein))
                                        
                #pythonsh autogrid4 -p my_receptor.gpf -l my_receptor.glg &
                #os.system("/home/rosalina/Documents/App/mgltools/bin/pythonsh /home/rosalina/Documents/App/PPDb/dock/autogrid4.exe -p %s -l %s &" % (gpf,'current.glg'))

                #pythonsh prepare_dpf4.py -l ligand_pdbqt_file -r receptor_pdbqt_file
                #os.system("/home/rosalina/Documents/App/mgltools/bin/pythonsh /home/rosalina/Documents/App/mgltools/MGLToolsPckgs/AutoDockTools/Utilities24/prepare_dpf4.py -l %s -r %s" % (ligand, protein))
                                
                #pythonsh autodock4 -p my_docking.dpf -l my_docking.dlg &
                #os.system('/home/rosalina/Documents/App/mgltools/bin/pythonsh /home/rosalina/Documents/App/PPDb/dock/autodock4.exe -p %s -l %s &' % (dpf,'current.dlg')
                #return render_template('results.html')

        return render_template('dock.html', form=form)

#most probably need abs path to the file
#output = os.system("/home/rosalina/Documents/App/mgltools/bin/pythonsh /home/rosalina/Documents/App/mgltools/MGLToolsPckgs/AutoDockTools/Utilities24/summarize_results4.py -d %s" % ('./'))   
#return render_template('results.html', output)



        



