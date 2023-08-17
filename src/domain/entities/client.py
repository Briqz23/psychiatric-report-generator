from domain.enums.escolaridade_enum import Escolaridade
from domain.enums.idade_enum import Idade
from domain.enums.sexualidade_enum import Sexualidade


class Client:

    def __init__(self, cpf: str, escolaridade: Escolaridade, idade: Idade, sexualidade: Sexualidade, date: int, name: str, 
                 depression_score: float, anxiety_score: float, stress_score: float):
        self.cpf = cpf
        self.escolaridade = escolaridade
        self.idade = idade
        self.sexualidade = sexualidade
        self.date = date
        self.name = name
        self.depression_score = depression_score 
        self.anxiety_score = anxiety_score
        self.stress_score = stress_score
    
    def __str__(self):
        return f"CPF: {self.cpf}\nEscolaridade: {self.escolaridade.value}\nIdade: {self.idade.value}\nSexualidade: {self.sexualidade.value}\nDate: {self.date}\nName: {self.name}\nDepression Score: {self.depression_score}\nAnxiety Score: {self.anxiety_score}\nStress Score: {self.stress_score}"

# Exemplo de uso
cliente1 = Client(cpf="12345678900", escolaridade=Escolaridade.MEDIO_COMPLETO, idade=Idade.ENTRE_19_30,
                  sexualidade=Sexualidade.CISGENERO, date=20230728, name="João da Silva", depression_score=3.5, anxiety_score=2.7, stress_score=4.1)

# Imprime a representação personalizada
print(cliente1)
