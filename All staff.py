class AllStaff:
    def __init__(self, name, age, emp_id, birth_date, job_title):
        self.name = name
        self.age = age
        self.emp_id = emp_id
        self.birth_date = birth_date
        self.job_title = job_title

    def show(self):
        print(f"{self.emp_id} is {self.name} aged {self.age} being born "
              f"{self.birth_date} and employed as {self.job_title}")

class Management(AllStaff):
    def __init__(self, name, age, emp_id, birth_date, job_title, car):
        super().__init__(name, age, emp_id, birth_date, job_title)
        self.typing_speed = typing_speed

    def show(self):
        print(f"")

