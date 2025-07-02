# Project Day 2 - BMI Calculator

print("BMI Calculator")
m = input("Input m (kg): ")
h = input("Input h (cm): ")

h_float = float(h)
m_float = float(m)

h_m = h_float / 100
bmi = m_float / (h_m ** 2)

print("BMI: ", bmi)
if bmi < 18.5:
    print("underweight")
elif 18.5 <= bmi < 25:
    print("normal weight")
elif bmi >= 25:
    print("overweight")