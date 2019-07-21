#include <iostream>
#include <string.h>  // needed on windows
using namespace std;

void string_test() {
  // A string is a character array

  char a[] = "Hello";
  cout << a << endl;

  // 'H'  'e'   'l'   'l'   'o'   '\0'

  cout << "a[0] = " << a[0] << endl;

  // return ;
  cout << "a[5] = " << a[5] << endl;    // special character:

  if (a[5] == '\0') {
    cout << "a[5] is NULL terminator!" << endl;
  }

  // return;

  int counter = 0;
  for(int i =0; i < 5; i++ ) {
    if (a[i] == 'l')
      counter += 1;
  }

  cout << counter << endl;
  // return ;

  string name = "Mudasser";
  cout << name << endl;
  cout << name[0] << endl;  // exactly the same. So, we'll use this.

}

void string_arrays() {
  int a[] = {1, 5};  // shortcut
  cout << a[0] << endl;


  string people[] = {"Lecturer", "Student"};
  for (int i = 0; i < 2; i++) {
    cout << people[i] << endl;
  }

  // return;

  cout << "Using 2d arrays " << endl;
  char people_chars[2][20] = {"Lecturer", "Student"};
  for (int i = 0; i < 2; i++) {
    cout << people_chars[i] << endl;
  }

}

void string_ops() {
  char s1[10] = "Hello";
  char s2[10] = "World";

  strcpy(s2, s1);
  cout << "After strcpy, s2 is: " << s2 << endl;

  // return ;

  char s3[10] = "Universe";
  strcat(s1, s3);
  cout << "After concat of s3, s1= " << s1 << endl;   // Error
  cout << "After concat of s3, s3= " << s3 << endl;

  // return;




  string name1, name2;
  name1 = "dog";
  name2 = "banana";


  if (name1 == name2)  {
    cout << "name1 and name2 are equal" << endl;
  } else {
    cout << "name1 and name2 are NOT equal" << endl;
  }


  cout << "Comparing " << name1 << " and " << name2 <<  ": "
       << name1.compare(name2) << endl;



}


int main() {
  string_test();
  // string_arrays();

  // string_ops();
  return 0;
}
