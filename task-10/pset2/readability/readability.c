#include <stdio.h>
#include <cs50.h>
#include <math.h>
#include <string.h>
#include <ctype.h>

int get_index(string s);

int main(void)

{
    string text = get_string("Text:");

    int index = get_index(text);

    if (index >= 16)
    {
        printf("Grade 16+\n");
    }

    else if (index < 1)
    {
        printf("Before Grade 1\n");
    }

    else
    {
        printf("Grade %d\n", index);
    }

}

int get_index(string s)
{
    int letters = 0, sentences = 0, words = 0;
    for (int i = 0; i < strlen(s); i++)
    {
        char ch = s[i];

        if (isalpha(ch))
        {
            letters++;
        }

        if (isspace(ch))
        {
            words++;
        }

        if (ch == '.' || ch == '?' || ch == '!')
        {
            sentences++;
        }
    }

    words++;

    float L = ((float)letters / words * 100);
    float S = ((float)sentences / words * 100);

    float index = 0.0588 * L - 0.296 * S - 15.8;

    return round(index);
}


