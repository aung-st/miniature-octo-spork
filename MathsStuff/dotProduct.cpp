#include <iostream>

using namespace std;

int main(){
    int n;
    int product;
    
    cout << "Enter dimension(s):";
    cin >> n;

    int *v1 = new int(n);
    int *v2 = new int(n);

    for (int i = 0; i < n; i++) {
 
            int e;
            cout << "Vector 1: Enter Element:";
            cin >> v1[i];
        }

    cout << "Vector 1: ";
    for (int i = 0; i < n; i++) {
 
        cout << v1[i] << " ";
	}
	cout << endl;

    for (int i = 0; i < n; i++) {
 
            int e;
            cout << "Vector 2: Enter Element:";
            cin >> v2[i];

    }

    cout << "Vector 2: ";
    for (int i = 0; i < n; i++) {
 
            cout << v2[i] << " ";
	}
	cout << endl;

    for (int i = 0; i < n; i++) {
        product += v1[i] * v2[i];
	}

    cout << "Dot product is: " << product;

  
}
