import datetime

doctors = {
    1: {"name": "Scott", "surname": "Ricart"},
    2: {"name": "John", "surname": "Johnson"},
}


class Person:
    def __init__(self, name, surname, birthdate, address, telephone, email):
        self.name = name
        self.surname = surname
        self.birthdate = birthdate
        self.address = address
        self.telephone = telephone
        self.email = email

    def age(self):
        today = datetime.date.today()
        age = today.year - self.birthdate.year

        if today < datetime.date(today.year, self.birthdate.month, self.birthdate.day):
            age -= 1

        return age

    def personal_info(self, x):
        if x == "name":
            print("My name is {} {}".format(self.name, self.surname))
        elif x == "birthdate":
            print("My birthdate is {}".format(self.birthdate))
        elif x == "address":
            print("My address is {}".format(self.address))
        elif x == "address":
            print("My phone number is {}".format(self.telephone))
        elif x == "email":
            print("My email is {}".format(self.email))


class Patient(Person):
    def __init__(self, name, surname, birthdate, address, telephone, email, symptoms, mouth_state, valid_doctor):
        super().__init__(name, surname, birthdate, address, telephone, email)
        self.symptoms = symptoms
        self.mouth_state = mouth_state
        self.valid_doctor = valid_doctor

    def validate_doctors_instructions(self, doctor_id, doctor_info, instruction):
        if doctors.get(doctor_id) is not None and doctors[doctor_id]["name"] == doctor_info["name"] and doctors[doctor_id]["surname"] == doctor_info["surname"]:
            self.valid_doctor = True
            print(
                f"{doctor_info['name']} {doctor_info['surname']} has been validated. He/She is your doctor")
        else:
            self.valid_doctor = False
            print(
                f"I am sorry you are not my doctor why are you asking me to {instruction}")

    def __mouth_handler__(self):
        if self.valid_doctor:
            self.mouth_state = True
            print(f"{self.name} opened his/her mouth")
        else:
            self.mouth_state = False
            print(f"Doctor couldn't not bevalidated")


class Employee(Person):
    def __init__(self, name, surname, birthdate, address, telephone, email, position, id, experience):
        super().__init__(name, surname, birthdate, address, telephone, email)
        self.position = position
        self.id = id
        self.experience = experience

    def introduce(self):
        print(
            f"Hi my name is {self.name} {self.surname} and I am {self.position}. I have {self.experience} years of experience. Thank you for visiting me today")

    def give_instructions(self, patient, instructions):
        print(f"{patient}, please tell me what are your symptoms and {instructions}")


person = Person(
    "Jane",
    "Doe",
    datetime.date(1992, 3, 12),  # year, month, day
    "No. 12 Short Street, Greenville",
    "555 456 0987",
    "jane.doe@example.com",
)

patient = Patient("Jane",
                  "Doe",
                  datetime.date(1992, 3, 12),  # year, month, day
                  "No. 12 Short Street, Greenville",
                  "555 456 0987",
                  "jane.doe@example.com", "Tummy Pain", False, False)

doctor = Employee("Scott", "Ricart", datetime.date(1992, 3, 12),  # year, month, day
                  "240 E 38th St, NY, NY, 10016",
                  "123456789",
                  "scott.ricart@example.com", "ENT doctor", 777, 28)

visiting_doctor = {"id": 1, "name": "Scott", "surname": "Ricart"}

doctor.introduce()
doctor.give_instructions(patient.name, "open your mouth")
patient.validate_doctors_instructions(1, visiting_doctor, "open mouth")
patient.__mouth_handler__()
