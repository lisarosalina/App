from flask import Flask, render_template, request, Response, Blueprint
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
        
@dock.route('/dock', methods=['GET','POST'])
def dock():
        form = DockForm()
        Job_name=form.Job_name.data["Job_name"]
        protein = form.protein.data["protein"]
        ligand = form.ligand.data["ligand"]
        userPDBQT = request.file["userPDBQT"]

        if request.method == 'POST':
                #prepare_gpf4.py -l ligand_pdbqt_file -r receptor_pdbqt_file
                try:
                        os.system("/home/rosalina/Documents/App/mgltools/bin/pythonsh /home/rosalina/Documents/App/mgltools/MGLToolsPckgs/AutoDockTools/Utilities24/prepare_gpf4.py -l %s -r %s" % (ligand,protein))
                        os.rename(ligand+"_.gpf")
                except:
                        os.system("/home/rosalina/Documents/App/mgltools/bin/pythonsh /home/rosalina/Documents/App/mgltools/MGLToolsPckgs/AutoDockTools/Utilities24/prepare_gpf4.py -l %s -r %s" % (userPDBQT,protein))
                        gpf = os.rename(userPDBQT+"_.gpf")
                
                #pythonsh autogrid4 -p my_receptor.gpf -l my_receptor.glg &
                os.system("/home/rosalina/Documents/App/mgltools/bin/pythonsh /home/rosalina/Documents/App/mgltools/autodocksuite/autodock4.exe -p %s -l %s &" % (gpf, 'current.glg'))

                #pythonsh prepare_dpf4.py -l ligand_pdbqt_file -r receptor_pdbqt_file
                try:
                        os.system("/home/rosalina/Documents/App/mgltools/bin/pythonsh /home/rosalina/Documents/App/mgltools/MGLToolsPckgs/AutoDockTools/Utilities24/prepare_dpf4.py -l %s -r %s" % (ligand, protein))
                        dpf = os.rename(ligand+"_.dpf")
                except:
                        dpf = os.system("/home/rosalina/Documents/App/mgltools/bin/pythonsh /home/rosalina/Documents/App/mgltools/MGLToolsPckgs/AutoDockTools/Utilities24/prepare_dpf4.py -l %s -r %s" % (userPDBQT, protein))
                        #dpf = os.rename(userPDBQT+"_.dpf")
                
                #pythonsh autodock4 -p my_docking.dpf -l my_docking.dlg &
                try:
                        os.system('/home/rosalina/Documents/App/mgltools/bin/pythonsh /home/rosalina/Documents/App/mgltools/autodocksuite/autodock4.exe -p %s -l %s &' % (dpf,'current.dlg')
                finally:
                        print ('Try again')
        return render_template('dock.html', form=form)

#most probably need abs path to the file
#output = os.system("/home/rosalina/Documents/App/mgltools/bin/pythonsh /home/rosalina/Documents/App/mgltools/MGLToolsPckgs/AutoDockTools/Utilities24/summarize_results4.py -d %s" % ('./'))   
#return render_template('results.html', output)



        



