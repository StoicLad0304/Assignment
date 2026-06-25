Score = int(input("Enter your score: "))
if 100>= Score >= 90:
    Grade = "A"
elif 90 > Score >= 80:
    Grade = "B"
elif 80 > Score >= 70:
    Grade = "C"
elif 70 > Score >= 60:
    Grade = "D"
elif 60 > Score >= 0:
    Grade = "F"
else:
    print("Invalid score.")
print("Your grade is: ",Grade)