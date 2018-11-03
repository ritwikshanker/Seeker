# Seeker
Find the date of release of next episode of your favorite TV series and spoil it for your friends ;)

# Installation
Check out a copy of my repository.
```sh
$ git clone https://github.com/ritwikshanker/Seeker.git
$ cd Seeker
$ pip install -r requirements.txt
```

# Running
On running, the script will request your email and the name of your favorite TV series, for example
```sh
$ py -3 main.py
```

```
Email Address: ritwikshanker@gmail.com
TV Series: DareDevil
```
After the execution of the script, you will receive an email containing the date of air of the next episode of the TV Series.

NOTE : Before running make sure MySQL server is configured and running.

# How was the task achieved?
* Ask the user for email address and TV Series.
    * If the user enters several TV Series (comma separated), then split the string.
* Searched across the IMDb database for the TV Series entered by the user.
* Fetched all the seasons of the TV Series.
* Finally fetched the airing date in USA for all the episodes of last season.

-----
# SideNote
Doing this project using python and using IMDbPy API helped me learn a lot of new things. This was my first interaction with APIs. Thanks for the opportunity :)
