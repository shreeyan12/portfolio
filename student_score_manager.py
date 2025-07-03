students = []
scores = []

for i in range(3):
    name = input("Enter student name: ")
    score = int(input("Enter their score: "))
    students.append(name)
    scores.append(score)

for i in range(3):
    print(students[i], "scored", scores[i])

print("Average score:", sum(scores) / len(scores))
