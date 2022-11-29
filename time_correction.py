from urllib.request import urlopen

def findDUT1Correction(year,day,month):
    '''
    Input: year,month,day (2-digit),(2-digit),(2-digit) (str) e.g. 22,06,01
    Output: DUT1 = UTC-UT1 correction (float)
    -----
    # Web scraping and automated UTC-UT1 finder (only double digit day dates), used https://realpython.com/python-web-scraping-practical-introduction/
    '''
    # gather all data
    url = "https://maia.usno.navy.mil/ser7/finals.daily"
    open = urlopen(url)
    html = open.read()
    html = html.decode("utf-8")
    # initialise the slice strings
    begin_string = year+month+day
    nextDay = str(int(day) + 1)
    if int(day) < 10:
        end_string = year+month+"0"+nextDay 
    else:
        end_string = year+month+nextDay
    #slice string
    begin_index = html.find(begin_string)
    end_index = html.find(end_string)
    DUTone = html[begin_index:end_index]
    DUTone = float(DUTone[59:68]) # time correction in seconds
    return DUTone

def findLeapSeconds(year_in):
    '''
    Input: year (4-digit) (str)
    Output: leap-second correction (float)
    -----
    Web scraping and automated leap seconds finder, used https://realpython.com/python-web-scraping-practical-introduction/
    '''
    url = "https://maia.usno.navy.mil/ser7/tai-utc.dat"
    open = urlopen(url)
    html = open.read()
    html = html.splitlines()
    year = year_in
    for i in html:
        i = i.decode('utf-8')
        minimum = 1000
        leap_year = i[0:5]
        if float(year) - float(leap_year) < minimum:
            minimum = float(year) - float(leap_year)
            leap_seconds = float(i[38:42])
    return leap_seconds