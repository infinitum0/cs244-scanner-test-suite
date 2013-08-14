cs244-scanner-test-suite
========================
* Testing using python's unit tests
* Updated makefile for compiling the testscanner__full.c file
* See http://web.ee.sun.ac.za/~ccoetzee/wiki/ for a guide on creating test files

=How to use=

==Getting this repository==
* Enter git clone [REPOSITORY_URL_HERE]

==Creating testcases / running==
* Place the testscanner_full.c in your source directory
* Place the new MakeFile in your source directory
* Place testcases in the test directory
* Modify variables in the unit_test2.py script file to point to your specific directories
* Make sure that your scanner.c only uses eprintf/leprintf as using normal printf anywhere will make the tests fail
