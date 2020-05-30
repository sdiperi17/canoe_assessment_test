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


class Mouth():
    def __init__(self, name, surname, doctor_id=None, doctor_info=None, instruction=None, mouth_open=False, valid_doctor=False):  # instantiating the base
        self.name = name
        self.surname = surname
        self.mouth_open = mouth_open
        self.valid_doctor = valid_doctor
        # self.doctor_id = doctor_id
        # self.doctor_info = doctor_info
        # self.instruction = instruction

    def __mouth_handler__(self, instruction):
        if self.valid_doctor:
            if instruction == 'open':
                self.mouth_open = True
            else:
                self.mouth_open = False
            print(f"{self.name} {instruction}ed his/her mouth")
        else:
            print(f"Doctor couldn't not be validated. Unknown doctor")

    def validate_doctor(self, doctor_id, doctor_info, instruction):
        print(f"Please wait. {self.name} is validating your information")
        if doctors.get(doctor_id) is not None and doctors[doctor_id]["name"] == doctor_info["name"] and doctors[doctor_id]["surname"] == doctor_info["surname"]:
            self.valid_doctor = True
            print(
                f"{doctor_info['name']} {doctor_info['surname']} has been validated. He/She is your doctor")
            self.__mouth_handler__(instruction)
        else:
            self.valid_doctor = False
            print(
                f"I am sorry you are not my doctor why are you asking me to {instruction} my mouth")


class Employee(Person):
    def __init__(self, name, surname, birthdate, address, telephone, email, position, id, experience):
        super().__init__(name, surname, birthdate, address, telephone, email)
        self.position = position
        self.id = id
        self.experience = experience

    def introduce(self):
        print(
            f"Hi my name is {self.name} {self.surname} and I am {self.position}. I have {self.experience} years of experience. Thank you for visiting me today")

    def give_instructions(self, patient, instruction):
        print(
            f"{patient}, please tell me what are your symptoms and {instruction} your mouth")
        return instruction


class Patient(Person):

    def __init__(self, name, surname, birthdate, address, telephone, email, symptoms):
        super().__init__(name, surname, birthdate, address, telephone, email)
        self.symptoms = symptoms
        self.mouth = Mouth(name, surname, None, None, None,
                           mouth_open=False, valid_doctor=False)

    def __follow_instructions__(self, doctor_info, instruction):
        return self.mouth.validate_doctor(doctor_info["id"], doctor_info, instruction)


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
                  "jane.doe@example.com", "Tummy Pain")

doctor = Employee("Scott", "Ricart", datetime.date(1992, 3, 12),  # year, month, day
                  "240 E 38th St, NY, NY, 10016",
                  "123456789",
                  "scott.ricart@example.com", "ENT doctor", 1, 28)

test_visiting_doctor = {"id": 1, "name": "Scott", "surname": "Ricart"}

doctor.introduce()
patient.__follow_instructions__(
    test_visiting_doctor, doctor.give_instructions(patient.name, "open"))
print("Patient's mouth state:", patient.mouth.mouth_open)
