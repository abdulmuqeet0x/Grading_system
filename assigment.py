print("Welcome To My Grading System.\n")

name = input("Enter Your Name: ")
Roll_no = (input("Enter Your Roll no: "))

Percentage = float(input("Enter You'r Percentage: "))
print(f"\nHello! {name}\nRoll no: {Roll_no}")

if Percentage >= 90:
  print("Congrats! You got A1 Grade Keep it up")

elif Percentage >= 80 and Percentage < 90:
  print("Very good!, You got A Grade.")

elif Percentage >= 70 and Percentage < 80:
  print("Good work, You got B Grade but there's room for improvement")

elif Percentage >= 70 and Percentage < 80:
  print("You Got C Grade, try to study harder next time.")

elif Percentage >= 60 and Percentage < 70:
    print("You Got D Grade Work much harder! ")

elif Percentage >= 50 and Percentage < 60:
  print("You are just pass but you grade is not enough")

elif Percentage < 50:
  print("You are fail! work hard to geeting better garde next time")

else:
  print("Invalid input! Something Went Wrong please enter the valid input ")




