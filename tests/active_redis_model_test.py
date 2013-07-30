from active_redis import ActiveRedis, ActiveRedisModel, UUIDGenerator
import unittest


TOPGUN_UUID = 1
TITANIC_UUID = 2


class Movie(ActiveRedisModel):
    stored_attrs = ['title', 'year', 'author']

    def __init__(self, uuid, title, year, author):
        self.uuid = uuid
        self.title, self.year, self.author = title, year, author


class ActiveRedisModelTest(unittest.TestCase):

    def setUp(self):
        ActiveRedis.config = {'connexion': {'db': 3},
                              'namespace_prefix': 'mycinema'}
        Movie.delete_all()

    def test_pluralize_model_name(self):
        self.assertEqual('movies', Movie.pluralize_model_name())

    def test_delete_all(self):
        Movie(TOPGUN_UUID, 'TopGun', 1987, 'Tony S.').save()
        self.assertTrue(Movie.delete_all())
        self.assertEqual(0, Movie.count())

    def test_save(self):
        self.assertTrue(Movie.delete_all())
        self.assertEqual(0, Movie.count())
        topgun = Movie(TOPGUN_UUID, 'TopGun', 1987, 'Tony S.')
        self.assertTrue(topgun.save())
        titanic = Movie(TITANIC_UUID, 'Titanic', 1997, 'James C.')
        self.assertTrue(titanic.save())
        self.assertEqual(2, Movie.count())
        self.assertEqual(2, len(Movie.find_all()))

    def test_find(self):
        topgun = Movie(TOPGUN_UUID, 'TopGun', 1987, 'Tony S.')
        topgun.save()
        titanic = Movie(TITANIC_UUID, 'Titanic', 1997, 'James C.')
        titanic.save()
        self.assertEqual(topgun.title, Movie.find(TOPGUN_UUID).title)
        self.assertEqual(titanic.title, Movie.find(TITANIC_UUID).title)

    def test_update_attr(self):
        topgun = Movie(TOPGUN_UUID, 'TopGun', 1987, 'Tony S.')
        topgun.save()
        topgun.update_attr('title', 'Top Gun')
        self.assertEqual('Top Gun', Movie.find(TOPGUN_UUID).title)

    def test_delete(self):
        Movie(TOPGUN_UUID, 'TopGun', 1987, 'Tony S.').save()
        Movie(TITANIC_UUID, 'Titanic', 1997, 'James C.').save()
        m = Movie.find(TOPGUN_UUID)
        self.assertTrue(m.delete())
        self.assertEqual(1, Movie.count())
        self.assertEqual(1, len(Movie.find_all()))


if __name__ == '__main__':
    unittest.main()

