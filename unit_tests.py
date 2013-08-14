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

class Color:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'


def append_fail(string)
    return Color.FAIL + "[FAIL]: " + string + Color.ENDC

def print_err(string):
    print append_fail(string) 

def print_ok(string):
    print Color.OKBLUE+ "[OK]: " + string + Color.ENDC


class Token:
    TOKEN_EOF=                  0
    TOKEN_ID=                   1
    TOKEN_NUMBER=               2
    TOKEN_STRING=               3
    
    
    TOKEN_ARRAY=                4
    TOKEN_BEGIN=                5
    TOKEN_BOOLEAN=              6
    TOKEN_DEFINE=               7
    TOKEN_DO=                   8
    TOKEN_ELSE=                 9
    TOKEN_ELSIF=                10
    TOKEN_END=                  11
    TOKEN_FALSE=                12
    TOKEN_IF=                   13
    TOKEN_INTEGER=              14
    TOKEN_LEAVE=                15
    TOKEN_NOT=                  16
    TOKEN_PROGRAM=              17
    TOKEN_READ=                 18
    TOKEN_RELAX=                19
    TOKEN_THEN=                 20
    TOKEN_TRUE=                 21
    TOKEN_WHILE=                22
    TOKEN_WRITE=                23
    
    
    TOKEN_EQUAL=                24
    TOKEN_GREATER_EQUAL=        25
    TOKEN_GREATER_THAN=         26
    TOKEN_LESS_EQUAL=           27
    TOKEN_LESS_THAN=            28
    TOKEN_NOT_EQUAL=            29
    
    
    TOKEN_MINUS=                30
    TOKEN_OR=                   31
    TOKEN_PLUS=                 32
    
    
    TOKEN_AND=                  33
    TOKEN_DIVIDE=               34
    TOKEN_MULTIPLY=             35
    TOKEN_REMAINDER=            36
    
    
    TOKEN_CLOSE_BRACKET=        37
    TOKEN_CLOSE_PARENTHESIS=    38
    TOKEN_COMMA=                39
    TOKEN_DOT=                  40
    TOKEN_GETS=                 41
    TOKEN_OPEN_BRACKET=         42
    TOKEN_OPEN_PARENTHESIS=     43
    TOKEN_SEMICOLON=            44
    TOKEN_TO=                   45


def pre_test():
    old = os.getcwd()
    os.chdir("parts/part1")
    subprocess.call("make");
    os.chmod("testscanner", 0755)
    os.chdir(old)

DRIVER_PROGRAM = 'parts/part1/testscanner_int'

def run_command(program, *args):
    program = [program]
    program.extend(args)
    try:
        output = subprocess.check_output(program);
        return (0, output)
    except subprocess.CalledProcessError as e:
        return (e.returncode, None)




class Tests(unittest.TestCase):
    #(testfile, output)
    to_pass = [
        ("tests/test1_reserved_words_P.simpl", [
        11
        33
        4
        5
        6
        7
        8 9 10 12 13 14 15 16 31 17 18 19 20 21 22 23
        ]),
        # Comment testing
        ("tests/test2_comment_nested_P.simpl", ""),
        ("tests/test3_comment_neted_P.simpl", ""),
        
        # Numerical
        ("tests/test8_numerical_P.simpl", "2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2"),
    ]
    
    comments_fail = [
        ("tests/test4_comment_nested_broken_F.simpl"),
        ("tests/test5_comment_nested_broken_F.simpl"),
        ("tests/test6_comment_nested_broken_F.simpl"),        
        ("tests/test7_comment_nested_broken_F.simpl"),        
    ]


    def test_pass(self):
        for c, test_case in enumerate(self.to_pass):
            result = run_command(DRIVER_PROGRAM, test_case[0])
            
            if(result[0] != 0):
                print_err(test_case[0])
            else:
                print_ok(test_case[0])
            self.assertEqual(0, result[0])
            
            if(result[1].strip() != test_case[1]): 
                print_err(test_case[0])
            else:
                print_ok(test_case[0])
                
            self.assertEqual(result[1].strip(), test_case[1])
    
    def test_broken_comments(self):
        for c, i in enumerate(self.comments_fail):
            result = run_command(DRIVER_PROGRAM, i)
            if(result[0] != 2): 
                print_err(i)
            else:
                print_ok(i)
            self.assertEqual(2, result[0])
            # check for segfault
            if(result[0]==139): 
                print(result[1])
            self.assertNotEqual(139, result[0])
def main():
    pre_test()
    unittest.main()

if (__name__=="__main__"):
    main()

