from flask_login import login_required

@main.route('/category/pitch/new/<int:id>', methods = ['GET','POST'])
@login_required
def new_pitch(id):