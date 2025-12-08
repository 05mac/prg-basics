# class definition
class Song:
   def __init__(self,Performer,Title,Album,Year):
    self.Performer = Performer
    self.Title = Title
    self.Album = Album
    self.Year = Year

   def __str__(self):
    print (f"Performer: {self.Performer}")
    print (f"Title: {self.Title}")
    print (f"Album: {self.Album}")
    print (f"Year: {self.Year}")
    return "";


# object creation
song1 = Song("Ed Sheeran","Hearts Don't Break Around Here","Divide",2017)
song2 = Song("Queen","Bohemian Rhapsody","A Night at the Opera",1975)

## object usage
print(song1)
print(song2)