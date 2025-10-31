#include <iostream>
#include <string>
#include <vector>

using namespace std;

int main() {
    vector<string> messages = { "Hello", "from", "C++", "in", "WSL2!"};

    for (const string& word : messages) {
        cout << word << " ";
    }
    cout << endl;


    int five = 5;
    cout << five << endl;
    int seven = 7;
    cout << seven << endl;

    five = seven + 2;
    cout << five << endl;

    return 0;
}