class Employee:
    def __init__(self, name, role, **kwargs):
        self.name = name
        self.role = role

    def display(self):
        print(f"Employee: {self.name}, Role: {self.role}")


class Trainer(Employee):
    def __init__(self, specialization, **kwargs):
        super().__init__(**kwargs)
        self.specialization = specialization

    def display(self):
        print(f"Trainer: {self.name}, Role: {self.role}, Specialization: {self.specialization}")


class YogaInstructor(Employee):
    def __init__(self, yoga_style, **kwargs):
        super().__init__(**kwargs)
        self.yoga_style = yoga_style

    def display(self):
        print(f"Yoga Instructor: {self.name}, Role: {self.role}, Yoga Style: {self.yoga_style}")


class MultiTrainer(Trainer, YogaInstructor):
    def __init__(self, name, role, specialization, yoga_style):
        super().__init__(name=name, role=role, specialization=specialization, yoga_style=yoga_style)

    def display(self):
        print(f"Multi-Trainer: {self.name}, Role: {self.role}, "
              f"Specialization: {self.specialization}, Yoga Style: {self.yoga_style}")


# Objects
emp = Employee(name="Sam", role="Manager")
trn = Trainer(name="Joshua", role="Trainer", specialization="Strength Training")
yoga = YogaInstructor(name="Hiba", role="Yoga Instructor", yoga_style="Hatha Yoga")
multi = MultiTrainer(name="Shibin", role="Multi Trainer", specialization="Cardio", yoga_style="Ashtanga Yoga")

# Display
emp.display()
trn.display()
yoga.display()
multi.display()
