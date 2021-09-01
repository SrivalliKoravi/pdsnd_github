import time
import pandas as pd
import numpy as np


CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv' }

def get_filters():
    """
        Asks user to specify a city, month, and day to analyze.

        Returns:
            (str) city - name of the city to analyze
            (str) month - name of the month to filter by, or "all" to apply no month filter
            (str) day - name of the day of week to filter by, or "all" to apply no day filter
        """
    print('Hello! Let\'s explore some US bikeshare data!')
    # TO DO: get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs
    while True:
        city=input("Enter a city name(chicago,washington,new york city): ")
        city=city.lower()
        if city in['chicago','new york city','washington']:
            break
        else:
            print("enter valid city name ")


        # TO DO: get user input for month (all, january, february, ... , june)
    while True:
        month=input("enter name of month from first six months  to  get data or enter 'all' to get data: ")
        month=month.lower()
        if month in ['january','february','march','april','may','june','all']:
            break
        else:
            print("please enter a valid month: ")


        # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)
    while True:
        day=input("enter day of week to get data or enter 'all': ")
        day=day.lower()
        if day in ['monday','tuesday','wednesday','thursday','friday','saturday','sunday','all']:
            break
        else:
            print("enter a valid input")

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
    df=pd.read_csv(CITY_DATA[city])
    df['Start Time']=pd.to_datetime(df['Start Time'])
    df['month']=df['Start Time'].dt.month
    df['day_of_week']=df['Start Time'].dt.weekday_name
    if month !='all':
        months=['january','february','march','april','may','june']
        month=months.index(month)+1
        df=df[df['month']==month]
    if day !='all':
        df=df[df['day_of_week']==day.title()]

    return df


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # TO DO: display the most common month
    print("Most common month is:",df['month'].mode()[0], "\n")

    # TO DO: display the most common day of week
    print("Most common day of week is: ",df['day_of_week'].mode()[0], "\n")    


    # TO DO: display the most common start hour
    df['hour']=df['Start Time'].dt.hour
    print("Most common start hour is: ",df['hour'].mode()[0])

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # TO DO: display most commonly used start station
    print("Most commonly used start station is: ",df['Start Station'].mode()[0], "\n")


    # TO DO: display most commonly used end station
    print("Most commonly use end station is: ",df['End Station'].mode()[0], "\n")


    # TO DO: display most frequent combination of start station and end station trip
    df['combination']=df['Start Station']+"  " +df['End Station']
    print("Most frequent combination of start and end trips: ",df['combination'].mode()[0])


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # TO DO: display total travel time
    print("Total time travel is: ",df['Trip Duration'].sum(), "\n")


    # TO DO: display mean travel time
    print("Total mean time is : ",df['Trip Duration'].mean(), "\n")


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df,city):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # TO DO: Display counts of user types
    user_types=df.groupby(['User Type']) ['User Type'].count()
    print(user_types, "\n")
    if city !='washington':
        # TO DO: Display counts of gender
        gen=df.groupby(['Gender']) ['Gender'].count()
        print(gen)


    # TO DO: Display earliest, most recent, and most common year of birth
        mrb=sorted(df.groupby(['Birth Year']) ['Birth Year'], reverse=True)[0][0]
        eb=sorted(df.groupby(['Birth Year']) ['Birth Year'])[0][0]
        mcb=df['Birth Year'].mode()[0]
        print("Earliest year of birth: ",eb, "\n")
        print("Recent year of birth: ",mrb, "\n")
        print("Common year of birth: ",mcb, "\n")
   # print("warning1")	


    print("\nThis took %s seconds." %round((time.time() - start_time)))
    print('-'*40)
    x=1
    while True:
        raw=input("would you like to see raw input? Enter yes or no \n")
        if raw.lower()== 'yes':
            print(df[x:x+5])
   # print("warning msg2")
            x=x+5
        else:
            break
                

def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df,city)

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
         main()
