#Student grade book
student_score={
    "Zayn":495,
    "John":486,
    "Jagan":400,
    "Nithin":389,
    "Tara":440   
}
total_score=0
for score in student_score.values():
    total_score += score
avg_score=total_score/len(student_score)
print("The class average is : ",avg_score)

top_score=max(student_score)
bottom_score=min(student_score)
print("The top scorer is:",top_score)
print("The bottom scorer is:",bottom_score)

name=input("Enter student name to look up:")
score = student_score.get(name,"student not found")
print("Result:",score)



