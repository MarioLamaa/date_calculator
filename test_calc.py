'''
This programme tests the date calculator to ensure that the backend calculations for the web application provide the answers expected.

'''


# Imports relevant function to format date inputs and calculations from back-end programme 

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
    
def test_zero_duration():
    # initialise user inputs for a choice of two different dates
    start_date = datetime.datetime(2021,11,16)
    end_date = datetime.datetime(2021,11,16)
    # calculate the difference when the day is the same
    difference = duration(start_date, end_date)
    # check the resulting answer
    assert difference == 0
    
def test_duration_negative():
    # initialise user inputs for a choice of two different dates
    start_date = datetime.datetime(2021,11,15)
    end_date = datetime.datetime(2021,11,9)
    # calculate the difference in days between the two dates
    difference = duration(start_date, end_date)
    # check the resulting answer
    assert difference == 6
    

