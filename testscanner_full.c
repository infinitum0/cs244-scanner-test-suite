/**
 * @brief	A driver program to test the scanner unit.
 * @author	W. H. K. Bester (Modified by C. Coetzee)
 * @date	2013/08/14
 */

#include <stdio.h>
#include <stdlib.h>

#include "error.h"
#include "scanner.h"
#include "token.h"

/* --- function prototypes -------------------------------------------------- */

void print_token(token_t *token);

/* --- main routine --------------------------------------------------------- */

int main(int argc, char *argv[])
{
    char c;
	token_t token;
	FILE *in_file;

	/* set up program name and token */
	setprogname(argv[0]);
	token.string = NULL;

	/* check command-line argument and open file */
	if (argc != 2) {
		eprintf("Usage: %s <filename>", progname());
	}

	if ((in_file = fopen(argv[1], "r")) == NULL) {
		eprintf("File '%s' could not be opened:", argv[1]);
	}
    /*remove the first line of input*/
    while((c = fgetc(in_file))!='\n');
	/* initialise scanner */
	init_scanner(in_file);

	/* iterate over tokens in the input file */
	get_token(&token);
	while (token.type != TOKEN_EOF) {
		print_token(&token);
		get_token(&token);
	}

	/* tell Linux we're happy */
	return EXIT_SUCCESS;
}

/* --- functions ------------------------------------------------------------ */

void print_token(token_t *token)
{   
    printf("%d", token->type);
	switch (token->type) {
	case TOKEN_ID:
		printf("{%s} ", token->lexeme);
		break;
	case TOKEN_NUMBER:
		printf("{%d} ", token->value);
		break;
	case TOKEN_STRING:
		printf("{%s} ", token->string);
		free(token->string);
		break;
    default:
        printf("{} ");
	}
}

/* vim: textwidth=80 tabstop=4
 */
