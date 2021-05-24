# Python3 code to calculate age in years 

import datetime

def calculateAge(birthDate): 
	today = datetime.date.today() 
	age = today.year - birthDate.year -((today.month, today.day) < (birthDate.month, birthDate.day)) 

	return age 
	
# Driver code
def calcu(a,b,c):
    print(type(a),type(b),type(c),a,b,c)
    print(calculateAge(datetime.date(int(a), int(b), int(c))), "years")
    return calculateAge(datetime.date(int(a), int(b), int(c)))
