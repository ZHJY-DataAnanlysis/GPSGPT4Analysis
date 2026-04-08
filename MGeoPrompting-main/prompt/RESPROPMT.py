MATH_PROMPT = '''
Question:Find the area of the trapezoid.
Answer:The polygon shown in the image is a regular triangle, also known as an equilateral triangle, which means all three sides are equal in length. Since one of the sides, AC, is given as 6 inches, the other two sides (AB and BC) are also 6 inches each.To find the perimeter of the polygon, we sum the lengths of all sides:Perimeter = AC(the first side) + AB(the second side) + BC(the third side)=6+6+6=18

Question:WX = ZY, and m \widehat ZW = 120. Find the measure of \\angle 2.
Answer:According to the picture, the length of the longer base of this trapezoid is 16, the length of the shorter base is 6, and the height between the longer and shorter base is 12. According to the area formula of the trapezoid, the area of the trapezoid is equal to 0.5 * (longer base+shorter base) * height. So the area of this trapezoid is 0.5 * (16(longer_base)+6(shorter_base)) * 12(height)=132


How about this question?
Q: {question}

'''.strip() + '\n\n\n'