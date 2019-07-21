#include <iostream>
using namespace std;

struct student {
  int rollno;
  float marks;
};

void struct_array_test() {
  student s1;
  s1.rollno = 24;
  s1.marks = 24.5;

  cout << "s1.marks      = " << s1.marks << endl;

  // return;


  student *sPtr;
  sPtr = &s1;

  cout << "(*sPtr).marks = " << (*sPtr).marks   << endl;






  // or shorthand
  cout << "sPtr->marks   = " <<   sPtr->marks   << endl; // don't need the * here!
  // (*p).      is equivalent to       p->

}



int main() {
  struct_array_test();
  return 0;
}
