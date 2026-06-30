#age calc

# def calculateAge (bd,bm,by,cd,cm,cy):
#     years=0
#     for y in range(by,cy):
#         years+=1
#     if (cm,cd)<(bm,bd):
#         years-=1

#     return years

# bd, bm, by = map(int, input("Enter birth day, month, year (separated by spaces): ").split())
# cd,cm,cy = map(int, input("Enter birth day, month, year (separated by spaces): ").split())

# age = calculateAge(bd,bm,by,cd,cm,cy)

# print(f"Age: {age} years old")


#bmi calc
def check_bmi(w,h):
    bmi=w/((h/100)**2)
    if bmi < 18.5:
        category = "Underweight"
    elif bmi < 25:
        category = "Normal"
    elif bmi < 30:
        category = "Overweight"
    else:
        category = "Obese"
    return bmi,category

w = float(input("Enter weight: "))
h = float(input("Enter height: "))

bmi_value, bmi_category = check_bmi(w, h)
print("BMI:", bmi_value)
print("Category:", bmi_category)