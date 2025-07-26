#variables

student_id= 102
student_name= "Chintu"
student_age= 40
quiz_score= 80
assignment_score= 85
exam_score= 90
student_attendance=65

#total score
total_score = quiz_score + assignment_score + exam_score

#average score
average_score = total_score / 3 #static
#average_score =total_score / len(total_score) #dynamic

#student passed
student_passed = average_score >= 75

#attendance simulation
student_passed +=1

#award eligibility
award_eligibility = student_passed and student_attendance >= 90

print(f"Student Name: {student_name}")
print(f"Total score: {total_score}")
print(f"Average score: {average_score}")
print(f"Student passed: {student_passed}")
print(f"Student Current Attendance: {student_attendance}")
print(f"student Awarded: {award_eligibility}")



