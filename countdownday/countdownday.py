import datetime
def count_down_day(dates):
    '''
    return the days until today
    parameters:
    --------------
    yyyy(int):year
    mm(int):month
    dd(int):day
    '''
    yyyy=int(dates.split(",")[0])
    mm=int(dates.split(",")[1])
    dd=int(dates.split(",")[2])
    currday=datetime.date.today()
    gday=datetime.date(yyyy,mm,dd)
    if currday < gday:
        diff = gday - currday
        print(f"{diff.days} days until {yyyy}.{mm}.{dd}")
    elif currday > gday:
        diff = currday - gday
        print(f"{diff.days} days since {yyyy}.{mm}.{dd}")
    else:
        print(f"{currday} is today")

if __name__=='__main__':
    count_down_day("1997,3,6")
    count_down_day("2077,12,25")