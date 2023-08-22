from enum import Enum

class EDUCATION_LEVEL(Enum):
    FUNDAMENTAL_INCOMPLETO = "Ensino Fundamental incompleto"
    FUNDAMENTAL_COMPLETO = "Ensino Fundamental completo"
    MEDIO_INCOMPLETO = "Ensino Médio incompleto"
    MEDIO_COMPLETO = "Ensino Médio completo"
    SUPERIOR_INCOMPLETO = "Ensino Superior incompleto"
    SUPERIOR_COMPLETO = "Ensino Superior completo"

class AGE(Enum):
    ATE_18 = "até 18"
    ENTRE_19_30 = "19-30"
    ENTRE_31_40 = "31-40"   
    ENTRE_41_50 = "41-50"
    ENTRE_51_60 = "51-60"
    ENTRE_61_70 = "61-70"
    ACIMA_70 = "+70"

class SEX(Enum):
    MAN = "Homem"
    WOMAN = "Mulher"

class Client:

    def __init__(self, termos: bool, name: str, mail: str, age: AGE, education_level: EDUCATION_LEVEL, sex: SEX, date: int,
                 state: str, job: str, role: str, depression_score: float, anxiety_score: float, stress_score: float,
                 suggestion: str, mail_confirmation: str):
        self.termos = termos
        self.name = name
        self.mail = mail
        self.age = age
        self.education_level = education_level
        self.sex = sex
        self.date = date  #usar epoch 
        self.state = state
        self.job = job
        self.role = role
        self.depression_score = depression_score
        self.anxiety_score = anxiety_score
        self.stress_score = stress_score
        self.suggestion = suggestion
        self.mail_confirmation = mail_confirmation

    def __str__(self):
        return f"Client(name={self.name}, mail={self.mail}, age={self.age}, education_level={self.education_level}, " \
               f"sex={self.sex}, date={self.date}, state={self.state}, job={self.job}, role={self.role}, " \
               f"depression_score={self.depression_score}, anxiety_score={self.anxiety_score}, " \
               f"stress_score={self.stress_score}, suggestion={self.suggestion}, mail_confirmation={self.mail_confirmation})"

client1 = Client(name="John Doe", cpf="12345678900", age=AGE.ENTRE_19_30, education_level=EDUCATION_LEVEL.SUPERIOR_COMPLETO,
                 sex=SEX.MAN, date=1990, state="California", job="Software Engineer", role="Developer",
                 depression_score=3.5, anxiety_score=2.0, stress_score=4.2,
                 suggestion="Practice mindfulness daily.", mail="john@example.com")

client2 = Client(name="Jane Smith", cpf="98765432100", age=AGE.ENTRE_31_40, education_level=EDUCATION_LEVEL.MEDIO_COMPLETO,
                 sex=SEX.WOMAN, date=1985, state="New York", job="Marketing Manager", role="Manager",
                 depression_score=2.0, anxiety_score=3.8, stress_score=3.5,
                 suggestion="Try engaging in regular exercise.", mail="jane@example.com")

client3 = Client(name="Michael Johnson", cpf="45678912300", age=AGE.ENTRE_41_50, education_level=EDUCATION_LEVEL.SUPERIOR_INCOMPLETO,
                 sex=SEX.MAN, date=1972, state="Texas", job="Teacher", role="Educator",
                 depression_score=1.5, anxiety_score=1.2, stress_score=2.8,
                 suggestion="Explore a new hobby for relaxation.", mail="michael@example.com")

client4 = Client(name="Emily Brown", cpf="78912345600", age=AGE.ENTRE_19_30, education_level=EDUCATION_LEVEL.MEDIO_INCOMPLETO,
                 sex=SEX.WOMAN, date=1995, state="Florida", job="Student", role="College Student",
                 depression_score=4.0, anxiety_score=4.5, stress_score=3.7,
                 suggestion="Consider talking to a counselor.", mail="emily@example.com")

# Printing the objects
print(client1)
print(client2)
print(client3)
print(client4)