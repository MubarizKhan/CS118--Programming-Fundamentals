#include <iostream>
using namespace std;


int out(int x) {
  cout << "  - called with value: "<< x << endl;
  return x;
}

void if_test() {
  int x = 30;

  if ( x < 25 ) {
    cout << "x is less than 25" << endl;
  } else {
    cout << "x is NOT less than 25" << endl;
  }


  // booleans
  int v = 1;

  if (v)
    cout << "v is true! " << endl;
  else
    cout << "v is false" << endl;


  // 0 is 'false', all other values are 'true'


  // boolean operators
  cout << "Checking and: " << (true && true) << endl;    // python and
  cout << "Checking or : " << (false || false) << endl;  // python or
  cout << "Checking not: " << (!true) << endl;          // python not





  // short circuiting
  cout << "Checking short circuiting ... " << endl;
  int final_val =  out(1) && out(0) ;

  cout << "Final value: " << final_val << endl;

  // ternary operator
  int t =     (3 < 2) ? 7 : 3;
  cout << "t = " << t << endl;

}


void while_test() {
  int i = 0;
  while (i < 5) {
    cout << i << endl;
    i++;   // (almost) the same as:  i += 1;
           // which is the same as:  i = i + 1;
  }
}

void for_test() {
  int i;
  for (i = 0  ; i < 5 ; i++) {
    cout << "for: " << i << endl;
  }
}

int main() {

  // if_test();

  // while_test();

  for_test();

  return 0;
}
