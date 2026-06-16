# C++ 完整基础语法大全（超详细、纯罗列，直接背就能用）
## 一、基础结构
### 1. 最简程序框架
```cpp
#include <iostream>   // 输入输出头文件
using namespace std; // 标准命名空间

int main()
{
    // 代码写这里
    
    return 0; // 程序结束
}
```

## 二、数据类型
### 1. 基本整型
- `int` 整型
- `short` 短整型
- `long` 长整型
- `long long` 长长整型
- `unsigned int` 无符号整型

### 2. 浮点型
- `float` 单精度
- `double` 双精度

### 3. 字符与布尔
- `char` 字符
- `bool` 布尔（true / false）
- `string` 字符串（需 `#include <string>`）

## 三、变量与常量
### 1. 变量定义
```cpp
int a;
int b = 10;
double pi = 3.14;
char ch = 'A';
string s = "hello";
```

### 2. 常量
```cpp
const int MAX = 100;   // 只读常量
#define N 50            // 宏常量
```

## 四、运算符
### 1. 算术运算符
`+` `-` `*` `/` `%` `++` `--`

### 2. 赋值运算符
`=` `+=` `-=` `*=` `/=` `%=`

### 3. 关系运算符
`>` `<` `>=` `<=` `==` `!=`

### 4. 逻辑运算符
`&&` 与、`||` 或、`!` 非

### 5. 三目运算符
```cpp
int max = a > b ? a : b;
```

## 五、输入输出
```cpp
cout << "输出内容" << endl;
cin >> 变量;
```
示例：
```cpp
int a;
cin >> a;
cout << "a = " << a << endl;
```

## 六、流程控制
### 1. if 分支
```cpp
if(条件)
{

}
else if(条件)
{

}
else
{

}
```

### 2. switch 分支
```cpp
switch(变量)
{
    case 1:
        break;
    case 2:
        break;
    default:
        break;
}
```

### 3. for 循环
```cpp
for(初始化; 条件; 递增)
{

}
```

### 4. while 循环
```cpp
while(条件)
{

}
```

### 5. do-while 循环
```cpp
do
{

}while(条件);
```

### 6. 跳转语句
- `break` 跳出循环/switch
- `continue` 跳过本次循环
- `return` 函数返回

## 七、数组
### 1. 一维数组
```cpp
int arr[5];
int arr2[3] = {1,2,3};
```

### 2. 二维数组
```cpp
int arr[2][3] = {{1,2,3},{4,5,6}};
```

## 八、函数
### 1. 函数定义格式
```cpp
返回值类型 函数名(参数列表)
{
    函数体
    return 值;
}
```

### 2. 示例
```cpp
int add(int x, int y)
{
    return x + y;
}
```

### 3. 函数声明
```cpp
int add(int x, int y);
```

### 4. 无参无返回值
```cpp
void show()
{

}
```

## 九、指针
### 1. 基础指针
```cpp
int a = 10;
int *p = &a;   // p 存a的地址
*p = 20;       // 通过指针改a的值
```

### 2. 指针与数组
```cpp
int arr[3] = {1,2,3};
int *p = arr;
```

## 十、引用
```cpp
int a = 10;
int &b = a;  // b是a的别名
```

## 十一、结构体
```cpp
struct Student
{
    int id;
    string name;
};

Student s;
s.id = 101;
```

## 十二、字符串 string
需头文件：`#include <string>`
```cpp
string s1 = "abc";
string s2 = "def";
string s3 = s1 + s2;   // 拼接
s1.size();             // 长度
```

## 十三、命名空间
```cpp
namespace MySpace
{
    int a = 100;
}
// 使用
MySpace::a;
```

## 十四、面向对象基础（类）
```cpp
class Person
{
private:
    int age;    // 私有成员
public:
    void setAge(int a)
    {
        age = a;
    }
    int getAge()
    {
        return age;
    }
};

// 创建对象
Person p;
p.setAge(18);
```

## 十五、常用头文件
```cpp
#include <iostream>   // 输入输出
#include <string>     // 字符串
#include <cstdlib>    // 随机数
#include <ctime>      // 时间种子
#include <algorithm>  // 排序等算法
```

我可以给你整理一份**可直接复制默写的精简版**，不带多余解释，只留纯语法模板，要吗？