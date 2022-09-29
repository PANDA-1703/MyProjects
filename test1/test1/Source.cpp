#include <locale>
#include <iostream>
#include <iterator>
#include <vector>
#include <fstream>
#include <limits>

using namespace std;

class MyCharCType : public ctype<char>
{
public:
    mask const* get_table()
    {
        static vector<ctype<char>::mask> table(classic_table(),
            classic_table() + table_size);
        table[','] = space;
        return &table[0];
    }

    MyCharCType(size_t refs = 0)
        : ctype<char>(get_table(), false, refs)
    {
    }
};

int main()
{
    auto loc = locale(locale(), new MyCharCType());

    ifstream inFile("testdata.csv");
    inFile.imbue(loc);

    inFile.ignore(numeric_limits<streamsize>::max(),
        inFile.widen('\n'));

    int data1;
    while (inFile >> data1)
    {
        cout << data1 << endl;
    }

    return 0;
}