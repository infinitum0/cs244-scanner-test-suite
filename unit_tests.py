'''
    Author: Chris Coetzee
    
    Python unit tests to be used with the testscanner binary
'''

import os
import sys
import re
import subprocess
import unittest

#self.assertRaises
#self.assertEqual

def pre_test():
    old = os.getcwd()
    os.chdir("parts/part1")
    subprocess.call("make");
    os.chmod("testscanner", 0755)
    os.chdir(old)

DRIVER_PROGRAM = 'parts/part1/testscanner'

def run_command(program, *args):
    program = [program]
    program.extend(args)
    try:
        output = subprocess.check_output(program);
        return (0, output)
    except subprocess.CalledProcessError as e:
        return (e.returncode, None)

    
class ReturnCodesKnown(unittest.TestCase):
    to_pass = [
        'tests/test1.simpl',
        'tests/test2.simpl',
        'tests/test3_comment.simpl',
        'tests/test4_comment.simpl',
        'tests/test6_comments_nested.simpl',
    ]
    results = [0,0,0,0,0]
    
    to_fail = [
        'tests/test5_comment_broken_deep.simpl'
    ]


    def test_pass_return_code(self):
        for c,i in enumerate(self.to_pass):
            print "***[Testing]: {}".format(i)
            self.assertEqual(self.results[c],run_command(DRIVER_PROGRAM, i)[0])
    def test_fail_return_code(self):
        for c,i in enumerate(self.to_fail):
            print "***[Testing]: {}".format(i)
            result = run_command(DRIVER_PROGRAM, i)
            self.assertNotEqual(0, result[0])
            # check for segfault
            self.assertNotEqual(139, result[0])
def main():
    pre_test()
    unittest.main()

if (__name__=="__main__"):
    main()

