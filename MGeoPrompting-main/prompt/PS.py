MATH_PROMPT = '''

Q：Find the area of the trapezoid.
A:
Given:
A regular triangle which one of the sides, AC, is given as 6 inches
Calculation:
Regular triangle, also known as an equilateral triangle, which means all three sides are equal in length. Since one of the sides, AC, is given as 6 inches, the other two sides are also 6 inches each.We sum the lengths of all sides:Perimeter = AC + AB + BC=6+6+6=18
Answer:
The perimeter of the triangle is 18




Q：WX = ZY, and m \widehat ZW = 120. Find the measure of \\angle 2.
A:
Given:
A trapezoidal with a longer base length of 16, a shorter base length of 6, and a height of 12
Plan:
We need to calculate the area of this trapezoid
Calculation:
the area formula of the trapezoid is 0.5 * (longer base+shorter base) * height
the area of the trapezoid is 0.5 * (16+6) * 12=132
Answer:
the area of the trapezoid is 132



How about this question?
Q: {question}

'''.strip() + '\n\n\n'