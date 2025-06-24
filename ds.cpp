// Task 1 : работа с алгоритмом 
/*
#include <iostream>
#include <vector>
#include <random>
#include <algorithm>
using namespace std;
int main(){
    mt19937 gen(time(0));
    uniform_int_distribution<> dist(1,100);

    vector <int> m;
    for (int i=0; i<10; ++i){
        m.push_back(dist(gen));
    }
    for (int x:m){
        cout << x<<" ";
        cout<<"\n";
    }
    sort(m.begin(), m.end());
    cout<< " sorted vector "<< "  ";
    for (int v:m){
        cout << v<<" ";
        cout<<"\n";
    }
    auto min_el= min_element(m.begin(),m.end());
    auto max_el = max_element(m.begin(),m.end());
    cout<< " MinN : "<< *min_el<< "  "<< " Max :"<< *max_el<<"\n";

    auto last =unique(m.begin(),m.end());
    m.erase(last, m.end());
    for(int d: m ){
        cout<< << "  ";
    }

return 0;

}
*/


// Task 2: работа с set  
/*
#include <iostream>
#include <set>
using namespace std;
    int main(){
    int d;
    cin>> d; 
    set <int> den;
    for(int i =0;i<d;i++){
        int r;
        cin>> r ; 
        den.insert(r);
    }
    cout<< "Unique numbers : ";
    for(int num  : den){
        cout << num<< " " ;
    }
    cout<< endl;
    cout<<"Введи число чел:  ";
    int fin ;
    cin>> fin ; 
    if(den.find(fin) != den.end()){
        cout << " Нашел твой number "<<endl;
    } 
    else{
        cout << "Забудь, его нету "<< endl;
    }

     for(set<int>:: iterator it =den.begin(); it != den.end(); ++it ){
        cout << *it<<"   ";
     }

    return 0;
}
*/


// Task 3: будем работать с map   
/*
#include <iostream>
#include <map>
#include <sstream>

using namespace std;
int main(){
    string input;
    getline(cin, input);
    stringstream ss(input);
    string word;
    map<string ,int> wordcount;
    while(ss>> word){
        wordcount[word]++;

    }
    for(auto &p : wordcount ){
        cout<< p.first<< ":" << p.second<< endl;
    }
    return 0; 

}
    */
// Task 4: про Stack 
/*
#include <iostream>
#include <stack>
using namespace std; 
bool isbalanced(string expr){
    stack<char> st;

    for(char ds: expr){
        if(ds == '('){
            st.push(ds);
    }
        else if(ds ==')'){
            if(st.empty()){
                return false;
            }
            st.pop();


        }
    }
    return st.empty();
}
int main(){
    string input;
    getline(cin,input);
    if(isbalanced(input)){
        cout << " correct! "<<endl;
    }
    else{
        cout<< " Incorrect ! "<< endl ;
    }
    return 0;
}
    */

//Task 5: working with queue 
#include <iostream>
#include <queue>
#include <string>
using namespace std;
    int main(){
        queue<string> names;
        string name;
        cout << "ВВедите 5 имен: "<<endl;
        for(int i =0;i<5;i++){
            cin >> name;
            names.push(name);
        } 
        while(!names.empty()){
            cout << names.front()<<endl;
            names.pop();
        }
        return 0;




}
