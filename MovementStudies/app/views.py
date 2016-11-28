from flask import render_template, flash, redirect, session, url_for
from app import app
from app import db
from .forms import UserForm, SegmentForm, CombinedForm, RenewForm
from .models import User, Segment, Video, Numbers
import random

videos = [#'static/blurredVideos/video1.mp4',
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
    user = User(user_name="name",numvideos=1,whichvideos="")
    form = UserForm()
    if form.validate_on_submit():
        # flash('Data requested for business_name="%s", owner="%s", business_type="%s", location="%s"' %
        #   (form.business_name.data, form.owner.data, form.business_type.data, form.location.data))
        session['user_name'] = form.user_name.data
        form.populate_obj(user)
        present = User.query.filter(User.user_name == session['user_name']).first()
        if not present:
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
    user = User.query.filter(User.user_name == session['user_name']).first()
    if not user:
        return redirect(url_for('renew_user'))
    user_num = user.numvideos
    if not user_num:
        user_num = 1
    numbers = Numbers.query.get(1)
    num = numbers.num
    if user.whichvideos:
        if str(num+1) in user.whichvideos.split(' ')[len(user.whichvideos.split(' '))-1]:
            flash("It's likely that your last submission did not go through. If the data is still there, please submit it again.")
        elif str(num+1) in user.whichvideos.split(' '):
            while str(num+1) in user.whichvideos.split(' '):
                if str(1) in user.whichvideos.split(' ') and str(2) in user.whichvideos.split(' ') and str(3) in user.whichvideos.split(' ') and str(4) in user.whichvideos.split(' '):
                    return redirect(url_for('moVid2'))
                print "changed moNum, already seen"
                num += 1
                num=num%len(videos)
    else:
        user.whichvideos = ''
    user.whichvideos += str(num+1)+' '

    print "NUMBERS", "which", user.whichvideos, "usernum",user_num
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
        flash("Saved Changes! You're doing great! Let's do another video!")
        num += 1
        num=num%len(videos)
        numbers.num = num
        user.numvideos = user_num +1
        db.session.commit()
        print "NUMBERS", "which", user.whichvideos,"usernum",user_num
        if form.complete.data:
            return redirect(url_for('thanks'))
        else:
            return redirect(url_for('moVid'))
    return render_template('segments.html', form=form, num=num+1, this_video=videos[num], duration=durations[num], choice=0, user_num=user_num)

@app.route('/video2', methods=['GET', 'POST'])
def vid2():
    #global num
    user = User.query.filter(User.user_name == session['user_name']).first()
    if not user:
        return redirect(url_for('renew_user'))
    user_num = user.numvideos
    numbers = Numbers.query.get(1)

    num = numbers.num
    if user.whichvideos:
        if str(num+1) in user.whichvideos.split(' ')[len(user.whichvideos.split(' '))-1]:
            flash("It's likely that your last submission did not go through. If the data is still there, please submit it again.")
        elif str(num+1) in user.whichvideos.split(' '):
            while str(num+1) in user.whichvideos.split(' '):
                if str(1) in user.whichvideos.split(' ') and str(2) in user.whichvideos.split(' ') and str(3) in user.whichvideos.split(' ') and str(4) in user.whichvideos.split(' '):
                    return redirect(url_for('moVid2'))
                print "changed moNum, already seen"
                num += 1
                num=num%len(videos)
    else:
        user.whichvideos = ''
    user.whichvideos += str(num+1)+' '

    print "NUMBERS", "which", user.whichvideos, "usernum",user_num
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
        flash("Saved Changes! You're doing great! Let's do another video!")
        num += 1
        num=num%len(videos)
        numbers.num = num
        user_num += 1
        user.numvideos = user_num
        db.session.commit()
        print "NUMBERS", "which", user.whichvideos, "usernum",user_num
        if form.complete.data:
            return redirect(url_for('thanks'))
        else:
            choice = random.randint(1, 3)
            if choice==1:
                return redirect(url_for('vid2'))
            else:
                return redirect(url_for('moVid2'))
    return render_template('segments.html', form=form, num=num+1, this_video=videos[num], duration=durations[num], choice=1, user_num=user_num)

@app.route('/moVideo', methods=['GET', 'POST'])
def moVid():
    #global moNum
    user = User.query.filter(User.user_name == session['user_name']).first()
    if not user:
        return redirect(url_for('renew_user'))
    print session['user_name']
    user_num = user.numvideos
    numbers = Numbers.query.get(1)
    moNum = numbers.moNum
    if user.whichvideos:
        if str(moNum+5) in user.whichvideos.split(' ')[len(user.whichvideos.split(' '))-1]:
            flash("It's likely that your last submission did not go through. If the data is still there, please submit it again.")
        elif str(moNum+5) in user.whichvideos.split(' '):
            while str(moNum+5) in user.whichvideos.split(' '):
                if str(5) in user.whichvideos.split(' ') and str(6) in user.whichvideos.split(' ') and str(7) in user.whichvideos.split(' ') and str(8) in user.whichvideos.split(' ') and str(9) in user.whichvideos.split(' ') and str(10) in user.whichvideos.split(' ') and str(11) in user.whichvideos.split(' ') and str(12) in user.whichvideos.split(' '):
                    if str(1) in user.whichvideos.split(' ') and str(2) in user.whichvideos.split(' ') and str(3) in user.whichvideos.split(' ') and str(4) in user.whichvideos.split(' '):
                        return redirect(url_for('thanks'))
                    else:
                        return redirect(url_for('vid2'))
                print "changed moNum, already seen"
                moNum += 1
                moNum=moNum%len(mocapVideos)
    else:
        user.whichvideos = ''
    user.whichvideos += str(moNum+5)+' '

    print "NUMBERS", "which", user.whichvideos,"usernum",user_num
    # always "blindly" load the user
    video = Video(user_name=session['user_name'],video=str(moNum+5))
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
        flash("Saved Changes! You're doing great! Let's do another video!")
        moNum += 1
        moNum=moNum%len(mocapVideos)
        numbers.moNum = moNum
        user_num += 1
        user.numvideos = user_num
        db.session.commit()
        print "NUMBERS", "which", user.whichvideos, "usernum",user_num
        if form.complete.data:
            return redirect(url_for('thanks'))
        else:
            return redirect(url_for('moVid2'))
    return render_template('segments.html', form=form, num=moNum+1, this_video=mocapVideos[moNum], duration=moDurations[moNum],choice=0,user_num=user_num)

@app.route('/moVideo2', methods=['GET', 'POST'])
def moVid2():
    #global moNum
    user = User.query.filter(User.user_name == session['user_name']).first()
    if not user:
        return redirect(url_for('renew_user'))
    user_num = user.numvideos
    numbers = Numbers.query.get(1)
    moNum = numbers.moNum
    if user.whichvideos:
        if str(moNum+5) in user.whichvideos.split(' ')[len(user.whichvideos.split(' '))-1]:
            flash("It's likely that your last submission did not go through. If the data is still there, please submit it again.")
        elif str(moNum+5) in user.whichvideos.split(' '):
            while str(moNum+5) in user.whichvideos.split(' '):
                if str(5) in user.whichvideos.split(' ') and str(6) in user.whichvideos.split(' ') and str(7) in user.whichvideos.split(' ') and str(8) in user.whichvideos.split(' ') and str(9) in user.whichvideos.split(' ') and str(10) in user.whichvideos.split(' ') and str(11) in user.whichvideos.split(' ') and str(12) in user.whichvideos.split(' '):
                    if str(1) in user.whichvideos.split(' ') and str(2) in user.whichvideos.split(' ') and str(3) in user.whichvideos.split(' ') and str(4) in user.whichvideos.split(' '):
                        return redirect(url_for('thanks'))
                    else:
                        return redirect(url_for('vid2'))
                print "changed moNum, already seen"
                moNum += 1
                moNum=moNum%len(mocapVideos)
    else:
        user.whichvideos = ''
    user.whichvideos += str(moNum+5)+' '
    
    print "NUMBERS", "which", user.whichvideos,"usernum",user_num
    # always "blindly" load the user
    video = Video(user_name=session['user_name'],video=str(moNum+5))
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
        flash("Saved Changes! You're doing great! Let's do another video!")
        moNum += 1
        moNum=moNum%len(mocapVideos)
        numbers.moNum = moNum
        user_num += 1
        user.numvideos = user_num
        db.session.commit()
        print "NUMBERS", "which", user.whichvideos, "usernum",user_num
        if form.complete.data:
            return redirect(url_for('thanks'))
        else:
            choice = random.randint(1, 3)
            if choice==1:
                return redirect(url_for('vid2'))
            else:
                return redirect(url_for('moVid2'))
    return render_template('segments.html', form=form, num=moNum+1, this_video=mocapVideos[moNum], duration=moDurations[moNum],choice=1,user_num=user_num)


@app.route('/thanks', methods=['GET', 'POST'])
def thanks():
    return render_template('thanks.html',
                           user=session['user_name'])

@app.route('/renew_user', methods=['GET', 'POST'])
def renew_user():
    user = User(user_name="name",numvideos=1,whichvideos="")
    form = RenewForm()
    if form.validate_on_submit():
        # flash('Data requested for business_name="%s", owner="%s", business_type="%s", location="%s"' %
        #   (form.business_name.data, form.owner.data, form.business_type.data, form.location.data))
        session['user_name'] = form.user_name.data
        form.populate_obj(user)
        present = User.query.filter(User.user_name == session['user_name']).first()
        if not present:
            db.session.add(user)
        db.session.commit()
        return redirect(url_for('instruct'))
    return render_template('renew.html',
                           form=form)