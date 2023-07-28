class Client:
    date : int
    name: str
    depression_score: float
    anxiety_score: float
    stress_score: float

    def __init__(self, date: int, name: str, depression_score: float,
                  anxiety_score: float, stress_score: float):
        self.date = date
        self.name = name
        self.depression_score = depression_score 
        self.anxiety_score = anxiety_score
        self.stress_score = stress_score

  