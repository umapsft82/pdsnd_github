# -*- coding: utf-8 -*-
"""
#BikeShare Project
#This program explores data related to bike share systems for three major
#cities in the United States—Chicago, New York City, and Washington.
#Umadevi R
#01/14/2019

"""
#'Importing libraries'
import pandas as pd
from datetime import datetime
#Defining dictionaries for city data files,city names and months
CITY_DATA = { 1: 'chicago.csv',
              2: 'new_york_city.csv',
              3: 'washington.csv' }
CITY_NAME = {1: 'Chicago',
             2: 'New York City',
             3: 'Washington'}
MONTH_DATA = {0: 'all months', 1: 'January', 2: 'February', 3: 'March', 4: 'April', 5: 'May', 6: 'June'}

def welcome_message():

    """
    Asks user to select a city from options 1,2 or 3 to analyze or 4 to exit.
    Then passes control to function category_input()
    """

    print('\n*****************Hello! Welcome to Bikeshare Data*****************')
    print('\nSelect the option for the city you wish to get statistics about:')
    print('\n1. Chicago')
    print('2. New York')
    print('3. Washington')
    print('4. Exit')


    while True:
        try:
            city_num = int(input('Choose an option from 1 to 4: '))
            if ((city_num>=1) and (city_num<=4)):
                break
        except:
            print('\nIncorrect option!')


    if (city_num == 4):
        print('\nThanks for accessing Bikeshare Data. Goodbye')
        exit()
    else:
        df = pd.read_csv(CITY_DATA[city_num])
        rec_count = df['Start Time'].count()
        print('Number of records for {} is {}.'.format(CITY_NAME[city_num],rec_count))
        category_input(city_num)



def category_input(city_num):
    """
    Asks user to specify a month and option to analyze for the selected city.
    Args:
        (int) city_num - number corresponding to that city
   """


    while True:
        try:
            month_num = int(input('\nChoose month (1 to 6) or 0 for all months: '))
            if ((month_num>=0) and (month_num<=6)):
                break
        except:
            print('Incorrect option!')

    print('\nSelect a category for data analysis about {} for {}:'.format(CITY_NAME[city_num],MONTH_DATA[month_num]))
    print('\n 1. Popular time to travel')
    print(' 2. Popular start/end station')
    print(' 3. Trip Duration')
    print(' 4. User Info')
    print(' 5. All of the above')
    print(' 6. Raw Data')
    print(' 7. Exit (Go to the main screen)')
    while True:
        try:
            option_num = int(input('Choose a category from 1 to 7: '))
            if((option_num>=1) and (option_num<=7)):
                break
        except:
            print('Incorrect option!')


    print('\nRetrieving data about {} for {}...' .format(CITY_NAME[city_num],MONTH_DATA[month_num]))

    if option_num == 1:
        category_one(city_num,month_num,option_num)
    if option_num == 2:
        category_two(city_num,month_num,option_num)
    if option_num == 3:
        category_three(city_num,month_num,option_num)
    if option_num == 4:
        category_four(city_num,month_num,option_num)
    if option_num == 5:
        category_one(city_num,month_num,option_num)
        category_two(city_num,month_num,option_num)
        category_three(city_num,month_num,option_num)
        category_four(city_num,month_num,option_num)
        post_category(city_num)
    if option_num == 6:
        category_six(city_num,month_num)
    if option_num == 7:
        welcome_message()

def post_category(city_num):

    """
    Prompts the user whether to continue with the analysis or to go to the main menu.

    Args:
        (int) city - name of the city to analyze

    """

    print('\n********************************************************')
    print('\nEnter 1 for more city analysis')
    print('Enter 2 for Main Menu')
    while True:
        try:
            post_num = int(input('Choose an option 1 or 2: '))
            if ((post_num>=1) and (post_num<=2)):
                 break
        except:
            print('Choose an option 1 or 2: ')


    if post_num == 1:
        category_input(city_num)
    else:
        welcome_message()



def category_one(city_num,month_num,option_num):
    """
    Loads data for the specified city and filters by month and category if applicable.
    Displays statistics on the most frequent times of travel.

    Args:
        (int) city - name of the city to analyze
        (int) month - name of the month to filter by, or "all" to apply no month filter
        (int) option - used to determine if user picked one or all category

    """
    start_time = datetime.now()
    #load data from csv of the corresponding city into the dataframe
    df = pd.read_csv(CITY_DATA[city_num])
    # convert the Start Time column to datetime
    df['Start Time'] = pd.to_datetime(df['Start Time'])
    # extract month from the Start Time column to create a month column
    df['month'] = df['Start Time'].dt.month
    if (month_num != 0):
        df=df[df['month'] == month_num]
    # extract hour from the Start Time column to create an hour column
    df['hour'] = df['Start Time'].dt.hour
    # the most common hour (from 0 to 23)
    print('\n******************Popular Times to Travel******************')
    print('\nMost Popular Hour\t\t: ', df['hour'].mode().loc[0])
    print('Number of occurences\t: ', df['hour'].value_counts().iloc[0])
    #find the popular weekday
    df['day_of_week'] = df['Start Time'].dt.weekday_name
    print('Most popular day\t\t: ' , df['day_of_week'].mode().loc[0])
    print('Number of occurences\t: ', df['day_of_week'].value_counts().iloc[0])
    end_time = datetime.now()
    print('\nProcessing Time: {}'.format(end_time - start_time))


    if (option_num != 5):
        post_category(city_num)


