import unittest             #we need to import the built-in module 'unittest'
import test_me                 #we need to import the file we want to test.  (i.e. - 'test_me.py')

class TestMain(unittest.TestCase):
    def test_do_stuff(self):                            #Test no.1
        '''Testing what happens if an integer is given'''
        test_param = 10
        result = test_me.do_stuff(test_param)
        self.assertEqual(result, 15)

    def test_do_stuff2(self):                           #Test no.2
        '''Testing what happens if a string is given'''
        test_param = 'asdf'
        result = test_me.do_stuff(test_param)
        self.assertIsInstance(result, ValueError)

    def test_do_stuff3(self):                           #Test no.3
        '''Testing what happens if we have a NONE type'''
        test_param = None
        result = test_me.do_stuff(test_param)
        self.assertEqual(result, 'Please enter a number')

    def test_do_stuff4(self):                           #Test no.4
        '''Testing what happens if we enter an empty string'''
        test_param = ''
        result = test_me.do_stuff(test_param)
        self.assertEqual(result, 'Please enter a number')

if __name__ == '__main__':                                  #this is standard practice 
    unittest.main()                                         #this is how we run the test