print ("\f")
''' to clear the screen '''


import pandas as pd
from datetime import datetime 
from datetime import timedelta 
import time


'''THE FILE USED IN THIS PROGRAMME ARE BELOW'''
chicago = 'chicago.csv'
new_york_city = 'new_york_city.csv'
washington = 'washington.csv'

'''SOME GREETINGS BELOW'''
s = input("please enter you name :")
s = s+' sir,'
print ("\nHello {} \nLet\'s explore some US bikeshare data!".format(s))


'''TOO GET THE CITY WHICH THE USER WANT TO FILTER DATA FROM'''
def get_city():
    
    city = ''
    while city.lower() not in ['chicago', 'new york', 'washington']:
        city = input('Please choose from one of these cities Chicago, New York, or'
                     ' Washington?\n')
        if city.lower() == 'chicago':
            return 'chicago.csv'
        elif city.lower() == 'new york':
            return 'new_york_city.csv'
        elif city.lower() == 'washington':
            return 'washington.csv'       
        else:
            print('AAH ! {} TRY AGAIN !'.format(s))


'''BELOW CODES IS TO ASK THE USER ABOUT THE TIME PERIOD'''
def get_time_period():
    
    time_period = ''
    while time_period.lower() not in ['month', 'day', 'none']:
        time_period = input('\nWould you like to filter the data by month, day,'
                            ' or not at all? Type "none" for no time filter.\n')
        if time_period.lower() not in ['month', 'day', 'none']:
            print('Sorry {} I do not understand your input.'.format(s))
    return time_period


'''BELOW CODE IS TO GET THE DESIRED MONTH'''
def get_month():
    
    month_input = ''
    months_dict = {'january': 1, 'february': 2, 'march': 3, 'april': 4,
                   'may': 5, 'june': 6}
    while month_input.lower() not in months_dict.keys():
        month_input = input('\nWhich month? {} January, February, March, April,'
                            ' May, or June?\n'.format(s))
        if month_input.lower() not in months_dict.keys():
            print('Sorry Sir, Please type in a '
                  'month between January and June')
    month = months_dict[month_input.lower()]
    return ('2017-{}'.format(month), '2017-{}'.format(month + 1))


'''CODE TO GET THE DAY, BELOW'''
def get_day():

    this_month = get_month()[0]
    month = int(this_month[5:])
    valid_date = False
    while valid_date == False:    
        is_int = False
        day = input('\nWhich day? Please type your response as an integer.\n')
        while is_int == False:
            try:
                day = int(day)
                is_int = True
            except ValueError:
                print('Sorry, I do not understand your input. Please type your'
                      ' response as an integer.')
                day = input('\nWhich day? Please type your response as an integer.\n')
        try:
            start_date = datetime(2017, month, day)
            valid_date = True
        except ValueError as e:
            print(str(e).capitalize())
    end_date = start_date + timedelta(days=1)
    return (str(start_date), str(end_date))

''' BELOW IS THE CODE TO GET THE MOST POPULAR MONTH'''
def popular_month(A):
    
    months = ['January', 'February', 'March', 'April', 'May', 'June']
    index = int(A['start_time'].dt.month.mode())
    most_pop_month = months[index - 1]
    print('The most popular month is {}.'.format(most_pop_month))

''' BELOW IS THE CODE TO GET THE MOST POPULAR DAY'''
def popular_day(A):
    
    days_of_week = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday',
                    'Saturday', 'Sunday']
    index = int(A['start_time'].dt.dayofweek.mode())
    most_pop_day = days_of_week[index]
    print('The most popular day of week for start time is {}.'.format(most_pop_day))

''' BELOW IS THE CODE TO GET THE MOST POPULAR HOUR'''
def popular_hour(A):
    most_pop_hour = int(A['start_time'].dt.hour.mode())
    if most_pop_hour == 0:
        am_pm = 'am'
        pop_hour_readable = 12
    elif 1 <= most_pop_hour < 13:
        am_pm = 'am'
        pop_hour_readable = most_pop_hour
    elif 13 <= most_pop_hour < 24:
        am_pm = 'pm'
        pop_hour_readable = most_pop_hour - 12
    print('The most popular hour of day for start time is {}{}.'.format(pop_hour_readable, am_pm))


