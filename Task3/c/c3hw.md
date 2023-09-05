#include <stdio.h>

void main()
{
    int n;
    printf("enter a value: ");
    scanf("%i", &n);
    int i, j;
    for (i = 0; i <= n; i++)
    {
        for (j = 2; j < i; j++)
        {
            if (i % j == 0)
            {
                break;
            }
        }
        if (i == j)
        {
            printf("%i ", i);
        }

    }
}
