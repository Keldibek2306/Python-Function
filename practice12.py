def calculate_bmi(w, h):
    return w / (h * h)

def bmi_status(bmi):
    if bmi < 18.5:
        return "underweight"
    if bmi < 25:
        return "normal"
    if bmi < 30:
        return "overweight"
    return "obese"   