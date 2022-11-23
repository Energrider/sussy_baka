import json
with open("students.json") as jsonFile:
	data = json.load(jsonFile)
	jsonData = data["Students"]
	for i in data['Students']:
        print(f"{student['FirstName']} {student['Lastname']} ")
		