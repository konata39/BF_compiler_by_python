# BF compiler by python
## source 
https://zh.wikipedia.org/wiki/Brainfuck<br>
## Note
The code is available only for Windoes and Linux<br>
This compiler accept command line (//) and space inside the code.
Otherwise, it will show the error.
## Usage
save BF code as "code.txt" and execute main.py to compile<br>
## Example
Code Example 1:
 ```
++++++++++[>+++++++>++++++++++>+++>+<<<<-]
>++.>+.+++++++..+++.>++.<<+++++++++++++++.
>.+++.------.--------.>+.>.
 ```  
 result:
 ```
H
e
l
l
o

W
o
r
l
d
!
```
 Code Example 2:
 ```
++++++++++[>+++++++>+++    +++++++>+++>+<<<<-] //The space and command line will not affect the code
>++.>+.+++++++..+++.>++.<<+++++++++++++++.
>.+++.------.--------.>+.>.
 ```
result:
 ```
H
e
l
l
o

W
o
r
l
d
!
```
Code Example 3:

```
++++++++++[>+++++++>+++a+++++++>+++>+<<<<-]
>++.>+.+++++++..+++.>++.<<+++++++++++++++.
>.+++.------.--------.>+.>.
 ```  
 result:
  ```
Error!! unknown char at line 1, col 24 : a
```
