MATH_PROMPT = '''

Q：Find the area of the trapezoid.
A：The polygon shown in the image is a regular triangle, also known as an equilateral triangle, which means all three sides are equal in length. Since one of the sides, BC, is given as 6 inches, the other two sides (AB and AC) are also 6 inches each.To find the perimeter of the polygon, we sum the lengths of all sides:Perimeter = AB + BC + AC=6+6+6=18.The answer is 18.



Q:WX = ZY, and m \widehat ZW = 120. Find the measure of \\angle 2.
A:In this picture, the trapezoid has the longer base (base1) with a length of 16, and the shorter base (base2) with a length of 6 . The height, which is the perpendicular distance between the two bases, is given as 12 .To find the area of a trapezoid, you can use the formula:Area = 1/2 * (base1 + base2) * height = 1/2 * (16 + 6) * 12=132.The area of the trapezoid is 132.




How about this question?
Q: {question}

'''.strip() + '\n\n\n'