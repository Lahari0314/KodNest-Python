def build_patient_index(patients):
    patient_by_id = {}
    for patient in patients:
        id=patient["patient_id"]
        patient_by_id[id]=patient
    return patient_by_id

n = int(input())

patients = []

for i in range(n):
    patient_id, name, age, blood_group= input().split()
    patients.append({"patient_id": patient_id, "name": name, "age": int(age), "blood_group": blood_group })
required_id=input()
patient_by_id=build_patient_index(patients)
patient = patient_by_id.get(required_id)

if patient is None:
    print("Patient not found")

else:
    print (patient["name"]) 
    print(patient["age"]) 
    print(patient["blood_group"])