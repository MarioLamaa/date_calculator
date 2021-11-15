'''
This programme tests the date calculator

Types of tests:
Logic of the calculation
Is the data type we expect
Boundaries for inputs

'''
import datetime
from datecalc import duration, when

# test that checks functionality of testing 

def test_functionality():
   assert 10 == 6 + 4

# test that the days between functionality works to add the number of days
   
def test_logic_when():
    # initialise user inputs for start date and duration of days
    start_date2 = datetime.datetime(2021,11,20)
    days_between = 10
    # calculate the answer for what the new date would be
    answer = when(start_date2, days_between)
    # check the resulting answer
    assert answer == datetime.datetime(2021,11,30)
    
def test_logic_duration():
    # initialise user inputs for a choice of two different dates
    start_date = datetime.datetime(2021,11,10)
    end_date = datetime.datetime(2021,11,25)
    # calculate the difference in days between the two dates
    difference = duration(start_date, end_date)
    # check the resulting answer
    assert difference == 15
    
def test_zero_when():
    # initialise user inputs for adding zero days
    start_date2 = datetime.datetime(2021,11,20)
    days_between = 0
    # calculate new date based on zero input
    answer = when(start_date2, days_between)
    # check the resulting date hasn't changed
    assert answer == datetime.datetime(2021,11,20)
    
def test_logic_negative():
    # initialise user inputs for a choice of two different dates
    start_date = datetime.datetime(2021,11,15)
    end_date = datetime.datetime(2021,11,9)
    # calculate the difference in days between the two dates
    difference = duration(start_date, end_date)
    # check the resulting answer
    assert difference == 6

    
