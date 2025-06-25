
// Task 1:
 
#include <iostream> 
#include <stack> 
using namespace std;
int main(){
    int x;
    cin>> x;
    stack<int> den;
    for(int i=0;i<x; i++){
        int l;
        cin>> l;
        den.push(l);
    }
    while(!den.empty()){
        cout << den.top()<<" ";
        den.pop();
    }
   

    return 0 ;
}

//task 2:

#include <iostream>
#include <stack>
#include <string>
using namespace std;
int main(){
    string word;
    cin>> word;
    stack<char> letters;
    for(char d : word ){
        letters.push(d);
    }
    while(!letters.empty()){
        cout<<letters.top();
        letters.pop();

    }
      return 0;
}

// Task 3:

#include <iostream>
#include <queue>
using namespace std;
int main(){
    queue<int> num;
    for(int i=0;i<5;i++){
        int d;
        cin>>d;
        num.push(d);
    }
    cout<<"Dequeued: ";
    while(!num.empty()){
        cout<< num.front()<< " ";
        num.pop();
    }
    return 0;
}
    
   // Task 4
   
#include <iostream>
#include <queue>
#include <string>

using namespace std;
int main(){
    queue<string> names;
    for(int i=0;i<3; i++){
        string name;
        cin>> name;
        names.push(name);
    }
    while(!names.empty()){
        cout<<" Serving: " << names.front()<< endl;
        names.pop();
    }
    return 0;
}
    */
   // Task 5: 
   
#include <iostream>
#include <deque>
#include <algorithm>
using namespace std;
int main(){
    deque<int> num;
    for(int i=0;i<3;i++){
        int d;
        cin>>d;
        num.push_back(d);
    }
    sort(num.begin(),num.end());
    for(int rev_num : num ){
        cout << rev_num<<" ";
    }
    cout<< endl;
    cout<<"Pop back: "<< num.back()<< endl;
    num.pop_back();
    cout<<"Pop front: "<< num.front()<< endl;
    num.pop_front();

    cout<< "Remaining: ";
    for(int x: num){
        cout<< x<<" ";

    }
    cout << endl;

}
    
   //Task 6: 
   #include <iostream>
   #include <deque>
   #include <string>
   using namespace std; 
   int main(){
    string m;
    cin>>m;
    deque<char> dan;
    for(char x: m){
        dan.push_back(x);
    }

    bool ispalindrom = true;
    while(dan.size()>1){
        if(dan.front() != dan.back()){
            ispalindrom = false;
            break;
            
        }
        dan.pop_front();
        dan.pop_back();
    }
    if(ispalindrom){
        cout<<"Полиндром , все четко ╰(▔∀▔)╯ ";
    }
    else{
        cout<<"Чел , это не полиндром (´･ᴗ･ ` )";
    }
    return 0;


   }





