
//Task 1: Recursive Factorial

#include <iostream>
using namespace std;
int factorial(int n){
    if(n == 0){ 
    return 1;
}
    return n * factorial(n-1);
}
int main(){
   int d;
    cin>> d;
    if(d>=0 && d<=12) 
    cout << factorial(d);
   
    return 0;
   
}

   //Task 2: Recursive Fibonacci

   #include <iostream>
   using namespace std ;
   int fiboncci(int n){
    if(n == 0){
        return 0;
    }

    return  fiboncci(n-1)+fiboncci(n-2);
   }
   int main(){
    int d;
    cin>> d;
    if(d>=0 && d<=20) 
    cout << fiboncci(d);
   


    return 0;
   }


   // Task 3: Recursively Reverse a String
   
   #include <iostream>
   #include <string> 
   #include <algorithm>
   using namespace std;
   string reverseString(string n){
    reverse(n.begin(),n.end());
 
    return n;
   }
   int main(){
    string d;
    cin>> d;
    cout << "Reversed string: "<< reverseString(d);
    return 0;
   }



//Task 4: Use `count`, `min_element`, `max_element`

#include <iostream>
#include <algorithm>
#include <vector>
using namespace std ;
int main(){
    vector <int> num(7);

    
    for(int i=0;i<7;i++){
        cin>>num[i];
    }
    int count=0;
    int  f;
    cin>>f;
    for(int i=0;i<7; i++){  //int  count = count_if(nums.begin(), nums.end(), [f](int x){ return x == f; });
        if(f == num[i] ){
            count++;
            
        }
       
    }
    cout << "Count of "<< f << " : "<<count ;
    cout <<endl;
    auto min= min_element(num.begin(),num.end());
    auto max = max_element(num.begin(),num.end());
    cout<<"MAX: "<< *max<<endl;
    cout<<"MIN: "<< *min;



    return 0 ;
}
    

   //Task 5: Recursive Power Function
   
   #include  <iostream>
   using namespace std;
   int Powerfunction(int first, int powerr){
    if(powerr == 0) return 1;
    return first *Powerfunction(first, powerr-1);
}
int main(){
    int m,b;
    cin>>m>>b;
    if(m<=10&& m>=0  && b>=0 && b<=10)
    cout<< Powerfunction(m,b);
}



 
