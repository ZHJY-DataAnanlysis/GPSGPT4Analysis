Geometry_Prompt = '''
Q：Find the area of the trapezoid.

# solution in Python:

def solution():
    """Find the perimeter of the regular polygon."""
    AC=6
    AB=AC
    BC=AC
    Perimeter=AC+AB+BC
    result=Perimeter
    return result




Q：WX = ZY, and m \widehat ZW = 120. Find the measure of \\angle 2.

# solution in Python:

def solution():
    """Find the area of the trapezoid."""
    base1 = 16
    base2 = 6
    height = 12
    area = 0.5 * (base1+base2) * height
    result = area
    return result



Q: {question}


# solution in Python:


'''.strip() + '\n\n\n'