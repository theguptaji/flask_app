import numpy as np
import sys
from flaskblog import create_app

app = create_app()
app = app.app_context().push()

from flaskblog import db
from flaskblog.models import User, Calender, Shift

# Get all entries from calender
# schedule_list = Calender.query.all()


all_schedule = []
# process the values in a list of users
for schedule in Calender.query.order_by("date_posted"):
	all_schedule.append(schedule.get_all())

sa_schedules = np.array(all_schedule)
# print(sa_schedules)

# logic
num_of_sa = len(sa_schedules)

if num_of_sa!=0:
	max_hours = 48/num_of_sa
else:
	sys.exit()

row = sa_schedules.shape[0]
col = sa_schedules.shape[1]

shifts = np.zeros(shape = (6, 3))
total_val = np.zeros(row)

slots_allotted = []
people_allotted = []

for i in range(0,row):
	for j in range(1, 7):
		if sa_schedules[i][j*4] and shifts[j-1][:].all()==0:
			shifts[j-1][:] = sa_schedules[i][0]
			slots_allotted.extend([j*4-3,j*4-2,j*4-1,j*4])
			people_allotted.append(i)
			total_val[i]=8
			break


slots_copy = slots_allotted

for x in [i for i in range(0,row) if i not in people_allotted]:
	for y in [j for j in range(1,col) if j not in slots_copy]:
		if sa_schedules[x][y] and total_val[x]<=8 and shifts[int(y/4)][(int(y%4))-1]==0:
			shifts[int(y/4)][(int(y%4))-1] = sa_schedules[x][0]
			slots_allotted.append(y)
			if (y%4) == 1:
				total_val[x]+=2
			else:
				total_val[x]+=3

slots_copy = slots_allotted

for i in [j for j in range(1,col) if j not in slots_copy]:
	for x in range(0,row):
		if sa_schedules[x][i] and total_val[x]<=14 and shifts[int(i/4)][(int(i%4))-1]==0:
			# print(f'user:{x+1} for slot {i}')
			shifts[int(i/4)][(int(i%4))-1] = sa_schedules[x][0]
			slots_allotted.append(i)
			if (i%4) == 1:
				total_val[x]+=2
			else:
				total_val[x]+=3

 		
# print(shifts)

# sa_schedules[x][4*y] = whole day schedule of days
# shifts = shifts.reshape(18,2)
shifts = shifts.flatten()
# print(shifts)

# change the values of existing shifts
Shift.query.filter_by(id=1).delete()
# db.session.commit()

shifts_t = Shift(mon1=User.query.get(shifts[0]).username if shifts[0]!=0 else 'free',
				mon2=User.query.get(shifts[1]).username if shifts[1]!=0 else 'free',
				mon3=User.query.get(shifts[2]).username if shifts[2]!=0 else 'free',
				tues1=User.query.get(shifts[3]).username if shifts[3]!=0 else 'free',
				tues2=User.query.get(shifts[4]).username if shifts[4]!=0 else 'free',
				tues3=User.query.get(shifts[5]).username if shifts[5]!=0 else 'free',
				wed1=User.query.get(shifts[6]).username if shifts[6]!=0 else 'free',
				wed2=User.query.get(shifts[7]).username if shifts[7]!=0 else 'free',
				wed3=User.query.get(shifts[8]).username if shifts[8]!=0 else 'free',
				thurs1=User.query.get(shifts[9]).username if shifts[9]!=0 else 'free',
				thurs2=User.query.get(shifts[10]).username if shifts[10]!=0 else 'free',
				thurs3=User.query.get(shifts[11]).username if shifts[11]!=0 else 'free',
				fri1=User.query.get(shifts[12]).username if shifts[12]!=0 else 'free',
				fri2=User.query.get(shifts[13]).username if shifts[13]!=0 else 'free',
				fri3=User.query.get(shifts[14]).username if shifts[14]!=0 else 'free',
				sat1=User.query.get(shifts[15]).username if shifts[15]!=0 else 'free',
				sat2=User.query.get(shifts[16]).username if shifts[16]!=0 else 'free',
				sat3=User.query.get(shifts[17]).username if shifts[17]!=0 else 'free')

print(shifts_t)
db.session.add(shifts_t)
db.session.commit()
# Drop all values in Calender database
Calender.query.delete()
db.session.commit()
# commit to database