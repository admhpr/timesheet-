import re
import datetime

get_date = datetime.datetime.today() #day script is run
days_working = 5 #amount of working days
work_week = []
dateRegEx = re.compile(r'(\d\d\d\d)-(\d\d-\d\d)')

for i in range (days_working):
    work_week.append(get_date + datetime.timedelta(days=i))

for i in range (0, len(work_week)):

   string_list = ''.join(str(e) for e in work_week)

mo = dateRegEx.findall(string_list)

timesheet_days = [x[1] for x in mo]

print('| Date | Start Time| End Time | Hours Worked ') 
for i in range (0, len(timesheet_days)):
   
    print('| ' + timesheet_days[i] + ' | x: | x: | x: |')

print('| Weekly Total: | | <3 | %CALC{"$SUM( $ABOVE() )"}% |')

    


    

    
