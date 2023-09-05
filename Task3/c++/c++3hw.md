include <iostream>
int main ()
{
    int x;
    std::cout << "enter value: ";
    std::cin >> x;

    int a, b;
    for(a = 1; a <= x; a++)
    {
        for(b=2;b<a;b++)
        {
            if(a%b==0)
            {
                break;
            }
        }
        if(a==b)
        {
            std::cout << a;
        }
    }
    

