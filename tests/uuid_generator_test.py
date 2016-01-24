from active_redis import UUIDGenerator
import unittest

class UUIDGeneratorTest(unittest.TestCase):

    def test_generate_uuid(self):
        self.assertIsNotNone(UUIDGenerator.generate())


if __name__ == '__main__':
    unittest.main()

