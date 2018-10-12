from imdb import IMDb
import connect
from datetime import date, datetime

global flag
global formatted_date


def res(status):
    if (status == 1):
        print("Next Season Begins on", formatted_date)
    elif (status == 2):
        print("Next episode airs on ", formatted_date)
    elif (status == 3):
        print("The show has finished Streaming all its episode")
    print(status)


def check_date():
    for j in range(no_Episode):  # running the loop for all the episodes
        episode_id = season_episode[j + 1].movieID  # Fetching every Episode's Unique ID
        episode_Release_date = ia.get_movie_release_dates(episode_id)  # Every episode's release date data
        print(j + 1, "Episode Release Date: ", episode_Release_date)
        global flag
        for USA_release_Date in episode_Release_date['data']['raw release dates']:
            if USA_release_Date['country'] == "USA":  # Working on USA Release Data
                us_release_date = USA_release_Date['date']
                us_release_date = us_release_date.lstrip()  # Trimming leading spaces
                us_release_date = us_release_date.rstrip()  # Trimming ending spaces
                print(us_release_date)
                global formatted_date
                if (len(us_release_date) == 4):  # If only release year is announced for new Season
                    flag = 1
                    print("Only release Year")
                    formatted_date = us_release_date
                    return flag
                formatted_date = datetime.strptime(USA_release_Date['date'],
                                                   '%d %B %Y')  # Formatting date for comparison
                formatted_date = formatted_date.strftime('%Y-%m-%d')
                print(formatted_date)
                if (formatted_date > present and j == 0):  # if full release date is announced for
                    flag = 1
                    print("cond1")
                    return flag
                elif (formatted_date > present):
                    flag = 2
                    print("cond2")
                    return flag
                else:
                    print("cond3")
                    flag = 3
    return flag


# create an instance of the IMDb class
ia = IMDb()
present = str(date.today())
# print(present)
# Getting Email address from console line
email_Add = input("Email Address: ")
all_Series = input("TV Series: ")  # All series name from console line
# Splitting series names by comma separator
series_Name = all_Series.split(',')
connect.connect_to_db(email_Add, all_Series)  # Sending data to database
for i in range(len(series_Name)):
    tv_Series = ia.search_movie(series_Name[i])  # searching Series
    series_Id = tv_Series[0].movieID  # Obtaining id of first search result
    ia.update(tv_Series[0], 'episodes')
    series_Season = sorted(tv_Series[0]['episodes'].keys())  # No of seasons in a series
    no_Season = len(series_Season)
    season_episode = tv_Series[0]['episodes'][no_Season]  # episode details in last season
    no_Episode = len(season_episode)
    print('Series Name: ', tv_Series[0])
    print("ID:", series_Id)
    print("Season", series_Season)
    print('No Of Season :', no_Season)
    print("Episode in season", no_Season, 'are', season_episode)
    print("No of Episode: ", no_Episode)
    return_value = check_date()  # Calling function to check date
    res(return_value)
    flag = -1
