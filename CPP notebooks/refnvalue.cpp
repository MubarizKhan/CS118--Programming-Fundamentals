#include <iostream>
using namespace std;


void second_function(int &v) {
  v = v + 10;
  cout << " - second function changed v to: " << v << endl;
  cout << " - address of v : " << &v << endl;
}
// ^-- BAD idea! Do not do this!



void first_function(int v) {
  v = v + 10;
  cout << " - first function changed v to:  " << v << endl;
  cout << " - address of v : " << &v << endl;
}

void runner() {
  int x;
  x = 0;

  cout << "Address of x = " << &x << endl << endl;
  cout << "Step 1: x = " << x << endl;

  first_function(x);
  cout << "Step 2: x = " << x << endl;

  second_function(x);
  cout << "Step 3: x = " << x << endl;
}








void test_array(int b[], int size) {
    cout << "Inner function ... " << endl;
    cout << "Address of b: " << b << endl; 
    for (int i=0; i < size; i++)
      cout << b[i] << " ";
    cout << endl;

    b[0] = 24;
}

void array_as_args() {
  int a[] = {0, 1, 2, 3, 4};
  test_array(a, 5);
  cout << "Address of a: " << a << endl;

  cout << "Outer function ...  " << endl;
  for (int i=0; i < 5; i++)
    cout << a[i] << " ";
  cout << endl;
}


int main() {
  // runner();

  array_as_args();
  return 0;
}
