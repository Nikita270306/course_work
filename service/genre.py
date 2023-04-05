from dao.genre import GenreDAO


class GenreService:
    def __init__(self, dao: GenreDAO):
        self.dao = dao

    def get_one(self, bid):
        return self.dao.get_one(bid)

    def get_all(self, filters):
        genre = self.dao.get_all()
        if filters.get('page') is not None:
            genre = genre.limit(12).offset((int(filters.get('page')) - 1) * 12)
        return genre

    def create(self, genre_d):
        return self.dao.create(genre_d)

    def update(self, genre_d):
        self.dao.update(genre_d)
        return self.dao

    def delete(self, rid):
        self.dao.delete(rid)