''' CODE TO GET THE TRIP DURATION'''
def trip_duration(A):
    
    total_duration = A['trip_duration'].sum()
    minute, second = divmod(total_duration, 60)
    hour, minute = divmod(minute, 60)
    print('The total trip duration is {} hours, {} minutes and {}'
          ' seconds.'.format(hour, minute, second))
    average_duration = round(A['trip_duration'].mean())
    m, s = divmod(average_duration, 60)
    if m > 60:
        h, m = divmod(m, 60)
        print('The average trip duration is {} hours, {} minutes and {}'
              ' seconds.'.format(h, m, s))
    else:
        print('The average trip duration is {} minutes and {} seconds.'.format(m, s))


'''TO PRINT THE MOST POPULAR STATION'''
def popular_stations(A):
    
    pop_start = A['start_station'].mode().to_string(index = False)
    pop_end = A['end_station'].mode().to_string(index = False)
    print('The most popular start station is {}.'.format(pop_start))
    print('The most popular end station is {}.'.format(pop_end))


'''TO PRINT THE MOST POPULAR TRIP'''
def popular_trip(A):
    
    most_pop_trip = A['journey'].mode().to_string(index = False)
    # you will get the 'journey' column in the statistics() function.
    print('The most popular trip is {}.'.format(most_pop_trip))


'''TO PRINT USER TYPE'''
def users(A):
    
    subs = A.query('user_type == "Subscriber"').user_type.count()
    cust = A.query('user_type == "Customer"').user_type.count()
    print('There are {} Subscribers and {} Customers.'.format(subs, cust))


'''TO PRINT THE GENDER OF THE RIDER'''
def gender(A):
    
    male_count = A.query('gender == "Male"').gender.count()
    female_count = A.query('gender == "Male"').gender.count()
    print('There are {} male users and {} female users.'.format(male_count, female_count))


'''TO PRINT THE YOUNGEST AND OLDEST RIDER'''
''' ALSO THE MOST POPULAR BIRTH YEAR'''
def birth_years(a):
    
    yong = int(a['birth_year'].min())
    eld = int(a['birth_year'].max())
    pop = int(a['birth_year'].mode())
    print('The oldest users are born in {}.\nThe youngest users are born in {}.'
          '\nThe most popular birth year is {}.'.format(yong, eld, pop))
    
   
    
    
    
    
'''BELOW IS THE DISPLAY FUNCTION IT SHOWS USER FIVE LINES OF DATA WHICH HE HAD CHOSEN ABOVE''' 
   
def display_data(A):
    
    def is_valid(display):
        if display.lower() in ['yes', 'no']:
            return True
        else:
            return False
    head = 0
    tail = 5
    valid_input = False
    while valid_input == False:
        display = input('\nWould you like to view individual trip data? '
                        'Type \'yes\' or \'no\'.\n')
        valid_input = is_valid(display)
        if valid_input == True:
            break
        else:
            print("Sorry, I do not understand your input. Please type 'yes' or"
                  " 'no'.")
    if display.lower() == 'yes':
        # prints every column except the 'journey' column created in statistics()
        print(A[A.columns[0:-1]].iloc[head:tail])
        display_more = ''
        while display_more.lower() != 'no':
            valid_input_2 = False
            while valid_input_2 == False:
                display_more = input('\nWould you like to view more individual'
                                     ' trip data? Type \'yes\' or \'no\'.\n')
                valid_input_2 = is_valid(display_more)
                if valid_input_2 == True:
                    break
                else:
                    print("Sorry, I do not understand your input. Please type "
                          "'yes' or 'no'.")
            if display_more.lower() == 'yes':
                head += 5
                tail += 5
                print(A[A.columns[0:-1]].iloc[head:tail])
            elif display_more.lower() == 'no':
                break   
    
  
    
