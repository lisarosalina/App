class  LigandCleanupForm(FlaskForm):
        Job_name = StringField('Job name here')
        userPDB = FileField(u'Upload your own ligand in pdbqt format here')
        submitform = SubmitField('Run')

@dock.route('/cleanup', methods=['GET','POST'])
def cleanup():
        form = LigandCleanupForm()
        if request.method == 'POST' and 'userPDB' in request.files:
		# Upload the input file
		userPDBfile = userPDB.save(request.files['userPDB'])
                return ('File uploaded sucessfully')
                        molecules = ['HOH', 'GOL', 'ACT', 'CL' ]
                        with open (userPDBfile) as oldfile, open(userPDBfile.split(".")[0]+"_clean.pdb",'w') as newfile:
                                for line in oldfile:
                                        if not any(molecule in line for molecule in molecules):
                                                newfile.write(line)
                return render_template('cleanup.html')