from active_redis import PluralizeEngine
import unittest

class PluralizeEngineTest(unittest.TestCase):

    def test_pluralize(self):
        self.assertEqual('', PluralizeEngine.pluralize(''))
        self.assertEqual('posts', PluralizeEngine.pluralize('post'))
        self.assertEqual('movies', PluralizeEngine.pluralize('movie'))
        self.assertEqual('geese', PluralizeEngine.pluralize('goose'))
        self.assertEqual('dollies', PluralizeEngine.pluralize('dolly'))
        self.assertEqual('genii', PluralizeEngine.pluralize('genius'))
        self.assertEqual('joneses', PluralizeEngine.pluralize('jones'))
        self.assertEqual('passes', PluralizeEngine.pluralize('pass'))
        self.assertEqual('zeros', PluralizeEngine.pluralize('zero'))
        self.assertEqual('casinos', PluralizeEngine.pluralize('casino'))
        self.assertEqual('heroes', PluralizeEngine.pluralize('hero'))
        self.assertEqual('churches', PluralizeEngine.pluralize('church'))
        self.assertEqual('xs', PluralizeEngine.pluralize('x'))
        self.assertEqual('cars', PluralizeEngine.pluralize('car'))


if __name__ == '__main__':
    unittest.main()

