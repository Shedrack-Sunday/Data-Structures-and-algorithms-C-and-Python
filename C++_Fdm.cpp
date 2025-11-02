#include <iostream>
#include <string>
#include <vector>
#include <iomanip>   // Defines setprecision
#include <limits>    // Defines numeric_limits
#include <math.h>


/// C++ is efficient and only loads the code it's told to.

// #include <iostream> gives you cout, cin, and endl.

// #include <iomanip> gives you I/O manipulators like setprecision.

// #include <limits> gives you access to information about data types, like numeric_limits<double>::max(). 

using namespace std;

int main() {
    /*vector<string> messages = { "Hello", "from", "C++", "in", "WSL2!"};

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

    cout << (5/3) << endl;
    cout << (15/5) << endl;

    cout << (3/3) << endl;

    cout << (-5/3) << endl;
    cout << (5/-3) << endl;


    string text = "john' said: \"heya!\" \\";
    cout << text << endl;

    char letter = '@';
    cout << letter << endl;

    int number = 7; //between -21^31 to 2^31 -1
    cout << number << endl;

    long long largeNumber = 98888888LL; // -2^26 to 2^62 - 1
    cout << largeNumber << endl;

    double decimalNumber = 344.33; // higher precisson than floats
    cout << decimalNumber << endl;

    bool thisisfalse = false;
    bool thisistrue = true;
    cout << thisisfalse << " and " << thisistrue << endl;



 // Set precision for full double output
    cout << setprecision(numeric_limits<double> ::digits10 + 1);

    // 1. Assign the maximum possible value for a double
    double d = numeric_limits<double> ::max();
    cout << "Maximum double value:    " << d << endl;

    // 2. "Increment" the variable (d = d + 1)
    // Note: Adding 1 to such a huge number might do nothing due to precision.
    // Let's try adding a huge number instead, or multiplying.
    d = d * 2; 
    cout << "After multiplying max by 2: " << d << endl;
    cout << "---" << endl;

    // 3. Assign the "most negative" value (which is -max)
    d = numeric_limits<double> ::max();
    cout << "Most negative double:    " << d << endl;

    // 4. "Decrement" the variable (multiply by 2)
    d = d * 2;
    cout << "After multiplying min by 2: " << d << endl;
    cout << "---" << endl;

    // 5. What about std::numeric_limits<double>::min()?
    // This is the SMALLEST POSITIVE number, not the most negative.
    d = numeric_limits<double>::min();
    std::cout << "Smallest POSITIVE double: " << d << endl;
    
    // 6. Decrement it (d = d - 1)
    d = d - 1.0;
    cout << "Smallest positive - 1.0:  " << d << endl;

    
   //  If a variable is declared as auto and
   // assigned a value at the same time its type is inferred from that of the value.
   auto textNew = 456.999999999999;
   cout << textNew << endl;

   // C++ has a construct called the typedef, or type definition. It allows us to
   // give certain types new names. Since typing ❧♦♥❣ ❧♦♥❣ for every large integer
   // variable is very annoying, we could use a type definition to alias it with the
   // much shorter ❧❧ instead

   typedef long long ll;

   ll largeFigure = 98993934979734LL;
   cout<< largeFigure << endl;

   string name;
   string fullname;

   cout << "Hello, what is your name?";
   cin >> name;

   // Clear the leftover newline from the input buffer
   cin.ignore(numeric_limits<streamsize>::max(), '\n');

   cout << "Try your full name please" <<  endl;
   getline(cin, fullname);

   int age;
   cout<< "Kindy input your age.";
   cin >> age;

   cout << " Your name is " << name << "," << " You are " << age << " Years old" << endl;


   int num1, num2;
   cout << " Enter two mumbers:";
   cin >> num1;
   cin >> num2;

   cout << (num1 == num2);
   cout << (num1 != num2);
   cout << (num1 == num2);
   cout << (num1 > num2);
   cout << (num1 < num2);
   cout << (num1 <= num2);
   cout << (num1 >= num2);


   int input;
   cout << "please enter an input:" << endl;
   cin >> input;

   if (input % 15 == 0) {
    cout << " FizzBuzz" << endl;
   } else if (input % 5 ==0) {
    cout << " Buzz" << endl;
   } else {
    cout << input << endl;
   }
*/

    int repetitions = 0;
    cin >> repetitions;

    for ( double i = 0; i < repetitions; i++) {
        cout << "This is a sample repetitive task" << endl;
    }
    

    int check = 36;

    for (int divisor = 2; divisor * divisor <= check; ++divisor) {
        if (check % divisor == 0) {
            cout << check << "is not prime!" << endl;
            cout << "It equals" << divisor << "x" << (check / divisor) << endl;
            break;
        }
    }

    for (int divisor = 1; divisor <= check; ++divisor) {
        if (check % divisor == 0) {
            continue;
        }
        cout << divisor << "does not divide" << check << endl;
        }
   
    return 0;
}