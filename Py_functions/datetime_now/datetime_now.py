from datetime import datetime

now = datetime.now()
print now

#get individual year, month, day
print now
print now.year
print now.month
print now.day

#display the date dd/mm/yyyy using string substitution
print "Todays date is %s/%s/%s" % (now.day,now.month,now.year)

#display the time in military 24hr format
print "Current time is %s:%s:%s" % (now.hour,now.minute,now.second)
