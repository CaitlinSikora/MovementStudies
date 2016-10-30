# -*- coding: utf-8 -*-
from app import app
from app import db
from flask.ext.wtf import Form
from wtforms import FieldList
from wtforms import Form as NoCsrfForm
from wtforms.fields import StringField, FormField, SubmitField, SelectField
from wtforms.validators import DataRequired, Length

# app = Flask(__name__)
# app.config.from_object('config')
# db = SQLAlchemy(app)

"""
   Simple example to load and save a User instance with related phone
   entries in a WTForm
"""

# videos = ['3k9TNhTaP6g',
# 'htn9HtJRvgE',
# 'Vw4-BhHALv8',
# '1J_LKT_mWwo']

choices = [('Punch','Punch'),('Dab','Dab'),('Float','Float'),('Flick','Flick'),('Press','Press'),('Glide','Glide'),('Wring','Wring'),('Slash','Slash')]


# - - - Models - - -
class Video(db.Model):
    __tablename__ = 'videos'
    entry = db.Column(db.Integer(),primary_key=True)
    video = db.Column(db.String(50))
    user_name = db.Column(db.String(50))
    segments = db.relationship('Segment')

class Segment(db.Model):
    __tablename__ = 'segments'
    segment_id = db.Column(db.Integer(), primary_key=True)
    video_entry = db.Column(db.Integer(), db.ForeignKey('videos.entry'))
    start_time = db.Column(db.String(4))
    end_time = db.Column(db.String(4))
    laban_effort = db.Column(db.String(50))
    emotion = db.Column(db.String(50))
    body = db.Column(db.String(50))

class User(db.Model):
    __tablename__ = 'users'
    user_id = db.Column(db.Integer(), primary_key=True)
    user_name = db.Column(db.String(50))
    age = db.Column(db.String(50))
    gender_id = db.Column(db.String(50))
    country = db.Column(db.String(50))

# - - - Forms - - -
class UserForm(Form):
    user_name = StringField('First and Last Names', validators=[DataRequired()])
    age = StringField('Age')
    gender_id = StringField('Gender Identity')
    country = StringField('Birth Country')

class SegmentForm(NoCsrfForm):
    # this forms is never exposed so we can use the non CSRF version
    start_time = StringField('Start Time', validators=[DataRequired(),Length(min=4, max=4)])
    end_time = StringField('End Time', validators=[DataRequired(),Length(min=4, max=4)])
    laban_effort = SelectField(u'Quality', choices = choices, validators = [DataRequired()])
    emotion = StringField('Emotion',validators=[DataRequired()])
    body = StringField('Body Parts Involved',validators=[DataRequired()])

class CombinedForm(Form):
    # video = StringField('Video', validators=[DataRequired()])
    # we must provide empth Phone() instances else populate_obj will fail
    segments = FieldList(FormField(SegmentForm, default=lambda: Segment()))
    #submit = SubmitField('Submit')


# - - - Routes - - -
# @app.route('/', methods=['GET', 'POST'])
# def get_user():
#     user = User(user_name="name")
#     form = UserForm()
#     if form.validate_on_submit():
#         # flash('Data requested for business_name="%s", owner="%s", business_type="%s", location="%s"' %
#         #   (form.business_name.data, form.owner.data, form.business_type.data, form.location.data))
#         session['user_name'] = form.user_name.data
#         form.populate_obj(user)
#         db.session.add(user)
#         db.session.commit()
#         return redirect(url_for('instruct'))
#     return render_template('index.html',
#                            form=form)

# @app.route('/instructions', methods=['GET', 'POST'])
# def instruct():
#     return render_template('instructions.html',
#                            user=session['user_name'])

# @app.route('/1', methods=['GET', 'POST'])
# def vid_1():
#     num = 1
#     # always "blindly" load the user
#     video = Video(user_name=session['user_name'],video=str(num))
#     # video = Video.query.first()

#     # if User has no phones, provide an empty one so table is rendered
#     if len(video.segments) == 0:
#         video.segments = [Segment(start_time="0:00",end_time="0:10")]
#         # flash("empty Segment provided")

#     # else: forms loaded through db relation
#     form = CombinedForm(obj=video)

#     if form.validate_on_submit():
#         form.populate_obj(video)
#         db.session.add(video)
#         db.session.commit()
#         flash("Saved Changes")
#         return redirect(url_for('vid_2'))
#     return render_template('segments.html', form=form, num=num, this_video=videos[num-1])

# @app.route('/2', methods=['GET', 'POST'])
# def vid_2():
#     num = 2
#     # always "blindly" load the user
#     video = Video(user_name=session['user_name'],video=str(num))
#     # video = Video.query.first()

#     # if User has no phones, provide an empty one so table is rendered
#     if len(video.segments) == 0:
#         video.segments = [Segment(start_time="0:00",end_time="0:10")]
#         # flash("empty Segment provided")

#     # else: forms loaded through db relation
#     form = CombinedForm(obj=video)

#     if form.validate_on_submit():
#         form.populate_obj(video)
#         db.session.add(video)
#         db.session.commit()
#         flash("Saved Changes")
#         return redirect(url_for('vid_3'))
#     return render_template('segments.html', form=form, num=num, this_video=videos[num-1])

# @app.route('/3', methods=['GET', 'POST'])
# def vid_3():
#     num = 3
#     # always "blindly" load the user
#     video = Video(user_name=session['user_name'],video=str(num))
#     # video = Video.query.first()

#     # if User has no phones, provide an empty one so table is rendered
#     if len(video.segments) == 0:
#         video.segments = [Segment(start_time="0:00",end_time="0:10")]
#         # flash("empty Segment provided")

#     # else: forms loaded through db relation
#     form = CombinedForm(obj=video)

#     if form.validate_on_submit():
#         form.populate_obj(video)
#         db.session.add(video)
#         db.session.commit()
#         flash("Saved Changes")
#         return redirect(url_for('vid_4'))
#     return render_template('segments.html', form=form, num=num, this_video=videos[num-1])

# @app.route('/4', methods=['GET', 'POST'])
# def vid_4():
#     num = 4
#     # always "blindly" load the user
#     video = Video(user_name=session['user_name'],video=str(num))
#     # video = Video.query.first()

#     # if User has no phones, provide an empty one so table is rendered
#     if len(video.segments) == 0:
#         video.segments = [Segment(start_time="0:00",end_time="0:10")]
#         # flash("empty Segment provided")

#     # else: forms loaded through db relation
#     form = CombinedForm(obj=video)

#     if form.validate_on_submit():
#         form.populate_obj(video)
#         db.session.add(video)
#         db.session.commit()
#         flash("Saved Changes")
#         return redirect(url_for('thanks'))
#     return render_template('segments.html', form=form, num=num, this_video=videos[num-1])

# @app.route('/thanks', methods=['GET', 'POST'])
# def thanks():
#     return render_template('thanks.html',
#                            user=session['user_name'])

# # - - - Execute - - -
# def prep_db():
#     db.drop_all()
#     db.create_all()
#     # db.session.add(Video(video="My Video"))
#     db.session.commit()

# if __name__ == '__main__':
#     prep_db()
#     app.run(debug=True, port=5002)
