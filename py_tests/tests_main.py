import unittest

class TestMethods(unittest.TestCase):

	def test_one(self):
		var = 1
		self.assertEqual(var, 1)

if __name__ == "__main__":
	unittest.main()