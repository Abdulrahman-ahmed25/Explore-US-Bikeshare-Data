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
    # get user input for city (chicago, new york city, washington). 

    while True:
        city = input("enter your city : ").lower()
        if city not in ['chicago','new york city','washington']:
            print("please enter the city again")
            continue
        else:
            break

    
    # get user input for month (all, january, february, ... , june)
    while True:
        month = input("input for month (all, january, february, ... , june) : ").lower()
        if month not in ['all','january','february','march','april','june']:
            print("please enter the month again")
            continue
        else:
            break
    # get user input for day of week (all, monday, tuesday, ... sunday)
    while True:
        day   = input("input for day of week (all, monday, tuesday, ... sunday) : ").lower()
        if day not in ['all','monday','tuesday','wednesday', 'thursday', 'friday', 'saturday','sunday']:
            print("please enter the day again")
            continue
        else:
            break


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
    df = pd.read_csv(CITY_DATA[city])
    # print(df)
    return df


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()
    df['Start Time'] = pd.to_datetime(df['Start Time'])
    # display the most common month
    df['month'] = df['Start Time'].dt.month
    popular_month = df['month'].mode()[0]
    print(f"popular_month = {popular_month}")
    # display the most common day of week
    df['day_of_week'] = df['Start Time'].dt.weekday
    popular_day_of_week = df['day_of_week'].mode()[0]
    print(f"popular_day_of_week = {popular_day_of_week}")

    # display the most common start hour
    df['hour'] = df['Start Time'].dt.hour
    popular_hour = df['hour'].mode()[0]
    print(f"popular_hour = {popular_hour}")

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # display most commonly used start station
    most_commonly_used_start_station = df['Start Station'].mode()[0]
    print(f'most_commonly_used_start_station = {most_commonly_used_start_station}')

    # display most commonly used end station
    most_commonly_used_end_station = df['End Station'].mode()[0]
    print(f'most_commonly_used_END_station = {most_commonly_used_end_station}')
    # display most frequent combination of start station and end station trip
    most_commonly_used_start_eND_station = df.groupby(['Start Station'])['End Station'].count()
    print(most_commonly_used_start_eND_station)
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # display total travel time
    total_trip = df['Trip Duration'].sum()
    print(f"total_trip = {total_trip}")
    # display mean travel time
    mean_Trip= df['Trip Duration'].mean()
    print(f"mean_Trip = {mean_Trip}")

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # Display counts of user types
    # df['Adj Close'].describe()
    user_types = df['User Type'].value_counts()
    print(f"user_type = {user_types}")
    # # Display counts of gender
    try:
        genders = df['Gender'].value_counts()
        print('\nGenders:\n', genders)
    except:
        print("sorry we haven't data about gender")
    
    # Display earliest, most recent, and most common year of birth
    try:
        earliest_year = df['Birth Year'].min()
        print(f'earliest_year = {earliest_year}')
        
        recent_year = df['Birth Year'].max()
        print(f'recent_year = {recent_year}')

        most_common_year = df['Birth Year'].mode()[0]
        print(f"most_common_year = {most_common_year}")
    except:
        print("sorry we haven't data about Birth Year")

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def main():

    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)
        while True:
            view_data = input("Would you like to view 5 rows of individual trip data? Enter yes or no?").lower()
            start_loc = 0
            if view_data not in ['yes','no']:
                print('please enter yes or no only')
                continue
            else:
                break
        while (True):
            if view_data =='yes':
                print(df.iloc[start_loc:start_loc+5])
                start_loc += 5
                view_display = input("Do you wish to continue?: ").lower()
                if view_display == 'yes':
                    continue
                elif view_display == 'no':
                    break
            elif view_data == 'NO':
                break
            
        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
	main()
