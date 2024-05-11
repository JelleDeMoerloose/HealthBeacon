from logic.context import Patients_db

patients_db = Patients_db()
patients_db.initializer()


patients = patients_db.get_patients()

for patient in patients:

    print(patient)
