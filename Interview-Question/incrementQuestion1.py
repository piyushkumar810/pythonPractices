# i=1
# j=2
# l=1

# k= (i++ + ++i + j || l++)
# print(i,l,k)


''''However, keep in mind that Python does not support the ++ and -- increment/decrement operators as 
     in C/C++'''

# in c++

'''
include <iostream>
using namespace std;
int main() {
    int i = 1;
    int j = 2;
    int l = 1;

    int k = (i++ + ++i + j || l++);

    cout << "i = " << i << endl;
    cout << "l = " << l << endl;
    cout << "k = " << k << endl;

    return 0;
}
'''