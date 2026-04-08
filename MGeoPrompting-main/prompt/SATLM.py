MATH_PROMPT = '''

Q：Find the area of the trapezoid.
AC=6
AB=AC
BC=AC
Perimeter=Variable()
Perimeter=AC+AB+BC
result=Perimeter
slove(result)



Q：WX = ZY, and m \widehat ZW = 120. Find the measure of \\angle 2.
Shorter_base=6
Longer_ base=16
Height=12
Area=Variable()
Area=0.5 * (Shorter_base+Longer_ base) * Height
result=Area
slove(result)



How about this question?
Q: {question}

'''.strip() + '\n\n\n'