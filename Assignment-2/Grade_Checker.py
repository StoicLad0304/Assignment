Score = int(input("Enter your score: "))
if 100>= Score >= 90:
    print("Your grade is A")
elif 90 > Score >= 80:
    print("Your grade is B")
elif 80 > Score >= 70:
    print("Your grade is C")
elif 70 > Score >= 60:
    print("Your grade is D")
elif 60 > Score >= 0:
    print("Your grade is F")
print("Your score is: ", Score)