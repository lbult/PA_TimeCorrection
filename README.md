# PA_TimeCorrection

## How to use

Using the functions in "time_correction.py" you will be able to find the time correction value from UTC to UT1 and GPS and/or TAI. 

The function findDUT1Correction(year,day,month) returns the DUT1 time correction (float) and requires three input arguments (in string format), where the year is the last two digits of the calendar year, and the day and month are two digits (month example: 01 or 11)(day example: 05 or 31).

The function findLeapSeconds(year) returns the amount of leap seconds (float) on a certain data and requires one input argument (in string format). The input argument is the current 4-digit year.

## Example

An example is provided below. First you specify a date, after which you can slice the date to comply to input specifications. You then save the function return in variables DUTone and leap_seconds.

~~~
today = "2022-11-28"
DUTone = findDUT1Correction(today[2:4],today[8:10],today[5:7])
leap_seconds = findLeapSeconds(today[0:4])
~~~
