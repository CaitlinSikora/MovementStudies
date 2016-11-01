from flask import render_template, flash, redirect, session, url_for
from app import app
from app import db
from .forms import UserForm, SegmentForm, CombinedForm, User, Segment, Video

videos = ['static/video1.mov',
'static/video2.mov',
'static/video3.mov',
'static/video4.mov',
'static/video5.mov',
'static/video6.mov']

durations = [25.088,33.976289,34.416667,25.68127,21.182211,24.4]

num = 0

@app.route('/', methods=['GET', 'POST'])
def get_user():
    user = User(user_name="name")
    form = UserForm()
    if form.validate_on_submit():
        # flash('Data requested for business_name="%s", owner="%s", business_type="%s", location="%s"' %
        #   (form.business_name.data, form.owner.data, form.business_type.data, form.location.data))
        session['user_name'] = form.user_name.data
        form.populate_obj(user)
        db.session.add(user)
        db.session.commit()
        return redirect(url_for('instruct'))
    return render_template('index.html',
                           form=form)

@app.route('/instructions', methods=['GET', 'POST'])
def instruct():
    return render_template('instructions.html',
                           user=session['user_name'])

@app.route('/video', methods=['GET', 'POST'])
def vid():
    global num
    # always "blindly" load the user
    video = Video(user_name=session['user_name'],video=str(num+1))
    # video = Video.query.first()

    # if User has no phones, provide an empty one so table is rendered
    if len(video.segments) == 0:
        video.segments = [Segment(start_time="0:00",end_time="0:10")]
        # flash("empty Segment provided")

    # else: forms loaded through db relation
    form = CombinedForm(obj=video)

    if form.validate_on_submit():
        form.populate_obj(video)
        db.session.add(video)
        db.session.commit()
        flash("Saved Changes")
        num += 1
        print num
        num=num%len(videos)
        return redirect(url_for('vid'))
    return render_template('segments.html', form=form, num=num+1, this_video=videos[num], duration=durations[num])

@app.route('/thanks', methods=['GET', 'POST'])
def thanks():
    return render_template('thanks.html',
                           user=session['user_name'])