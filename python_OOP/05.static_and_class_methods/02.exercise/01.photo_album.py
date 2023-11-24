class PhotoAlbum:
    def __init__(self, pages: int):
        self.pages = pages
        self.photos = [[] for _ in range(pages)]

    @classmethod
    def from_photos_count(cls, photos_count: int):
        return cls(photos_count//4 + (1 if photos_count % 4 else 0))

    def add_photo(self, label: str):
        for page in self.photos:
            if len(page) < 4:
                page.append(label)
                return f'{label} photo added successfully on page {self.photos.index(page)+1} slot {len(page)}'
        return 'No more free slots'

    def display(self):
        return ('-----------\n' +
                '-----------\n'.join([(' '.join(['[]' for _ in self.photos[x]])+'\n')
                                      if x < len(self.photos) else '\n' for x in range(self.pages)]) + '-----------')


album = PhotoAlbum(2)

print(album.add_photo("baby"))

print(album.add_photo("first grade"))

print(album.add_photo("eight grade"))

print(album.add_photo("party with friends"))

print(album.photos)

print(album.add_photo("prom"))

print(album.add_photo("wedding"))

print(album.display())
