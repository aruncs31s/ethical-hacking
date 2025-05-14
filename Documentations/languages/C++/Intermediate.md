---
dg-publish: true
---
# Intermediate
In this section you will learn about 
1. Functions
2. Scope 
3. Precedence
4. OOP
5. Classes 
6. Objects 

 >[!important]
 >You should know [[Basics|this]] before doing this. 



## 1. Functions 
###  Declerations or function prototyping 
```cpp
type functionName(argument list);
```
type is essentially means the **return type** of the function. 
#examples 
```cpp
int sum(int a , int b);
int sum(int,int);
```


### Return type 
Consider this following program 
```cpp
#include <iostream>
int sum(int number_1,int number_2){
    return number_1 + number_2; 
}
int main(){
    int a = 10 , b = 5 ;
    int c = sum(a,b);
    std::cout << "a + b = " <<  c << std::endl;
}
```

```output
a + b = 15
```
There is a function named `sum` which has a **return type** of `int` , the return type is chose according to what type of data we are expecting from the function. For simplicity  lets consider the following program which is similar to the above program 
```cpp
#include <iostream>
int sum(int number_1,int number_2){
    return number_1 + number_2; 
}
int main(){
    int a = 10.1, b = 5.4 ;
    int c = sum(a,b);
    std::cout << "a + b = " <<  c << std::endl;
}
```
the main change is that `a` is now 10.1 and `b` is now 5.4 
**output**
```output 
a + b = 15
```
But we can not see any difference in the **output** it is still $15$ also we get warnings like `implicit conversion from double to int` 

![[Screenshot 2025-05-13 at 6.54.57 PM.png]]
ie 
- 10.1(double) is converted to 10(integer)
- 5.4(double) is converted to 5(integer)

```cpp
#include <iostream>
float sum(float number_1,float number_2){
    return number_1 + number_2; 
}
int main(){
    float a = 10.1, b = 5.4 ;
    float c = sum(a,b);
    std::cout << "a + b = " <<  c << std::endl;
}
```

```output
a + b = 15.5
```

**Can we achieve this using only int?** YES

```cpp
#include <iostream>
typedef struct result{
    int integer_part;
    int decimal_part;
}result;
result sum(int number_1, int number_2,int number_3, int number_4){
    result r;
    r.integer_part = number_1 + number_2;
    r.decimal_part = number_3 + number_4;
    return r;
}
int main(){
    int a = 10, b = 5 , c = 1, d = 4; // 0.1 -> 1 , .4 -> 4 
    result res = sum(a, b, c, d);
    std::cout << "a + b = " << res.integer_part + (res.decimal_part/10.0) << std::endl;
    return 0;
}
```
```output
a + b = 15.5
```
we can see that there are already extra complexity , and if the number is `0.01` instead of `0.1` this program will fail. but we can overcome that using a while or for loop by simply checking the length of the **integer**


>[!Summary] choosing datatypes
>Data type is must be chose carefully , most of the round off errors will happen due to incorrect datatypes and data types can also influence the performance of the program 


### Scope of a variable
*Scope of a variable the region of code within which a variable is accessible*[^1]. 
- the scope of a variable is constrained inside `{}`  
[^1]: https://docs.julialang.org/en/v1/manual/variables-and-scoping
```cpp
#include <iostream>
int a = 10;
void funtion(){
    std::cout << "from function a = " << a << std::endl;
}
int main(){
    std::cout << "global a = " << a << std::endl;
    
    int a = 5;
    funtion();
    std::cout << "local a = " << a << std::endl;

    std::cout << "global a = " << ::a << std::endl;
}
```

```output
global a = 10
from function a = 10
local a = 5
global a = 10
```
## Precedence


## Control Statements 
- if-else
- while 
- do-while
- for
- switch

### if-else
#syntax
```cpp
if (expression)
	statement
```
```cpp
if (expression)
	statement
else
	statement
```

```cpp
if (expression)
	statement
else if (expression)
	statement 
else
	statement 
```
- we can also chain if-else 
```cpp
if (expression)
	if(expression)
		if(expression)
			statement
```
which is similar to 
```cpp
if(expression && expression && expression)
	statement
```

#examples 
```cpp
#include <iostream>
int main(){
int a = 10 ;
if (a == 10 ){
	std::cout << "HI" << std::endl;
	}
}
```
```output
HI
```
```cpp
```cpp
#include <iostream>
int main(){
int a = 10 ;
if (a == 9 ){
	std::cout << "HI" << std::endl;
	}
}
```
```output

```

>[!note] true and flase 
>a value other than 1 is consderd as true , so the following programs all will output the same result 
>
>```cpp
> #include <iostream>
> int main(){
> int a = 10 ;
> if (a - 5 ){ // true
> 	std::cout << "HI" << std::endl;
> 	}
> }
> ```
> ```cpp
> #include <iostream>
> int main(){
> int a = 10 ;
> if (a - 100){ // true 
>  	std::cout << "HI" << std::endl;
> 	}
> }
> ```


### While

```cpp
while(expression)
	statement
```