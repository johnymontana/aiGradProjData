import pickle
from datetime import datetime
from datetime import timedelta
from datetime import date

def daterange(start_date, end_date):
    for n in range(int ((end_date - start_date).days)):
        yield start_date + timedelta(n)

fkl_file = open('newsDict2.pkl', 'rb')
newsDict = pickle.load(fkl_file)
fkl_file.close()
start_date=date(2011, 7, 27)
end_date = date(2012, 11, 9)
totaldays = 0
numStories = 0
for single_date in daterange(start_date, end_date):
	totaldays += 1
	print single_date
	for newsItem in newsDict[single_date]:
		numStories += 1
		print str(single_date) + newsItem


print "Total number of days: " + str(totaldays)
print "Total number of stories " + str(numStories)
print "Avg stories per day: " + str(numStories/totaldays) 
