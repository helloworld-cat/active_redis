
class PluralizeEngine(object):
    ABERRANT_PLURAL_MAP = {
        'appendix': 'appendices',
        'barracks': 'barracks',
        'cactus': 'cacti',
        'child': 'children',
        'criterion': 'criteria',
        'deer': 'deer',
        'echo': 'echoes',
        'elf': 'elves',
        'embargo': 'embargoes',
        'focus': 'foci',
        'fungus': 'fungi',
        'goose': 'geese',
        'hero': 'heroes',
        'hoof': 'hooves',
        'index': 'indices',
        'knife': 'knives',
        'leaf': 'leaves',
        'life': 'lives',
        'man': 'men',
        'mouse': 'mice',
        'nucleus': 'nuclei',
        'person': 'people',
        'phenomenon': 'phenomena',
        'potato': 'potatoes',
        'self': 'selves',
        'syllabus': 'syllabi',
        'tomato': 'tomatoes',
        'torpedo': 'torpedoes',
        'veto': 'vetoes',
        'woman': 'women',
    }

    VOWELS = set('aeiou')

    @classmethod
    def pluralize(cls, singular):
        if not singular:
            return ''
        plural = cls.ABERRANT_PLURAL_MAP.get(singular)
        if plural:
            return plural
        root = singular
        try:
            if singular[-1] == 'y' and singular[-2] not in cls.VOWELS:
                root = singular[:-1]
                suffix = 'ies'
            elif singular[-1] == 's':
                if singular[-2] in cls.VOWELS:
                    if singular[-3:] == 'ius':
                        root = singular[:-2]
                        suffix = 'i'
                    else:
                        root = singular[:-1]
                        suffix = 'ses'
                else:
                    suffix = 'es'
            elif singular[-2:] in ('ch', 'sh'):
                suffix = 'es'
            else:
                suffix = 's'
        except IndexError:
            suffix = 's'
        plural = root + suffix
        return plural

