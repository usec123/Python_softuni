from .song import Song

class Album:
    def __init__(self, name:str, *songs) -> None:
        self.name = name
        self.songs = [song for song in songs] if songs else []
        self.published = False
    
    def add_song(self, song:Song):
        if song.single:
            return f'Cannot add {song.name}. It\'s a single'
        if self.published:
            return 'Cannot add songs. Album is published.'
        if song in self.songs:
            return 'Song is already in the album.'
        self.songs.append(song)
        return f'Song {song.name} has been added to the album {self.name}.'

    def remove_song(self,song_name:str):
        if self.published:
            return "Cannot remove songs. Album is published."
        for x in range(len(self.songs)):
            if self.songs[x].name == song_name:
                self.songs.pop(x)
                return f"Removed song {song_name} from album {self.name}."
        return "Song is not in the album."

    def publish(self):
        if self.published:
            return f'Album {self.name} is already published.'
        self.published = True
        return f"Album {self.name} has been published."
    
    def details(self):
        songs_text = '\n== '.join([song.get_info() for song in self.songs])
        return f'Album {self.name}\n{songs_text}'