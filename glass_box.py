from concurrent.futures.thread import _threads_queues
from curses import flash
from enum import Flag
from fcntl import F_GETLEASE
import unittest

def is_of_legal_age(age):
    if age >= 18:
        return True
    else :
        return False

class glass_box (unittest.TestCase):
    
    def test_is_of_legal_age(self):
        age = 20

        result = is_of_legal_age(age)

        self.assertEqual(result,True)

    def test_is_under_age(self):
        age=14

        result= is_of_legal_age(age)

        self.assertEqual(result,False) 

if __name__=='__main__':
    unittest.main()
