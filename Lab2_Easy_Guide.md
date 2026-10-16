# Lab 2 – Easy Guide
**Data Types, Variables, Operators, I/O and Type Casting (C++)**

Structure: **Part A** – topics with solved examples (explain + trace) → **Part B** – in-class activity (students do in lab) → **Part C** – home task → **Part D** – solutions (teacher only).

Tip for teaching: for every example, write the code on the board, ask "what will it print?", then run it.

---

# PART A – Topics with Solved Examples

## 1. Output – `cout`

**Idea:** `cout` shows things on the screen. `<<` means "send to screen". `endl` = new line.

```cpp
#include <iostream>
using namespace std;

int main()
{
    int age = 20;

    cout << "Name: Ali" << endl;
    cout << "Age: " << age << endl;
    cout << "Age after 5 years: " << age + 5 << endl;
    return 0;
}
```

**How it works, line by line**
| Line | What happens |
|---|---|
| `#include <iostream>` | Brings in the tools for input/output |
| `int age = 20;` | Makes a box named `age` and puts 20 inside |
| `cout << "Age: " << age` | Prints the text, then the value inside the box |
| `age + 5` | C++ calculates 20 + 5 = 25 first, then prints |

**Output**
```
Name: Ali
Age: 20
Age after 5 years: 25
```
Note: text in `" "` is printed exactly as written. A variable name without quotes prints its value.

---

## 2. Input – `cin`

**Idea:** `cin` takes a value from the keyboard. `>>` means "put into the variable".

```cpp
int number;
cout << "Enter a number: ";
cin >> number;
cout << "You entered: " << number << endl;
```

**Trace (user types 7):**
1. Program prints `Enter a number: `
2. Program waits. User types `7` and presses Enter.
3. `7` goes into the box `number`.
4. Prints `You entered: 7`

**Two values at once:**
```cpp
int length, width;
cout << "Enter length and width: ";
cin >> length >> width;
cout << "Area = " << length * width << endl;
```
User types `5 3` → `length = 5`, `width = 3` → prints `Area = 15`.

---

## 3. Variables

**Idea:** A variable is a **named box in memory**. Its value can change.

```cpp
int age;          // 1. declare (empty box)
age = 25;         // 2. assign a value
int marks = 80;   // 3. declare + assign together
int x = 1, y = 2, z = 3;   // 4. several at once
```

**Trace of changing value:**
```cpp
int score = 10;
cout << score << endl;   // 10
score = 50;              // old value 10 is replaced
cout << score << endl;   // 50
```

**Naming rules** (give students this quick test)
| Name | Valid? | Why |
|---|---|---|
| `totalMarks` | ✅ | letters only |
| `_count` | ✅ | can start with `_` |
| `student1` | ✅ | digit allowed, but not first |
| `2ndValue` | ❌ | starts with digit |
| `total marks` | ❌ | has a space |
| `float` | ❌ | keyword |
| `net-salary` | ❌ | hyphen not allowed |

`marks` and `Marks` are **different** variables (case sensitive).

---

## 4. Data Types

**Idea:** The type tells C++ *what kind* of value the box holds and *how big* the box is.

| Type | Holds | Example |
|---|---|---|
| `int` | whole number | `int age = 21;` |
| `float` | decimal (small) | `float height = 5.9f;` |
| `double` | decimal (bigger, more accurate) | `double distance = 12345.678;` |
| `char` | one character, single quotes | `char grade = 'A';` |
| `bool` | true / false | `bool passed = true;` |
| `string` | text, double quotes (needs `<string>`) | `string name = "Ali";` |

**Complete example**
```cpp
#include <iostream>
#include <string>
using namespace std;

int main()
{
    string name = "Ali";
    int age = 21;
    double gpa = 3.75;
    char grade = 'A';
    bool passed = true;

    cout << name << " is " << age << " years old." << endl;
    cout << "GPA: " << gpa << ", Grade: " << grade << endl;
    cout << "Passed (1=yes, 0=no): " << passed << endl;
    return 0;
}
```
**Output**
```
Ali is 21 years old.
GPA: 3.75, Grade: A
Passed (1=yes, 0=no): 1
```
Why `1`? `cout` prints `true` as 1 and `false` as 0.

