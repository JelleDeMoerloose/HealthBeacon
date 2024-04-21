from logic.patients_db import Patients_db
from logic.nurse import Nurse


patients_db = Patients_db()
patients_db.initializer()

patient = patients_db.get_patient_by_id(1)



nurse = Nurse(1)
