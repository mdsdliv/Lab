
// Task 1: Sum of Elements in a One-Dimensional Array

#include <iostream>
using namespace std;
int main(){
    int n;
    cin>>n;
    int arr[n], sum =0;
    for(int i=0; i<n; i++){
        cin >> arr[i];
        sum+=arr[i];
    }
    cout<<sum ;
    return 0;
}


// Task 2: Find Minimum and Maximum in an Array

#include <iostream>
using namespace std ;
int main(){
    int n;
    cin>> n;
    int arr[n];
    for(int i =0; i<n; i++){
        cin>>arr[i];
    }
    int max_value = arr[0];
    int min_value = arr[0];

    for(int i =1;i<n;i++){
        if(arr[i] > max_value ){
            max_value= arr[i];
        }
        if(arr[i] < min_value ){
            min_value = arr[i];
        }

    }
    cout<< " Min_vaalue : " << min_value<<endl;
    cout << "Max_value: " << max_value;
    return 0;
}
    

//  Task 3: Count Even and Odd Numbers

#include <iostream>
using namespace std;
int main(){
    int n ;
    cin>> n;
    int arr[n];
    for(int i=0; i < n; i++){
        cin >> arr[i];
    }
    int even_sum = 0, odd_sum =0;

    for(int i =0; i<n; i++){
        if(arr[i]%2 == 0){
        even_sum++;
        }
        else{
            odd_sum++;
        }
    cout<< " even_sum: " << even_sum<<endl;
    cout << "odd_sum: " << odd_sum;
        
    }
    return 0;
}
    
//Task 4: Reverse Array
// Сначала используя вектор и алгоритм  

#include <iostream>
#include <algorithm>
#include <vector>
using namespace std;
int main(){
    int n;
    cin>>n;
    vector<int> v(n);
    for(int i =0; i<n; i++){
        cin>> v[i];
    }
    reverse(v.begin(), v.end());
    for(int i=0; i<n; i++){
        cout<< v[i]<< endl;
    }  

    return 0;
}
    
// теперь используя только самго массива :

#include <iostream>
#include <algorithm> // для reverse 
using namespace std;
int main(){
    int n;
    cin>>n;
    int arr[n];
    for(int i =0;i<n;i++){
        cin>>arr[i];
    } 
    reverse(arr,arr+n); // в массиве используеться просто арр для того что бы указать вес диапазон 
    for(int i=0; i<n;i++){
        cout<< arr[i]<<"  ";
    }


    return 0;
}
    

// Task 5: Linear Search in Array 

#include <iostream>
using namespace std;
int main(){
    int n;
    cin>> n;
    int arr[n];
    for(int i = 0;i<n;i++){
        cin>> arr[i];
    }
    int f;
    cin>> f;
    for(int i = 0; i<n; i++){
        if(arr[i] == f){
            cout<<i;
            return 0;
        }


    }
    cout<< "Ничего не найдено !";
    return 0;
}
    


// Task 6: Matrix Addition

#include <iostream>
using namespace std;
int main(){
    int matrisya1[3][3], sum[3][3];
    for(int i=0;i<3;i++){
        for(int j =0;j<3;j++){
            cin>>matrisya1[i][j];
        }
    }
    int matrisya2[3][3];
    for(int i=0;i<3;i++){
        for(int j=0;j<3;j++){
            cin>>matrisya2[i][j];
        }
    }
    for(int i=0;i<3;i++){
        for(int j=0;j<3;j++){
            sum[i][j]=matrisya1[i][j]+matrisya2[i][j];

        }
    }
    for(int i=0;i<3;i++){
        for(int j =0;j<3;j++){
            cout<< sum[i][j]<< "  ";
            
        }
        cout << endl;
    }
    


    return 0;
}
    


// когда сайзы разные:

#include <iostream>
using namespace std;
int main(){
    int a[2][3], b[4][3], c[2][3];
    for(int i =0; i<2 ; i++){
        for(int j=0; j<3; j++){
            cin >> a[i][j];
        }
    }
    for(int i=0;i<4;i++){
        for(int j=0; j<3;j++){
            cin>> b[i][j];
        }
    }
    for(int i =0;i<2;i++){
        for(int j=0; j<3;j++){
            c[i][j]=a[i][j]+b[i][j];
        }
    }
    for(int i = 0; i< 2; i++){
        for(int j =0;j< 3; j++){
            cout << c[i][j]<<" ";
        }
        cout<< endl;
    }

    return 0;
}
    

// Task 7: Matrix Transpose

#include <iostream>
using namespace std;
int main(){
    int size1,size2;
    cin>>size1>>size2;

   
    int A[size1][size2], C[size2][size1];
    for(int i =0;i<size1; i++){
        for(int j =0; j<size2;j++){
            cin>>A[i][j];
        }
    }
  
    for(int i=0;i<size1; i++){
        for(int j=0;j<size2;j++){
            
            C[j][i]=A[i][j] ;
            
        }
        
    }
    for(int i=0; i < size2;i++){
        for(int j =0; j<size1; j++){
            cout<<C[i][j]<<"  ";
        }
        cout<<endl;
    }
    return 0;

}
    
    // Task 8: Find Row with Maximum Sum
    
#include <iostream>
using namespace std;
int main(){
    int R[4][4];
    for(int i=0; i<4;i++){
        for(int j =0;j<4;j++){
            cin>>R[i][j];
        }
    }
     int maxSum = 0;
    int maxRow = 1;

    for (int i = 0; i < 4; i++) {
        int rowSum = 0;
        for (int j = 0; j < 4; j++) {
            rowSum += R[i][j];
        }

        if (rowSum > maxSum) {
            maxSum = rowSum;
            maxRow = i;
        }
    }
    cout << "Row " << maxRow << " has the maximum sum: " << maxSum << endl;

    return 0;
}
    

// Task 9: Diagonal Elements of a Matrix
#include <iostream>
using namespace std;
int main(){
    int mat[4][4];
    for(int i=0;i<4;i++){
        for(int j =0; j<4; j++){
            cin>> mat[i][j];
        }
    }
    cout<<"Main : ";
    for(int i=0;i<4;i++){
            cout << mat[i][i]<<" ";    
    }
    cout<<endl;
    cout<<"Secondary : " ;
    for(int i=0;i<4;i++){
            cout << mat[i][4-1-i]<<" ";
        
    }

    return 0;
}

// Task 10: Sort an Array

#include <iostream>
#include <algorithm>
using namespace std;
int main(){
    int n;
    cin>>n;
    int arr[n];
    for(int i=0;i<n;i++){
        cin>>arr[i];
    }
    sort(arr,arr+n);
    for(int i=0;i<n;i++){
        cout<<arr[i]<<"  ";
    }

    return 0;
}
    

