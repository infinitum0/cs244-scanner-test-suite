#!/usr/bin/python
import os
import sys
import subprocess
import unittest
import re

C_HEADER = '\033[95m'
C_OKBLUE = '\033[94m'
C_OKGREEN = '\033[92m'
C_WARNING = '\033[93m'
C_FAIL = '\033[91m'
C_ENDC = '\033[0m'

# For your convenience
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



RESULT_PATTERN =  re.compile("(?P<id>\d+)\{(?P<output>.*?)\}\s")

def print_ok(string):
    print C_OKBLUE + string + C_ENDC

def print_fail(string):
    print C_FAIL + string + C_ENDC

def print_pass(string):
    print C_OKGREEN + string + C_ENDC

def get_files(path):
    '''Returns a list of files with `path`  their relative paths'''
    files = os.listdir(path)
    files = [os.path.join(path,i) for i in files]
    return files
    
def get_token_results(path_to_file):
    '''Returns a list token_id, result pairs'''
    f = open(path_to_file,'r')
    line = f.readline()
    f.close()
    line = line.strip()
    # adding space so the pattern matches
    line = line + ' '
    line = line[1:]
    RESULT_PATTERN.findall(line)
    return line

def get_pairs_postfix(path, postfix):
    '''Returns list of (file_path, expected_output) tuples'''
    final = []
    for i in os.listdir(path):
        if(not i.endswith(postfix)): continue
        rp = os.path.join(path, i)
        tokens = get_token_results(rp)
        final.append((rp,tokens.strip()))
    return final

def get_fail(path, postfix="F.simpl"):
    return get_pairs_postfix(path, postfix)
        
def get_pass(path, postfix="P.simpl"):
    return get_pairs_postfix(path, postfix)

def run_command(program, *args):
    '''Returns a returncode, output tuple receieved after running program with args'''
    program = [program]
    program.extend(args)
    try:
        try:
            output = subprocess.check_output(program);
            return (0, output.strip())
        except subprocess.CalledProcessError as e:
            return (e.returncode, "")
    except KeyboardInterrupt as e:
        print "Was running: `{}`, before crashing.".format(program)
        

def pre_test():
    old = os.getcwd()
    os.chdir("parts/part1/")
    subprocess.call(["make", "testscanner_full"]);
    os.chmod("testscanner_full", 0755)
    os.chdir(old)

class Part1Tests():
    program = 'parts/part1/testscanner_full'
    tests = "tests/"
    
    def assertEqual(self, expected, got):
        return expected == got
    def assertNotEqual(self, expected, got):
        return expected != got

    def test_pass(self):
        expected = get_pass(self.tests)
        for c, p in enumerate(expected):
            result = run_command(self.program, p[0])
            if(not self.assertEqual(0, result[0])):
                print_fail("[FAIL ON RETURN]: {}, {} != {}".format(p[0], result[0] , 0))
                continue
            if(not self.assertEqual(p[1], result[1])):
                print_fail("[FAIL ON OUTPUT]: {}\n OUTPUT EXPECTED:\n`{}`\n BUT GOT OUTPUT:\n`{}`".format(p[0], p[1], result[1]))
                continue
            print_pass("[PASS]: {}".format(p[0]))
    
    def test_fail(self):
        expected = get_fail(self.tests)
        for c, p in enumerate(expected):
            result = run_command(self.program, p[0])
            if(not self.assertNotEqual(0, result[0])):
                print_fail("[FAIL ON RETURN]: {}, {} == {}".format(p[0], result[0] , 0))
                if(result[0]==0): print_fail("PROGRAM EXITED WITH OUTPUT:\n `{}`".format(result[1]))
            print_pass("[PASS]: {}".format(p[0]))

    def run(self):
        self.test_pass()
        self.test_fail()


if __name__ == "__main__":
    pre_test()
    test1 = Part1Tests()
    test1.run()


