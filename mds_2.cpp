
// оператыры арифметические : 

#include <iostream>
using namespace std;
int main(){
    int a, b ;
    cin >> a>>b; 
    int sum = a+b, subtr = a-b, mult = a*b, div = a/b;
    int mod = a%b, increment= ++a ,  decrement = --b;
    cout<< sum<<" " << subtr<<" " << mult<<" " << div <<endl ;
    cout << mod <<" " << increment<<" " << decrement;

    return 0;
}
    */
   // что бы сравнить 
    
   #include <iostream> 
   using namespace std;
   int main(){
    int a,b;
    cin >> a>>b;
    if(a>b){
        cout << a << " больше  б " ;
    }
    else if  (a<b){
        cout << b << " больше "<< a;
    }
    else{
       cout << " они равны ";
    }



    return 0;
   } */

// водиться возраст человека

#include <iostream>
using namespace std;
int main(){
    int a;
    cin >>a;
    if(a >= 18 && a<= 60) {
        cout<< " рабочий возраст";
    }
    else if(a>60){
        cout << " Пенсионер";
    }
    else{
        cout << "школьник ";
    
    }

    return 0;
}
    */

    // про стринг этот ккод 
#include <iostream>
using namespace std;

int main() {
    string s; cin >> s;             
    cout << s[0] << endl;           
    return 0;
}






// while , do 

#include <iostream>
using namespace std;
int main(){
    int a;
    cin>>a ;
    int i =1;
    do{
        cout<< a<<" * "<< i << " = "<< i*a<< endl;
        i++;
    }
    while(i<=10);

    return 0;
}
    */




// for loop про:

#include <iostream>
using namespace std;

int main() {
    int n;
    cin >> n;

    int sum = 0, num;
    for (int i = 0; i < n; i++) {
        cin >> num;
        sum += num;
    }

    cout << "sum " << sum << endl;

    return 0;
}
*/
// if else про

#include <iostream>
using namespace std;

int main() {
    int num;
    cin >> num;

    if (num == 1)
        cout << 0;
    else if (num % 2 == 1)
        cout << num;
    else
        cout << num / 2;

    return 0;
} 
    */

    
   //проо булин
   
   #include <iostream>
   using namespace std; 
   int main(){
    bool islighton;
    cout << " свет включен да-1 ; нет -0";
    cin >> islighton;
    if(islighton){
        cout<< "свет горит";
    } 
    else{
        cout<< " темнота "
    }

    return 0;
   }
    */
// про switch 

#include <iostream>
using namespace std;
int main (){
    int gpa ;
    cout<< "Enter your gpa(1-4)";
    cin>> gpa ;
    switch(gpa ){
        case 4 :
        cout<< " exellent ";
        break;
        case 3:
        cout << " good ";
        break;
        case 2:
        cout << " not good ";
        break ;
        default:
    
        cout<< " keep trying ";
    }

    return  0; 
}
*/
// про continue :  вводит even numbers 

#include <iostream>
using namespace std;
int main(){
    for(int i=1; i <=100; i++ ){
        if(i%2 != 0){
            continue;
        }
    cout << i<< "\n" ;   
    }
 

    return 0;
}
    */
// about break 

#include <iostream> 
using namespace std ;
int main(){
    for ( int i =1; i <= 200; i ++){
        if(i % 2==0&& i%3==0 ){
            break;
        }
        cout << i << endl ;


    }

    

    return 0; 
}
    */

    // про смаз 
   #include <iostream>
   #include <cmath> 
   using namespace std; 
   int main (){
    int a;
    cin >> a;
    cout << "Корень из x: "<< sqrt(a)<< endl;
    cout <<"x в  кубе:  "<< pow(a, 3)<<endl; 

    return 0;
   }
   // про пии 
#include <iostream>
#include <cmath>
using namespace std;

int main() {
    double radius = 5.0;
    double area = M_PI * pow(radius, 2);  // Площадь круга = π * r^2
    double length = 2 * M_PI * radius;    // Длина окружности = 2πr

    cout << "Радиус: " << radius << endl;
    cout << "Площадь круга: " << area << endl;
    cout << "Длина окружности: " << length << endl;

    return 0;
}






