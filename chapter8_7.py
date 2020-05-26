# Exercise 8.7 Album: Write a function called "make_album()" that builds a dictionary describing a music album. 
# The function should take in an artist name and an album title, and it should return a dictionary containing these two pieces of information.
# Use the function to make three dictionaries representing different albums. 
# Print each return value to show that the dictionaries are storing the album information correctly.

def make_album(artist_name, album_title):    
    album = {'name': artist_name, 'title': album_title}
    return album
diff_album = make_album('Michael Jackson','Thriller') 
print(diff_album)
diff_album = make_album('Pink Floyd', 'The Dark Side of the Moon')
print(diff_album) 
diff_album = make_album('Michael Jackson', 'bad') 
print(diff_album)

