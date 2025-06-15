
// Task 1: User's name 

/*
#include <iostream>
#include <string>
using namespace std;
int main(){
    string name;
    cin >> name;
    cout <<"Hello , "<< name<< " !" << endl; 
    return 0;
}
    */


//Task 2: : Sum of Two Numbers (User Input)
/*
#include <iostream>
using namespace std;
int main(){
    int num1,num2;
    cin>> num1>>num2;
    cout<<"The sum is  "<< num1 + num2 << " . " << endl;



    return 0;
}
    */


//Task 3: : Circle Area
/*
#include <iostream>
using namespace std;
int main(){
    float r, pi = 3.14 ;
    cin>> r;
    float area = pi* r*r;
    cout<<" The area is " << area <<"."; 

    return 0;
}
    */
    

//  Task 4:Age in Months

/*
#include <iostream>
using namespace std;
int main(){
    int years;
    cin>> years;
    int month = years* 12;
    cout << " you are " << month << " month old";



    return 0;
} 
    */
    
   
    // Task 5:Temperature Converter
  /*  
#include <iostream>
#include <iomanip>
using namespace std;
int main(){
    float Celsius;
    cin>> Celsius;
    float F = (Celsius* 9.0/5.0) +32;
    cout<<fixed<<setprecision(1);
    cout << "Temperature in Fahrenhei: "<< F << endl;
    return 0;
}
    */
    

//Task 6: Square of a Number
/*
#include <iostream>
#include <cmath>
using namespace std;
int main(){
    int integer;
    cin>> integer;
    cout<<"The square is: " << pow(integer,2)<< endl;
    return 0;
}
    */
    
  //Task 7: Simple Interest Calculator 
 /* #include <iostream>
  using namespace std;
  int main(){
    int P, R, T;
    cin>>P>>R>>T;
    int SI =(P*R*T)/100;
    cout << "Simple Interest is " << SI <<endl;
    return 0;
  }
    */
    

   // Task 8: BMI Calculator
/*  #include <iostream>
   #include <iomanip>
   using namespace std;
   int main(){
    float w,h;
    cin>>w>>h;
    float BMI= w / (h*h);
    cout<< fixed<<setprecision(2);

    cout << "Your BMI is " << BMI<< endl;
    return 0;
   }
    */
    

   // Task 9: Average of Three Numbers
   
  /* #include <iostream>
   using namespace std;
   int main(){
    float  a,b,c;
    cin>>a>>b>>c;
    float Av = (a+b+c)/3;
    cout <<"The average is " << Av<< endl;

    return 0;
   }*/

    //Task 10: Even or Odd Checker
   #include <iostream>
    using namespace std;
    int main(){
        int a;
        cin >> a;
        if(a/2==0){
            cout<<"even";
        }
        else{ 
            cout << "odd";
        }

        return 0; 
    }
        
