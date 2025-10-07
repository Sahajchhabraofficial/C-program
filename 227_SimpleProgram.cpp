
#include <iostream>
using namespace std;
int main() {
    double length, width, area, perimeter;

    // Input length and width
    cout << "Enter length: ";
    cin >> length;
    cout << "Enter width: ";
    cin >> width;

    // Calculate area and perimeter
    area = length * width;
    perimeter = 2 * (length + width);

    // Display results
    cout << "Area: " << area << endl;
    cout << "Perimeter: " << perimeter << endl;

    return 0;
}