def album(name, title, songs=None):
    if songs != None:
        album = {"artist": name, "album": title, "songs": songs}
    else:
        album = {"artist": name, "album": title}
    return album

floyd = album("Pink Floyd", "Animals", 12)
print(floyd)
rihanna = album("Rihanna", "New York")
print(rihanna)
bonJovi = album("Bon Jovi", "Livin on a prayer")
print(bonJovi)
