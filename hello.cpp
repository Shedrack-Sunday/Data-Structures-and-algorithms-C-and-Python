#include <iostream>
#include <string>
#include <vector>

int main() {
    std::vector<std::string> messages = { "Hello", "from", "C++", "in", "WSL!"};

    for (const std::string& word : messages) {
        std::cout << word << " ";
    }
    std::cout << std::endl;

    return 0;
}