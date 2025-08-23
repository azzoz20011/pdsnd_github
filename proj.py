import time
import pandas as pd 
import numpy as np 

#import streamlit as st
CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv' }
WEEK_DAYS = {
    'saturday' : 6 ,
    'sunday' : 0 ,
    'monday' : 1,
    'teusday': 2,
    'wendesday' : 3,
    'thursday' : 4,
    'friday' : 5,
    'all' : 00
}
YEAR_MONTHS = {
    'january':1,
    'february':2,
    'mars':3,
    'abril':4,
    'may':5,
    'june':6,
    'all': 00
}
def check_input(inputs, expected_input):
    """
    this function compare the user inputs and  qand the list or dictunary of expected inputs and return False for the expected input.

    args:
        (str) inputs - the intered input.
        (str) expected_input - list or dict of the expected inputs.
    return
        boolen F for right input and T for wrong input.
    """
    if (inputs.lower() in expected_input):
        # false to end the loop
        return False
    print('Wrong input, enter sring only from the list')
    return True

def get_filters():
    """
    Asks user to specify a city, month, and day to analyze.
    with while loop to coorect the input.

    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """
    print('Hello! Let\'s explore some US bikeshare data!')
    # TO DO: get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs
    print('-'*40)

    # Q stand for question.
    q1,q2,q3 = True,True,True
    while q1:
        
        city = str(input("inter the name of the city you want to look for in this list [chicago , new york city , washington] ")).lower()
        q1=check_input(city,CITY_DATA)
    print('-'*40)

    # TO DO: get user input for month (all, january, february, ... , june)
    while q2:
        month = str(input("inter the month you are intrested as in the list (all, january, february, mars, abril, may, june) ")).lower()
        q2=check_input(month,YEAR_MONTHS)
    print('-'*40)

    # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)
    while q3:
        day = str(input("""enter the number of the day such as the following (all,saturday,sunday,monday,teusday,wendesday,thursday,friday)\n""")).lower()
        q3=check_input(day,WEEK_DAYS)
    print('-'*40)

    return city, month, day


def load_data(city, month, day):
    """
    Loads data for the specified city and filters by month and day if applicable.

    Args:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    Returns:
        df - Pandas DataFrame containing city data filtered by month and day
    """

    CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv' }
    
    # read the city file 
    df = pd.read_csv(CITY_DATA[city])
    
    # convert the Start Time column to datetime
    df['Start Time'] = pd.to_datetime(df['Start Time'])
    # extract month and day of week from Start Time to create new columns
    df['month'] = df['Start Time'].dt.month
    df['day_of_week'] = df['Start Time'].dt.weekday
    df['hour'] = df['Start Time'].dt.hour

    # filter the rows woth month then with day
    if (month != "all"):
        df = df[df["month"] == YEAR_MONTHS[month]]
    if (day!= "all"):
        df = df[df["day_of_week"] == WEEK_DAYS[day]]
        return df
    return df


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # TO DO: display the most common month
    months = df['month'].value_counts().max()
    max_month = df["month"].max()
    # this dict help convert int to string so i could produse understandable expression.
    DAYS_WEEK_I_to_S = {
    6: 'saturday',
    0: 'sunday',
    1: 'monday',
    2: 'teusday',
    3: 'wendesday',
    4: 'thursday',
    5: 'friday'
    }
    MONTHS_YEAR_I_to_S = {1: 'january', 2: 'february', 3: 'march', 4: 'april', 5: 'may', 6: 'june'}
    print(f"the most common month is:  {MONTHS_YEAR_I_to_S[max_month]   } with {months} time repeated" )

    # TO DO: display the most common day of week
    days = df['day_of_week'].value_counts().max()
    max_day = df["day_of_week"].max()
    print(f"the most common day is:  {DAYS_WEEK_I_to_S[max_day]} with {days} time repeated" )


    # TO DO: display the most common start hour
    hours = df['hour'].value_counts().max()
    max_hour = df["hour"].max()
    print(f"the most common hour is:  {max_hour} with {hours} time repeated" )


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # TO DO: display most commonly used start station
    start_station = df["Start Station"].max()
    print(f"the most common station:  {start_station}" )


    # TO DO: display most commonly used end station
    end_station = df["End Station"].max()
    print(f"the most common station:  {end_station}" )

    # TO DO: display most frequent combination of start station and end station trip
    df["station_combinations"] = df["Start Station"]+", with "+df["End Station"] 
    mfsc =  df["station_combinations"].max()
    print(f"Most common trip from start to end (i.e., most frequent combination of start station and end station):  {mfsc}" )


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # TO DO: display total travel time
    travel_count = float(df["Trip Duration"].sum())
    days, remainder1 = divmod(travel_count, 3600*24)
    hours, remainder2 = divmod(remainder1, 3600)
    minutes, seconds = divmod(remainder2, 60)
    print(f"the total travel time is: {int(days)} day, {int(hours)} hours, {int(minutes)} minutes, {int(seconds)} seconds")
    #print(f"the total travel time is: {date} \n" )


    # TO DO: display mean travel time
    travel_mean = float(df["Trip Duration"].mean())
    days, remainder1 = divmod(travel_mean, 3600*24)
    hours, remainder2 = divmod(remainder1, 3600)
    minutes, seconds = divmod(remainder2, 60)
    print(f"the avrage travel time is:  {int(hours)} hours, {int(minutes)} minutes, {int(seconds)} seconds")   

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # TO DO: Display counts of user types
    count_user_types = df["User Type"].value_counts()
    print(f"the counts of user types is: {count_user_types} \nn" )

    # TO DO: Display counts of gender
    if 'Gender' in df.columns:
        count_genders = df["Gender"].value_counts()
        print(f"the counts of gender is: {count_genders} \n" )
    else:
        print("there is no data about Gender \n")
    # TO DO: Display earliest, most recent, and most common year of birth
    if 'Birth Year' in df.columns:
        early_birth = float(df["Birth Year"].min())
        recent_birth = float(df["Birth Year"].max())
        common_birth = df["Birth Year"].value_counts().max()
        print(f"the ealiest year of birth is: {early_birth} ,most recent is: {recent_birth} and most common year of birth is{common_birth}\n" )
    else:
        print("there is no data about Birth year \n")

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)
        #ask for the first five rows of the dataframe.
        continues=str(input("enter 'yes' if you want to see the first five rows of data.\n"))
        if continues.lower()=='yes':
            ranges=0
            print(df[ranges:ranges+5])
            #loop to continue showing the dataframe.
            while True:
                nexts=str(input("if you want to see more enter 'yes'or 'no'\n"))       
                if nexts.lower()!='yes':
                    break
                ranges=ranges + 5
                print(df[ranges:ranges+5])
 
        del df
        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
	main()
