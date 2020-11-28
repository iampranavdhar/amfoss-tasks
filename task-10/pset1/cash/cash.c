#include <stdio.h>
#include <cs50.h>
#include <math.h>

int main(void)
{
    float owed;
    do
    {
        owed = get_float("Change Owed:");
    }
    while (owed < 0);

    int cents = round(owed * 100);

    int a;
    {
        a = (cents / 25);
    }

    int r1;
    {
        r1 = (cents - a * 25);
    }

    int b;
    {
        b = (r1 / 10);
    }

    int r2;
    {
        r2 = (cents - a * 25 - b * 10);
    }

    int c;
    {
        c = (r2 / 5);
    }

    int r3;
    {
        r3 = (cents - a * 25 - b * 10 - c * 5);
    }

    {
        printf("%i\n", a + b + c + r3);
    }
}