'''THIS BELOW FUNCTION "statistics" FIRST CONFIGURE AND THEN PRINT OUT THE STATISTICS '''
'''WHICH THE USER INPUTED AS A RAW DATA '''
def statistics():
    # Filter by city (Chicago, New York, Washington)
    city = get_city()
    print('Loading data...')
    df = pd.read_csv(city, parse_dates = ['Start Time', 'End Time'])
    
    # change all column names to lowercase letters and replace spaces with underscores
    new_labels = []
    for col in df.columns:
        new_labels.append(col.replace(' ', '_').lower())
    df.columns = new_labels
    
    # increases the column width, To display properly
    pd.set_option('max_colwidth', 100)
    
    # creates a 'journey' column that concatenates 'start_station' with 
    # 'end_station' for the use popular_trip() function
    df['journey'] = df['start_station'].str.cat(df['end_station'], sep=' to ')

    # Filter by time period (month, day, none)
    time_period = get_time_period()
    if time_period == 'none':
        df_filtered = df
    elif time_period == 'month' or time_period == 'day':
        if time_period == 'month':
            filter_lower, filter_upper = get_month()
        elif time_period == 'day':
            filter_lower, filter_upper = get_day()
        print('Filtering data...')
        df_filtered = df[(df['start_time'] >= filter_lower) & (df['start_time'] < filter_upper)]
    print('\nCalculating the first statistic...')

    if time_period == 'none':
        start_time = time.time()
        
        # What is the most popular month for start time?
        popular_month(df_filtered)
        print("That took %s seconds." % (time.time() - start_time))
        print("\nCalculating the next statistic...")
    
    if time_period == 'none' or time_period == 'month':
        start_time = time.time()
        
        # What is the most popular day of week (Monday, Tuesday, etc.) for start time?
        popular_day(df_filtered)
        print("That took %s seconds." % (time.time() - start_time))
        print("\nCalculating the next statistic...")    
        start_time = time.time()

    # What is the most popular hour of day for start time?
        popular_hour(df_filtered)
    
        print("That took %s seconds." % (time.time() - start_time))
        print("\nCalculating the next statistic...")
        start_time = time.time()

    # What is the total trip duration and average trip duration?
        trip_duration(df_filtered)
        print("That took %s seconds." % (time.time() - start_time))
        print("\nCalculating the next statistic...")
        start_time = time.time()

    # What is the most popular start station and most popular end station?
        popular_stations(df_filtered)
        print("That took %s seconds." % (time.time() - start_time))
        print("\nCalculating the next statistic...")
        start_time = time.time()

    # What is the most popular trip?
        popular_trip(df_filtered)
        print("That took %s seconds." % (time.time() - start_time))
        print("\nCalculating the next statistic...")
        start_time = time.time()

    # What are the counts of each user type?
        users(df_filtered)
        print("That took %s seconds." % (time.time() - start_time))
    
    if city == 'chicago.csv' or city == 'new_york_city.csv':
        print("\nCalculating the next statistic...")
        start_time = time.time()
        
        # What are the counts of gender?
        gender(df_filtered)
        print("That took %s seconds." % (time.time() - start_time))
        print("\nCalculating the next statistic...")
        start_time = time.time()

        # year used for the first time (i.e. oldest user), most recent (i.e. youngest
        # user), and most popular birth years?
        birth_years(df_filtered)
        print("That took %s seconds." % (time.time() - start_time))

    # to display 5 more lines of data if the user want 
    display_data(df_filtered)

    # to ask if the user want to restart
    restart = input('\nWould you like to restart? Type \'yes\' or \'no\'.\n')
    while restart.lower() not in ['yes', 'no']:
        print("Invalid input. Please type 'yes' or 'no'.")
        restart = input('\nWould you like to restart? Type \'yes\' or \'no\'.\n')
    if restart.lower() == 'yes':
        statistics()
    else:
        print ('bye bye {} may you have a good day'.format(s))


if __name__ == "__main__":
	statistics()    