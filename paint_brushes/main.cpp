#include <iostream>
#include <fstream>


using namespace std;
int look(int,int,int, int*, int);

ifstream infile ("input.txt");
int main()
{
    int brush1 = 0;
    int brush2 = 0;
    int t, n,found;
    int change = 0;
    //cin >> t;
    //cin >> n;
    infile >> t;
    for (int test=0; test<t; test++){
    change = 0;
    infile >> n;
    int colors[n];
    for (int i=0; i<n; i++)
        //cin >> colors[i];
        infile >> colors[i];

    brush1 = colors[0];
    change++;
    for (int i=1; i<n; i++)
    {
        if(colors[i] == brush1){}

        else if (colors[i] == brush2){}

        else if (i == 1)
            {   brush2 =colors[i];
                change++;
            }
        else{
            found = look(i+1,brush1, brush2, colors, n);
            if (found == brush1)
            {
                brush2 = colors[i];
                change++;
            }
            else if (found == brush2)
            {
                brush1 = colors[i];
                change++;
            }
            else if(found == 0)
            {
                brush1 == colors[i];
                change++;
            }
        }
    }
      cout << change << endl;
    }

      return 0;
}
int look(int i,int brush1, int brush2, int* colors, int len)
{
    for (int x =i; x<len; x++)
    {
        if (colors[x] == brush1)
            return brush1;
        else if (colors[x] == brush2)
            return brush2;
        else{return 0;}

    }
}