def category_two(city_num,month_num,option_num):
    """
    Loads data for the specified city and filters by month and category if applicable.
    Displays statistics on the most popular stations and trip.

    Args:
        (int) city - name of the city to analyze
        (int) month - name of the month to filter by, or "all" to apply no month filter
        (int) option - used to determine if user picked one or all category

    """
    start_time = datetime.now()
    df = pd.read_csv(CITY_DATA[city_num])
    # convert the Start Time column to datetime
    df['Start Time'] = pd.to_datetime(df['Start Time'])
    # extract month from the Start Time column to create a month column
    df['month'] = df['Start Time'].dt.month
    if (month_num != 0):
        df=df[df['month'] == month_num]

    print('\n*****************Popular Start/End Stations*****************')
    #common start station
    print('\nMost popular start station\t\t: ' ,df['Start Station'].mode().loc[0])
    print('Number of occurences for Start Station\t: ', df['Start Station'].value_counts().iloc[0])
    #common end station
    popular_endstation =
    print('Most popular end station\t\t: ' ,df['End Station'].mode().loc[0])
    print('Number of occurences for End Station\t: ', df['End Station'].value_counts().iloc[0])
    #common start/end combo trip
    df['combo_trip'] = df['Start Station'] +','+ df['End Station']
    print('Most Common trip\t\t\t: ', df['combo_trip'].mode().loc[0])
    end_time = datetime.now()
    print('\nProcessing Time: {}'.format(end_time - start_time))

    if (option_num != 5):
        post_category(city_num)

def category_three(city_num,month_num,option_num):
    """
    Loads data for the specified city and filters by month and category if applicable.
    Displays statistics on the total and average trip duration.

    Args:
        (int) city - name of the city to analyze
        (int) month - name of the month to filter by, or "all" to apply no month filter
        (int) option - used to determine if user picked one or all category

    """
    start_time = datetime.now()
    df = pd.read_csv(CITY_DATA[city_num])
    # convert the Start Time column to datetime
    df['Start Time'] = pd.to_datetime(df['Start Time'])
    # extract month from the Start Time column to create a month column
    df['month'] = df['Start Time'].dt.month
    if (month_num != 0):
        df=df[df['month'] == month_num]

    print('\n******************Trip Duration Information******************')
    print('\nTotal Trip time\t\t: ', df['Trip Duration'].sum())
    #Average Trip Time
    Avg_trip_time = Total_Trip_Time/df['Start Time'].count()
    print('Average Trip Time\t\t: ', Avg_trip_time)
    #Longest Trip duration
    print('Max Trip time\t\t: ', df['Trip Duration'].max())
    #Shortest Trip duration
    print('Min Trip time\t\t: ', df['Trip Duration'].min())
    end_time = datetime.now()
    print('\nProcessing Time: {}'.format(end_time - start_time))
    if (option_num != 5):
        post_category(city_num)

def category_four(city_num,month_num,option_num):
    """
    Loads data for the specified city and filters by month and category if applicable.
    Displays statistics on bikeshare users.

    Args:
        (int) city - name of the city to analyze
        (int) month - name of the month to filter by, or "all" to apply no month filter
        (int) option - used to determine if user picked one or all category

    """
    print('\n********************User Information********************')
    start_time = datetime.now()
    df = pd.read_csv(CITY_DATA[city_num])
    # convert the Start Time column to datetime
    df['Start Time'] = pd.to_datetime(df['Start Time'])
    # extract month from the Start Time column to create a month column
    df['month'] = df['Start Time'].dt.month
    if (month_num != 0):
        df=df[df['month'] == month_num]

    #count of each user_types
    user_types = df['User Type'].value_counts()
    print ('\nUser Types:')
    print(user_types)
    if city_num == 2 or city_num == 1:
        #user_info only available for nyc and chicago
        gender_count = df['Gender'].value_counts()
        print('\nGender Information:')
        print(gender_count)
        #common birth year
        print('\nCommon Birth Year\t\t: ', df['Birth Year'].mode().loc[0])
        #Total birth counts
        print('Number of Births\t\t: ', df['Birth Year'].value_counts().iloc[0] )
        #Earliest birth year
        print('Earliest Birth Year\t\t: ', df['Birth Year'].min())
        #Recent birth year
        print('Recent Birth Year\t\t: ', df['Birth Year'].max())
        end_time = datetime.now()
        print('\nProcessing Time: {}'.format(end_time - start_time))

    if (option_num != 5):
        post_category(city_num)

def category_six(city_num,month_num):
    """
    Loads data for the specified city and filters by month.
    Displays five lines of raw data to the users.

    Args:
        (int) city - name of the city to analyze
        (int) month - name of the month to filter by, or "all" to apply no month filter

     """

    df = pd.read_csv(CITY_DATA[city_num])
    # convert the Start Time column to datetime
    df['Start Time'] = pd.to_datetime(df['Start Time'])
    # extract month from the Start Time column to create a month column
    df['month'] = df['Start Time'].dt.month
    if (month_num != 0):
        df=df[df['month'] == month_num]
    print('\n*********************Raw Data Output*********************')
    raw_option = 'y'
    rec_count = df['Start Time'].count()
    while(raw_option == 'y'):
        for i in range(0,rec_count,5):
            print(df[i:(i+5)])
            while True:
                try:
                    raw_option = str(input('\nDo you want to continue (y or n)? ' ))
                    if (raw_option.lower() == 'y') or (raw_option.lower() == 'n'):
                        break
                except:
                    print('Enter y or n: ')

            if(raw_option.lower() == 'n'):
                break
            else:
                continue

    post_category(city_num)



welcome_message()
