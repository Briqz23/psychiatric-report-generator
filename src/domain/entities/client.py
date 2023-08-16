class Client:
    date : int
    name: str
    idade: int
    esclaridade: str
    depression_score: float
    anxiety_score: float
    stress_score: float

    def __init__(self, date: int, name: str, idade:int, escolaridade:str, depression_score: float,
                  anxiety_score: float, stress_score: float):
        self.date = date
        self.name = name
        self.idade = idade
        self.escolaridade = escolaridade
        self.depression_score = depression_score 
        self.anxiety_score = anxiety_score
        self.stress_score = stress_score
    
cliente1 = Client(date=20230728, name="João da Silva", depression_score=3.5, anxiety_score=2.7, stress_score=4.1)
