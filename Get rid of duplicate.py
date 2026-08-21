student_data ={
    "id1":{"name":"Sara","class":"X","subject_integraion":"math,english,science"},
    "id2":{"name":"John","class":"X","subject_integraion":"math,english,science"},
    "id3":{"name":"Mike","class":"X","subject_integraion":"math,english,science"},
    "id4":{"name":"Sara","class":"X","subject_integraion":"math,english,science"},

}
result = {}
seen_keys = []
for student_id , details in student_data.items():
    unique_keys = (details["name"], details["class"], details["subject_integraion"])
    if unique_keys not in seen_keys:
        seen_keys.append(unique_keys)
        result[student_id] = details

for k,v in result.items():
    print(k,":",v)    
