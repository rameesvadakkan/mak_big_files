student_scores = {
    "student1":{
        "Name":"Ramees",
        "Score": 95},
    "student2":{
        "Name":"Arun",
        "Score": 89},
    "student3":{
        "Name":"Favaz",
        "Score":80},
}

print(student_scores)
print(student_scores["student3"]["Score"])

for x , obj in student_scores.items():
    print(x)

    for y in obj :
      print(y + ':',obj[y])