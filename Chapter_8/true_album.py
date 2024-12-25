#  Write a while loop that allows users to enter an album’s artist and title. Once you have that
# information, call make_album() with the user’s input and print the dictionary
# that’s created. Be sure to include a quit value in the while loop.

    
    
def make_album(artist, title, track=""):
    """Create a dictionary for an album."""
    album = {'artist': artist, 'title': title}
    if track:  # Add the number of tracks if provided
        album['track'] = track
    return album


# Start the while loop
active = True
while active:
    # Prompt the user for input
    print("\nEnter album information (or 'q' to quit):")

    artist = input("What is the name of your favorite artist? (press 'q' to quit): ")
    if artist.lower() == 'q':
        break

    title = input("What is the name of your favorite album? (press 'q' to quit): ")
    if title.lower() == 'q':
        break

    track = input("Optional: How many tracks are there? (press 'q' to quit, 'n' for none): ")
    if track.lower() == 'q':
        break
    elif track.lower() == 'n':
        track = ""

    # Create the album dictionary
    album = make_album(artist, title, track)
    print("\nAlbum details:")
    print(album)
    