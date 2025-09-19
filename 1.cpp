#include <iostream>
#include <deque>
using namespace std;

deque<int> build_initial_deck(int n) {
    deque<int> d;
    for (int i = n; i >= 1; i--) {
        d.push_front(i);
        for (int j = 0; j < i; j++) {
            int last = d.back(); 
            d.pop_back();   
            d.push_front(last); 
        }
    }
    return d;
}

int main() {
    int t;
    cin >> t; 
    while (t--) {
        int n;
        cin >> n; 
        deque<int> d = build_initial_deck(n);
        
        for (int i = 0; i < d.size(); i++) {
            cout << deck[i] << " ";
        }
        cout << endl;
    }
    return 0;
}
