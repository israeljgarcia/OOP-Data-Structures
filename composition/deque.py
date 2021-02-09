from collections import deque


class Song:

    def __init__(self):
        self.title = ''
        self.artist = ''

    def prompt(self):
        title = input("Enter the title: ")
        self.title = title
        artist = input("Enter the artist: ")
        self.artist = artist

    def display(self):
        print("Playing song:")
        print(f'{self.title} by {self.artist}\n')


playlist = deque()

condition = 0


while condition != 4:
    print("Options:")
    print("1. Add a new song to the end of the playlist")
    print("2. Insert a new song to the beginning of the playlist")
    print("3. Play the next song")
    print("4. Quit\n")
    condition = int(input("Enter selection: "))

    if(condition == 3 and len(playlist) == 0):
        print("The playlist is currently empty")

    elif condition == 1:
        song = Song()
        song.prompt()
        playlist.append(song)

    elif condition == 2:
        song = Song()
        song.prompt()
        playlist.appendleft(song)

    elif(condition == 3):
        song = playlist.popleft()
        song.display()

    else:
        print("Invalid input. Please enter 1 - 4\n")