**`sizeof` – how many bytes?**
```cpp
cout << sizeof(int) << endl;     // 4
cout << sizeof(double) << endl;  // 8
cout << sizeof(char) << endl;    // 1
```

---

## 5. Constants

**Idea:** A box that is **locked** after the first value. Use `const`.

```cpp
const double PI = 3.14159;
double radius = 2.5;

cout << "Area = " << PI * radius * radius << endl;
// PI = 3.14;   ← ERROR! cannot change a constant
```
**Trace:** 3.14159 × 2.5 × 2.5 = **19.6349**. Constant names are written in CAPITALS by convention.

---

## 6. Arithmetic Operators `+ - * / %`

```cpp
int a = 10, b = 3;
cout << a + b << endl;   // 13
cout << a - b << endl;   // 7
cout << a * b << endl;   // 30
cout << a / b << endl;   // 3   (not 3.33!)
cout << a % b << endl;   // 1
```

**Why is `10 / 3` = 3?** Both are `int`, so the answer is `int` — the decimal part is thrown away.
**What is `%`?** The **remainder**. 10 ÷ 3 = 3 remainder **1**.

**Get the decimal answer:**
```cpp
cout << 10.0 / 3 << endl;   // 3.33333  (one side is decimal)
```

**Real-life use of `%`:** even/odd check → `num % 2` gives 0 for even, 1 for odd.

---

## 7. Assignment Operators `= += -= *= /= %=`

**Idea:** shortcuts. `x += 5` means `x = x + 5`.

```cpp
int total = 100;
total += 50;   // 100 + 50 = 150
total -= 30;   // 150 - 30 = 120
total /= 4;    // 120 / 4  = 30
cout << total; // 30
```
**Trace table**
| Statement | total becomes |
|---|---|
| `int total = 100;` | 100 |
| `total += 50;` | 150 |
| `total -= 30;` | 120 |
| `total /= 4;` | 30 |

---

## 8. Increment / Decrement `++` `--`

**Idea:** `++` adds 1, `--` subtracts 1.
- **Prefix** `++a` → change **first**, then use.
- **Postfix** `a++` → use **first**, then change.

```cpp
int a = 5;
cout << ++a << endl;   // 6   (a becomes 6, then prints 6)
cout << a++ << endl;   // 6   (prints 6, then a becomes 7)
cout << a   << endl;   // 7
cout << a-- << endl;   // 7   (prints 7, then a becomes 6)
cout << --a << endl;   // 5   (a becomes 5, then prints 5)
```

**Trace table**
| Statement | Printed | `a` after |
|---|---|---|
| start | – | 5 |
| `++a` | 6 | 6 |
| `a++` | 6 | 7 |
| `a` | 7 | 7 |
| `a--` | 7 | 6 |
| `--a` | 5 | 5 |

Easy memory trick: **sign before = act before; sign after = act after.**

---

## 9. Relational Operators `== != > < >= <=`

**Idea:** compare two values. Answer is `1` (true) or `0` (false).

```cpp
int x = 5, y = 3;
cout << (x > y)  << endl;   // 1  (5 is greater than 3)
cout << (x == y) << endl;   // 0  (5 is not equal to 3)
cout << (x != y) << endl;   // 1
cout << (x <= 3) << endl;   // 0
```
⚠️ **Common mistake:** `=` stores a value, `==` compares. `x = y` is NOT a comparison.

---

## 10. Logical Operators `&&  ||  !`

| Operator | Meaning | Easy words |
|---|---|---|
| `&&` | AND | both must be true |
| `\|\|` | OR | at least one true |
| `!` | NOT | flips the answer |

```cpp
int marks = 75, attendance = 80;

cout << (marks >= 50 && attendance >= 75) << endl;  // 1
cout << (marks >= 90 || attendance >= 75) << endl;  // 1
cout << !(marks >= 50) << endl;                     // 0
```
**Trace**
1. `marks >= 50` → true, `attendance >= 75` → true → true AND true = **1**
2. `marks >= 90` → false, `attendance >= 75` → true → false OR true = **1**
3. `marks >= 50` → true, NOT true = **0**

---

## 11. Ternary Operator `? :`

**Idea:** a one-line if-else.
`variable = (condition) ? value_if_true : value_if_false;`

```cpp
int a = 2, b = 7;
int max = (a > b) ? a : b;
cout << max;    // 7
```
**Trace:** Is `2 > 7`? No (false) → take the part after `:` → `b` → **7**.

