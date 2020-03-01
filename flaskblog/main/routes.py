import datetime
from flask import render_template, request, Blueprint
from flaskblog.models import Post, Shift

main = Blueprint('main', __name__)

def weekdays(x):
	today = datetime.date.today()
	the_day = today + datetime.timedelta(days=-today.weekday()+x, weeks=1)
	return the_day

@main.route("/")
@main.route("/home")
def home():
	page = request.args.get('page', 1, type=int) 
	posts = Post.query.order_by(Post.date_posted.desc()).paginate(page=page, per_page=5)
	return render_template('home.html', posts=posts)


@main.route("/week_shift")
def week_shift():
	shifts = Shift.query.get(1)
	return render_template('shifts.html', title='About',
    						 shifts=shifts, weekdays=weekdays, legend='This week\'s shift')