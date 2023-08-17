from enum import Enum

class Escolaridade(Enum):
    FUNDAMENTAL_INCOMPLETO = "Ensino Fundamental incompleto"
    FUNDAMENTAL_COMPLETO = "Ensino Fundamental completo"
    MEDIO_INCOMPLETO = "Ensino Médio incompleto"
    MEDIO_COMPLETO = "Ensino Médio completo"
    SUPERIOR_INCOMPLETO = "Ensino Superior incompleto"
    SUPERIOR_COMPLETO = "Ensino Superior completo"

class Idade(Enum):
    ATE_18 = "até 18"
    ENTRE_19_30 = "19-30"
    ENTRE_31_40 = "31-40"
    ENTRE_41_50 = "41-50"
    ENTRE_51_60 = "51-60"
    ENTRE_61_70 = "61-70"
    ACIMA_70 = "+70"

class Client:

    def __init__(self, cpf: str, escolaridade: Escolaridade, idade: Idade, date: int, name: str, 
                 depression_score: float, anxiety_score: float, stress_score: float):
        self.cpf = cpf
        self.escolaridade = escolaridade
        self.idade = idade
        self.date = date
        self.name = name
        self.depression_score = depression_score 
        self.anxiety_score = anxiety_score
        self.stress_score = stress_score
    
    def __str__(self):
        return f"CPF: {self.cpf}\nEscolaridade: {self.escolaridade.value}\nIdade: {self.idade.value}\nDate: {self.date}\nName: {self.name}\nDepression Score: {self.depression_score}\nAnxiety Score: {self.anxiety_score}\nStress Score: {self.stress_score}"

# Exemplo de uso
cliente1 = Client(cpf="12345678900", escolaridade=Escolaridade.MEDIO_COMPLETO, idade=Idade.ENTRE_19_30,
                  date=20230728, name="João da Silva", depression_score=3.5, anxiety_score=2.7, stress_score=4.1)

# Imprime a representação personalizada
print(cliente1)
