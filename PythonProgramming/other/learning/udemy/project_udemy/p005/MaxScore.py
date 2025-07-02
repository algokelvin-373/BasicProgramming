score_students = [98, 65, 78, 90, 75, 60, 45, 78, 88, 89, 93, 99, 67, 74, 70, 63]

max_score = 0
for score in score_students:
    if score > max_score:
        max_score = score

print(max_score)