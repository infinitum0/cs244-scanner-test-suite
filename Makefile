#
# Makefile for SIMPL
#

# compiler flags
DEBUG    = -ggdb
OPTIMISE = -O0
WARNINGS = -Wall -Wextra -Wno-variadic-macros -pedantic
CFLAGS   = $(DEBUG) $(OPTIMISE) $(WARNINGS)
DFLAGS   = -DDEBUG_PARSER

# commands
CC       = gcc
RM       = rm -f
COMPILE  = $(CC) $(CFLAGS) $(DFLAGS)

# files
EXES     = testscanner

# directories
LOCALBIN = ~/bin

### RULES ######################################################################

# executables

testscanner: testscanner.c error.o scanner.o token.o
	$(COMPILE) -o $@ $^


testscanner_full: testscanner_full.c error.o scanner.o token.o
	$(COMPILE) -o $@ $^

testscanner_int: testscanner_int.c error.o scanner.o token.o
	$(COMPILE) -o $@ $^

# units

error.o: error.c error.h
	$(COMPILE) -c $<

scanner.o: scanner.c scanner.h
	$(COMPILE) -c $<

token.o: token.c token.h
	$(COMPILE) -c $<

### PHONY TARGETS ##############################################################

.PHONY: all clean install uninstall

all: testscanner

clean:
	$(RM) $(EXES)
	$(RM) *.o
