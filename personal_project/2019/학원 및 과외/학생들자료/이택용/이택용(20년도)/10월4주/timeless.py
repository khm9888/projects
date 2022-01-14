
import datetime

def leapyear(y):
    if (y%4==0 and y%100!=0) or y%400==0:
        return True
    else:
        return False
    
def first_difference(year1, year2):
    
    # year1,year2=min(year1,year2),max(year1,year2)
    year1_leapyear= leapyear(year1)
    year2_leapyear= leapyear(year2)
    
    # print(year1_leapyear)
    # print(year2_leapyear)
    
    month=1
    day=1
    
    year1_first_day = datetime.date(year1,month,day)
    year2_first_day = datetime.date(year2,month,day)
    
    if year1_first_day.weekday()==year2_first_day.weekday():
        if year1_leapyear == year2_leapyear: #none
            return None
        elif year1_leapyear == True and False== year2_leapyear:
            return datetime.date(year2,3,1)
        elif year1_leapyear == False and True== year2_leapyear:
            return datetime.date(year2,2,29)
    else:
        return datetime.date(year2,month,day)

        
def reuse_calendar(year1,previous=False):
    year2=int(year1)
    month=1
    day=1
    while True:
        if not previous:
            year2+=1
        else:
            year2-=1          
        if first_difference(year1,year2) is None:
            return year2           

def reuse_calendars(year1,cnt=10,previous=False):

    year2=int(year1)
    month=1
    day=1
    answers = []
    while True:
        if not previous:
            year2+=1
        else:
            year2-=1          
        if first_difference(year1,year2) is None:
            answers.append(year2)
        if len(answers)==cnt:
            return answers       
            
        # # print(year2)
        # year1_first_day = datetime.date(year1,month,day)
        # year2_first_day = datetime.date(year2,month,day)
        # year1_leapyear= leapyear(year1)
        # year2_leapyear= leapyear(year2)
        # if year1_first_day.weekday()==year2_first_day.weekday():
        #     if year1_leapyear == year2_leapyear: #none
            
    
    
    


# v= first_difference(2018, 2019)
# datetime.date(2019, 1, 1)
# first_difference(2018, 2024)
# datetime.date(2024, 2, 29)
# first_difference(2018, 2029)

v=reuse_calendar(2018)
# 2029
# v=reuse_calendar(2018, True)
# 2007
# v=reuse_calendar(2019, previous=False)
# 2030
# reuse_calendar(2019, previous=True)
# 2013

# reuse_calendars(2018, 10)
# [2029, 2035, 2046, 2057, 2063, 2074, 2085, 2091, 2103, 2114]
# reuse_calendars(2018, 10, True)
# [2007, 2001, 1990, 1979, 1973, 1962, 1951, 1945, 1934, 1923]
# reuse_calendars(2019, 10, previous=False)
# [2030, 2041, 2047, 2058, 2069, 2075, 2086, 2097, 2109, 2115]
# reuse_calendars(2019, 10, previous=True)
# [2013, 2002, 1991, 1985, 1974, 1963, 1957, 1946, 1935, 1929]

print(v)