**Pass / Fail example**
```cpp
int marks = 62;
string result = (marks >= 50) ? "Pass" : "Fail";
cout << result;   // Pass
```

**Nested (3 outcomes)**
```cpp
int num = -4;
cout << ((num > 0) ? "Positive" : (num < 0) ? "Negative" : "Zero");
// Negative
```
Trace: `-4 > 0`? No → check `-4 < 0`? Yes → "Negative".

---

## 12. Type Casting

### Implicit (automatic)
C++ converts smaller → bigger by itself.
```cpp
int count = 9;
double value = count;       // 9 becomes 9.0 automatically
cout << value + 0.5;        // 9.5
```

### Explicit (you force it)
**Problem:**
```cpp
int total = 7, count = 2;
cout << total / count;      // 3  ← wrong if we want decimal
```
**Fix with casting:**
```cpp
cout << (float)total / count << endl;               // 3.5
cout << static_cast<double>(total) / count << endl; // 3.5
```
**Why it works:** `total` is turned into 7.0 first, so it is now decimal ÷ int → decimal answer.

**Decimal → int (decimal lost):**
```cpp
float price = 99.99f;
int whole = (int)price;
cout << whole;              // 99 (not rounded, just cut)
```

### Character ↔ ASCII
Every character has a number: `A`=65, `B`=66, `a`=97.
```cpp
char ch = 'A';
cout << (int)ch << endl;        // 65
cout << (char)66 << endl;       // B
cout << (char)(ch + 1) << endl; // B   (65 + 1 = 66 → 'B')
```

---

## 13. Operator Precedence

**Idea:** like BODMAS. Order: **( )** → **unary (`++ -- !`)** → **`* / %`** → **`+ -`** → **relational** → **`==  !=`** → **`&&`** → **`||`** → **assignment**.

```cpp
int r = 10 + 4 * 3 / 2 - 1;
```
| Step | Work | Result |
|---|---|---|
| 1 | `4 * 3` | 12 |
| 2 | `12 / 2` (same level, left to right) | 6 |
| 3 | `10 + 6` | 16 |
| 4 | `16 - 1` | **15** |

With brackets:
```cpp
int s = (10 + 4) * 3;   // 14 * 3 = 42
```

---

## 14. Everything Together – Student Marks Calculator

```cpp
#include <iostream>
#include <string>
using namespace std;

int main()
{
    const int TOTAL_MARKS = 300;
    string name;
    int pf, calculus, ict;

    cout << "Enter student name: ";
    cin >> name;
    cout << "Enter marks of PF, Calculus and ICT: ";
    cin >> pf >> calculus >> ict;

    int total = pf + calculus + ict;
    double average = static_cast<double>(total) / 3;
    double percentage = static_cast<double>(total) / TOTAL_MARKS * 100;

    cout << "Name: " << name << endl;
    cout << "Total Marks = " << total << endl;
    cout << "Average Marks = " << average << endl;
    cout << "Percentage = " << percentage << "%" << endl;
    return 0;
}
```
**Trace (Ali, 78 84 91):**
- total = 78 + 84 + 91 = **253**
- average = 253.0 / 3 = **84.3333**
- percentage = 253.0 / 300 × 100 = **84.3333 %**

**Why `static_cast<double>(total)`?** Without it, `253 / 3` would be integer division = 84 (decimal lost).

---

# PART B – In-Class Activity (students perform in lab)

Rule: first **predict the output on paper**, then type and run to check.

### Activity 1 – Predict the output (5 min)
```cpp
int a = 4, b = 9;
cout << a + b * 2 << endl;
cout << (a + b) * 2 << endl;
cout << b / a << endl;
cout << b % a << endl;
cout << (double)b / a << endl;
```
*(Answers: 22, 26, 2, 1, 2.25)*

### Activity 2 – Pre/Post increment trace (5 min)
```cpp
int n = 10;
cout << n++ << endl;
cout << ++n << endl;
cout << n-- << endl;
cout << n << endl;
```
Students fill the trace table. *(Answers: 10, 12, 12, 11)*

### Activity 3 – Rectangle (10 min)
Take length and width from the user. Print the **area** and **perimeter**.
Hint: area = l × w, perimeter = 2 × (l + w).

