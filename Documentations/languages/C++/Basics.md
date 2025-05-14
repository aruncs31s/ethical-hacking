---
dg-publish: true
---
# Basics 1
**Before**:  [[Intermediate]]
- First program
- Printing 
- Variables 
- Operations 

Basics of all programming languages are almost the same , so if you have already know another programming language just skip this part.


There are few things to consider when first starting to code 
1. Compatible OS[^1] ,
	- **windows** should be fine but i highly recommend using **wsl** on windows. 
	- **Linux** i use linux , windows and macos , and i find linux is good for programming , but only when you do advanced stuffs. It easy to install linux in virtual machine or
		- Dual boot 
		- WSL 
		- Cloud  
2. Editor , i personally use **vim** , **neovim** , **vscode** for coding. But when im just learning something i always tends to use **neovim** because it is light weight and feels good to use. 
3. Compiler , **linux** comes pre installed with **[clang](https://clang.llvm.org/)** 
 [^1]: OS means operating system, which is the programs that allows you to interract with your computer 

## First Program 
When someone try to learn programming language the first thing they write is a **Hello World** program -> more about it [here](https://press.rebus.community/programmingfundamentals/chapter/hello-world/#:~:text=A%20%E2%80%9CHello%2C%20world!%E2%80%9D,very%20first%20program%20people%20write.) 


```cpp
#include <iostream>  
using namespace std;  
  
int main() {  
  cout << "Hello World!";  
  return 0;  
}
```
```
Hello World!
```

![[Screenshot 2025-05-13 at 6.54.34 AM.png]]
![[Screenshot 2025-05-13 at 6.54.27 AM.png]]
![[Screenshot 2025-05-13 at 6.54.46 AM.png]]
*I have used [Vim](https://www.vim.org/) as the text editor , which is the default editor for linux and [g++](https://www.geeksforgeeks.org/compiling-with-g-plus-plus/) for compiling*

## Printing

```cpp
#include <iostream>  
using namespace std;  
  
int main() {  
  cout << "Hello World!";  
  return 0;  
}
```

### Escape characters 
Complete list of escape characters can be found [here](https://www.geeksforgeeks.org/cpp-escape-sequences/)
#### New Line 
```cpp
#include <iostream>  
using namespace std;  
  
int main() {  
  cout << "Hello \n World!";  
  return 0;  
}
```

```
Hello 
World!
```

![[Screenshot 2025-05-13 at 12.25.29 PM.png]]

## Variable
#syntax
```
type variableName = value;
```

```cpp
int a = 10;
double b = 10.10;
char letter = 'A';
const char* some_string = "Hello World";
std::string some_another_string = "Hello, world";
bool something = false; 
```


![[Screenshot 2025-05-13 at 12.28.23 PM.png]]


>[!Note] `string`
>When using `std::string`  the **string** lib should be included. 
>```cpp
>#include \<string>
>```


```cpp
// valid 
int a =10 , b=20 , c 30 ;
// invalid
int a,b,c = 10,20,30 ;
// valid 
int a = 10; 
// valid 
int a ;
a = 10 ; 
```

### Constants 
```cpp 
const int number = 10 ;
// Error 
number = 20;
```

- the value of the constant can't be changed after the first assingment , and it is initialized the moment it is created. 


![[Screenshot 2025-05-13 at 12.30.20 PM.png]]

## Operations

lets `a=10` , `b=5`
```cpp
// Addition
c = a + b ; // c = 15 
// increment 
c = c+1 ; // c = 16 

++c; // c = c + 1 ; but beforez excecution c = 17
c++; // c = c + 1 ; but after excecution  c = 17
--c; // c = c - 1 ; but beforez excecution c = 16 
c--; // c = c - 1 ; but after excecution c = 16 
// substract
c = a - b ; // c = 5 

// Multiplication
c = a * b; // c = 50 
// Division 
c = a/b; // c = 2 

// Mod 

c = a % b ; // c = 0 
```

![[Screenshot 2025-05-13 at 12.38.56 PM.png]]
>[!Note] `print_c`
> `print_c()` is a **function** which *prints out* the value of `c` and you will learn about **functions** in [[Intermediate]] section 




| Operator | Operation        |
| -------- | ---------------- |
| **+**    | addition         |
| **-**    | substraction     |
| **/**    | division         |
| *****    | multiplication   |
| **%**    | modulus operator |


### Assignment operators 
```cpp
int a = 10 ; // Assigns the value 10 to variable a 
```


### Binary Operations

```c
int a = 10 ; // 1010 
int b = 5 ; // 0111
// bitwise or
c = a | b ; // c = 1010 or 0111 = 1111 -> 15 

// bitwise xor
c = a ^ b; // c = 1010 or 0111 = 1101 -> 13 

// bitwise not
c = ~a; // c =  not 1010 -> 0101 -> 5

// bitwise and 
c = a & b ; // c = 1010 & 0111 = 0010 -> 2 

// bitwise left shift 
c = a << 2; // c = 1010 << 2 = 0b101000 -> 40  

// bitwise right shift 
c = a >> 2 ; // c = 1010 >> 2 = 0b0010 -> 2 
```


![[Screenshot 2025-05-13 at 12.59.08 PM.png]]
![[Screenshot 2025-05-13 at 12.59.16 PM.png]]
- Here the value of the `~a` will not be 5 , instead it will have a value `1111 0101` but is is maked here to avoid confusion .

| Operator | Operation    |
| -------- | ------------ |
| **\|**   | or           |
| **^**    | xor          |
| **~**    | not          |
| **&**    | and          |
| **<<**   | left shift   |
| **>>**   | right shift  |

### Comparison operator 



```cpp
int a = 10 ;
int b = 20;

// Equal to ;
a == b; // false 
a == 10 ; // true 

// Not equal to 
a != b; // true
a != 10; // false

// Greater than 
a > b ; // false
// Greater than or equal to 
a >= 10 ; // true 

// Less than 
a < b; // true 
a <= 10; // true
```

*comparison operators are normally used to check some conditions*

![[Screenshot 2025-05-13 at 1.08.36 PM.png]]
We can see that sometimes it runs the code inside `if{code}` and sometimes the code runs `else{code}` which is the primary use of **comparison operator** , that is run `if else` is used to 

| Operator | Name                     |
| -------- | ------------------------ |
| **==**   | Equal to                 |
| **!=**   | Not equal                |
| **>**    | Greater than             |
| **<**    | Less than                |
| **>=**   | Greater than or equal to |
| **<=**   | Less than or equal to    |

### Logical Operators

```cpp
int a = 10 , b = 20 , c = 30 ;

// logical and 
a > b && a < c ; // false && true -> false
a < b && a < c ; // true && true -> true 

// logical or 
a > b || a < c ; // false | true -> true 

// logical not

!(a > b) ; // !false -> true 
!(a < b) ; // !true -> false 
```
![[Screenshot 2025-05-13 at 1.12.28 PM.png]]

| Operator | Name        |
| -------- | ----------- |
| &&       | Logical and |
| \|\|     | Logical or  |
| !        | Logical not |

### Comma Operator


![[Screenshot 2025-05-13 at 4.58.46 PM.png]]