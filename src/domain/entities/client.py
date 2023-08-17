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

class GENDER(Enum):
    CISGENERO = "Cisgênero"
    TRANSGENERO = "Transgênero"
    NAO_BINARIO = "Não Binário"

class Client:

    def __init__(self, cpf: str, education_level: EDUCATION_LEVEL, age: AGE, gender: GENDER, date: int, name: str, 
                 depression_score: float, anxiety_score: float, stress_score: float, suggestion: str):
        self.cpf = cpf
        self.education_level = education_level
        self.age = age
        self.gender = gender
        self.date = date
        self.name = name
        self.depression_score = depression_score 
        self.anxiety_score = anxiety_score
        self.stress_score = stress_score
        self.suggestion = suggestion
    
    def __str__(self):
        return f"CPF: {self.cpf}\nEducation level: {self.education_level.value}\nAge: {self.age.value}\nGender: {self.gender.value}\nDate: {self.date}\nName: {self.name}\nDepression Score: {self.depression_score}\nAnxiety Score: {self.anxiety_score}\nStress Score: {self.stress_score}\nSuggestion: {self.suggestion}"

cliente1 = Client(cpf="12345678900", education_level=EDUCATION_LEVEL.MEDIO_COMPLETO, age=AGE.ENTRE_19_30,
                  gender=GENDER.CISGENERO, date=20230728, name="João da Silva", depression_score=3.5, anxiety_score=2.7, stress_score=4.1,
                  suggestion="Consider taking breaks and practicing mindfulness.")

print(cliente1)
