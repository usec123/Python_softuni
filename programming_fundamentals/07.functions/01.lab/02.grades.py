def grade_calc(grade:float)->str:
    if grade<3: return 'Fail'
    elif grade<3.5: return 'Poor'
    elif grade<4.5: return 'Good'
    elif grade<5.5: return 'Very Good'
    return 'Excellent'

print(grade_calc(float(input())))