from .album import Album

class Band:
    def __init__(self,name) -> None:
        self.name = name
        self.albums = []
    
    def add_album(self,album:Album):
        if album in self.albums:
            return f'Band {self.name} already has {album.name} in their library.'
        self.albums.append(album)
        return f"Band {self.name} has added their newest album {album.name}."
    
    def remove_album(self,album_name:str):
        for x in range(len(self.albums)):
            if self.albums[x].name == album_name:
                if self.albums[x].published:
                    return f'Album has been published. It cannot be removed.'
                self.albums.pop(x)
                return f'Album {album_name} has been removed.'
        return f'Album {album_name} is not found.'
    
    def details(self):
        album_text = '\n'.join([album.details() for album in self.albums])
        return f'Band {self.name}\n{album_text}'
