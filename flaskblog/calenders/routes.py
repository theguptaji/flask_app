import datetime
from flask import (render_template, url_for, flash,
                   redirect, request, abort, Blueprint)
from flask_login import current_user, login_required
from flaskblog import db
from flaskblog.models import Calender
from flaskblog.calenders.forms import CalenderForm

calenders = Blueprint('calenders', __name__)

def val_func(x):
    if x:
        return 'Available'
    else:
        return '-'

def weekdays(x):
    today = datetime.date.today()
    the_day = today + datetime.timedelta(days=-today.weekday()+x, weeks=1)
    return the_day

@calenders.route("/calender/fill", methods=['GET', 'POST'])
@login_required
def calender_fill():
    form = CalenderForm()
    if Calender.query.get(current_user.get_id()) is None:
        if form.validate_on_submit():
            calender = Calender(mon1=form.mon1.data, mon2=form.mon2.data, mon3=form.mon3.data, mon4=form.mon4.data,
            					tues1=form.tues1.data, tues2=form.tues2.data, tues3=form.tues3.data, tues4=form.tues4.data,
            					wed1=form.wed1.data, wed2=form.wed2.data, wed3=form.wed3.data, wed4=form.wed4.data,
            					thurs1=form.thurs1.data, thurs2=form.thurs2.data, thurs3=form.thurs3.data, thurs4=form.thurs4.data,
            					fri1=form.fri1.data, fri2=form.fri2.data, fri3=form.fri3.data, fri4=form.fri4.data,
            					sat1=form.sat1.data, sat2=form.sat2.data, sat3=form.sat3.data, sat4=form.sat4.data,
            					 author=current_user)
            db.session.add(calender)
            db.session.commit()
            flash('Your schedule has been submitted!', 'success')
            return redirect(url_for('main.home'))
    else:
        return redirect(url_for('calenders.calender'))

    return render_template('fill_schedule.html', title='Schedule',
                           form=form, weekdays=weekdays, legend='Schedule')


@calenders.route("/calender")
def calender():
    calender = Calender.query.get_or_404(current_user.get_id())
    return render_template('calender.html', calender=calender,
                            val_func=val_func, weekdays=weekdays, legend='Your Schedule')

@calenders.route("/calender/update", methods=['GET', 'POST'])
@login_required
def update():
    calender = Calender.query.get_or_404(current_user.get_id())
    form = CalenderForm()
    if form.validate_on_submit():
        calender.mon1 = form.mon1.data
        calender.mon2 = form.mon2.data
        calender.mon3 = form.mon3.data
        calender.mon4 = form.mon4.data
        calender.tues1 = form.tues1.data
        calender.tues2 = form.tues2.data
        calender.tues3 = form.tues3.data
        calender.tues4 = form.tues4.data
        calender.wed1 = form.wed1.data
        calender.wed2 = form.wed2.data
        calender.wed3 = form.wed3.data
        calender.wed4 = form.wed4.data
        calender.thurs1 = form.thurs1.data
        calender.thurs2 = form.thurs2.data
        calender.thurs3 = form.thurs3.data
        calender.thurs4 = form.thurs4.data
        calender.fri1 = form.fri1.data
        calender.fri2 = form.fri2.data
        calender.fri3 = form.fri3.data
        calender.fri4 = form.fri4.data
        calender.sat1 = form.sat1.data
        calender.sat2 = form.sat2.data
        calender.sat3 = form.sat3.data
        calender.sat4 = form.sat4.data
        db.session.commit()
        flash('Your calender has been updated!', 'success')
        return redirect(url_for('calenders.calender'))
    elif request.method == 'GET':
        form.mon1.data = calender.mon1
        form.mon2.data = calender.mon2
        form.mon3.data = calender.mon3
        form.mon4.data = calender.mon4
        form.tues1.data = calender.tues1
        form.tues2.data = calender.tues2
        form.tues3.data = calender.tues3
        form.tues4.data = calender.tues4
        form.wed1.data = calender.wed1
        form.wed2.data = calender.wed2
        form.wed3.data = calender.wed3
        form.wed4.data = calender.wed4
        form.thurs1.data = calender.thurs1
        form.thurs2.data = calender.thurs2
        form.thurs3.data = calender.thurs3
        form.thurs4.data = calender.thurs4
        form.fri1.data = calender.fri1
        form.fri2.data = calender.fri2
        form.fri3.data = calender.fri3
        form.fri4.data = calender.fri4
        form.sat1.data = calender.sat1
        form.sat2.data = calender.sat2
        form.sat3.data = calender.sat3
        form.sat4.data = calender.sat4
    return render_template('fill_schedule.html', title='Update Schedule',
                           form=form, weekdays=weekdays, legend='Update Schedule')