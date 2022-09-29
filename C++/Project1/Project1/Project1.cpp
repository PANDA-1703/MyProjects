#include <iostream>
#include <string>
#include <fstream>
#include <sstream>
#include <vector>

using namespace std;

struct StudentRecord {
public:
    StudentRecord(
        string id,
        string firstName,
        int age,
        string phoneNumber
    )
    {
        Id = id;
        FirstName = firstName;
        PhoneNumber = phoneNumber;
        Age = age;
    };

    void display() {
        cout << "   Student ID: " << Id << endl;
        cout << "   First Name: " << FirstName << endl;
        cout << " Phone Number: " << PhoneNumber << endl;
        cout << "          Age: " << Age << endl;
        cout << endl;
    }

    string Id;
    string FirstName;
    string PhoneNumber;
    int Age;


};

void displayStudents(vector<StudentRecord>& students) {

    for (auto student : students) {
        student.display();
    }
}

int main()
{
    ifstream inputFile;
    inputFile.open("testdata.csv");
    string line = "";

    vector<StudentRecord> students;
    while (getline(inputFile, line)) {

        stringstream inputString(line);

        //StudentId, Last Name, FirstName, Age, Phone Number, GPA
        string studentId;
        string lastName;
        int age;
        string phone;
        string tempString;

        getline(inputString, studentId, ',');
        getline(inputString, lastName, ',');
        getline(inputString, tempString, ',');
        age = atoi(tempString.c_str());
        getline(inputString, phone, ',');


        StudentRecord student(studentId, lastName, age, phone);
        students.push_back(student);
        line = "";
    }

    displayStudents(students);
}