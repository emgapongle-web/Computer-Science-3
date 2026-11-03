import time

class Patient:
    def __init__(self, name, bill_amount):
        self.name = name
        self._bill_amount = bill_amount
    def bill_amount(self):
        return self._bill_amount
    def calculate_bill(self):
        return self._bill_amount

class SeniorPatient(Patient):
    def __init__(self, name, bill_amount):
        super().__init__(name, bill_amount)
    def calculate_bill(self):
        bill_amount = (self._bill_amount - self._bill_amount * 0.20)
        return bill_amount
        
class PhilHealthPatient(Patient):
    def __init__(self, name, bill_amount):
        super().__init__(name, bill_amount)
    def calculate_bill(self):
        bill_amount = (self._bill_amount - self._bill_amount * 0.15)
        return bill_amount

patient1 = Patient("Auni", 10000)
patient2 = SeniorPatient("Liam", 11000)
patient3 = PhilHealthPatient("Sabine", 13000)

patients = [patient1, patient2, patient3]

print("Hospital Billing System:")
print("")
time.sleep(3)
for i in range(3):
    print(f"Patient Name: {patients[i].name}")
    time.sleep(1)
    print(f"Bill Amount: ₱{patients[i].bill_amount():.2f}")
    time.sleep(1)
    print(f"Final Bill: ₱{patients[i].calculate_bill():.2f}")
    time.sleep(1)
    print()
    time.sleep(2)