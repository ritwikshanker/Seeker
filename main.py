from imdb import IMDb
import connect
from datetime import date, datetime
import sendmailfunc

# global Variables
global flag
global formatted_date
global msg


def res(status):
    global msg
    if (status == 1):
        msg = "Status : Next Season Begins on " + formatted_date
    elif (status == 2):
        msg = "Status : Next episode airs on " + formatted_date
    elif (status == 3):
        msg = "Status : The show has finished Streaming all its episode"


def check_date():
    for j in range(no_Episode):  # running the loop for all the episodes
        episode_id = season_episode[j + 1].movieID  # Fetching every Episode's Unique ID
        episode_Release_date = ia.get_movie_release_dates(episode_id)  # Every episode's release date data
        global flag
        for USA_release_Date in episode_Release_date['data']['raw release dates']:
            if USA_release_Date['country'] == "USA":  # Working on USA Release Data
                us_release_date = USA_release_Date['date']
                us_release_date = us_release_date.lstrip()  # Trimming leading spaces
                us_release_date = us_release_date.rstrip()  # Trimming ending spaces
                global formatted_date
                if (len(us_release_date) == 4):  # If only release year is announced for new Season
                    flag = 1  # Assigned 1 for the series whose new season hasn't started
                    formatted_date = us_release_date
                    return flag
                formatted_date = datetime.strptime(USA_release_Date['date'],
                                                   '%d %B %Y')  # Formatting date for comparison
                formatted_date = formatted_date.strftime('%Y-%m-%d')
                # if full release date is announced for the series and first episode hasn't released yet
                if (formatted_date > present and j == 0):
                    flag = 1  # Assigned 1 for the series whose new season hasn't started
                    return flag
                elif (formatted_date > present):
                    flag = 2  # Assigned 2 for the series which is already running
                    return flag
                else:
                    flag = 3  # Assigned 3 for the series which has finished airing
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
message_to_send = "\n\n"
for i in range(len(series_Name)):
    tv_Series = ia.search_movie(series_Name[i])  # searching Series
    series_Id = tv_Series[0].movieID  # Obtaining id of first search result
    ia.update(tv_Series[0], 'episodes')
    series_Season = sorted(tv_Series[0]['episodes'].keys())  # No of seasons in a series
    no_Season = len(series_Season)
    season_episode = tv_Series[0]['episodes'][no_Season]  # episode details in last season
    no_Episode = len(season_episode)
    name = 'TV Series Name : ' + str(tv_Series[0])
    return_value = check_date()  # Calling function to check date
    res(return_value)  # Calling function to generate the final status
    message_to_send = message_to_send + str(name) + "\n" + str(msg) + "\n\n"

sendmailfunc.sendMail(message_to_send, str(email_Add))
flag = -1
