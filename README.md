# Scientific Computating with Python FreeCodeCamp course

These are five small projects to test my Python skills

# Time Calculator

Write a function named add_time that takes in two required parameters and one optional parameter:

a start time in the 12-hour clock format (ending in AM or PM)
a duration time that indicates the number of hours and minutes
(optional) a starting day of the week, case insensitive
The function should add the duration time to the start time and return the result.

If the result will be the next day, it should show (next day) after the time. If the result will be more than one day later, it should show (n days later) after the time, where "n" is the number of days later.

If the function is given the optional starting day of the week parameter, then the output should display the day of the week of the result. The day of the week in the output should appear after the time and before the number of days later.

Below are some examples of different cases the function should handle. Pay close attention to the spacing and punctuation of the results.

```python
add_time("3:00 PM", "3:10")
```

Returns: 

```python
6:10 PM
```

```python
add_time("11:30 AM", "2:32", "Monday")
```
Returns: 

```python
2:02 PM, Monday
```

```python
add_time("11:43 AM", "00:20")
```
Returns: 
```python
12:03 PM
```

```python
add_time("10:10 PM", "3:30")
```

Returns: 

```python
1:40 AM (next day)
```

```python
add_time("11:43 PM", "24:20", "tueSday")
```

Returns:

```python
12:03 AM, Thursday (2 days later)
```

```python
add_time("6:30 PM", "205:12")
```

Returns:

```python
7:42 AM (9 days later)
```


# Arithmetic Calculator

Create a function that receives a list of strings that are arithmetic problems and
returns the problems arranged vertically and side-by-side. 

The function should optionally take a second argument. When the second argument is set to True, 
the answers should be displayed.

Example

```python
1.) arithmetic_arranger(["32 + 698", "3801 - 2", "45 + 43", "123 + 49"])
```

Outputs

```python
   32      3801      45      123
+ 698    -    2    + 43    +  49
-----    ------    ----    -----
```

```python
2.) arithmetic_arranger(["32 + 8", "1 - 3801", "9999 + 9999", "523 - 49"], True)
```
Outputs

```python
  32         1      9999      523
+  8    - 3801    + 9999    -  49
----    ------    ------    -----
  40     -3800     19998      474
```

## Rules

The function will return the correct conversion if the supplied problems are properly formatted, otherwise, it will return a string that describes an error that is meaningful to the user.

### Situations that will return an error:

- If there are too many problems supplied to the function. The limit is five, anything more will return: Error: Too many problems.

- The appropriate operators the function will accept are addition and subtraction. Multiplication and division will return an error. Other operators not mentioned in this bullet point will not need to be tested. The error returned will be: Error: Operator must be '+' or '-'.

- Each number (operand) should only contain digits. Otherwise, the function will return: Error: Numbers must only contain digits.

- Each operand (aka number on each side of the operator) has a max of four digits in width. Otherwise, the error string returned will be: Error: Numbers cannot be more than four digits.

### **If the user supplied the correct format of problems, the conversion you return will follow these rules:**

- There should be a single space between the operator and the longest of the two operands, the operator will be on the same line as the second operand, both operands will be in the same order as provided (the first will be the top one and the second will be the bottom).

- Numbers should be right-aligned.

- There should be four spaces between each problem.

- There should be dashes at the bottom of each problem. The dashes should run along the entire length of each problem individually. (The example above shows what this should look like.)


# Polygon Area Calculator

In this project you will use object oriented programming to create a Rectangle class and a Square class. The Square class should be a subclass of Rectangle and inherit methods and attributes.

#### Rectangle class
When a Rectangle object is created, it should be initialized with width and height attributes. The class should also contain the following methods:

set_width
set_height
get_area: Returns area (width * height)
get_perimeter: Returns perimeter (2 * width + 2 * height)
get_diagonal: Returns diagonal ((width ** 2 + height ** 2) ** .5)
get_picture: Returns a string that represents the shape using lines of "*". The number of lines should be equal to the height and the number of "*" in each line should be equal to the width. There should be a new line (\n) at the end of each line. If the width or height is larger than 50, this should return the string: "Too big for picture.".
get_amount_inside: Takes another shape (square or rectangle) as an argument. Returns the number of times the passed in shape could fit inside the shape (with no rotations). For instance, a rectangle with a width of 4 and a height of 8 could fit in two squares with sides of 4.
Additionally, if an instance of a Rectangle is represented as a string, it should look like: Rectangle(width=5, height=10)

#### Square class
The Square class should be a subclass of Rectangle. When a Square object is created, a single side length is passed in. The __init__ method should store the side length in both the width and height attributes from the Rectangle class.

The Square class should be able to access the Rectangle class methods but should also contain a set_side method. If an instance of a Square is represented as a string, it should look like: Square(side=9)

Additionally, the set_width and set_height methods on the Square class should set both the width and height.

#### Usage example

```python
rect = shape_calculator.Rectangle(10, 5)
print(rect.get_area())
rect.set_height(3)
print(rect.get_perimeter())
print(rect)
print(rect.get_picture())

sq = shape_calculator.Square(9)
print(sq.get_area())
sq.set_side(4)
print(sq.get_diagonal())
print(sq)
print(sq.get_picture())

rect.set_height(8)
rect.set_width(16)
print(rect.get_amount_inside(sq))
```

That code should return:

```python
50
26
Rectangle(width=10, height=3)
**********
**********
**********

81
5.656854249492381
Square(side=4)
****
****
****
****

8
```