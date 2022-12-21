import pendulum

def clean_date(input_string):
    year, month, day = [int(date_part) for date_part in input_string.split('-')]
    
    return pendulum.Date(year, month, day)