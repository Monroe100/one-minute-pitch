from flask_wtf import FlaskForm
from wtforms import StringField,TextAreaField,SubmitField

<<<<<<< HEAD
class PitchForm(FlaskForm):
=======
class PeptalkForm(FlaskForm):
>>>>>>> c74fb1c5c010f7302e5447fd11140ed96877d666
    content = TextAreaField('New Pitch')
    submit = SubmitField('Submit')

class CommentForm(FlaskForm):
    comment_section_id = TextAreaField('New Comment')
<<<<<<< HEAD
    submit = SubmitField('Submit')
=======
    submit = SubmitField('Submit')
>>>>>>> c74fb1c5c010f7302e5447fd11140ed96877d666
