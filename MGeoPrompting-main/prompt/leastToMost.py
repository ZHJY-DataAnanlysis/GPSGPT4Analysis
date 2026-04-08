MATH_PROMPT = '''

Q：Find the area of the trapezoid.
A：Let’s break down this problem：1.What information can we obtain from the graph?2.How to use this information to calculate the measure of the perimeter of the regular polygon.
1.A regular triangle which one of the sides, AC, is given as 6 inches
2.Regular triangle, also known as an equilateral triangle, which means all three sides are equal in length. Since one of the sides, AC, is given as 6 inches, the other two sides are also 6 inches each.We sum the lengths of all sides:Perimeter = AC + AB + BC=6+6+6=18


Q：WX = ZY, and m \widehat ZW = 120. Find the measure of \\angle 2.
A：Let’s break down this problem：1.What information can we obtain from the graph？2.How to use this information to calculate the area of this trapezoid
1.length of the longer base of this trapezoid is 16, the length of the shorter base is 6, and the height between the longer and shorter base is 12.
2.According to the area formula of the trapezoid,the area of this trapezoid is 0.5 * (16+6) * 12=132


How about this question?
Q: {question}

'''.strip() + '\n\n\n'