records = {
    "Math": 85,
    "Science": 90,
    "History": 75,
    "Duplicate_Math": 85,
}
print("Math score:", records.get("Math"))
records["English"] = 88
records["History"] = 80
records.pop("Duplicate_Math")
print("Total number of subjects:", len(records))
print("Final Subject Records:")
for subject, score in records.items():
    print(f"{subject}: {score}")
    
