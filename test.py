import unittest
import mask_string

class TestMaskString(unittest.TestCase):

	def testMask(self):
		self.assertEqual(mask_string('Hello world!', 2, 7), 'He****rld!')
		self.assertEqual(mask_string('Hello world!', 2, -1), 'He****')
		self.assertEqual(mask_string('Hello world!', 2, 7, mask='...'), 'He...rld!')
		self.assertEqual(mask_string('Hello world!', 0, 7, mask='...'), '...rld!')


if __name__ == '__main__':
	unittest.main()
