import unittest 

def add(num_1,num_2):
    return num_1 + num_2

class Black_boxtest(unittest.TestCase):

    def test_add_two_positive(self):
        num_1 =10
        num_2 = 5

        result = add(num_1,num_2)

        self.assertEqual(result,15)

    def test_add_two_negatives(self):
        num_1 =-10
        num_2 = -7

        result = add(num_1,num_2)

        self.assertEqual(result,-17)

if __name__=='__main__':
    unittest.main()

