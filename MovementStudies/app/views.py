from flask import render_template, flash, redirect, session, url_for
from app import app
from app import db
from .forms import UserForm, SegmentForm, CombinedForm
from .models import User, Segment, Video, Numbers
import random

videos = [#'static/blurredVideos/video1.mov',
'static/blurredVideos/video2.mp4',
#'static/blurredVideos/video3.mov',
'static/blurredVideos/video4.mp4',
'static/blurredVideos/video5.mp4',
'static/blurredVideos/video6.mp4']

mocapVideos = ['static/mocapVideos/AlisonAngryClip.mp4',
'static/mocapVideos/EdwinContentClip.mp4',
'static/mocapVideos/AlisonJoyfulClip.mp4',
'static/mocapVideos/EdwinSadClip.mp4',
'static/mocapVideos/AlisonContentClip.mp4',
'static/mocapVideos/EdwinAngryClip.mp4',
'static/mocapVideos/AlisonSadClip.mp4',
'static/mocapVideos/EdwinJoyfulClip.mp4']

#durations = [25.088,33.976289,34.416667,25.68127,21.182211,24.4]
durations = [29.504,25.301333,20.309333,22.378667]

moDurations = [31.296,29.290667,35.093333,31.445333,39.68,30.08,29.290667,29.482667]
# You will be presented with 3 short videos.

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
    #global num
    numbers = Numbers.query.get(1)
    num = numbers.num
    print "NUM", num
    # always "blindly" load the user
    video = Video(user_name=session['user_name'],video=str(num+1))
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
        flash("Saved Changes")
        num += 1
        num=num%len(videos)
        numbers.num = num
        db.session.commit()
        print num
        if form.complete.data:
            return redirect(url_for('thanks'))
        else:
            return redirect(url_for('moVid'))
    return render_template('segments.html', form=form, num=num+1, this_video=videos[num], duration=durations[num], choice=0)

@app.route('/video2', methods=['GET', 'POST'])
def vid2():
    #global num
    numbers = Numbers.query.get(1)
    num = numbers.num
    print "NUM", num
    # always "blindly" load the user
    video = Video(user_name=session['user_name'],video=str(num+1))
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
        flash("Saved Changes")
        num += 1
        num=num%len(videos)
        numbers.num = num
        db.session.commit()
        if form.complete.data:
            return redirect(url_for('thanks'))
        else:
            choice = random.randint(1, 3)
            if choice==1:
                return redirect(url_for('vid2'))
            else:
                return redirect(url_for('moVid2'))
    return render_template('segments.html', form=form, num=num+1, this_video=videos[num], duration=durations[num], choice=1)

@app.route('/moVideo', methods=['GET', 'POST'])
def moVid():
    #global moNum
    numbers = Numbers.query.get(1)
    moNum = numbers.moNum
    print "NUM", moNum
    # always "blindly" load the user
    video = Video(user_name=session['user_name'],video=str(moNum+1))
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
        flash("Saved Changes")
        moNum += 1
        moNum=moNum%len(videos)
        numbers.moNum = moNum
        db.session.commit()
        print moNum
        if form.complete.data:
            return redirect(url_for('thanks'))
        else:
            return redirect(url_for('moVid2'))
    return render_template('segments.html', form=form, num=moNum+1, this_video=mocapVideos[moNum], duration=moDurations[moNum],choice=0)

@app.route('/moVideo2', methods=['GET', 'POST'])
def moVid2():
    #global moNum
    numbers = Numbers.query.get(1)
    moNum = numbers.moNum
    print "NUM", moNum
    # always "blindly" load the user
    video = Video(user_name=session['user_name'],video=str(moNum+1))
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
        flash("Saved Changes")
        moNum += 1
        moNum=moNum%len(videos)
        numbers.moNum = moNum
        db.session.commit()
        print moNum
        if form.complete.data:
            return redirect(url_for('thanks'))
        else:
            choice = random.randint(1, 3)
            if choice==1:
                return redirect(url_for('vid2'))
            else:
                return redirect(url_for('moVid2'))
    return render_template('segments.html', form=form, num=moNum+1, this_video=mocapVideos[moNum], duration=moDurations[moNum],choice=1)


@app.route('/thanks', methods=['GET', 'POST'])
def thanks():
    return render_template('thanks.html',
                           user=session['user_name'])