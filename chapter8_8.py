# Exercise 8.8 User Albums: Start with your program from Exercise 8.7. Write a "while" loop that allows users to enter an album's artist and title. 
# Once you have that information, call "make_album()" with the user's input and print the dictionary that's created. 
# Be sure to include a "quit" value in the while loop.

def make_album(artist_name, album_title):    
    album = {'name': artist_name, 'title': album_title}
    return album
while True: 
    print("please enter 'quit' to stop")
    print("\nPlease tell artist name ")
    artist_name = input("Artist name: ")    
    if artist_name == 'quit':
        break
    print("\n Enter Album title")
    album_title = input("Album title: ")
    if album_title == 'quit':
        break
    Album = make_album(artist_name,album_title)
    print(Album)
    
    