from flask import render_template, flash, redirect, session, url_for
from app import app
from app import db
from .forms import UserForm, SegmentForm, CombinedForm, User, Segment, Video

videos = ['3k9TNhTaP6g',
'htn9HtJRvgE',
'Vw4-BhHALv8',
'1J_LKT_mWwo']

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

@app.route('/1', methods=['GET', 'POST'])
def vid_1():
    num = 1
    # always "blindly" load the user
    video = Video(user_name=session['user_name'],video=str(num))
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
        return redirect(url_for('vid_2'))
    return render_template('segments.html', form=form, num=num, this_video=videos[num-1])

@app.route('/2', methods=['GET', 'POST'])
def vid_2():
    num = 2
    # always "blindly" load the user
    video = Video(user_name=session['user_name'],video=str(num))
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
        return redirect(url_for('vid_3'))
    return render_template('segments.html', form=form, num=num, this_video=videos[num-1])

@app.route('/3', methods=['GET', 'POST'])
def vid_3():
    num = 3
    # always "blindly" load the user
    video = Video(user_name=session['user_name'],video=str(num))
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
        return redirect(url_for('vid_4'))
    return render_template('segments.html', form=form, num=num, this_video=videos[num-1])

@app.route('/4', methods=['GET', 'POST'])
def vid_4():
    num = 4
    # always "blindly" load the user
    video = Video(user_name=session['user_name'],video=str(num))
    # video = Video.query.first()

    # if User has no phones, provide an empty one so table is rendered
    if len(video.segments) == 0:
        video.segments = [Segment(start_time="0",end_time="10")]
        # flash("empty Segment provided")

    # else: forms loaded through db relation
    form = CombinedForm(obj=video)

    if form.validate_on_submit():
        form.populate_obj(video)
        db.session.add(video)
        db.session.commit()
        flash("Saved Changes")
        return redirect(url_for('thanks'))
    return render_template('segments.html', form=form, num=num, this_video=videos[num-1])

@app.route('/thanks', methods=['GET', 'POST'])
def thanks():
    return render_template('thanks.html',
                           user=session['user_name'])