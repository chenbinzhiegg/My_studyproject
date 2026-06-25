# include <iostream>
int main()
{
    using namespace std;
    const int ArSize = 20;
    char name[ArSize];
    char dessert[ArSize];

    cout << "Enter you name :\n";
    cin.get(name,ArSize);
    cin.get();  //吃掉换行符
    cout << "Enter your favorite dessert \n";
    cin.get(dessert,ArSize).get();
    cout << "I have some delicous " <<dessert;
    cout << " for you ," << name << ".\n";
    return 0;

}