### Activity 4 – Celsius to Fahrenheit (10 min)
Take temperature in Celsius (as `double`) and show Fahrenheit.
Hint: `F = C * 9 / 5 + 32`. Test with 37 → 98.6.

### Activity 5 – Even or Odd (ternary) (10 min)
Take an integer and print `Even` or `Odd` using `%` and the ternary operator.

### Activity 6 – Character magic (10 min)
Take one character from the user. Print its ASCII code and the **next** character.
Test with `a` → 97 and `b`.

### Activity 7 – Debug hunt (5 min)
Find and fix the 4 errors:
```cpp
#include <iostream>
using namespace std;
int main()
{
    int 2ndNumber = 5;
    float total marks = 40;
    const int LIMIT = 10;
    LIMIT = 20;
    cout << "Value: " << 2ndNumber
    return 0;
}
```
*(Errors: name starts with digit, space in name, changing a const, missing `;`)*

---

# PART C – Home Task

Complete these 7 tasks (same as the lab manual). Take screenshots of code and output.

1. **Calculator:** Take two integers, show sum, difference, product, quotient and remainder.
2. **Percentage:** A student got 425 out of 500. Calculate the percentage using explicit casting. Expected: **85%**.
3. **Currency converter:** Convert Rs. 12,500 to USD, EUR, GBP, AED, SAR (rates: 280, 330, 380, 76, 75). Store the rate in a `double`; show original amount, rate and converted amount.
4. **Parking counter:** Start with 20 spaces. One vehicle enters (decrease) and one leaves (increase). Use `++` / `--` and show the difference between prefix and postfix.
5. **Binary operators:** Take two integers; show arithmetic, relational and logical results with clear labels.
6. **Pass/Fail:** Take marks; print `Pass` if ≥ 50, else `Fail`, using the **ternary operator**.
7. **Mini application – Semester Fee Slip:** Take name, registration number and credit hours. Keep fee per credit hour as a constant, add a fixed service charge, and print a fee slip (credit hours, fee per credit hour, tuition fee, additional charges, total payable).
8. **Conclusion:** Write 4–5 lines on what you learned.

Hints: Task 2 → cast before dividing. Task 3 → use `12500.0 / rate`. Task 4 → show `cout << spaces--` vs `cout << --spaces`. Task 7 → `tuition = creditHours * FEE_PER_CREDIT`.

---

# PART D – Solutions (Teacher Key)

### Activity 3 – Rectangle
```cpp
#include <iostream>
using namespace std;
int main()
{
    int l, w;
    cout << "Enter length and width: ";
    cin >> l >> w;
    cout << "Area = " << l * w << endl;
    cout << "Perimeter = " << 2 * (l + w) << endl;
    return 0;
}
```

### Activity 4 – Celsius to Fahrenheit
```cpp
#include <iostream>
using namespace std;
int main()
{
    double c;
    cout << "Enter temperature in Celsius: ";
    cin >> c;
    double f = c * 9 / 5 + 32;
    cout << "Fahrenheit = " << f << endl;
    return 0;
}
```

### Activity 5 – Even / Odd
```cpp
#include <iostream>
using namespace std;
int main()
{
    int n;
    cout << "Enter a number: ";
    cin >> n;
    cout << ((n % 2 == 0) ? "Even" : "Odd") << endl;
    return 0;
}
```

### Activity 6 – Character magic
```cpp
#include <iostream>
using namespace std;
int main()
{
    char ch;
    cout << "Enter a character: ";
    cin >> ch;
    cout << "ASCII code = " << (int)ch << endl;
    cout << "Next character = " << (char)(ch + 1) << endl;
    return 0;
}
```

### Task 1
```cpp
#include <iostream>
using namespace std;
int main()
{
    int a, b;
    cout << "Enter two integers: ";
    cin >> a >> b;
    cout << "Sum = " << a + b << endl;
    cout << "Difference = " << a - b << endl;
    cout << "Product = " << a * b << endl;
    cout << "Quotient = " << a / b << endl;
    cout << "Remainder = " << a % b << endl;
    return 0;
}
```
(Warn students: entering 0 as the second number crashes the program – conditions come in a later lab.)

### Task 2
```cpp
#include <iostream>
using namespace std;
int main()
{
    int obtained = 425, total = 500;
    double percentage = static_cast<double>(obtained) / total * 100;
    cout << "Percentage = " << percentage << "%" << endl;   // 85%
    return 0;
}
```

