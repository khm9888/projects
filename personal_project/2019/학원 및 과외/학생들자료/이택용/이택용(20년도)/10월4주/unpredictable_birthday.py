

from datetime import date

import datetime

def birthday(date1, date2):#생일이 맞는지 월,일
    date1 = str(date1)
    date2 = str(date2)
    date1 = date1.replace("-", "")
    date2 = date2.replace("-", "")
    if date1[4:] == date2[4:]:
        return True
    else:
        return False


def sameweekday(date1, date2):#일 과 요일이 맞는지
    if date1.day==date2.day and date1.weekday()==date2.weekday():
        return True
    else:
        return False        

def hundredday(date1, date2):#차이가 100의 배수인가
    days = (date2-date1).days
    if days%100==0:
        return True
    else:
        return False



def unbirthday(date1, date2):#생일이 아니라면, True
    date1 = str(date1)
    date2 = str(date2)
    if date1[5:] == date2[5:]:
        return False
    else:
        return True


def birthdays(birth,end=date.today(), birthday=birthday,start=None):
    if start==None:
        start_day = birth.toordinal()
    else:
        start_day = start.toordinal()
    end_day = end.toordinal()
    birthdays_list=list()
    for day in range(start_day,end_day+1):
        day_short=(date.fromordinal(day))
        if birthday(birth,day_short):
            birthdays_list.append(day_short)
    return tuple(birthdays_list)

