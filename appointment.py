# "Finding an Appointment"
# Codewars kata url: https://www.codewars.com/kata/525f277c7103571f47000147
#
# Takes in a list of schedules and a duration. Finds the earliest appointment of 
# the specified duration that fits all the schedules.
#
# Author: Jennine Nash (2016)

# converts a number of minutes into a string of the form hh:mm
def comp_ans(mins):
    h = str(int(mins // 60)).zfill(2)
    m = str(int(mins % 60)).zfill(2)
    return h + ':' + m

def get_start_time(schedules, duration):
    meetings = []
    
    for b in range(0, len(schedules)):
       
		# creates a new list which holds the schedules all people
		# with times represented as floats instead of strings
        for i in range(0, len(schedules[b])):
            m = schedules[b][i]
            colon1 = m[0].index(':')
            h1 = int(m[0][0:colon1])
            m1 = float(m[0][colon1+1:])/60
            
            colon2 = m[1].index(':')
            h2 = int(m[1][0:colon2])
            m2 = float(m[1][colon2+1:])/60
            meetings.append([h1+m1, h2+m2])
    
	# sorts all the combined meetings and adds earliest and latest times
    meetings.sort(key=lambda x: x[0])
    meetings.append([19.0, 19.0])
    meetings = [[9.0, 9.0]] + meetings
    
	# groups meetings into larger blocks of times
	# each block represents a length of time when at least one person is in a meeting
    for m in range(1, len(meetings)):
        s1 = meetings[m-1][0]
        f1 = meetings[m-1][1]
        s2 = meetings[m][0]
        f2 = meetings[m][1]
        
        if s2 <= f1:
            meetings[m][0] = s1
            if f1 >= f2:
                meetings[m][1] = f1
            meetings[m-1] = None
    
    meetings = [x for x in meetings if x != None]
    
	# finds first free space of at least the specified duration
    for i in range(1, len(meetings)):
        f1 = meetings[i-1][1]
        s2 = meetings[i][0]
        
        if s2*60 - f1*60 >= duration:
            return comp_ans(f1*60)