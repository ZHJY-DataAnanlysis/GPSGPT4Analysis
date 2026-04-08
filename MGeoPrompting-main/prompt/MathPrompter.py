MATH_PROMPT = '''
Q：Find the area of the trapezoid.
Mapping=(AC:6,AB:6,BC:6)
# Algabraic answer
Perimeter=AC+AB+BC
# python code
def solution(AC,AB,BC):
Return AC+AB+BC


Q：WX = ZY, and m \widehat ZW = 120. Find the measure of \\angle 2.
Mapping=(Shorter_base:6,Longer_base:16,Height:12)
# Algabraic answer
Answer=0.5 * (Shorter_base+Longer_ base) * Height
# python code
def solution(Shorter_base,Longer_ base,Height):
    return 0.5 * (Shorter_base+Longer_ base) * Height



How about this question?
Q: {question}


'''.strip() + '\n\n\n'