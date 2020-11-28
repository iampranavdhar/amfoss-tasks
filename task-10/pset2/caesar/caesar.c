#include <stdio.h>
#include <cs50.h>
#include <string.h>
#include <ctype.h>
#include <math.h>
#include <stdlib.h>

bool is_valid_key(string s);

int main(int argc, string argv[])
{
    if (argc != 2 || !is_valid_key(argv[1]))
    {
        printf("Usage: ./caesar key\n");
        return 1;
    }

    string s = get_string("Plaintext:");
    printf("ciphertext:");
    int i = 0;
    int k = atoi(argv[1]);
    char ch = s[i];
    {

        for (i = 0; i < strlen(s); i++)
        {

            if (!isalpha(s[i]))
            {
                printf("%c", s[i]);
            }

            else if (s[i] > 'Z') //if its >Z it must be definitely an small number(see ascii table) so subtract 'a' so that we get dist from a.
            {
                printf("%c", ((s[i] - 'a' + k) % 26) + 'a');
            }
            else
            {
                printf("%c", ((s[i] - 'A' + k) % 26) + 'A');
            }
        }
    }
    printf("\n");
}

bool is_valid_key(string(s))
{
    for (int i = 0; i < strlen(s); i++)
    {
        char ch = s[i];
        if (!isdigit(ch))
        {
            return false;
        }
    }
    return true;
}


