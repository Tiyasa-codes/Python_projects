to_marks=int(input("Enter total marks:"))
ob_marks=int(input("Enter your marks:"))
if(to_marks<ob_marks or to_marks<=0 or ob_marks<0):
   print("Invalid input")
else:
  per=(ob_marks*100)/to_marks
  if(per>=90 ):
    grade='A'
    print("Excellent")
  elif(per>=80):
    grade='B'
    print("Very good")
  elif(per>=70):
    grade='C'
    print("Good")
  elif(per>=60):
    grade='D'
    print("well")
  else:
    grade='F'
    print("study more")
  print(grade)