### Task 3 (shown for USD and EUR; repeat the same pattern for GBP, AED, SAR)
```cpp
#include <iostream>
using namespace std;
int main()
{
    const double AMOUNT = 12500;

    double usdRate = 280;
    cout << "Original: Rs. " << AMOUNT << "  Rate: " << usdRate
         << "  USD = " << AMOUNT / usdRate << endl;

    double eurRate = 330;
    cout << "Original: Rs. " << AMOUNT << "  Rate: " << eurRate
         << "  EUR = " << AMOUNT / eurRate << endl;

    // GBP 380, AED 76, SAR 75 – same pattern
    return 0;
}
```
Expected: USD 44.6429, EUR 37.8788, GBP 32.8947, AED 164.474, SAR 166.667.

### Task 4 – Parking counter
```cpp
#include <iostream>
using namespace std;
int main()
{
    int spaces = 20;
    cout << "Available spaces: " << spaces << endl;       // 20

    cout << "Vehicle enters (postfix): " << spaces-- << endl;  // prints 20, then 19
    cout << "Now available: " << spaces << endl;                // 19

    cout << "Vehicle enters (prefix): " << --spaces << endl;   // 18
    cout << "Vehicle leaves (prefix): " << ++spaces << endl;   // 19
    cout << "Vehicle leaves (postfix): " << spaces++ << endl;  // prints 19, then 20
    cout << "Final available: " << spaces << endl;              // 20
    return 0;
}
```
Key point to explain: postfix prints the **old** value, prefix prints the **new** value.

### Task 5 – Binary operators
```cpp
#include <iostream>
using namespace std;
int main()
{
    int a, b;
    cout << "Enter two integers: ";
    cin >> a >> b;

    cout << "a + b = " << a + b << endl;
    cout << "a - b = " << a - b << endl;
    cout << "a * b = " << a * b << endl;
    cout << "a / b = " << a / b << endl;
    cout << "a % b = " << a % b << endl;

    cout << "a > b  : " << (a > b) << endl;
    cout << "a < b  : " << (a < b) << endl;
    cout << "a == b : " << (a == b) << endl;
    cout << "a != b : " << (a != b) << endl;

    cout << "a > 0 && b > 0 : " << (a > 0 && b > 0) << endl;
    cout << "a > 0 || b > 0 : " << (a > 0 || b > 0) << endl;
    cout << "!(a > b)       : " << !(a > b) << endl;
    return 0;
}
```

### Task 6 – Pass / Fail
```cpp
#include <iostream>
using namespace std;
int main()
{
    int marks;
    cout << "Enter obtained marks: ";
    cin >> marks;
    cout << ((marks >= 50) ? "Pass" : "Fail") << endl;
    return 0;
}
```

### Task 7 – Semester Fee Calculator
```cpp
#include <iostream>
#include <string>
using namespace std;
int main()
{
    const int FEE_PER_CREDIT = 8000;
    const int SERVICE_CHARGE = 5000;

    string name, regNo;
    int creditHours;

    cout << "Enter student name: ";
    cin >> name;
    cout << "Enter registration number: ";
    cin >> regNo;
    cout << "Enter credit hours: ";
    cin >> creditHours;

    int tuition = creditHours * FEE_PER_CREDIT;
    int total = tuition + SERVICE_CHARGE;

    cout << "\n===== SEMESTER FEE SLIP =====" << endl;
    cout << "Name              : " << name << endl;
    cout << "Registration No   : " << regNo << endl;
    cout << "Credit Hours      : " << creditHours << endl;
    cout << "Fee per Credit    : Rs. " << FEE_PER_CREDIT << endl;
    cout << "Tuition Fee       : Rs. " << tuition << endl;
    cout << "Additional Charges: Rs. " << SERVICE_CHARGE << endl;
    cout << "Total Payable     : Rs. " << total << endl;
    return 0;
}
```
Sample: 15 credit hours → tuition 120000, total 125000.

### Sample conclusion
> In this lab I learned how to use `cout` and `cin`, declare variables and constants, choose data types, and use arithmetic, assignment, increment, relational, logical and ternary operators. I also learned operator precedence and how type casting prevents wrong results in integer division.
