def student_info(name,age,/,*,city, gender):
    print(f"{name} ,{age} years old, lives in {city}, {gender}") 
student_info("udhay",22,city="rajamundry",gender="male")

Output:
    udhay ,22 years old, lives in rajamundry, male
    #include <iostream>


void modifyValue(int x) {
    x = x + 10; 
    cout << "Inside function: " << x << endl;
}

int main() {
    int num = 5;
    cout << "Before function call: " << num << endl;

    // Pass the value of num to the function
    modifyValue(num);

    // The original value of num remains unchanged
    cout << "After function call: " << num << endl;

    return 0;
}