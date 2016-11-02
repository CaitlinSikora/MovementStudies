# -*- coding: utf-8 -*-
from app import app
from app import db
from flask.ext.wtf import Form
from wtforms import FieldList
from wtforms import Form as NoCsrfForm
from wtforms.fields import StringField, FormField, SubmitField, SelectField
from wtforms.validators import DataRequired, Length

"""
   Simple example to load and save a User instance with related phone
   entries in a WTForm
"""

choices = [('Punch','Punch'),('Dab','Dab'),('Float','Float'),('Flick','Flick'),('Press','Press'),('Glide','Glide'),('Wring','Wring'),('Slash','Slash')]


# - - - Models - - -
class Video(db.Model):
    __tablename__ = 'videos'
    entry = db.Column(db.Integer(),primary_key=True)
    video = db.Column(db.String(50))
    user_name = db.Column(db.String(50))
    overall = db.Column(db.String(100))
    reason = db.Column(db.String(200))
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
    start_time = StringField('Start Time', validators=[DataRequired(),Length(min=1, max=10)])
    end_time = StringField('End Time', validators=[DataRequired(),Length(min=1, max=10)])
    laban_effort = SelectField(u'Quality', choices = choices, validators = [DataRequired()])
    emotion = StringField('Emotion',validators=[DataRequired()])
    body = StringField('Body Parts Involved',validators=[DataRequired()])

class CombinedForm(Form):
    # video = StringField('Video', validators=[DataRequired()])
    # we must provide empth Phone() instances else populate_obj will fail
    segments = FieldList(FormField(SegmentForm, default=lambda: Segment()))
    complete = SubmitField('Complete Survey')
    submit = SubmitField('Do Another Video')
    overall = StringField('Overall Interpretation', validators=[DataRequired()])
    reason = StringField('Overall Interpretation', validators=[DataRequired()])





