from imdb import IMDb

# create an instance of the IMDb class
ia = IMDb()
# Getting Email address from console line
#email_Add = input("Email Address: ")
all_Series = input("TV Series: ")  # All series name from console line
# Splitting series names by comma separator
series_Name = all_Series.split(',')

for i in range(len(series_Name)):
    tv_Series = ia.search_movie(series_Name[i])
    series_Id = tv_Series[i].movieID
    print('Series Name: ',tv_Series[0])
    print("ID:",series_Id)
    