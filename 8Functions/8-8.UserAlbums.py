def album(name, title):
    album = {"artist": name, "album": title}
    return album

while True:
        artist = input("Input a new artist (or \"quit\" to quit): ")
        if artist != "quit":
            disc = input("Input the album name: ")
            print(album(artist, disc))
        else:
            break

